"""
Unit tests for tools/eval_run.py: the plugin it assembles, the cases it selects and checks, the command it runs.
"""
import datetime
import pathlib
import re
import shutil
import stat
import subprocess

import pytest

import eval_run
import scaffold

# A Skill call's input as the harness JSON-encodes it, and as the notes of step zero printed it.
SKILL_INPUT_COMPACT = '{"skill":"kaxanuk-researcher-evals:query","args":"What does my library say?"}'
SKILL_INPUT_SPACED = '{"skill": "kaxanuk-researcher-evals:query", "args": "What does my library say?"}'
QUERY_TABLE = {
    'query': {
        'fires': ['What does my library say about momentum?'],
        'near_miss': [],
    },
}
QUERY_TABLE_TOML = '\n'.join([
    '[query]',
    'fires = ["What does my library say about momentum?"]',
    'near_miss = []',
    '',
])
FIXTURE_CASE_YAML = '\n'.join([
    'schema_version: "1.1"',
    'name: contract/read/with-book',
    'context:',
    '  scaffold_script: scaffold.sh   # written by the runner',
    '',
])
HISTORY_CASE_YAML = '\n'.join([
    'schema_version: "1.1"',
    'name: contract/read/after-go',
    'context:',
    '  history_file: history.jsonl   # captured on a host with a shell',
    '',
])
TOOLS_IN_CASE_YAML = '\n'.join([
    'schema_version: "1.1"',
    'name: contract/read/bad',
    'execution:',
    '  allowed_tools: [Read, Bash]',
    '',
])
SCAFFOLD_SCRIPT_TEXT = '\n'.join([
    '#!/usr/bin/env bash',
    'set -euo pipefail',
    'here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"',
    'cp -r "$here/fixture/." .',
    '',
])


def committed_case(
    root: pathlib.Path,
    folder: str,
    frontmatter: list[str],
) -> pathlib.Path:
    """
    A committed case folder below `root/source`, with a prompt.md holding the given frontmatter.
    """
    case_directory = root / 'source' / folder
    prompt = '\n'.join([
        '---',
        *frontmatter,
        '---',
        'Read the book.',
        '',
    ])
    write(
        case_directory / 'prompt.md',
        prompt,
    )

    return case_directory


def eval_case(
    name: str,
    tools: tuple[str, ...],
) -> eval_run.EvalCase:
    """
    A generated case with a name and a tool list, for selection and grants.
    """
    case = eval_run.EvalCase(
        name=name,
        folder=name,
        tools=tools,
    )

    return case


def fail_like_a_missing_program(
    repository: pathlib.Path,
    destination: pathlib.Path,
) -> None:
    """
    Stand in for the export when git is not installed.
    """
    missing = FileNotFoundError(
        2,
        'No such file or directory',
        'git',
    )

    raise missing


def fail_like_uvx(
    repository: pathlib.Path,
    destination: pathlib.Path,
) -> None:
    """
    Stand in for a step whose command fails, as a failed install does.
    """
    failed = subprocess.CalledProcessError(
        1,
        [
            'uvx',
            '--from',
            'apm-cli',
        ],
    )

    raise failed


def history_case(
    eval_directory: pathlib.Path,
) -> pathlib.Path:
    """
    A committed after-the-go case below `eval_directory` whose case.yaml names a history file.
    """
    case_directory = eval_directory / 'contract' / 'read' / 'after-go'
    write(
        case_directory / 'prompt.md',
        '---\nname: contract/read/after-go\n---\nGo.\n',
    )
    write(
        case_directory / 'case.yaml',
        HISTORY_CASE_YAML,
    )

    return case_directory


def input_match(
    grader: str,
) -> str:
    """
    The `input_match` regex of a generated grader, as the harness reads it from single-quoted YAML.
    """
    found = next(
        candidate
        for candidate
        in grader.splitlines()
        if candidate.startswith('input_match: ')
    )
    quoted = found.removeprefix('input_match: ')
    pattern = quoted[1:-1].replace(
        "''",
        "'",
    )

    return pattern


def point_at(
    monkeypatch: pytest.MonkeyPatch,
    root: pathlib.Path,
) -> None:
    """
    Point the runner's folders and table below `root`, so nothing in the repository is touched.
    """
    write(
        root / 'evals' / 'triggering' / 'requests.toml',
        QUERY_TABLE_TOML,
    )
    monkeypatch.setattr(
        eval_run,
        'EVALS_DIRECTORY',
        root / 'evals',
    )
    monkeypatch.setattr(
        eval_run,
        'TRIGGERING_TABLE',
        root / 'evals' / 'triggering' / 'requests.toml',
    )
    monkeypatch.setattr(
        eval_run,
        'RUN_DIRECTORY',
        root / 'run',
    )
    monkeypatch.setattr(
        eval_run,
        'PLUGIN_DIRECTORY',
        root / 'run' / 'plugin',
    )
    monkeypatch.setattr(
        eval_run,
        'FIXTURES_DIRECTORY',
        root / 'run' / 'fixtures',
    )


def write(
    path: pathlib.Path,
    text: str,
) -> None:
    """
    Write a text file, creating its folder.
    """
    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    path.write_text(
        text,
        encoding='utf-8',
    )


class TestAssemblePlugin:
    def test_skills_commands_and_manifest_land_in_the_run_folder(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        claude = tmp_path / 'home' / '.claude'
        write(claude / 'skills' / 'query' / 'SKILL.md', 'query')
        write(claude / 'commands' / 'blueprint.md', 'blueprint')
        run = tmp_path / 'run'
        eval_run.assemble_plugin(
            claude,
            run,
        )
        present = sorted(
            path.relative_to(run).as_posix()
            for path
            in run.rglob('*')
            if path.is_file()
        )

        assert present == [
            '.claude-plugin/plugin.json',
            'commands/blueprint.md',
            'skills/query/SKILL.md',
        ]


class TestCaseMatches:
    def test_a_question_mark_is_one_character(
        self,
    ) -> None:
        assert eval_run.case_matches(
            'triggering/query/fires-?',
            'triggering/query/fires-1',
        )

    def test_a_star_crosses_slashes(
        self,
    ) -> None:
        assert eval_run.case_matches(
            'triggering/*',
            'triggering/query/fires-1',
        )

    def test_brackets_stand_for_themselves(
        self,
    ) -> None:
        assert not eval_run.case_matches(
            'triggering/[q]uery/*',
            'triggering/query/fires-1',
        )

    def test_the_whole_name_must_match(
        self,
    ) -> None:
        assert not eval_run.case_matches(
            'contract/read/*',
            'contract/query/after-go',
        )


class TestCheckHistories:
    def test_a_captured_history_lets_the_case_run(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        case_directory = history_case(tmp_path / 'source')
        write(
            case_directory / 'history.jsonl',
            '{"type": "user"}\n',
        )
        cases = eval_run.read_authored_cases(tmp_path / 'source')
        eval_run.check_histories(tuple(cases))

        assert cases[0].history == 'history.jsonl'

    def test_a_case_without_history_needs_none(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        committed_case(
            tmp_path,
            'contract/read/first-turn',
            ['name: contract/read/first-turn'],
        )
        cases = eval_run.read_authored_cases(tmp_path / 'source')
        eval_run.check_histories(tuple(cases))

        assert cases[0].history is None

    def test_a_missing_history_is_refused_naming_the_capture(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        history_case(tmp_path / 'source')
        cases = eval_run.read_authored_cases(tmp_path / 'source')

        with pytest.raises(
            ValueError,
            match='contract/read/after-go: case.yaml names history.jsonl, which is not there; capture it first',
        ):
            eval_run.check_histories(tuple(cases))


class TestCopyAuthoredCase:
    def test_a_case_without_a_fixture_is_copied_alone(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        committed_case(
            tmp_path,
            'contract/read/plain',
            ['name: contract/read/plain'],
        )
        cases = eval_run.read_authored_cases(tmp_path / 'source')
        target = tmp_path / 'evals'
        eval_run.copy_authored_case(
            cases[0],
            target,
            tmp_path / 'fixtures',
        )
        present = sorted(
            path.relative_to(target).as_posix()
            for path
            in target.rglob('*')
            if path.is_file()
        )

        assert present == ['contract/read/plain/prompt.md']

    def test_a_named_fixture_is_copied_into_the_case_as_real_files(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        case_directory = committed_case(
            tmp_path,
            'contract/read/with-book',
            ['name: contract/read/with-book'],
        )
        write(case_directory / 'case.yaml', FIXTURE_CASE_YAML)
        write(case_directory / 'FIXTURE', 'home-with-book\n')
        write(tmp_path / 'fixtures' / 'home-with-book' / 'Sources' / 'book.md', 'a book')
        cases = eval_run.read_authored_cases(tmp_path / 'source')
        target = tmp_path / 'evals'
        eval_run.copy_authored_case(
            cases[0],
            target,
            tmp_path / 'fixtures',
        )
        copied = target / 'contract' / 'read' / 'with-book' / 'fixture' / 'Sources' / 'book.md'
        links = [
            path
            for path
            in target.rglob('*')
            if path.is_symlink()
        ]

        assert copied.read_text(encoding='utf-8') == 'a book'
        assert links == []

    def test_the_case_gets_an_executable_scaffold_that_copies_its_fixture(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        case_directory = committed_case(
            tmp_path,
            'contract/read/with-book',
            ['name: contract/read/with-book'],
        )
        write(case_directory / 'case.yaml', FIXTURE_CASE_YAML)
        write(case_directory / 'FIXTURE', 'home-with-book\n')
        write(tmp_path / 'fixtures' / 'home-with-book' / 'README.md', 'home')
        cases = eval_run.read_authored_cases(tmp_path / 'source')
        target = tmp_path / 'evals'
        eval_run.copy_authored_case(
            cases[0],
            target,
            tmp_path / 'fixtures',
        )
        script = target / 'contract' / 'read' / 'with-book' / 'scaffold.sh'
        mode = script.stat().st_mode

        assert script.read_text(encoding='utf-8') == SCAFFOLD_SCRIPT_TEXT
        assert mode & stat.S_IXUSR


class TestCopyStartingPoints:
    def test_the_scaffold_script_of_the_plugin_sees_the_run_folder_as_its_package(
        self,
    ) -> None:
        script = eval_run.PLUGIN_DIRECTORY / 'skills' / 'init-strategy' / 'scripts' / 'scaffold.py'

        assert script.parents[4] == eval_run.RUN_DIRECTORY

    def test_the_three_starting_points_land_beside_the_plugin(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        package = tmp_path / 'package'
        write(package / 'templates' / 'researcher' / 'RESEARCHER.md', 'home')
        write(package / 'templates' / 'strategy' / 'OBJECTIVE.md', 'objective')
        write(package / 'examples' / 'liquid-golden-cross' / 'README.md', 'example')
        write(package / 'docs' / 'notes.md', 'not a starting point')
        run = tmp_path / 'run'
        eval_run.copy_starting_points(
            package,
            run,
        )
        present = sorted(
            path.relative_to(run).as_posix()
            for path
            in run.rglob('*')
            if path.is_file()
        )

        assert present == [
            'examples/liquid-golden-cross/README.md',
            'templates/researcher/RESEARCHER.md',
            'templates/strategy/OBJECTIVE.md',
        ]
        assert scaffold.find_package(run, tmp_path) == run


class TestEvalCommand:
    def test_models_ablation_and_ceiling_are_pinned(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        command = eval_run.eval_command(
            tmp_path,
            runs=3,
            max_cost_usd=5.0,
            output_directory=tmp_path / 'results',
            granted_tools=['Write'],
        )
        joined = ' '.join(command)

        assert all(
            part in joined
            for part
            in (
                '--model claude-opus-5-5',
                '--judge-model claude-fable-5-1',
                '--ablation none',
                '--max-cost-usd 5.0',
                '--runs 3',
                '--scaffold',
                '--no-publish',
                '--trust-plugin',
                '--keep-temp',
            )
        )

    def test_no_grant_leaves_out_allow_tools(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        command = eval_run.eval_command(
            tmp_path,
            runs=None,
            max_cost_usd=1.0,
            output_directory=tmp_path / 'results',
            granted_tools=[],
        )

        assert '--allow-tools' not in command

    def test_results_and_report_go_to_the_batch_folder(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        output = tmp_path / 'results' / 'batch'
        command = eval_run.eval_command(
            tmp_path,
            runs=1,
            max_cost_usd=1.0,
            output_directory=output,
            granted_tools=[],
        )
        joined = ' '.join(command)

        assert f'--output-dir {output}' in joined
        assert f'--report {output / "report.html"}' in joined

    def test_runs_are_left_to_the_cases_unless_given(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        command = eval_run.eval_command(
            tmp_path,
            runs=None,
            max_cost_usd=1.0,
            output_directory=tmp_path / 'results',
            granted_tools=[],
        )

        assert '--runs' not in command

    def test_the_grant_names_exactly_the_tools_given(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        command = eval_run.eval_command(
            tmp_path,
            runs=1,
            max_cost_usd=1.0,
            output_directory=tmp_path / 'results',
            granted_tools=[
                'Bash(npm test *)',
                'Write',
            ],
        )
        start = command.index('--allow-tools')

        assert command[start:start + 4] == [
            '--allow-tools',
            'Bash(npm test *)',
            'Write',
            '--case',
        ]

    def test_the_harness_is_given_every_assembled_case(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        command = eval_run.eval_command(
            tmp_path,
            runs=None,
            max_cost_usd=1.0,
            output_directory=tmp_path / 'results',
            granted_tools=[],
        )
        start = command.index('--case')

        assert command[start:start + 2] == [
            '--case',
            '*',
        ]
        assert command.count('--case') == 1

    def test_the_plugin_folder_is_the_target_and_comes_first(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        command = eval_run.eval_command(
            tmp_path,
            runs=1,
            max_cost_usd=1.0,
            output_directory=tmp_path / 'results',
            granted_tools=['Write'],
        )

        assert command[:4] == [
            'claude',
            'plugin',
            'eval',
            str(tmp_path),
        ]


class TestExportPackage:
    @pytest.mark.skipif(
        shutil.which('git') is None,
        reason='git is not installed',
    )
    def test_tracked_and_untracked_files_are_exported_and_ignored_ones_are_not(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        repository = tmp_path / 'repository'
        write(repository / '.gitignore', 'results/\n')
        write(repository / 'tracked.md', 'edited after staging')
        write(repository / 'drafts' / 'untracked.md', 'new')
        write(repository / 'results' / 'report.html', 'ignored')
        subprocess.run(
            [
                'git',
                'init',
                '--quiet',
                str(repository),
            ],
            check=True,
        )
        subprocess.run(
            [
                'git',
                '-C',
                str(repository),
                'add',
                'tracked.md',
            ],
            check=True,
        )
        write(repository / 'tracked.md', 'edited on disk')
        export = tmp_path / 'export'
        eval_run.export_package(
            repository,
            export,
        )
        present = sorted(
            path.relative_to(export).as_posix()
            for path
            in export.rglob('*')
            if path.is_file()
        )

        assert present == [
            '.gitignore',
            'drafts/untracked.md',
            'tracked.md',
        ]
        assert (export / 'tracked.md').read_text(encoding='utf-8') == 'edited on disk'


class TestGatedTools:
    def test_each_gated_tool_names_the_cases_that_list_it(
        self,
    ) -> None:
        cases = [
            eval_case(
                'contract/read/runs-extract',
                (
                    'Skill',
                    'Read',
                    'Bash(uv run *)',
                    'Write',
                ),
            ),
            eval_case(
                'contract/read/writes',
                (
                    'Read',
                    'Write',
                ),
            ),
        ]

        assert eval_run.gated_tools(cases) == {
            'Bash(uv run *)': ['contract/read/runs-extract'],
            'Write': [
                'contract/read/runs-extract',
                'contract/read/writes',
            ],
        }

    def test_triggering_cases_need_no_grant(
        self,
    ) -> None:
        cases = eval_run.generated_cases(eval_run.triggering_cases(QUERY_TABLE))

        assert eval_run.gated_tools(cases) == {}


class TestMain:
    def test_a_failed_command_stops_with_one_line(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: pathlib.Path,
        capsys: pytest.CaptureFixture,
    ) -> None:
        point_at(
            monkeypatch,
            tmp_path,
        )
        monkeypatch.setattr(
            eval_run,
            'export_package',
            fail_like_uvx,
        )
        exit_code = eval_run.main([
            '--max-cost-usd',
            '1',
            '--dry-run',
        ])
        last_line = capsys.readouterr().out.splitlines()[-1]

        assert exit_code == 1
        assert last_line == 'eval_run: stopped: uvx exited with 1'

    def test_a_glob_that_matches_nothing_stops_before_any_install(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: pathlib.Path,
        capsys: pytest.CaptureFixture,
    ) -> None:
        point_at(
            monkeypatch,
            tmp_path,
        )
        monkeypatch.setattr(
            eval_run,
            'export_package',
            fail_like_uvx,
        )
        exit_code = eval_run.main([
            '--case',
            'nothing/*',
            '--max-cost-usd',
            '1',
            '--dry-run',
        ])

        assert exit_code == 1
        assert 'No case matches' in capsys.readouterr().out

    def test_a_malformed_case_stops_with_one_line_before_any_install(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: pathlib.Path,
        capsys: pytest.CaptureFixture,
    ) -> None:
        point_at(
            monkeypatch,
            tmp_path,
        )
        write(
            tmp_path / 'evals' / 'contract' / 'read' / 'bad' / 'case.yaml',
            TOOLS_IN_CASE_YAML,
        )
        monkeypatch.setattr(
            eval_run,
            'export_package',
            fail_like_uvx,
        )
        exit_code = eval_run.main([
            '--max-cost-usd',
            '1',
            '--dry-run',
        ])
        output = capsys.readouterr().out.splitlines()

        assert exit_code == 1
        assert len(output) == 1
        assert output[0].startswith('eval_run: stopped: contract/read/bad: allowed_tools')

    def test_a_missing_program_stops_with_one_line(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: pathlib.Path,
        capsys: pytest.CaptureFixture,
    ) -> None:
        point_at(
            monkeypatch,
            tmp_path,
        )
        monkeypatch.setattr(
            eval_run,
            'export_package',
            fail_like_a_missing_program,
        )
        exit_code = eval_run.main([
            '--max-cost-usd',
            '1',
            '--dry-run',
        ])
        last_line = capsys.readouterr().out.splitlines()[-1]

        assert exit_code == 1
        assert last_line == "eval_run: stopped: [Errno 2] No such file or directory: 'git'"

    def test_a_repeated_case_glob_that_matches_nothing_names_every_glob(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: pathlib.Path,
        capsys: pytest.CaptureFixture,
    ) -> None:
        point_at(
            monkeypatch,
            tmp_path,
        )
        monkeypatch.setattr(
            eval_run,
            'export_package',
            fail_like_uvx,
        )
        exit_code = eval_run.main([
            '--case',
            'nothing/*',
            '--case',
            'none/*',
            '--max-cost-usd',
            '1',
            '--dry-run',
        ])
        output = capsys.readouterr().out

        assert exit_code == 1
        assert "No case matches --case 'nothing/*' --case 'none/*'" in output

    def test_a_selected_case_without_its_history_stops_before_any_install(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: pathlib.Path,
        capsys: pytest.CaptureFixture,
    ) -> None:
        point_at(
            monkeypatch,
            tmp_path,
        )
        history_case(tmp_path / 'evals')
        monkeypatch.setattr(
            eval_run,
            'export_package',
            fail_like_uvx,
        )
        exit_code = eval_run.main([
            '--case',
            'contract/*',
            '--max-cost-usd',
            '1',
            '--dry-run',
        ])
        output = capsys.readouterr().out.splitlines()

        assert exit_code == 1
        assert output[-1].startswith('eval_run: stopped: contract/read/after-go: case.yaml names history.jsonl')

    def test_an_unselected_case_without_its_history_does_not_stop_the_batch(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: pathlib.Path,
        capsys: pytest.CaptureFixture,
    ) -> None:
        point_at(
            monkeypatch,
            tmp_path,
        )
        history_case(tmp_path / 'evals')
        monkeypatch.setattr(
            eval_run,
            'export_package',
            fail_like_uvx,
        )
        exit_code = eval_run.main([
            '--case',
            'triggering/*',
            '--max-cost-usd',
            '1',
            '--dry-run',
        ])
        last_line = capsys.readouterr().out.splitlines()[-1]

        assert exit_code == 1
        assert last_line == 'eval_run: stopped: uvx exited with 1'


class TestReadAuthoredCases:
    def test_a_block_list_is_refused(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        committed_case(
            tmp_path,
            'contract/read/bad',
            [
                'name: contract/read/bad',
                'allowed_tools:',
                '  - Read',
                '  - Bash',
            ],
        )

        with pytest.raises(
            ValueError,
            match='contract/read/bad: allowed_tools must be one line',
        ):
            eval_run.read_authored_cases(tmp_path / 'source')

    def test_a_case_without_a_name_is_refused(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        committed_case(
            tmp_path,
            'contract/read/unnamed',
            ['allowed_tools: [Read]'],
        )

        with pytest.raises(
            ValueError,
            match='contract/read/unnamed: the case has no name',
        ):
            eval_run.read_authored_cases(tmp_path / 'source')

    def test_a_fixture_case_that_does_not_name_the_scaffold_is_refused(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        case_directory = committed_case(
            tmp_path,
            'contract/read/with-book',
            ['name: contract/read/with-book'],
        )
        write(case_directory / 'FIXTURE', 'home-with-book\n')

        with pytest.raises(
            ValueError,
            match='scaffold_script: scaffold.sh',
        ):
            eval_run.read_authored_cases(tmp_path / 'source')

    def test_a_multi_line_flow_list_is_refused(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        committed_case(
            tmp_path,
            'contract/read/bad',
            [
                'name: contract/read/bad',
                'allowed_tools: [Read,',
                '  Bash]',
            ],
        )

        with pytest.raises(
            ValueError,
            match='contract/read/bad: allowed_tools must be one line',
        ):
            eval_run.read_authored_cases(tmp_path / 'source')

    def test_a_one_line_list_is_read_without_its_comment(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        committed_case(
            tmp_path,
            'contract/read/writes',
            [
                'name: contract/read/writes   # what --case matches',
                'allowed_tools: [Skill, Read, "Bash(uv run *)", Write] # the grant',
            ],
        )
        cases = eval_run.read_authored_cases(tmp_path / 'source')

        assert cases == [
            eval_run.EvalCase(
                name='contract/read/writes',
                folder='contract/read/writes',
                tools=(
                    'Skill',
                    'Read',
                    'Bash(uv run *)',
                    'Write',
                ),
                source=tmp_path / 'source' / 'contract' / 'read' / 'writes',
            ),
        ]

    def test_a_scaffold_named_without_a_fixture_is_refused(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        case_directory = committed_case(
            tmp_path,
            'contract/read/with-book',
            ['name: contract/read/with-book'],
        )
        write(case_directory / 'case.yaml', FIXTURE_CASE_YAML)

        with pytest.raises(
            ValueError,
            match='no FIXTURE',
        ):
            eval_run.read_authored_cases(tmp_path / 'source')

    def test_an_unknown_fixture_is_refused(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        case_directory = committed_case(
            tmp_path,
            'contract/read/with-book',
            ['name: contract/read/with-book'],
        )
        write(case_directory / 'case.yaml', FIXTURE_CASE_YAML)
        write(case_directory / 'FIXTURE', 'no-such-fixture\n')

        with pytest.raises(
            ValueError,
            match='no-such-fixture',
        ):
            eval_run.read_authored_cases(tmp_path / 'source')

    @pytest.mark.parametrize(
        'reserved',
        [
            'fixture/README.md',
            'scaffold.sh',
        ],
    )
    def test_files_the_runner_writes_may_not_be_committed(
        self,
        tmp_path: pathlib.Path,
        reserved: str,
    ) -> None:
        case_directory = committed_case(
            tmp_path,
            'contract/read/with-book',
            ['name: contract/read/with-book'],
        )
        write(case_directory / 'case.yaml', FIXTURE_CASE_YAML)
        write(case_directory / 'FIXTURE', 'home-with-book\n')
        write(case_directory / reserved, 'committed by hand')

        with pytest.raises(
            ValueError,
            match='written by the runner',
        ):
            eval_run.read_authored_cases(tmp_path / 'source')

    def test_tools_in_case_yaml_are_refused(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        write(
            tmp_path / 'source' / 'contract' / 'read' / 'bad' / 'case.yaml',
            TOOLS_IN_CASE_YAML,
        )

        with pytest.raises(
            ValueError,
            match='contract/read/bad: allowed_tools belongs in prompt.md',
        ):
            eval_run.read_authored_cases(tmp_path / 'source')


class TestResultsDirectory:
    def test_a_batch_folder_is_named_by_its_time_and_its_cases(
        self,
    ) -> None:
        started = datetime.datetime(
            2026,
            9,
            22,
            23,
            15,
            36,
            tzinfo=datetime.UTC,
        )
        folder = eval_run.results_directory(
            ['contract/read/*'],
            started,
        )

        assert folder == eval_run.RESULTS_DIRECTORY / '20260922T231536Z-contract-read-all'

    def test_a_label_names_the_folder(
        self,
    ) -> None:
        started = datetime.datetime(
            2026,
            9,
            22,
            23,
            15,
            36,
            tzinfo=datetime.UTC,
        )
        folder = eval_run.results_directory(
            [
                'triggering/read/*',
                'triggering/query/*',
            ],
            started,
            label='triggering 1',
        )

        assert folder == eval_run.RESULTS_DIRECTORY / '20260922T231536Z-triggering-1'

    def test_without_a_label_every_glob_names_the_folder(
        self,
    ) -> None:
        started = datetime.datetime(
            2026,
            9,
            22,
            23,
            15,
            36,
            tzinfo=datetime.UTC,
        )
        folder = eval_run.results_directory(
            [
                'triggering/read/*',
                'triggering/query/*',
            ],
            started,
        )

        assert folder == eval_run.RESULTS_DIRECTORY / '20260922T231536Z-triggering-read-all-triggering-query-all'


class TestSelectCases:
    def test_no_shell_leaves_out_every_case_that_lists_bash(
        self,
    ) -> None:
        cases = [
            eval_case(
                'contract/read/runs-extract',
                (
                    'Read',
                    'Bash(uv run *)',
                ),
            ),
            eval_case(
                'contract/read/plain',
                ('Read',),
            ),
        ]
        selection = eval_run.select_cases(
            cases,
            ['contract/*'],
            no_shell=True,
        )

        assert selection.selected == (cases[1],)
        assert selection.left_out == (cases[0],)

    def test_only_the_cases_the_glob_matches_are_selected(
        self,
    ) -> None:
        cases = [
            eval_case(
                'contract/read/plain',
                ('Read',),
            ),
            eval_case(
                'triggering/query/fires-1',
                ('Skill',),
            ),
        ]
        selection = eval_run.select_cases(
            cases,
            ['triggering/*'],
            no_shell=False,
        )

        assert selection.selected == (cases[1],)
        assert selection.left_out == ()

    def test_several_globs_select_the_union_once_each(
        self,
    ) -> None:
        cases = [
            eval_case(
                'contract/read/plain',
                ('Read',),
            ),
            eval_case(
                'triggering/query/fires-1',
                ('Skill',),
            ),
            eval_case(
                'triggering/read/fires-1',
                ('Skill',),
            ),
        ]
        selection = eval_run.select_cases(
            cases,
            [
                'triggering/read/*',
                'triggering/*',
            ],
            no_shell=False,
        )

        assert selection.selected == (
            cases[1],
            cases[2],
        )

    def test_without_no_shell_a_bash_case_is_kept(
        self,
    ) -> None:
        cases = [
            eval_case(
                'contract/read/runs-extract',
                ('Bash',),
            ),
        ]
        selection = eval_run.select_cases(
            cases,
            ['*'],
            no_shell=False,
        )

        assert selection.selected == (cases[0],)


class TestTriggeringCases:
    def test_a_near_miss_asks_for_no_call(
        self,
    ) -> None:
        table = {
            'read': {
                'fires': [],
                'near_miss': ['What have I read about momentum crashes?'],
            },
        }
        cases = eval_run.triggering_cases(table)
        grader = cases['triggering/read/near-miss-1/graders/not-fired.md']

        assert 'min: 0' in grader
        assert 'max: 0' in grader

    def test_a_request_that_should_fire_asks_for_at_least_one_call(
        self,
    ) -> None:
        cases = eval_run.triggering_cases(QUERY_TABLE)
        grader = cases['triggering/query/fires-1/graders/fired.md']

        assert 'min: 1' in grader

    def test_each_generated_case_is_named_by_its_folder(
        self,
    ) -> None:
        cases = eval_run.generated_cases(eval_run.triggering_cases(QUERY_TABLE))

        assert cases == [
            eval_run.EvalCase(
                name='triggering/query/fires-1',
                folder='triggering/query/fires-1',
                tools=(
                    'Skill',
                    'Read',
                    'Glob',
                    'Grep',
                ),
            ),
        ]

    @pytest.mark.parametrize(
        'skill_input',
        [
            SKILL_INPUT_COMPACT,
            SKILL_INPUT_SPACED,
        ],
    )
    def test_the_input_match_finds_the_namespaced_skill_call(
        self,
        skill_input: str,
    ) -> None:
        cases = eval_run.triggering_cases(QUERY_TABLE)
        pattern = input_match(cases['triggering/query/fires-1/graders/fired.md'])

        assert re.search(pattern, skill_input)

    def test_the_input_match_ignores_another_skill(
        self,
    ) -> None:
        cases = eval_run.triggering_cases(QUERY_TABLE)
        pattern = input_match(cases['triggering/query/fires-1/graders/fired.md'])
        other_input = SKILL_INPUT_COMPACT.replace(
            ':query',
            ':read',
        )

        assert re.search(pattern, other_input) is None

    def test_the_request_is_the_prompt_body(
        self,
    ) -> None:
        cases = eval_run.triggering_cases(QUERY_TABLE)
        prompt = cases['triggering/query/fires-1/prompt.md']

        assert prompt.rstrip().endswith('What does my library say about momentum?')
