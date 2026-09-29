"""
Fixtures shared by the tests of the skills' scripts: the scripts as modules, and PDFs built at run time.

No PDF is committed: each is written by hand — one Helvetica line per page — and its outline added
by pypdf, inside the test that needs it.
"""
import importlib
import importlib.util
import io
import itertools
import pathlib
import types

import pypdf
import pytest

REPOSITORY_ROOT = pathlib.Path(__file__).resolve().parents[1]
READ_SCRIPTS = REPOSITORY_ROOT / '.apm' / 'skills' / 'read' / 'scripts'
SCAFFOLD_SCRIPT = REPOSITORY_ROOT / '.apm' / 'skills' / 'init-strategy' / 'scripts' / 'scaffold.py'
# The pages of the book with an outline: front matter, then chapter one on page 2, chapter two on 3-4.
BOOK_PAGES = [
    'Preface of the test book, written only so that this page carries enough characters.',
    'Chapter One opens here: the equity premium was 4.25 percent over 1,200 months of data.',
    'Chapter Two opens here: momentum earned 0.75 percent a month across 480 portfolios.',
    'Chapter Two continues here: the crash of 2009 took 73.4 percent from the long-short book.',
]
BOOK_OUTLINE = {
    'Chapter One': 1,
    'Chapter Two': 2,
}
PLAIN_PAGES = [
    'Opening page of a report that carries no outline, long enough to hold a text layer.',
    'Second page of the report without an outline, again long enough to hold a text layer.',
    'Third and last page of the report without an outline, long enough for a text layer.',
]


def build_pdf(
    page_texts: list[str],
) -> bytes:
    """
    A PDF with one page per text, each text one line of Helvetica: catalog, pages, font, then a page
    and its content stream per text, with the cross-reference table their offsets make.
    """
    kids = ' '.join(
        f'{4 + 2 * index} 0 R'
        for index
        in range(len(page_texts))
    )
    header_objects = [
        '<< /Type /Catalog /Pages 2 0 R >>',
        f'<< /Type /Pages /Kids [{kids}] /Count {len(page_texts)} >>',
        '<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>',
    ]
    page_objects = [
        body
        for index, text
        in enumerate(page_texts)
        for body
        in _page_objects(
            index,
            text,
        )
    ]
    bodies = [
        *header_objects,
        *page_objects,
    ]
    chunks = [
        f'{number} 0 obj\n{body}\nendobj\n'.encode('latin-1')
        for number, body
        in enumerate(bodies, start=1)
    ]
    header = b'%PDF-1.4\n'
    chunk_lengths = [
        len(chunk)
        for chunk
        in chunks
    ]
    offsets = list(itertools.accumulate([
        len(header),
        *chunk_lengths[:-1],
    ]))
    cross_reference_start = len(header) + sum(chunk_lengths)
    object_count = len(bodies) + 1
    offset_lines = [
        f'{offset:010d} 00000 n \n'
        for offset
        in offsets
    ]
    cross_reference = ''.join([
        'xref\n',
        f'0 {object_count}\n',
        '0000000000 65535 f \n',
        *offset_lines,
        'trailer\n',
        f'<< /Size {object_count} /Root 1 0 R >>\n',
        'startxref\n',
        f'{cross_reference_start}\n',
        '%%EOF\n',
    ])
    pdf_bytes = b''.join([
        header,
        *chunks,
        cross_reference.encode('latin-1'),
    ])

    return pdf_bytes


@pytest.fixture
def extract_module(
    monkeypatch: pytest.MonkeyPatch,
) -> types.ModuleType:
    """
    `extract.py`, imported from the read skill's scripts folder.
    """
    monkeypatch.syspath_prepend(str(READ_SCRIPTS))
    module = importlib.import_module('extract')

    return module


@pytest.fixture
def outlined_book(
    tmp_path: pathlib.Path,
) -> pathlib.Path:
    """
    A four-page PDF whose outline names two chapters: page 1 is front matter, chapter two runs 3-4.
    """
    path = write_pdf(
        tmp_path / 'book.pdf',
        BOOK_PAGES,
        BOOK_OUTLINE,
    )

    return path


@pytest.fixture
def plain_report(
    tmp_path: pathlib.Path,
) -> pathlib.Path:
    """
    A three-page PDF with no outline.
    """
    path = write_pdf(
        tmp_path / 'report.pdf',
        PLAIN_PAGES,
        {},
    )

    return path


@pytest.fixture
def scaffold_module() -> types.ModuleType:
    """
    `scaffold.py`, loaded from the init-strategy skill's scripts folder.
    """
    specification = importlib.util.spec_from_file_location(
        'scaffold',
        SCAFFOLD_SCRIPT,
    )
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)

    return module


def write_pdf(
    path: pathlib.Path,
    page_texts: list[str],
    outline: dict[str, int],
) -> pathlib.Path:
    """
    Write a PDF of the given pages to `path`, with an outline item per title pointing to its 0-based page.
    """
    pdf_bytes = build_pdf(page_texts)
    reader = pypdf.PdfReader(io.BytesIO(pdf_bytes))
    writer = pypdf.PdfWriter(clone_from=reader)

    for title, page_index in outline.items():
        writer.add_outline_item(
            title,
            page_index,
        )

    with path.open('wb') as pdf_file:
        writer.write(pdf_file)

    return path


def _page_objects(
    index: int,
    text: str,
) -> list[str]:
    """
    The page object and the content stream of the page at `index`, the text drawn as one line.
    """
    stream = f'BT /F1 12 Tf 72 720 Td ({text}) Tj ET'
    page = ' '.join([
        '<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792]',
        '/Resources << /Font << /F1 3 0 R >> >>',
        f'/Contents {5 + 2 * index} 0 R >>',
    ])
    content = f'<< /Length {len(stream)} >>\nstream\n{stream}\nendstream'
    objects = [
        page,
        content,
    ]

    return objects
