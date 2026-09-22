"""
Unit tests for tools/sync_investment_lab_references.py: a missing example file stops the sync.
"""
import pathlib

import pytest

import sync_investment_lab_references


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
