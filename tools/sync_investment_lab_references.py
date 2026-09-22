"""
Regenerate the `experiment-lifecycle` references from the worked example, or check that they match.

The worked example -- `examples/liquid-golden-cross/` -- is the source of truth for the four
experiment documents and the experiment notebook that `experiment-lifecycle` ships as copyable
references.  A skill that carried its own version of those files drifted from the template once
already, so the copies are regenerated from the example rather than edited by hand, and
`tools/check_repo.py` fails when they differ.

Run from the repository root after changing the example's experiment documents:

    uv run --no-project python tools/sync_investment_lab_references.py
    uv run --no-project python tools/sync_investment_lab_references.py --check

Only the references that differ are written, so a run on an unchanged example leaves no change.
A missing example document stops the run with its name, before anything is written.

The example works one strategy through the process, and keeps that strategy's own lines between
whole-line markers -- `<!-- example: begin -->` and `<!-- example: end -->` in Markdown, and
`# EXAMPLE-ONLY CELL` at the top of a notebook cell -- so they are stripped before anything is
written: a reference is the template's description, never another strategy's content.  The four
documents then have `_1` rewritten to `_N` so they read as templates for any experiment; the
notebook keeps its name inside, because a new experiment copies and renames it.
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
# A marker counts only as a whole line: `JOURNAL_1.md` quotes both markers inside a sentence, and a
# match that started or stopped there would cut the file in the wrong place.
EXAMPLE_BLOCK = re.compile(
    r"^<!-- example: begin -->$.*?^<!-- example: end -->$\n?",
    re.MULTILINE
    | re.DOTALL,
)
EXAMPLE_ONLY_CELL = "# EXAMPLE-ONLY CELL"
EXTRA_BLANK_LINES = re.compile(r"\n{3,}")


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


def main() -> int:
    """Parse the command line, then write the references or check them."""
    parser = argparse.ArgumentParser(
        description="Regenerate the experiment-lifecycle references from the worked example.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="write nothing; exit 1 when a reference differs from what the example says",
    )
    arguments = parser.parse_args()
    stale = stale_references(REPOSITORY_ROOT)

    if arguments.check:
        for reference_name in stale:
            print(f"  stale  {reference_name}")
        exit_code = 1 if stale else 0

        return exit_code

    if not stale:
        print("references already match the example")

        return 0

    references_directory = REPOSITORY_ROOT / REFERENCES_DIRECTORY
    references_directory.mkdir(
        parents=True,
        exist_ok=True,
    )
    references = expected_references(REPOSITORY_ROOT)
    for reference_name in stale:
        (references_directory / reference_name).write_text(
            references[reference_name],
            encoding="utf-8",
            newline="\n",
        )
        print(f"  {reference_name}")
    print(f"references regenerated from {EXPERIMENT_DIRECTORY}")

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
        message = f"{path} is missing; the worked example is the source of the references"

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
) -> str:
    """
    Remove the worked strategy's own lines from a Markdown text.

    A removed block leaves the blank lines on both sides of it, so runs of blank lines collapse to
    one, and a block that closed the file leaves it ending as it did — only when something was
    removed, so a text with no markers comes back untouched.
    """
    stripped, removed_blocks = EXAMPLE_BLOCK.subn(
        "",
        text,
    )

    if removed_blocks == 0:

        return text

    collapsed = EXTRA_BLANK_LINES.sub(
        "\n\n",
        stripped,
    )
    trimmed = collapsed.rstrip("\n")

    if text.endswith("\n"):

        return f"{trimmed}\n"

    return trimmed


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
