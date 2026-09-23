"""
Unit tests for tools/eval_fixtures.py: every fixture has the shape its cases rely on.
"""
import json
import pathlib
import shutil

import pypdf
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

    def test_home_with_book_holds_an_outlined_pdf(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        reader = pypdf.PdfReader(str(fixtures / 'home-with-book' / eval_fixtures.BOOK_PATH))

        assert len(reader.outline) == 3

    def test_home_with_image_pdf_has_no_text(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        reader = pypdf.PdfReader(str(fixtures / 'home-with-image-pdf' / eval_fixtures.BOOK_PATH))
        text = ''.join(
            page.extract_text()
            for page
            in reader.pages
        )

        assert text.strip() == ''

    def test_home_with_notes_has_an_index_that_links_the_notes(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        index = (fixtures / 'home-with-notes' / 'Knowledge' / 'INDEX.md').read_text(encoding='utf-8')

        assert 'Moskowitz_2012_Time_Series_Momentum.md' in index

    def test_notebook_fixture_is_valid_json(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        notebook = fixtures / 'strategy-ready' / 'Experiments' / 'Experiment_1' / 'experiment_1.ipynb'
        parsed = json.loads(notebook.read_text(encoding='utf-8'))

        assert 'cells' in parsed

    def test_researcher_existing_is_a_filled_home(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        researcher = (fixtures / 'researcher-existing' / 'Luna' / 'RESEARCHER.md').read_text(encoding='utf-8')

        assert 'Luna' in researcher

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

    def test_strategy_no_claims_keeps_the_template_objective(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        objective = (fixtures / 'strategy-no-claims' / 'OBJECTIVE.md').read_text(encoding='utf-8')

        assert eval_fixtures.CLAIMS_MARKER not in objective

    def test_strategy_non_empty_target_holds_a_file(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        files = list((fixtures / 'strategy-non-empty-target' / 'fcf-yield-quality').iterdir())

        assert len(files) == 1

    def test_strategy_ready_has_claims_and_a_seed_with_rows(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        seed = (fixtures / 'strategy-ready' / 'Universe' / 'Investable_Universe.csv').read_text(encoding='utf-8')
        rows = seed.strip().splitlines()

        assert len(rows) > 1


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
        built = target / 'home-with-book' / 'RESEARCHER.md'

        assert built.read_text(encoding='utf-8').startswith('This package, not the repository.')
