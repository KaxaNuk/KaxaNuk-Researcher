"""
Regenerate what the worked example generates -- the `experiment-lifecycle` references and the
template's files -- or check that they match.

The worked example -- `examples/liquid-golden-cross/` -- is the source of truth for two sets of
files.  The four experiment documents and the experiment notebook that `experiment-lifecycle` ships
as copyable references: a skill that carried its own version of those files drifted from the
template once already.  And every file inside the folders of `templates/strategy/` -- the drivers,
the shared modules, the notebooks, Experiment 1's documents, the paper-trading files -- which a new
strategy used to bring across from the example one by one and strip by hand.  Both sets are
regenerated from the example rather than edited by hand, and `tools/check_repo.py` fails when they
differ.

Run from the repository root after changing the example:

    uv run --no-project python tools/sync_investment_lab_references.py
    uv run --no-project python tools/sync_investment_lab_references.py --check

Only the files that differ are written, so a run on an unchanged example leaves no change.  A
missing example file stops the run with its name, before anything is written.

The example works one strategy through the process, and keeps that strategy's own lines between
whole-line markers -- `<!-- example: begin -->` and `<!-- example: end -->` in Markdown,
`# --- example: begin ---` and `# --- example: end ---` in Python, and `# EXAMPLE-ONLY CELL` at the
top of a notebook cell -- so they are stripped before anything is written: what is generated is the
template's description, never another strategy's content.  A Python file of the example keeps its
code inside the block, so its template copy is the module docstring.  The four reference documents
then have `_1` rewritten to `_N` so they read as templates for any experiment; the template's own
copies keep `_1`, because they sit in `Experiments/Experiment_1/`.  Notebooks keep their names.
"""

import argparse
import functools
import json
import pathlib
import re
import sys

REPOSITORY_ROOT = pathlib.Path(__file__).resolve().parent.parent
REFERENCES_DIRECTORY = ".apm/skills/experiment-lifecycle/references"
EXPERIMENT_DIRECTORY = "examples/liquid-golden-cross/Experiments/Experiment_1"
EXAMPLE_DIRECTORY = "examples/liquid-golden-cross"
TEMPLATE_DIRECTORY = "templates/strategy"
# The files the template ships as generated from the example: every file inside the folders that
# its README's *What is in here* table names.  Each lands at the same path under the template with
# the worked strategy's own lines removed, so what is outside the markers is the template's.
TEMPLATE_FILES = (
    "Data/Curator/custom_calculations.py",
    "Data/Refinery/custom_calculations.py",
    "Data/analyzer.ipynb",
    "Data/curator.py",
    "Data/refinery.py",
    "Experiments/Experiment_1/BLUEPRINT_1.md",
    "Experiments/Experiment_1/BRAINSTORMING_1.md",
    "Experiments/Experiment_1/FINDINGS_1.md",
    "Experiments/Experiment_1/JOURNAL_1.md",
    "Experiments/Experiment_1/experiment_1.ipynb",
    "Experiments/attribution_analysis.py",
    "Experiments/backtest_engine.py",
    "Experiments/portfolio_construction.py",
    "Experiments/securities_panel.py",
    "Paper_Trading/BITACORA.md",
    "Paper_Trading/Paper_Trading_1/paper_trading_1.py",
    "Paper_Trading/daily_update.py",
    "Universe/universe.ipynb",
)

# Example file -> reference file.  The documents are renamed from `_1` to `_N`; the notebook keeps
# its content and takes the name the skill refers to.
DOCUMENTS = {
    "BLUEPRINT_1.md": "blueprint-template.md",
    "BRAINSTORMING_1.md": "brainstorming-template.md",
    "JOURNAL_1.md": "journal-template.md",
    "FINDINGS_1.md": "findings-template.md",
}
NOTEBOOK = {
    "experiment_1.ipynb": "experiment-notebook.ipynb",
}
RENAMES = (
    (
        re.compile(r"_1\.md\b"),
        "_N.md",
    ),
    (
        re.compile(r"^# (Blueprint|Brainstorming|Journal|Findings) — Experiment 1", re.MULTILINE),
        r"# \1 — Experiment N",
    ),
    (
        re.compile(r"^## Experiment 1 — .*$", re.MULTILINE),
        "## Experiment N — <the idea, in five words>",
    ),
)
# The worked strategy's own lines sit between markers that count only as whole lines at column 0:
# `JOURNAL_1.md` quotes both markers inside a sentence, and a match that started or stopped there
# would cut the file in the wrong place.  Markdown and Python each have their pair; a notebook marks
# whole cells instead.  `tools/check_repo.py` reads these markers and checks that they stand alone
# at column 0 and open and close in order.
EXAMPLE_MARKERS = {
    ".md": (
        "<!-- example: begin -->",
        "<!-- example: end -->",
    ),
    ".py": (
        "# --- example: begin ---",
        "# --- example: end ---",
    ),
}
# One pattern per pair: the block, with the runs of newlines on both sides of it captured, so the
# replacement can keep the longer run.  Blocks separated only by blank lines are removed as one
# match, so the seam sees only the outer runs and the gap between them is not counted twice.  A
# suffix not here has no line markers: a notebook marks whole cells, and any other file is copied
# whole.
EXAMPLE_BLOCKS = {
    suffix: re.compile(
        "".join([
            r"(\n*)^",
            re.escape(begin),
            r"$.*?^",
            re.escape(end),
            r"$(?:\n*^",
            re.escape(begin),
            r"$.*?^",
            re.escape(end),
            r"$)*(\n*)",
        ]),
        re.MULTILINE
        | re.DOTALL,
    )
    for suffix, (begin, end)
    in EXAMPLE_MARKERS.items()
}
MARKDOWN_EXAMPLE_BLOCK = EXAMPLE_BLOCKS[".md"]
PYTHON_EXAMPLE_BLOCK = EXAMPLE_BLOCKS[".py"]
EXAMPLE_ONLY_CELL = "# EXAMPLE-ONLY CELL"


def expected_references(
    root: pathlib.Path,
) -> dict[str, str]:
    """Every reference file's name, and the text the worked example says it should hold."""
    experiment_directory = root / EXPERIMENT_DIRECTORY
    documents = {
        reference_name: rename_experiment(
            strip_example_content(
                read_example_text(experiment_directory / example_name),
            ),
        )
        for example_name, reference_name
        in DOCUMENTS.items()
    }
    notebooks = {
        reference_name: strip_example_cells(
            read_example_text(experiment_directory / example_name),
        )
        for example_name, reference_name
        in NOTEBOOK.items()
    }
    references = {
        **documents,
        **notebooks,
    }

    return references


def expected_template_files(
    root: pathlib.Path,
) -> dict[str, str]:
    """Every generated template file's path, and the text the worked example says it should hold."""
    example_directory = root / EXAMPLE_DIRECTORY
    files = {
        relative_path: template_part(
            read_example_text(example_directory / relative_path),
            pathlib.PurePosixPath(relative_path).suffix,
        )
        for relative_path
        in TEMPLATE_FILES
    }

    return files


def main() -> int:
    """Parse the command line, then write the references and the template's files, or check them."""
    parser = argparse.ArgumentParser(
        description="Regenerate the experiment-lifecycle references and the template's files from the worked example.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="write nothing; exit 1 when a reference or a template file differs from what the example says",
    )
    arguments = parser.parse_args()
    stale_reference_names = stale_references(REPOSITORY_ROOT)
    stale_template_paths = stale_template_files(REPOSITORY_ROOT)

    if arguments.check:
        for reference_name in stale_reference_names:
            print(f"  stale  {REFERENCES_DIRECTORY}/{reference_name}")
        for relative_path in stale_template_paths:
            print(f"  stale  {TEMPLATE_DIRECTORY}/{relative_path}")
        exit_code = 1 if stale_reference_names or stale_template_paths else 0

        return exit_code

    if not stale_reference_names and not stale_template_paths:
        print("references and template files already match the example")

        return 0

    references_directory = REPOSITORY_ROOT / REFERENCES_DIRECTORY
    references_directory.mkdir(
        parents=True,
        exist_ok=True,
    )
    references = expected_references(REPOSITORY_ROOT)
    for reference_name in stale_reference_names:
        (references_directory / reference_name).write_text(
            references[reference_name],
            encoding="utf-8",
            newline="\n",
        )
        print(f"  {REFERENCES_DIRECTORY}/{reference_name}")

    template_directory = REPOSITORY_ROOT / TEMPLATE_DIRECTORY
    template_files = expected_template_files(REPOSITORY_ROOT)
    for relative_path in stale_template_paths:
        target = template_directory / relative_path
        target.parent.mkdir(
            parents=True,
            exist_ok=True,
        )
        target.write_text(
            template_files[relative_path],
            encoding="utf-8",
            newline="\n",
        )
        print(f"  {TEMPLATE_DIRECTORY}/{relative_path}")

    print(f"regenerated from {EXAMPLE_DIRECTORY}")

    return 0


def read_cell_source(
    cell: dict[str, object],
) -> str:
    """A notebook cell's source as one string; the format allows a string or a list of lines."""
    source = cell["source"]

    if isinstance(source, list):

        return "".join(source)

    return source


def read_example_text(
    path: pathlib.Path,
) -> str:
    """A worked-example file's text with line endings made LF; a missing one stops the sync."""
    if not path.is_file():
        message = f"{path} is missing; the worked example is the source of what is generated"

        raise FileNotFoundError(message)

    text = read_text(path)

    return text


def read_text(
    path: pathlib.Path,
) -> str:
    """A file's text with line endings made LF, or an empty text when it does not exist."""
    if not path.is_file():

        return ""

    raw = path.read_text(encoding="utf-8")
    text = raw.replace("\r\n", "\n")

    return text


def rename_experiment(
    text: str,
) -> str:
    """Turn the example's Experiment 1 document into a document for any Experiment N."""
    renamed = functools.reduce(
        _apply_rename,
        RENAMES,
        text,
    )

    return renamed


def stale_references(
    root: pathlib.Path,
) -> list[str]:
    """The reference files that differ from what the worked example says, by name."""
    references_directory = root / REFERENCES_DIRECTORY
    stale = [
        reference_name
        for reference_name, text
        in expected_references(root).items()
        if read_text(references_directory / reference_name) != text
    ]

    return stale


def stale_template_files(
    root: pathlib.Path,
) -> list[str]:
    """The template files that differ from what the worked example says, by path."""
    template_directory = root / TEMPLATE_DIRECTORY
    stale = [
        relative_path
        for relative_path, text
        in expected_template_files(root).items()
        if read_text(template_directory / relative_path) != text
    ]

    return stale


def strip_example_cells(
    text: str,
) -> str:
    """
    Remove the worked strategy's cells from a notebook, and its lines from the cells that stay.

    A notebook with nothing to strip is returned exactly as it was read, so regenerating it from an
    unchanged example leaves no diff.
    """
    notebook = json.loads(text)
    original_cells = notebook["cells"]
    kept_cells = [
        cell
        for cell in original_cells
        if not _is_example_only_cell(cell)
    ]
    rewritten = [
        _strip_cell(cell)
        for cell in kept_cells
    ]
    cells_dropped = len(kept_cells) != len(original_cells)
    cells_rewritten = any(rewritten)
    changed = cells_dropped or cells_rewritten

    if not changed:

        return text

    notebook["cells"] = kept_cells
    # nbformat's own form -- keys sorted, one space of indent, a final newline -- so stripping the
    # outputs of a notebook copied from the reference changes nothing.
    serialized = json.dumps(
        notebook,
        indent=1,
        sort_keys=True,
        ensure_ascii=False,
    )

    return f"{serialized}\n"


def strip_example_content(
    text: str,
    block: re.Pattern[str] = MARKDOWN_EXAMPLE_BLOCK,
) -> str:
    """
    Remove the worked strategy's own lines from a text.

    The blocks are Markdown's unless another pattern is given.  A removed block gives way to the
    longer of the blank runs that surrounded it — one blank line in prose stays one, two blank lines
    between definitions stay two — and a block that closed the file leaves it ending as it did.
    Only when something was removed: a text with no markers comes back untouched.  The text's line
    endings are LF, as `read_text` leaves them; a marker before a carriage return is not matched.
    """
    stripped, removed_blocks = block.subn(
        _seam,
        text,
    )

    if removed_blocks == 0:

        return text

    trimmed = stripped.rstrip("\n")

    if text.endswith("\n"):

        return f"{trimmed}\n"

    return trimmed


def template_part(
    text: str,
    suffix: str,
) -> str:
    """
    The template's part of one example file: its text with the worked strategy's own lines removed.

    A notebook loses its example-only cells and the example lines of the cells that stay; a Markdown
    or Python file loses its example blocks; any other file is the template's whole.
    """
    if suffix == ".ipynb":

        return strip_example_cells(text)

    block = EXAMPLE_BLOCKS.get(suffix)

    if block is None:

        return text

    stripped = strip_example_content(
        text,
        block,
    )

    return stripped


def write_cell_source(
    cell: dict[str, object],
    source: str,
) -> None:
    """Put a source back in the form the cell already used, a string or a list of lines."""
    if isinstance(cell["source"], list):
        cell["source"] = source.splitlines(keepends=True)
    else:
        cell["source"] = source


def _apply_rename(
    text: str,
    rename: tuple[re.Pattern[str], str],
) -> str:
    """One step of the `_1` to `_N` rewrite, shaped for `functools.reduce`."""
    pattern, replacement = rename
    renamed = pattern.sub(
        replacement,
        text,
    )

    return renamed


def _is_example_only_cell(
    cell: dict[str, object],
) -> bool:
    """Whether a cell is the worked strategy's alone, marked on its first line."""
    source = read_cell_source(cell)
    example_only = source.startswith(EXAMPLE_ONLY_CELL)

    return example_only


def _seam(
    match: re.Match[str],
) -> str:
    """
    What replaces a removed block: the longer of the newline runs on either side of it.

    Both runs hold only newlines, so runs of equal length are equal strings and a tie needs no rule.
    """
    longer = max(
        match.group(1),
        match.group(2),
        key=len,
    )

    return longer


def _strip_cell(
    cell: dict[str, object],
) -> bool:
    """Strip a kept cell's example lines in place, and say whether anything was removed."""
    source = read_cell_source(cell)
    stripped_source = strip_example_content(source)
    stripped = stripped_source != source

    if stripped:
        write_cell_source(
            cell,
            stripped_source.rstrip("\n"),
        )

    return stripped


if __name__ == "__main__":
    sys.exit(main())
