"""
Unit tests for the init-strategy skill's scaffold script.
"""
import os
import pathlib
import subprocess

import pytest

import scaffold

# The checkout these tests run in: init_strategy/ -> unit/ -> tests/ -> the root.
TEST_PATH = pathlib.Path(__file__)
REPOSITORY_ROOT = TEST_PATH.resolve().parents[3]


@pytest.fixture
def package(
    tmp_path: pathlib.Path,
) -> pathlib.Path:
    """
    A package with the three starting points, each holding a nested file.
    """
    root = tmp_path / 'researcher'

    for relative_source, _ in scaffold.STARTING_POINTS.values():
        nested = root / relative_source / 'Folder'
        nested.mkdir(parents=True)
        (root / relative_source / 'README.md').write_text(
            relative_source,
            encoding='utf-8',
        )
        (nested / 'file.md').write_text(
            'nested',
            encoding='utf-8',
        )

    return root


class TestFindPackage:
    def test_checkout_is_found_before_any_install(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        result = scaffold.find_package(
            None,
            tmp_path,
        )
        expected = REPOSITORY_ROOT

        assert result == expected

    def test_explicit_folder_without_starting_points_is_rejected(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        result = scaffold.find_package(
            tmp_path,
            tmp_path,
        )

        assert result is None

    def test_explicit_package_is_used(
        self,
        package: pathlib.Path,
        tmp_path: pathlib.Path,
    ) -> None:
        result = scaffold.find_package(
            package,
            tmp_path,
        )

        assert result == package

    def test_install_above_the_start_is_found(
        self,
        package: pathlib.Path,
        tmp_path: pathlib.Path,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        installed = tmp_path / 'project' / 'apm_modules' / 'KaxaNuk'
        installed.mkdir(parents=True)
        package.rename(installed / 'KaxaNuk-Researcher')
        start = tmp_path / 'project' / 'deep' / 'folder'
        start.mkdir(parents=True)
        monkeypatch.setattr(
            scaffold,
            'SOURCE_PACKAGE',
            tmp_path / 'nowhere',
        )
        result = scaffold.find_package(
            None,
            start,
        )
        expected = installed / 'KaxaNuk-Researcher'

        assert result == expected


class TestMain:
    def test_failed_commit_prints_the_command_that_finishes_it(
        self,
        package: pathlib.Path,
        tmp_path: pathlib.Path,
        monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        global_config = tmp_path / 'gitconfig'
        global_config.write_text(
            '[user]\n\tuseConfigOnly = true\n',
            encoding='utf-8',
        )
        monkeypatch.setenv('GIT_CONFIG_GLOBAL', str(global_config))
        monkeypatch.setenv('GIT_CONFIG_NOSYSTEM', '1')
        identity_variables = [
            'GIT_AUTHOR_NAME',
            'GIT_AUTHOR_EMAIL',
            'GIT_COMMITTER_NAME',
            'GIT_COMMITTER_EMAIL',
            'EMAIL',
        ]

        for variable in identity_variables:
            monkeypatch.delenv(
                variable,
                raising=False,
            )

        destination = tmp_path / 'no-identity'
        exit_code = scaffold.main([
            'researcher',
            str(destination),
            '--package',
            str(package),
        ])
        printed = capsys.readouterr().out
        expected = 'git commit -m "Start from the KaxaNuk Researcher template"'

        assert exit_code == 0
        assert expected in printed

    def test_git_repository_has_a_first_commit(
        self,
        package: pathlib.Path,
        tmp_path: pathlib.Path,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.setenv('GIT_AUTHOR_NAME', 'Test')
        monkeypatch.setenv('GIT_AUTHOR_EMAIL', 'test@example.com')
        monkeypatch.setenv('GIT_COMMITTER_NAME', 'Test')
        monkeypatch.setenv('GIT_COMMITTER_EMAIL', 'test@example.com')
        monkeypatch.setenv('GIT_CONFIG_GLOBAL', os.devnull)
        destination = tmp_path / 'with-git'
        exit_code = scaffold.main([
            'researcher',
            str(destination),
            '--package',
            str(package),
        ])
        head = subprocess.run(
            [
                'git',
                'rev-parse',
                '--verify',
                'HEAD',
            ],
            cwd=destination,
            capture_output=True,
            check=False,
        )

        assert exit_code == 0
        assert head.returncode == 0

    def test_git_repository_starts_on_main(
        self,
        package: pathlib.Path,
        tmp_path: pathlib.Path,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.setenv('GIT_AUTHOR_NAME', 'Test')
        monkeypatch.setenv('GIT_AUTHOR_EMAIL', 'test@example.com')
        monkeypatch.setenv('GIT_COMMITTER_NAME', 'Test')
        monkeypatch.setenv('GIT_COMMITTER_EMAIL', 'test@example.com')
        monkeypatch.setenv('GIT_CONFIG_GLOBAL', os.devnull)
        destination = tmp_path / 'on-main'
        scaffold.main([
            'strategy',
            str(destination),
            '--package',
            str(package),
        ])
        completed = subprocess.run(
            [
                'git',
                'branch',
                '--show-current',
            ],
            cwd=destination,
            capture_output=True,
            text=True,
            check=True,
        )
        branch = completed.stdout.strip()

        assert branch == 'main'

    def test_new_folder_receives_the_starting_point(
        self,
        package: pathlib.Path,
        tmp_path: pathlib.Path,
    ) -> None:
        destination = tmp_path / 'My-Strategy'
        exit_code = scaffold.main([
            'strategy',
            str(destination),
            '--package',
            str(package),
            '--no-git',
        ])
        copied = (destination / 'Folder' / 'file.md').read_text(encoding='utf-8')

        assert exit_code == 0
        assert copied == 'nested'

    def test_non_empty_destination_is_refused(
        self,
        package: pathlib.Path,
        tmp_path: pathlib.Path,
    ) -> None:
        destination = tmp_path / 'taken'
        destination.mkdir()
        (destination / 'mine.md').write_text(
            'mine',
            encoding='utf-8',
        )
        exit_code = scaffold.main([
            'strategy',
            str(destination),
            '--package',
            str(package),
            '--no-git',
        ])
        contents = sorted(
            path.name
            for path
            in destination.iterdir()
        )

        assert exit_code == 1
        assert contents == ['mine.md']

    def test_only_copies_one_folder_into_an_existing_one(
        self,
        package: pathlib.Path,
        tmp_path: pathlib.Path,
    ) -> None:
        strategy = tmp_path / 'strategy'
        strategy.mkdir()
        exit_code = scaffold.main([
            'example',
            str(strategy),
            '--only',
            'Folder',
            '--package',
            str(package),
        ])
        copied = (strategy / 'Folder' / 'file.md').read_text(encoding='utf-8')

        assert exit_code == 0
        assert copied == 'nested'

    def test_only_never_overwrites(
        self,
        package: pathlib.Path,
        tmp_path: pathlib.Path,
    ) -> None:
        strategy = tmp_path / 'strategy'
        (strategy / 'Folder').mkdir(parents=True)
        (strategy / 'Folder' / 'file.md').write_text(
            'mine',
            encoding='utf-8',
        )
        exit_code = scaffold.main([
            'example',
            str(strategy),
            '--only',
            'Folder',
            '--package',
            str(package),
        ])
        kept = (strategy / 'Folder' / 'file.md').read_text(encoding='utf-8')

        assert exit_code == 1
        assert kept == 'mine'

    def test_only_skips_identical_files(
        self,
        package: pathlib.Path,
        tmp_path: pathlib.Path,
    ) -> None:
        strategy = tmp_path / 'strategy'
        (strategy / 'Folder').mkdir(parents=True)
        (strategy / 'Folder' / 'file.md').write_text(
            'nested',
            encoding='utf-8',
        )
        (package / 'examples' / 'liquid-golden-cross' / 'Folder' / 'new.md').write_text(
            'new',
            encoding='utf-8',
        )
        exit_code = scaffold.main([
            'example',
            str(strategy),
            '--only',
            'Folder',
            '--package',
            str(package),
        ])
        copied = (strategy / 'Folder' / 'new.md').read_text(encoding='utf-8')

        assert exit_code == 0
        assert copied == 'new'


class TestPlanCopy:
    def test_every_file_lands_under_the_destination(
        self,
        package: pathlib.Path,
        tmp_path: pathlib.Path,
    ) -> None:
        source = package / 'templates' / 'strategy'
        destination = tmp_path / 'new'
        plan = scaffold.plan_copy(
            source,
            destination,
        )
        landings = [
            target.relative_to(destination).as_posix()
            for _, target
            in plan.files
        ]
        expected = [
            'Folder/file.md',
            'README.md',
        ]

        assert landings == expected
