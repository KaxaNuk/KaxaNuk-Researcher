"""
Run the KaxaNuk Researcher's evals against what a user actually installs.

It exports the repository's working tree without its ignored files (what `git ls-files --cached
--others --exclude-standard` lists, so uncommitted edits count and `evals/results/` does not) into a
temporary folder, builds the real `apm install -g <that export> --target claude` into a throwaway
home beside it, outside the repository, and assembles `evals/.run/` from the install:

    evals/.run/plugin/             the plugin the harness runs: skills/, commands/, a minimal
                                   .claude-plugin/plugin.json, and the batch's cases in evals/
    evals/.run/templates/          the three starting points, copied from where apm put the package,
    evals/.run/examples/           so `scaffold.py` finds them beside the plugin (its `parents[4]`)
    evals/.run/fixtures/           every fixture, built fresh from the export's templates

Only the cases whose name matches `--case` are assembled: the committed contract and quality cases,
and the triggering cases generated from `evals/triggering/requests.toml`.  The tools a case lists in
its `allowed_tools` are the single source of its grants: the batch is granted, with `--allow-tools`,
exactly the gated tools (Bash, Write, Edit, ...) its cases list, and nothing when they list none.
`allowed_tools` is a one-line list in `prompt.md`'s frontmatter; anything else stops the run.

A case folder that holds a one-line `FIXTURE` file naming a fixture gets a real copy of it in
`fixture/` and a `scaffold.sh` that copies it into the empty workspace; its `case.yaml` names
`scaffold_script: scaffold.sh` itself.  A case whose case.yaml names a `history_file` it does not
hold stops the run, naming the capture step.  Then `claude plugin eval` runs on the plugin folder.
Sessions run on Opus 5.5 and the quality judge on Fable 5.1; the no-plugin comparison arm is off.
`--case` may be repeated: the batch is the union of the cases its globs match, and the harness is
given `--case '*'` over a plugin that holds only those.  Each batch writes its results and report to
its own `evals/results/<UTC time>-<label or cases>/`, and keeps every run's folder under
/tmp/claude-eval-* for diagnosis.

Every triggering run ends with the error "Reached maximum number of turns (2)": the case stops as
soon as the skill is chosen, and the run is still graded.  The error is expected there.

Run from the repository root:

    uv run --no-project --with pypdf python tools/eval_run.py --case 'triggering/*' --max-cost-usd 5
    uv run --no-project --with pypdf python tools/eval_run.py --case 'contract/read/*' --dry-run \
      --max-cost-usd 1

`--no-shell` leaves out every case that lists Bash, for a machine whose sandbox cannot run a shell.
Every run spends the plan of whoever runs it; `--max-cost-usd` is required for that reason.
Exit code: the harness's, or 1 with a one-line message when a case is malformed or lacks its
history, no case matches, or the export, the install or the fixtures cannot be built.  Console
output is ASCII only.
"""
import argparse
import dataclasses
import datetime
import json
import os
import pathlib
import re
import shlex
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
# The export and the throwaway home live outside the repository: apm copies the whole folder it
# installs, ignored files included, so a home inside it would be copied into itself.
INSTALL_PREFIX = 'kaxanuk-eval-install-'
# The export's folder name, which apm uses as the package's name below `_local/`.
PACKAGE_NAME = 'KaxaNuk-Researcher'
# Where `apm install -g <a local path>` puts the package, below the home it installs into.
INSTALLED_PACKAGE = pathlib.Path('.apm') / 'apm_modules' / '_local' / PACKAGE_NAME
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
SCAFFOLD_LINE = re.compile(r'^\s*scaffold_script:\s*scaffold\.sh\s*(#.*)?$')
HISTORY_LINE = re.compile(r'^\s*history_file\s*:(.*)$')
ALLOWED_TOOLS_LINE = re.compile(r'^(\s*)allowed_tools\s*:(.*)$')
NAME_LINE = re.compile(r'^name\s*:(.*)$')
FLOW_LIST = re.compile(r'\[([^\[\]]*)\]')
TRAILING_COMMENT = re.compile(r'(^|\s+)#.*$')
# The tools a case's `allowed_tools` grants by itself; every other tool needs the operator's grant.
READ_ONLY_TOOLS = (
    'Read',
    'Glob',
    'Grep',
    'NotebookRead',
    'Skill',
    'Agent',
    'TodoWrite',
    'TaskCreate',
    'TaskGet',
    'TaskList',
    'TaskUpdate',
    'TaskStop',
)
# The tools that need the sandbox: a case listing one is left out under --no-shell.
SHELL_TOOLS = (
    'Bash',
    'PowerShell',
)
JUDGE_MODEL = 'claude-fable-5-1'
SESSION_MODEL = 'claude-opus-5-5'
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


@dataclasses.dataclass(frozen=True)
class EvalCase:
    """
    One case as the runner sees it: the name `--case` matches, its folder below the eval folder,
    the tools it lists, and, for a committed case, the folder it comes from, its fixture and the
    replayed history its case.yaml names.
    """
    name: str
    folder: str
    tools: tuple[str, ...]
    source: pathlib.Path | None = None
    fixture: str | None = None
    history: str | None = None


@dataclasses.dataclass(frozen=True)
class Selection:
    """
    The cases of one batch, and the ones `--no-shell` left out of it.
    """
    selected: tuple[EvalCase, ...]
    left_out: tuple[EvalCase, ...]


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
    # uv finds its cache through HOME; keep the real one, so apm-cli is not downloaded again.
    environment = {
        **os.environ,
        'HOME': str(home),
        'USERPROFILE': str(home),
        'UV_CACHE_DIR': _uv_cache_directory(),
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


def case_matches(
    case_glob: str,
    name: str,
) -> bool:
    """
    Whether a case name matches a `--case` glob as the harness reads it.

    The harness turns `*` into any run of characters, `/` included, and `?` into one character;
    every other character, brackets and braces too, stands for itself.
    """
    pattern = ''.join(
        _glob_part(character)
        for character
        in case_glob
    )
    matched = re.fullmatch(
        pattern,
        name,
    )

    return matched is not None


def check_histories(
    cases: tuple[EvalCase, ...],
) -> None:
    """
    Raise ValueError naming the first case whose case.yaml names a history file it does not hold.

    A replayed first turn is captured on a host that can run it, then committed; until it is, the
    case cannot run, and the harness would be handed a path to nothing.
    """
    missing = [
        case
        for case
        in cases
        if case.history is not None and not (case.source / case.history).is_file()
    ]

    if missing:
        uncaptured = ' '.join([
            f'{missing[0].name}: case.yaml names {missing[0].history}, which is not there;',
            'capture it first, as "Replayed turns" in evals/README.md says (tools/eval_history.py)',
        ])

        raise ValueError(uncaptured)


def copy_authored_case(
    case: EvalCase,
    eval_directory: pathlib.Path,
    fixtures_directory: pathlib.Path,
) -> None:
    """
    Copy a committed case below the eval folder, with its fixture and the script that seeds it.
    """
    target = eval_directory / case.folder
    shutil.copytree(
        case.source,
        target,
    )

    if case.fixture is None:

        return

    shutil.copytree(
        fixtures_directory / case.fixture,
        target / FIXTURE_FOLDER,
    )
    script = target / SCAFFOLD_FILE
    script.write_text(
        SCAFFOLD_SCRIPT,
        encoding='utf-8',
        newline='\n',
    )
    script.chmod(0o755)


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
    runs: int | None,
    max_cost_usd: float,
    output_directory: pathlib.Path,
    granted_tools: list[str],
) -> list[str]:
    """
    The `claude plugin eval` command for one batch; the plugin folder comes first, as the harness asks.

    The plugin holds only the batch's cases, so the harness is given `--case '*'`, however many
    globs chose them.  `--allow-tools` names exactly `granted_tools`, and is left out when there are
    none; `--runs` is passed only when given, so a case's own `runs` counts otherwise.
    """
    grant = ['--allow-tools', *granted_tools] if granted_tools else []
    run_count = ['--runs', str(runs)] if runs is not None else []
    command = [
        'claude',
        'plugin',
        'eval',
        str(plugin_directory),
        *grant,
        '--case',
        '*',
        *run_count,
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


def export_package(
    repository: pathlib.Path,
    destination: pathlib.Path,
) -> None:
    """
    Copy the repository's working tree into `destination`, leaving out every file git ignores.

    The files are those `git ls-files --cached --others --exclude-standard` lists, with their
    content as it is on disk: uncommitted edits and new files count, ignored ones do not.
    """
    listed = subprocess.run(
        [
            'git',
            '-C',
            str(repository),
            'ls-files',
            '--cached',
            '--others',
            '--exclude-standard',
            '-z',
        ],
        check=True,
        capture_output=True,
    )
    relative_paths = [
        entry.decode('utf-8')
        for entry
        in listed.stdout.split(b'\0')
        if entry
    ]

    for relative_path in relative_paths:
        source = repository / relative_path

        if not source.is_file():

            continue

        target = destination / relative_path
        target.parent.mkdir(
            parents=True,
            exist_ok=True,
        )
        shutil.copy2(
            source,
            target,
        )


def gated_tools(
    cases: list[EvalCase],
) -> dict[str, list[str]]:
    """
    Every tool the cases list that needs the operator's grant, with the names of the cases listing it.
    """
    listings = [
        (tool, case.name)
        for case
        in cases
        for tool
        in case.tools
        if _base_tool(tool) not in READ_ONLY_TOOLS
    ]
    listers = {}

    for tool, name in listings:
        listers.setdefault(tool, []).append(name)

    ordered = {
        tool: listers[tool]
        for tool
        in sorted(listers)
    }

    return ordered


def generated_cases(
    files: dict[str, str],
) -> list[EvalCase]:
    """
    The generated cases among files keyed by their path below the eval folder, one per prompt.md.
    """
    folders = sorted(
        path.removesuffix('/prompt.md')
        for path
        in files
        if path.endswith('/prompt.md')
    )
    cases = [
        _generated_case(
            folder,
            files[f'{folder}/prompt.md'],
        )
        for folder
        in folders
    ]

    return cases


def grants_shell(
    case: EvalCase,
) -> bool:
    """
    Whether a case lists a shell tool, which runs only where the sandbox can confine it.
    """
    shelled = any(
        _base_tool(tool) in SHELL_TOOLS
        for tool
        in case.tools
    )

    return shelled


def main(
    arguments: list[str] | None = None,
) -> int:
    """
    Check the cases, build the install, assemble the run folder, and run one batch.
    """
    parser = _build_parser()
    parsed = parser.parse_args(arguments)

    try:
        exit_code = _run_batch(parsed)
    except (
        OSError,
        ValueError,
        subprocess.CalledProcessError,
    ) as error:
        print(f'eval_run: stopped: {_one_line(error)}')

        return 1

    return exit_code


def read_authored_cases(
    source_directory: pathlib.Path,
) -> list[EvalCase]:
    """
    Every committed case of the authored layers, checked; raises ValueError naming a malformed one.
    """
    cases = [
        _read_authored_case(
            case_directory,
            source_directory,
        )
        for case_directory
        in _authored_case_directories(source_directory)
    ]

    return cases


def results_directory(
    case_globs: list[str],
    started: datetime.datetime,
    label: str | None = None,
) -> pathlib.Path:
    """
    The folder of one batch's results, named by its UTC start and its label, else its case globs.

    No batch overwrites another.
    """
    stamp = started.astimezone(datetime.UTC).strftime('%Y%m%dT%H%M%SZ')
    named = label if label else ' '.join(case_globs)
    spelled = named.replace(
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


def select_cases(
    cases: list[EvalCase],
    case_globs: list[str],
    no_shell: bool,
) -> Selection:
    """
    The cases whose name matches any of the globs, each once, in their order; with `no_shell`,
    those listing a shell tool are left out.
    """
    matching = [
        case
        for case
        in cases
        if _matches_any(
            case_globs,
            case.name,
        )
    ]
    left_out = tuple(
        case
        for case
        in matching
        if no_shell and grants_shell(case)
    )
    selected = tuple(
        case
        for case
        in matching
        if case not in left_out
    )
    selection = Selection(
        selected=selected,
        left_out=left_out,
    )

    return selection


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


def _allowed_tools(
    frontmatter: list[str],
    folder: str,
) -> tuple[str, ...]:
    """
    The tools a case's frontmatter lists; raises ValueError unless it is one line of flow list.
    """
    found = [
        ALLOWED_TOOLS_LINE.match(line)
        for line
        in frontmatter
        if ALLOWED_TOOLS_LINE.match(line)
    ]

    if not found:
        no_tools: tuple[str, ...] = ()

        return no_tools

    value = _strip_comment(found[0].group(2))
    listed = FLOW_LIST.fullmatch(value)

    if len(found) > 1 or found[0].group(1) or listed is None:
        malformed = ' '.join([
            f'{folder}: allowed_tools must be one line of list in prompt.md,',
            'such as allowed_tools: [Read, Write]',
        ])

        raise ValueError(malformed)

    tools = tuple(
        item.strip().strip('\'"')
        for item
        in listed.group(1).split(',')
        if item.strip()
    )

    return tools


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


def _base_tool(
    tool: str,
) -> str:
    """
    A tool's name without its pattern: `Bash` for `Bash(npm test *)`.
    """
    base = tool.split('(')[0].strip()

    return base


def _build_parser() -> argparse.ArgumentParser:
    """
    The command line: which cases, their label, how many runs, the cost ceiling, the shell, and a
    dry run.
    """
    parser = argparse.ArgumentParser(
        description="Run the KaxaNuk Researcher's evals against a fresh install.",
    )
    parser.add_argument(
        '--case',
        action='append',
        default=None,
        help=' '.join([
            "a glob over case names, such as 'contract/read/*': * matches any run of characters,",
            '/ included, and ? one character; braces and brackets stand for themselves;',
            'repeat it to run the union of several globs as one batch (default: every case)',
        ]),
    )
    parser.add_argument(
        '--label',
        default=None,
        help="names the batch's results folder; by default its case globs do",
    )
    parser.add_argument(
        '--runs',
        type=int,
        default=None,
        help="runs per case; by default each case's own runs, else 3",
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
        help='leave out every case that lists Bash, for a machine whose sandbox cannot run a shell',
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='build and assemble, print the command, and run nothing',
    )

    return parser


def _case_name(
    frontmatter: list[str],
    case_yaml_lines: list[str],
    folder: str,
) -> str:
    """
    The name a case gives itself, in prompt.md's frontmatter or else in case.yaml.
    """
    values = [
        NAME_LINE.match(line).group(1)
        for line
        in [
            *frontmatter,
            *case_yaml_lines,
        ]
        if NAME_LINE.match(line)
    ]
    names = [
        _strip_comment(value).strip('\'"')
        for value
        in values
    ]

    if not names or not names[0]:
        unnamed = f'{folder}: the case has no name; add name: {folder} to its prompt.md'

        raise ValueError(unnamed)

    return names[0]


def _describe(
    error: Exception,
) -> str:
    """
    What went wrong, in words: a failed command by its program and exit code.
    """
    if isinstance(error, subprocess.CalledProcessError):
        program = pathlib.Path(str(error.cmd[0])).name
        failed = f'{program} exited with {error.returncode}'

        return failed

    return str(error)


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


def _fixture_name(
    case_directory: pathlib.Path,
    case_yaml_lines: list[str],
    folder: str,
) -> str | None:
    """
    The fixture a committed case names, checked against the scaffold rules; None when it names none.
    """
    committed = [
        reserved
        for reserved
        in (
            FIXTURE_FOLDER,
            SCAFFOLD_FILE,
        )
        if (case_directory / reserved).exists()
    ]

    if committed:
        runner_owned = f'{folder}: {committed[0]} is written by the runner; do not commit it'

        raise ValueError(runner_owned)

    names_script = any(
        SCAFFOLD_LINE.match(line)
        for line
        in case_yaml_lines
    )
    fixture_file = case_directory / FIXTURE_FILE

    if not fixture_file.is_file():
        if names_script:
            no_fixture = f'{folder}: case.yaml names {SCAFFOLD_FILE}, but the case has no {FIXTURE_FILE}'

            raise ValueError(no_fixture)

        return None

    fixture_name = fixture_file.read_text(encoding='utf-8').strip()

    if fixture_name not in eval_fixtures.FIXTURE_NAMES:
        unknown = f'{folder}: {FIXTURE_FILE} names {fixture_name!r}, which is not a fixture'

        raise ValueError(unknown)

    if not names_script:
        unnamed = f'{folder}: a case with a {FIXTURE_FILE} needs scaffold_script: {SCAFFOLD_FILE} in case.yaml'

        raise ValueError(unnamed)

    return fixture_name


def _frontmatter_lines(
    text: str,
) -> list[str]:
    """
    The lines between a Markdown file's opening and closing `---`; empty when it has none.
    """
    lines = text.splitlines()

    if not lines or lines[0].strip() != '---':

        return []

    closings = [
        index
        for index, line
        in enumerate(lines)
        if index > 0 and line.strip() == '---'
    ]
    front = lines[1:closings[0]] if closings else []

    return front


def _generated_case(
    folder: str,
    prompt_text: str,
) -> EvalCase:
    """
    A generated case, read from its prompt.md as a committed one would be.
    """
    frontmatter = _frontmatter_lines(prompt_text)
    case = EvalCase(
        name=_case_name(
            frontmatter,
            [],
            folder,
        ),
        folder=folder,
        tools=_allowed_tools(
            frontmatter,
            folder,
        ),
    )

    return case


def _glob_part(
    character: str,
) -> str:
    """
    One character of a `--case` glob as a regular expression, as the harness translates it.
    """
    translations = {
        '*': '.*',
        '?': '.',
    }
    part = translations.get(character, re.escape(character))

    return part


def _history_name(
    case_yaml_lines: list[str],
) -> str | None:
    """
    The history file a case.yaml names in `context.history_file`; None when it names none.
    """
    values = [
        HISTORY_LINE.match(line).group(1)
        for line
        in case_yaml_lines
        if HISTORY_LINE.match(line)
    ]
    names = [
        _strip_comment(value).strip('\'"')
        for value
        in values
    ]
    history = names[0] if names and names[0] else None

    return history


def _matches_any(
    case_globs: list[str],
    name: str,
) -> bool:
    """
    Whether a case name matches at least one of the `--case` globs.
    """
    matched = any(
        case_matches(
            case_glob,
            name,
        )
        for case_glob
        in case_globs
    )

    return matched


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


def _one_line(
    error: Exception,
) -> str:
    """
    An error as one line of ASCII.
    """
    described = _describe(error)
    flattened = ' '.join(described.split())
    ascii_only = flattened.encode(
        'ascii',
        'replace',
    ).decode('ascii')

    return ascii_only


def _prepare_run(
    install_folder: pathlib.Path,
) -> None:
    """
    Export and install into a temporary folder; copy the plugin, starting points and fixtures out.
    """
    export = install_folder / PACKAGE_NAME
    export_package(
        REPOSITORY_ROOT,
        export,
    )
    claude_directory = build_install(
        export,
        install_folder / 'home',
    )
    package_directory = install_folder / 'home' / INSTALLED_PACKAGE

    if not package_directory.is_dir():
        misplaced = f'apm did not put the package where the runner looks: {package_directory}'

        raise FileNotFoundError(misplaced)

    assemble_plugin(
        claude_directory,
        PLUGIN_DIRECTORY,
    )
    copy_starting_points(
        package_directory,
        RUN_DIRECTORY,
    )
    eval_fixtures.build_all(
        FIXTURES_DIRECTORY,
        package_root=export,
    )


def _print_grants(
    grants: dict[str, list[str]],
) -> None:
    """
    Say which gated tools the batch is granted, and which cases list each.
    """
    if not grants:
        print('Granted: nothing beyond the read-only tools')

        return

    for tool, names in grants.items():
        print(f'Granted {tool}, listed by: {", ".join(names)}')


def _read_authored_case(
    case_directory: pathlib.Path,
    source_directory: pathlib.Path,
) -> EvalCase:
    """
    One committed case, checked: its name, its one-line tool list, and its fixture.
    """
    folder = case_directory.relative_to(source_directory).as_posix()
    frontmatter = _frontmatter_lines(_read_if_present(case_directory / 'prompt.md'))
    case_yaml_lines = _read_if_present(case_directory / 'case.yaml').splitlines()
    in_case_yaml = any(
        ALLOWED_TOOLS_LINE.match(line)
        for line
        in case_yaml_lines
    )

    if in_case_yaml:
        misplaced = f'{folder}: allowed_tools belongs in prompt.md frontmatter, not in case.yaml'

        raise ValueError(misplaced)

    case = EvalCase(
        name=_case_name(
            frontmatter,
            case_yaml_lines,
            folder,
        ),
        folder=folder,
        tools=_allowed_tools(
            frontmatter,
            folder,
        ),
        source=case_directory,
        fixture=_fixture_name(
            case_directory,
            case_yaml_lines,
            folder,
        ),
        history=_history_name(case_yaml_lines),
    )

    return case


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


def _run_batch(
    parsed: argparse.Namespace,
) -> int:
    """
    Select and check the batch's cases, assemble the run folder, and run the harness on it.
    """
    generated_files = triggering_cases(_read_table(TRIGGERING_TABLE))
    every_case = [
        *read_authored_cases(EVALS_DIRECTORY),
        *generated_cases(generated_files),
    ]
    case_globs = parsed.case if parsed.case else ['*']
    selection = select_cases(
        every_case,
        case_globs,
        parsed.no_shell,
    )

    for left in selection.left_out:
        print(f'Left out (lists Bash, --no-shell): {left.name}')

    if not selection.selected:
        asked = ' '.join(
            f'--case {case_glob!r}'
            for case_glob
            in case_globs
        )
        print(f'No case matches {asked}')

        return 1

    check_histories(selection.selected)
    grants = gated_tools(list(selection.selected))
    _print_grants(grants)
    shutil.rmtree(
        RUN_DIRECTORY,
        ignore_errors=True,
    )

    with tempfile.TemporaryDirectory(prefix=INSTALL_PREFIX) as install_folder:
        _prepare_run(pathlib.Path(install_folder))

    _write_selected(
        selection.selected,
        generated_files,
    )
    command = eval_command(
        PLUGIN_DIRECTORY,
        runs=parsed.runs,
        max_cost_usd=parsed.max_cost_usd,
        output_directory=results_directory(
            case_globs,
            datetime.datetime.now(datetime.UTC),
            label=parsed.label,
        ),
        granted_tools=list(grants),
    )
    print(shlex.join(command))

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


def _strip_comment(
    value: str,
) -> str:
    """
    A YAML value without its trailing comment and surrounding spaces.
    """
    stripped = TRAILING_COMMENT.sub(
        '',
        value,
    ).strip()

    return stripped


def _uv_cache_directory() -> str:
    """
    The uv cache of the environment this runs in: UV_CACHE_DIR when set, else what `uv cache dir` says.
    """
    given = os.environ.get('UV_CACHE_DIR')

    if given:

        return given

    answered = subprocess.run(
        [
            'uv',
            'cache',
            'dir',
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    cache = answered.stdout.strip()

    return cache


def _write_selected(
    cases: tuple[EvalCase, ...],
    generated_files: dict[str, str],
) -> None:
    """
    Put the batch's cases below the plugin's eval folder: committed ones copied, generated ones written.
    """
    eval_directory = PLUGIN_DIRECTORY / 'evals'

    for case in cases:
        if case.source is not None:
            copy_authored_case(
                case,
                eval_directory,
                FIXTURES_DIRECTORY,
            )

            continue

        for relative_path, text in generated_files.items():
            if relative_path.startswith(f'{case.folder}/'):
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
