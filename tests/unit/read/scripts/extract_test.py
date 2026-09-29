"""
Tests of the read skill's `extract.py`: the outline, the chapter files and their page markers, the
split for a PDF with no outline, the refusal of a chapter the outline lacks, and the slug.
"""
import pathlib
import subprocess
import sys
import types

EXTRACT_SCRIPT = pathlib.Path(__file__).resolve().parents[4] / '.apm' / 'skills' / 'read' / 'scripts' / 'extract.py'


class TestMain:
    """
    The command line, run as a user runs it, with pypdf as the engine so pdftotext is not needed.
    """

    def test_main_chapter_not_in_outline_exits_one(
        self,
        outlined_book: pathlib.Path,
    ) -> None:
        """
        A chapter number the outline does not have is a usage error: exit 1, no chapter written.
        """
        completed = _run_extract(
            [
                outlined_book.name,
                '--chapters',
                '9',
                '--engine',
                'pypdf',
            ],
            outlined_book.parent,
        )
        expected = 1

        assert completed.returncode == expected

    def test_main_chapters_marks_every_page(
        self,
        outlined_book: pathlib.Path,
    ) -> None:
        """
        Each page of a chapter follows its `<!-- p.N -->` marker, numbered as the PDF numbers it.
        """
        _run_extract(
            [
                outlined_book.name,
                '--chapters',
                '2',
                '--engine',
                'pypdf',
            ],
            outlined_book.parent,
        )
        chapter_path = outlined_book.parent / 'Extracts' / 'book' / '02_Chapter_Two.md'
        content = chapter_path.read_text(encoding='utf-8')
        result = content.split('# 2. Chapter Two\n\n', 1)[1]
        expected = ''.join([
            '<!-- p.3 -->\n',
            'Chapter Two opens here: momentum earned 0.75 percent a month across 480 portfolios.\n',
            '\n',
            '<!-- p.4 -->\n',
            'Chapter Two continues here: the crash of 2009 took 73.4 percent from the long-short book.\n',
        ])

        assert result == expected

    def test_main_chapters_without_outline_exits_three(
        self,
        plain_report: pathlib.Path,
    ) -> None:
        """
        `--chapters` on a PDF with no outline and no `--split` has nothing to number, and exits 3.
        """
        completed = _run_extract(
            [
                plain_report.name,
                '--chapters',
                '1',
                '--engine',
                'pypdf',
            ],
            plain_report.parent,
        )
        expected = 3

        assert completed.returncode == expected

    def test_main_chapters_writes_frontmatter(
        self,
        outlined_book: pathlib.Path,
    ) -> None:
        """
        A chapter file opens with its source, number, title and pages, before the engine's name.
        """
        _run_extract(
            [
                outlined_book.name,
                '--chapters',
                '2',
                '--engine',
                'pypdf',
            ],
            outlined_book.parent,
        )
        chapter_path = outlined_book.parent / 'Extracts' / 'book' / '02_Chapter_Two.md'
        result = chapter_path.read_text(encoding='utf-8')
        expected = '\n'.join([
            '---',
            'source: "book.pdf"',
            'chapter: 2',
            'title: "Chapter Two"',
            'pages: "3–4"',
            'engine: "pypdf',
        ])

        assert result.startswith(expected)

    def test_main_chapters_writes_one_file_per_chapter(
        self,
        outlined_book: pathlib.Path,
    ) -> None:
        """
        `--chapters 1,2` writes the two chapters and the outline, and nothing for the front matter.
        """
        _run_extract(
            [
                outlined_book.name,
                '--chapters',
                '1,2',
                '--engine',
                'pypdf',
            ],
            outlined_book.parent,
        )
        result = sorted(
            path.name
            for path
            in (outlined_book.parent / 'Extracts' / 'book').iterdir()
        )
        expected = [
            '01_Chapter_One.md',
            '02_Chapter_Two.md',
            'OUTLINE.md',
        ]

        assert result == expected

    def test_main_outline_lists_every_chapter(
        self,
        outlined_book: pathlib.Path,
    ) -> None:
        """
        `--outline` prints the front matter and both chapters, numbered as `--chapters` takes them.
        """
        completed = _run_extract(
            [
                outlined_book.name,
                '--outline',
            ],
            outlined_book.parent,
        )
        expected_lines = [
            '0. Front matter',
            '1. Chapter One',
            '2. Chapter Two',
        ]

        assert all(
            line in completed.stdout
            for line
            in expected_lines
        )

    def test_main_outline_writes_nothing(
        self,
        outlined_book: pathlib.Path,
    ) -> None:
        """
        `--outline` leaves the folder as it was: the PDF alone.
        """
        _run_extract(
            [
                outlined_book.name,
                '--outline',
            ],
            outlined_book.parent,
        )
        result = sorted(
            path.name
            for path
            in outlined_book.parent.iterdir()
        )
        expected = ['book.pdf']

        assert result == expected

    def test_main_split_without_outline(
        self,
        plain_report: pathlib.Path,
    ) -> None:
        """
        `--split` names the chapters of a PDF with no outline, and `--all` writes each of them.
        """
        _run_extract(
            [
                plain_report.name,
                '--split',
                'Opening=1-1; Rest=2-3',
                '--all',
                '--engine',
                'pypdf',
            ],
            plain_report.parent,
        )
        result = sorted(
            path.name
            for path
            in (plain_report.parent / 'Extracts' / 'report').iterdir()
        )
        expected = [
            '01_Opening.md',
            '02_Rest.md',
            'OUTLINE.md',
        ]

        assert result == expected


class TestSlugify:
    """
    The extract folder's and a chapter file's name, made the way the notes are named.
    """

    def test_slugify_cuts_at_limit_without_trailing_underscore(
        self,
        extract_module: types.ModuleType,
    ) -> None:
        """
        A slug stops at its limit, and an underscore the cut leaves at the end goes.
        """
        result = extract_module.slugify(
            'Alpha Beta Gamma',
            11,
        )
        expected = 'Alpha_Beta'

        assert result == expected

    def test_slugify_drops_accents(
        self,
        extract_module: types.ModuleType,
    ) -> None:
        """
        An accented letter keeps its base letter, so a slug is ASCII.
        """
        result = extract_module.slugify('Économie Politique à Genève')
        expected = 'Economie_Politique_a_Geneve'

        assert result == expected

    def test_slugify_joins_words_with_underscores(
        self,
        extract_module: types.ModuleType,
    ) -> None:
        """
        Every run of other ASCII characters becomes one underscore, a curly apostrophe is dropped, and
        the source's own capitals are kept.
        """
        result = extract_module.slugify('Ilmanen 2011 - Expected Returns: An Investor’s Guide')
        expected = 'Ilmanen_2011_Expected_Returns_An_Investors_Guide'

        assert result == expected

    def test_slugify_names_an_empty_title_untitled(
        self,
        extract_module: types.ModuleType,
    ) -> None:
        """
        A title with no letter or digit becomes `Untitled`.
        """
        result = extract_module.slugify('!!! ???')
        expected = 'Untitled'

        assert result == expected


def _run_extract(
    arguments: list[str],
    folder: pathlib.Path,
) -> subprocess.CompletedProcess:
    """
    Run `extract.py` in `folder` with the Python running the tests, its output captured as UTF-8.
    """
    completed = subprocess.run(
        [
            sys.executable,
            str(EXTRACT_SCRIPT),
            *arguments,
        ],
        cwd=folder,
        capture_output=True,
        encoding='utf-8',
        check=False,
    )

    return completed
