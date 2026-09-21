"""
Unit tests for tools/check_repo.py: each check finds the defect it exists for.
"""
import pathlib

import check_repo


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


class TestCheckPathLength:
    def test_long_path_is_reported(self) -> None:
        long_path = 'a' * (check_repo.PATH_LIMIT + 1)
        findings = check_repo.check_path_length([
            'short.md',
            long_path,
        ])
        checks = [
            finding.check
            for finding
            in findings
        ]

        assert checks == ['path length']


class TestFoldedDescription:
    def test_folded_lines_are_joined(self) -> None:
        text = 'name: x\ndescription: >\n  One line\n  and another.\nmetadata:\n'
        result = check_repo.folded_description(text)

        assert result == 'One line and another.'


class TestMarkerProblems:
    def test_balanced_markers_pass(self) -> None:
        text = 'a\n<!-- example: begin -->\nb\n<!-- example: end -->\n'
        result = check_repo.marker_problems(
            text,
            check_repo.MARKERS['.md'],
        )

        assert result == []

    def test_block_left_open_is_reported(self) -> None:
        text = 'a\n<!-- example: begin -->\nb\n'
        result = check_repo.marker_problems(
            text,
            check_repo.MARKERS['.md'],
        )

        assert result == ['line 2 opens a block that never closes']

    def test_close_without_open_is_reported(self) -> None:
        text = 'a\n<!-- example: end -->\n'
        result = check_repo.marker_problems(
            text,
            check_repo.MARKERS['.md'],
        )

        assert result == ['line 2 closes a block that is not open']


class TestMissingHeadings:
    def test_heading_the_example_dropped_is_reported(self) -> None:
        template = '# Title\n\n## Kept\n\n## Dropped\n'
        example = '# Title\n\n## Kept\n\nworked lines\n'
        result = check_repo.missing_headings(
            template,
            example,
        )

        assert result == ['## Dropped']


class TestVersionProblems:
    def test_agreeing_versions_pass(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        write(tmp_path / 'apm.yml', 'name: x\nversion: 1.2.3\n')
        write(tmp_path / 'CHANGELOG.md', '# Changelog\n\n## [1.2.3] - 2026-01-01\n')
        write(tmp_path / 'pyproject.toml', '[project]\nversion = "1.2.3"\n')
        result = check_repo.version_problems(
            'x',
            tmp_path,
        )

        assert result == []

    def test_changelog_behind_is_reported(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        write(tmp_path / 'apm.yml', 'name: x\nversion: 1.2.4\n')
        write(tmp_path / 'CHANGELOG.md', '# Changelog\n\n## 1.2.3 (2026-01-01)\n')
        result = check_repo.version_problems(
            'x',
            tmp_path,
        )
        messages = [
            finding.message
            for finding
            in result
        ]

        assert messages == ['x: apm.yml declares 1.2.4; CHANGELOG.md says 1.2.3']
