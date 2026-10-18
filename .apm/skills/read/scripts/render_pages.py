# /// script
# requires-python = ">=3.10"
# dependencies = ["pypdfium2>=4.30", "pillow>=10.0"]
# ///
"""
A PDF's pages as PNG images, whole or a part, for what an extract cannot carry or a PDF reader
cannot show: a contents page, an equation, a figure, a table.

    uv run render_pages.py BOOK.pdf 12                        PDF page 12, at 150 dpi
    uv run render_pages.py BOOK.pdf 1-15 --dpi 100            a book's first fifteen pages
    uv run render_pages.py BOOK.pdf 52 --region 0,0.4,1,0.7   the band from 40% to 70% down the page
    uv run render_pages.py BOOK.pdf 52,60 --dpi 300 --grayscale

Pages are PDF pages, counted from the PDF's first page, as the extract's `<!-- p.N -->` markers
count them, never the numbers printed on a book's pages. The images go to a folder of their own in
the system's temporary folder, `kaxanuk-pages/<slug>/`, the slug made as extract.py makes it, and
never into a library: they are a view of the source, regenerable, and never cited. Each image is
named by its page, `p052.png`, and a part by its region in percent, `p052_0-40-100-70.png`. One
line is printed per image: its path, its page and its size in pixels. It renders with PDFium,
through pypdfium2, so it needs no Poppler, no `pdftoppm` and nothing on the PATH.

Options
    --dpi N              dots per inch, 36 to 600 (default 150; 200 to 300 for an equation)
    --region L,T,R,B     a part of the page: its left, top, right and bottom edges as fractions of
                         the page's width and height, 0 to 1, from its top left corner
    --grayscale          render in shades of grey
    --out DIR            where the images go, in place of the temporary folder
    --password TEXT      a PDF that asks for one; an owner-only lock needs none

Exit codes: 0 every image written · 1 usage: a file that is not a PDF, a page outside it, a region
or a dpi out of range · 2 the PDF cannot be opened: damaged, or a password needed.
Without uv: pip install pypdfium2 pillow, then python render_pages.py ...
"""
import argparse
import dataclasses
import pathlib
import re
import sys
import tempfile
import typing
import unicodedata

try:
    import pypdfium2
except ImportError:
    sys.exit('pypdfium2 is not installed: run this with `uv run`, or `pip install pypdfium2 pillow`.')

DPI_RANGE = range(
    36,
    601,
)
OUTPUT_FOLDER_NAME = 'kaxanuk-pages'
PAGE_ITEM = re.compile(r'^\s*(\d+)\s*(?:-\s*(\d+))?\s*$')
POINTS_PER_INCH = 72
SLUG_LENGTH = 80
WORD = re.compile(r'[A-Za-z0-9]+')


@dataclasses.dataclass(frozen=True)
class Region:
    """
    A part of a page: its left, top, right and bottom edges as fractions of the page, from its top
    left corner.
    """
    bottom: float
    left: float
    right: float
    top: float


class CommandLineParser(argparse.ArgumentParser):
    """
    The argument parser, exiting 1 on a command line it rejects, so that 2 means a PDF it cannot open.
    """

    def error(
        self,
        message: str,
    ) -> typing.NoReturn:
        """
        Print the usage and the problem, and exit 1.
        """
        self.print_usage(sys.stderr)
        problem = f'{self.prog}: error: {message}'
        print(problem, file=sys.stderr)
        sys.exit(1)


def default_folder(
    pdf_path: pathlib.Path,
) -> pathlib.Path:
    """
    Where a PDF's images go by default: `kaxanuk-pages/<slug>/` in the system's temporary folder.
    """
    temporary = pathlib.Path(tempfile.gettempdir())
    folder = temporary / OUTPUT_FOLDER_NAME / slugify(pdf_path.stem)

    return folder


def image_name(
    page_number: int,
    region: Region | None,
) -> str:
    """
    An image's file name: its page, three digits, and its region in whole percent when there is one.
    """
    page_part = f'p{page_number:03d}'

    if region is None:

        return f'{page_part}.png'

    edges = '-'.join(
        str(round(edge * 100))
        for edge
        in (
            region.left,
            region.top,
            region.right,
            region.bottom,
        )
    )
    name = f'{page_part}_{edges}.png'

    return name


def main(
    arguments: list[str] | None = None,
) -> int:
    """
    Parse the command line, open the PDF, and write one image per page asked for.
    """
    for console_stream in (sys.stdout, sys.stderr):
        try:
            console_stream.reconfigure(
                encoding='utf-8',
                errors='replace',
            )
        except (AttributeError, ValueError):
            pass

    parser = _build_parser()
    parsed = parser.parse_args(arguments)
    pdf_path = pathlib.Path(parsed.pdf)

    if not pdf_path.is_file() or pdf_path.suffix.lower() != '.pdf':
        parser.error(f'not a PDF file: {pdf_path}')

    if parsed.dpi not in DPI_RANGE:
        parser.error(f'--dpi {parsed.dpi} is outside 36 to 600')

    region = parse_region(parsed.region) if parsed.region else None

    if parsed.region and region is None:
        parser.error(f'--region {parsed.region}: four fractions L,T,R,B with 0 <= L < R <= 1 and 0 <= T < B <= 1')

    try:
        document = pypdfium2.PdfDocument(
            str(pdf_path),
            password=parsed.password,
        )
    except pypdfium2.PdfiumError as error:
        print(f'cannot open {pdf_path}: {error}', file=sys.stderr)

        return 2

    page_count = len(document)
    page_numbers = parse_pages(
        parsed.pages,
        page_count,
    )

    if page_numbers is None:
        parser.error(f'pages {parsed.pages}: the PDF has pages 1 to {page_count}')

    out_folder = pathlib.Path(parsed.out) if parsed.out else default_folder(pdf_path)
    out_folder.mkdir(
        parents=True,
        exist_ok=True,
    )

    for page_number in page_numbers:
        line = render_page(
            document,
            page_number,
            region,
            parsed.dpi,
            parsed.grayscale,
            out_folder,
        )
        print(line)

    return 0


def parse_pages(
    text: str,
    page_count: int,
) -> list[int] | None:
    """
    The pages a list asks for — `12`, `1-15`, `52,60-62` — in order, each once; None when an item
    cannot be read or names a page outside the PDF.
    """
    matches = [
        PAGE_ITEM.match(item)
        for item
        in text.split(',')
    ]

    unreadable = [
        item
        for item, match
        in zip(text.split(','), matches)
        if match is None
    ]

    if unreadable:

        return None

    ranges = [
        _page_range(match)
        for match
        in matches
    ]
    pages = list(dict.fromkeys(
        page
        for page_range
        in ranges
        for page
        in page_range
    ))
    inside = bool(pages) and all(
        1 <= page <= page_count
        for page
        in pages
    )
    chosen = pages if inside else None

    return chosen


def parse_region(
    text: str,
) -> Region | None:
    """
    A region from `L,T,R,B`, four fractions of the page; None when it is not four numbers with the
    left edge before the right, the top above the bottom, all of them from 0 to 1.
    """
    parts = text.split(',')

    try:
        edges = [
            float(part)
            for part
            in parts
        ]
    except ValueError:

        return None

    if len(edges) != 4:

        return None

    left, top, right, bottom = edges
    is_ordered = 0 <= left < right <= 1 and 0 <= top < bottom <= 1
    region = Region(
        bottom=bottom,
        left=left,
        right=right,
        top=top,
    ) if is_ordered else None

    return region


def render_page(
    document: pypdfium2.PdfDocument,
    page_number: int,
    region: Region | None,
    dpi: int,
    grayscale: bool,
    out_folder: pathlib.Path,
) -> str:
    """
    One page, or its region, rendered and saved as a PNG; the line that reports it.
    """
    page = document[page_number - 1]
    width, height = page.get_size()
    # What PDFium crops from each side, in points: left, bottom, right, top.
    crop = (
        0,
        0,
        0,
        0,
    ) if region is None else (
        region.left * width,
        (1 - region.bottom) * height,
        (1 - region.right) * width,
        region.top * height,
    )
    bitmap = page.render(
        scale=dpi / POINTS_PER_INCH,
        crop=crop,
        grayscale=grayscale,
    )
    image = bitmap.to_pil()
    image_path = out_folder / image_name(
        page_number,
        region,
    )
    image.save(image_path)
    line = f'{image_path.as_posix()}  page {page_number}  {image.width}x{image.height}'

    return line


def slugify(
    text: str,
) -> str:
    """
    A file name as extract.py makes its folder's: its ASCII words joined by underscores, at most 80
    characters.
    """
    decomposed = unicodedata.normalize(
        'NFKD',
        text,
    )
    ascii_bytes = decomposed.encode(
        'ascii',
        'ignore',
    )
    ascii_text = ascii_bytes.decode('ascii')
    joined = '_'.join(WORD.findall(ascii_text))
    slug = joined[:SLUG_LENGTH].rstrip('_') or 'Untitled'

    return slug


def _build_parser() -> CommandLineParser:
    """
    The command line: the PDF, its pages, and how to render them.
    """
    parser = CommandLineParser(
        prog='render_pages.py',
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        'pdf',
        help='the PDF',
    )
    parser.add_argument(
        'pages',
        help='PDF pages: 12, 1-15 or 52,60-62',
    )
    parser.add_argument(
        '--dpi',
        type=int,
        default=150,
        help='dots per inch, 36 to 600 (default 150)',
    )
    parser.add_argument(
        '--region',
        help='L,T,R,B: a part of the page, as fractions from its top left corner',
    )
    parser.add_argument(
        '--grayscale',
        action='store_true',
        help='render in shades of grey',
    )
    parser.add_argument(
        '--out',
        help='where the images go (default: kaxanuk-pages/<slug>/ in the temporary folder)',
    )
    parser.add_argument(
        '--password',
        help='the password of a PDF that asks for one',
    )

    return parser



def _page_range(
    match: re.Match[str],
) -> range:
    """
    The pages one item of a page list names, inclusive: `12`, or `1-15`.
    """
    first_page = int(match.group(1))
    last_text = match.group(2) or match.group(1)
    last_page = int(last_text)
    pages = range(first_page, last_page + 1)

    return pages

if __name__ == '__main__':
    sys.exit(main())
