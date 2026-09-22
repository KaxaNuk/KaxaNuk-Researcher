"""
Run the KaxaNuk Researcher's evals against what a user actually installs.

It builds the real `apm install -g <this repository> --target claude` into a throwaway home in the
system's temporary folder, outside the repository (apm copies the whole repository into the
install, so a home inside it would copy itself), and assembles `evals/.run/` from it:

    evals/.run/plugin/             the plugin the harness runs: skills/, commands/, a minimal
                                   .claude-plugin/plugin.json, and the cases in evals/
    evals/.run/templates/          the three starting points, copied from where apm put the package,
    evals/.run/examples/           so `scaffold.py` finds them beside the plugin (its `parents[4]`)
    evals/.run/fixtures/           every fixture, built fresh from the current templates

The committed contract and quality cases are copied below `plugin/evals/`, and the triggering cases
are generated there from `evals/triggering/requests.toml`.  A case folder that holds a one-line
`FIXTURE` file naming a fixture gets a real copy of it in `fixture/` and a `scaffold.sh` that copies
it into the empty workspace; its `case.yaml` names `context.scaffold_script: scaffold.sh` itself.
Then `claude plugin eval` runs on the plugin folder.  Sessions run on Opus 5.5 and the quality judge
on Fable 5.1; the no-plugin comparison arm is off.  Each batch writes its results and report to its
own `evals/results/<UTC time>-<cases>/`, and keeps every run's folder under /tmp/claude-eval-* for
diagnosis.

Every triggering run ends with the error "Reached maximum number of turns (2)": the case stops as
soon as the skill is chosen, and the run is still graded.  The error is expected there.

Run from the repository root:

    uv run --no-project --with pypdf python tools/eval_run.py --case 'triggering/*' --max-cost-usd 5
    uv run --no-project --with pypdf python tools/eval_run.py --case 'contract/read/*' --dry-run \
      --max-cost-usd 1

`--no-shell` leaves out every case that grants Bash, for a machine whose sandbox cannot run a
shell.  Every run spends the plan of whoever runs it; `--max-cost-usd` is required for that reason.
Exit code: the harness's, or 1 when the install or the run folder cannot be built.  Console output
is ASCII only.
"""
import argparse
import datetime
import itertools
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib

import eval_fixtures

REPOSITORY_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVALS_DIRECTORY = REPOSITORY_ROOT / 'evals'
RUN_DIRECTORY = EVALS_DIRECTORY / '.run'
PLUGIN_DIRECTORY = RUN_DIRECTORY / 'plugin'
FIXTURES_DIRECTORY = RUN_DIRECTORY / 'fixtures'
RESULTS_DIRECTORY = EVALS_DIRECTORY / 'results'
TRIGGERING_TABLE = EVALS_DIRECTORY / 'triggering' / 'requests.toml'
# The throwaway home lives outside the repository: apm copies the whole repository into the
# install, so a home inside it would be copied into itself.
INSTALL_PREFIX = 'kaxanuk-eval-install-'
# Where `apm install -g <a local path>` puts the package, below the home it installs into.
INSTALLED_PACKAGE = pathlib.Path('.apm') / 'apm_modules' / '_local' / 'KaxaNuk-Researcher'
# The starting points `scaffold.py` copies from, relative to the package root.
STARTING_POINTS = (
    'templates/researcher',
    'templates/strategy',
    'examples/liquid-golden-cross',
)
# The layers whose cases are committed folders; triggering's are generated from the table.
AUTHORED_LAYERS = (
    'contract',
    'quality',
)
CASE_FILES = (
    'prompt.md',
    'case.yaml',
)
# A case names its fixture in this file; the runner puts the copy and the script beside it.
FIXTURE_FILE = 'FIXTURE'
FIXTURE_FOLDER = 'fixture'
SCAFFOLD_FILE = 'scaffold.sh'
SCAFFOLD_SCRIPT = '\n'.join([
    '#!/usr/bin/env bash',
    'set -euo pipefail',
    'here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"',
    f'cp -r "$here/{FIXTURE_FOLDER}/." .',
    '',
])
ALLOWED_TOOLS_LINE = re.compile(r'\s*allowed_tools\s*:(.*)')
LIST_ITEM_LINE = re.compile(r'\s*-\s')
SHELL_TOOL = re.compile(r'\bBash\b')
JUDGE_MODEL = 'claude-fable-5-1'
SESSION_MODEL = 'claude-opus-5-5'
# Granted by the operator to every case of a batch; Bash only where the sandbox can run a shell.
WRITE_TOOLS = (
    'Write',
    'Edit',
)
MANIFEST = {
    'name': 'kaxanuk-researcher-evals',
    'version': '0.0.0',
}
KEPT_FOLDERS_REMINDER = ' '.join([
    'Every run folder is kept under /tmp/claude-eval-* for diagnosis; copy out/trace.jsonl and',
    'config/projects/*/*.jsonl, then remove it: chmod -R u+rwX <folder> && rm -rf <folder>',
])
# A triggering case only needs to see which skill is called; it may read, never write.
TRIGGERING_FRONTMATTER = '\n'.join([
    '---',
    'name: {name}',
    'runs: 3',
    'max_turns: 2',
    'timeout_seconds: 120',
    'allowed_tools: [Skill, Read, Glob, Grep]',
    '---',
    '{request}',
    '',
])
FIRED_GRADER = '\n'.join([
    '---',
    'type: tool_used',
    'tool: Skill',
    "input_match: '\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?{skill}\"'",
    'min: 1',
    '---',
    'The request is one `{skill}` exists for, so `{skill}` is called.',
    '',
])
# `max: 0` alone fails every run: `min` defaults to 1, so a call that must not happen sets both.
NOT_FIRED_GRADER = '\n'.join([
    '---',
    'type: tool_used',
    'tool: Skill',
    "input_match: '\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?{skill}\"'",
    'min: 0',
    'max: 0',
    '---',
    'The request belongs to another skill, so `{skill}` is not called.',
    '',
])


def assemble_plugin(
    claude_directory: pathlib.Path,
    plugin_directory: pathlib.Path,
) -> None:
    """
    Lay the installed skills and commands out as a plugin, with a minimal manifest.
    """
    shutil.rmtree(
        plugin_directory,
        ignore_errors=True,
    )
    shutil.copytree(
        claude_directory / 'skills',
        plugin_directory / 'skills',
    )
    shutil.copytree(
        claude_directory / 'commands',
        plugin_directory / 'commands',
    )
    manifest = plugin_directory / '.claude-plugin' / 'plugin.json'
    manifest.parent.mkdir(parents=True)
    manifest.write_text(
        json.dumps(MANIFEST),
        encoding='utf-8',
    )


def build_install(
    repository: pathlib.Path,
    home: pathlib.Path,
) -> pathlib.Path:
    """
    Install this repository for Claude into a throwaway home, and return its `.claude` folder.
    """
    shutil.rmtree(
        home,
        ignore_errors=True,
    )
    home.mkdir(parents=True)
    environment = {
        **os.environ,
        'HOME': str(home),
        'USERPROFILE': str(home),
    }
    subprocess.run(
        [
            'uvx',
            '--from',
            'apm-cli',
            'apm',
            'install',
            '-g',
            str(repository),
            '--target',
            'claude',
        ],
        check=True,
        env=environment,
    )
    claude_directory = home / '.claude'

    return claude_directory


def copy_authored_cases(
    source_directory: pathlib.Path,
    eval_directory: pathlib.Path,
    fixtures_directory: pathlib.Path,
    no_shell: bool,
) -> list[str]:
    """
    Copy the committed cases below the eval folder, each with its fixture; return those left out.

    With `no_shell`, a case that grants Bash is left out.  A case with a `FIXTURE` file gets a copy
    of that fixture and the scaffold script that puts it in the workspace.  Raises ValueError when
    a case names an unknown fixture or does not name the scaffold script.
    """
    left_out = []

    for case_directory in _authored_case_directories(source_directory):
        name = case_directory.relative_to(source_directory).as_posix()

        if no_shell and _grants_shell(case_directory):
            left_out.append(name)

            continue

        target = eval_directory / name
        shutil.copytree(
            case_directory,
            target,
            dirs_exist_ok=True,
        )

        if (case_directory / FIXTURE_FILE).is_file():
            _add_fixture(
                case_directory,
                target,
                fixtures_directory,
            )

    return left_out


def copy_starting_points(
    package_directory: pathlib.Path,
    run_directory: pathlib.Path,
) -> None:
    """
    Copy the package's three starting points into the run folder, beside the plugin.
    """
    for relative_path in STARTING_POINTS:
        shutil.copytree(
            package_directory / relative_path,
            run_directory / relative_path,
        )


def eval_command(
    plugin_directory: pathlib.Path,
    case_glob: str,
    runs: int,
    max_cost_usd: float,
    output_directory: pathlib.Path,
    no_shell: bool,
) -> list[str]:
    """
    The `claude plugin eval` command for one batch; the plugin folder comes first, as the harness asks.
    """
    shell_grant = [] if no_shell else ['Bash']
    command = [
        'claude',
        'plugin',
        'eval',
        str(plugin_directory),
        '--allow-tools',
        *WRITE_TOOLS,
        *shell_grant,
        '--case',
        case_glob,
        '--runs',
        str(runs),
        '--model',
        SESSION_MODEL,
        '--judge-model',
        JUDGE_MODEL,
        '--ablation',
        'none',
        '--max-cost-usd',
        str(max_cost_usd),
        '--scaffold',
        '--trust-plugin',
        '--keep-temp',
        '--no-publish',
        '--output-dir',
        str(output_directory),
        '--report',
        str(output_directory / 'report.html'),
    ]

    return command


def main(
    arguments: list[str] | None = None,
) -> int:
    """
    Build the install, assemble the run folder, and run one batch of cases.
    """
    parser = _build_parser()
    parsed = parser.parse_args(arguments)

    shutil.rmtree(
        RUN_DIRECTORY,
        ignore_errors=True,
    )

    with tempfile.TemporaryDirectory(prefix=INSTALL_PREFIX) as install_home:
        installed = _install_into_run(pathlib.Path(install_home))

    if not installed:

        return 1

    eval_fixtures.build_all(FIXTURES_DIRECTORY)

    try:
        left_out = copy_authored_cases(
            EVALS_DIRECTORY,
            PLUGIN_DIRECTORY / 'evals',
            FIXTURES_DIRECTORY,
            no_shell=parsed.no_shell,
        )
    except ValueError as error:
        print(error)

        return 1

    for name in left_out:
        print(f'Left out (grants Bash, --no-shell): {name}')

    _write_cases(
        PLUGIN_DIRECTORY / 'evals',
        triggering_cases(_read_table(TRIGGERING_TABLE)),
    )
    started = datetime.datetime.now(datetime.UTC)
    command = eval_command(
        PLUGIN_DIRECTORY,
        case_glob=parsed.case,
        runs=parsed.runs,
        max_cost_usd=parsed.max_cost_usd,
        output_directory=results_directory(
            parsed.case,
            started,
        ),
        no_shell=parsed.no_shell,
    )
    print(' '.join(command))

    if parsed.dry_run:

        return 0

    print(KEPT_FOLDERS_REMINDER)
    completed = subprocess.run(
        command,
        cwd=PLUGIN_DIRECTORY,
        check=False,
    )
    print(KEPT_FOLDERS_REMINDER)

    return completed.returncode


def results_directory(
    case_glob: str,
    started: datetime.datetime,
) -> pathlib.Path:
    """
    The folder of one batch's results, named by its UTC start and its case glob, so none overwrites another.
    """
    stamp = started.astimezone(datetime.UTC).strftime('%Y%m%dT%H%M%SZ')
    spelled = case_glob.replace(
        '*',
        'all',
    )
    slug = re.sub(
        r'[^A-Za-z0-9]+',
        '-',
        spelled,
    ).strip('-')
    folder = RESULTS_DIRECTORY / f'{stamp}-{slug}'

    return folder


def triggering_cases(
    table: dict[str, dict[str, list[str]]],
) -> dict[str, str]:
    """
    Every triggering case's files, by path below the eval folder, from the table of requests.
    """
    cases = {}

    for skill, requests in table.items():
        cases.update(_fires_cases(
            skill,
            requests['fires'],
        ))
        cases.update(_near_miss_cases(
            skill,
            requests['near_miss'],
        ))

    return cases


def _add_fixture(
    case_directory: pathlib.Path,
    target: pathlib.Path,
    fixtures_directory: pathlib.Path,
) -> None:
    """
    Copy the fixture a case names into its run copy, with the script that puts it in the workspace.
    """
    fixture_name = (case_directory / FIXTURE_FILE).read_text(encoding='utf-8').strip()

    if fixture_name not in eval_fixtures.FIXTURE_NAMES:
        unknown = f'{case_directory}: {FIXTURE_FILE} names {fixture_name!r}, which is not a fixture'

        raise ValueError(unknown)

    case_yaml = case_directory / 'case.yaml'
    names_script = case_yaml.is_file() and SCAFFOLD_FILE in case_yaml.read_text(encoding='utf-8')

    if not names_script:
        unnamed = f'{case_directory}: a case with a {FIXTURE_FILE} names `context.scaffold_script: {SCAFFOLD_FILE}` in case.yaml'

        raise ValueError(unnamed)

    shutil.copytree(
        fixtures_directory / fixture_name,
        target / FIXTURE_FOLDER,
    )
    script = target / SCAFFOLD_FILE
    script.write_text(
        SCAFFOLD_SCRIPT,
        encoding='utf-8',
        newline='\n',
    )
    script.chmod(0o755)


def _allowed_tools_text(
    text: str,
) -> str:
    """
    What an `allowed_tools` key holds in YAML text, inline or as a block list; empty when absent.
    """
    lines = text.splitlines()
    starts = [
        index
        for index, line
        in enumerate(lines)
        if ALLOWED_TOOLS_LINE.match(line)
    ]

    if not starts:

        return ''

    first = starts[0]
    inline = ALLOWED_TOOLS_LINE.match(lines[first]).group(1)
    items = list(itertools.takewhile(
        LIST_ITEM_LINE.match,
        lines[first + 1:],
    ))
    held = '\n'.join([
        inline,
        *items,
    ])

    return held


def _authored_case_directories(
    source_directory: pathlib.Path,
) -> list[pathlib.Path]:
    """
    Every committed case folder of the authored layers: each folder holding a prompt.md or case.yaml.
    """
    case_files = [
        path
        for layer
        in AUTHORED_LAYERS
        for file_name
        in CASE_FILES
        for path
        in (source_directory / layer).rglob(file_name)
    ]
    directories = sorted({
        path.parent
        for path
        in case_files
    })

    return directories


def _build_parser() -> argparse.ArgumentParser:
    """
    The command line: which cases, how many runs, the cost ceiling, the shell, and a dry run.
    """
    parser = argparse.ArgumentParser(
        description="Run the KaxaNuk Researcher's evals against a fresh install.",
    )
    parser.add_argument(
        '--case',
        default='*',
        help=' '.join([
            "a glob over case names, such as 'contract/read/*'; only * works:",
            'braces and brackets match nothing',
        ]),
    )
    parser.add_argument(
        '--runs',
        type=int,
        default=3,
        help='runs per case; a case passes when every run passes',
    )
    parser.add_argument(
        '--max-cost-usd',
        type=float,
        required=True,
        help="the harness's cost ceiling for this batch; the run stops when it is reached",
    )
    parser.add_argument(
        '--no-shell',
        action='store_true',
        help='leave out every case that grants Bash, and grant only Write and Edit',
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='build and assemble, print the command, and run nothing',
    )

    return parser


def _fires_cases(
    skill: str,
    requests: list[str],
) -> dict[str, str]:
    """
    The cases of the requests that should fire a skill.
    """
    cases = {}

    for number, request in enumerate(requests, start=1):
        name = f'triggering/{skill}/fires-{number}'
        cases[f'{name}/prompt.md'] = TRIGGERING_FRONTMATTER.format(
            name=name,
            request=request,
        )
        cases[f'{name}/graders/fired.md'] = FIRED_GRADER.format(skill=skill)

    return cases


def _frontmatter(
    text: str,
) -> str:
    """
    The frontmatter of a Markdown file, between its opening and closing `---`; empty when it has none.
    """
    if not text.startswith('---'):

        return ''

    closing = text.find(
        '\n---',
        3,
    )
    front = text[3:closing] if closing != -1 else ''

    return front


def _grants_shell(
    case_directory: pathlib.Path,
) -> bool:
    """
    Whether a case lists Bash in its `allowed_tools`, in prompt.md's frontmatter or in case.yaml.
    """
    prompt = _read_if_present(case_directory / 'prompt.md')
    texts = [
        _frontmatter(prompt),
        _read_if_present(case_directory / 'case.yaml'),
    ]
    grants_held = [
        _allowed_tools_text(text)
        for text
        in texts
    ]
    grants = any(
        SHELL_TOOL.search(held)
        for held
        in grants_held
    )

    return grants


def _install_into_run(
    home: pathlib.Path,
) -> bool:
    """
    Install into a throwaway home, and copy the plugin and the starting points into the run folder.
    """
    try:
        claude_directory = build_install(
            REPOSITORY_ROOT,
            home,
        )
    except subprocess.CalledProcessError as error:
        print(f'The install could not be built: apm exited with {error.returncode}')

        return False

    package_directory = home / INSTALLED_PACKAGE

    if not package_directory.is_dir():
        print(f'apm did not put the package where the runner looks: {package_directory}')

        return False

    assemble_plugin(
        claude_directory,
        PLUGIN_DIRECTORY,
    )
    copy_starting_points(
        package_directory,
        RUN_DIRECTORY,
    )

    return True


def _near_miss_cases(
    skill: str,
    requests: list[str],
) -> dict[str, str]:
    """
    The cases of the near-misses: requests that must not fire a skill.
    """
    cases = {}

    for number, request in enumerate(requests, start=1):
        name = f'triggering/{skill}/near-miss-{number}'
        cases[f'{name}/prompt.md'] = TRIGGERING_FRONTMATTER.format(
            name=name,
            request=request,
        )
        cases[f'{name}/graders/not-fired.md'] = NOT_FIRED_GRADER.format(skill=skill)

    return cases


def _read_if_present(
    path: pathlib.Path,
) -> str:
    """
    A text file's content, or empty when there is no such file.
    """
    text = path.read_text(encoding='utf-8') if path.is_file() else ''

    return text


def _read_table(
    path: pathlib.Path,
) -> dict[str, dict[str, list[str]]]:
    """
    The triggering table: per skill, the requests that should fire it and the near-misses.
    """
    with path.open('rb') as handle:
        table = tomllib.load(handle)

    return table


def _write_cases(
    eval_directory: pathlib.Path,
    cases: dict[str, str],
) -> None:
    """
    Write generated case files below the eval folder.
    """
    for relative_path, text in cases.items():
        target = eval_directory / relative_path
        target.parent.mkdir(
            parents=True,
            exist_ok=True,
        )
        target.write_text(
            text,
            encoding='utf-8',
            newline='\n',
        )


if __name__ == '__main__':
    sys.exit(main())
