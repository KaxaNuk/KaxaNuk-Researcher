"""
Tests of the init-strategy skill's `scaffold.py`: a copy is the template byte for byte, `--only`
copies one file and nothing else, and every refusal leaves the destination as it was.
"""
import pathlib
import types

import pytest

REPOSITORY_ROOT = pathlib.Path(__file__).resolve().parents[4]
STRATEGY_TEMPLATE = REPOSITORY_ROOT / 'templates' / 'strategy'


class TestMain:
    """
    The command line, called in process with the checkout this file sits in as the package.
    """

    def test_main_only_copies_one_file(
        self,
        scaffold_module: types.ModuleType,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        `--only OBJECTIVE.md` into an existing folder writes that one file and nothing else.
        """
        scaffold_module.main([
            'strategy',
            str(tmp_path),
            '--only',
            'OBJECTIVE.md',
        ])
        result = _relative_files(tmp_path)
        expected = {'OBJECTIVE.md'}

        assert result == expected

    def test_main_only_keeps_the_existing_file(
        self,
        scaffold_module: types.ModuleType,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        `--only` onto a file with other content leaves that content as it was.
        """
        objective = tmp_path / 'OBJECTIVE.md'
        objective.write_text('my own objective', encoding='utf-8')
        scaffold_module.main([
            'strategy',
            str(tmp_path),
            '--only',
            'OBJECTIVE.md',
        ])
        result = objective.read_text(encoding='utf-8')
        expected = 'my own objective'

        assert result == expected

    def test_main_only_refuses_a_path_leading_outside(
        self,
        scaffold_module: types.ModuleType,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        `--only` with a path that climbs out through `..` is refused with exit code 1.
        """
        destination = tmp_path / 'strategy'
        destination.mkdir()
        result = scaffold_module.main([
            'strategy',
            str(destination),
            '--only',
            '../templates/researcher/AGENTS.md',
        ])
        expected = 1

        assert result == expected

    def test_main_only_refuses_to_overwrite(
        self,
        scaffold_module: types.ModuleType,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        `--only` onto a file with other content exits 1.
        """
        (tmp_path / 'OBJECTIVE.md').write_text('my own objective', encoding='utf-8')
        result = scaffold_module.main([
            'strategy',
            str(tmp_path),
            '--only',
            'OBJECTIVE.md',
        ])
        expected = 1

        assert result == expected

    def test_main_refusal_writes_nothing(
        self,
        scaffold_module: types.ModuleType,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        A refused destination is left as it was: its one file, and nothing copied beside it.
        """
        (tmp_path / 'mine.txt').write_text('mine', encoding='utf-8')
        scaffold_module.main([
            'strategy',
            str(tmp_path),
            '--no-git',
        ])
        result = _relative_files(tmp_path)
        expected = {'mine.txt'}

        assert result == expected

    def test_main_refuses_a_folder_that_is_not_empty(
        self,
        scaffold_module: types.ModuleType,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        A destination holding a file is refused with exit code 1.
        """
        (tmp_path / 'mine.txt').write_text('mine', encoding='utf-8')
        result = scaffold_module.main([
            'strategy',
            str(tmp_path),
            '--no-git',
        ])
        expected = 1

        assert result == expected

    def test_main_refuses_a_path_too_long_for_windows(
        self,
        scaffold_module: types.ModuleType,
        tmp_path: pathlib.Path,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """
        With the Windows path limit in force, a destination too deep for the template is refused, exit 1.
        """
        monkeypatch.setattr(
            scaffold_module,
            '_path_limit_applies',
            _limit_applies,
        )
        destination = tmp_path / ('deep' * 60)
        result = scaffold_module.main([
            'strategy',
            str(destination),
            '--no-git',
        ])
        expected = 1

        assert result == expected

    def test_main_strategy_copies_every_file(
        self,
        scaffold_module: types.ModuleType,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        The copy holds every file of the template, cache folders aside, and no other.
        """
        destination = tmp_path / 'strategy'
        scaffold_module.main([
            'strategy',
            str(destination),
            '--no-git',
        ])
        result = _relative_files(destination)
        expected = _template_files(scaffold_module)

        assert result == expected

    def test_main_strategy_copy_is_byte_for_byte(
        self,
        scaffold_module: types.ModuleType,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        Every copied file has exactly the bytes of the template's.
        """
        destination = tmp_path / 'strategy'
        scaffold_module.main([
            'strategy',
            str(destination),
            '--no-git',
        ])
        different = [
            relative_path
            for relative_path
            in _template_files(scaffold_module)
            if (destination / relative_path).read_bytes() != (STRATEGY_TEMPLATE / relative_path).read_bytes()
        ]
        expected = []

        assert different == expected


def _limit_applies() -> bool:
    """
    The Windows path limit, in force whatever the platform.
    """
    applies = True

    return applies


def _relative_files(
    folder: pathlib.Path,
) -> set[str]:
    """
    Every file under a folder, as a POSIX path relative to it.
    """
    files = {
        path.relative_to(folder).as_posix()
        for path
        in folder.rglob('*')
        if path.is_file()
    }

    return files


def _template_files(
    scaffold_module: types.ModuleType,
) -> set[str]:
    """
    Every file of the strategy template a copy should carry: all of them but those in a cache folder.
    """
    files = {
        relative_path
        for relative_path
        in _relative_files(STRATEGY_TEMPLATE)
        if not set(pathlib.PurePosixPath(relative_path).parts) & scaffold_module.CACHE_FOLDERS
    }

    return files
