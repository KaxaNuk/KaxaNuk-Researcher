# /// script
# requires-python = ">=3.10"
# dependencies = ["pypdf>=4.0"]
# ///
"""The deterministic half of /read: a PDF's table of contents, and one markdown file per chapter.

It reads the outline — the bookmarks — a PDF carries, turns it into page ranges, and writes the
text of the chapters asked for into an extracts folder, a marker before every page. It has no
opinion about what matters: choosing chapters is the owner's, with this outline in front of them,
and the note is the researcher's. Extracts are a cache — regenerable, gitignored, never cited.

    uv run extract.py BOOK.pdf --outline                the outline and the page count; nothing written
    uv run extract.py BOOK.pdf --chapters 3,4,7         those chapters, by their number in the outline
    uv run extract.py BOOK.pdf --all                    every chapter; with no outline, the whole PDF as one file
    uv run extract.py BOOK.pdf --split "Introduction=1-12; Chapter 1=13-40"
                                                        no outline: chapters by page range, titles yours

Options
    --out DIR       where extracts go (default ./Extracts); this PDF's land in DIR/<pdf stem>/
    --depth N       the outline depth that counts as a chapter (default 1; use 2 when depth 1 is parts)
    --engine E      auto | pdftotext | pypdf (default auto: pdftotext when on PATH, else pypdf).
                    pdftotext reflows a page's lines into paragraphs; pypdf keeps the line breaks,
                    which tables and verse prefer
    --min-chars N   fewer characters per page than this, on average, means no text layer (default 40)

Exit codes: 0 done · 1 usage · 2 no text layer, nothing written · 3 no outline for --chapters
Without uv: pip install pypdf, then python extract.py ...
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:  # pragma: no cover
    sys.exit("pypdf is not installed: run this with `uv run`, or `pip install pypdf`.")

for stream in (sys.stdout, sys.stderr):  # page ranges carry an en dash; Windows consoles may not
    try:
        stream.reconfigure(encoding="utf-8")
    except Exception:  # pragma: no cover
        pass


@dataclass
class Entry:
    depth: int
    title: str
    page: int  # 0-based


@dataclass
class Chapter:
    number: int
    title: str
    start: int  # 0-based, inclusive
    end: int  # 0-based, inclusive

    @property
    def pages(self) -> str:
        return f"{self.start + 1}–{self.end + 1}" if self.end > self.start else f"{self.start + 1}"


# ------------------------------------------------------------------------------- the outline
def flatten_outline(reader: PdfReader) -> list[Entry]:
    """The bookmarks as a flat list with depths. pypdf nests children as a list after their parent."""
    entries: list[Entry] = []

    def walk(items, depth: int) -> None:
        for item in items:
            if isinstance(item, list):
                walk(item, depth + 1)
                continue
            try:
                page = reader.get_destination_page_number(item)
            except Exception:
                page = None
            title = str(getattr(item, "title", "")).strip() or "(untitled)"
            if page is None:
                print(f"  outline entry without a page, skipped: {title!r}", file=sys.stderr)
                continue
            entries.append(Entry(depth, title, int(page)))

    try:
        outline = reader.outline
    except Exception as exc:
        print(f"  outline unreadable: {exc}", file=sys.stderr)
        return []
    walk(outline or [], 1)
    return entries


def chapters_from_outline(entries: list[Entry], depth: int, n_pages: int) -> list[Chapter]:
    """Entries at `depth` are the chapters. A chapter runs to the page before the next entry at
    that depth or shallower begins; the last runs to the end. Pages before the first chapter are
    chapter 0, front matter."""
    boundaries = sorted((e for e in entries if e.depth <= depth), key=lambda e: e.page)
    first = next((e.page for e in boundaries if e.depth == depth), None)
    if first is None:
        return []
    chapters: list[Chapter] = []
    if first > 0:
        chapters.append(Chapter(0, "Front matter", 0, first - 1))
    number = 0
    for i, e in enumerate(boundaries):
        if e.depth != depth:
            continue
        nxt = next((b.page for b in boundaries[i + 1 :] if b.page > e.page), n_pages)
        number += 1
        chapters.append(Chapter(number, e.title, e.page, min(nxt, n_pages) - 1))
    return chapters


def parse_split(spec: str, n_pages: int) -> list[Chapter]:
    """`Title=first-last; Title=first-last` — pages 1-based, inclusive."""
    chapters: list[Chapter] = []
    for k, part in enumerate(p.strip() for p in spec.split(";") if p.strip()):
        if "=" not in part:
            sys.exit(f"--split: each item is Title=first-last, got {part!r}")
        title, rng = part.rsplit("=", 1)
        m = re.fullmatch(r"\s*(\d+)\s*(?:-\s*(\d+))?\s*", rng)
        if not m:
            sys.exit(f"--split: bad page range {rng!r} in {part!r}")
        a, b = int(m.group(1)), int(m.group(2) or m.group(1))
        if not 1 <= a <= b <= n_pages:
            sys.exit(f"--split: pages {a}-{b} outside 1-{n_pages} in {part!r}")
        chapters.append(Chapter(k + 1, title.strip() or f"Part {k + 1}", a - 1, b - 1))
    return chapters


def parse_numbers(spec: str, available: list[int]) -> list[int]:
    wanted: list[int] = []
    for tok in (t.strip() for t in spec.split(",") if t.strip()):
        m = re.fullmatch(r"(\d+)(?:-(\d+))?", tok)
        if not m:
            sys.exit(f"--chapters: numbers and ranges only, got {tok!r}")
        a, b = int(m.group(1)), int(m.group(2) or m.group(1))
        wanted.extend(range(a, b + 1))
    missing = sorted(set(wanted) - set(available))
    if missing:
        sys.exit(f"--chapters: no chapter {missing} at this depth; run --outline to see the numbers")
    return sorted(set(wanted))


# ------------------------------------------------------------------------------- the text
def pdftotext_label() -> str | None:
    exe = shutil.which("pdftotext")
    if not exe:
        return None
    try:
        out = subprocess.run([exe, "-v"], capture_output=True, text=True)
        first = ((out.stderr or out.stdout).strip().splitlines() or ["pdftotext"])[0]
        return first.strip()
    except Exception:
        return "pdftotext"


def pages_pdftotext(pdf: Path, start: int, end: int) -> list[str]:
    cmd = ["pdftotext", "-f", str(start + 1), "-l", str(end + 1), "-enc", "UTF-8", str(pdf), "-"]
    out = subprocess.run(cmd, capture_output=True)
    if out.returncode != 0:
        raise RuntimeError(out.stderr.decode("utf-8", "replace").strip() or "pdftotext failed")
    pages = out.stdout.decode("utf-8", "replace").split("\f")
    if pages and pages[-1].strip() == "":
        pages.pop()
    want = end - start + 1
    return (pages + [""] * want)[:want]


def pages_pypdf(reader: PdfReader, start: int, end: int) -> list[str]:
    return [(reader.pages[i].extract_text() or "") for i in range(start, end + 1)]


def clean(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def slugify(title: str, limit: int = 60) -> str:
    """`Author_Year_Title` style, the way the notes are named: ascii words joined by underscores,
    the source's own capitals kept."""
    s = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    s = re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")
    return s[:limit].rstrip("_") or "Untitled"


def yaml_str(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


# ------------------------------------------------------------------------------- writing
def write_outline(out_dir: Path, source: str, n_pages: int, chapters: list[Chapter], how: str) -> Path:
    lines = [
        f"# {out_dir.name} — table of contents",
        "",
        f"Source: `{source}` — {n_pages} pages — chapters from {how}.",
        "Extracted chapters sit beside this file, one per chapter, numbered as below.",
        "Regenerable and gitignored: cite the source, never this.",
        "",
        "| # | Chapter | Pages |",
        "| --- | --- | --- |",
    ]
    lines += [f"| {c.number} | {c.title} | {c.pages} |" for c in chapters]
    path = out_dir / "OUTLINE.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return path


def write_chapter(out_dir: Path, source: str, ch: Chapter, pages: list[str], engine: str) -> Path:
    body = "\n".join(f"<!-- p.{ch.start + i + 1} -->\n{clean(text)}\n" for i, text in enumerate(pages))
    content = (
        "---\n"
        f"source: {yaml_str(source)}\n"
        f"chapter: {ch.number}\n"
        f"title: {yaml_str(ch.title)}\n"
        f"pages: {yaml_str(ch.pages)}\n"
        f"engine: {yaml_str(engine)}\n"
        "---\n\n"
        f"# {ch.number}. {ch.title}\n\n"
        f"{body}"
    )
    path = out_dir / f"{ch.number:02d}_{slugify(ch.title)}.md"
    path.write_text(content, encoding="utf-8", newline="\n")
    return path


def print_outline(pdf: Path, n_pages: int, entries: list[Entry], depth: int) -> None:
    print(f"{pdf.name}: {n_pages} pages")
    if not entries:
        print("  no outline (no bookmarks). Read the table-of-contents pages and pass")
        print('  --split "Title=first-last; Title=first-last", or --all for the whole PDF as one file.')
        return
    counts = {d: sum(1 for e in entries if e.depth == d) for d in sorted({e.depth for e in entries})}
    print("  outline entries: " + ", ".join(f"depth {d}: {c}" for d, c in counts.items()))
    chapters = chapters_from_outline(entries, depth, n_pages)
    print(f"  chapters at --depth {depth} (the numbers --chapters takes):")
    width = max(len(c.title) for c in chapters) if chapters else 10
    for c in chapters:
        print(f"  {c.number:>3}. {c.title:<{min(width, 70)}}  p. {c.pages}")
        if depth == 1:
            for e in entries:
                if e.depth == 2 and c.start <= e.page <= c.end:
                    print(f"         · {e.title}  (p. {e.page + 1})")
    if counts.get(depth, 0) <= 3 and counts.get(depth + 1, 0) >= 4:
        print(f"  depth {depth} looks like parts; consider --depth {depth + 1}")


# ------------------------------------------------------------------------------- main
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="extract.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("pdf")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--outline", action="store_true", help="print the outline; write nothing")
    mode.add_argument("--chapters", metavar="N,N-M", help="extract these chapters, by outline number")
    mode.add_argument("--all", action="store_true", help="extract every chapter")
    mode.add_argument("--split", metavar="SPEC", help='"Title=first-last; ..." when there is no outline')
    ap.add_argument("--out", default="Extracts", help="extracts root (default ./Extracts)")
    ap.add_argument("--depth", type=int, default=1, help="outline depth that counts as a chapter")
    ap.add_argument("--engine", choices=["auto", "pdftotext", "pypdf"], default="auto")
    ap.add_argument("--min-chars", type=int, default=40, help="avg chars/page below which there is no text layer")
    a = ap.parse_args(argv)

    pdf = Path(a.pdf)
    if not pdf.is_file():
        print(f"not a file: {pdf}", file=sys.stderr)
        return 1
    reader = PdfReader(str(pdf))
    if reader.is_encrypted:
        try:
            reader.decrypt("")
        except Exception:
            print("encrypted PDF: cannot read it", file=sys.stderr)
            return 2
    n_pages = len(reader.pages)  # loads the page tree; outline destinations resolve only after this
    source = pdf.as_posix()
    entries = flatten_outline(reader)

    if a.outline:
        print_outline(pdf, n_pages, entries, a.depth)
        return 0

    if a.split:
        chapters = parse_split(a.split, n_pages)
        how = "--split, page ranges given by hand"
    else:
        chapters = chapters_from_outline(entries, a.depth, n_pages)
        how = f"the PDF outline at depth {a.depth}"
        if not chapters:
            if a.all:
                chapters = [Chapter(1, pdf.stem, 0, n_pages - 1)]
                how = "no outline: the whole PDF as one chapter"
            else:
                print(
                    "no outline in this PDF: run --outline, read the table-of-contents pages,"
                    ' and pass --split "Title=first-last; ..."',
                    file=sys.stderr,
                )
                return 3
    full_list = chapters
    if a.chapters:
        wanted = parse_numbers(a.chapters, [c.number for c in chapters])
        chapters = [c for c in chapters if c.number in wanted]

    label = pdftotext_label() if a.engine in ("auto", "pdftotext") else None
    if a.engine == "pdftotext" and not label:
        print("pdftotext is not on PATH; use --engine pypdf", file=sys.stderr)
        return 1
    use_pdftotext = bool(label)
    try:
        from importlib.metadata import version as _v

        engine = label if use_pdftotext else f"pypdf {_v('pypdf')}"
    except Exception:  # pragma: no cover
        engine = label or "pypdf"

    out_dir = Path(a.out) / slugify(pdf.stem, 80)
    out_dir.mkdir(parents=True, exist_ok=True)
    write_outline(out_dir, source, n_pages, full_list, how)

    THIN = 200  # chars per page: written, but flagged — a preface, a plates section, a page of figures
    written, empty, thin = [], [], []
    for ch in chapters:
        pages = pages_pdftotext(pdf, ch.start, ch.end) if use_pdftotext else pages_pypdf(reader, ch.start, ch.end)
        avg = sum(len(p.strip()) for p in pages) / max(1, len(pages))
        if avg < a.min_chars:
            empty.append((ch, avg))
            continue
        if avg < THIN:
            thin.append((ch, avg))
        written.append(write_chapter(out_dir, source, ch, pages, engine))

    print(f"{pdf.name}: {n_pages} pages, {engine}, extracts in {out_dir.as_posix()}/")
    for path in written:
        print(f"  wrote {path.name}")
    for ch, avg in thin:
        print(f"  thin: {ch.number}. {ch.title} (p. {ch.pages}) — {avg:.0f} chars/page; written, check it is prose", file=sys.stderr)
    for ch, avg in empty:
        print(f"  not written: {ch.number}. {ch.title} (p. {ch.pages}) — {avg:.0f} chars/page, no text layer", file=sys.stderr)
    if not written:
        print("nothing written: no text layer in what was asked for — a scanned PDF. Report it as unreadable.", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
