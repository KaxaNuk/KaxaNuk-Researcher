"""
Unit tests for tools/eval_fixtures.py: every fixture has the shape its cases rely on.
"""
import pathlib
import shutil

import pytest

import eval_fixtures


@pytest.fixture(scope='module')
def fixtures(
    tmp_path_factory: pytest.TempPathFactory,
) -> pathlib.Path:
    """
    Every fixture, built once from this repository's templates.
    """
    target = tmp_path_factory.mktemp('fixtures')
    eval_fixtures.build_all(target)

    return target


class TestBuildAll:
    def test_every_fixture_is_built(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        names = sorted(
            path.name
            for path
            in fixtures.iterdir()
        )

        assert names == sorted(eval_fixtures.FIXTURE_NAMES)

    def test_home_with_clipping_holds_one_clipping_and_no_note(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        home = fixtures / 'home-with-clipping'
        clippings = sorted(
            path.name
            for path
            in (home / 'Sources' / 'Clippings').iterdir()
            if path.suffix == '.md'
        )
        lines = (home / eval_fixtures.CLIPPING_PATH).read_text(encoding='utf-8').splitlines()

        assert clippings == [eval_fixtures.CLIPPING_PATH.name]
        assert 30 <= len(lines) <= 50
        assert not (home / 'Knowledge' / 'Markets').exists()

    def test_home_with_notes_has_an_index_that_links_the_notes(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        index = (fixtures / 'home-with-notes' / 'Knowledge' / 'INDEX.md').read_text(encoding='utf-8')

        assert 'Moskowitz_2012_Time_Series_Momentum.md' in index

    def test_home_with_notes_warns_in_the_older_note_above_the_superseded_claim(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        markets = fixtures / 'home-with-notes' / 'Knowledge' / 'Markets'
        older = (markets / 'Moskowitz_2012_Time_Series_Momentum.md').read_text(encoding='utf-8')
        newer = (markets / 'Daniel_2016_Momentum_Crashes.md').read_text(encoding='utf-8')
        warning = older.index('> [!WARNING]')
        claim = older.index('## The effect partly reverses after a year (p. 240)')

        assert warning < claim
        assert '(Daniel_2016_Momentum_Crashes.md)' in older[warning:claim]
        assert '[!WARNING]' not in newer

    def test_researcher_existing_is_a_filled_home(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        researcher = (fixtures / 'researcher-existing' / 'Ada' / 'RESEARCHER.md').read_text(encoding='utf-8')

        assert 'Ada' in researcher

    def test_strategy_blueprint_filled_has_no_template_slots(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        blueprint = (
            fixtures
            / 'strategy-blueprint-filled'
            / 'Experiments'
            / 'Experiment_1'
            / 'BLUEPRINT_1.md'
        ).read_text(encoding='utf-8')

        assert eval_fixtures.FILLED_BLUEPRINT_MARKER in blueprint

    def test_strategy_no_claims_with_home_keeps_the_template_objective_beside_the_home(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        folder = fixtures / 'strategy-no-claims-with-home'
        objective = (folder / 'OBJECTIVE.md').read_text(encoding='utf-8')
        paper = folder / 'Bibliotheca' / 'Papers' / 'Moskowitz_2012_Time_Series_Momentum.pdf'

        assert eval_fixtures.CLAIMS_MARKER not in objective
        assert paper.is_file()
        assert (folder / eval_fixtures.HOME_FOLDER / 'RESEARCHER.md').is_file()

    def test_strategy_ready_has_a_seed_with_rows(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        seed = (fixtures / 'strategy-ready' / 'Universe' / 'Investable_Universe.csv').read_text(encoding='utf-8')
        rows = seed.strip().splitlines()

        assert len(rows) > 1

    def test_strategy_with_home_carries_a_filled_home_for_ada(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        folder = fixtures / 'strategy-with-home'
        home = folder / eval_fixtures.HOME_FOLDER
        objective = (folder / 'OBJECTIVE.md').read_text(encoding='utf-8')
        researcher = (home / 'RESEARCHER.md').read_text(encoding='utf-8')
        index = (home / 'Knowledge' / 'INDEX.md').read_text(encoding='utf-8')

        assert eval_fixtures.CLAIMS_MARKER in objective
        assert researcher.startswith('# Ada')
        assert '<' not in researcher
        assert '1. Do trends in prices persist' in researcher
        assert '2. What ends a trend' in researcher
        assert (home / 'AGENTS.md').is_file()
        assert (home / 'Knowledge' / 'LOG.md').is_file()
        assert 'nothing read yet' in index


class TestBuildAllFromAnotherPackage:
    def test_the_fixtures_follow_the_package_they_are_given(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        package = tmp_path / 'package'

        for relative_path in (
            'templates/researcher',
            'templates/strategy',
            'examples/liquid-golden-cross',
            '.apm/skills/init-strategy/scripts',
        ):
            shutil.copytree(
                eval_fixtures.REPOSITORY_ROOT / relative_path,
                package / relative_path,
            )

        marked = package / 'templates' / 'researcher' / 'RESEARCHER.md'
        marked.write_text(
            'This package, not the repository.\n',
            encoding='utf-8',
        )
        target = tmp_path / 'fixtures'
        eval_fixtures.build_all(
            target,
            package_root=package,
        )
        built = target / 'home-with-clipping' / 'RESEARCHER.md'

        assert built.read_text(encoding='utf-8').startswith('This package, not the repository.')
