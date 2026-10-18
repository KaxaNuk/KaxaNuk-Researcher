"""
The checks `audit` makes on every run, made the same way every time: links, frontmatter, the index,
local copies on disk, each book's INDEX.md against its chapter files, concept pages, studies,
unread sources, and clippings older than their project's CHANGELOG.

    uv run --no-project python check_library.py                  the library in this folder
    uv run --no-project python check_library.py "D:/Research/Arya" --verbose

What it checks — each a kind of finding, printed under its name
    broken link       a link to a file that is not there
    link leaves       a link out of the library's own repository: into the home from a strategy, or
                      into another project
    cites an extract  a note, page or study that links into Extracts/ or names a path there; a page
                      or a study that links to a PDF
    orphan            a note or a page that no other file links to — a chapter is linked from its
                      book's INDEX.md, a paper or a book from the index
    index             at home, a note or a page that Knowledge/INDEX.md does not link, and a line of
                      it whose note is not there; in a strategy, a paper or a book's INDEX.md that
                      BIBLIOGRAPHY.md does not link — a book's chapters are listed in its INDEX.md
    book              a book's folder with no INDEX.md; a chapter file its table does not link; a
                      row marked read with no note, or a note with another status; a status outside
                      read, skimmed, skipped and to come; two chapter files of one number
    frontmatter       a note or a book's INDEX.md without source, citation, local_copy or read, or
                      with a field beyond those and tags; a read field that is only a date; a page
                      without type, updated or sources, or whose sources name a note not there
    duplicate         two notes, not chapters of one book, whose local_copy is the same file
    concept page      at home, a chapter note that no concept page names, in its sources or by a
                      link; a claim under a page's What the sources say that links no note
    study             at home, a study whose first line is not its state, in italics
    stray file        a markdown file where no note belongs: beside the index at the top of
                      Knowledge/, or deeper than a book's folder
    unread source     a source no note's local_copy names, as unread_sources.py finds it
    stale clipping    at home, a clipping of a project in RESEARCHER.md's projects table that states
                      a version older than the newest in the CHANGELOG.md at the project's path —
                      the only file of the project it opens
    missing copies    notes whose local_copy names a file that is not on this computer: one finding
                      with the count, since a fresh clone holds no PDF; --verbose lists them

What it leaves to `audit`: one source read twice under two paths, tags against the policy, an idea a
note leans on that nothing defines, contradictions, the installed copies of the skills, the agent
and the researcher's skill, and, in a strategy, the claims and the figures of OBJECTIVE.md and the
blueprints.

Exit codes: 0 no finding · 1 usage: the folder is not a library · 2 at least one finding.
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
import unread_sources  # noqa: E402 - the same.

# The kinds of finding, in the order the report prints them.
BOOK = 'book'
BROKEN_LINK = 'broken link'
CITES_EXTRACT = 'cites an extract'
CONCEPT_PAGE = 'concept page'
DUPLICATE = 'duplicate'
FRONTMATTER = 'frontmatter'
INDEX = 'index'
LINK_LEAVES = 'link leaves'
MISSING_COPIES = 'missing copies'
ORPHAN = 'orphan'
STALE_CLIPPING = 'stale clipping'
STRAY_FILE = 'stray file'
STUDY = 'study'
UNREAD_SOURCE = 'unread source'
FINDING_KINDS = [
    BROKEN_LINK,
    LINK_LEAVES,
    CITES_EXTRACT,
    ORPHAN,
    INDEX,
    BOOK,
    FRONTMATTER,
    DUPLICATE,
    CONCEPT_PAGE,
    STUDY,
    STRAY_FILE,
    UNREAD_SOURCE,
    STALE_CLIPPING,
    MISSING_COPIES,
]
# The fields a note or a book's INDEX.md carries, and a page's.
NOTE_FIELDS = [
    'source',
    'citation',
    'local_copy',
    'read',
]
NOTE_OPTIONAL_FIELDS = frozenset({
    'tags',
})
PAGE_FIELDS = [
    'type',
    'updated',
    'sources',
]
# The words a cell or a table holds that mean something to a check.
BOOK_STATUSES = frozenset({
    'read',
    'skimmed',
    'skipped',
    'to come',
})
NO_PATH = frozenset({
    '',
    '-',
    'none',
    '—',
})
PROJECT_STOP_WORDS = frozenset({
    'a',
    'an',
    'de',
    'el',
    'kaxanuk',
    'la',
    'of',
    'the',
})
# The markdown and the text the checks read.
CHANGELOG_VERSION = re.compile(r'^#{2,3}\s+\[?v?(\d+)\.(\d+)\.(\d+)\b')
CHAPTER_NUMBER = re.compile(r'^(\d+)_')
DATE_ONLY = re.compile(r'^\d{4}-\d{2}-\d{2}\.?$')
EXTRACTS_PATH = re.compile(r'(?<![\w/])(?:Bibliotheca/)?Extracts/')
HEADING = re.compile(r'^#{1,2}\s')
INLINE_LIST = re.compile(r'^\[(.*)\]$')
LIST_ITEM = re.compile(r'^[-*+]\s+')
MARKDOWN_LINK_TEXT = re.compile(r'\[([^\]]*)\]\([^)]*\)')
NAMED_VERSION = re.compile(
    r'(?:version|versión|release|\bv)\s*(\d+)\.(\d+)\.(\d+)(?![.\d])',
    re.IGNORECASE,
)
SOURCES_SAY_HEADING = re.compile(
    r'^##\s+What the sources say\s*$',
    re.IGNORECASE,
)
TABLE_ROW = re.compile(r'^\s*\|')
TABLE_SEPARATOR = re.compile(r'^\s*\|?\s*:?-{3,}')
VERSION = re.compile(r'(?<![\w.])(\d+)\.(\d+)\.(\d+)(?![.\d])')


@dataclasses.dataclass(frozen=True)
class BookRow:
    """
    One row of a book's table: its line in INDEX.md, its status, and the files its links reach.
    """
    line: int
    linked: list[str]
    status: str


@dataclasses.dataclass(frozen=True)
class Finding:
    """
    One finding: its kind, the file it is in, the line when there is one, and what is wrong.
    """
    kind: str
    line: int | None
    message: str
    path: str


@dataclasses.dataclass(frozen=True)
class Project:
    """
    A row of RESEARCHER.md's projects table with a folder on this computer: its name, its folder,
    and the newest version its CHANGELOG.md gives.
    """
    folder: pathlib.Path
    name: str
    newest: tuple[int, int, int]


@dataclasses.dataclass(frozen=True)
class ProjectRow:
    """
    A row of RESEARCHER.md's projects table as written: its first cell and its Path cell.
    """
    name: str
    path_text: str


def book_findings(
    found: library.Library,
    files: list[library.LibraryFile],
) -> list[Finding]:
    """
    Each book's folder against its INDEX.md: the index there, every chapter file in its table, every
    row's status and note, and one file per chapter number.
    """
    chapters_by_folder = collections.defaultdict(list)

    for chapter in files:
        if chapter.kind == library.CHAPTER:
            chapters_by_folder[chapter.path.parent].append(chapter)

    indexes = {
        book.path.parent: book
        for book
        in files
        if book.kind == library.BOOK_INDEX
    }
    folder_set = set(chapters_by_folder) | set(indexes)
    findings = [
        finding
        for folder
        in sorted(folder_set)
        for finding
        in _book_folder_findings(
            found,
            indexes.get(folder),
            chapters_by_folder[folder],
            folder,
        )
    ]

    return findings


def check_library(
    found: library.Library,
    files: list[library.LibraryFile],
    verbose: bool,
) -> list[Finding]:
    """
    Every check, in the order the report prints them.
    """
    findings = [
        *link_findings(
            found,
            files,
        ),
        *orphan_findings(
            found,
            files,
        ),
        *index_findings(
            found,
            files,
        ),
        *book_findings(
            found,
            files,
        ),
        *frontmatter_findings(
            found,
            files,
        ),
        *duplicate_findings(
            found,
            files,
        ),
        *concept_page_findings(
            found,
            files,
        ),
        *study_findings(
            found,
            files,
        ),
        *stray_findings(
            found,
            files,
        ),
        *unread_findings(
            found,
            files,
        ),
        *stale_clipping_findings(
            found,
            files,
        ),
        *missing_copy_findings(
            found,
            files,
            verbose,
        ),
    ]

    return findings


def concept_page_findings(
    found: library.Library,
    files: list[library.LibraryFile],
) -> list[Finding]:
    """
    At home: each chapter note no concept page names, and each claim of a concept page that links
    no note.
    """
    if found.kind != 'home':

        return []

    pages = [
        page
        for page
        in files
        if page.kind == library.CONCEPT
    ]
    named = {
        library.comparable_path(named_path)
        for page
        in pages
        for named_path
        in _page_named_paths(
            found,
            page,
        )
    }
    unnamed_chapters = [
        Finding(
            kind=CONCEPT_PAGE,
            line=None,
            message='a chapter note no concept page names, in its sources or by a link',
            path=library.relative_name(found, chapter.path),
        )
        for chapter
        in files
        if chapter.kind == library.CHAPTER
        and library.comparable_path(chapter.path) not in named
    ]
    unsourced_claims = [
        Finding(
            kind=CONCEPT_PAGE,
            line=line_number,
            message='a claim under What the sources say that links no note',
            path=library.relative_name(found, page.path),
        )
        for page
        in pages
        for line_number
        in _unsourced_claim_lines(page)
    ]
    findings = unnamed_chapters + unsourced_claims

    return findings


def duplicate_findings(
    found: library.Library,
    files: list[library.LibraryFile],
) -> list[Finding]:
    """
    Two notes, not chapters of one book, whose `local_copy` is the same file.
    """
    readers_by_copy = collections.defaultdict(set)

    for note in files:
        copy = library.local_copy_path(
            found,
            note,
        ) if note.kind in library.NOTE_KINDS else None

        if copy is not None:
            copy_key = library.comparable_path(copy)
            readers_by_copy[copy_key].add(_reading_unit(note))

    findings = [
        Finding(
            kind=DUPLICATE,
            line=None,
            message=f'{len(names)} notes read the same file: {", ".join(names)}',
            path=names[0],
        )
        for readers
        in readers_by_copy.values()
        if len(readers) > 1
        for names
        in [_sorted_names(found, readers)]
    ]

    return findings


def frontmatter_findings(
    found: library.Library,
    files: list[library.LibraryFile],
) -> list[Finding]:
    """
    The fields of every note, book index and page: the ones it lacks, the ones it should not carry,
    a `read` that is only a date, and a page's sources that are not there.
    """
    findings = [
        finding
        for checked
        in files
        for finding
        in _file_frontmatter_findings(
            found,
            checked,
        )
    ]

    return findings


def index_findings(
    found: library.Library,
    files: list[library.LibraryFile],
) -> list[Finding]:
    """
    The notes and pages the library's index does not link: at home every note, chapter and page; in
    a strategy every paper and book, whose chapters its INDEX.md lists.
    """
    index_name = library.relative_name(
        found,
        found.index,
    )
    index_files = [
        index_file
        for index_file
        in files
        if index_file.kind == library.INDEX
    ]

    if not index_files:
        no_index = Finding(
            kind=INDEX,
            line=None,
            message='the library has no index',
            path=index_name,
        )

        return [no_index]

    indexed = _linked_paths(index_files[0])
    strategy_kinds = {
        library.BOOK_INDEX,
        library.PAPER,
    }
    expected_kinds = library.NOTE_KINDS | library.PAGE_KINDS if found.kind == 'home' else strategy_kinds
    findings = [
        Finding(
            kind=INDEX,
            line=None,
            message=f'not linked from {index_name}',
            path=library.relative_name(found, unindexed.path),
        )
        for unindexed
        in files
        if unindexed.kind in expected_kinds
        and library.comparable_path(unindexed.path) not in indexed
    ]

    return findings


def link_findings(
    found: library.Library,
    files: list[library.LibraryFile],
) -> list[Finding]:
    """
    Every link that is broken, leaves the repository, or reaches an extract or a PDF it should not,
    and every path into `Extracts/` a note, page or study names.
    """
    link_problems = [
        finding
        for linking
        in files
        for link
        in library.markdown_links(linking.text)
        if library.is_local_target(link.target)
        for finding
        in _link_problems(
            found,
            linking,
            link,
        )
    ]
    linked_lines = {
        (finding.path, finding.line)
        for finding
        in link_problems
        if finding.kind == CITES_EXTRACT
    }
    citing_kinds = library.NOTE_KINDS | library.PAGE_KINDS | {library.STUDY}
    named_extracts = [
        Finding(
            kind=CITES_EXTRACT,
            line=line_number,
            message='names a path in Extracts/: notes cite the source and its pages',
            path=name,
        )
        for naming
        in files
        if naming.kind in citing_kinds
        for name
        in [library.relative_name(found, naming.path)]
        for line_number
        in _extract_path_lines(naming)
        if (name, line_number) not in linked_lines
    ]
    findings = link_problems + named_extracts

    return findings


def main(
    arguments: list[str] | None = None,
) -> int:
    """
    Parse the command line, find the library, check it, and print the findings by kind.
    """
    library.configure_console()
    parsed = _build_parser().parse_args(arguments)
    found = library.find_library(pathlib.Path(parsed.folder))

    if found is None:
        problem = f'not a library: {parsed.folder} holds neither RESEARCHER.md nor Bibliotheca/'
        print(problem, file=sys.stderr)

        return 1

    files = library.library_files(found)
    findings = check_library(
        found,
        files,
        parsed.verbose,
    )
    print_report(
        found,
        files,
        findings,
    )
    exit_code = 2 if findings else 0

    return exit_code


def missing_copy_findings(
    found: library.Library,
    files: list[library.LibraryFile],
    verbose: bool,
) -> list[Finding]:
    """
    The notes whose `local_copy` names a file not on this computer, as one finding with their count;
    with `verbose`, one more finding per note.
    """
    missing = [
        note
        for note
        in files
        if note.kind in library.NOTE_KINDS
        and _names_missing_copy(
            found,
            note,
        )
    ]

    if not missing:

        return []

    missing_files = {
        library.comparable_path(library.local_copy_path(found, note))
        for note
        in missing
    }
    summary_message = ' '.join([
        'local_copy not on this computer:',
        f'{library.counted(len(missing), "note")},',
        f'{library.counted(len(missing_files), "file")};',
        'a fresh clone holds no PDF',
    ])
    summary = Finding(
        kind=MISSING_COPIES,
        line=None,
        message=summary_message,
        path=library.relative_name(found, found.notes_root),
    )
    listed = [
        Finding(
            kind=MISSING_COPIES,
            line=None,
            message=f'local_copy {library.field_value(note.front, "local_copy")} is not there',
            path=library.relative_name(found, note.path),
        )
        for note
        in missing
    ] if verbose else []
    findings = [summary] + listed

    return findings


def orphan_findings(
    found: library.Library,
    files: list[library.LibraryFile],
) -> list[Finding]:
    """
    The notes and pages no other file of the library links to.
    """
    linked_by_others = {
        linked_path
        for linking
        in files
        for linked_path
        in _linked_paths(linking)
        if linked_path != library.comparable_path(linking.path)
    }
    linkable_kinds = library.NOTE_KINDS | library.PAGE_KINDS
    findings = [
        Finding(
            kind=ORPHAN,
            line=None,
            message='nothing else in the library links to it',
            path=library.relative_name(found, orphan.path),
        )
        for orphan
        in files
        if orphan.kind in linkable_kinds
        and library.comparable_path(orphan.path) not in linked_by_others
    ]

    return findings


def print_report(
    found: library.Library,
    files: list[library.LibraryFile],
    findings: list[Finding],
) -> None:
    """
    The summary line, the findings under each kind's name, the kinds with none, and the total.
    """
    counts = collections.Counter(
        checked.kind
        for checked
        in files
    )
    note_count = sum(
        counts[kind]
        for kind
        in library.NOTE_KINDS
    )
    page_count = sum(
        counts[kind]
        for kind
        in library.PAGE_KINDS
    )
    source_count = len(library.source_files(found))
    summary = ', '.join([
        library.counted(note_count, 'note'),
        library.counted(page_count, 'page'),
        library.counted(counts[library.STUDY], 'study file'),
        library.counted(source_count, 'source'),
    ])
    print(f'{found.kind} {found.root.as_posix()}: {summary}')
    by_kind = collections.defaultdict(list)

    for finding in findings:
        by_kind[finding.kind].append(finding)

    for kind in FINDING_KINDS:
        if by_kind[kind]:
            print(f'{kind} — {len(by_kind[kind])}')

        for finding in by_kind[kind]:
            print(_finding_line(finding))

    clean_kinds = ', '.join(
        kind
        for kind
        in FINDING_KINDS
        if not by_kind[kind]
    )
    clean_line = f'none of: {clean_kinds}' if clean_kinds else 'a finding of every kind'
    print(clean_line)
    total = library.counted(
        len(findings),
        'finding',
    )
    print(total)


def projects_on_disk(
    found: library.Library,
) -> list[Project]:
    """
    The rows of RESEARCHER.md's projects table — the table with a Path column — whose path is a
    folder holding a CHANGELOG.md with at least one version.
    """
    researcher_text = (found.root / 'RESEARCHER.md').read_text(
        encoding='utf-8-sig',
        errors='replace',
    )
    rows = _path_table_rows(researcher_text.splitlines())
    projects = [
        project
        for row
        in rows
        for project
        in [_project(found, row)]
        if project is not None
    ]

    return projects


def stale_clipping_findings(
    found: library.Library,
    files: list[library.LibraryFile],
) -> list[Finding]:
    """
    At home, each clipping of a project in RESEARCHER.md's projects table whose stated version is
    older than the newest one in the project's CHANGELOG.md.
    """
    if found.kind != 'home':

        return []

    projects = projects_on_disk(found)
    findings = [
        Finding(
            kind=STALE_CLIPPING,
            line=None,
            message=_stale_message(
                project,
                stated,
            ),
            path=library.relative_name(found, clipping.path),
        )
        for clipping
        in files
        if clipping.kind == library.PAPER
        for project
        in projects
        if _describes(
            clipping,
            project,
        )
        for stated
        in [_stated_version(clipping)]
        if stated is not None and stated < project.newest
    ]

    return findings


def stray_findings(
    found: library.Library,
    files: list[library.LibraryFile],
) -> list[Finding]:
    """
    The markdown files where no note belongs.
    """
    findings = [
        Finding(
            kind=STRAY_FILE,
            line=None,
            message='a markdown file where no note belongs: beside the index, or deeper than a book',
            path=library.relative_name(found, stray.path),
        )
        for stray
        in files
        if stray.kind == library.STRAY
    ]

    return findings


def study_findings(
    found: library.Library,
    files: list[library.LibraryFile],
) -> list[Finding]:
    """
    At home, each study — `Studies/<name>.md`, or a study folder's `README.md` — whose first line
    is not its state in italics.
    """
    studies_root = found.root / 'Studies'
    findings = [
        Finding(
            kind=STUDY,
            line=None,
            message='its first line is not its state, in italics: idea, active, parked, closed or moved to',
            path=library.relative_name(found, study.path),
        )
        for study
        in files
        if study.kind == library.STUDY
        and _is_study_file(
            study.path,
            studies_root,
        )
        and not _opens_with_state(study)
    ]

    return findings


def unread_findings(
    found: library.Library,
    files: list[library.LibraryFile],
) -> list[Finding]:
    """
    Each source no note's `local_copy` names, with the namesakes `unread_sources.py` finds.
    """
    report = unread_sources.unread_report(
        found,
        files,
    )
    findings = [
        Finding(
            kind=UNREAD_SOURCE,
            line=None,
            message=_unread_message(
                found,
                status,
            ),
            path=library.relative_name(found, status.path),
        )
        for status
        in report.unread
    ]

    return findings


def _book_folder_findings(
    found: library.Library,
    book_index: library.LibraryFile | None,
    chapters: list[library.LibraryFile],
    folder: pathlib.Path,
) -> list[Finding]:
    """
    One book's folder: its INDEX.md, its table's rows and statuses, and its chapter files.
    """
    folder_name = library.relative_name(
        found,
        folder,
    )

    if book_index is None:
        no_index = Finding(
            kind=BOOK,
            line=None,
            message='a book folder with no INDEX.md',
            path=folder_name,
        )

        return [no_index]

    index_name = library.relative_name(
        found,
        book_index.path,
    )
    rows = _status_rows(book_index)

    if not rows:
        no_table = Finding(
            kind=BOOK,
            line=None,
            message='INDEX.md has no table with a Status column',
            path=index_name,
        )

        return [no_table]

    chapter_paths = {
        library.comparable_path(chapter.path): chapter
        for chapter
        in chapters
    }
    linked_chapters = {
        linked
        for row
        in rows
        for linked
        in row.linked
        if linked in chapter_paths
    }
    row_findings = [
        Finding(
            kind=BOOK,
            line=row.line,
            message=message,
            path=index_name,
        )
        for row
        in rows
        for message
        in _row_problems(
            row,
            chapter_paths,
        )
    ]
    unknown_statuses = sorted({
        row.status
        for row
        in rows
        if row.status not in BOOK_STATUSES
    })
    unknown_text = ', '.join(
        repr(status)
        for status
        in unknown_statuses
    )
    status_findings = [
        Finding(
            kind=BOOK,
            line=None,
            message=f'statuses outside read, skimmed, skipped and to come: {unknown_text}',
            path=index_name,
        ),
    ] if unknown_statuses else []
    unlisted = [
        Finding(
            kind=BOOK,
            line=None,
            message=f'a chapter file its INDEX.md table does not link: {chapter.path.name}',
            path=index_name,
        )
        for path_key, chapter
        in sorted(chapter_paths.items())
        if path_key not in linked_chapters
    ]
    numbers = collections.Counter(
        number_match.group(1)
        for chapter
        in chapters
        for number_match
        in [CHAPTER_NUMBER.match(chapter.path.name)]
        if number_match is not None
    )
    doubled = [
        Finding(
            kind=BOOK,
            line=None,
            message=f'{count} chapter files numbered {number}',
            path=folder_name,
        )
        for number, count
        in sorted(numbers.items())
        if count > 1
    ]
    findings = row_findings + status_findings + unlisted + doubled

    return findings


def _build_parser() -> library.CommandLineParser:
    """
    The command line: the library's folder, and whether to list each missing copy.
    """
    parser = library.CommandLineParser(
        prog='check_library.py',
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
        '--verbose',
        action='store_true',
        help='list each note whose local_copy is not on this computer',
    )

    return parser


def _cell_name(
    cell: str,
) -> str:
    """
    A cell's plain text, case folded.
    """
    plain = _plain(cell)
    name = plain.casefold()

    return name


def _cells(
    row: str,
) -> list[str]:
    """
    A table row's cells, their spaces stripped.
    """
    stripped = row.strip()
    inner = stripped.strip('|')
    cells = [
        cell.strip()
        for cell
        in inner.split('|')
    ]

    return cells


def _describes(
    clipping: library.LibraryFile,
    project: Project,
) -> bool:
    """
    Whether a note describes a project: every distinctive word of the project's name, or of its
    folder's, is in the note's file name, its title or its citation.
    """
    citation = library.field_value(
        clipping.front,
        'citation',
    )
    note_text = ' '.join([
        clipping.path.stem,
        _title(clipping),
        citation,
    ])
    note_words = set(library.words(note_text))
    name_keys = [
        _distinctive_words(project.name),
        _distinctive_words(project.folder.name),
    ]
    describes = any(
        key and key <= note_words
        for key
        in name_keys
    )

    return describes


def _distinctive_words(
    name: str,
) -> frozenset[str]:
    """
    A project's name as the words that tell it from another: `KaxaNuk Backtest Engine` gives
    `backtest` and `engine`.
    """
    distinctive = frozenset(
        word
        for word
        in library.words(name)
        if word not in PROJECT_STOP_WORDS
    )

    return distinctive


def _ends_item(
    line: str,
) -> bool:
    """
    Whether a line ends the list item above it: a blank line, or a callout or a quote.
    """
    stripped = line.strip()
    ends = not stripped or stripped.startswith('>')

    return ends


def _extract_path_lines(
    naming: library.LibraryFile,
) -> list[int]:
    """
    The numbers of the lines that name a path into `Extracts/`.
    """
    line_numbers = [
        index + 1
        for index, line
        in enumerate(naming.text.splitlines())
        if EXTRACTS_PATH.search(line)
    ]

    return line_numbers


def _file_frontmatter_findings(
    found: library.Library,
    checked: library.LibraryFile,
) -> list[Finding]:
    """
    One file's frontmatter findings, by its kind.
    """
    name = library.relative_name(
        found,
        checked.path,
    )

    if checked.kind in library.NOTE_KINDS:
        messages = _note_field_problems(checked.front)
    elif checked.kind in library.PAGE_KINDS:
        messages = _page_field_problems(
            found,
            checked,
        )
    else:
        messages = []

    findings = [
        Finding(
            kind=FRONTMATTER,
            line=None,
            message=message,
            path=name,
        )
        for message
        in messages
    ]

    return findings


def _finding_line(
    finding: Finding,
) -> str:
    """
    One finding as the report prints it: its file, its line when there is one, and what is wrong.
    """
    where = finding.path if finding.line is None else f'{finding.path}:{finding.line}'
    line = f'  {where}: {finding.message}'

    return line


def _header_names(
    row: str,
) -> list[str]:
    """
    A table header's cells as names: plain text, case folded.
    """
    names = [
        _cell_name(cell)
        for cell
        in _cells(row)
    ]

    return names


def _is_inside(
    path: pathlib.Path,
    root: pathlib.Path,
) -> bool:
    """
    Whether a path, resolved, is inside a folder.
    """
    resolved = path.resolve()

    try:
        resolved.relative_to(root)
    except ValueError:

        return False

    return True


def _is_study_file(
    path: pathlib.Path,
    studies_root: pathlib.Path,
) -> bool:
    """
    Whether a file under `Studies/` is a study itself: a file at its top, or a study folder's
    `README.md`.
    """
    parts = path.relative_to(studies_root).parts
    is_study = len(parts) == 1 or (len(parts) == 2 and parts[1] == 'README.md')

    return is_study


def _item_lines(
    lines: list[str],
    start: int,
    end: int,
) -> list[str]:
    """
    A list item's own lines: its first, and those after it up to a blank line, a callout or the
    next item.
    """
    stop = next(
        (
            position
            for position
            in range(start + 1, end)
            if _ends_item(lines[position])
        ),
        end,
    )
    item = lines[start:stop]

    return item


def _link_problems(
    found: library.Library,
    linking: library.LibraryFile,
    link: library.Link,
) -> list[Finding]:
    """
    What is wrong with one local link: into `Extracts/` or to a PDF where that is not allowed, not
    there, or out of the repository.
    """
    name = library.relative_name(
        found,
        linking.path,
    )
    target_path = library.link_path(
        linking.path,
        link.target,
    )
    cleaned = library.clean_target(link.target)
    forward = cleaned.replace('\\', '/')
    target_parts = pathlib.PurePosixPath(forward).parts
    record_kinds = {
        library.INDEX,
        library.LOG,
    }
    into_extracts = 'Extracts' in target_parts and linking.kind not in record_kinds
    pdf_kinds = library.PAGE_KINDS | {library.STUDY}
    to_pdf = forward.casefold().endswith('.pdf') and linking.kind in pdf_kinds
    exists = target_path.exists()
    leaves = exists and not _is_inside(
        target_path,
        found.root,
    )
    broken_kind = INDEX if linking.kind == library.INDEX else BROKEN_LINK
    candidates = [
        Finding(
            kind=CITES_EXTRACT,
            line=link.line,
            message=f'links {cleaned}: notes cite the source and its pages, never an extract',
            path=name,
        ) if into_extracts else None,
        Finding(
            kind=CITES_EXTRACT,
            line=link.line,
            message=f'links {cleaned}: a page or a study cites notes, never a PDF',
            path=name,
        ) if to_pdf else None,
        Finding(
            kind=broken_kind,
            line=link.line,
            message=f'links {cleaned}, which is not there',
            path=name,
        ) if not exists else None,
        Finding(
            kind=LINK_LEAVES,
            line=link.line,
            message=f'links {cleaned}, outside this repository',
            path=name,
        ) if leaves else None,
    ]
    problems = [
        candidate
        for candidate
        in candidates
        if candidate is not None
    ]

    return problems


def _linked_paths(
    linking: library.LibraryFile,
) -> frozenset[str]:
    """
    Every file a file's local links reach, as comparable paths.
    """
    linked = frozenset(
        library.comparable_path(library.link_path(linking.path, link.target))
        for link
        in library.markdown_links(linking.text)
        if library.is_local_target(link.target)
    )

    return linked


def _links_a_note(
    item_lines: list[str],
) -> bool:
    """
    Whether some lines link a markdown file of this computer, as a claim links its note.
    """
    item_text = '\n'.join(item_lines)
    targets = [
        library.clean_target(link.target)
        for link
        in library.markdown_links(item_text)
        if library.is_local_target(link.target)
    ]
    links_note = any(
        target.casefold().endswith('.md')
        for target
        in targets
    )

    return links_note


def _names_missing_copy(
    found: library.Library,
    note: library.LibraryFile,
) -> bool:
    """
    Whether a note's `local_copy` names a file that is not on this computer.
    """
    copy = library.local_copy_path(
        found,
        note,
    )
    missing = copy is not None and not copy.is_file()

    return missing


def _note_field_problems(
    front: library.Frontmatter,
) -> list[str]:
    """
    A note's or a book index's field problems: missing, extra, and a `read` that is only a date.
    """
    if not front.fields:

        return ['no frontmatter: it needs source, citation, local_copy and read']

    missing = [
        field
        for field
        in NOTE_FIELDS
        if field not in front.fields
    ]
    extra = sorted(
        field
        for field
        in front.fields
        if field not in NOTE_FIELDS and field not in NOTE_OPTIONAL_FIELDS
    )
    read_value = library.field_value(
        front,
        'read',
    )
    candidates = [
        f'missing {", ".join(missing)}' if missing else None,
        f'carries {", ".join(extra)}, beyond source, citation, local_copy, read and tags' if extra else None,
        f'read is only a date, {read_value}: it says what was read' if DATE_ONLY.match(read_value) else None,
    ]
    problems = [
        candidate
        for candidate
        in candidates
        if candidate is not None
    ]

    return problems


def _opens_with_state(
    study: library.LibraryFile,
) -> bool:
    """
    Whether a study's first line, after any frontmatter, is in italics, as its state line is.
    """
    body = study.text.splitlines()[study.front.body_start:]
    first_line = next(
        (
            line.strip()
            for line
            in body
            if line.strip()
        ),
        '',
    )
    italic = any(
        _wrapped_in(
            first_line,
            mark,
        )
        for mark
        in ('*', '_')
    ) and not first_line.startswith('**')

    return italic


def _page_field_problems(
    found: library.Library,
    page: library.LibraryFile,
) -> list[str]:
    """
    A page's field problems: missing type, updated or sources, and a source that is not there.
    """
    missing = [
        field
        for field
        in PAGE_FIELDS
        if field not in page.front.fields
    ]
    unfound = [
        source_name
        for source_name
        in _page_sources(page.front)
        if not _page_source_path(
            found,
            page,
            source_name,
        ).is_file()
    ]
    candidates = [
        f'missing {", ".join(missing)}' if missing else None,
        f'sources names notes that are not there: {", ".join(unfound)}' if unfound else None,
    ]
    problems = [
        candidate
        for candidate
        in candidates
        if candidate is not None
    ]

    return problems


def _page_named_paths(
    found: library.Library,
    page: library.LibraryFile,
) -> list[pathlib.Path]:
    """
    Every note a page names: in its `sources`, and by its links.
    """
    from_sources = [
        _page_source_path(
            found,
            page,
            source_name,
        )
        for source_name
        in _page_sources(page.front)
    ]
    from_links = [
        library.link_path(
            page.path,
            link.target,
        )
        for link
        in library.markdown_links(page.text)
        if library.is_local_target(link.target)
    ]
    named = from_sources + from_links

    return named


def _page_source_path(
    found: library.Library,
    page: library.LibraryFile,
    source_name: str,
) -> pathlib.Path:
    """
    The note a page's `sources` entry names: from the page's own folder, as the convention writes
    it, or else from `Knowledge/`.
    """
    beside = page.path.parent / source_name
    from_root = found.notes_root / source_name
    path = beside if beside.is_file() or not from_root.is_file() else from_root

    return path


def _page_sources(
    front: library.Frontmatter,
) -> list[str]:
    """
    A page's `sources`, written as a block list or as an inline one.
    """
    sources_text = library.field_value(
        front,
        'sources',
    )
    inline = INLINE_LIST.match(sources_text)
    inline_items = [
        library.unquoted(item)
        for item
        in inline.group(1).split(',')
        if item.strip()
    ] if inline is not None else []
    sources = front.items.get('sources', []) + inline_items

    return sources


def _path_table_rows(
    lines: list[str],
) -> list[ProjectRow]:
    """
    The rows of the first table with a Path column, each as its first cell and its path, the
    markdown taken out.
    """
    table_starts = [
        index
        for index, line
        in enumerate(lines)
        if TABLE_ROW.match(line)
        and (index == 0 or not TABLE_ROW.match(lines[index - 1]))
    ]
    tables = [
        _table_lines(
            lines,
            start,
        )
        for start
        in table_starts
    ]
    with_path = [
        table
        for table
        in tables
        if 'path' in _header_names(table[0])
    ]

    if not with_path:

        return []

    header = _header_names(with_path[0][0])
    path_column = header.index('path')
    rows = [
        ProjectRow(
            name=_plain(cells[0]),
            path_text=_plain(cells[path_column]),
        )
        for row
        in with_path[0][1:]
        if not TABLE_SEPARATOR.match(row)
        for cells
        in [_cells(row)]
        if len(cells) > path_column
    ]

    return rows


def _plain(
    cell: str,
) -> str:
    """
    A cell's text without its markdown: a link's text kept, emphasis, code marks and quotes dropped.
    """
    without_links = MARKDOWN_LINK_TEXT.sub(
        r'\1',
        cell,
    )
    without_code = without_links.replace('`', '')
    without_emphasis = without_code.replace('*', '')
    plain = library.unquoted(without_emphasis)

    return plain


def _project(
    found: library.Library,
    row: ProjectRow,
) -> Project | None:
    """
    A projects-table row as a project on disk, or None when its path is not a folder holding a
    CHANGELOG.md with a version in it.
    """
    if row.path_text.casefold() in NO_PATH:

        return None

    given_path = pathlib.Path(row.path_text)
    given = given_path.expanduser()
    folder = given if given.is_absolute() else found.root / given
    changelog = folder / 'CHANGELOG.md'

    if not changelog.is_file():

        return None

    changelog_text = changelog.read_text(
        encoding='utf-8-sig',
        errors='replace',
    )
    versions = [
        _version_numbers(version_match)
        for line
        in changelog_text.splitlines()
        for version_match
        in [CHANGELOG_VERSION.match(line)]
        if version_match is not None
    ]

    if not versions:

        return None

    project = Project(
        folder=folder,
        name=row.name,
        newest=max(versions),
    )

    return project


def _reading_unit(
    note: library.LibraryFile,
) -> pathlib.Path:
    """
    What a note belongs to when two notes read one file: a book's folder for its index and its
    chapters, the note itself otherwise.
    """
    book_kinds = {
        library.BOOK_INDEX,
        library.CHAPTER,
    }
    unit = note.path.parent if note.kind in book_kinds else note.path

    return unit


def _row_links(
    book_index: library.LibraryFile,
    row: str,
) -> list[str]:
    """
    The files a table row's local links reach, as comparable paths.
    """
    linked = [
        library.comparable_path(library.link_path(book_index.path, link.target))
        for link
        in library.markdown_links(row)
        if library.is_local_target(link.target)
    ]

    return linked


def _row_problems(
    row: BookRow,
    chapter_paths: dict[str, library.LibraryFile],
) -> list[str]:
    """
    What is wrong with one row of a book's table: marked read with no note, or a note with another
    status.
    """
    links_chapter = any(
        linked in chapter_paths
        for linked
        in row.linked
    )
    unlinked_read = row.status == 'read' and not row.linked
    linked_unread = links_chapter and row.status != 'read'
    candidates = [
        'a row marked read that links no note' if unlinked_read else None,
        f'a row that links a note but is marked {row.status!r}' if linked_unread else None,
    ]
    problems = [
        candidate
        for candidate
        in candidates
        if candidate is not None
    ]

    return problems


def _sorted_names(
    found: library.Library,
    paths: set[pathlib.Path],
) -> list[str]:
    """
    Paths as the report prints them, sorted.
    """
    names = sorted(
        library.relative_name(found, path)
        for path
        in paths
    )

    return names


def _stale_message(
    project: Project,
    stated: tuple[int, int, int],
) -> str:
    """
    What a stale clipping's finding says: the version it describes, the newest one, and the fix.
    """
    changelog = (project.folder / 'CHANGELOG.md').as_posix()
    message = ' '.join([
        f'describes {project.name} {_version_text(stated)};',
        f'{changelog} is at {_version_text(project.newest)}:',
        'bring its new README and CHANGELOG in as clippings, then read them',
    ])

    return message


def _stated_version(
    clipping: library.LibraryFile,
) -> tuple[int, int, int] | None:
    """
    The version a clipping says it read: the one its citation or its title names after *version*,
    *release* or *v*, else the newest its citation names; None when they name none.
    """
    citation = library.field_value(
        clipping.front,
        'citation',
    )
    stated_text = f'{citation} {_title(clipping)}'
    named = [
        _version_numbers(version_match)
        for version_match
        in NAMED_VERSION.finditer(stated_text)
    ]
    bare = [
        _version_numbers(version_match)
        for version_match
        in VERSION.finditer(citation)
    ]
    stated = named[0] if named else max(bare, default=None)

    return stated


def _status_rows(
    book_index: library.LibraryFile,
) -> list[BookRow]:
    """
    The rows of a book's table — the first with a Status column — each with its line, its status,
    and the files its links reach.
    """
    lines = book_index.text.splitlines()
    header_positions = [
        index
        for index, line
        in enumerate(lines)
        if TABLE_ROW.match(line)
        and 'status' in _header_names(line)
    ]

    if not header_positions:

        return []

    header_position = header_positions[0]
    header = _header_names(lines[header_position])
    status_column = header.index('status')
    table = _table_lines(
        lines,
        header_position + 1,
    )
    rows = [
        BookRow(
            line=header_position + offset + 2,
            linked=_row_links(
                book_index,
                row,
            ),
            status=_cell_name(cells[status_column]) if len(cells) > status_column else '',
        )
        for offset, row
        in enumerate(table)
        if not TABLE_SEPARATOR.match(row)
        for cells
        in [_cells(row)]
    ]

    return rows


def _table_lines(
    lines: list[str],
    start: int,
) -> list[str]:
    """
    The lines of the table that starts at a line, up to the first that is not a row.
    """
    end = next(
        (
            position
            for position
            in range(start, len(lines))
            if not TABLE_ROW.match(lines[position])
        ),
        len(lines),
    )
    table = lines[start:end]

    return table


def _title(
    note: library.LibraryFile,
) -> str:
    """
    A note's title: its first heading of level one after the frontmatter, or empty.
    """
    body = note.text.splitlines()[note.front.body_start:]
    title = next(
        (
            line
            for line
            in body
            if line.startswith('# ')
        ),
        '',
    )

    return title


def _unread_message(
    found: library.Library,
    status: unread_sources.SourceStatus,
) -> str:
    """
    What an unread source's finding says: that no note names it, and any namesake.
    """
    namesake_texts = [
        ' '.join([
            f'{namesake.kind} of the same first author and year,',
            f'{library.relative_name(found, namesake.path)}, has local_copy',
            library.field_value(namesake.front, 'local_copy') or 'missing',
        ])
        for namesake
        in status.namesakes
    ]
    unread_text = 'no note names it in local_copy'
    message = '; '.join([unread_text] + namesake_texts)

    return message


def _unsourced_claim_lines(
    page: library.LibraryFile,
) -> list[int]:
    """
    The lines of a page's claims — the list items under What the sources say — whose item links no
    note.
    """
    lines = page.text.splitlines()
    starts = [
        index
        for index, line
        in enumerate(lines)
        if SOURCES_SAY_HEADING.match(line)
    ]

    if not starts:

        return []

    section_end = next(
        (
            position
            for position
            in range(starts[0] + 1, len(lines))
            if HEADING.match(lines[position])
        ),
        len(lines),
    )
    item_starts = [
        index
        for index
        in range(starts[0] + 1, section_end)
        if LIST_ITEM.match(lines[index])
    ]
    item_ends = item_starts[1:] + [section_end]
    unsourced = [
        start + 1
        for start, end
        in zip(item_starts, item_ends)
        if not _links_a_note(_item_lines(
            lines,
            start,
            end,
        ))
    ]

    return unsourced


def _version_numbers(
    version_match: re.Match[str],
) -> tuple[int, int, int]:
    """
    A version's three numbers, from a match of its three groups.
    """
    numbers = tuple(
        int(part)
        for part
        in version_match.groups()
    )

    return numbers


def _version_text(
    version: tuple[int, int, int],
) -> str:
    """
    A version as it is written, `0.67.0`.
    """
    text = '.'.join(
        str(part)
        for part
        in version
    )

    return text


def _wrapped_in(
    text: str,
    mark: str,
) -> bool:
    """
    Whether a text opens and closes with a mark, with something between: `*idea, 2026-10-18*`.
    """
    is_long_enough = len(text) > 2
    opens_and_closes = text.startswith(mark) and text.endswith(mark)
    wrapped = is_long_enough and opens_and_closes

    return wrapped


if __name__ == '__main__':
    sys.exit(main())
