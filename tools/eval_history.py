"""
Write a replayed case's `history.jsonl` from a run of its first turn, keeping only what may be committed.

The history of an "after the go" case is the Claude Code session transcript of a run of its partner
case, kept by `--keep-temp`.  The transcript as written carries the account e-mail of whoever ran it
and a snapshot of the system prompt; this keeps only its `user` and `assistant` lines, which is what
a replay needs, and refuses to write anything that still holds an e-mail address.

The source is one of:

    a batch's aggregate-result.json, with --case naming the first-turn case: the kept folder of that
        case's first run is found from its tracePath, <kept folder>/out/trace.jsonl
    a kept run folder, /tmp/claude-eval-*: its session is config/projects/*/*.jsonl
    a session transcript, *.jsonl

Run from the repository root, after running the first-turn case once with tools/eval_run.py:

    uv run --no-project python tools/eval_history.py \
      evals/results/<batch>/aggregate-result.json --case contract/blueprint/waits-before-write \
      evals/quality/blueprint/predictions-cite/history.jsonl

Exit code: 0 written, 1 with a one-line message when the source cannot be read or found, when it holds
no user or assistant line, or when what would be written holds an e-mail address; then nothing is
written.  Console output is ASCII only.
"""
import argparse
import json
import os
import pathlib
import re
import subprocess
import sys

# A top-level domain that is one of these is a file name after an @, such as `@AGENTS.md`.
FILE_EXTENSIONS = (
    'csv',
    'ipynb',
    'json',
    'md',
    'pdf',
    'py',
    'toml',
    'txt',
    'yaml',
    'yml',
)
EXTENSION_ALTERNATIVES = '|'.join(FILE_EXTENSIONS)
# The local part starts at a word boundary that is not the letter of a JSON escape such as `\t`, or
# right after one of `\n`, `\r`, `\t`.
EMAIL_PARTS = (
    r'(?:(?<=\\[nrt])|(?<![\\A-Za-z0-9._%+-]))',
    r'[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*',
    rf'\.(?!(?:{EXTENSION_ALTERNATIVES})\b)[A-Za-z]{{2,}}\b',
)
EMAIL_ADDRESS = re.compile(''.join(EMAIL_PARTS))
KEPT_LINE_TYPES = (
    'user',
    'assistant',
)
SESSION_GLOB = 'config/projects/*/*.jsonl'


def holds_e_mail(
    text: str,
) -> bool:
    """
    Whether the text holds an e-mail address: one of the runner's own, or any that looks like one.

    The runner's own are `CLAUDE_CODE_USER_EMAIL` and `git config user.email`, when set; they are
    refused whatever their domain.  Any other address is found by `EMAIL_ADDRESS`, which does not
    take a JSON escape before an @ or a file name after it for one.
    """
    lowered = text.lower()
    known = [
        address
        for address
        in _known_addresses()
        if address.lower() in lowered
    ]

    if known:

        return True

    found = EMAIL_ADDRESS.search(text) is not None

    return found


def kept_folder(
    results: dict,
    case_name: str,
) -> pathlib.Path:
    """
    The kept folder of a case's first run, from a batch's aggregate-result.json.

    Each run records `tracePath`, `<kept folder>/out/trace.jsonl`; it is empty when the run never
    started, and the folder exists only when the batch ran with `--keep-temp`.
    """
    runs = [
        run
        for case
        in results.get('cases', [])
        if case.get('name') == case_name
        for run
        in case.get('arms', {}).get('with', [])
    ]

    if not runs:
        absent = f'no run of {case_name} in these results'

        raise ValueError(absent)

    trace_path = runs[0].get('tracePath') or ''

    if not trace_path:
        unstarted = f'the first run of {case_name} has no trace: {runs[0].get("error")}'

        raise ValueError(unstarted)

    folder = pathlib.Path(trace_path).parent.parent

    return folder


def main(
    arguments: list[str] | None = None,
) -> int:
    """
    Find the session, filter it, check it for e-mail addresses, and write the history.
    """
    parser = _build_parser()
    parsed = parser.parse_args(arguments)

    try:
        written = write_history(
            parsed.source,
            parsed.destination,
            parsed.case,
        )
    except (
        OSError,
        ValueError,
    ) as error:
        print(f'eval_history: nothing written: {_one_line(error)}')

        return 1

    print(f'Wrote {written} lines to {parsed.destination}')

    return 0


def replay_lines(
    transcript: str,
) -> list[str]:
    """
    The lines of a session transcript whose `type` is `user` or `assistant`, as they were written.
    """
    lines = [
        line
        for line
        in transcript.splitlines()
        if line.strip()
    ]
    kept = [
        line
        for line
        in lines
        if _line_type(line) in KEPT_LINE_TYPES
    ]

    return kept


def session_file(
    source: pathlib.Path,
    case_name: str | None,
) -> pathlib.Path:
    """
    The session transcript a source names: itself, the one in a kept folder, or a case's in results.
    """
    if source.suffix == '.json':
        if case_name is None:
            no_case = 'a results file needs --case, naming the first-turn case'

            raise ValueError(no_case)

        results = json.loads(source.read_text(encoding='utf-8'))
        folder = kept_folder(
            results,
            case_name,
        )

        return _only_session(folder)

    if source.is_dir():

        return _only_session(source)

    if source.suffix != '.jsonl':
        unknown = f'{source} is not a results .json, a kept run folder or a session .jsonl'

        raise ValueError(unknown)

    return source


def write_history(
    source: pathlib.Path,
    destination: pathlib.Path,
    case_name: str | None,
) -> int:
    """
    Write the replayable lines of the source's session to `destination`, and return how many.

    Raises ValueError, writing nothing, when there are none or they hold an e-mail address.
    """
    transcript = session_file(
        source,
        case_name,
    )
    lines = replay_lines(transcript.read_text(encoding='utf-8'))

    if not lines:
        empty = f'{transcript} holds no user or assistant line'

        raise ValueError(empty)

    text = ''.join(
        f'{line}\n'
        for line
        in lines
    )

    if holds_e_mail(text):
        personal = f'the filtered {transcript.name} still holds an e-mail address; remove it from the run first'

        raise ValueError(personal)

    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    destination.write_text(
        text,
        encoding='utf-8',
        newline='\n',
    )
    count = len(lines)

    return count


def _build_parser() -> argparse.ArgumentParser:
    """
    The command line: the source, where the history goes, and the case when the source is results.
    """
    parser = argparse.ArgumentParser(
        description="Write a replayed case's history.jsonl from a run of its first turn.",
    )
    parser.add_argument(
        'source',
        type=pathlib.Path,
        help='aggregate-result.json (with --case), a kept run folder, or a session .jsonl',
    )
    parser.add_argument(
        'destination',
        type=pathlib.Path,
        help="the replayed case's history.jsonl",
    )
    parser.add_argument(
        '--case',
        default=None,
        help='the first-turn case whose first run is taken, when the source is aggregate-result.json',
    )

    return parser


def _known_addresses() -> list[str]:
    """
    The addresses of whoever runs this: `CLAUDE_CODE_USER_EMAIL` and `git config user.email`, if set.
    """
    from_environment = os.environ.get(
        'CLAUDE_CODE_USER_EMAIL',
        '',
    )

    try:
        configured = subprocess.run(
            [
                'git',
                'config',
                'user.email',
            ],
            capture_output=True,
            text=True,
            check=False,
        ).stdout
    except OSError:
        configured = ''

    addresses = [
        address.strip()
        for address
        in (
            from_environment,
            configured,
        )
        if address.strip()
    ]

    return addresses


def _line_type(
    line: str,
) -> str | None:
    """
    The `type` of one transcript line; raises ValueError when the line is not a JSON object.
    """
    try:
        entry = json.loads(line)
    except json.JSONDecodeError as error:
        malformed = f'a transcript line is not JSON: {error}'

        raise ValueError(malformed) from error

    if not isinstance(entry, dict):
        not_object = 'a transcript line is not a JSON object'

        raise ValueError(not_object)

    line_type = entry.get('type')

    return line_type


def _one_line(
    error: Exception,
) -> str:
    """
    An error as one line of ASCII.
    """
    described = str(error)
    flattened = ' '.join(described.split())
    ascii_only = flattened.encode(
        'ascii',
        'replace',
    ).decode('ascii')

    return ascii_only


def _only_session(
    folder: pathlib.Path,
) -> pathlib.Path:
    """
    The one session transcript in a kept run folder; raises ValueError when there is not exactly one.
    """
    found = sorted(folder.glob(SESSION_GLOB))

    if len(found) != 1:
        not_one = f'{folder} holds {len(found)} session files under {SESSION_GLOB}, not one'

        raise ValueError(not_one)

    return found[0]


if __name__ == '__main__':
    sys.exit(main())
