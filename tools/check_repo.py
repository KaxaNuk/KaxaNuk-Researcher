"""
Check this repository before a commit reaches `main`: the defects that have shipped before without an
error, found by a script so a person only reads what it says.

Run from the repository root:

    uv run --no-project python tools/check_repo.py

It reads the working tree.  Each check exists because what it looks for happened:

- **versions** — the package and each starting point declare one version in `apm.yml`, and it leads
  their `CHANGELOG.md`, their `pyproject.toml` and their `uv.lock` where they have one.  Two fields that
  always move together once did not.
- **headings** — every heading of a template document is in the example's copy, so the example keeps
  the template's structure.  The two lived on separate branches and drifted; the example's `README.md`
  is its strategy's own and is left out.
- **markers** — the example's markers open and close in order, each alone on its line at column 0,
  or a copy made with them in mind keeps or loses the wrong lines.  The sync tool strips no other
  form of a marker: an indented one would carry the worked strategy's lines into the template.
  A notebook's cells are checked one by one with the Markdown pair, which the sync tool strips
  inside them too.
- **section symbol** — never used; the word is "section".
- **descriptions** — a skill's `description`, folded as an agent reads it, within what APM accepts;
  one written in a form the check cannot read fails, so it is never skipped.
- **references** — the experiment documents and notebook `experiment-lifecycle` ships are what
  `tools/sync_investment_lab_references.py` makes from the worked example.  A skill that kept its own
  copies drifted from the template once.
- **template** — every file `tools/sync_investment_lab_references.py`'s `TEMPLATE_FILES` lists,
  the files inside the folders the template's README table names, is what the same tool makes
  from the worked example.  A new strategy used to bring them across one by one and strip them by
  hand.
- **path length** — no tracked path longer than Windows allows once installed under a home folder;
  a 130-character path once made `apm install -g` fail.

Exit code 0 when every check passes, 1 when any fails.
"""
import dataclasses
import json
import pathlib
import re
import subprocess
import sys

import sync_investment_lab_references

REPOSITORY_ROOT = pathlib.Path(__file__).resolve().parent.parent
# The package, then each starting point, by its folder; `.` is the package at the root.
RELEASE_FOLDERS = [
    '.',
    'examples/liquid-golden-cross',
    'templates/researcher',
    'templates/strategy',
]
EXAMPLE_FOLDER = 'examples/liquid-golden-cross'
TEMPLATE_FOLDER = 'templates/strategy'
# Documents of the template whose headings the example need not keep.
HEADING_EXCEPTIONS = {
    'README.md',
}
# What APM accepts in a skill's `description`, and the longest path this repository allows.
DESCRIPTION_LIMIT = 1024
PATH_LIMIT = 120
# The sync tool declares the markers, and matches them only as whole lines at column 0.
MARKERS = sync_investment_lab_references.EXAMPLE_MARKERS
# The kinds of file searched for the section symbol.
TEXT_SUFFIXES = (
    '.ipynb',
    '.md',
    '.py',
    '.toml',
    '.yml',
)
# Built from its code point so this file does not break the rule it checks.
SECTION_SYMBOL = chr(0x00A7)
APM_VERSION = re.compile(
    r'^version:\s*(\S+)',
    re.MULTILINE,
)
CHANGELOG_VERSION = re.compile(
    r'^## \[?(\d+\.\d+\.\d+)\]?',
    re.MULTILINE,
)
FOLDED_DESCRIPTION = re.compile(
    r'^description: >-?\n((?:[ \t]+\S.*\n)+)',
    re.MULTILINE,
)
HEADING = re.compile(
    r'^#{1,6} \S.*$',
    re.MULTILINE,
)
# A description written on its one line: not a block scalar, and not continued on the next line.
ONE_LINE_DESCRIPTION = re.compile(
    r'^description:[ \t]+([^>|\s].*)\n(?![ \t])',
    re.MULTILINE,
)
PYPROJECT_VERSION = re.compile(
    r'^version\s*=\s*"([^"]+)"',
    re.MULTILINE,
)
UV_LOCK_VERSION = re.compile(
    r'^\[\[package\]\]\nname = "[^"]+"\nversion = "([^"]+)"\nsource = \{ virtual = "\." \}',
    re.MULTILINE,
)


@dataclasses.dataclass(frozen=True)
class Finding:
    """
    One failed check: which, and where.
    """
    check: str
    message: str


def check_descriptions(
    root: pathlib.Path,
    files: list[str],
) -> list[Finding]:
    """
    Every skill's description readable by this check, and within the length APM accepts.
    """
    # A skill deleted from the working tree but still tracked is not read: it has nothing to check.
    tracked_manifests = [
        path
        for path
        in files
        if path.startswith('.apm/skills/') and path.endswith('/SKILL.md')
    ]
    manifests = [
        path
        for path
        in tracked_manifests
        if (root / path).is_file()
    ]
    texts = {
        path: _read(root / path)
        for path
        in manifests
    }
    descriptions = {
        path: folded_description(text)
        for path, text
        in texts.items()
    }
    too_long = [
        Finding(
            check='description',
            message=f'{path}: {len(description)} characters, over {DESCRIPTION_LIMIT}',
        )
        for path, description
        in descriptions.items()
        if len(description) > DESCRIPTION_LIMIT
    ]
    unreadable = [
        Finding(
            check='description',
            message=f'{path}: no description this check can read; write `description: >` and indent the text',
        )
        for path, description
        in descriptions.items()
        if not description
    ]
    findings = [
        *too_long,
        *unreadable,
    ]

    return findings


def check_headings(
    root: pathlib.Path,
) -> list[Finding]:
    """
    Every heading of a template document present in the example's copy of it.
    """
    template = root / TEMPLATE_FOLDER
    example = root / EXAMPLE_FOLDER
    shared = sorted(
        path.relative_to(template).as_posix()
        for path
        in template.rglob('*.md')
        if (example / path.relative_to(template)).is_file()
    )
    findings = [
        Finding(
            check='headings',
            message=f'{EXAMPLE_FOLDER}/{document} lacks the template heading "{heading}"',
        )
        for document
        in shared
        if document not in HEADING_EXCEPTIONS
        for heading
        in missing_headings(
            _read(template / document),
            _read(example / document),
        )
    ]

    return findings


def check_markers(
    root: pathlib.Path,
    files: list[str],
) -> list[Finding]:
    """
    The example's markers open and close in order, in every file that has a kind of marker, and in
    every cell of its notebooks.
    """
    marked = [
        path
        for path
        in files
        if path.startswith(f'{EXAMPLE_FOLDER}/') and pathlib.PurePosixPath(path).suffix in MARKERS
    ]
    notebooks = [
        path
        for path
        in files
        if path.startswith(f'{EXAMPLE_FOLDER}/') and path.endswith('.ipynb')
    ]
    file_findings = [
        Finding(
            check='markers',
            message=f'{path}: {problem}',
        )
        for path
        in marked
        for problem
        in marker_problems(
            _read(root / path),
            MARKERS[pathlib.PurePosixPath(path).suffix],
        )
    ]
    cell_findings = [
        Finding(
            check='markers',
            message=f'{path} {problem}',
        )
        for path
        in notebooks
        for problem
        in _notebook_marker_problems(_read(root / path))
    ]
    findings = [
        *file_findings,
        *cell_findings,
    ]

    return findings


def check_path_length(
    files: list[str],
) -> list[Finding]:
    """
    No tracked path longer than the limit.
    """
    findings = [
        Finding(
            check='path length',
            message=f'{path}: {len(path)} characters, over {PATH_LIMIT}',
        )
        for path
        in files
        if len(path) > PATH_LIMIT
    ]

    return findings


def check_references(
    root: pathlib.Path,
) -> list[Finding]:
    """
    The references `experiment-lifecycle` ships match what the worked example says they hold.
    """
    try:
        stale = sync_investment_lab_references.stale_references(root)
    except FileNotFoundError as error:
        missing = Finding(
            check='references',
            message=str(error),
        )

        return [missing]

    findings = [
        Finding(
            check='references',
            message=f'{reference_name}: differs from the example; run tools/sync_investment_lab_references.py',
        )
        for reference_name
        in stale
    ]

    return findings


def check_section_symbol(
    root: pathlib.Path,
    files: list[str],
) -> list[Finding]:
    """
    No text file uses the section symbol.
    """
    texts = [
        path
        for path
        in files
        if pathlib.PurePosixPath(path).suffix in TEXT_SUFFIXES
    ]
    findings = [
        Finding(
            check='section symbol',
            message=f'{path}: uses the section symbol; write "section"',
        )
        for path
        in texts
        if SECTION_SYMBOL in _read(root / path)
    ]

    return findings


def check_template_files(
    root: pathlib.Path,
) -> list[Finding]:
    """
    Every generated file of the template matches what the worked example says it holds.
    """
    try:
        stale = sync_investment_lab_references.stale_template_files(root)
    except FileNotFoundError as error:
        missing = Finding(
            check='template',
            message=str(error),
        )

        return [missing]

    findings = [
        Finding(
            check='template',
            message=f'{TEMPLATE_FOLDER}/{relative_path}: differs from the example; run tools/sync_investment_lab_references.py',
        )
        for relative_path
        in stale
    ]

    return findings


def check_versions(
    root: pathlib.Path,
) -> list[Finding]:
    """
    Each release folder's versions agree, and its changelog leads with them.
    """
    findings = [
        finding
        for folder
        in RELEASE_FOLDERS
        for finding
        in version_problems(
            folder,
            root / folder,
        )
    ]

    return findings


def folded_description(
    text: str,
) -> str:
    """
    A skill's `description` as an agent reads it: folded lines joined by single spaces, or the one
    line it is written on.  Empty when it is missing or written in any other form.
    """
    folded = FOLDED_DESCRIPTION.search(text)

    if folded is None:
        one_line = ONE_LINE_DESCRIPTION.search(text)
        description = one_line.group(1).strip() if one_line is not None else ''

        return description

    lines = folded.group(1).splitlines()
    joined = ' '.join(
        line.strip()
        for line
        in lines
    )

    return joined


def main() -> int:
    """
    Run every check on this repository and report.
    """
    files = tracked_files(REPOSITORY_ROOT)
    findings = [
        *check_versions(REPOSITORY_ROOT),
        *check_headings(REPOSITORY_ROOT),
        *check_markers(
            REPOSITORY_ROOT,
            files,
        ),
        *check_section_symbol(
            REPOSITORY_ROOT,
            files,
        ),
        *check_descriptions(
            REPOSITORY_ROOT,
            files,
        ),
        *check_references(REPOSITORY_ROOT),
        *check_template_files(REPOSITORY_ROOT),
        *check_path_length(files),
    ]

    for finding in findings:
        print(f'  FAIL  {finding.check:<15} {finding.message}')

    failure_count = len(findings)
    file_count = len(files)
    print(f'{failure_count} failures in {file_count} tracked files.')
    exit_code = 1 if findings else 0

    return exit_code


def marker_problems(
    text: str,
    markers: tuple[str, str],
) -> list[str]:
    """
    Where a text's markers fail to stand alone at column 0, or to open and close in order.

    The text's line endings are LF, as `_read` leaves them; a marker before a carriage return is
    reported, because the sync tool would not strip it.
    """
    begin, end = markers
    lines = text.split('\n')
    misplaced = [
        number
        for number, line
        in enumerate(lines, start=1)
        if line.strip() in markers and line not in markers
    ]

    if misplaced:

        return [f'line {misplaced[0]} has a marker that is not alone at column 0']

    marker_lines = [
        (number, line)
        for number, line
        in enumerate(lines, start=1)
        if line in markers
    ]
    out_of_turn = [
        (number, line)
        for position, (number, line)
        in enumerate(marker_lines)
        if line != (begin if position % 2 == 0 else end)
    ]

    if out_of_turn:
        number, line = out_of_turn[0]
        problem = (
            f'line {number} closes a block that is not open'
            if line == end
            else f'line {number} opens a block before the one above it closes'
        )

        return [problem]

    if len(marker_lines) % 2 == 1:
        last_number, _ = marker_lines[-1]

        return [f'line {last_number} opens a block that never closes']

    return []


def missing_headings(
    template_text: str,
    example_text: str,
) -> list[str]:
    """
    The template's headings the example's text does not carry, in the template's order.
    """
    example_headings = set(HEADING.findall(example_text))
    missing = [
        heading
        for heading
        in HEADING.findall(template_text)
        if heading not in example_headings
    ]

    return missing


def tracked_files(
    root: pathlib.Path,
) -> list[str]:
    """
    Every file git tracks, by its path inside the repository.
    """
    completed = subprocess.run(
        [
            'git',
            'ls-files',
            '-z',
        ],
        cwd=root,
        capture_output=True,
        encoding='utf-8',
        check=True,
    )
    # With -z git gives each path whole and unquoted, a non-ASCII one included, ended by a NUL.
    files = [
        path
        for path
        in completed.stdout.split('\0')
        if path
    ]

    return files


def version_problems(
    label: str,
    folder: pathlib.Path,
) -> list[Finding]:
    """
    One release folder's versions, compared with the one its `apm.yml` declares.
    """
    declared = _first(
        APM_VERSION,
        _read(folder / 'apm.yml'),
    )
    recorded = {
        'CHANGELOG.md': _first(
            CHANGELOG_VERSION,
            _read(folder / 'CHANGELOG.md'),
        ),
        'pyproject.toml': _first(
            PYPROJECT_VERSION,
            _read(folder / 'pyproject.toml'),
        ),
        'uv.lock': _first(
            UV_LOCK_VERSION,
            _read(folder / 'uv.lock'),
        ),
    }
    findings = [
        Finding(
            check='versions',
            message=f'{label}: apm.yml declares {declared}; {name} says {version}',
        )
        for name, version
        in recorded.items()
        if (folder / name).is_file() and version != declared
    ]

    return findings


def _first(
    pattern: re.Pattern[str],
    text: str,
) -> str | None:
    """
    The first group of a pattern's first match, or None.
    """
    match = pattern.search(text)
    value = match.group(1) if match is not None else None

    return value


def _notebook_marker_problems(
    text: str,
) -> list[str]:
    """
    Where a notebook's cells break the Markdown markers, each problem led by its cell, from 1.
    """
    cells = json.loads(text)['cells']
    problems = [
        f'cell {number}: {problem}'
        for number, cell
        in enumerate(cells, start=1)
        for problem
        in marker_problems(
            sync_investment_lab_references.read_cell_source(cell),
            MARKERS['.md'],
        )
    ]

    return problems


def _read(
    path: pathlib.Path,
) -> str:
    """
    A file's text with line endings made LF, or an empty text when it does not exist.
    """
    if not path.is_file():

        return ''

    raw = path.read_text(encoding='utf-8')
    text = raw.replace('\r\n', '\n')

    return text


if __name__ == '__main__':
    sys.exit(main())
