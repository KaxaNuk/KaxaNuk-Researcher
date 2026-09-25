# Journal — Experiment 3

> **Append-only, dated, oldest first.** Every iteration of this experiment, in the order it
> happened. Maintained by the AI as work proceeds.
>
> **Earlier entries are never edited.** The one exception is correcting an error, and the correction
> is written as a new entry saying what was wrong — not by rewriting the original.
>
> The hypothesis is in [`BLUEPRINT_3.md`](BLUEPRINT_3.md); what to try next is in
> [`BRAINSTORMING_3.md`](BRAINSTORMING_3.md); the results that survive are in
> [`FINDINGS_3.md`](FINDINGS_3.md).

**Paths and figures inside entries are as they were written.** Where a path has since moved the
entry is left alone — it was correct on its date.

**Repository-level history belongs here** — choosing the benchmark, the data step, the architecture.
Experiment 1 is the first rule tested against the benchmark and therefore the shared context; later
experiments' journals point here rather than copying it.

**Entry format:**

```
## YYYY-MM-DD — short topic

- Idea / question:
- What we tried / considered:
- Outcome / decision:
- Open threads:
```

---

The first entry is usually *repository instantiated from the template*: what this repository is for,
which template version it was created from, the strategy name, and everything `OBJECTIVE.md` still
leaves open.

<!-- example: begin -->

## 2026-09-24 — what this experiment reads of the others, before its blueprint

- **Idea / question:** Experiment 3 trades the members Experiment 2 traded, on the panel it built,
  without the names it excluded. `AGENTS.md`, *One experiment at a time*, lets an experiment read
  another's files once the request and the reason are written here first.
- **What we tried / considered:**
    - **Read, and why.** Experiment 1's files, the standing exception. `RESULTS.md`, the shared
      record, for the controls' figures, the trial count and the 2% reserve's overdraw. Of
      Experiment 2: `JOURNAL_2.md`, for the fifty-one names it excluded and the coverage it
      measured before its rule, because this experiment trades the same members on the same panel
      and a second reading of the same data issues would be a second universe; `FINDINGS_2.md`,
      for the figures `RESULTS.md` compiles from it, at their source; and `BLUEPRINT_2.md` and
      `BRAINSTORMING_2.md`, for the documents' shape.
    - **Carried:** the widened seed, the exclusions and their tests, the fill convention, the
      liquidity rank and the cost row, the 5% reserve included. **Not carried:** the cross, the
      band, the trigger, the sub-periods and the perturbation; this experiment's rule, control,
      dates and cells are its own, fixed by the owner's choice and `BLUEPRINT_3.md` before any book
      is built.
- **Outcome / decision:** the look-across is the one above and no wider. Anything else read from
  Experiment 2 before `FINDINGS_3.md` reports is written here first.
- **Open threads:** the exclusions by name and the coverage re-measured, both recorded here before
  the rule runs.

<!-- example: end -->

<!-- example: begin -->

## 2026-09-24 — before the rule: the exclusions and the coverage

- **Idea / question:** what `BLUEPRINT_3.md` asks to be recorded before the rule runs.
- **What we tried / considered:** the notebook's setup and panel cells, run alone after the
  blueprint's commit and before the rule cell held code. The register gives the same fifty-one
  exclusions as Experiment 2 — the 47 names with no price file, and `CIT`, `FMC`, `LCI` and `PARA`,
  whose adjusted price multiplies by more than six in a day — and none carries two companies under
  one identifier. The panel is 6,390 dates by 1,437 positions, to 2026-06-01, and the index's
  membership is known from 2000-01-03 to 2026-08-14. Inside the test window, 2002-07-30 to
  2026-06-01, the priced members hold at least 99.71% of the index's weight on every date, the
  lowest on 2003-09-02, and no date falls below 95%.
- **Outcome / decision:** the rule runs on this window and these exclusions, as the blueprint fixed
  them.
- **Open threads:** none before the run.

<!-- example: end -->

<!-- example: begin -->

## 2026-09-24 — the first full run stopped at the null; a name with no price in a window

- **Idea / question:** the notebook's first end-to-end run, 18:26 to 18:52, stopped in the engine
  cell. The rule and its control priced over the whole window — the rule at a CAGR of 10.81% and a
  Sharpe of 0.436, the control at 11.03% and 0.465, both valued to 2026-06-01 — and the third run,
  the null holding the whole pool, was refused: the engine found an empty table for `WCOEQ`.
- **What we tried / considered:** `WCOEQ` is WorldCom, a Sharadar row of the seed. Its last two
  prices are 2002-07-26 and 2002-07-29; the window opens on 2002-07-30. It was among the hundred
  most traded on the lagged date of the first rebalance, so the null holds it, and a name held with
  no price anywhere in a run's window leaves the engine nothing to fill or value. The rule and the
  control never held it, which is why they priced. Nothing after the null ran, and no verdict was
  drawn from the two figures: the blueprint reads every run in the record, not the first two.
- **Outcome / decision:** a mechanical fix, not a change of rule. Before each run's weight file is
  written, a name held with no price anywhere inside that run's window is dropped from it and
  named in the output; its weight stays in cash until the next rebalance, as the reserve does. The
  selection, the control, the dates, the cells and the costs are the blueprint's, unchanged, and a
  run that drops nothing writes the same weight file as before. The notebook is re-run end to end
  with the fix.
- **Open threads:** which runs drop a name, and how many, read from the re-run's output into
  `FINDINGS_3.md`.

<!-- example: end -->

<!-- example: begin -->

## 2026-09-24 — two runs the engine could not price, and the notebook that stopped at the first

- **Idea / question:** the second end-to-end run, 18:56 to 20:13 in this working copy, with a run
  from a wiped working copy beside it from 19:14, stopped inside the perturbation. What does the
  blueprint say to do with a run the engine cannot price?
- **What we tried / considered:**
    - **The null priced**, with `WCOEQ` dropped from its weight file as the previous entry fixed.
    - **The lookback 6 months cell's rule stopped valuing the book.** The engine logged a cash
      error on 2003-03-03 of −$16,557.91, a full re-strike overdrawing the 5% reserve, and still
      returned a summary of the seven months before it.
    - **The pool 150 cell's rule was refused**, in both copies. The engine's integrity check found
      no price on 2023-12-01 for `VMW`, a name the book held. VMware last traded on 2023-11-21, and
      its file repeats that day's bar on 2023-11-24, 2023-12-13 and 2023-12-15, so the engine does
      not read it as delisted and finds the position open on a month start with no price. A scan of
      every price file found nine listings whose file ends in a run of repeated bars after their
      last distinct one inside the test window: `CSC`, `ABMD`, `ATVI`, `VMW`, `SGEN`, `SRCL`,
      `ZIONO`, `CMA` and `SNCR`, all from FMP; `CSC`'s run lasts from 2017-04-03 to 2021-09-10.
    - **The notebook raised at the refusal**, so no later cell was priced in that run.
- **Outcome / decision:** the blueprint already answers it. "A run that overdraws even so is not
  priced and is excluded by name", and a sub-period or a cell "with either of its runs unpriced
  counts against the rule"; an unpriced rule or control over the test window leaves claim 5
  measured. So no price file is changed, and no name is excluded: the exclusions stay the
  fifty-one. The notebook now records a run the engine refuses, or that stops valuing the book
  before its window ends, by name with the engine's reason, never as figures, and goes on; the
  summary counts such a cell or sub-period against the rule, and the Verify section checks that
  each is named. The verdict cell named claim 1 and `FINDINGS_2.md`, carried from Experiment 2's
  notebook: it now names claim 5 and `FINDINGS_3.md`, and its confirmed status also asks that the
  rule's Sharpe be above the index's, as the blueprint's claim section does. The notebook is re-run
  end to end, the run from a wiped working copy as the record.
- **Open threads:** the repeated bars are a data check nobody wrote; which books held any of the
  nine names across a repeated bar, and what a check at the curator would have caught, is for
  `FINDINGS_3.md` and a later experiment, never this one.

<!-- example: end -->
