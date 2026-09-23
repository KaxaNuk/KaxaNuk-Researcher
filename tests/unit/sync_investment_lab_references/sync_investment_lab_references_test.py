"""
Unit tests for tools/sync_investment_lab_references.py: the example's own lines come out, nothing
else moves, and a missing example file stops the sync.
"""
import json
import pathlib

import pytest

import sync_investment_lab_references

EMPTY_NOTEBOOK = '{"cells": []}\n'


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



def write_every_template_file(
    root: pathlib.Path,
) -> None:
    """
    Write every generated file, in the example and in the template, as the same empty notebook.

    An empty notebook is also a Markdown or Python text with no markers, so every suffix reads it.
    """
    for relative_path in sync_investment_lab_references.TEMPLATE_FILES:
        write(root / sync_investment_lab_references.EXAMPLE_DIRECTORY / relative_path, EMPTY_NOTEBOOK)
        write(root / sync_investment_lab_references.TEMPLATE_DIRECTORY / relative_path, EMPTY_NOTEBOOK)


class TestExpectedReferences:
    def test_missing_example_file_is_named(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        with pytest.raises(
            FileNotFoundError,
            match='BLUEPRINT_1.md is missing',
        ):
            sync_investment_lab_references.expected_references(tmp_path)


class TestStripExampleContent:
    def test_adjacent_markdown_blocks_leave_one_blank_line(self) -> None:
        text = 'a\n\n<!-- example: begin -->\nx\n<!-- example: end -->\n\n<!-- example: begin -->\ny\n<!-- example: end -->\n\nb\n'
        result = sync_investment_lab_references.strip_example_content(text)

        assert result == 'a\n\nb\n'

    def test_adjacent_python_blocks_leave_one_seam(self) -> None:
        text = 'def kept_one() -> None:\n    pass\n\n\n# --- example: begin ---\nours = 1\n# --- example: end ---\n\n\n# --- example: begin ---\nours = 2\n# --- example: end ---\n\n\ndef kept_two() -> None:\n    pass\n'
        result = sync_investment_lab_references.strip_example_content(
            text,
            sync_investment_lab_references.PYTHON_EXAMPLE_BLOCK,
        )

        assert result == 'def kept_one() -> None:\n    pass\n\n\ndef kept_two() -> None:\n    pass\n'

    def test_longer_blank_run_beside_the_block_wins(self) -> None:
        text = 'import csv\n\n# --- example: begin ---\nours = 1\n# --- example: end ---\n\n\ndef kept() -> None:\n    pass\n'
        result = sync_investment_lab_references.strip_example_content(
            text,
            sync_investment_lab_references.PYTHON_EXAMPLE_BLOCK,
        )

        assert result == 'import csv\n\n\ndef kept() -> None:\n    pass\n'

    def test_python_block_in_the_middle_leaves_one_blank_line(self) -> None:
        text = 'a\n\n# --- example: begin ---\nx\n# --- example: end ---\n\nb\n'
        result = sync_investment_lab_references.strip_example_content(
            text,
            sync_investment_lab_references.PYTHON_EXAMPLE_BLOCK,
        )

        assert result == 'a\n\nb\n'

    def test_python_block_to_the_end_leaves_the_docstring_and_one_newline(self) -> None:
        text = '"""\nDocstring.\n"""\n\n# --- example: begin ---\n\nimport csv\n\n# --- example: end ---\n'
        result = sync_investment_lab_references.strip_example_content(
            text,
            sync_investment_lab_references.PYTHON_EXAMPLE_BLOCK,
        )

        assert result == '"""\nDocstring.\n"""\n'

    def test_python_marker_not_alone_on_its_line_is_kept(self) -> None:
        text = '"""\nThe markers are `# --- example: begin ---` and `# --- example: end ---`.\n"""\n'
        result = sync_investment_lab_references.strip_example_content(
            text,
            sync_investment_lab_references.PYTHON_EXAMPLE_BLOCK,
        )

        assert result == text

    def test_python_text_without_markers_is_unchanged(self) -> None:
        text = 'a\n\n\n\nb'
        result = sync_investment_lab_references.strip_example_content(
            text,
            sync_investment_lab_references.PYTHON_EXAMPLE_BLOCK,
        )

        assert result == text

    def test_python_two_blank_lines_between_kept_definitions_stay(self) -> None:
        text = 'def kept_one() -> None:\n    pass\n\n\n# --- example: begin ---\nours = 1\n# --- example: end ---\n\n\ndef kept_two() -> None:\n    pass\n'
        result = sync_investment_lab_references.strip_example_content(
            text,
            sync_investment_lab_references.PYTHON_EXAMPLE_BLOCK,
        )

        assert result == 'def kept_one() -> None:\n    pass\n\n\ndef kept_two() -> None:\n    pass\n'


class TestTemplatePart:
    def test_markdown_file_loses_its_blocks(self) -> None:
        text = '# Title\n\n<!-- example: begin -->\nours\n<!-- example: end -->\n\nprose\n'
        result = sync_investment_lab_references.template_part(
            text,
            '.md',
        )

        assert result == '# Title\n\nprose\n'

    def test_notebook_loses_its_example_only_cells(self) -> None:
        kept_cell = {
            'cell_type': 'markdown',
            'metadata': {},
            'source': ['# Section'],
        }
        example_cell = {
            'cell_type': 'code',
            'metadata': {},
            'source': [
                '# EXAMPLE-ONLY CELL\n',
                'print(1)',
            ],
        }
        raw = {
            'cells': [
                kept_cell,
                example_cell,
            ],
            'nbformat': 4,
        }
        notebook = json.dumps(raw)
        result = sync_investment_lab_references.template_part(
            notebook,
            '.ipynb',
        )
        cells = json.loads(result)['cells']

        assert cells == [kept_cell]

    def test_other_file_is_the_whole_text(self) -> None:
        text = 'main_identifier\n'
        result = sync_investment_lab_references.template_part(
            text,
            '.csv',
        )

        assert result == text

    def test_python_file_keeps_only_what_is_outside_the_block(self) -> None:
        text = '"""\nDocstring.\n"""\n\n# --- example: begin ---\nimport csv\n# --- example: end ---\n'
        result = sync_investment_lab_references.template_part(
            text,
            '.py',
        )

        assert result == '"""\nDocstring.\n"""\n'


class TestExpectedTemplateFiles:
    def test_stripping_is_idempotent(self) -> None:
        expected = sync_investment_lab_references.expected_template_files(
            sync_investment_lab_references.REPOSITORY_ROOT,
        )
        stripped_again = {
            relative_path: sync_investment_lab_references.template_part(
                text,
                pathlib.PurePosixPath(relative_path).suffix,
            )
            for relative_path, text
            in expected.items()
        }

        assert stripped_again == expected


class TestRenameExperiment:
    def test_experiment_1_becomes_experiment_n(self) -> None:
        text = '# Blueprint — Experiment 1\n\nSee [`FINDINGS_1.md`](FINDINGS_1.md).\n\n## Experiment 1 — liquid golden cross\n'
        result = sync_investment_lab_references.rename_experiment(text)
        expected = '# Blueprint — Experiment N\n\nSee [`FINDINGS_N.md`](FINDINGS_N.md).\n\n## Experiment N — <the idea, in five words>\n'

        assert result == expected


class TestStaleTemplateFiles:
    def test_changed_copy_is_stale(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        write_every_template_file(tmp_path)
        example = tmp_path / sync_investment_lab_references.EXAMPLE_DIRECTORY
        template = tmp_path / sync_investment_lab_references.TEMPLATE_DIRECTORY
        write(example / 'Paper_Trading/daily_update.py', 'new\n')
        write(template / 'Paper_Trading/daily_update.py', 'old\n')
        result = sync_investment_lab_references.stale_template_files(tmp_path)

        assert result == ['Paper_Trading/daily_update.py']

    def test_missing_copy_is_stale(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        write_every_template_file(tmp_path)
        example = tmp_path / sync_investment_lab_references.EXAMPLE_DIRECTORY
        write(example / 'Paper_Trading/daily_update.py', 'text\n')
        result = sync_investment_lab_references.stale_template_files(tmp_path)

        assert result == ['Paper_Trading/daily_update.py']

    def test_stripped_copy_is_not_stale(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        write_every_template_file(tmp_path)
        example = tmp_path / sync_investment_lab_references.EXAMPLE_DIRECTORY
        template = tmp_path / sync_investment_lab_references.TEMPLATE_DIRECTORY
        write(
            example / 'Data/curator.py',
            '"""\nD.\n"""\n\n# --- example: begin ---\nimport csv\n# --- example: end ---\n',
        )
        write(template / 'Data/curator.py', '"""\nD.\n"""\n')
        result = sync_investment_lab_references.stale_template_files(tmp_path)

        assert result == []
