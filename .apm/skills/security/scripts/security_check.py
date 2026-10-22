"""
What in a folder should not leave the computer: a check run before a home, a strategy or a library
is pushed, sent or shared.

    uv run --no-project python security_check.py                  the folder you are in
    uv run --no-project python security_check.py "D:/Research/Arya"

What it reads
    the files   in a git repository, every file git tracks or would add — tracked, staged, and new
                files no `.gitignore` rule covers; in a folder without git, every file under it.
                Never `.git/`, a virtual environment, or a file over 2 MB or with a NUL byte
    the history the commit authors' e-mail addresses, and the folder's GitHub copy, when there is
                one and `gh` is signed in

What it reports, as *fix before you share* or *look at*
    fix         a secret: a provider key, a token, a private key, a password or licence written
                beside its name, a web address carrying a password; a file that holds secrets by
                its kind — `.env` (not `.env.template` or `.env.example`), `.kaxanuk_license`, a
                `.pem` or `.key`, an SSH key, `credentials.json`; at home, a copy on GitHub that is
                public; a `.gitignore` that would let `.env` in
    look at     a personal e-mail address in a file or as a commit's author; a notebook saved with
                its outputs; a strategy's or library's copy on GitHub that is public

A value is never printed: each secret shows its first four characters, its length and its line. A
placeholder — `<your key>`, `{SERVER}`, `${KEY}`, `your_api_key`, `xxxx`, `...` — is never a
finding, nor are the addresses an example or a generic mailbox uses.

Exit codes: 0 nothing found · 1 usage: not a folder · 2 something to fix · 3 only things to look at.
It needs only the standard library, writes nothing, and reads nothing outside the folder.
"""
import argparse
import dataclasses
import json
import pathlib
import re
import shutil
import subprocess
import sys

GENERIC_MAILBOXES = frozenset({
    'admin',
    'analytics',
    'contact',
    'hello',
    'info',
    'lab',
    'no-reply',
    'noreply',
    'research',
    'support',
    'workshops',
})
# Domains an example address uses, and GitHub's private address.
EXAMPLE_DOMAINS = (
    'example.com',
    'example.net',
    'example.org',
    'users.noreply.github.com',
)
EXAMPLE_TOP_LEVEL_DOMAINS = (
    '.example',
    '.invalid',
    '.local',
    '.localhost',
    '.test',
)
EMAIL = re.compile(r'(?<![\w.%+:-])[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}\b')
FIX = 'fix before you share'
LOOK = 'look at'
MAXIMUM_FILE_BYTES = 2_000_000
# Words that make a value a placeholder, never a secret.
PLACEHOLDER_WORDS = (
    'change',
    'dummy',
    'example',
    'fake',
    'placeholder',
    'redacted',
    'sample',
    'secret_here',
    'your',
    'xxxx',
)
SECRET_FILE_NAMES = frozenset({
    '.kaxanuk_license',
    'credentials.json',
    'id_dsa',
    'id_ecdsa',
    'id_ed25519',
    'id_rsa',
})
SECRET_FILE_SUFFIXES = frozenset({
    '.key',
    '.p12',
    '.pem',
    '.pfx',
})
SKIPPED_FOLDERS = frozenset({
    '.git',
    '.venv',
    '__pycache__',
    'node_modules',
    'venv',
})
TEMPLATE_ENVIRONMENT_FILES = frozenset({
    '.env.example',
    '.env.sample',
    '.env.template',
})
# Each kind of secret, by its shape. The named assignment comes last: it catches what the others do
# not, a password or a key written beside its name.
SECRET_PATTERNS = (
    (
        'an AWS access key',
        re.compile(r'\b(AKIA[0-9A-Z]{16})\b'),
    ),
    (
        'a GitHub token',
        re.compile(r'\b((?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b'),
    ),
    (
        'a Google API key',
        re.compile(r'\b(AIza[0-9A-Za-z_-]{35})\b'),
    ),
    (
        'an AI provider key',
        re.compile(r'\b(sk-(?:ant-|proj-)?[A-Za-z0-9_-]{24,})\b'),
    ),
    (
        'a Slack token',
        re.compile(r'\b(xox[abprs]-[A-Za-z0-9-]{10,})\b'),
    ),
    (
        'a private key',
        re.compile(r'(-----BEGIN [A-Z ]*PRIVATE KEY-----)'),
    ),
    (
        'a password in a web address',
        re.compile(r'\b[a-z][a-z0-9+.-]*://[^\s:/@]+:([^\s@/]+)@'),
    ),
)
# A password or a key written beside its name, `FMP_API_KEY=…`: what the shapes above do not catch.
# Its value counts when it holds a digit, as a real key or password almost always does, and, in code,
# only when quoted, since an unquoted one there is a call or a name: `api_key=read_key()`.
NAMED_SECRET = re.compile(''.join([
    r'(?i)(?<![a-z0-9])(?:api[_-]?key|apikey|access[_-]?token|auth[_-]?token|client[_-]?secret|',
    r'licen[cs]e[_-]?key|passwd|password|private[_-]?key|secret[_-]?key|token)',
    r'["\']?\s*[:=]\s*(?P<quote>["\']?)(?P<value>[^\s"\'#,;&()\[\]{}]{8,})',
]))
CODE_SUFFIXES = frozenset({
    '.ipynb',
    '.js',
    '.py',
    '.r',
    '.sql',
    '.ts',
})


@dataclasses.dataclass(frozen=True)
class Finding:
    """
    One thing to fix or to look at, with where it is and what it is, never the value itself.
    """
    level: str
    location: str
    what: str


def check_file(
    folder: pathlib.Path,
    relative_path: str,
) -> list[Finding]:
    """
    The findings in one file: its name, then its text, line by line.
    """
    findings = []
    path = folder / relative_path
    name = path.name.casefold()
    is_environment_file = (
        name == '.env'
        or name.endswith('.env')
        or name.startswith('.env.')
    )

    if is_environment_file and name not in TEMPLATE_ENVIRONMENT_FILES:
        findings.append(Finding(
            FIX,
            relative_path,
            'a file of keys that git would save; add it to .gitignore and keep it off any copy',
        ))
    elif name in SECRET_FILE_NAMES or path.suffix.casefold() in SECRET_FILE_SUFFIXES:
        findings.append(Finding(
            FIX,
            relative_path,
            'a file that holds a key or a licence by its kind; add it to .gitignore',
        ))

    text = _read_text(path)

    if text is None:
        return findings

    if path.suffix.casefold() == '.ipynb' and _notebook_has_outputs(text):
        findings.append(Finding(
            LOOK,
            relative_path,
            'a notebook saved with its outputs, which may show data or a value; clear them first',
        ))

    is_code = path.suffix.casefold() in CODE_SUFFIXES

    for line_number, line in enumerate(
        text.splitlines(),
        start=1,
    ):
        findings.extend(_check_line(
            f'{relative_path}:{line_number}',
            line,
            is_code,
        ))

    return findings


def check_folder(
    folder: pathlib.Path,
) -> list[Finding]:
    """
    Every finding in the folder: its files, its `.gitignore`, its authors and its copy on GitHub.
    """
    in_git = (folder / '.git').exists()
    files = _git_files(folder) if in_git else _all_files(folder)
    kind = folder_kind(folder)
    findings = []

    for relative_path in files:
        findings.extend(check_file(
            folder,
            relative_path,
        ))

    if in_git:
        findings.extend(_check_ignore_rules(folder))
        findings.extend(_check_authors(folder))
        findings.extend(_check_copy(
            folder,
            kind,
        ))

    return findings


def folder_kind(
    folder: pathlib.Path,
) -> str:
    """
    What the folder is: a researcher's home, a strategy, a Python library, or another folder.
    """
    if (folder / 'RESEARCHER.md').is_file():
        return 'home'

    if (folder / 'Bibliotheca').is_dir():
        return 'strategy'

    if (folder / 'pyproject.toml').is_file():
        return 'library'

    return 'folder'


def main(
    arguments: list[str] | None = None,
) -> int:
    """
    Parse the command line, check the folder, and print what was found.
    """
    _configure_console()
    parsed = _build_parser().parse_args(arguments)
    folder = pathlib.Path(parsed.folder).resolve()

    if not folder.is_dir():
        problem = f'not a folder: {parsed.folder}'
        print(
            problem,
            file=sys.stderr,
        )

        return 1

    findings = check_folder(folder)
    print_report(
        folder,
        findings,
    )
    exit_code = _exit_code(findings)

    return exit_code


def mask(
    value: str,
) -> str:
    """
    A value shown without being shown: its first four characters and its length.
    """
    masked = f'{value[:4]}… ({len(value)} characters)'

    return masked


def print_report(
    folder: pathlib.Path,
    findings: list[Finding],
) -> None:
    """
    Print the findings, those to fix first, or one line saying there are none.
    """
    if not findings:
        print(f'Nothing to fix in {folder}: no secret, no key file, no personal address found.')

        return

    for level in (
        FIX,
        LOOK,
    ):
        at_level = [
            finding
            for finding in findings
            if finding.level == level
        ]

        if not at_level:
            continue

        heading = level.capitalize()
        print(f'{heading} ({len(at_level)}):')

        for finding in at_level:
            print(f'  {finding.location}  {finding.what}')

    print('No value was printed. A secret that was ever saved or sent is rotated, not only removed.')


def _all_files(
    folder: pathlib.Path,
) -> list[str]:
    """
    Every file under a folder that has no git, outside the folders that are never read.
    """
    paths = sorted(folder.rglob('*'))
    relative_paths = [
        path.relative_to(folder)
        for path in paths
        if path.is_file()
    ]
    files = [
        relative_path.as_posix()
        for relative_path in relative_paths
        if not _is_skipped(relative_path)
    ]

    return files


def _build_parser() -> argparse.ArgumentParser:
    """
    The command line: the folder to check.
    """
    parser = argparse.ArgumentParser(
        prog='security_check.py',
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        'folder',
        nargs='?',
        default='.',
        help='the folder to check: a home, a strategy, a library (default: this folder)',
    )

    return parser


def _check_authors(
    folder: pathlib.Path,
) -> list[Finding]:
    """
    Each personal e-mail address that signs a commit, once.
    """
    output = _run_git(
        folder,
        [
            'log',
            '--format=%ae',
        ],
    )
    unique_addresses = set(output.split())
    addresses = sorted(unique_addresses)
    findings = [
        Finding(
            LOOK,
            'the saved versions',
            f'signed with a personal e-mail, {_mask_address(address)}; a copy on GitHub shows it',
        )
        for address in addresses
        if _is_personal_address(address)
    ]

    return findings


def _check_copy(
    folder: pathlib.Path,
    kind: str,
) -> list[Finding]:
    """
    Whether the folder's copy on GitHub is public, when `gh` can say.
    """
    address = _run_git(
        folder,
        [
            'remote',
            'get-url',
            'origin',
        ],
    ).strip()

    if 'github.com' not in address or shutil.which('gh') is None:
        return []

    completed = subprocess.run(
        [
            'gh',
            'repo',
            'view',
            address,
            '--json',
            'visibility',
            '-q',
            '.visibility',
        ],
        capture_output=True,
        check=False,
        encoding='utf-8',
        errors='replace',
    )
    visibility = completed.stdout.strip().upper()

    if visibility != 'PUBLIC':
        return []

    level = FIX if kind == 'home' else LOOK
    what = 'its copy on GitHub is public: anyone can read every saved version'

    return [Finding(
        level,
        address,
        what,
    )]


def _check_ignore_rules(
    folder: pathlib.Path,
) -> list[Finding]:
    """
    Whether `.gitignore` keeps a file of keys out, at the root and in `Config/`.
    """
    findings = []

    for probe in (
        '.env',
        'Config/.env',
    ):
        completed = subprocess.run(
            [
                'git',
                '-C',
                str(folder),
                'check-ignore',
                '-q',
                '--no-index',
                probe,
            ],
            capture_output=True,
            check=False,
        )

        if completed.returncode == 1:
            findings.append(Finding(
                FIX,
                '.gitignore',
                f'does not keep {probe} out; add a line `.env` so a file of keys is never saved',
            ))

    return findings


def _check_line(
    location: str,
    line: str,
    is_code: bool,
) -> list[Finding]:
    """
    The secrets and personal addresses in one line of text, each masked.
    """
    findings = []

    for what, pattern in SECRET_PATTERNS:
        for match in pattern.finditer(line):
            value = match.group(1)

            if _is_placeholder(value):
                continue

            findings.append(Finding(
                FIX,
                location,
                f'{what}, {mask(value)}',
            ))

    for match in NAMED_SECRET.finditer(line):
        named_value = match.group('value')
        is_quoted = bool(match.group('quote'))
        has_digit = any(
            character.isdigit()
            for character in named_value
        )
        is_literal = is_quoted or not is_code

        if not has_digit or not is_literal or _is_placeholder(named_value):
            continue

        findings.append(Finding(
            FIX,
            location,
            f'a secret beside its name, {mask(named_value)}',
        ))

    for match in EMAIL.finditer(line):
        address = match.group(0)

        if _is_personal_address(address):
            findings.append(Finding(
                LOOK,
                location,
                f'a personal e-mail address, {_mask_address(address)}',
            ))

    return findings


def _configure_console() -> None:
    """
    Print in UTF-8 whatever the console's own encoding, as `python -I` ignores PYTHONIOENCODING.
    """
    for console_stream in (
        sys.stdout,
        sys.stderr,
    ):
        try:
            console_stream.reconfigure(
                encoding='utf-8',
                errors='replace',
            )
        except (AttributeError, ValueError):
            pass


def _exit_code(
    findings: list[Finding],
) -> int:
    """
    The exit code: 2 when anything is to fix, 3 when there are only things to look at, else 0.
    """
    levels = {
        finding.level
        for finding in findings
    }

    if FIX in levels:
        return 2

    if LOOK in levels:
        return 3

    return 0


def _git_files(
    folder: pathlib.Path,
) -> list[str]:
    """
    Every file git tracks or would add: tracked, staged, and new files no ignore rule covers.
    """
    output = _run_git(
        folder,
        [
            'ls-files',
            '-z',
            '--cached',
            '--others',
            '--exclude-standard',
        ],
    )
    names = sorted({
        name
        for name in output.split('\0')
        if name and (folder / name).is_file()
    })

    return names


def _is_personal_address(
    address: str,
) -> bool:
    """
    Whether an e-mail address is a person's, not an example's, a generic mailbox's or GitHub's
    private one.
    """
    local_part, _, domain = address.casefold().rpartition('@')
    is_example = (
        domain.endswith(EXAMPLE_DOMAINS)
        or domain.endswith(EXAMPLE_TOP_LEVEL_DOMAINS)
        or local_part in GENERIC_MAILBOXES
        or local_part == ''
    )

    return not is_example


def _is_placeholder(
    value: str,
) -> bool:
    """
    Whether a matched value is a placeholder rather than a secret.
    """
    folded = value.casefold()
    has_marker = any(
        marker in value
        for marker in (
            '<',
            '{',
            '$',
            '...',
            '…',
            '*',
        )
    )
    has_word = any(
        word in folded
        for word in PLACEHOLDER_WORDS
    )
    is_one_character = len(set(folded)) == 1

    return has_marker or has_word or is_one_character


def _is_skipped(
    relative_path: pathlib.PurePath,
) -> bool:
    """
    Whether a file sits in a folder that is never read: git's own, a virtual environment, a cache.
    """
    skipped = bool(SKIPPED_FOLDERS.intersection(relative_path.parts))

    return skipped


def _mask_address(
    address: str,
) -> str:
    """
    An e-mail address shown by its first two characters and its domain.
    """
    local_part, _, domain = address.rpartition('@')
    masked = f'{local_part[:2]}…@{domain}'

    return masked


def _notebook_has_outputs(
    text: str,
) -> bool:
    """
    Whether a notebook was saved with any cell's outputs.
    """
    try:
        notebook = json.loads(text)
    except json.JSONDecodeError:
        return False

    has_outputs = any(
        cell.get('outputs')
        for cell in notebook.get('cells', [])
    )

    return has_outputs


def _read_text(
    path: pathlib.Path,
) -> str | None:
    """
    A file's text, or None for a file too large, binary or unreadable.
    """
    try:
        if path.stat().st_size > MAXIMUM_FILE_BYTES:
            return None

        content = path.read_bytes()
    except OSError:
        return None

    if b'\0' in content[:8192]:
        return None

    text = content.decode(
        'utf-8',
        errors='replace',
    )

    return text


def _run_git(
    folder: pathlib.Path,
    arguments: list[str],
) -> str:
    """
    A git command's output in the folder, or nothing when it fails.
    """
    completed = subprocess.run(
        [
            'git',
            '-C',
            str(folder),
            *arguments,
        ],
        capture_output=True,
        check=False,
        encoding='utf-8',
        errors='replace',
    )
    output = completed.stdout if completed.returncode == 0 else ''

    return output


if __name__ == '__main__':
    sys.exit(main())
