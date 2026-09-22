---
name: data-curator-custom-calculations
description: >
  Load this skill whenever you need to author, modify, review or debug a KaxaNuk Data Curator custom calculation,
  meaning any `c_*` feature function that becomes an output column.
  Use it when the user asks to add a custom calculation, computed column, custom indicator, feature or financial
  metric; when they mention `custom_calculations.py`, `custom_calculation_modules`, `Output_Columns`, `DataColumn`,
  or column tags like `m_*`, `f_*`, `fbs_*`, `fcf_*`, `fis_*`, `d_*`, `s_*`, `c_*`; or when they want to compute a
  ratio, moving average, momentum, volatility, returns or signal from curated market or fundamental data.
  It covers naming, valid input columns, the DataColumn API, composition, and how to wire the column into the
  output, for both configuration-file projects and programmatic or notebook runs of `main()`.
metadata:
  version: 0.3.1
---

# Data Curator Custom Calculations

A custom calculation is a plain Python function whose name starts with `c_`.
The Data Curator turns each such function into one output column with the exact same name as the function, and
injects each of the function's parameters with the data of the column named after that parameter.

Work in English: function names, parameters, docstrings and comments in the generated code are all English,
matching the Data Curator codebase.

## 1. Detect the loading and selection surface

Two things vary by project, and nothing else in this skill does: **where the calculation functions come from**,
and **where the output columns are selected**. Both are just arguments to `kaxanuk.data_curator.main()` —
`custom_calculation_modules` and `configuration.columns` — so identify how the project supplies them before
writing anything. Look for an entry script (usually `__main__.py` at the project root), a notebook, or any
other caller of `main()`, and match it to one of these surfaces:

**(a) Configuration file + modules on disk.** The stock entry script imports `Config/custom_calculations.py`
if it exists, and builds the `Configuration` from `Config/data_curator_parameters.xlsx` through
`ExcelConfigurator`. Add new functions to that module. Some projects replace it with their own multi-file
layout, for example a package of category subfolders scanned into a list of modules; if so **follow the layout
that is already there** — read that project's loader to see which files it picks up and which it skips, and
read a sibling module to copy its shape.

**(b) Programmatic `main()` with modules on disk.** The caller builds the `Configuration` in Python and imports
its calculation modules normally. Files as in (a), selection as in (c).

**(c) Programmatic `main()` with in-memory modules.** Typical of a self-contained experiment notebook: the
`c_*` functions are defined in a cell, attached to a module object built at run time, and the `Configuration`
is constructed inline. No files, no workbook. See `references/programmatic-run.md`.

Discovery does not care which of these it is: a column is resolved to a function by **attribute name** on each
object in `custom_calculation_modules`, first match wins, with no check on where the function was defined.
Writing the function into a file is a project convention, not a library requirement.

**In a KaxaNuk Strategy Template repository the surface is (b), and the files are fixed.** The
functions go in `Data/Curator/custom_calculations.py`. `Data/curator.py`, the step-3 driver, loads
that file and passes the output columns to `main()` as `Configuration.columns`; in the worked
example's driver they are the `OUTPUT_COLUMNS` tuple. Never create `Config/custom_calculations.py`
there. The template ships both, as descriptions of what belongs in them, to be filled in. When
they are missing — a strategy made before template 0.11.0 — ask the owner to restore them from the
template, never from the example, with the `init-strategy` skill's script run in the strategy's
root; `--only Data` restores the whole folder, and one file comes by its own path:

```bash
uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" \
  strategy . --only Data
```

Two kinds of column are not `c_*` columns, even when asked for as a "signal": one that compares
securities on a date (a rank, a breadth reading), and one with a setting an experiment will sweep
(a fitted model, or a window such as the 50- and 200-day averages the example builds as
`r_trend_50_200`). Both are `r_*` columns in `Data/Refinery/custom_calculations.py`, which the
worked example's `Data/refinery.py` computes and this skill does not cover; the template's `Data/`
holds both files. Only their frozen arithmetic inputs are `c_*` columns.

Anywhere else, if a project has no surface yet, default to (a): create
`Config/custom_calculations.py` and confirm the entry script imports it.

## 2. Reuse before writing

Never duplicate an existing column.

- List the built-ins in the installed package's `kaxanuk/data_curator/features/calculations.py`
  (every `def c_*`), and the reusable helpers in `kaxanuk/data_curator/features/helpers.py`.
- List the project's existing custom `c_*` functions in the layout found in step 1.
- Show the user the relevant matches. If one already computes what they want, stop and point them to it.
  If one computes part of it, depend on it by parameter name instead of recomputing it.

Custom modules are searched **before** the built-ins, so a custom function whose name matches a built-in
silently overrides it for the whole run. Only do that deliberately, and tell the user.

## 3. Interrogate before generating

Ask **one question at a time**, and prefer concrete multiple-choice questions.
Do not write code until the inputs and the output name are settled. Resolve at least:

- The financial concept, in plain words, and its formula.
- Price adjustment: raw (`m_close`), split-adjusted (`m_close_split_adjusted`), or dividend-and-split-adjusted
  (`m_close_dividend_and_split_adjusted`). This changes the result; never pick it silently.
- Window and horizon (`5d` / `21d` / `63d` / `252d`, rolling vs exponential) if the concept has one.
- For fundamentals: whether the configured `period` is `annual` or `quarterly`, since the same function yields
  different values for each, and last-twelve-months logic only makes sense for `quarterly`.
- Edge handling: what the leading rows should be before the window fills (`None`), and what a zero denominator
  or a missing input should produce (`None`).

## 4. Write the function

- Read `references/conventions.md` for the naming rules and the full contract of a calculation function.
- Read `references/input-columns.md` to resolve every parameter name to a real column, and to enumerate the
  valid names from the installed package rather than guessing them.
- Read `references/data-column-api.md` for the `DataColumn` operations, and the shift-and-pad pattern.
- Start from `references/template.py`.
- Follow the project's Python style instructions if it has any (KaxaNuk projects normally apply the PEP 8 and
  Bloom Code instructions); otherwise match the surrounding module or cell.

## 5. Select the column in the output

Defining the function is not enough: the column has to be selected, or it is never computed. The output table
contains exactly the selected columns, in the order they were given. Columns used only as intermediate steps
are resolved as dependencies and need not be selected.

- Surface (a): add the exact function name, `c_` prefix included, to the `Output_Columns` sheet of
  `Config/data_curator_parameters.xlsx`. If you cannot edit the workbook, tell the user the exact string to add.
- Surfaces (b) and (c): add the name to the `columns` tuple of the `Configuration` passed to `main()`.
- A KaxaNuk Strategy Template repository: add the name to the output columns `Data/curator.py`
  requests (`OUTPUT_COLUMNS` in the example). Widening them changes every file's header, so the
  next run of the driver refetches every identifier. Say so before adding the column.
- Projects with their own configuration surface (a column picker, a settings service, an API): follow theirs.

`m_date` is not added automatically — include it in the selection whenever the output needs a date, and always
when using `InMemoryOutput.export_dataframe()`, which indexes by it and raises without it.

## 6. Validate

Run every check, and fix until all pass:

- [ ] The function name starts with `c_` and is a valid Python identifier in `snake_case`.
- [ ] The function is reachable: for surfaces (a) and (b), the file is in a location the project's loader
      actually picks up (mind loaders that skip files whose name starts with `_`); for surface (c), the
      function object is attached to one of the modules in `custom_calculation_modules`, under exactly its own
      name.
- [ ] The column name is in `Configuration.columns`, or is a dependency of a column that is.
- [ ] Every parameter name is an existing column: a real entity field with its prefix, a built-in `c_*`,
      another custom `c_*`, or the special `configuration` parameter. A wrong name fails at run time with
      `ColumnBuilderUnavailableEntityFieldError` or `ColumnBuilderCustomFunctionNotFoundError`.
- [ ] No dependency cycle among the `c_*` functions (the builder raises
      `ColumnBuilderCircularDependenciesError`).
- [ ] The return value is an iterable of the **same length** as the inputs; shifted results are padded with
      `None` on the leading positions.
- [ ] No `inf` or `NaN` leaks into the output; they must be `None`.
- [ ] The code parses: `python -m py_compile <file>` for a file, or a clean run of the cell for a notebook,
      and the linter the project uses passes.
- [ ] If the calculation depends, directly or transitively, on any `f_*`, `fbs_*`, `fcf_*`, `fis_*`, `d_*` or
      `s_*` column, the run needs a provider for the fundamentals, dividends or splits block in
      `data_block_providers`, and for the fundamental blocks the result also depends on the
      configured `period`.

## 7. Report

Tell the user: the new column name, its direct and transitive dependencies, whether it requires a fundamental
data provider and which `period` it assumes, how many leading rows come out `None`, and the exact step they
must take to select the column on their surface.

## References

- `references/conventions.md` — naming rules and the calculation function contract.
- `references/input-columns.md` — the column tags and how to enumerate the valid ones.
- `references/data-column-api.md` — the `DataColumn` API and the common patterns.
- `references/programmatic-run.md` — running `main()` without configuration files, and in-memory calculation
  modules for notebooks.
- `references/template.py` — skeleton to copy, with worked examples.