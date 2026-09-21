# /// script
# requires-python = ">=3.10"
# dependencies = ["pypdf>=4.0"]
# ///
"""
The deterministic half of /read: a PDF's table of contents, and one markdown file per chapter.

It reads the outline — the bookmarks — a PDF carries, turns it into page ranges, and writes the
text of the chapters asked for into an extracts folder, a marker before every page. It has no
opinion about what matters: choosing chapters is the owner's, with this outline in front of them,
and the note is the researcher's. Extracts are a cache — regenerable, gitignored, never cited.

    uv run extract.py BOOK.pdf --outline                the outline and the page count; nothing written
    uv run extract.py BOOK.pdf --chapters 3,4,7         those chapters, by their number in the outline
    uv run extract.py BOOK.pdf --all                    every chapter; with no outline, the whole PDF as one file
    uv run extract.py BOOK.pdf --split "Introduction=1-12; Chapter 1=13-40"
                                                        no outline: chapters by page range, titles yours

Options
    --out DIR       where extracts go (default ./Extracts); this PDF's land in DIR/<pdf stem>/
    --depth N       the outline depth that counts as a chapter (default 1; use 2 when depth 1 is parts)
    --engine E      auto | pdftotext | pypdf (default auto: pdftotext when on PATH, else pypdf).
                    pdftotext reflows a page's lines into paragraphs; pypdf keeps the line breaks,
                    which tables and verse prefer
    --min-chars N   fewer characters per page than this, on average, means no text layer (default 40)

Exit codes: 0 done · 1 usage · 2 no text layer, nothing written · 3 no outline for --chapters
Without uv: pip install pypdf, then python extract.py ...
"""
import argparse
import dataclasses
import importlib.metadata
import json
import pathlib
import re
import shutil
import subprocess
import sys
import unicodedata

try:
    import pypdf
except ImportError:
    sys.exit('pypdf is not installed: run this with `uv run`, or `pip install pypdf`.')

# Page ranges carry an en dash, which a Windows console may not encode.
for console_stream in (sys.stdout, sys.stderr):
    try:
        console_stream.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Fewer characters per page than this, on average, and a written chapter is flagged as thin: a preface,
# a plates section, a page of figures.
THIN_PAGE_CHARACTERS = 200
FRONT_MATTER_TITLE = 'Front matter'
NO_OUTLINE_MESSAGE = ' '.join([
    'no outline in this PDF: run --outline, read the table-of-contents pages,',
    'and pass --split "Title=first-last; ..."',
])
NOTHING_WRITTEN_MESSAGE = ' '.join([
    'nothing written: no text layer in what was asked for — a scanned PDF.',
    'Report it as unreadable.',
])
PAGE_RANGE = re.compile(r'\s*(\d+)\s*(?:-\s*(\d+))?\s*')
CHAPTER_NUMBERS = re.compile(r'(\d+)(?:-(\d+))?')


@dataclasses.dataclass(frozen=True)
class Chapter:
    """
    A chapter: its number in the outline, its title, and its pages, 0-based and inclusive.
    """
    number: int
    title: str
    start: int
    end: int

    @property
    def pages(self) -> str:
        """
        The pages as a reader writes them: 1-based, a range with an en dash, or one page.
        """
        first_page = self.start + 1
        last_page = self.end + 1
        label = f'{first_page}–{last_page}' if self.end > self.start else f'{first_page}'

        return label


@dataclasses.dataclass(frozen=True)
class ChapterPlan:
    """
    The chapters a run knows of, and how it came to know them — the line `OUTLINE.md` states.
    """
    chapters: list[Chapter]
    how: str


@dataclasses.dataclass(frozen=True)
class Entry:
    """
    One outline entry: its depth, its title, and the 0-based page it points to.
    """
    depth: int
    title: str
    page: int


@dataclasses.dataclass(frozen=True)
class Extraction:
    """
    What one extraction run did: the files written, and the chapters thin or empty with their averages.
    """
    written: list[pathlib.Path]
    thin: list[tuple[Chapter, float]]
    empty: list[tuple[Chapter, float]]


def chapters_from_outline(
    entries: list[Entry],
    depth: int,
    page_count: int,
) -> list[Chapter]:
    """
    The chapters: entries at `depth`, each running to the page before the next entry at that depth
    or shallower; the last to the end. Pages before the first chapter are chapter 0, front matter.
    """
    boundaries = sorted(
        (
            entry
            for entry
            in entries
            if entry.depth <= depth
        ),
        key=_entry_page,
    )
    first_page = next(
        (
            entry.page
            for entry
            in boundaries
            if entry.depth == depth
        ),
        None,
    )

    if first_page is None:

        return []

    front_matter = (
        [
            Chapter(
                0,
                FRONT_MATTER_TITLE,
                0,
                first_page - 1,
            ),
        ]
        if first_page > 0
        else []
    )
    chapter_positions = [
        position
        for position, entry
        in enumerate(boundaries)
        if entry.depth == depth
    ]
    chapters = [
        Chapter(
            number,
            boundaries[position].title,
            boundaries[position].page,
            _chapter_end(
                boundaries,
                position,
                page_count,
            ),
        )
        for number, position
        in enumerate(chapter_positions, start=1)
    ]
    all_chapters = [
        *front_matter,
        *chapters,
    ]

    return all_chapters


def clean(
    text: str,
) -> str:
    """
    A page's text with line endings made LF, trailing spaces dropped and blank runs collapsed.
    """
    unified = text.replace('\r\n', '\n').replace('\r', '\n')
    trimmed = re.sub(
        r'[ \t]+\n',
        '\n',
        unified,
    )
    collapsed = re.sub(
        r'\n{3,}',
        '\n\n',
        trimmed,
    )
    cleaned = collapsed.strip()

    return cleaned


def extract_chapters(
    arguments: argparse.Namespace,
    reader: pypdf.PdfReader,
    chapters: list[Chapter],
    engine: str,
    output_directory: pathlib.Path,
    source: str,
) -> Extraction:
    """
    Write every chapter with a text layer, and sort the rest into thin and empty.
    """
    pdf_path = pathlib.Path(arguments.pdf)
    use_pdftotext = not engine.startswith('pypdf')
    page_texts = {
        chapter.number: (
            pages_pdftotext(
                pdf_path,
                chapter.start,
                chapter.end,
            )
            if use_pdftotext
            else pages_pypdf(
                reader,
                chapter.start,
                chapter.end,
            )
        )
        for chapter
        in chapters
    }
    averages = {
        chapter.number: _average_characters(page_texts[chapter.number])
        for chapter
        in chapters
    }
    kept = [
        chapter
        for chapter
        in chapters
        if averages[chapter.number] >= arguments.min_chars
    ]
    written = [
        write_chapter(
            output_directory,
            source,
            chapter,
            page_texts[chapter.number],
            engine,
        )
        for chapter
        in kept
    ]
    thin = [
        (chapter, averages[chapter.number])
        for chapter
        in kept
        if averages[chapter.number] < THIN_PAGE_CHARACTERS
    ]
    empty = [
        (chapter, averages[chapter.number])
        for chapter
        in chapters
        if averages[chapter.number] < arguments.min_chars
    ]
    extraction = Extraction(
        written=written,
        thin=thin,
        empty=empty,
    )

    return extraction


def flatten_outline(
    reader: pypdf.PdfReader,
) -> list[Entry]:
    """
    The bookmarks as a flat list with depths; pypdf nests children as a list after their parent.
    """
    try:
        outline = reader.outline
    except Exception as exception:
        print(f'  outline unreadable: {exception}', file=sys.stderr)

        return []

    entries = _walk_outline(
        reader,
        outline or [],
        1,
    )

    return entries


def main(
    argv: list[str] | None = None,
) -> int:
    """
    Parse the command line, read the PDF, and print its outline or write the chapters asked for.
    """
    arguments = _build_parser().parse_args(argv)
    pdf_path = pathlib.Path(arguments.pdf)

    if not pdf_path.is_file():
        print(f'not a file: {pdf_path}', file=sys.stderr)

        return 1

    reader = pypdf.PdfReader(str(pdf_path))

    if reader.is_encrypted and not _decrypted(reader):
        print('encrypted PDF: cannot read it', file=sys.stderr)

        return 2

    # Loads the page tree; outline destinations resolve only after this.
    page_count = len(reader.pages)
    entries = flatten_outline(reader)

    if arguments.outline:
        print_outline(
            pdf_path,
            page_count,
            entries,
            arguments.depth,
        )

        return 0

    plan = _plan_chapters(
        arguments,
        pdf_path,
        entries,
        page_count,
    )

    if plan is None:
        print(NO_OUTLINE_MESSAGE, file=sys.stderr)

        return 3

    exit_code = _extract_plan(
        arguments,
        reader,
        pdf_path,
        page_count,
        plan,
    )

    return exit_code


def pages_pdftotext(
    pdf_path: pathlib.Path,
    start: int,
    end: int,
) -> list[str]:
    """
    The text of each page from `start` to `end`, 0-based and inclusive, by pdftotext.
    """
    command = [
        'pdftotext',
        '-f',
        str(start + 1),
        '-l',
        str(end + 1),
        '-enc',
        'UTF-8',
        str(pdf_path),
        '-',
    ]
    completed = subprocess.run(
        command,
        capture_output=True,
    )

    if completed.returncode != 0:
        error_text = completed.stderr.decode('utf-8', 'replace').strip()
        message = error_text or 'pdftotext failed'

        raise RuntimeError(message)

    pages = completed.stdout.decode('utf-8', 'replace').split('\f')
    trimmed = pages[:-1] if pages and pages[-1].strip() == '' else pages
    wanted = end - start + 1
    padded = (trimmed + [''] * wanted)[:wanted]

    return padded


def pages_pypdf(
    reader: pypdf.PdfReader,
    start: int,
    end: int,
) -> list[str]:
    """
    The text of each page from `start` to `end`, 0-based and inclusive, by pypdf.
    """
    pages = [
        reader.pages[index].extract_text() or ''
        for index
        in range(start, end + 1)
    ]

    return pages


def parse_numbers(
    specification: str,
    available: list[int],
) -> list[int]:
    """
    The chapter numbers `--chapters` names, as a sorted list; numbers and ranges only.
    """
    tokens = [
        token.strip()
        for token
        in specification.split(',')
        if token.strip()
    ]
    matches = {
        token: CHAPTER_NUMBERS.fullmatch(token)
        for token
        in tokens
    }
    unreadable = [
        token
        for token, match
        in matches.items()
        if match is None
    ]

    if unreadable:
        sys.exit(f'--chapters: numbers and ranges only, got {unreadable[0]!r}')

    wanted = {
        number
        for match
        in matches.values()
        for number
        in _number_range(match)
    }
    missing = sorted(wanted - set(available))

    if missing:
        sys.exit(f'--chapters: no chapter {missing} at this depth; run --outline to see the numbers')

    numbers = sorted(wanted)

    return numbers


def parse_split(
    specification: str,
    page_count: int,
) -> list[Chapter]:
    """
    The chapters `--split` names: `Title=first-last; Title=first-last`, pages 1-based and inclusive.
    """
    parts = [
        part.strip()
        for part
        in specification.split(';')
        if part.strip()
    ]
    chapters = [
        _split_chapter(
            number,
            part,
            page_count,
        )
        for number, part
        in enumerate(parts, start=1)
    ]

    return chapters


def pdftotext_label() -> str | None:
    """
    pdftotext's own version line, when it is on PATH; None when it is not.
    """
    executable = shutil.which('pdftotext')

    if not executable:

        return None

    try:
        completed = subprocess.run(
            [
                executable,
                '-v',
            ],
            capture_output=True,
            text=True,
        )
    except Exception:

        return 'pdftotext'

    version_text = (completed.stderr or completed.stdout).strip()
    first_line = (version_text.splitlines() or ['pdftotext'])[0]
    label = first_line.strip()

    return label


def print_outline(
    pdf_path: pathlib.Path,
    page_count: int,
    entries: list[Entry],
    depth: int,
) -> None:
    """
    Print the outline: entries per depth, and the chapters `--chapters` numbers, with their sections.
    """
    print(f'{pdf_path.name}: {page_count} pages')

    if not entries:
        print('  no outline (no bookmarks). Read the table-of-contents pages and pass')
        print('  --split "Title=first-last; Title=first-last", or --all for the whole PDF as one file.')

        return

    depths = sorted({
        entry.depth
        for entry
        in entries
    })
    counts = {
        level: sum(
            1
            for entry
            in entries
            if entry.depth == level
        )
        for level
        in depths
    }
    count_text = ', '.join(
        f'depth {level}: {count}'
        for level, count
        in counts.items()
    )
    print(f'  outline entries: {count_text}')
    chapters = chapters_from_outline(
        entries,
        depth,
        page_count,
    )
    print(f'  chapters at --depth {depth} (the numbers --chapters takes):')
    title_lengths = [
        len(chapter.title)
        for chapter
        in chapters
    ]
    title_width = max(title_lengths) if title_lengths else 10
    column_width = min(title_width, 70)

    for chapter in chapters:
        print(f'  {chapter.number:>3}. {chapter.title:<{column_width}}  p. {chapter.pages}')
        _print_sections(
            chapter,
            entries,
            depth,
        )

    if counts.get(depth, 0) <= 3 and counts.get(depth + 1, 0) >= 4:
        print(f'  depth {depth} looks like parts; consider --depth {depth + 1}')


def slugify(
    title: str,
    limit: int = 60,
) -> str:
    """
    `Author_Year_Title` style, the way the notes are named: ascii words joined by underscores,
    the source's own capitals kept.
    """
    normalized = unicodedata.normalize('NFKD', title)
    ascii_title = normalized.encode('ascii', 'ignore').decode()
    replaced = re.sub(
        r'[^A-Za-z0-9]+',
        '_',
        ascii_title,
    )
    joined = replaced.strip('_')
    slug = joined[:limit].rstrip('_') or 'Untitled'

    return slug


def write_chapter(
    output_directory: pathlib.Path,
    source: str,
    chapter: Chapter,
    pages: list[str],
    engine: str,
) -> pathlib.Path:
    """
    One chapter's extract: frontmatter, its heading, and each page's text after a page marker.
    """
    body = '\n'.join(
        f'<!-- p.{chapter.start + index + 1} -->\n{clean(text)}\n'
        for index, text
        in enumerate(pages)
    )
    content = ''.join([
        '---\n',
        f'source: {yaml_string(source)}\n',
        f'chapter: {chapter.number}\n',
        f'title: {yaml_string(chapter.title)}\n',
        f'pages: {yaml_string(chapter.pages)}\n',
        f'engine: {yaml_string(engine)}\n',
        '---\n\n',
        f'# {chapter.number}. {chapter.title}\n\n',
        body,
    ])
    file_name = f'{chapter.number:02d}_{slugify(chapter.title)}.md'
    path = output_directory / file_name
    path.write_text(
        content,
        encoding='utf-8',
        newline='\n',
    )

    return path


def write_outline(
    output_directory: pathlib.Path,
    source: str,
    page_count: int,
    chapters: list[Chapter],
    how: str,
) -> pathlib.Path:
    """
    `OUTLINE.md`: every chapter the run knows of, whether or not it was written.
    """
    header = [
        f'# {output_directory.name} — table of contents',
        '',
        f'Source: `{source}` — {page_count} pages — chapters from {how}.',
        'Extracted chapters sit beside this file, one per chapter, numbered as below.',
        'Regenerable and gitignored: cite the source, never this.',
        '',
        '| # | Chapter | Pages |',
        '| --- | --- | --- |',
    ]
    rows = [
        f'| {chapter.number} | {chapter.title} | {chapter.pages} |'
        for chapter
        in chapters
    ]
    lines = [
        *header,
        *rows,
    ]
    path = output_directory / 'OUTLINE.md'
    path.write_text(
        '\n'.join(lines) + '\n',
        encoding='utf-8',
        newline='\n',
    )

    return path


def yaml_string(
    value: str,
) -> str:
    """
    A value quoted for YAML frontmatter, the way JSON quotes it.
    """
    quoted = json.dumps(
        value,
        ensure_ascii=False,
    )

    return quoted


def _average_characters(
    pages: list[str],
) -> float:
    """
    The characters per page, on average, once each page is stripped.
    """
    total = sum(
        len(page.strip())
        for page
        in pages
    )
    average = total / max(1, len(pages))

    return average


def _build_parser() -> argparse.ArgumentParser:
    """
    The command line: the PDF, one of four modes, and the options.
    """
    parser = argparse.ArgumentParser(
        prog='extract.py',
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('pdf')
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        '--outline',
        action='store_true',
        help='print the outline; write nothing',
    )
    mode.add_argument(
        '--chapters',
        metavar='N,N-M',
        help='extract these chapters, by outline number',
    )
    mode.add_argument(
        '--all',
        action='store_true',
        help='extract every chapter',
    )
    mode.add_argument(
        '--split',
        metavar='SPEC',
        help='"Title=first-last; ..." when there is no outline',
    )
    parser.add_argument(
        '--out',
        default='Extracts',
        help='extracts root (default ./Extracts)',
    )
    parser.add_argument(
        '--depth',
        type=int,
        default=1,
        help='outline depth that counts as a chapter',
    )
    parser.add_argument(
        '--engine',
        choices=[
            'auto',
            'pdftotext',
            'pypdf',
        ],
        default='auto',
    )
    parser.add_argument(
        '--min-chars',
        type=int,
        default=40,
        help='avg chars/page below which there is no text layer',
    )

    return parser


def _chapter_end(
    boundaries: list[Entry],
    position: int,
    page_count: int,
) -> int:
    """
    The last page of the chapter at `position`: the page before the next boundary that starts later.
    """
    this_page = boundaries[position].page
    next_page = next(
        (
            boundary.page
            for boundary
            in boundaries[position + 1:]
            if boundary.page > this_page
        ),
        page_count,
    )
    end = min(next_page, page_count) - 1

    return end


def _chosen_chapters(
    specification: str,
    chapters: list[Chapter],
) -> list[Chapter]:
    """
    The chapters `--chapters` names, in outline order.
    """
    numbers = [
        chapter.number
        for chapter
        in chapters
    ]
    wanted = parse_numbers(
        specification,
        numbers,
    )
    chosen = [
        chapter
        for chapter
        in chapters
        if chapter.number in wanted
    ]

    return chosen


def _decrypted(
    reader: pypdf.PdfReader,
) -> bool:
    """
    Whether an encrypted PDF opens with the empty password.
    """
    try:
        reader.decrypt('')
    except Exception:

        return False

    return True


def _engine_label(
    engine_choice: str,
) -> str | None:
    """
    The engine a run uses, as its extracts name it; None when pdftotext was asked for and is missing.
    """
    label = pdftotext_label() if engine_choice in ('auto', 'pdftotext') else None

    if engine_choice == 'pdftotext' and not label:

        return None

    if label:

        return label

    try:
        pypdf_version = importlib.metadata.version('pypdf')
    except Exception:

        return 'pypdf'

    return f'pypdf {pypdf_version}'


def _entry_page(
    entry: Entry,
) -> int:
    """
    The page an entry points to, the key the outline is sorted by.
    """
    page = entry.page

    return page


def _extract_plan(
    arguments: argparse.Namespace,
    reader: pypdf.PdfReader,
    pdf_path: pathlib.Path,
    page_count: int,
    plan: ChapterPlan,
) -> int:
    """
    Write `OUTLINE.md` and the chapters asked for, report, and give the exit code.
    """
    chosen = (
        _chosen_chapters(
            arguments.chapters,
            plan.chapters,
        )
        if arguments.chapters
        else plan.chapters
    )
    engine = _engine_label(arguments.engine)

    if engine is None:
        print('pdftotext is not on PATH; use --engine pypdf', file=sys.stderr)

        return 1

    source = pdf_path.as_posix()
    output_directory = pathlib.Path(arguments.out) / slugify(pdf_path.stem, 80)
    output_directory.mkdir(
        parents=True,
        exist_ok=True,
    )
    write_outline(
        output_directory,
        source,
        page_count,
        plan.chapters,
        plan.how,
    )
    extraction = extract_chapters(
        arguments,
        reader,
        chosen,
        engine,
        output_directory,
        source,
    )
    _report(
        pdf_path,
        page_count,
        engine,
        output_directory,
        extraction,
    )

    if not extraction.written:
        print(NOTHING_WRITTEN_MESSAGE, file=sys.stderr)

        return 2

    return 0


def _number_range(
    match: re.Match[str],
) -> range:
    """
    The chapter numbers one `--chapters` token names: one number, or a range, inclusive.
    """
    first_number = int(match.group(1))
    last_text = match.group(2) or match.group(1)
    last_number = int(last_text)
    numbers = range(first_number, last_number + 1)

    return numbers


def _outline_entry(
    reader: pypdf.PdfReader,
    item: object,
    depth: int,
) -> Entry | None:
    """
    One bookmark as an entry, or None — with a note — when it points to no page.
    """
    raw_title = getattr(
        item,
        'title',
        '',
    )
    title = str(raw_title).strip() or '(untitled)'

    try:
        page = reader.get_destination_page_number(item)
    except Exception:
        page = None

    if page is None:
        print(f'  outline entry without a page, skipped: {title!r}', file=sys.stderr)

        return None

    entry = Entry(
        depth,
        title,
        int(page),
    )

    return entry


def _plan_chapters(
    arguments: argparse.Namespace,
    pdf_path: pathlib.Path,
    entries: list[Entry],
    page_count: int,
) -> ChapterPlan | None:
    """
    The chapters a run works from: `--split`, the outline, or the whole PDF under `--all`; None when
    there is no outline and nothing else was asked for.
    """
    if arguments.split:
        split_plan = ChapterPlan(
            chapters=parse_split(
                arguments.split,
                page_count,
            ),
            how='--split, page ranges given by hand',
        )

        return split_plan

    outline_chapters = chapters_from_outline(
        entries,
        arguments.depth,
        page_count,
    )

    if outline_chapters:
        outline_plan = ChapterPlan(
            chapters=outline_chapters,
            how=f'the PDF outline at depth {arguments.depth}',
        )

        return outline_plan

    if arguments.all:
        whole_plan = ChapterPlan(
            chapters=[
                Chapter(
                    1,
                    pdf_path.stem,
                    0,
                    page_count - 1,
                ),
            ],
            how='no outline: the whole PDF as one chapter',
        )

        return whole_plan

    return None


def _print_sections(
    chapter: Chapter,
    entries: list[Entry],
    depth: int,
) -> None:
    """
    Under a depth-1 chapter, its depth-2 entries with their pages.
    """
    if depth != 1:

        return

    sections = [
        entry
        for entry
        in entries
        if entry.depth == 2 and chapter.start <= entry.page <= chapter.end
    ]

    for section in sections:
        print(f'         · {section.title}  (p. {section.page + 1})')


def _report(
    pdf_path: pathlib.Path,
    page_count: int,
    engine: str,
    output_directory: pathlib.Path,
    extraction: Extraction,
) -> None:
    """
    Print what was written, and what was thin or had no text layer.
    """
    print(f'{pdf_path.name}: {page_count} pages, {engine}, extracts in {output_directory.as_posix()}/')

    for path in extraction.written:
        print(f'  wrote {path.name}')

    for chapter, average in extraction.thin:
        thin_warning = ' '.join([
            f'  thin: {chapter.number}. {chapter.title} (p. {chapter.pages}) — {average:.0f} chars/page;',
            'written, check it is prose',
        ])
        print(thin_warning, file=sys.stderr)

    for chapter, average in extraction.empty:
        empty_warning = ' '.join([
            f'  not written: {chapter.number}. {chapter.title} (p. {chapter.pages}) —',
            f'{average:.0f} chars/page, no text layer',
        ])
        print(empty_warning, file=sys.stderr)


def _split_chapter(
    number: int,
    part: str,
    page_count: int,
) -> Chapter:
    """
    One `Title=first-last` item of `--split` as a chapter; exits on an item it cannot read.
    """
    if '=' not in part:
        sys.exit(f'--split: each item is Title=first-last, got {part!r}')

    title, page_range = part.rsplit('=', 1)
    match = PAGE_RANGE.fullmatch(page_range)

    if not match:
        sys.exit(f'--split: bad page range {page_range!r} in {part!r}')

    first_page = int(match.group(1))
    last_text = match.group(2) or match.group(1)
    last_page = int(last_text)

    if not 1 <= first_page <= last_page <= page_count:
        sys.exit(f'--split: pages {first_page}-{last_page} outside 1-{page_count} in {part!r}')

    chapter = Chapter(
        number,
        title.strip() or f'Part {number}',
        first_page - 1,
        last_page - 1,
    )

    return chapter


def _walk_outline(
    reader: pypdf.PdfReader,
    items: list,
    depth: int,
) -> list[Entry]:
    """
    The entries of one outline level and, depth first, of the lists nested in it.
    """
    entries = []

    for item in items:
        if isinstance(item, list):
            entries.extend(_walk_outline(
                reader,
                item,
                depth + 1,
            ))

            continue

        entry = _outline_entry(
            reader,
            item,
            depth,
        )

        if entry is not None:
            entries.append(entry)

    return entries


if __name__ == '__main__':
    sys.exit(main())
