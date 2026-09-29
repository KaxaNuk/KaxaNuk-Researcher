# Journal — Experiment 3

> **Append-only, dated, oldest first.** Every iteration of this experiment, in the order it
> happened. Maintained by the AI as work proceeds.
>
> **Earlier entries are never edited.** The one exception is correcting an error, and the correction
> is written as a new entry saying what was wrong — not by rewriting the original.
>
> The hypothesis is in [`BLUEPRINT_3.md`](BLUEPRINT_3.md); the results that survive are in
> [`FINDINGS_3.md`](FINDINGS_3.md); what to try next is in each entry's open threads.

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

## 2026-09-24 — momentum proper, on the same liquid names

- **Idea / question:** claim 1 is falsified on two windows. Experiment 1's two designs and
  Experiment 2 each earned less than the same liquid names without the cross, by 1.12, 0.86 and
  1.64 points a year, and each failed its kill switch (`RESULTS.md`). What does the strategy test
  next, and under what name? Earlier the same day the owner asked whether to rename it "Liquid
  Momentum", and was told the cross is not momentum: it sets a stock against its own past, where
  momentum ranks stocks against each other (`OBJECTIVE.md`, *What is not claimed*;
  [Paleologo (2021), ch. 5](../../Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/09_Understand_Factors.md),
  p. 74). Momentum proper would be a new signal.
- **What we tried / considered:**
    - *Renaming the strategy "Liquid Momentum".* Not taken: every book priced here holds the
      cross, and a name for a signal no experiment has tested would describe none of them.
    - *A new strategy for momentum*, from `init-strategy`, with an objective of its own. A clean
      lineage, but it would rebuild the universe, the widened seed and the data step this one
      already has, for the same liquid members.
    - *Experiment 3 in this strategy.* The same members, the same widened panel and the same pool,
      whose twenty most traded, without a signal, have been priced on both windows: 18.73% a year
      on 2017 to 2026 as Experiment 1's control and 5.87% on 2002 to 2016 as Experiment 2's, each
      on its own rule's dates (`RESULTS.md`). It needs a claim of its own: `OBJECTIVE.md` says the
      momentum literature is context for claim 1 rather than evidence, so a momentum book cannot
      move claim 1.
    - *The owner's sentence, read as a rule.* "The 20 most-traded members ranked by their own
      12-month return": the twenty most traded, ranked and then all held at one twentieth, would
      be the control itself, so the ranking has to choose. The blueprint reads it as the twenty
      with the highest twelve-month return, the latest month left out, from the hundred most
      traded members — the top fifth, the review's quintile — with the pool at 50, 150 and 200
      among the perturbation's cells.
    - *His two windows.* "Tested on 2002–2016 and 2017–2026": in the blueprint they are one test
      window, 2002-07-30 to 2026-06-01, which the kill switch reads in three sub-periods, 2002 to
      2008, 2009 to 2016 and 2017 to 2026. The last is his second window; his first is priced as a
      window of its own too, 2002-07-30 to 2016-12-30, as description, so that a silent kill switch
      with 2002 to 2008 lost is not read as a pass on 2002 to 2016.
- **Outcome / decision:** the owner chose, on 2026-09-24, from the options put to him:
  *"Experiment 3, then paper (Recommended) — A new idea on the same liquid names: the 20
  most-traded members ranked by their own 12-month return, the momentum proper. Blueprint and
  critic first, then tested on 2002–2016 and 2017–2026. If it passes the gate and you sign, it's
  frozen as Paper_Trading_1 and tracked daily."* A paper book takes its experiment's number, so it
  would be `Paper_Trading_3`. The same day claim 5 was added to `OBJECTIVE.md` in his words, the
  main idea and claims 1 to 4 untouched. **The analyzer measured the signal after the choice, not
  before it:** `r_momentum_12_1` was added to the refinery and the analyzer run on the widened
  panel, rows 19 to 30 of `RESULTS.md` — a coefficient at a month of 0.0134 on 2002 to 2016 and
  0.0304 on 2017 to 2026 among the hundred most traded, and below zero at a quarter and at a year
  on the first. `BLUEPRINT_3.md` comes next, then the critic, then the rule.
- **Open threads:** the coverage of the index's weight after 2017, which no run has printed,
  measured before the rule; whether a 5% reserve holds under a full re-strike every month, fixed
  in the blueprint before any run and not moved after one; a note on Lee & Swaminathan (2000), a
  lead against the claim on its own names; long-short, volatility-scaled, residual and
  industry-neutral momentum, each a later experiment.

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
