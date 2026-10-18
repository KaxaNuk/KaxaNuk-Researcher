"""
Every source in a library that no note has read: the files under `Sources/` at home, or a
strategy's PDFs and clippings in `Bibliotheca/`, that no note's `local_copy` names.

    uv run --no-project python unread_sources.py                  the library in this folder
    uv run --no-project python unread_sources.py "D:/Research/Arya"
    uv run --no-project python unread_sources.py . --all          every source, read or not

What it reads
    a library   the folder given, or this one: a home, which holds RESEARCHER.md, or a strategy,
                which holds Bibliotheca/
    a source    at home, every file under Sources/; in a strategy, every file under
                Bibliotheca/Papers/ and Books/ that is not a note, and every file under
                Bibliotheca/Notes/. Never a .gitkeep, a hidden file or what a file manager leaves
    a note      every markdown file under Knowledge/ at home, or under Bibliotheca/Papers/ and
                Books/ in a strategy, by its frontmatter's local_copy

A source is read when a note's local_copy names it by its full path — from the library's root,
`Sources/Papers/Markowitz, H. (1952) Portfolio Selection.pdf`, or, in a strategy, from the note's
own folder too. Paths are compared as paths, never through a shell, so commas, parentheses, spaces
and accents are safe, and in the case the platform folds to. Nothing filters by date: a source
filed months ago and never read is listed as one filed today is. A searchable copy of a scan,
named `<the scan's name> (OCR).pdf` beside it, reads for both: a note on either covers the other.

For an unread source it names, first and alone, any note that reads another copy of the same name
— `Deck_2026-10-04_0936.pdf` for `Deck.pdf`, an earlier or a later copy of one work. With none, it
names at most three notes of the same first author and year that share a word of its title, those
sharing the most first: an organisation that authors many clippings has many notes of one year,
and only a shared word makes one of them a lead.

Exit codes: 0 every source read · 1 usage: the folder is not a library · 2 at least one unread.
It needs only the standard library, and writes nothing.
"""
import argparse
import collections
import dataclasses
import pathlib
import re
import sys

SCRIPT_DIRECTORY = pathlib.Path(__file__).resolve().parent

if str(SCRIPT_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIRECTORY))

import library  # noqa: E402 - found beside this file once its folder is on the path, `python -I` too.

OCR_SUFFIX = ' (OCR)'
YEAR = re.compile(r'^(?:1[5-9]|20)\d\d$')
# What may follow a name in another copy's name: a date, a time, a version, a note in brackets.
COPY_SEPARATORS = frozenset({
    ' ',
    '(',
    '-',
    '.',
    '_',
})
MAXIMUM_NAMESAKES = 3
# What a `local_copy` writes when there is no copy.
NO_COPY = frozenset({
    '',
    'none',
})
# Words a title shares with any other, never a reason to name a note.
TITLE_STOP_WORDS = frozenset({
    'and',
    'del',
    'for',
    'from',
    'into',
    'las',
    'los',
    'md',
    'pdf',
    'readme',
    'the',
    'with',
})


@dataclasses.dataclass(frozen=True)
class SourceStatus:
    """
    One source and what the library holds on it: the notes that name it, the copy they read it
    through, and, when none does, the notes that read another copy of the same name, or those of the
    same first author and year that share a word of its title.
    """
    copies: list[library.LibraryFile]
    namesakes: list[library.LibraryFile]
    notes: list[library.LibraryFile]
    path: pathlib.Path
    read_through: pathlib.Path | None


@dataclasses.dataclass(frozen=True)
class UnreadReport:
    """
    Every source of a library with its status, in the order the sources sort.
    """
    sources: list[SourceStatus]

    @property
    def unread(self) -> list[SourceStatus]:
        """
        The sources no note names, directly or through an OCR copy.
        """
        unread_sources = [
            status
            for status
            in self.sources
            if not status.notes
        ]

        return unread_sources


def lead_texts(
    found: library.Library,
    status: SourceStatus,
) -> list[str]:
    """
    What an unread source's leads say: each note reading another copy of its name, else each
    namesake, with the `local_copy` it names.
    """
    copy_texts = [
        ' '.join([
            f'another copy of it is read: {library.relative_name(found, note.path)}',
            f'reads {library.field_value(note.front, "local_copy")}',
        ])
        for note
        in status.copies
    ]
    namesake_texts = [
        ' '.join([
            f'{note.kind} of the same first author and year, with a word of its title:',
            f'{library.relative_name(found, note.path)}, whose local_copy is',
            library.field_value(note.front, 'local_copy') or 'missing',
        ])
        for note
        in status.namesakes
    ]
    texts = copy_texts + namesake_texts

    return texts


def main(
    arguments: list[str] | None = None,
) -> int:
    """
    Parse the command line, find the library, and print its unread sources.
    """
    library.configure_console()
    parsed = _build_parser().parse_args(arguments)
    found = library.find_library(pathlib.Path(parsed.folder))

    if found is None:
        problem = f'not a library: {parsed.folder} holds neither RESEARCHER.md nor Bibliotheca/'
        print(problem, file=sys.stderr)

        return 1

    files = library.library_files(found)
    report = unread_report(
        found,
        files,
    )
    print_report(
        found,
        report,
        parsed.all,
    )
    exit_code = 2 if report.unread else 0

    return exit_code


def print_report(
    found: library.Library,
    report: UnreadReport,
    show_all: bool,
) -> None:
    """
    The summary line, then one line per unread source with any namesake beneath it; with `show_all`,
    the read sources too, each with the note that names it.
    """
    read_count = sum(
        1
        for status
        in report.sources
        if status.notes and status.read_through is None
    )
    through_count = sum(
        1
        for status
        in report.sources
        if status.notes and status.read_through is not None
    )
    unread_count = len(report.unread)
    summary = ', '.join([
        library.counted(len(report.sources), 'source'),
        f'{read_count} read',
        f'{through_count} read through an OCR copy',
        f'{unread_count} unread',
    ])
    print(f'{found.kind} {found.root.as_posix()}: {summary}')

    for status in report.sources:
        for line in _status_lines(
            found,
            status,
            show_all,
        ):
            print(line)


def unread_report(
    found: library.Library,
    files: list[library.LibraryFile],
) -> UnreadReport:
    """
    Every source of the library, matched against every note's `local_copy` by full path.
    """
    notes = [
        note
        for note
        in files
        if note.kind in library.NOTE_KINDS
    ]
    notes_by_path = collections.defaultdict(list)

    for note in notes:
        copy = library.local_copy_path(
            found,
            note,
        )

        if copy is not None:
            notes_by_path[library.comparable_path(copy)].append(note)

    statuses = [
        _source_status(
            source,
            notes_by_path,
            notes,
        )
        for source
        in library.source_files(found)
    ]
    report = UnreadReport(sources=statuses)

    return report


def _author_and_year(
    words: list[str],
) -> str | None:
    """
    A name's first word and its first year, `markowitz 1952`, or None when it has no year after a
    first word.
    """
    years = [
        word
        for word
        in words[1:]
        if YEAR.match(word)
    ]

    if not words or not years:

        return None

    author_year = f'{words[0]} {years[0]}'

    return author_year


def _build_parser() -> library.CommandLineParser:
    """
    The command line: the library's folder, and whether to list every source.
    """
    parser = library.CommandLineParser(
        prog='unread_sources.py',
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        'folder',
        nargs='?',
        default='.',
        help='the library: a home or a strategy (default: this folder)',
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='list every source, read or not',
    )

    return parser


def _copy_stem(
    note: library.LibraryFile,
) -> str:
    """
    The file name, without its extension, a note's `local_copy` names; empty when it names none.
    """
    value = library.field_value(
        note.front,
        'local_copy',
    )
    forward = value.replace('\\', '/')
    names_none = value.casefold() in NO_COPY
    stem = '' if names_none else pathlib.PurePosixPath(forward).stem

    return stem


def _is_other_copy(
    source_stem: str,
    copy_stem: str,
) -> bool:
    """
    Whether two file names are two copies of one work: the same name in another folder, or one name
    with something after it — a date, a time, a version — joined by a space, a hyphen, an
    underscore, a dot or a bracket.
    """
    source_name = source_stem.casefold()
    copy_name = copy_stem.casefold()
    shorter, longer = sorted(
        [
            source_name,
            copy_name,
        ],
        key=len,
    )
    extends = longer != shorter and longer.startswith(shorter)
    is_extended = extends and longer[len(shorter)] in COPY_SEPARATORS
    is_copy = bool(shorter) and (longer == shorter or is_extended)

    return is_copy


def _namesakes(
    source: pathlib.Path,
    notes: list[library.LibraryFile],
) -> list[library.LibraryFile]:
    """
    At most three notes whose name — for a book, its folder's — has the source's first author and
    year and shares at least one word of its title, those sharing the most first.
    """
    source_words = library.words(source.stem)
    source_key = _author_and_year(source_words)

    if source_key is None:

        return []

    title_words = _title_words(source_words)
    shared_counts = {
        note.path: len(title_words & _note_title_words(note))
        for note
        in notes
        if note.kind != library.CHAPTER
        and _note_author_and_year(note) == source_key
    }
    ranked = sorted(
        (
            -shared_counts[note.path],
            note.path.as_posix(),
            note,
        )
        for note
        in notes
        if shared_counts.get(note.path, 0) > 0
    )
    namesakes = [
        note
        for _, _, note
        in ranked[:MAXIMUM_NAMESAKES]
    ]

    return namesakes


def _note_author_and_year(
    note: library.LibraryFile,
) -> str | None:
    """
    A note's first author and year, from the name it is known by.
    """
    name_words = library.words(_note_name(note))
    author_year = _author_and_year(name_words)

    return author_year


def _note_name(
    note: library.LibraryFile,
) -> str:
    """
    The name a note is known by: a book's folder for its index, the file's own name otherwise.
    """
    name = note.path.parent.name if note.kind == library.BOOK_INDEX else note.path.stem

    return name


def _note_title_words(
    note: library.LibraryFile,
) -> set[str]:
    """
    The title words of the name a note is known by.
    """
    name_words = library.words(_note_name(note))
    title_words = _title_words(name_words)

    return title_words


def _notes_text(
    found: library.Library,
    notes: list[library.LibraryFile],
) -> str:
    """
    The notes that read a source, as one line: a book by its INDEX.md with its chapters counted,
    any other note by its path.
    """
    chapter_count = sum(
        1
        for note
        in notes
        if note.kind == library.CHAPTER
    )
    named = [
        library.relative_name(found, note.path)
        for note
        in notes
        if note.kind != library.CHAPTER
    ]
    chapters = [library.counted(chapter_count, 'chapter')] if chapter_count else []
    text = ', '.join(named + chapters)

    return text


def _ocr_partner(
    source: pathlib.Path,
) -> pathlib.Path:
    """
    The other half of a scan and its searchable copy: `X (OCR).pdf` for `X.pdf`, and `X.pdf` for
    `X (OCR).pdf`.
    """
    stem = source.stem

    if stem.endswith(OCR_SUFFIX):
        scan = source.with_name(f'{stem[:-len(OCR_SUFFIX)]}{source.suffix}')

        return scan

    searchable = source.with_name(f'{stem}{OCR_SUFFIX}{source.suffix}')

    return searchable


def _other_copies(
    source: pathlib.Path,
    notes: list[library.LibraryFile],
) -> list[library.LibraryFile]:
    """
    The notes — a book by its `INDEX.md`, never its chapters — whose `local_copy` is another copy of
    the source's name: an earlier or a later copy of one work.
    """
    copies = [
        note
        for note
        in notes
        if note.kind != library.CHAPTER
        and _is_other_copy(
            source.stem,
            _copy_stem(note),
        )
    ]

    return copies


def _source_status(
    source: pathlib.Path,
    notes_by_path: dict[str, list[library.LibraryFile]],
    notes: list[library.LibraryFile],
) -> SourceStatus:
    """
    What the library holds on one source: the notes naming it, else those naming its OCR partner,
    else none, with the namesakes.
    """
    direct = notes_by_path.get(library.comparable_path(source), [])
    partner = _ocr_partner(source)
    through_partner = [] if direct else notes_by_path.get(library.comparable_path(partner), [])
    namers = direct or through_partner
    copies = [] if namers else _other_copies(
        source,
        notes,
    )
    namesakes = [] if namers or copies else _namesakes(
        source,
        notes,
    )
    status = SourceStatus(
        copies=copies,
        namesakes=namesakes,
        notes=namers,
        path=source,
        read_through=partner if through_partner else None,
    )

    return status


def _status_lines(
    found: library.Library,
    status: SourceStatus,
    show_all: bool,
) -> list[str]:
    """
    The lines one source prints: an unread one always, with its namesakes; a read one with
    `show_all` only.
    """
    name = library.relative_name(
        found,
        status.path,
    )

    if not status.notes:
        lead_lines = [
            f'  {lead}'
            for lead
            in lead_texts(
                found,
                status,
            )
        ]
        unread_lines = [f'unread: {name}'] + lead_lines

        return unread_lines

    if not show_all:

        return []

    note_names = _notes_text(
        found,
        status.notes,
    )
    through = '' if status.read_through is None else ' through {}'.format(
        library.relative_name(found, status.read_through),
    )
    read_lines = [f'read{through}: {name} — {note_names}']

    return read_lines


def _title_words(
    name_words: list[str],
) -> set[str]:
    """
    The words of a name's title — after its first year, so never its author's — that can tell one
    work from another: no number, no word of two letters or fewer, none of the words every title
    shares.
    """
    year_positions = [
        position
        for position, word
        in enumerate(name_words)
        if YEAR.match(word)
    ]
    title_start = year_positions[0] + 1 if year_positions else len(name_words)
    distinctive = {
        word
        for word
        in name_words[title_start:]
        if len(word) > 2
        and not word.isdigit()
        and word not in TITLE_STOP_WORDS
    }

    return distinctive

if __name__ == '__main__':
    sys.exit(main())
