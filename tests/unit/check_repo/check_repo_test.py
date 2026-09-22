"""
Unit tests for tools/check_repo.py: each check finds the defect it exists for.
"""
import json
import pathlib
import subprocess

import check_repo
import sync_investment_lab_references

# The least each kind of example file can hold and still be read: none has markers to strip, so
# its template copy is the same text.
MINIMAL_TEXTS = {
    '.ipynb': '{"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}',
    '.md': '# Document\n',
    '.py': '"""\nDocstring.\n"""\n',
}


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


def write_example_and_template(
    root: pathlib.Path,
) -> None:
    """
    Write every file the template is generated from, and its matching template copy, each with the
    minimal text of its kind.
    """
    example = root / sync_investment_lab_references.EXAMPLE_DIRECTORY
    template = root / sync_investment_lab_references.TEMPLATE_DIRECTORY
    for relative_path in sync_investment_lab_references.TEMPLATE_FILES:
        suffix = pathlib.PurePosixPath(relative_path).suffix
        write(example / relative_path, MINIMAL_TEXTS[suffix])
        write(template / relative_path, MINIMAL_TEXTS[suffix])


class TestCheckDescriptions:
    def test_long_folded_description_is_reported(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        long_text = 'a' * (check_repo.DESCRIPTION_LIMIT + 1)
        write(tmp_path / '.apm/skills/long/SKILL.md', f'---\nname: long\ndescription: >\n  {long_text}\n---\n')
        write(tmp_path / '.apm/skills/short/SKILL.md', '---\nname: short\ndescription: >\n  Short.\n---\n')
        findings = check_repo.check_descriptions(
            tmp_path,
            [
                '.apm/skills/long/SKILL.md',
                '.apm/skills/short/SKILL.md',
            ],
        )
        messages = [
            finding.message
            for finding
            in findings
        ]

        assert messages == ['.apm/skills/long/SKILL.md: 1025 characters, over 1024']

    def test_long_one_line_description_is_reported(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        manifest = '.apm/skills/x/SKILL.md'
        description = 'a' * (check_repo.DESCRIPTION_LIMIT + 1)
        write(tmp_path / manifest, f'---\nname: x\ndescription: {description}\n---\n')
        findings = check_repo.check_descriptions(
            tmp_path,
            [manifest],
        )
        checks = [
            finding.check
            for finding
            in findings
        ]

        assert checks == ['description']

    def test_unreadable_description_is_reported(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        manifest = '.apm/skills/x/SKILL.md'
        write(tmp_path / manifest, '---\nname: x\ndescription: |\n  Literal text.\n---\n')
        findings = check_repo.check_descriptions(
            tmp_path,
            [manifest],
        )
        checks = [
            finding.check
            for finding
            in findings
        ]

        assert checks == ['description']


class TestCheckHeadings:
    def test_readme_is_left_out_and_other_documents_are_checked(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        template = tmp_path / check_repo.TEMPLATE_FOLDER
        example = tmp_path / check_repo.EXAMPLE_FOLDER
        write(template / 'README.md', '# Title\n\n## Template only\n')
        write(example / 'README.md', '# Liquid golden cross\n')
        write(template / 'SETUP.md', '# Setup\n\n## Kept\n\n## Dropped\n')
        write(example / 'SETUP.md', '# Setup\n\n## Kept\n')
        findings = check_repo.check_headings(tmp_path)
        messages = [
            finding.message
            for finding
            in findings
        ]

        assert messages == [f'{check_repo.EXAMPLE_FOLDER}/SETUP.md lacks the template heading "## Dropped"']


class TestCheckMarkers:
    def test_balanced_markers_in_a_notebook_cell_pass(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        notebook = json.dumps({
            'cells': [
                {
                    'cell_type': 'markdown',
                    'metadata': {},
                    'source': [
                        '<!-- example: begin -->\n',
                        'worked lines\n',
                        '<!-- example: end -->',
                    ],
                },
            ],
            'nbformat': 4,
        })
        path = f'{check_repo.EXAMPLE_FOLDER}/balanced.ipynb'
        write(tmp_path / path, notebook)
        findings = check_repo.check_markers(
            tmp_path,
            [path],
        )

        assert findings == []

    def test_block_left_open_in_a_notebook_cell_is_reported(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        notebook = json.dumps({
            'cells': [
                {
                    'cell_type': 'markdown',
                    'metadata': {},
                    'source': [
                        '<!-- example: begin -->\n',
                        'worked lines',
                    ],
                },
            ],
            'nbformat': 4,
        })
        path = f'{check_repo.EXAMPLE_FOLDER}/open.ipynb'
        write(tmp_path / path, notebook)
        findings = check_repo.check_markers(
            tmp_path,
            [path],
        )
        messages = [
            finding.message
            for finding
            in findings
        ]

        assert messages == [f'{path} cell 1: line 1 opens a block that never closes']

    def test_deleted_notebook_is_not_read(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        path = f'{check_repo.EXAMPLE_FOLDER}/deleted.ipynb'
        findings = check_repo.check_markers(
            tmp_path,
            [path],
        )

        assert findings == []

    def test_python_block_left_open_is_reported(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        begin, _ = check_repo.MARKERS['.py']
        path = f'{check_repo.EXAMPLE_FOLDER}/Experiments/rule.py'
        write(tmp_path / path, f'x = 1\n{begin}\ny = 2\n')
        findings = check_repo.check_markers(
            tmp_path,
            [path],
        )
        messages = [
            finding.message
            for finding
            in findings
        ]

        assert messages == [f'{path}: line 2 opens a block that never closes']


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


class TestCheckReferences:
    def test_missing_example_file_is_reported(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        findings = check_repo.check_references(tmp_path)
        checks = [
            finding.check
            for finding
            in findings
        ]

        assert checks == ['references']

    def test_reference_edited_by_hand_is_reported(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        experiment = tmp_path / sync_investment_lab_references.EXPERIMENT_DIRECTORY
        references = tmp_path / sync_investment_lab_references.REFERENCES_DIRECTORY
        documents = sync_investment_lab_references.DOCUMENTS.items()
        for example_name, reference_name in documents:
            write(experiment / example_name, '# Document\n')
            write(references / reference_name, '# Document\n')
        write(experiment / 'experiment_1.ipynb', '{"cells": []}')
        write(references / 'experiment-notebook.ipynb', '{"cells": []}')
        write(references / 'blueprint-template.md', '# Edited by hand\n')
        findings = check_repo.check_references(tmp_path)
        messages = [
            finding.message
            for finding
            in findings
        ]

        assert messages == [
            'blueprint-template.md: differs from the example; run tools/sync_investment_lab_references.py',
        ]


class TestCheckSectionSymbol:
    def test_section_symbol_is_reported(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        write(tmp_path / 'clean.md', 'See section 2.\n')
        write(tmp_path / 'marked.md', f'See {check_repo.SECTION_SYMBOL}2.\n')
        findings = check_repo.check_section_symbol(
            tmp_path,
            [
                'clean.md',
                'marked.md',
            ],
        )
        messages = [
            finding.message
            for finding
            in findings
        ]

        assert messages == ['marked.md: uses the section symbol; write "section"']


class TestCheckTemplateFiles:
    def test_matching_copies_pass(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        write_example_and_template(tmp_path)
        findings = check_repo.check_template_files(tmp_path)

        assert findings == []

    def test_missing_example_file_is_reported(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        findings = check_repo.check_template_files(tmp_path)
        checks = [
            finding.check
            for finding
            in findings
        ]

        assert checks == ['template']

    def test_template_copy_that_differs_is_reported(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        write_example_and_template(tmp_path)
        example = tmp_path / check_repo.EXAMPLE_FOLDER
        template = tmp_path / check_repo.TEMPLATE_FOLDER
        write(example / 'Paper_Trading/daily_update.py', 'new\n')
        write(template / 'Paper_Trading/daily_update.py', 'old\n')
        findings = check_repo.check_template_files(tmp_path)
        messages = [
            finding.message
            for finding
            in findings
        ]

        assert messages == [
            'templates/strategy/Paper_Trading/daily_update.py: differs from the example; run tools/sync_investment_lab_references.py',
        ]


class TestFoldedDescription:
    def test_folded_lines_are_joined(self) -> None:
        text = 'name: x\ndescription: >\n  One line\n  and another.\nmetadata:\n'
        result = check_repo.folded_description(text)

        assert result == 'One line and another.'

    def test_one_line_description_is_read(self) -> None:
        text = 'name: x\ndescription: One line.\nmetadata:\n'
        result = check_repo.folded_description(text)

        assert result == 'One line.'

    def test_other_forms_are_not_read(self) -> None:
        text = 'name: x\ndescription: One line\n  continued.\nmetadata:\n'
        result = check_repo.folded_description(text)

        assert result == ''


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

    def test_indented_marker_is_reported(self) -> None:
        text = 'a\n    # --- example: begin ---\nb\n    # --- example: end ---\n'
        result = check_repo.marker_problems(
            text,
            check_repo.MARKERS['.py'],
        )

        assert result == ['line 2 has a marker that is not alone at column 0']

    def test_marker_before_a_carriage_return_is_reported(self) -> None:
        text = 'a\r\n<!-- example: begin -->\r\nb\r\n<!-- example: end -->\r\n'
        result = check_repo.marker_problems(
            text,
            check_repo.MARKERS['.md'],
        )

        assert result == ['line 2 has a marker that is not alone at column 0']

    def test_marker_with_trailing_space_is_reported(self) -> None:
        text = 'a\n<!-- example: begin --> \nb\n<!-- example: end -->\n'
        result = check_repo.marker_problems(
            text,
            check_repo.MARKERS['.md'],
        )

        assert result == ['line 2 has a marker that is not alone at column 0']


class TestMissingHeadings:
    def test_heading_the_example_dropped_is_reported(self) -> None:
        template = '# Title\n\n## Kept\n\n## Dropped\n'
        example = '# Title\n\n## Kept\n\nworked lines\n'
        result = check_repo.missing_headings(
            template,
            example,
        )

        assert result == ['## Dropped']


class TestTrackedFiles:
    def test_non_ascii_path_is_read_whole(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        note_name = 'Émile Borel.md'
        write(tmp_path / note_name, 'A note.\n')
        subprocess.run(
            [
                'git',
                'init',
                '--quiet',
            ],
            cwd=tmp_path,
            check=True,
        )
        subprocess.run(
            [
                'git',
                'add',
                '.',
            ],
            cwd=tmp_path,
            check=True,
        )
        result = check_repo.tracked_files(tmp_path)

        assert result == [note_name]


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

    def test_uv_lock_behind_is_reported(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        write(tmp_path / 'apm.yml', 'name: x\nversion: 1.2.4\n')
        write(tmp_path / 'CHANGELOG.md', '# Changelog\n\n## [1.2.4] - 2026-01-01\n')
        write(tmp_path / 'pyproject.toml', '[project]\nversion = "1.2.4"\n')
        write(
            tmp_path / 'uv.lock',
            'version = 1\n\n[[package]]\nname = "x"\nversion = "1.2.3"\nsource = { virtual = "." }\n',
        )
        result = check_repo.version_problems(
            'x',
            tmp_path,
        )
        messages = [
            finding.message
            for finding
            in result
        ]

        assert messages == ['x: apm.yml declares 1.2.4; uv.lock says 1.2.3']
