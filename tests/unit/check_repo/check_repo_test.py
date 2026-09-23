"""
Unit tests for tools/check_repo.py: each check finds the defect it exists for.
"""
import json
import pathlib
import subprocess

import check_repo
import sync_investment_lab_references


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
    def test_readme_and_changelog_are_left_out_and_other_documents_are_checked(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        template = tmp_path / check_repo.TEMPLATE_FOLDER
        example = tmp_path / check_repo.EXAMPLE_FOLDER
        write(template / 'README.md', '# Title\n\n## Template only\n')
        write(example / 'README.md', '# Liquid golden cross\n')
        write(template / 'SETUP.md', '# Setup\n\n## Kept\n\n## Dropped\n')
        write(example / 'SETUP.md', '# Setup\n\n## Kept\n')
        write(template / 'CHANGELOG.md', '# Changelog\n\n## 0.10.3 (2026-09-23)\n')
        write(example / 'CHANGELOG.md', '# Changelog\n\n## 0.10.4 (2026-09-23)\n')
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
        path = 'examples/liquid-golden-cross/balanced.ipynb'
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
        path = 'examples/liquid-golden-cross/open.ipynb'
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
        example = tmp_path / check_repo.EXAMPLE_FOLDER
        template = tmp_path / check_repo.TEMPLATE_FOLDER
        # An empty notebook is also a Markdown or Python text with no markers, so every suffix reads it.
        for relative_path in sync_investment_lab_references.TEMPLATE_FILES:
            write(example / relative_path, '{"cells": []}\n')
            write(template / relative_path, '{"cells": []}\n')
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
        example = tmp_path / check_repo.EXAMPLE_FOLDER
        template = tmp_path / check_repo.TEMPLATE_FOLDER
        for relative_path in sync_investment_lab_references.TEMPLATE_FILES:
            write(example / relative_path, '{"cells": []}\n')
            write(template / relative_path, '{"cells": []}\n')
        write(example / 'Paper_Trading/daily_update.py', 'new\n')
        findings = check_repo.check_template_files(tmp_path)
        messages = [
            finding.message
            for finding
            in findings
        ]

        assert messages == [
            f'{check_repo.TEMPLATE_FOLDER}/Paper_Trading/daily_update.py: differs from the example; run tools/sync_investment_lab_references.py',
        ]


class TestCheckWidth:
    def test_changelog_and_generated_references_are_left_out(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        wide_text = f'{"a" * (check_repo.WIDTH_LIMIT + 1)}\n'
        write(tmp_path / 'templates/researcher/CHANGELOG.md', wide_text)
        write(tmp_path / '.apm/skills/experiment-lifecycle/references/structure.md', wide_text)
        write(tmp_path / 'examples/liquid-golden-cross/README.md', wide_text)
        findings = check_repo.check_width(
            tmp_path,
            [
                'templates/researcher/CHANGELOG.md',
                '.apm/skills/experiment-lifecycle/references/structure.md',
                'examples/liquid-golden-cross/README.md',
            ],
        )

        assert findings == []

    def test_wide_prose_line_is_reported_with_its_number(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        wide_line = 'a' * (check_repo.WIDTH_LIMIT + 4)
        write(tmp_path / '.apm/skills/x/SKILL.md', f'---\nname: x\n---\n\n# Title\n\n{wide_line}\n')
        write(tmp_path / 'README.md', 'Short.\n')
        findings = check_repo.check_width(
            tmp_path,
            [
                '.apm/skills/x/SKILL.md',
                'README.md',
            ],
        )
        messages = [
            finding.message
            for finding
            in findings
        ]

        assert messages == ['.apm/skills/x/SKILL.md: line 7 has 104 columns, over 100']


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
            [],
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
            [],
        )
        messages = [
            finding.message
            for finding
            in result
        ]

        assert messages == ['x: apm.yml declares 1.2.4; CHANGELOG.md says 1.2.3']

    def test_tracked_uv_lock_behind_is_reported(
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
            ['x/uv.lock'],
        )
        messages = [
            finding.message
            for finding
            in result
        ]

        assert messages == ['x: apm.yml declares 1.2.4; uv.lock says 1.2.3']

    def test_untracked_uv_lock_is_not_read(
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
            '.',
            tmp_path,
            ['examples/other/uv.lock'],
        )

        assert result == []


class TestWideLines:
    def test_fenced_code_table_rows_and_urls_are_set_aside(self) -> None:
        wide = 'a' * (check_repo.WIDTH_LIMIT + 1)
        text = '\n'.join([
            '---',
            f'description: {wide}',
            '---',
            '',
            '```',
            wide,
            '```',
            f'| {wide} |',
            f'{wide} https://example.com',
            '',
        ])
        result = check_repo.wide_lines(text)

        assert result == {}

    def test_wide_prose_line_is_reported_by_number_and_width(self) -> None:
        wide = 'a' * (check_repo.WIDTH_LIMIT + 3)
        text = f'# Title\n\nShort.\n{wide}\n'
        result = check_repo.wide_lines(text)

        assert result == {4: 103}

    def test_width_counts_characters_not_bytes(self) -> None:
        accented = 'é' * check_repo.WIDTH_LIMIT
        result = check_repo.wide_lines(f'{accented}\n')

        assert result == {}
