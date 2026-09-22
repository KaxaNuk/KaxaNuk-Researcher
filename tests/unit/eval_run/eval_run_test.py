"""
Unit tests for tools/eval_run.py: the plugin it assembles, the cases it generates, the command it runs.
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
SHELL_PROMPT = '\n'.join([
    '---',
    'name: contract/read/runs-extract',
    'allowed_tools: [Skill, Read, Bash]',
    '---',
    'Read the book.',
    '',
])
SHELL_CASE_YAML = '\n'.join([
    'schema_version: "1.1"',
    'name: contract/read/runs-in-yaml',
    'execution:',
    '  allowed_tools:',
    '    - Read',
    '    - Bash',
    '',
])
PLAIN_PROMPT = '\n'.join([
    '---',
    'name: contract/read/plain',
    'allowed_tools: [Skill, Read]',
    '---',
    'Mention Bash in the body; only the grant counts.',
    '',
])
FIXTURE_CASE_YAML = '\n'.join([
    'schema_version: "1.1"',
    'name: contract/read/with-book',
    'context:',
    '  scaffold_script: scaffold.sh',
    '',
])


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


class TestCopyAuthoredCases:
    def test_a_fixture_case_that_does_not_name_the_scaffold_stops_the_assembly(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        case = tmp_path / 'source' / 'contract' / 'read' / 'with-book'
        write(case / 'prompt.md', PLAIN_PROMPT)
        write(case / 'FIXTURE', 'home-with-book\n')
        write(tmp_path / 'fixtures' / 'home-with-book' / 'README.md', 'home')

        with pytest.raises(
            ValueError,
            match='scaffold_script',
        ):
            eval_run.copy_authored_cases(
                tmp_path / 'source',
                tmp_path / 'evals',
                tmp_path / 'fixtures',
                no_shell=False,
            )

    def test_a_named_fixture_is_copied_into_the_case_as_real_files(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        case = tmp_path / 'source' / 'contract' / 'read' / 'with-book'
        write(case / 'prompt.md', PLAIN_PROMPT)
        write(case / 'case.yaml', FIXTURE_CASE_YAML)
        write(case / 'FIXTURE', 'home-with-book\n')
        write(tmp_path / 'fixtures' / 'home-with-book' / 'Sources' / 'book.md', 'a book')
        target = tmp_path / 'evals'
        eval_run.copy_authored_cases(
            tmp_path / 'source',
            target,
            tmp_path / 'fixtures',
            no_shell=False,
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

    def test_an_unknown_fixture_stops_the_assembly(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        case = tmp_path / 'source' / 'contract' / 'read' / 'with-book'
        write(case / 'prompt.md', PLAIN_PROMPT)
        write(case / 'case.yaml', FIXTURE_CASE_YAML)
        write(case / 'FIXTURE', 'no-such-fixture\n')

        with pytest.raises(
            ValueError,
            match='no-such-fixture',
        ):
            eval_run.copy_authored_cases(
                tmp_path / 'source',
                tmp_path / 'evals',
                tmp_path / 'fixtures',
                no_shell=False,
            )

    def test_no_shell_leaves_out_every_case_that_grants_bash(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        source = tmp_path / 'source' / 'contract' / 'read'
        write(source / 'runs-extract' / 'prompt.md', SHELL_PROMPT)
        write(source / 'runs-in-yaml' / 'case.yaml', SHELL_CASE_YAML)
        write(source / 'runs-in-yaml' / 'prompt.md', 'Read the book.\n')
        write(source / 'plain' / 'prompt.md', PLAIN_PROMPT)
        target = tmp_path / 'evals'
        left_out = eval_run.copy_authored_cases(
            tmp_path / 'source',
            target,
            tmp_path / 'fixtures',
            no_shell=True,
        )
        copied = sorted(
            path.name
            for path
            in (target / 'contract' / 'read').iterdir()
        )

        assert left_out == [
            'contract/read/runs-extract',
            'contract/read/runs-in-yaml',
        ]
        assert copied == ['plain']

    def test_the_case_gets_an_executable_scaffold_that_copies_its_fixture(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        case = tmp_path / 'source' / 'contract' / 'read' / 'with-book'
        write(case / 'prompt.md', PLAIN_PROMPT)
        write(case / 'case.yaml', FIXTURE_CASE_YAML)
        write(case / 'FIXTURE', 'home-with-book\n')
        write(tmp_path / 'fixtures' / 'home-with-book' / 'README.md', 'home')
        target = tmp_path / 'evals'
        eval_run.copy_authored_cases(
            tmp_path / 'source',
            target,
            tmp_path / 'fixtures',
            no_shell=False,
        )
        script = target / 'contract' / 'read' / 'with-book' / 'scaffold.sh'
        mode = script.stat().st_mode

        assert script.read_text(encoding='utf-8') == '\n'.join([
            '#!/usr/bin/env bash',
            'set -euo pipefail',
            'here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"',
            'cp -r "$here/fixture/." .',
            '',
        ])
        assert mode & stat.S_IXUSR

    def test_without_no_shell_every_case_is_copied(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        source = tmp_path / 'source' / 'quality' / 'read'
        write(source / 'runs-extract' / 'prompt.md', SHELL_PROMPT)
        write(source / 'plain' / 'prompt.md', PLAIN_PROMPT)
        target = tmp_path / 'evals'
        left_out = eval_run.copy_authored_cases(
            tmp_path / 'source',
            target,
            tmp_path / 'fixtures',
            no_shell=False,
        )
        copied = sorted(
            path.name
            for path
            in (target / 'quality' / 'read').iterdir()
        )

        assert left_out == []
        assert copied == [
            'plain',
            'runs-extract',
        ]


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
            case_glob='contract/read/*',
            runs=3,
            max_cost_usd=5.0,
            output_directory=tmp_path / 'results',
            no_shell=False,
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
                '--case contract/read/*',
                '--runs 3',
                '--scaffold',
                '--no-publish',
                '--trust-plugin',
                '--keep-temp',
            )
        )

    def test_no_shell_grants_write_and_edit_only(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        command = eval_run.eval_command(
            tmp_path,
            case_glob='*',
            runs=1,
            max_cost_usd=1.0,
            output_directory=tmp_path / 'results',
            no_shell=True,
        )

        assert '--allow-tools Write Edit' in ' '.join(command)
        assert 'Bash' not in command

    def test_results_and_report_go_to_the_batch_folder(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        output = tmp_path / 'results' / 'batch'
        command = eval_run.eval_command(
            tmp_path,
            case_glob='*',
            runs=1,
            max_cost_usd=1.0,
            output_directory=output,
            no_shell=False,
        )
        joined = ' '.join(command)

        assert f'--output-dir {output}' in joined
        assert f'--report {output / "report.html"}' in joined

    def test_the_operator_grant_includes_bash_by_default(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        command = eval_run.eval_command(
            tmp_path,
            case_glob='*',
            runs=1,
            max_cost_usd=1.0,
            output_directory=tmp_path / 'results',
            no_shell=False,
        )

        assert '--allow-tools Write Edit Bash' in ' '.join(command)

    def test_the_plugin_folder_is_the_target_and_comes_first(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        command = eval_run.eval_command(
            tmp_path,
            case_glob='*',
            runs=1,
            max_cost_usd=1.0,
            output_directory=tmp_path / 'results',
            no_shell=False,
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
            'contract/read/*',
            started,
        )

        assert folder == eval_run.RESULTS_DIRECTORY / '20260922T231536Z-contract-read-all'


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
