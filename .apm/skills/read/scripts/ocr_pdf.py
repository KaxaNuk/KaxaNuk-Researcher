# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["numpy", "pypdf[crypto]>=4.0", "pypdfium2>=4.30", "rapidocr_onnxruntime>=1.3,<2"]
# ///
"""
A searchable copy of a scanned PDF: every page as it was, with the text an OCR engine reads on it
laid over the page as invisible text, so extract.py, a PDF reader's search and a copy all find it.

    uv run ocr_pdf.py "Sources/Books/Markowitz 1959.pdf"            every page
    uv run ocr_pdf.py "Sources/Books/Markowitz 1959.pdf" --pages 1-40
    uv run ocr_pdf.py SCAN.pdf --out Bibliotheca/Books --dpi 300

It writes `<the scan's name> (OCR).pdf` beside the scan, or in --out, never over a file that is
there, and never touches the scan. Each page is rendered at --dpi in shades of grey with PDFium,
through pypdfium2, and read by RapidOCR with its angle classifier off: on, it turned about one line
in ten upside down or into noise. Each line it finds is written at its place on the page in
invisible Helvetica, sized to its box, so the copy looks exactly like the scan. Text outside the
Windows-1252 characters Helvetica carries — a Greek letter, most mathematical signs — is written as
`?`: the page image keeps the original, and the read skill's render_pages.py shows it.

The copy holds every page of the scan, so its PDF pages are the scan's; --pages limits the pages
read, for a scan only some of whose pages lack a text layer. A page that already has one — at least
--min-chars characters a page on average over the pages asked for — is refused: extract.py reads it
as it is. OCR makes mistakes a reader must catch — it runs words together, `TOWARDSRISK`, and
misreads a digit or a sign — so a figure, a name or a formula from an OCR copy is checked against
the page's image before a note states it.

The engine runs on the computer, with nothing sent anywhere; the first run downloads it with its
models, about 100 MB, into uv's cache. A page takes a few seconds; one line is printed per page.

Options
    --pages LIST     PDF pages to read: 12, 1-40 or 3,7-9 (default every page)
    --dpi N          dots per inch the pages are read at, 100 to 400 (default 200)
    --out DIR        the folder the copy goes in (default the scan's own folder)
    --min-chars N    a text layer at or above this many characters a page refuses the run (default 40)

Exit codes: 0 the copy written · 1 usage: not a PDF, a page outside it, a dpi out of range, the copy
already there, or a text layer already · 2 the PDF cannot be opened: damaged, or a password needed.
Without uv: pip install numpy "pypdf[crypto]" pypdfium2 "rapidocr_onnxruntime<2" on Python 3.10 to
3.12, then python ocr_pdf.py ...
"""
import argparse
import dataclasses
import pathlib
import re
import sys
import time
import typing
import unicodedata

try:
    import numpy
    import pypdf
    import pypdfium2
    import rapidocr_onnxruntime
except ImportError as missing:
    sys.exit(f'{missing.name} is not installed: run this with `uv run`, which reads what it needs from its first lines.')

DPI_RANGE = range(
    100,
    401,
)
FONT_NAME = '/KaxaNukOCR'
OCR_SUFFIX = ' (OCR)'
PAGE_ITEM = re.compile(r'^\s*(\d+)\s*(?:-\s*(\d+))?\s*$')
POINTS_PER_INCH = 72
# How much of a line's box its letters fill, and where the baseline sits in it, from the bottom.
BASELINE_SHARE = 0.2
FONT_SHARE = 0.8
# Helvetica's widths, in thousandths of an em, for the characters from the space to the tilde; any
# other character is taken as 556, a digit's width.
HELVETICA_WIDTHS = [
    int(width)
    for width
    in ' '.join([
        '278 278 355 556 556 889 667 191 333 333 389 584 278 333 278 278',
        '556 556 556 556 556 556 556 556 556 556 278 278 584 584 584 556',
        '1015 667 667 722 722 667 611 778 722 278 500 667 556 833 722 778',
        '667 778 722 667 611 722 667 944 667 667 611 278 278 278 469 556',
        '333 556 556 500 556 556 278 556 556 222 222 500 222 833 556 556',
        '556 556 333 500 278 556 500 722 500 500 500 334 260 334 584',
    ]).split()
]
DEFAULT_WIDTH = 556
# Signs an OCR engine gives that Windows-1252 lacks, and the nearest it has.
PLAIN_SIGNS = str.maketrans({
    '−': '-',
    'ﬁ': 'fi',
    'ﬂ': 'fl',
})


@dataclasses.dataclass(frozen=True)
class PageGeometry:
    """
    Where a rendered page sits in the PDF's own coordinates: its visible box and its rotation.
    """
    bottom: float
    height: float
    left: float
    rotation: int
    width: float


@dataclasses.dataclass(frozen=True)
class PagePoint:
    """
    A point in the PDF's own coordinates, in points from its origin.
    """
    x_position: float
    y_position: float


@dataclasses.dataclass(frozen=True)
class TextLine:
    """
    One line the engine read: its text, and its box in points from the rendered page's top left.
    """
    bottom: float
    left: float
    right: float
    text: str
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


def copy_path(
    pdf_path: pathlib.Path,
    out_folder: pathlib.Path | None,
) -> pathlib.Path:
    """
    Where the searchable copy goes: `<the scan's name> (OCR).pdf`, beside the scan or in the folder
    given.
    """
    folder = pdf_path.parent if out_folder is None else out_folder
    path = folder / f'{pdf_path.stem}{OCR_SUFFIX}{pdf_path.suffix}'

    return path


def line_content(
    line: TextLine,
    geometry: PageGeometry,
) -> bytes:
    """
    The PDF operators that write one line as invisible text over its box: render mode 3, Helvetica
    sized to the box's height and stretched to its width, along the page as it is shown.
    """
    box_height = line.bottom - line.top
    box_width = line.right - line.left
    font_size = max(box_height * FONT_SHARE, 1.0)
    plain = _plain_text(line.text)
    nominal_width = font_size * _text_width(plain) / 1000
    stretch = 100 * box_width / nominal_width if nominal_width > 0 else 100
    baseline = line.bottom - box_height * BASELINE_SHARE
    origin = page_point(
        geometry,
        line.left,
        baseline,
    )
    along = page_point(
        geometry,
        line.left + 1,
        baseline,
    )
    upward = page_point(
        geometry,
        line.left,
        baseline - 1,
    )
    matrix = ' '.join(
        f'{number:.4f}'
        for number
        in (
            along.x_position - origin.x_position,
            along.y_position - origin.y_position,
            upward.x_position - origin.x_position,
            upward.y_position - origin.y_position,
            origin.x_position,
            origin.y_position,
        )
    )
    encoded = _pdf_string(plain)
    operators = b''.join([
        f'BT {FONT_NAME} {font_size:.2f} Tf 3 Tr {stretch:.2f} Tz {matrix} Tm '.encode('ascii'),
        encoded,
        b' Tj ET\n',
    ])

    return operators


def main(
    arguments: list[str] | None = None,
) -> int:
    """
    Parse the command line, check the scan and the copy's place, then read and write page by page.
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
    out_folder = pathlib.Path(parsed.out) if parsed.out else None
    target = copy_path(
        pdf_path,
        out_folder,
    )
    problem = _usage_problem(
        parsed,
        pdf_path,
        target,
    )

    if problem is not None:
        parser.error(problem)

    try:
        reader = pypdf.PdfReader(str(pdf_path))
        locked = reader.is_encrypted and not reader.decrypt('')
        rendered = pypdfium2.PdfDocument(str(pdf_path))
    except (
        pypdf.errors.PdfReadError,
        pypdfium2.PdfiumError,
        NotImplementedError,
    ) as error:
        print(f'cannot open {pdf_path}: {error}', file=sys.stderr)

        return 2

    if locked:
        print(f'{pdf_path} needs a password: save an unprotected copy and run this on it', file=sys.stderr)

        return 2

    page_numbers = parse_pages(
        parsed.pages,
        len(reader.pages),
    )

    if page_numbers is None:
        parser.error(f'--pages {parsed.pages}: the PDF has pages 1 to {len(reader.pages)}')

    text_average = _text_layer_average(
        reader,
        page_numbers,
    )

    if text_average >= parsed.min_chars:
        parser.error(f'{pdf_path.name} has a text layer, {text_average:.0f} characters a page: extract.py reads it as it is')

    writer = pypdf.PdfWriter(clone_from=reader)
    engine = rapidocr_onnxruntime.RapidOCR()
    started = time.monotonic()

    for page_number in page_numbers:
        lines = read_page(
            engine,
            rendered[page_number - 1],
            parsed.dpi,
        )
        geometry = _geometry(writer.pages[page_number - 1])
        _lay_text(
            writer,
            page_number,
            lines,
            geometry,
        )
        elapsed = time.monotonic() - started
        print(f'page {page_number}: {len(lines)} lines, {elapsed:.0f} s', flush=True)

    target.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with target.open('xb') as copy_file:
        writer.write(copy_file)

    page_count = len(reader.pages)
    read_count = len(page_numbers)
    print(f'wrote {target.as_posix()}: {read_count} of {page_count} pages read')

    return 0


def page_point(
    geometry: PageGeometry,
    across: float,
    down: float,
) -> PagePoint:
    """
    A point of the rendered page — points across from its left and down from its top, as it is
    shown — in the PDF's own coordinates, its rotation undone.
    """
    rotation = geometry.rotation % 360
    points = {
        0: PagePoint(
            x_position=geometry.left + across,
            y_position=geometry.bottom + geometry.height - down,
        ),
        90: PagePoint(
            x_position=geometry.left + down,
            y_position=geometry.bottom + across,
        ),
        180: PagePoint(
            x_position=geometry.left + geometry.width - across,
            y_position=geometry.bottom + down,
        ),
        270: PagePoint(
            x_position=geometry.left + geometry.width - down,
            y_position=geometry.bottom + geometry.height - across,
        ),
    }
    point = points.get(rotation, points[0])

    return point


def parse_pages(
    text: str | None,
    page_count: int,
) -> list[int] | None:
    """
    The pages a list asks for — `12`, `1-40`, `3,7-9` — in order, each once, or every page when no
    list is given; None when an item cannot be read or names a page outside the PDF.
    """
    if text is None:
        every_page = list(range(1, page_count + 1))

        return every_page

    matches = [
        PAGE_ITEM.match(item)
        for item
        in text.split(',')
    ]
    unreadable = [
        match
        for match
        in matches
        if match is None
    ]

    if unreadable:

        return None

    pages = list(dict.fromkeys(
        page
        for match
        in matches
        for page
        in _page_range(match)
    ))
    inside = bool(pages) and all(
        1 <= page <= page_count
        for page
        in pages
    )
    chosen = pages if inside else None

    return chosen


def read_page(
    engine: rapidocr_onnxruntime.RapidOCR,
    page: pypdfium2.PdfPage,
    dpi: int,
) -> list[TextLine]:
    """
    One page rendered in shades of grey and read by the engine, its angle classifier off; each line
    with its box in points.
    """
    scale = dpi / POINTS_PER_INCH
    bitmap = page.render(
        scale=scale,
        grayscale=True,
    )
    grey = numpy.asarray(bitmap.to_numpy())
    channels = grey.reshape(
        grey.shape[0],
        grey.shape[1],
        -1,
    )
    single = channels[:, :, 0]
    stacked = numpy.stack(
        [
            single,
            single,
            single,
        ],
        axis=-1,
    )
    image = numpy.ascontiguousarray(stacked)
    result, _ = engine(
        image,
        use_cls=False,
    )
    lines = [
        _text_line(
            box,
            text,
            scale,
        )
        for box, text, _
        in result or []
        if text.strip()
    ]

    return lines


def _build_parser() -> CommandLineParser:
    """
    The command line: the scan, its pages, the dpi, where the copy goes, and the text-layer bar.
    """
    parser = CommandLineParser(
        prog='ocr_pdf.py',
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        'pdf',
        help='the scanned PDF',
    )
    parser.add_argument(
        '--pages',
        help='PDF pages to read: 12, 1-40 or 3,7-9 (default every page)',
    )
    parser.add_argument(
        '--dpi',
        type=int,
        default=200,
        help='dots per inch the pages are read at, 100 to 400 (default 200)',
    )
    parser.add_argument(
        '--out',
        help="the folder the copy goes in (default the scan's own folder)",
    )
    parser.add_argument(
        '--min-chars',
        type=int,
        default=40,
        help='characters a page, on average, from which a text layer refuses the run (default 40)',
    )

    return parser


def _font_resource() -> pypdf.generic.DictionaryObject:
    """
    Helvetica, one of the fonts every PDF reader carries, so nothing is embedded.
    """
    font = pypdf.generic.DictionaryObject({
        pypdf.generic.NameObject('/Type'): pypdf.generic.NameObject('/Font'),
        pypdf.generic.NameObject('/Subtype'): pypdf.generic.NameObject('/Type1'),
        pypdf.generic.NameObject('/BaseFont'): pypdf.generic.NameObject('/Helvetica'),
        pypdf.generic.NameObject('/Encoding'): pypdf.generic.NameObject('/WinAnsiEncoding'),
    })

    return font


def _geometry(
    page: pypdf.PageObject,
) -> PageGeometry:
    """
    A page's visible box — its crop box, which is its media box when it has none — and its rotation.
    """
    box = page.cropbox
    geometry = PageGeometry(
        bottom=float(box.bottom),
        height=float(box.height),
        left=float(box.left),
        rotation=int(page.rotation or 0),
        width=float(box.width),
    )

    return geometry


def _lay_text(
    writer: pypdf.PdfWriter,
    page_number: int,
    lines: list[TextLine],
    geometry: PageGeometry,
) -> None:
    """
    One page's lines laid over it as invisible text: a page of text alone, merged onto the scan's.
    """
    if not lines:

        return

    page = writer.pages[page_number - 1]
    content = b''.join(
        line_content(
            line,
            geometry,
        )
        for line
        in lines
    )
    stream = pypdf.generic.DecodedStreamObject()
    stream.set_data(b''.join([
        b'q\n',
        content,
        b'Q\n',
    ]))
    overlay = pypdf.PageObject.create_blank_page(
        width=float(page.mediabox.width),
        height=float(page.mediabox.height),
    )
    fonts = pypdf.generic.DictionaryObject({
        pypdf.generic.NameObject(FONT_NAME): _font_resource(),
    })
    overlay[pypdf.generic.NameObject('/Resources')] = pypdf.generic.DictionaryObject({
        pypdf.generic.NameObject('/Font'): fonts,
    })
    overlay[pypdf.generic.NameObject('/Contents')] = stream
    page.merge_page(overlay)


def _page_range(
    match: re.Match[str],
) -> range:
    """
    The pages one item of a page list names, inclusive: `12`, or `1-40`.
    """
    first_page = int(match.group(1))
    last_text = match.group(2) or match.group(1)
    last_page = int(last_text)
    pages = range(first_page, last_page + 1)

    return pages


def _pdf_string(
    text: str,
) -> bytes:
    """
    A text as a PDF literal string in Windows-1252, its backslashes and parentheses escaped.
    """
    encoded = text.encode(
        'cp1252',
        errors='replace',
    )
    without_backslashes = encoded.replace(b'\\', b'\\\\')
    without_openings = without_backslashes.replace(b'(', b'\\(')
    escaped = without_openings.replace(b')', b'\\)')
    literal = b''.join([
        b'(',
        escaped,
        b')',
    ])

    return literal


def _plain_text(
    text: str,
) -> str:
    """
    A line's text in one Unicode form, the signs Windows-1252 lacks swapped for the nearest it has.
    """
    composed = unicodedata.normalize(
        'NFC',
        text,
    )
    plain = composed.translate(PLAIN_SIGNS)

    return plain


def _text_layer_average(
    reader: pypdf.PdfReader,
    page_numbers: list[int],
) -> float:
    """
    The characters a page the scan's own text layer holds, on average over the pages asked for.
    """
    characters = sum(
        len(reader.pages[page_number - 1].extract_text() or '')
        for page_number
        in page_numbers
    )
    average = characters / max(len(page_numbers), 1)

    return average


def _text_line(
    box: list[list[float]],
    text: str,
    scale: float,
) -> TextLine:
    """
    A line the engine gave — its four corners in pixels and its text — as a box in points.
    """
    across = [
        corner[0] / scale
        for corner
        in box
    ]
    down = [
        corner[1] / scale
        for corner
        in box
    ]
    line = TextLine(
        bottom=max(down),
        left=min(across),
        right=max(across),
        text=text.strip(),
        top=min(down),
    )

    return line


def _text_width(
    text: str,
) -> int:
    """
    A text's width in Helvetica, in thousandths of an em at size one.
    """
    width = sum(
        HELVETICA_WIDTHS[ord(character) - 32] if 32 <= ord(character) <= 126 else DEFAULT_WIDTH
        for character
        in text
    )

    return width


def _usage_problem(
    parsed: argparse.Namespace,
    pdf_path: pathlib.Path,
    target: pathlib.Path,
) -> str | None:
    """
    What makes the command line unusable before anything is read: not a PDF, a dpi out of range,
    the copy already there.
    """
    is_pdf = pdf_path.is_file() and pdf_path.suffix.lower() == '.pdf'
    candidates = [
        f'not a PDF file: {pdf_path}' if not is_pdf else None,
        f'--dpi {parsed.dpi} is outside 100 to 400' if parsed.dpi not in DPI_RANGE else None,
        f'{target} is there already: nothing is written over it' if target.exists() else None,
        f'{pdf_path.name} is a searchable copy already' if pdf_path.stem.endswith(OCR_SUFFIX) else None,
    ]
    problem = next(
        (
            candidate
            for candidate
            in candidates
            if candidate is not None
        ),
        None,
    )

    return problem


if __name__ == '__main__':
    sys.exit(main())
