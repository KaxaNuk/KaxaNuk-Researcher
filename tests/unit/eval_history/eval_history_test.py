"""
Unit tests for tools/eval_history.py: where it finds the session, what it keeps, and what it refuses.
"""
import json
import pathlib

import pytest

import eval_history

# Built here, so this file holds no address a scan would take for a real one.
AT_SIGN = chr(64)
CASE_NAME = 'contract/blueprint/waits-before-write'
USER_LINE = json.dumps({
    'type': 'user',
    'message': {
        'role': 'user',
        'content': 'Read Sources/Books/Aldous_2021_Signals_In_Prices.pdf into my library.',
    },
})
ASSISTANT_LINE = json.dumps({
    'type': 'assistant',
    'message': {
        'role': 'assistant',
        'content': [
            {
                'type': 'text',
                'text': 'Three chapters. Which do you want read?',
            },
        ],
    },
})
CONTEXT_LINE = json.dumps({
    'type': 'attachment',
    'attachment': {
        'type': 'session_context',
        'content': f'The user is someone{AT_SIGN}example.com.',
    },
})
# The line of a real transcript that was taken for an address: a CLAUDE.md read by the Read tool.
TOOL_RESULT_LINE = json.dumps({
    'type': 'user',
    'message': {
        'role': 'user',
        'content': [
            {
                'tool_use_id': 'toolu_01Si2HRwC42FhRvmfwWzGpT3',
                'type': 'tool_result',
                'content': f'1\t{AT_SIGN}AGENTS.md',
            },
        ],
    },
})
COST_LINE = json.dumps({
    'type': 'cost-state',
    'totalCostUSD': 0.14,
})
TRANSCRIPT = '\n'.join([
    CONTEXT_LINE,
    USER_LINE,
    COST_LINE,
    '',
    ASSISTANT_LINE,
    '',
])


def kept_run(
    root: pathlib.Path,
    transcript: str,
) -> pathlib.Path:
    """
    A kept run folder as `--keep-temp` leaves it, with one session transcript.
    """
    folder = root / 'claude-eval-abc123'
    session = folder / 'config' / 'projects' / '-tmp-claude-eval-abc123-home-cwd' / 'session.jsonl'
    session.parent.mkdir(parents=True)
    session.write_text(
        transcript,
        encoding='utf-8',
    )
    (folder / 'out').mkdir()

    return folder


def results_for(
    folder: pathlib.Path,
) -> dict:
    """
    An aggregate-result.json whose one case's first run was kept in `folder`.
    """
    results = {
        'schemaVersion': 1,
        'cases': [
            {
                'name': 'contract/read/other',
                'arms': {'with': [{'tracePath': '/tmp/elsewhere/out/trace.jsonl'}]},
            },
            {
                'name': CASE_NAME,
                'arms': {
                    'with': [
                        {
                            'tracePath': str(folder / 'out' / 'trace.jsonl'),
                            'error': None,
                        },
                    ],
                },
            },
        ],
    }

    return results


class TestHoldsEMail:
    def test_a_file_name_after_a_json_escape_is_not_an_address(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.delenv(
            'CLAUDE_CODE_USER_EMAIL',
            raising=False,
        )

        assert f'1\\t{AT_SIGN}AGENTS.md' in TOOL_RESULT_LINE
        assert not eval_history.holds_e_mail(TOOL_RESULT_LINE)

    def test_a_file_name_after_an_at_sign_is_not_an_address(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.delenv(
            'CLAUDE_CODE_USER_EMAIL',
            raising=False,
        )

        assert not eval_history.holds_e_mail(f'Import it with {AT_SIGN}AGENTS.md, or read notes{AT_SIGN}INDEX.md.')

    def test_an_address_after_a_json_escape_is_found(
        self,
    ) -> None:
        text = json.dumps({'content': f'Done.\nCommitted as eval{AT_SIGN}example.invalid.'})

        assert eval_history.holds_e_mail(text)

    def test_the_address_in_the_environment_is_found_whatever_its_domain(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.setenv(
            'CLAUDE_CODE_USER_EMAIL',
            f'owner{AT_SIGN}studio.md',
        )

        assert eval_history.holds_e_mail(f'Written by Owner{AT_SIGN}Studio.md today.')

    def test_the_git_address_is_found_whatever_its_domain(
        self,
        tmp_path: pathlib.Path,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        git_config = tmp_path / 'gitconfig'
        git_config.write_text(
            f'[user]\n\temail = author{AT_SIGN}desk.py\n',
            encoding='utf-8',
        )
        monkeypatch.setenv(
            'GIT_CONFIG_GLOBAL',
            str(git_config),
        )
        monkeypatch.setenv(
            'GIT_CONFIG_NOSYSTEM',
            '1',
        )
        monkeypatch.chdir(tmp_path)
        monkeypatch.delenv(
            'CLAUDE_CODE_USER_EMAIL',
            raising=False,
        )

        assert eval_history.holds_e_mail(f'Committed as author{AT_SIGN}desk.py.')


class TestKeptFolder:
    def test_a_case_not_in_the_results_is_refused(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        with pytest.raises(
            ValueError,
            match='no run of contract/read/missing',
        ):
            eval_history.kept_folder(
                results_for(tmp_path),
                'contract/read/missing',
            )

    def test_a_run_that_never_started_is_refused_with_its_error(
        self,
    ) -> None:
        results = {
            'cases': [
                {
                    'name': CASE_NAME,
                    'arms': {'with': [{'tracePath': '', 'error': 'scaffold failed (exit 1)'}]},
                },
            ],
        }

        with pytest.raises(
            ValueError,
            match='has no trace: scaffold failed',
        ):
            eval_history.kept_folder(
                results,
                CASE_NAME,
            )

    def test_the_folder_is_two_levels_above_the_trace(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        folder = eval_history.kept_folder(
            results_for(tmp_path / 'claude-eval-abc123'),
            CASE_NAME,
        )

        assert folder == tmp_path / 'claude-eval-abc123'


class TestMain:
    def test_a_results_file_gives_the_kept_session(
        self,
        tmp_path: pathlib.Path,
        capsys: pytest.CaptureFixture,
    ) -> None:
        folder = kept_run(
            tmp_path,
            TRANSCRIPT.replace(
                CONTEXT_LINE + '\n',
                '',
            ),
        )
        results_file = tmp_path / 'aggregate-result.json'
        results_file.write_text(
            json.dumps(results_for(folder)),
            encoding='utf-8',
        )
        destination = tmp_path / 'case' / 'history.jsonl'
        exit_code = eval_history.main([
            str(results_file),
            str(destination),
            '--case',
            CASE_NAME,
        ])

        assert exit_code == 0
        assert destination.read_text(encoding='utf-8') == f'{USER_LINE}\n{ASSISTANT_LINE}\n'
        assert capsys.readouterr().out == f'Wrote 2 lines to {destination}\n'

    def test_a_results_file_without_a_case_is_refused(
        self,
        tmp_path: pathlib.Path,
        capsys: pytest.CaptureFixture,
    ) -> None:
        results_file = tmp_path / 'aggregate-result.json'
        results_file.write_text(
            '{}',
            encoding='utf-8',
        )
        exit_code = eval_history.main([
            str(results_file),
            str(tmp_path / 'history.jsonl'),
        ])

        assert exit_code == 1
        assert 'needs --case' in capsys.readouterr().out

    def test_an_e_mail_address_left_after_filtering_writes_nothing(
        self,
        tmp_path: pathlib.Path,
        capsys: pytest.CaptureFixture,
    ) -> None:
        leaked = ASSISTANT_LINE.replace(
            'Which do you want read?',
            f'Committed as eval{AT_SIGN}example.invalid.',
        )
        folder = kept_run(
            tmp_path,
            f'{USER_LINE}\n{leaked}\n',
        )
        destination = tmp_path / 'history.jsonl'
        exit_code = eval_history.main([
            str(folder),
            str(destination),
        ])
        output = capsys.readouterr().out

        assert exit_code == 1
        assert not destination.exists()
        assert output.startswith('eval_history: nothing written: the filtered session.jsonl still holds an e-mail')
        assert AT_SIGN not in output

    def test_the_context_line_carrying_the_e_mail_is_dropped(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        folder = kept_run(
            tmp_path,
            TRANSCRIPT,
        )
        destination = tmp_path / 'history.jsonl'
        exit_code = eval_history.main([
            str(folder),
            str(destination),
        ])

        assert exit_code == 0
        assert 'example.com' not in destination.read_text(encoding='utf-8')


class TestReplayLines:
    def test_a_line_that_is_not_json_is_refused(
        self,
    ) -> None:
        with pytest.raises(
            ValueError,
            match='not JSON',
        ):
            eval_history.replay_lines(f'{USER_LINE}\nnot json\n')

    def test_only_user_and_assistant_lines_are_kept_as_written(
        self,
    ) -> None:
        kept = eval_history.replay_lines(TRANSCRIPT)

        assert kept == [
            USER_LINE,
            ASSISTANT_LINE,
        ]


class TestSessionFile:
    def test_a_folder_with_no_session_is_refused(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        with pytest.raises(
            ValueError,
            match='holds 0 session files',
        ):
            eval_history.session_file(
                tmp_path,
                None,
            )

    def test_a_kept_folder_gives_its_one_session(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        folder = kept_run(
            tmp_path,
            TRANSCRIPT,
        )
        session = eval_history.session_file(
            folder,
            None,
        )

        assert session.name == 'session.jsonl'

    def test_a_session_file_is_its_own_source(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        session = tmp_path / 'abc.jsonl'
        found = eval_history.session_file(
            session,
            None,
        )

        assert found == session

    def test_another_kind_of_file_is_refused(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        with pytest.raises(
            ValueError,
            match='is not a results .json',
        ):
            eval_history.session_file(
                tmp_path / 'trace.txt',
                None,
            )
