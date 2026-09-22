"""
Unit tests for the read skill's extract script: chapters from an outline, the page ranges the owner
gives, and the files an extraction writes.
"""
import pathlib

import pypdf
import pytest

import extract


def describe_chapters(
    chapters: list[extract.Chapter],
) -> list[str]:
    """
    Each chapter as one string, `number title start-end`, 0-based pages.
    """
    described = [
        f'{chapter.number} {chapter.title} {chapter.start}-{chapter.end}'
        for chapter
        in chapters
    ]

    return described


def describe_entries(
    entries: list[extract.Entry],
) -> list[str]:
    """
    Each outline entry as one string, `depth title page`, 0-based page.
    """
    described = [
        f'{entry.depth} {entry.title} {entry.page}'
        for entry
        in entries
    ]

    return described


def entry(
    depth: int,
    title: str,
    page: int,
) -> extract.Entry:
    """
    An outline entry.
    """
    built = extract.Entry(
        depth,
        title,
        page,
    )

    return built


@pytest.fixture
def locked_pdf(
    tmp_path: pathlib.Path,
) -> pathlib.Path:
    """
    A one-page PDF that opens only with its user password.
    """
    writer = pypdf.PdfWriter()
    writer.add_blank_page(
        width=200,
        height=200,
    )
    writer.encrypt(
        user_password='secret',
        owner_password='owner',
        algorithm='RC4-128',
    )
    path = tmp_path / 'locked.pdf'

    with path.open('wb') as stream:
        writer.write(stream)

    return path


@pytest.fixture
def outlined_pdf(
    tmp_path: pathlib.Path,
) -> pathlib.Path:
    """
    A ten-page PDF with no text, whose outline has two chapters and a section: front matter on pages
    1-2, chapter one on 3-6 with a section on 5, chapter two on 7-10.
    """
    writer = pypdf.PdfWriter()

    for _ in range(10):
        writer.add_blank_page(
            width=200,
            height=200,
        )

    chapter_one = writer.add_outline_item(
        'One',
        2,
    )
    writer.add_outline_item(
        'A section',
        4,
        parent=chapter_one,
    )
    writer.add_outline_item(
        'Two',
        6,
    )
    path = tmp_path / 'book.pdf'

    with path.open('wb') as stream:
        writer.write(stream)

    return path


class TestChapter:
    def test_one_page_has_no_range(self) -> None:
        chapter = extract.Chapter(
            1,
            'One',
            4,
            4,
        )

        assert chapter.pages == '5'

    def test_range_uses_an_en_dash(self) -> None:
        chapter = extract.Chapter(
            1,
            'One',
            2,
            5,
        )

        assert chapter.pages == '3–6'


class TestChaptersFromOutline:
    def test_front_matter_and_chapter_ends(self) -> None:
        entries = [
            entry(
                1,
                'One',
                2,
            ),
            entry(
                2,
                'Section',
                4,
            ),
            entry(
                1,
                'Two',
                6,
            ),
        ]
        chapters = extract.chapters_from_outline(
            entries,
            1,
            10,
        )
        expected = [
            '0 Front matter 0-1',
            '1 One 2-5',
            '2 Two 6-9',
        ]

        assert describe_chapters(chapters) == expected

    def test_no_entry_at_the_depth_gives_no_chapters(self) -> None:
        entries = [
            entry(
                1,
                'One',
                0,
            ),
        ]
        chapters = extract.chapters_from_outline(
            entries,
            2,
            10,
        )

        assert chapters == []


class TestClean:
    def test_line_endings_spaces_and_blank_runs(self) -> None:
        text = 'a  \r\nb\r\n\r\n\r\n\r\nc\t\n'
        result = extract.clean(text)

        assert result == 'a\nb\n\nc'


class TestFlattenOutline:
    def test_depths_and_pages_are_read(
        self,
        outlined_pdf: pathlib.Path,
    ) -> None:
        reader = pypdf.PdfReader(str(outlined_pdf))
        page_count = len(reader.pages)
        entries = extract.flatten_outline(reader)
        expected = [
            '1 One 2',
            '2 A section 4',
            '1 Two 6',
        ]

        assert page_count == 10
        assert describe_entries(entries) == expected


class TestMain:
    def test_encrypted_pdf_exits_with_a_message(
        self,
        locked_pdf: pathlib.Path,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        exit_code = extract.main([
            str(locked_pdf),
            '--outline',
        ])
        printed = capsys.readouterr().err

        assert exit_code == 2
        assert printed.startswith('encrypted PDF: it needs a password')

    def test_outline_prints_the_chapter_numbers(
        self,
        outlined_pdf: pathlib.Path,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        exit_code = extract.main([
            str(outlined_pdf),
            '--outline',
        ])
        printed = capsys.readouterr().out

        assert exit_code == 0
        assert '1. One' in printed
        assert '· A section  (p. 5)' in printed

    def test_pages_without_text_write_nothing(
        self,
        outlined_pdf: pathlib.Path,
        tmp_path: pathlib.Path,
    ) -> None:
        output = tmp_path / 'Extracts'
        exit_code = extract.main([
            str(outlined_pdf),
            '--all',
            '--engine',
            'pypdf',
            '--out',
            str(output),
        ])
        written = sorted(
            path.name
            for path
            in (output / 'book').iterdir()
        )

        assert exit_code == 2
        assert written == ['OUTLINE.md']

    def test_split_alone_is_refused(self) -> None:
        with pytest.raises(SystemExit):
            extract.main([
                'book.pdf',
                '--split',
                'Intro=1-2',
            ])

    def test_split_with_chapters_keeps_the_number(
        self,
        outlined_pdf: pathlib.Path,
        tmp_path: pathlib.Path,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        extract.main([
            str(outlined_pdf),
            '--split',
            'Intro=1-2; One=3-6; Two=7-10',
            '--chapters',
            '3',
            '--engine',
            'pypdf',
            '--out',
            str(tmp_path / 'Extracts'),
        ])
        reported = capsys.readouterr().err
        not_written = [
            line.strip()
            for line
            in reported.splitlines()
            if 'not written:' in line
        ]
        expected = ['not written: 3. Two (p. 7–10) — 0 chars/page, no text layer']

        assert not_written == expected

    def test_split_with_outline_is_refused(self) -> None:
        exit_code = extract.main([
            'book.pdf',
            '--outline',
            '--split',
            'Intro=1-2',
        ])

        assert exit_code == 1


class TestParseNumbers:
    def test_missing_chapter_exits(self) -> None:
        with pytest.raises(SystemExit):
            extract.parse_numbers(
                '9',
                [
                    1,
                    2,
                ],
            )

    def test_numbers_and_ranges(self) -> None:
        result = extract.parse_numbers(
            '3, 1-2',
            [
                1,
                2,
                3,
                4,
            ],
        )
        expected = [
            1,
            2,
            3,
        ]

        assert result == expected


class TestParseSplit:
    def test_pages_outside_the_pdf_exit(self) -> None:
        with pytest.raises(SystemExit):
            extract.parse_split(
                'Intro=5-12',
                10,
            )

    def test_titles_and_one_based_pages(self) -> None:
        chapters = extract.parse_split(
            'Intro=1-2; =3',
            10,
        )
        expected = [
            '1 Intro 0-1',
            '2 Part 2 2-2',
        ]

        assert describe_chapters(chapters) == expected


class TestSlugify:
    def test_accents_and_punctuation(self) -> None:
        result = extract.slugify('Économie: the Débat, 2nd ed.')

        assert result == 'Economie_the_Debat_2nd_ed'
