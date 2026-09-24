---
name: paper-trading-gate
description: >
  Load this skill whenever a KaxaNuk Strategy Template repository asks whether an experiment
  graduates to paper trading, step 7 — `Paper_Trading/BITACORA.md`, `promote.py`, `daily_update.py`,
  `record.py` and `Paper_Trading_N/paper_trading_N.py`. Use it when the user asks what the
  graduation gate is, how each of its five criteria is evidenced, whether a `FINDINGS_N.md` clears
  it, how a graduated book is frozen, what the daily run does and where it writes, what is
  registered before day one, why the parameters are frozen, what a promoted experiment's folder is
  named, or what the gate's status section should hold. It covers the five criteria and the usual
  ways each fails, the freeze, the daily run, and what the assistant never decides. It does NOT
  cover the cycle that produces the findings (use `backtest-engine-runs`,
  `attribution-analysis-runs`, `alpha-decomposition`), the documents of an experiment (use
  `experiment-lifecycle`), or step 8, Production, which is outside the repository.
metadata:
  version: 0.2.0
---

# The paper-trading gate — what graduation means, and what has to be true first

**In plain words:** a dress rehearsal on data nobody has seen yet. **It produces** out-of-sample
evidence and an operations checklist. **It prevents** finding the plumbing problems on day one of
funding.

A backtest says what a rule *would* have done; paper trading says what it *does*, on live prices,
with live universe changes, and with the delistings and corporate actions a historical file has
already tidied up. `Paper_Trading/BITACORA.md` is **the gate, not a log** — a contract that says
what graduation means and what has to be true before it happens. It is named apart from
`JOURNAL_N.md` so the two are never confused. Step 8, Production, is not here: a strategy leaves
the repository when it is funded.

## When to Use

- The user asks whether Experiment N graduates, or what would have to be true for it to.
- The user is filling the gate's *Current status* section, or writing a `paper_trading_N.py`.
- A `FINDINGS_N.md` reports a book that beats its benchmarks and the question turns to what
  comes next.
- The KaxaNuk Researcher's `challenge` command reaches the gate: it reads `BITACORA.md` only when
  graduation is being claimed, and this skill is how the criteria are read.

## The gate: five criteria, all of them

Strong backtest results are necessary and **not sufficient**. Every criterion is evidenced from
the experiment's `FINDINGS_N.md` and from `RESULTS.md`; **if it cannot be evidenced from those,
it has not been met.**

| # | Criterion | Evidenced by | The usual way it fails |
| --- | --- | --- | --- |
| 1 | **Beats the benchmarks on risk-adjusted return** — every benchmark it reports against *and* its own control row, over the same window | the ranking table of `FINDINGS_N.md`, and the control `BLUEPRINT_N.md` names in its *Rules* — the same rule with one ingredient removed — on the rule's own rebalance dates | a pass on Sharpe alone while the control earns more a year on the same dates — the single-metric pass the criterion exists to catch; a control on its own dates, which differs in two things |
| 2 | **Attribution shows idiosyncratic alpha in both layers** — selection in the Brinson-Fachler cut, a residual the factor model cannot explain, and a selection story that survives the third pass on residual returns | the attribution section of `FINDINGS_N.md`, read with `alpha-decomposition` | the residual is there but random books of the same shape earn most of it; the third pass was never run. Expect *a pass with a qualification*: a book half factor, half idiosyncratic has passed and been told how much of it is not the idea |
| 3 | **Conclusions survive parameter perturbation, and the trial count is published beside the winner** | a sweep read as a curve; the count of variants and of features screened | every setting a single value, none read as a curve; a count nobody wrote down; a setting the blueprint listed as unable to rescue the experiment moved after the result and counted as an edit rather than a trial. Publishing the count is the minimum, and the sign-off says whether the deflated figure was also computed |
| 4 | **Costs and capacity are modelled and stated** — turnover, commission, and every assumption the engine does not model, borrow cost above all | the cost rows of `FINDINGS_N.md`, a realistic-commission row beside the frozen one | costs modelled, capacity not modelled at all; a long/short book with borrow cost in a footnote |
| 5 | **Explicit sign-off** | a person's name and date in `BITACORA.md` | sought before 1 to 4 are evidenced |

Criterion 2 is evaluable here because the stack has a real attribution stage; a repository without
one would have to name a substitute — a beta-matched control book, a regression on the market — and
here there is no substitute to name, which means there is also no excuse.

## The promotion

An experiment is **promoted, not copied.** `Paper_Trading/Paper_Trading_N/` mirrors the
`Experiment_N` it came from, so the lineage of a paper-traded book is never in question; the
experiment's notebook stays where it is, as the record of how the rule was chosen. The template
ships `Paper_Trading_1/` as the contract of a frozen book, named for the experiment it would
mirror: it becomes Experiment 1's book if Experiment 1 graduates, and a later experiment that
graduates takes its own number.

A strategy's first graduation is its `1.0.0`: the changelog reserves it for the first strategy that
reaches paper trading with its results reproduced from a clean clone.

## The freeze

A graduated book is the strategy, frozen. After the sign-off, the rule is written into
`Paper_Trading_N/paper_trading_N.py` from the experiment's cells and committed; then
`Paper_Trading/promote.py N`, on a clean tree, copies byte for byte from that commit every file the
book needs — the refinery and its calculations, the reader of the desk's files, the shared modules
the rule calls, the seed and the security master — into `Paper_Trading_N/` in the strategy's own
layout, and writes `FREEZE.json`: the commit, the freeze date, the hash of every file, the library
versions, and the hash of what it cannot copy, the Curator's calculations. Every module resolves its
paths from its own folder, so the copies read and write inside the book's folder: an experiment
under construction can change the shared modules and the book never moves. A frozen book is never
frozen again; a new freeze is a new book, with its own number.

## What a paper-trading run is

Not a notebook: `daily_update.py`, run on a schedule after the close, because the question is no
longer *what would this have done* but *what does it hold today, and how is it doing*. It refreshes
the shared raw prices once, or reads what another machine published; checks the newest day and
stops every book on a close with no fill price or a move no price can make; runs each book in
`BOOKS` — its frozen refinery, its frozen rule from the experiment's first day, and the engine
twice, over the whole history and since the freeze; writes the record through `record.py` to local
CSV files, a DuckDB database or both, as `Config/.env` says; and exits 0, 1 or 2 — clean, flagged,
failed. A shared input that no longer matches `FREEZE.json` stops the book with `unfrozen-input`.

The record has six tables — runs, books, performance, statistics, diagnostics, flags — keyed so a
second run of a day replaces that day's rows. A past value the engine now prices differently is a
**restatement**: flagged, never overwritten. The template ships these files as their contract in a
docstring; the worked example carries them working.

**A paper-trading script re-fits nothing.** A run that tunes anything is a backtest wearing a
costume, and it re-introduces exactly the search that produces negative out-of-sample performance.
And **months on paper cannot show skill**: the daily record is read for whether the book behaves
like its backtest — turnover, holdings, exposure, costs — never for a good month.

## Before a book's first day

`BITACORA.md` gets a section for the book, committed before its first run and never edited: the
experiment, variant, commit and freeze date; the gate row by row with the sign-off; the bands for
each diagnostic, from `FINDINGS_N.md`'s structural table and carried as `BANDS` in the book; the
kill switch; the review dates and the period to watch before production; and what the record
cannot show.

## The status section

*Current status* in `BITACORA.md` is the gate's record. Until something graduates it says so —
*nothing has graduated, nothing has been tested*. When a candidate arrives, record which
experiment, which variant, which criteria it clears and, above all, **which it does not and why:
the blocking items are the content of this section, not the passing ones.** The worked example's
verdict table, criterion by criterion with its evidence, is the shape to follow.

## What the assistant never does here

- **Declare graduation.** Criterion 5 is a person's signature; the assistant lays the four others
  out, evidenced or not, and stops.
- **Compute a performance number**, a deflated Sharpe included. Every figure is quoted from
  `FINDINGS_N.md` or `RESULTS.md` with its source; a missing one is a re-run to ask for, never a
  value to supply.
- **Read a criterion as met on a number the findings do not carry.** Capacity not modelled is
  *not met*, not *probably fine*.
- **Re-fit, re-tune or widen a rule** in a paper-trading script, whatever the reason offered.
- **Freeze a book before the sign-off, or freeze one twice.**
- **Register the scheduled task.** It changes the machine: the command is given, the user runs it.
- **Read the record's figures back as its own.** They are the engine's, quoted with their file.
- **Touch step 8.** Nothing here deploys, executes or moves money.

## References

- `Paper_Trading/BITACORA.md`, `daily_update.py` and `Paper_Trading_1/paper_trading_1.py` in the
  worked example, `examples/liquid-golden-cross/` in the KaxaNuk Researcher package — the gate run
  once, and the answer no, with every row evidenced from `FINDINGS_1.md`. The template's copies are
  the same files with the example's lines removed.
- The strategy's `AGENTS.md`, *Research integrity — the five ways a backtest lies* and *What
  attribution must report*, which criteria 2, 3 and 4 rest on.
- `CHANGELOG.md` in the strategy, *What a version number means here* — `1.0.0` and the gate.
