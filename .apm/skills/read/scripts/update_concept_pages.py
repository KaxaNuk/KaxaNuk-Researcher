"""
Concept pages brought up to date in one pass, from a spec of what each page gains: the notes in its
`sources`, the claims under What the sources say, a blockquote for the owner's questions, and lines
under Open. `updated` takes the date; nothing else on the page changes.

    uv run --no-project python update_concept_pages.py SPEC                 the diff, nothing written
    uv run --no-project python update_concept_pages.py SPEC --write         the pages written
    uv run --no-project python update_concept_pages.py - --write < SPEC     the spec on standard input

The spec, one block per page, its markers alone at the start of their lines:

    @@FILE Finance/Position_Sizing_Rules.md
    @@SOURCES
    Paleologo_2021_Advanced_Portfolio_Management/10_Use_Effective_Heuristics_for_Alpha_Sizing.md
    @@BULLETS
    - A claim, in one or two lines
      ([Paleologo 2021, ch. 10, p. 93](Paleologo_2021_Advanced_Portfolio_Management/10_Use_Effective_Heuristics_for_Alpha_Sizing.md)).
    @@QUOTE
    > **Question 1:** what the idea now says to the question.
    @@OPEN
    - What the library does not yet hold on this idea.
    @@END

@@FILE names a page by its path under Knowledge/. Each part is optional, and each adds:
    @@SOURCES   one note a line, as the page's sources list writes it, appended to that list; one
                already there is skipped
    @@BULLETS   claims, each a list item and its own lines, appended after the last claim under
                What the sources say, before any callout that closes the section; one already
                there, word for word, is skipped
    @@QUOTE     a blockquote, appended to the section for the owner's questions — the heading that
                opens `## For` and names questions — after a blank line; skipped when already there
    @@OPEN      lines appended under Open; a line already there is skipped
A block ends at @@END, at the next @@FILE, or at the end of the spec.

Every page is checked before any is written: a page that is not there, is not a concept page — its
frontmatter's `type: concept` — or lacks a section a part needs, stops the run with nothing written,
as a spec it cannot read does. A page is never created here: a new page is written whole, in the
shape the read skill's references/note.md gives. Pages are read as UTF-8 and written with LF line
endings.

Options
    --knowledge DIR   the library's Knowledge/ folder (default ./Knowledge)
    --date DATE       the date `updated` takes, YYYY-MM-DD (default today)
    --write           write the pages; without it, print the diff and write nothing

Exit codes: 0 done, or the diff printed · 1 usage, a spec it cannot read or a page it cannot update:
nothing written.
It needs only the standard library.
"""
import argparse
import dataclasses
import datetime
import difflib
import pathlib
import re
import sys

SCRIPT_DIRECTORY = pathlib.Path(__file__).resolve().parent

if str(SCRIPT_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIRECTORY))

import library  # noqa: E402 - found beside this file once its folder is on the path, `python -I` too.

PART_MARKERS = frozenset({
    'BULLETS',
    'OPEN',
    'QUOTE',
    'SOURCES',
})
DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
LIST_ITEM = re.compile(r'^[-*+]\s+')
MARKER = re.compile(r'^@@([A-Z]+)(?:\s+(.*?))?\s*$')
OPEN_HEADING = re.compile(
    r'^##\s+Open\s*$',
    re.IGNORECASE,
)
QUESTIONS_HEADING = re.compile(
    r'^##\s+For\b.*\bquestions?\b',
    re.IGNORECASE,
)
SECTION_HEADING = re.compile(r'^#{1,2}\s')
SOURCES_ITEM = re.compile(r'^(\s+)-\s*(.*)$')
SOURCES_SAY_HEADING = re.compile(
    r'^##\s+What the sources say\s*$',
    re.IGNORECASE,
)


@dataclasses.dataclass(frozen=True)
class PageEdit:
    """
    What one block of the spec adds to one page: the page, the spec's line it starts on, and each
    part's lines.
    """
    bullets: list[str]
    file: str
    line: int
    open_lines: list[str]
    quote: list[str]
    sources: list[str]


@dataclasses.dataclass(frozen=True)
class PageText:
    """
    A page's text before the spec, and after it.
    """
    original: str
    updated: str


class EditProblem(Exception):
    """
    A spec or a page that cannot be applied; the run stops with nothing written.
    """


def apply_edit(
    text: str,
    edit: PageEdit,
    date: str,
) -> str:
    """
    A page's text with one block of the spec applied: `updated` set, then each part added.
    """
    lines = text.splitlines()
    with_date = _with_updated(
        lines,
        date,
        edit.file,
    )
    with_sources = _with_sources(
        with_date,
        edit.sources,
        edit.file,
    ) if edit.sources else with_date
    with_bullets = _with_bullets(
        with_sources,
        edit.bullets,
        edit.file,
    ) if edit.bullets else with_sources
    with_quote = _with_quote(
        with_bullets,
        edit.quote,
        edit.file,
    ) if edit.quote else with_bullets
    with_open = _with_open_lines(
        with_quote,
        edit.open_lines,
        edit.file,
    ) if edit.open_lines else with_quote
    updated = '\n'.join(with_open) + '\n'

    return updated


def main(
    arguments: list[str] | None = None,
) -> int:
    """
    Parse the command line and the spec, apply every block to its page in memory, and print the diff
    or write the pages.
    """
    library.configure_console()
    parser = _build_parser()
    parsed = parser.parse_args(arguments)
    date = parsed.date or datetime.date.today().isoformat()

    if not DATE.match(date):
        parser.error(f'--date {date} is not YYYY-MM-DD')

    knowledge = pathlib.Path(parsed.knowledge)

    if not knowledge.is_dir():
        parser.error(f'no such folder: {knowledge}')

    spec_text = _read_spec(parsed.spec)

    try:
        edits = parse_spec(spec_text)
        changed = updated_pages(
            knowledge,
            edits,
            date,
        )
    except EditProblem as problem:
        print(f'nothing written: {problem}', file=sys.stderr)

        return 1

    for page_path, page_text in changed.items():
        inside = page_path.relative_to(knowledge)
        name = f'{knowledge.name}/{inside.as_posix()}'

        if parsed.write:
            page_path.write_text(
                page_text.updated,
                encoding='utf-8',
                newline='\n',
            )
            print(f'updated {name}')
        else:
            diff = difflib.unified_diff(
                page_text.original.splitlines(keepends=True),
                page_text.updated.splitlines(keepends=True),
                fromfile=f'a/{name}',
                tofile=f'b/{name}',
            )
            sys.stdout.writelines(diff)

    named_pages = {
        edit.file
        for edit
        in edits
    }
    unchanged_count = len(named_pages) - len(changed)
    changed_text = library.counted(
        len(changed),
        'page',
    )
    done = 'written' if parsed.write else 'to change'
    summary = f'{changed_text} {done}, {unchanged_count} holding everything already'
    print(summary)

    return 0


def parse_spec(
    text: str,
) -> list[PageEdit]:
    """
    The spec's blocks, each a page and its parts, in the order written.
    """
    lines = text.splitlines()
    markers = [
        (index, match)
        for index, line
        in enumerate(lines)
        for match
        in [MARKER.match(line)]
        if match is not None
    ]
    unknown = [
        f'line {index + 1}: @@{match.group(1)} is not a marker'
        for index, match
        in markers
        if match.group(1) not in PART_MARKERS | {'FILE', 'END'}
    ]
    file_positions = [
        index
        for index, match
        in markers
        if match.group(1) == 'FILE'
    ]
    first_content = next(
        (
            index
            for index, line
            in enumerate(lines)
            if line.strip()
        ),
        None,
    )
    stray_start = first_content is not None and first_content not in file_positions
    problems = unknown + ([f'line {first_content + 1}: the spec opens with no @@FILE'] if stray_start else [])

    if problems:
        message = '; '.join(problems)

        raise EditProblem(message)

    block_ends = file_positions[1:] + [len(lines)]
    edits = [
        _parse_block(
            lines,
            start,
            end,
        )
        for start, end
        in zip(file_positions, block_ends)
    ]

    if not edits:
        no_page = 'the spec names no page: it needs @@FILE <path under Knowledge/>'

        raise EditProblem(no_page)

    return edits


def updated_pages(
    knowledge: pathlib.Path,
    edits: list[PageEdit],
    date: str,
) -> dict[pathlib.Path, PageText]:
    """
    Every page the spec changes, with its text before and after, every block applied in order; a
    page the spec leaves as it was is not among them.
    """
    texts = {}

    for edit in edits:
        page_path = _page_path(
            knowledge,
            edit,
        )
        known = texts.get(page_path)
        before = known.updated if known is not None else _read_page(
            page_path,
            edit,
        )
        after = apply_edit(
            before,
            edit,
            date,
        )
        texts[page_path] = PageText(
            original=before if known is None else known.original,
            updated=after,
        )

    changed = {
        page_path: page_text
        for page_path, page_text
        in texts.items()
        if page_text.original != page_text.updated
    }

    return changed


def _append_to_section(
    lines: list[str],
    heading: re.Pattern[str],
    added: list[str],
    file: str,
    separated: bool,
) -> list[str]:
    """
    Lines added at the end of a section, after its last line with text, a blank line between when
    `separated`; the section's own heading found by a pattern, or the edit refused.
    """
    start = _section_start(
        lines,
        heading,
        file,
    )
    end = _section_end(
        lines,
        start,
    )
    last_text = max(
        (
            index
            for index
            in range(start, end)
            if lines[index].strip()
        ),
    )
    spacer = [''] if separated else []
    appended = lines[:last_text + 1] + spacer + added + lines[last_text + 1:]

    return appended


def _build_parser() -> library.CommandLineParser:
    """
    The command line: the spec, the Knowledge folder, the date, and whether to write.
    """
    parser = library.CommandLineParser(
        prog='update_concept_pages.py',
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        'spec',
        help='the spec file, or - for standard input',
    )
    parser.add_argument(
        '--knowledge',
        default='Knowledge',
        help="the library's Knowledge/ folder (default ./Knowledge)",
    )
    parser.add_argument(
        '--date',
        help='the date updated takes, YYYY-MM-DD (default today)',
    )
    parser.add_argument(
        '--write',
        action='store_true',
        help='write the pages; without it, print the diff only',
    )

    return parser


def _ends_item(
    line: str,
) -> bool:
    """
    Whether a line ends the list item above it: a blank line, or a callout or a quote.
    """
    stripped = line.strip()
    ends = not stripped or stripped.startswith('>')

    return ends


def _frontmatter_end(
    lines: list[str],
    file: str,
) -> int:
    """
    The index of the line that closes a page's frontmatter; the edit refused when it has none.
    """
    closing = next(
        (
            position
            for position
            in range(1, len(lines))
            if lines[position].strip() == '---'
        ),
        None,
    ) if lines and lines[0].strip() == '---' else None

    if closing is None:
        message = f'{file} has no frontmatter'

        raise EditProblem(message)

    return closing


def _item_blocks(
    lines: list[str],
) -> list[list[str]]:
    """
    Lines grouped into list items: each item's first line and the lines that follow it, up to a
    blank line, a callout or the next item.
    """
    starts = [
        index
        for index, line
        in enumerate(lines)
        if LIST_ITEM.match(line)
    ]
    ends = starts[1:] + [len(lines)]
    blocks = [
        lines[start:last + 1]
        for start, end
        in zip(starts, ends)
        for last
        in [_item_end(
            lines,
            start,
            end,
        )]
    ]

    return blocks


def _item_end(
    lines: list[str],
    item_start: int,
    section_end: int,
) -> int:
    """
    The index of a list item's last line: its first, and those after it up to a blank line, a
    callout or the section's end.
    """
    following = [
        index
        for index
        in range(item_start + 1, section_end)
    ]
    stop = next(
        (
            index
            for index
            in following
            if _ends_item(lines[index])
        ),
        section_end,
    )
    last = stop - 1

    return last


def _marker_name(
    line: str,
) -> str:
    """
    The name of the marker a spec line opens with: `BULLETS` for `@@BULLETS`.
    """
    marker = MARKER.match(line)
    name = marker.group(1)

    return name


def _page_path(
    knowledge: pathlib.Path,
    edit: PageEdit,
) -> pathlib.Path:
    """
    The page a block names, inside the Knowledge folder; the edit refused when it climbs out of it,
    is not a markdown file, or is not there.
    """
    given = pathlib.PurePosixPath(edit.file.replace('\\', '/'))
    climbs = given.is_absolute() or '..' in given.parts or ':' in edit.file
    page_path = knowledge.joinpath(*given.parts)
    problem = next(
        (
            reason
            for applies, reason
            in [
                (climbs, 'is not a path under Knowledge/'),
                (given.suffix.lower() != '.md', 'is not a markdown page'),
                (not page_path.is_file(), 'is not there; a new page is written whole, never here'),
            ]
            if applies
        ),
        None,
    )

    if problem is not None:
        message = f'spec line {edit.line}: {edit.file} {problem}'

        raise EditProblem(message)

    return page_path


def _parse_block(
    lines: list[str],
    start: int,
    end: int,
) -> PageEdit:
    """
    One block of the spec, from its @@FILE line to the next: the page and each part's lines.
    """
    file_match = MARKER.match(lines[start])
    file = file_match.group(2) or ''

    if not file:
        message = f'spec line {start + 1}: @@FILE names no page'

        raise EditProblem(message)

    end_marker = next(
        (
            index
            for index
            in range(start + 1, end)
            if lines[index].strip() == '@@END'
        ),
        end,
    )
    part_starts = [
        index
        for index
        in range(start + 1, end_marker)
        if MARKER.match(lines[index])
    ]
    part_ends = part_starts[1:] + [end_marker]
    parts = {
        _marker_name(lines[part_start]): _trimmed(lines[part_start + 1:part_end])
        for part_start, part_end
        in zip(part_starts, part_ends)
    }
    loose = [
        index
        for index
        in range(start + 1, part_starts[0] if part_starts else end_marker)
        if lines[index].strip()
    ]

    if loose:
        loose_text = f'spec line {loose[0] + 1}: text before any @@SOURCES, @@BULLETS, @@QUOTE or @@OPEN'

        raise EditProblem(loose_text)

    edit = PageEdit(
        bullets=parts.get('BULLETS', []),
        file=file,
        line=start + 1,
        open_lines=parts.get('OPEN', []),
        quote=parts.get('QUOTE', []),
        sources=[
            _source_name(line)
            for line
            in parts.get('SOURCES', [])
            if line.strip()
        ],
    )

    return edit


def _read_page(
    page_path: pathlib.Path,
    edit: PageEdit,
) -> str:
    """
    A page's text, refused unless its frontmatter says it is a concept page.
    """
    text = page_path.read_text(encoding='utf-8-sig')
    front = library.parse_frontmatter(text)
    page_type = library.field_value(
        front,
        'type',
    )

    if page_type.casefold() != 'concept':
        message = f'spec line {edit.line}: {edit.file} is not a concept page — its type is {page_type or "missing"}'

        raise EditProblem(message)

    return text


def _read_spec(
    spec: str,
) -> str:
    """
    The spec's text, from its file or from standard input.
    """
    if spec == '-':
        text = sys.stdin.read()
    else:
        text = pathlib.Path(spec).read_text(encoding='utf-8-sig')

    return text


def _section_end(
    lines: list[str],
    start: int,
) -> int:
    """
    The index just past a section: the next heading of level one or two, or the end of the page.
    """
    end = next(
        (
            position
            for position
            in range(start + 1, len(lines))
            if SECTION_HEADING.match(lines[position])
        ),
        len(lines),
    )

    return end


def _section_start(
    lines: list[str],
    heading: re.Pattern[str],
    file: str,
) -> int:
    """
    The index of a section's heading; the edit refused when the page has none.
    """
    start = next(
        (
            index
            for index, line
            in enumerate(lines)
            if heading.match(line)
        ),
        None,
    )

    if start is None:
        message = f'{file} has no section headed as {heading.pattern} asks'

        raise EditProblem(message)

    return start


def _source_item(
    line: str,
) -> str:
    """
    The note a line of the `sources` list names, its quotes stripped.
    """
    item = SOURCES_ITEM.match(line)
    name = library.unquoted(item.group(2))

    return name


def _source_name(
    line: str,
) -> str:
    """
    A spec's source line as the list holds it: no list mark, no quotes.
    """
    stripped = line.strip()
    without_mark = stripped[1:] if stripped.startswith('-') else stripped
    name = library.unquoted(without_mark)

    return name


def _trimmed(
    lines: list[str],
) -> list[str]:
    """
    Lines without the blank lines at either end.
    """
    with_text = [
        index
        for index, line
        in enumerate(lines)
        if line.strip()
    ]
    trimmed = lines[with_text[0]:with_text[-1] + 1] if with_text else []

    return trimmed


def _with_bullets(
    lines: list[str],
    bullets: list[str],
    file: str,
) -> list[str]:
    """
    New claims after the last claim under What the sources say; a claim already there is skipped.
    """
    start = _section_start(
        lines,
        SOURCES_SAY_HEADING,
        file,
    )
    end = _section_end(
        lines,
        start,
    )
    section = lines[start + 1:end]
    present = [
        '\n'.join(block)
        for block
        in _item_blocks(section)
    ]
    new_blocks = [
        block
        for block
        in _item_blocks(bullets)
        if '\n'.join(block) not in present
    ]

    if not new_blocks:

        return lines

    item_positions = [
        start + 1 + index
        for index, line
        in enumerate(section)
        if LIST_ITEM.match(line)
    ]
    last_item = item_positions[-1] if item_positions else None
    insert_after = start if last_item is None else _item_end(
        lines,
        last_item,
        end,
    )
    added = [
        line
        for block
        in new_blocks
        for line
        in block
    ]
    spacer = [''] if last_item is None else []
    inserted = lines[:insert_after + 1] + spacer + added + lines[insert_after + 1:]

    return inserted


def _with_open_lines(
    lines: list[str],
    open_lines: list[str],
    file: str,
) -> list[str]:
    """
    New lines at the end of Open; a line already there is skipped.
    """
    start = _section_start(
        lines,
        OPEN_HEADING,
        file,
    )
    end = _section_end(
        lines,
        start,
    )
    present = {
        line.strip()
        for line
        in lines[start + 1:end]
    }
    new_lines = [
        line
        for line
        in open_lines
        if line.strip() and line.strip() not in present
    ]
    appended = _append_to_section(
        lines,
        OPEN_HEADING,
        new_lines,
        file,
        False,
    ) if new_lines else lines

    return appended


def _with_quote(
    lines: list[str],
    quote: list[str],
    file: str,
) -> list[str]:
    """
    A blockquote at the end of the section for the owner's questions, a blank line before it; one
    already there, word for word, is skipped.
    """
    start = _section_start(
        lines,
        QUESTIONS_HEADING,
        file,
    )
    end = _section_end(
        lines,
        start,
    )
    section_text = '\n'.join(lines[start + 1:end])
    quote_text = '\n'.join(quote)
    appended = lines if quote_text in section_text else _append_to_section(
        lines,
        QUESTIONS_HEADING,
        quote,
        file,
        True,
    )

    return appended


def _with_sources(
    lines: list[str],
    sources: list[str],
    file: str,
) -> list[str]:
    """
    New notes at the end of the frontmatter's `sources` list, written as a block list; a note already
    there is skipped.
    """
    closing = _frontmatter_end(
        lines,
        file,
    )
    field_index = next(
        (
            index
            for index
            in range(1, closing)
            if lines[index].startswith('sources:')
        ),
        None,
    )

    if field_index is None:
        message = f'{file} has no sources field in its frontmatter'

        raise EditProblem(message)

    inline_text = lines[field_index][len('sources:'):].strip()
    inline_items = [
        library.unquoted(item)
        for item
        in inline_text.strip('[]').split(',')
        if item.strip()
    ]
    item_indexes = [
        index
        for index
        in range(field_index + 1, closing)
        if SOURCES_ITEM.match(lines[index])
    ]
    contiguous = [
        index
        for position, index
        in enumerate(item_indexes)
        if index == field_index + 1 + position
    ]
    existing = inline_items + [
        _source_item(lines[index])
        for index
        in contiguous
    ]
    indent = SOURCES_ITEM.match(lines[contiguous[0]]).group(1) if contiguous else '  '
    new_items = [
        f'{indent}- {source}'
        for source
        in dict.fromkeys(sources)
        if source not in existing
    ]

    if not new_items:

        return lines

    rewritten_inline = [
        f'{indent}- {item}'
        for item
        in inline_items
    ]
    last_item = contiguous[-1] if contiguous else field_index
    with_items = [
        *lines[:field_index],
        'sources:',
        *rewritten_inline,
        *lines[field_index + 1:last_item + 1],
        *new_items,
        *lines[last_item + 1:],
    ]

    return with_items


def _with_updated(
    lines: list[str],
    date: str,
    file: str,
) -> list[str]:
    """
    The frontmatter's `updated` set to the date, added after `type` when the page has none.
    """
    closing = _frontmatter_end(
        lines,
        file,
    )
    updated_index = next(
        (
            index
            for index
            in range(1, closing)
            if lines[index].startswith('updated:')
        ),
        None,
    )
    type_index = next(
        (
            index
            for index
            in range(1, closing)
            if lines[index].startswith('type:')
        ),
        0,
    )
    dated_line = f'updated: {date}'

    if updated_index is not None:
        replaced = lines[:updated_index] + [dated_line] + lines[updated_index + 1:]

        return replaced

    inserted = lines[:type_index + 1] + [dated_line] + lines[type_index + 1:]

    return inserted


if __name__ == '__main__':
    sys.exit(main())
