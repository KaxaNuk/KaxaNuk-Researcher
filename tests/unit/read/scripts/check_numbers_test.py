"""
Tests of the read skill's `check_numbers.py`: a figure on its cited page, elsewhere, or not found; a
note left unchecked; the offset of a note citing printed pages; and the exit codes.
"""
import pathlib
import subprocess
import sys

SCRIPTS = pathlib.Path(__file__).resolve().parents[4] / '.apm' / 'skills' / 'read' / 'scripts'
CHECK_NUMBERS_SCRIPT = SCRIPTS / 'check_numbers.py'
EXTRACT_SCRIPT = SCRIPTS / 'extract.py'
# The extract of `Sources/Author_2020_Book.pdf`: pages 10 to 14, each with numbers of its own.
EXTRACT_CHAPTER = '\n'.join([
    '---',
    'source: "Sources/Author_2020_Book.pdf"',
    'chapter: 1',
    'title: "One"',
    'pages: "10–14"',
    'engine: "pypdf"',
    '---',
    '',
    '# 1. One',
    '',
    '<!-- p.10 -->',
    'The premium was 12.5% over 1,250 months.',
    '',
    '<!-- p.11 -->',
    'A beta of −0.35 across 480 firms.',
    '',
    '<!-- p.12 -->',
    'Turnover of 37.2 percent a year.',
    '',
    '<!-- p.13 -->',
    'A Sharpe ratio of 0.61 on 2,400 stocks.',
    '',
    '<!-- p.14 -->',
    'Costs of 18 basis points.',
    '',
])


class TestMain:
    """
    The command line, run as `audit deep` runs it, on a library built in a temporary folder.
    """

    def test_main_cited_page_not_extracted(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        A figure no page holds, whose cited page is not in the extract, is not extracted, not missing.
        """
        _write_library(
            tmp_path,
            '- The premium was 99.9% (p. 80).',
        )
        completed = _run_check(tmp_path)
        expected = '0 not found, 1 not extracted'

        assert expected in completed.stdout

    def test_main_every_figure_found_exits_zero(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        Figures on page and elsewhere, none not found, exit 0.
        """
        _write_library(
            tmp_path,
            '- The premium was 12.5%, across 480 firms (p. 10).',
        )
        completed = _run_check(tmp_path)
        expected = 0

        assert completed.returncode == expected

    def test_main_figure_elsewhere_names_its_page(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        A figure another page holds is elsewhere, and `--verbose` names that page.
        """
        _write_library(
            tmp_path,
            '- It covered 480 firms (p. 10).',
        )
        completed = _run_check(
            tmp_path,
            '--verbose',
        )
        expected = 'elsewhere: line 9 "480" (cites p. 10) — found on p. 11'

        assert expected in completed.stdout

    def test_main_figure_matches_any_minus(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        A hyphen in the note finds the Unicode minus on the page.
        """
        _write_library(
            tmp_path,
            '- The beta was -0.35 (pp. 11–12).',
        )
        completed = _run_check(tmp_path)
        expected = '1 cited figures — 1 on page'

        assert expected in completed.stdout

    def test_main_figure_not_found_exits_two(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        One figure not found makes the exit code 2.
        """
        _write_library(
            tmp_path,
            '- The premium was 99.9% (p. 10).',
        )
        completed = _run_check(tmp_path)
        expected = 2

        assert completed.returncode == expected

    def test_main_figure_not_found_is_listed(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        A figure no page holds is listed with its line and the pages it cites.
        """
        _write_library(
            tmp_path,
            '- The premium was 99.9% (p. 10).',
        )
        completed = _run_check(tmp_path)
        expected = 'not found: line 9 "99.9%" (cites p. 10)'

        assert expected in completed.stdout

    def test_main_figure_on_cited_page(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        A figure the cited page holds, thousands separator and percent aside, is on page.
        """
        _write_library(
            tmp_path,
            '- The premium was 12.5% over 1250 months (p. 10).',
        )
        completed = _run_check(tmp_path)
        expected = '2 cited figures — 2 on page, 0 elsewhere, 0 not found, 0 not extracted'

        assert expected in completed.stdout

    def test_main_figure_without_citation_is_uncited(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        A block with a figure and no page citation is counted, not checked.
        """
        _write_library(
            tmp_path,
            '- The premium was 99.9%, from memory.',
        )
        completed = _run_check(tmp_path)
        expected = '0 cited figures — 0 on page, 0 elsewhere, 0 not found, 0 not extracted; 1 uncited'

        assert expected in completed.stdout

    def test_main_folder_skips_indexes_logs_and_pages(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        A folder is walked for notes: its INDEX.md, LOG.md and a concept page are left out.
        """
        _write_library(
            tmp_path,
            '- The premium was 12.5% (p. 10).',
        )
        knowledge = tmp_path / 'Knowledge'
        (knowledge / 'INDEX.md').write_text('# Index\n\n- 99.9 (p. 10)\n', encoding='utf-8')
        (knowledge / 'LOG.md').write_text('# Log\n\n- 99.9 (p. 10)\n', encoding='utf-8')
        (knowledge / 'Concept.md').write_text('---\ntype: concept\n---\n\n- 99.9 (p. 10)\n', encoding='utf-8')
        completed = _run_check(tmp_path)
        expected = '1 notes: 1 checked, 0 unchecked'

        assert expected in completed.stdout

    def test_main_ignores_links_and_heading_numbers(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        A number inside a markdown link, a citation in a link's text, and a heading's section number
        are not figures.
        """
        _write_library(
            tmp_path,
            '\n'.join([
                '## 4.2 Costs (p. 14)',
                '',
                '- See [Other (2019), p. 77](Other_2019_Paper_With_99_Pages.md) for 18 more (p. 14).',
            ]),
        )
        completed = _run_check(tmp_path)
        expected = '1 cited figures — 1 on page'

        assert expected in completed.stdout

    def test_main_missing_path_exits_one(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        A path that does not exist is a usage error, exit 1.
        """
        completed = _run_arguments(
            [
                'No_Such_Folder',
            ],
            tmp_path,
        )
        expected = 1

        assert completed.returncode == expected

    def test_main_never_edits_a_note(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        The note and the extract read are left byte for byte as they were.
        """
        _write_library(
            tmp_path,
            '- The premium was 99.9% (p. 10).',
        )
        watched = sorted(tmp_path.rglob('*.md'))
        before = [
            path.read_bytes()
            for path
            in watched
        ]
        _run_check(tmp_path)
        after = [
            path.read_bytes()
            for path
            in watched
        ]

        assert after == before

    def test_main_no_offset_from_one_line(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        Figures from one line found at one offset are one cross-reference, not a pattern.
        """
        _write_library(
            tmp_path,
            '- Turnover 37.2, Sharpe 0.61, 2,400 stocks and 480 firms (p. 3).',
        )
        completed = _run_check(tmp_path)
        unexpected = 'consistent offset'

        assert unexpected not in completed.stdout

    def test_main_reads_what_extract_wrote(
        self,
        outlined_book: pathlib.Path,
    ) -> None:
        """
        From a PDF to a checked note: `extract.py` writes the extract, and the note's figures are on
        the page it cites.
        """
        library = outlined_book.parent
        sources = library / 'Sources'
        sources.mkdir()
        outlined_book.rename(sources / outlined_book.name)
        subprocess.run(
            [
                sys.executable,
                str(EXTRACT_SCRIPT),
                'Sources/book.pdf',
                '--all',
                '--engine',
                'pypdf',
            ],
            cwd=library,
            capture_output=True,
            check=True,
        )
        _write_note(
            library,
            '- The equity premium was 4.25 percent over 1,200 months (p. 2).',
            'Sources/book.pdf',
        )
        completed = _run_check(library)
        expected = '2 cited figures — 2 on page'

        assert expected in completed.stdout

    def test_main_reports_a_consistent_offset(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        Three lines whose figures all sit eight pages after the page they cite suggest printed pages.
        """
        _write_library(
            tmp_path,
            '\n'.join([
                '- Turnover was 37.2 percent (p. 4).',
                '- The Sharpe ratio was 0.61 (p. 5).',
                '- The universe held 2,400 stocks (p. 5).',
                '- The beta was −0.35 (p. 3).',
            ]),
        )
        completed = _run_check(tmp_path)
        expected = 'consistent offset +8, the note may cite printed pages'

        assert expected in completed.stdout

    def test_main_unchecked_without_extract(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        A note whose PDF has no extract on disk is unchecked, with the command that would make one.
        """
        _write_library(
            tmp_path,
            '- The premium was 99.9% (p. 10).',
            'Sources/Missing_2021_Paper.pdf',
        )
        completed = _run_check(tmp_path)
        expected = ' '.join([
            'unchecked — no extract on disk at Extracts/Missing_2021_Paper/;',
            'regenerate it with uv run extract.py "Sources/Missing_2021_Paper.pdf" --all --out "Extracts"',
        ])

        assert expected in completed.stdout

    def test_main_unchecked_without_local_copy(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        A note whose `local_copy` is `none` is unchecked, and its figures do not fail the run.
        """
        _write_library(
            tmp_path,
            '- The premium was 99.9% (p. 10).',
            'none',
        )
        completed = _run_check(tmp_path)
        expected = 0

        assert completed.returncode == expected

    def test_main_unknown_option_exits_one(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        """
        An option the parser does not know is a usage error, exit 1, never the 2 of a figure not found.
        """
        completed = _run_arguments(
            [
                '.',
                '--no-such-option',
            ],
            tmp_path,
        )
        expected = 1

        assert completed.returncode == expected


def _run_arguments(
    arguments: list[str],
    folder: pathlib.Path,
) -> subprocess.CompletedProcess:
    """
    Run `check_numbers.py` in `folder` with the Python running the tests, its output captured as UTF-8.
    """
    completed = subprocess.run(
        [
            sys.executable,
            str(CHECK_NUMBERS_SCRIPT),
            *arguments,
        ],
        cwd=folder,
        capture_output=True,
        encoding='utf-8',
        check=False,
    )

    return completed


def _run_check(
    library: pathlib.Path,
    *options: str,
) -> subprocess.CompletedProcess:
    """
    Run `check_numbers.py` on the library's `Knowledge/`, extracts in its `Extracts/`.
    """
    completed = _run_arguments(
        [
            'Knowledge',
            '--extracts',
            'Extracts',
            *options,
        ],
        library,
    )

    return completed


def _write_library(
    library: pathlib.Path,
    body: str,
    local_copy: str = 'Sources/Author_2020_Book.pdf',
) -> pathlib.Path:
    """
    The extract of `Author_2020_Book.pdf`, pages 10 to 14, and one note whose body starts on line 9.
    """
    extract_folder = library / 'Extracts' / 'Author_2020_Book'
    extract_folder.mkdir(parents=True)
    (extract_folder / '01_One.md').write_text(
        EXTRACT_CHAPTER,
        encoding='utf-8',
    )
    note_path = _write_note(
        library,
        body,
        local_copy,
    )

    return note_path


def _write_note(
    library: pathlib.Path,
    body: str,
    local_copy: str,
) -> pathlib.Path:
    """
    One note in the library's `Knowledge/`: frontmatter naming its `local_copy`, a heading, the body.
    """
    knowledge = library / 'Knowledge'
    knowledge.mkdir(exist_ok=True)
    content = '\n'.join([
        '---',
        'source: none',
        'citation: "Author (2020). Book."',
        f'local_copy: {local_copy}',
        'read: 2026-09-29, the whole book',
        '---',
        '',
        '# Book',
        body,
        '',
    ])
    note_path = knowledge / 'Author_2020_Book.md'
    note_path.write_text(
        content,
        encoding='utf-8',
    )

    return note_path
