---
name: data-curator-custom-calculations
description: >
  Load this skill whenever you need to author, modify, review or debug a KaxaNuk Data Curator custom
  calculation, meaning any `c_*` feature function that becomes an output column. Use it when the
  user asks to install or upgrade the Data Curator, or run `Data/curator.py`; to add a custom
  calculation, computed column, custom indicator, feature or financial metric; when they mention
  `custom_calculations.py`, `custom_calculation_modules`, `Output_Columns`, `DataColumn`, or column
  tags like `m_*`, `f_*`, `fbs_*`, `fcf_*`, `fis_*`, `d_*`, `s_*`, `c_*`; or when they want to
  compute a ratio, moving average, momentum, volatility, returns or signal from curated market or
  fundamental data; or when a downloaded value looks wrong, before it is reported as a bug. It
  covers the library and its upgrade, naming, valid input columns, the DataColumn API,
  composition, wiring the column into the output, for configuration files and runs of `main()`,
  and whether a wrong value is the provider's or the library's.
metadata:
  version: 0.5.0
  library_version: 0.50.0
---

# Data Curator Custom Calculations

A custom calculation is a plain Python function whose name starts with `c_`. The Data Curator
turns each such function into one output column with the exact same name as the function, and
injects each of the function's parameters with the data of the column named after that parameter.

This skill was checked against Data Curator **0.50.0**, the frontmatter's `library_version`:
compare it with the build `uv pip list` shows, and on a newer minor or major version treat every
trap here as unproven until it is checked again.

**What this skill knows comes from the documentation, the changelog and runs — never from the
library's code.** The Curator is open source, but the rule is the same for every KaxaNuk tool:
never open, search, print or inspect its installed files, nor a source page its documentation
links to. What neither the documentation nor a run says is not known; a run settles it. An error
is reported by the call, its type and its message, never by the library's own traceback lines.

## The library

Open source, on PyPI as `kaxanuk-data-curator`, with no Lab licence: a KaxaNuk strategy's `uv sync`
installs it, and `Data/curator.py`, written from its docstring, is the strategy's one caller of
`main()`, run as `uv run python Data/curator.py`, with `--end-date` for the paper-trading refresh.
Its documentation is <https://kaxanuk-data-curator.readthedocs.io/en/stable/>, whose `stable` pages
follow the newest release, with the changelog among its release notes.

**Upgrade it between experiments, never during one**: a new build can change what is downloaded.
`uv lock --upgrade-package kaxanuk-data-curator`, then `uv sync --group notebook --inexact`, which
keeps a hand-installed engine; a line in `JOURNAL_1.md` naming both builds; `uv.lock` committed
with a `CHANGELOG.md` entry. A book on paper stops with `unfrozen-input` on any Curator but the one
it was frozen with: where a book is frozen, say so and wait for the owner's go before upgrading.

## 1. Detect the loading and selection surface

Two things vary by project, and nothing else in this skill does: **where the calculation functions
come from**, and **where the output columns are selected**. Both are just arguments to
`kaxanuk.data_curator.main()` — `custom_calculation_modules` and `configuration.columns` — so
identify how the project supplies them before writing anything. Look for an entry script (usually
`__main__.py` at the project root, which `kaxanuk.data_curator init excel` writes, as the README
says), a notebook, or any other caller of `main()`, and match it to one of these surfaces:

**(a) Configuration file + modules on disk.** `kaxanuk.data_curator init excel` writes the entry
script, `Config/data_curator_parameters.xlsx` and `Config/custom_calculations.py`; the entry script
reads the workbook and loads that module, as the README's *Customization* and the documentation's
Custom Calculator Workflow page say. Add new functions to that module. Some projects replace it
with their own multi-file layout, for example a package of category subfolders scanned into a list
of modules; if so **follow the layout that is already there** — read that project's loader to see
which files it picks up and which it skips, and read a sibling module to copy its shape.

**(b) Programmatic `main()` with modules on disk.** The caller builds the `Configuration` in Python
and imports its calculation modules normally, as the documentation's Component Integrator Workflow
page describes. Files as in (a), selection as in (c).

**(c) Programmatic `main()` with in-memory modules — not checked by a run.** A self-contained
experiment notebook could define its `c_*` functions in a cell, attach them to a module object
built at run time, and construct the `Configuration` inline: no files, no workbook. Neither the
documentation nor a recorded run shows it working, so run it once in a scratch copy before an
experiment relies on it. See `references/programmatic-run.md`.

The documentation and the worked example's run show this much: a `c_` function in a module passed
in `custom_calculation_modules` becomes the column of its name, and a module loaded from its file
by path, under a name of the caller's own, works, as the worked example's `Data/curator.py` loads
its own.

**In a KaxaNuk Strategy Template repository the surface is (b), and the files are fixed.** The
functions go in `Data/Curator/custom_calculations.py`. `Data/curator.py`, the step-3 driver, loads
that file and passes the output columns to `main()` as `Configuration.columns`; in the worked
example's driver they are the `OUTPUT_COLUMNS` tuple. The identifiers are the seed's
`main_identifier`, chosen per experiment with its provider; FMP in the worked example is that
experiment's choice. Never create `Config/custom_calculations.py` there. The template ships both
as descriptions — a docstring each — to be filled in. In a strategy made from a template before
0.10.0 they are missing: they come back from the template, never from the example, through
`init-strategy`'s script run from the strategy's root —
`scaffold.py strategy . --only Data/curator.py` and `--only Data/Curator/custom_calculations.py`,
which never overwrite. Two kinds of column are not `c_*` columns, even when asked for as a
"signal": one that compares securities on a date (a rank, a breadth reading), and one with a
setting an experiment will sweep (a fitted model, or a window such as the 50- and 200-day averages
the example builds as `r_trend_50_200`). Both are `r_*` columns in
`Data/Refinery/custom_calculations.py`, which the worked example's `Data/refinery.py` computes
and this skill does not cover. Only their frozen arithmetic inputs are `c_*` columns.

Anywhere else, if a project has no surface yet, default to (a): create
`Config/custom_calculations.py` and confirm the entry script imports it.

## 2. Reuse before writing

Never duplicate an existing column.

- List the built-ins on the documentation's Features page,
  <https://kaxanuk-data-curator.readthedocs.io/en/stable/api_reference/features.html>: one page per
  built-in, with the columns it reads, what it returns and its formula. The helpers to reuse are on
  the Helpers page, <https://kaxanuk-data-curator.readthedocs.io/en/stable/api_reference/helpers.html>.
- List the project's existing custom `c_*` functions in the layout found in step 1.
- Show the user the relevant matches. If one already computes what they want, stop and point them to
  it. If one computes part of it, depend on it by parameter name instead of recomputing it.

Never name a custom function after one on the Features page: which of the two a run would use is
not documented.

## 3. Interrogate before generating

Ask **one question at a time**, and prefer concrete multiple-choice questions.
Do not write code until the inputs and the output name are settled. Resolve at least:

- The financial concept, in plain words, and its formula.
- Price adjustment: raw (`m_close`), split-adjusted (`m_close_split_adjusted`), or
  dividend-and-split-adjusted (`m_close_dividend_and_split_adjusted`). This changes the result;
  never pick it silently.
- Window and horizon (`5d` / `21d` / `63d` / `252d`, rolling vs exponential) if the concept has one.
- For fundamentals: whether the configured `period` is `annual` or `quarterly`, since the same
  function yields different values for each, and last-twelve-months logic only makes sense for
  `quarterly`.
- Edge handling: what the leading rows should be before the window fills (`None`), and what a zero
  denominator or a missing input should produce (`None`).

## 4. Write the function

- Read `references/conventions.md` for the naming rules and the full contract of a calculation
  function.
- Read `references/input-columns.md` to resolve every parameter name to a real column, and to find
  the valid names on the documentation's lists rather than guessing them.
- Read `references/data-column-api.md` for the `DataColumn` operations, and the shift-and-pad
  pattern.
- Start from `references/template.py`.
- Follow the project's Python style. `template.py` is in a KaxaNuk strategy's, Bloom Code at 100
  columns, which `bloom-code-lint` checks; elsewhere, match the surrounding module or cell.
- Write in English — names, parameters, docstrings and comments — as the Data Curator's
  documentation is.

## 5. Select the column in the output

Defining the function is not enough: the column has to be selected, or it is never computed. The
output table contains exactly the selected columns, in the order they were given, as the worked
example's runs wrote them. Columns used only as intermediate steps are resolved as dependencies and
need not be selected.

- Surface (a): add the exact function name, `c_` prefix included, to the `Output_Columns` sheet of
  `Config/data_curator_parameters.xlsx`. The documentation's Custom Calculations page says the entry
  includes the prefix; its Features page says the opposite, and the worked example's run, through
  `Configuration.columns`, used the prefix. If you cannot edit the workbook, tell the user the exact
  string to add.
- Surfaces (b) and (c): add the name to the `columns` tuple of the `Configuration` passed to
  `main()`.
- A KaxaNuk Strategy Template repository: add the name to the output columns `Data/curator.py`
  requests (`OUTPUT_COLUMNS` in the example). Widening them changes every file's header, so the
  next run of the driver refetches every identifier. Say so before adding the column.
- Projects with their own configuration surface (a column picker, a settings service, an API):
  follow theirs.

Always select `m_date`: the worked example's runs did, and the documentation does not say it is
added for you.

## 6. Validate

Run every check, and fix until all pass:

- [ ] The function name starts with `c_` and is a valid Python identifier in `snake_case`.
- [ ] The function is reachable: for surfaces (a) and (b), the file is in a location the project's
      loader actually picks up (mind loaders that skip files whose name starts with `_`); for
      surface (c), the function is attached to one of the modules in
      `custom_calculation_modules`, a surface no run has checked yet.
- [ ] The column name is in `Configuration.columns`, or is a dependency of a column that is.
- [ ] Every parameter name is an existing column: a documented tag with its prefix, a built-in
      `c_*` from the Features page, another custom `c_*`, or the special `configuration`
      parameter. A wrong name stops the run with an error naming the column (the changelog, 0.12,
      improved those errors).
- [ ] No dependency cycle among the `c_*` functions: a cycle stops the run with an error.
- [ ] The return value is an iterable of the **same length** as the inputs; shifted results are
      padded with `None` on the leading positions.
- [ ] No `inf` or `NaN` leaks into the output; they must be `None`.
- [ ] A column built on volume or traded value — the built-in `c_daily_traded_value` and anything
      averaged or ranked on it — is checked for continuity at every split before anything reads
      it, as `universe-point-in-time`'s register says: a provider's unadjusted volume can already
      be in post-split shares before the split date, and the split adjustment then counts it twice.
- [ ] The code parses: `uv run --no-project python -m py_compile <file>` for a file, or a clean run
      of the cell for a notebook, and the linter the project uses passes.
- [ ] If the calculation depends, directly or transitively, on any `f_*`, `fbs_*`, `fcf_*`, `fis_*`,
      `d_*` or `s_*` column, the run needs a provider for the fundamentals, dividends or splits
      block in `data_block_providers`, and for the fundamental blocks the result also depends on the
      configured `period`.

## 7. Report

Tell the user: the new column name, its direct and transitive dependencies, whether it requires a
fundamental data provider and which `period` it assumes, how many leading rows come out `None`, and
the exact step they must take to select the column on their surface.

## When a value looks wrong — the provider's or the library's?

The Data Curator downloads what the data provider sends, adjusts it and computes from it. Most
wrong values a strategy meets are the provider's, and they go to the provider, never to the Data
Curator's issues. Before anyone reports a bug, tell them apart:

1. **Find the provider's raw value** — the unadjusted column the Curator wrote, `m_close`,
   `m_volume` or a fundamental field as delivered — for the security and the date in question.
2. **The raw value is already wrong** — a price, a volume or a field that cannot be true on that
   date, or that breaks with the security's own history, as the data-issues register's checks
   find it: it is the provider's data. Record it in `Universe/Data_Issues.csv` with its severity,
   as `universe-point-in-time` says, handle it there — exclude the name, or correct the value
   with its source named — and report it to the provider: the security, the date, the field,
   the value, and why it cannot be right. The library's maintainers cannot fix it.
3. **The raw value is right and the Curator's output is wrong** — a correct input adjusted or
   computed wrongly: it is the library's. Report it on
   <https://github.com/KaxaNuk/Data-Curator/issues>, with the Curator's version, the provider,
   the input and the output.

**Known provider faults** are register checks, so a run finds them on its own. FMP's unadjusted
volume before some 2025 splits is already in post-split shares — ORLY 15:1 on 2025-06-10, NOW
5:1 on 2025-12-18, TPL 3:1 on 2025-12-23 — so `m_volume_split_adjusted` and
`c_daily_traded_value` adjust it twice. The Data Curator's maintainers confirmed it is FMP's
data, <https://github.com/KaxaNuk/Data-Curator/issues/36>: it is reported to FMP. The
documentation's FMP page maps `m_volume_split_adjusted` straight to FMP's own split-adjusted
volume, so the second count is FMP's adjustment, not the Curator's.

## References

- `references/conventions.md` — naming rules and the calculation function contract.
- `references/input-columns.md` — the column tags, and the documentation's lists of valid ones.
- `references/data-column-api.md` — the `DataColumn` API and the common patterns.
- `references/programmatic-run.md` — running `main()` without configuration files, as the worked
  example does, and the in-memory modules no run has checked yet.
- `references/template.py` — skeleton to copy, with worked examples.
