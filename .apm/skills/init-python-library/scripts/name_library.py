"""
Name a fresh copy of the KaxaNuk Python Library Template: the library's names where the template
has its own, the holder on the licence's first line, and the package folder moved.

`scaffold.py python-library <folder>` copies the template byte for byte and saves its first
version; this script then puts in the names the owner chose, and nothing else.  Every name derives
from one, the name on PyPI: `fcf-screen` gives `fcf_screen` to import, `FcfScreenError` for its
error and `Fcf Screen` as its title, unless `--title` gives another.  No text of its own is
written: the status line, `CHANGELOG.md`'s `## [Unreleased]` entry and `__version__` are true
before and after naming, and `AGENTS.md`, which quotes the template's names on purpose, is never
touched.

Usage:
    uv run --no-project python name_library.py --check-name <name> [--title <title>] [--unpublished]
    uv run --no-project python name_library.py <folder> --name <name> --holder <holder>
        [--title <title>] [--description <sentence>] [--unpublished] [--dry-run]

Both refuse, saying why, a name Python cannot import or that would hide one of its own modules or
built-ins, a folder of the template or of a build, a distribution the template's tools install or a
module they bring, a name Windows keeps for a device, and one longer than 40 characters; and a title
outside plain ASCII.  Both ask PyPI whether the name is taken, the one request either makes, and
refuse a name another project holds there, or one PyPI could not be asked about, unless
`--unpublished` says the library is never published.  `--check-name` writes nothing, and prints the
four names one name gives.

Naming refuses, writing nothing, a folder that is not the top of a git repository of its own — the
template itself, inside the package, or a copy whose repository is not finished — one whose history
holds anything but the copy's first commit, and one with a change not saved; the one exception is a
`uv.lock` that `uv sync` wrote before the naming, which the next `uv sync` rewrites.  It moves the
package folder first, with `git mv`, then rewrites each file that holds a name, as UTF-8 bytes, so
its line endings stay as they are, and prints each; `--dry-run` prints the same and writes nothing.
A run the system stops partway names the file and the reason, and `git -C <folder> reset --hard`
puts the copy back as it was copied.

Exit code 0 when the name can be used, or the folder was named; 1 when not; 2 for a command line
that cannot be read.  The console is written in UTF-8, so a path or a name in any alphabet prints;
the script's own words are ASCII.
"""
import argparse
import builtins
import dataclasses
import datetime
import functools
import http.client
import keyword
import os
import pathlib
import re
import subprocess
import sys
import urllib.error
import urllib.request

# The template's own names, which a copy carries until it is named, and the first commit
# `scaffold.py` saves for a copy: the message in its `STARTING_POINTS`, changed with this one.
FIRST_COMMIT = 'Start from the KaxaNuk Python Library Template'
TEMPLATE_DESCRIPTION = '[One sentence on what the library does.]'
TEMPLATE_DISTRIBUTION = 'kn-python-library-template'
TEMPLATE_ERROR_PREFIX = 'KnPythonLibraryTemplate'
TEMPLATE_HOLDER = 'KaxaNuk SC'
TEMPLATE_IMPORT = 'kn_python_library_template'
TEMPLATE_TITLE = 'KN Python Library Template'
# The files naming treats apart, as POSIX paths from the copy's root: `AGENTS.md` is never touched,
# and its marker tells a copy of this template from any other folder; the licence's first line
# names the holder, who goes into `pyproject.toml` alone; the package lives under `src/`; and the
# lock `uv sync` writes is the one file a fresh copy may hold unsaved.
AGENTS_FILE = 'AGENTS.md'
LICENSE_FILE = 'LICENSE'
LICENSE_PREFIX = 'Copyright since '
LOCK_FILE = 'uv.lock'
MARKER = '<!-- kaxanuk-starting-point: python-library -->'
PACKAGE_PARENT = 'src'
PYPROJECT_FILE = 'pyproject.toml'
# What a name, a title, a holder and a description may be.  A name of 40 characters with a title of
# 80 keeps every line of the template's Python within its 120 columns.
DESCRIPTION_MAX_LENGTH = 200
HOLDER_MAX_LENGTH = 100
NAME_MAX_LENGTH = 40
NAME_PATTERN = re.compile(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*')
TITLE_MAX_LENGTH = 80
# Characters a title may not hold, since it lands inside Python strings and Markdown; and those a
# holder or a description may not, since each lands inside a TOML string.
TITLE_FORBIDDEN = frozenset({
    '"',
    "'",
    '\\',
    '`',
})
TOML_FORBIDDEN = frozenset({
    '"',
    '\\',
})
# Names a library cannot take: a built-in every module sees, such as `zip`, which the library's own
# lint refuses to hide with an import; a folder of the template or of a build; a distribution the
# template's development tools install, as `uv sync` resolved them for template 0.1.0 — the
# library's own name would shadow it, and `uv sync` could not resolve — and a module one of them
# brings under another name, which the library's package would hide in `.venv/`; and a name Windows
# keeps for a device, which no folder can take.
BUILTIN_NAMES = frozenset(dir(builtins))
RESERVED_NAMES = frozenset({
    'build',
    'dist',
    'docs',
    'src',
    'test',
    'tests',
})
TOOL_DISTRIBUTIONS = frozenset({
    'accessible-pygments',
    'alabaster',
    'ast-serialize',
    'babel',
    'beautifulsoup4',
    'certifi',
    'charset-normalizer',
    'colorama',
    'docutils',
    'idna',
    'imagesize',
    'iniconfig',
    'jinja2',
    'librt',
    'markdown-it-py',
    'markupsafe',
    'mdit-py-plugins',
    'mdurl',
    'mypy',
    'mypy-extensions',
    'myst-parser',
    'packaging',
    'pathspec',
    'pdm-backend',
    'pluggy',
    'pydata-sphinx-theme',
    'pygments',
    'pytest',
    'pyyaml',
    'requests',
    'roman-numerals',
    'ruff',
    'snowballstemmer',
    'soupsieve',
    'sphinx',
    'sphinx-copybutton',
    'sphinxcontrib-applehelp',
    'sphinxcontrib-devhelp',
    'sphinxcontrib-htmlhelp',
    'sphinxcontrib-jsmath',
    'sphinxcontrib-qthelp',
    'sphinxcontrib-serializinghtml',
    'typing-extensions',
    'urllib3',
})
# The modules those distributions install whose names their own do not give, read from each one's
# RECORD; one starting with an underscore or a digit, which no name gives, is left out.
TOOL_IMPORT_NAMES = frozenset({
    'a11y_pygments',  # accessible-pygments
    'bs4',  # beautifulsoup4
    'markdown_it',  # markdown-it-py
    'mypyc',  # mypy
    'py',  # pytest
    'sphinxcontrib',  # the six sphinxcontrib-* distributions
    'yaml',  # pyyaml
})
WINDOWS_DEVICE_NAMES = frozenset({
    'aux',
    'con',
    'nul',
    'prn',
    *(
        f'{device}{number}'
        for device
        in ('com', 'lpt')
        for number
        in range(10)
    ),
})
# PyPI's answer for a name, asked once with a short wait: a project's page answers 200, a name no
# project holds 404, and anything else, or no answer, leaves the name unchecked.
PYPI_FREE = 'free'
PYPI_PROJECT_PAGE = 'https://pypi.org/project/{name}/'
PYPI_PROJECT_URL = 'https://pypi.org/pypi/{name}/json'
PYPI_TAKEN = 'taken'
PYPI_TIMEOUT_SECONDS = 10
PYPI_UNKNOWN = 'unknown'
# What is said when git cannot be run at all, and the exit code a shell gives a command not found.
GIT_MISSING_CODE = 127
GIT_NOT_FOUND = 'git was not found on this computer; install it first'


@dataclasses.dataclass(frozen=True)
class LibraryNames:
    """
    The four names one name gives: on PyPI, for its errors, to import, and as its title.
    """
    distribution: str
    error_prefix: str
    import_name: str
    title: str


@dataclasses.dataclass(frozen=True)
class PypiAnswer:
    """
    What PyPI said of a name, `free`, `taken` or `unknown`, and in words why when unknown.
    """
    state: str
    detail: str


@dataclasses.dataclass(frozen=True)
class Rewrite:
    """
    One tracked file of the copy: its path once the package folder has moved, and its content
    before and after naming.
    """
    path: pathlib.PurePosixPath
    before: bytes
    after: bytes


def copy_problem(
    folder: pathlib.Path,
    names: LibraryNames,
) -> str | None:
    """
    Why the folder is not a fresh copy of the template to name, or None when it is.

    A fresh copy is the top of a git repository of its own, whose history is the copy's first
    commit alone and whose working tree holds no change but a `uv.lock` left untracked; its
    `AGENTS.md` carries the marker and `src/` still holds the template's package.
    """
    if not folder.is_dir():
        not_a_folder = f'{folder} is not a folder'

        return not_a_folder

    top_level = _git(
        folder,
        [
            'rev-parse',
            '--show-toplevel',
        ],
    )
    top_level_text = top_level.stdout.strip()
    top_level_path = pathlib.Path(top_level_text).resolve()
    own_repository = top_level.returncode == 0 and top_level_path == folder.resolve()

    if not own_repository:
        git_says = _first_line(top_level.stderr) or f'its repository starts at {top_level_text}'
        not_own = ' '.join([
            f'{folder} is not the top of a git repository of its own ({git_says}).',
            'The template itself, or a folder inside another repository, is never named:',
            '`init-python-library <name>` copies the template into a folder of its own;',
            'or a copy whose repository is not finished: run the commands scaffold.py printed, then name it.',
        ])

        return not_own

    history = _git(
        folder,
        [
            'log',
            '--format=%s',
        ],
    )

    if history.returncode != 0:
        unsaved = ' '.join([
            'the copy has no saved version yet: finish its repository with the commands scaffold.py',
            'printed, then name it',
        ])

        return unsaved

    if history.stdout.splitlines() != [FIRST_COMMIT]:
        not_fresh = ' '.join([
            f'not a fresh copy: its history holds more than its first commit, "{FIRST_COMMIT}" - a',
            'version saved since the copy, or the names already in',
        ])

        return not_fresh

    status = _git(
        folder,
        [
            'status',
            '--porcelain',
        ],
    )
    changes = [
        line
        for line
        in status.stdout.splitlines()
        if line != f'?? {LOCK_FILE}'
    ]

    if status.returncode != 0 or changes:
        found = '; '.join(changes) or _first_line(status.stderr)
        not_saved = f'a change not saved: {found}'

        return not_saved

    agents = folder / AGENTS_FILE
    agents_text = agents.read_text(
        encoding='utf-8',
        errors='replace',
    ) if agents.is_file() else ''
    agents_lines = agents_text.splitlines()

    if MARKER not in agents_lines:
        no_marker = f'{AGENTS_FILE} does not carry {MARKER}: not a copy of the KaxaNuk Python Library Template'

        return no_marker

    template_package = folder / PACKAGE_PARENT / TEMPLATE_IMPORT

    if not (template_package / '__init__.py').is_file():
        named = f'{PACKAGE_PARENT}/{TEMPLATE_IMPORT}/ is missing: the library is named already'

        return named

    if (folder / PACKAGE_PARENT / names.import_name).exists():
        taken = ' '.join([
            f'{PACKAGE_PARENT}/{names.import_name}/ already exists; if a naming that stopped left it,',
            'delete it and run this again',
        ])

        return taken

    return None


def derive_names(
    name: str,
    title: str | None,
) -> LibraryNames:
    """
    The four names one name gives: hyphens become underscores to import it, and each of its words
    is capitalised, joined for the error and spaced for the title, unless a title is given.
    """
    words = [
        word.capitalize()
        for word
        in name.split('-')
    ]
    derived_title = ' '.join(words) if title is None else title
    names = LibraryNames(
        distribution=name,
        error_prefix=''.join(words),
        import_name=name.replace('-', '_'),
        title=derived_title,
    )

    return names


def main(
    arguments: list[str] | None = None,
) -> int:
    """
    Read the command line, check the name and, given a folder, check it and name it.
    """
    for console_stream in (sys.stdout, sys.stderr):
        try:
            console_stream.reconfigure(
                encoding='utf-8',
                errors='replace',
            )
        except Exception:
            pass

    parser = _build_parser()
    parsed = parser.parse_args(arguments)
    usage_problem = _usage_problem(parsed)

    if usage_problem is not None:
        parser.error(usage_problem)

    name = parsed.check_name if parsed.check_name is not None else parsed.name
    names = derive_names(
        name,
        parsed.title,
    )
    problems = [
        name_problem(names),
        _value_problem(
            'holder',
            parsed.holder,
            HOLDER_MAX_LENGTH,
        ),
        _value_problem(
            'description',
            parsed.description,
            DESCRIPTION_MAX_LENGTH,
        ),
    ]
    found_problems = [
        problem
        for problem
        in problems
        if problem is not None
    ]

    if found_problems:
        print(f'Refused: {found_problems[0]}')

        return 1

    _print_names(names)
    folder = None if parsed.folder is None else parsed.folder.resolve()

    if folder is not None:
        folder_problem = copy_problem(
            folder,
            names,
        )

        if folder_problem is not None:
            print(f'Nothing was named: {folder_problem}')

            return 1

    answer = _ask_pypi(names.distribution)
    print(_pypi_line(
        answer,
        names,
    ))
    pypi_problem = _pypi_problem(
        answer,
        names,
        parsed.unpublished,
    )

    if pypi_problem is not None:
        print(f'Refused: {pypi_problem}')

        return 1

    if folder is None:

        return 0

    exit_code = _name_copy(
        folder,
        names,
        parsed,
    )

    return exit_code


def name_problem(
    names: LibraryNames,
) -> str | None:
    """
    Why the name or its title cannot be used, or None when both can.
    """
    name = names.distribution
    title = names.title
    title_outside_ascii = any(
        not ' ' <= character <= '~'
        for character
        in title
    )
    title_forbidden = sorted(set(title) & TITLE_FORBIDDEN)
    checks = [
        (
            NAME_PATTERN.fullmatch(name) is None,
            f'"{name}" is not a name: lowercase letters, digits and single hyphens, starting with a letter',
        ),
        (
            len(name) > NAME_MAX_LENGTH,
            f'"{name}" is {len(name)} characters; a name takes at most {NAME_MAX_LENGTH}',
        ),
        (
            TEMPLATE_DISTRIBUTION in name,
            f'"{name}" holds the template\'s own name, {TEMPLATE_DISTRIBUTION}',
        ),
        (
            names.import_name in RESERVED_NAMES,
            f'"{name}" is a folder of the template, or one a build writes',
        ),
        (
            keyword.iskeyword(names.import_name) or keyword.issoftkeyword(names.import_name),
            f'"{names.import_name}" is a word of Python itself, so it cannot be imported',
        ),
        (
            names.import_name in sys.stdlib_module_names,
            f'"{names.import_name}" would hide the module of that name Python comes with',
        ),
        (
            names.import_name in BUILTIN_NAMES,
            f'"{names.import_name}" would hide the built-in of that name every module sees, which ruff refuses',
        ),
        (
            name in TOOL_DISTRIBUTIONS,
            f'"{name}" is a distribution the template\'s tools install, which `uv sync` could not tell apart',
        ),
        (
            names.import_name in TOOL_IMPORT_NAMES,
            f'"{names.import_name}" is a module the template\'s tools install, which the library would hide',
        ),
        (
            names.import_name in WINDOWS_DEVICE_NAMES,
            f'"{name}" is a name Windows keeps for a device, so no folder can take it',
        ),
        (
            title != title.strip() or not title,
            'the title is empty, or starts or ends with a space',
        ),
        (
            len(title) > TITLE_MAX_LENGTH,
            f'the title is {len(title)} characters; it takes at most {TITLE_MAX_LENGTH}',
        ),
        (
            title_outside_ascii,
            'the title holds a character outside plain ASCII, such as a curly quote or a long dash',
        ),
        (
            bool(title_forbidden),
            f'the title holds {" ".join(title_forbidden)}, which would break the Python it lands in',
        ),
    ]
    reasons = [
        reason
        for failed, reason
        in checks
        if failed
    ]
    problem = reasons[0] if reasons else None

    return problem


def plan_naming(
    folder: pathlib.Path,
    names: LibraryNames,
    holder: str,
    description: str | None,
) -> list[Rewrite]:
    """
    Every file git tracks in the copy but `AGENTS.md`, with the path and content naming gives it.

    The names are put in where the template has its own, in one pass, so a name is never read again
    as a placeholder; the holder goes into `pyproject.toml` alone, and the licence's first line is
    rewritten with this year and the holder.  A file that is not UTF-8 is left as it is.
    """
    tracked = _git(
        folder,
        [
            'ls-files',
            '-z',
        ],
    )
    paths = sorted(
        pathlib.PurePosixPath(tracked_path)
        for tracked_path
        in tracked.stdout.split('\0')
        if tracked_path and tracked_path != AGENTS_FILE
    )
    description_replacement = {} if description is None else {TEMPLATE_DESCRIPTION: description}
    replacements = {
        TEMPLATE_DISTRIBUTION: names.distribution,
        TEMPLATE_ERROR_PREFIX: names.error_prefix,
        TEMPLATE_IMPORT: names.import_name,
        TEMPLATE_TITLE: names.title,
        **description_replacement,
    }
    year = datetime.date.today().year
    rewrites = [
        _planned_rewrite(
            folder,
            path,
            names,
            replacements,
            holder,
            year,
        )
        for path
        in paths
    ]

    return rewrites


def _ask_pypi(
    distribution: str,
) -> PypiAnswer:
    """
    Whether PyPI holds a project of this name: `taken` on 200, `free` on 404, otherwise `unknown`.
    """
    url = PYPI_PROJECT_URL.format(name=distribution)

    try:
        with urllib.request.urlopen(
            url,
            timeout=PYPI_TIMEOUT_SECONDS,
        ) as response:
            status = response.status
    except urllib.error.HTTPError as http_error:
        status = http_error.code
    except (OSError, http.client.HTTPException) as network_error:
        reason = getattr(
            network_error,
            'reason',
            network_error,
        )
        unanswered = PypiAnswer(
            state=PYPI_UNKNOWN,
            detail=f'no answer from PyPI: {reason}',
        )

        return unanswered

    states = {
        200: PYPI_TAKEN,
        404: PYPI_FREE,
    }
    answer = PypiAnswer(
        state=states.get(status, PYPI_UNKNOWN),
        detail=f'PyPI answered HTTP {status}',
    )

    return answer


def _build_parser() -> argparse.ArgumentParser:
    """
    The command line: a name to check, or a folder to name with its name, holder and options.
    """
    parser = argparse.ArgumentParser(
        description='Check a Python library name, or name a fresh copy of the KaxaNuk Python Library Template.',
    )
    parser.add_argument(
        'folder',
        nargs='?',
        type=_expanded_path,
        default=None,
        help='the fresh copy to name; leave it out with --check-name',
    )
    parser.add_argument(
        '--check-name',
        default=None,
        help='check this name and print its four forms; nothing is written',
    )
    parser.add_argument(
        '--description',
        default=None,
        help="the owner's one sentence on what the library does, in place of the template's",
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='print what naming would move and rewrite, and write nothing',
    )
    parser.add_argument(
        '--holder',
        default=None,
        help="the licence's holder, also the author in pyproject.toml",
    )
    parser.add_argument(
        '--name',
        default=None,
        help='the name on PyPI, which gives the other three',
    )
    parser.add_argument(
        '--title',
        default=None,
        help='the title, in plain ASCII; by default each word of the name capitalised',
    )
    parser.add_argument(
        '--unpublished',
        action='store_true',
        help='the library is never published, so a name PyPI holds, or could not check, is accepted',
    )

    return parser


def _expanded_path(
    text: str,
) -> pathlib.Path:
    """
    A path from the command line, a leading `~` turned into the user's home folder.
    """
    path = pathlib.Path(text).expanduser()

    return path


def _first_line(
    text: str,
) -> str:
    """
    The first line of a command's output that holds anything, stripped, or an empty string.
    """
    lines = [
        line.strip()
        for line
        in text.splitlines()
        if line.strip()
    ]
    first = lines[0] if lines else ''

    return first


def _git(
    folder: pathlib.Path,
    arguments: list[str],
) -> subprocess.CompletedProcess[str]:
    """
    Run one git command in the folder and return what it did; a git not found returns as a failure.

    Its output is decoded as UTF-8 with replacement, so a localised message cannot raise, and
    `GIT_OPTIONAL_LOCKS=0` keeps a reading command from refreshing the index.
    """
    command = [
        'git',
        '-C',
        str(folder),
        *arguments,
    ]
    environment = {
        **os.environ,
        'GIT_OPTIONAL_LOCKS': '0',
    }

    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            encoding='utf-8',
            errors='replace',
            env=environment,
            check=False,
        )
    except FileNotFoundError:
        missing = subprocess.CompletedProcess(
            args=command,
            returncode=GIT_MISSING_CODE,
            stdout='',
            stderr=GIT_NOT_FOUND,
        )

        return missing

    return completed


def _leftovers(
    rewrites: list[Rewrite],
    names: LibraryNames,
    holder: str,
    description: str | None,
) -> list[str]:
    """
    Each planned file that would still hold one of the template's names, with the name it holds.

    A name the owner's own values contain — the holder `KaxaNuk SC`, a title holding the template's
    — is not looked for.  Any hit is a fault in the template or in this script.
    """
    given = [
        names.distribution,
        names.error_prefix,
        names.import_name,
        names.title,
        holder,
        description or '',
    ]
    placeholders = [
        placeholder
        for placeholder
        in sorted({
            TEMPLATE_DISTRIBUTION,
            TEMPLATE_ERROR_PREFIX,
            TEMPLATE_HOLDER,
            TEMPLATE_IMPORT,
            TEMPLATE_TITLE,
        })
        if not any(
            placeholder in value
            for value
            in given
        )
    ]
    hits = [
        f'{rewrite.path}: {placeholder}'
        for rewrite
        in rewrites
        for placeholder
        in placeholders
        if placeholder.encode('utf-8') in rewrite.after
    ]

    return hits


def _move_package(
    folder: pathlib.Path,
    names: LibraryNames,
) -> str | None:
    """
    Move the template's package folder to the library's import name with `git mv`: None when moved,
    otherwise git's reason.
    """
    moved = _git(
        folder,
        [
            'mv',
            '--',
            f'{PACKAGE_PARENT}/{TEMPLATE_IMPORT}',
            f'{PACKAGE_PARENT}/{names.import_name}',
        ],
    )
    failure = None if moved.returncode == 0 else _first_line(moved.stderr)

    return failure


def _name_copy(
    folder: pathlib.Path,
    names: LibraryNames,
    parsed: argparse.Namespace,
) -> int:
    """
    Plan the naming, check it leaves none of the template's names, then move the package folder
    and write each file that changes; with `--dry-run`, print the plan and stop.
    """
    rewrites = plan_naming(
        folder,
        names,
        parsed.holder,
        parsed.description,
    )
    leftovers = _leftovers(
        rewrites,
        names,
        parsed.holder,
        parsed.description,
    )

    if leftovers:
        print("Nothing was named: these files would still hold the template's names, a fault in the template:")

        for leftover in leftovers:
            print(f'  {leftover}')

        return 1

    changed = [
        rewrite
        for rewrite
        in rewrites
        if rewrite.after != rewrite.before
    ]
    move = f'{PACKAGE_PARENT}/{TEMPLATE_IMPORT}/ to {PACKAGE_PARENT}/{names.import_name}/'

    if parsed.dry_run:
        print(f'Would move {move}')

        for rewrite in changed:
            print(f'Would rewrite {rewrite.path}')

        print('Nothing was written: --dry-run')

        return 0

    recovery = f'`git -C "{folder}" reset --hard` puts the copy back as it was copied; then run this again.'
    move_failure = _move_package(
        folder,
        names,
    )

    if move_failure is not None:
        print(f'Nothing was named: moving {move} failed: {move_failure}')
        print(f'Close what holds the folder - an editor, a sync client, an antivirus scan. {recovery}')

        return 1

    print(f'Moved {move}')
    write_failure = _write_rewrites(
        folder,
        changed,
    )

    if write_failure is not None:
        print(f'The naming stopped at {write_failure}.')
        print(recovery)

        return 1

    print(f'Named {folder} {names.distribution}. Save it with:')
    print(f'  git -C "{folder}" commit --all -m "Name the library {names.distribution}"')

    if (folder / LOCK_FILE).is_file():
        print(f"{LOCK_FILE}, written before the naming under the template's name, is not saved; `uv sync` rewrites it.")

    return 0


def _planned_rewrite(
    folder: pathlib.Path,
    path: pathlib.PurePosixPath,
    names: LibraryNames,
    replacements: dict[str, str],
    holder: str,
    year: int,
) -> Rewrite:
    """
    One file's path and content once named: its names replaced in one pass, the holder too in
    `pyproject.toml`, and the licence's first line rewritten.
    """
    before = (folder / path).read_bytes()
    parts = path.parts
    in_package = parts[:2] == (
        PACKAGE_PARENT,
        TEMPLATE_IMPORT,
    )
    moved_path = pathlib.PurePosixPath(
        PACKAGE_PARENT,
        names.import_name,
        *parts[2:],
    ) if in_package else path

    try:
        text = before.decode('utf-8')
    except UnicodeDecodeError:
        undecoded = Rewrite(
            path=moved_path,
            before=before,
            after=before,
        )

        return undecoded

    holder_replacement = {TEMPLATE_HOLDER: holder} if path.as_posix() == PYPROJECT_FILE else {}
    file_replacements = {
        **replacements,
        **holder_replacement,
    }
    pattern = re.compile('|'.join(
        re.escape(placeholder)
        for placeholder
        in sorted(
            file_replacements,
            key=len,
            reverse=True,
        )
    ))
    renamed = pattern.sub(
        functools.partial(
            _replacement,
            replacements=file_replacements,
        ),
        text,
    )
    licensed = _with_license_holder(
        path,
        renamed,
        holder,
        year,
    )
    rewrite = Rewrite(
        path=moved_path,
        before=before,
        after=licensed.encode('utf-8'),
    )

    return rewrite


def _print_names(
    names: LibraryNames,
) -> None:
    """
    Print the four names one name gives, one per line.
    """
    print(f'The names {names.distribution} gives:')
    print(f'  on PyPI, and in pip install   {names.distribution}')
    print(f'  in Python, to import          {names.import_name}')
    print(f'  its error                     {names.error_prefix}Error')
    print(f'  its title                     {names.title}')


def _pypi_line(
    answer: PypiAnswer,
    names: LibraryNames,
) -> str:
    """
    What PyPI said of the name, in one line.
    """
    page = PYPI_PROJECT_PAGE.format(name=names.distribution)
    lines = {
        PYPI_FREE: 'PyPI: free - no project holds the name; PyPI may still refuse one too close to another',
        PYPI_TAKEN: f'PyPI: taken - another project holds the name, {page}',
        PYPI_UNKNOWN: f'PyPI: not checked - {answer.detail}',
    }
    line = lines[answer.state]

    return line


def _pypi_problem(
    answer: PypiAnswer,
    names: LibraryNames,
    unpublished: bool,
) -> str | None:
    """
    Why PyPI's answer refuses the name, or None: a name taken or unchecked passes for a Python
    library that is never published.
    """
    if answer.state == PYPI_FREE or unpublished:

        return None

    reason = (
        f'another project holds {names.distribution} on PyPI'
        if answer.state == PYPI_TAKEN
        else 'PyPI could not be asked whether the name is taken; run this again online'
    )
    problem = ' '.join([
        f'{reason}. Choose another name, or pass --unpublished for a Python library that is never',
        'published.',
    ])

    return problem


def _replacement(
    match: re.Match[str],
    replacements: dict[str, str],
) -> str:
    """
    The library's own name for the template's name a pattern matched.
    """
    replaced = replacements[match.group(0)]

    return replaced


def _usage_problem(
    parsed: argparse.Namespace,
) -> str | None:
    """
    Why the command line asks for neither of the two things the script does, or None.
    """
    checking = parsed.check_name is not None
    naming_given = parsed.folder is not None or parsed.name is not None
    naming_complete = parsed.folder is not None and parsed.name is not None and parsed.holder is not None

    if checking and naming_given:

        return 'give either --check-name <name>, or a folder with --name and --holder, not both'

    if not checking and not naming_complete:

        return 'naming takes the folder, --name and --holder; checking a name alone takes --check-name'

    return None


def _value_problem(
    label: str,
    value: str | None,
    max_length: int,
) -> str | None:
    """
    Why a holder or a description cannot go into `pyproject.toml`, or None when it can, or is not given.
    """
    if value is None:

        return None

    unsafe = any(
        character in TOML_FORBIDDEN or not character.isprintable()
        for character
        in value
    )
    checks = [
        (
            value != value.strip() or not value,
            f'the {label} is empty, or starts or ends with a space',
        ),
        (
            len(value) > max_length,
            f'the {label} is {len(value)} characters; it takes at most {max_length}',
        ),
        (
            unsafe,
            f'the {label} holds a double quote, a backslash or a character that does not print',
        ),
    ]
    reasons = [
        reason
        for failed, reason
        in checks
        if failed
    ]
    problem = reasons[0] if reasons else None

    return problem


def _with_license_holder(
    path: pathlib.PurePosixPath,
    text: str,
    holder: str,
    year: int,
) -> str:
    """
    The licence with its first line naming this year and the holder; any other file as it is.

    Only a first line in the template's form, `Copyright since <year> <holder>`, is rewritten; a
    licence of another form keeps the template's holder, which the leftover check then finds.
    """
    if path.as_posix() != LICENSE_FILE or not text.startswith(LICENSE_PREFIX):

        return text

    _, separator, rest = text.partition('\n')
    licensed = f'{LICENSE_PREFIX}{year} {holder}{separator}{rest}'

    return licensed


def _write_rewrites(
    folder: pathlib.Path,
    rewrites: list[Rewrite],
) -> str | None:
    """
    Write each rewritten file as bytes and say so: None when all were written, otherwise the file
    the system stopped at and its reason.
    """
    for rewrite in rewrites:
        target = folder / rewrite.path

        try:
            target.write_bytes(rewrite.after)
        except OSError as exception:
            reason = exception.strerror or str(exception)
            failure = f'{rewrite.path}: {reason}'

            return failure

        print(f'Rewrote {rewrite.path}')

    return None


if __name__ == '__main__':
    sys.exit(main())
