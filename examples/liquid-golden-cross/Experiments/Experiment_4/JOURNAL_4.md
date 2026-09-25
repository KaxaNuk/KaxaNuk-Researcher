# Journal — Experiment 4

> **Append-only, dated, oldest first.** Every iteration of this experiment, in the order it
> happened. Maintained by the AI as work proceeds.
>
> **Earlier entries are never edited.** The one exception is correcting an error, and the correction
> is written as a new entry saying what was wrong — not by rewriting the original.
>
> The hypothesis is in [`BLUEPRINT_4.md`](BLUEPRINT_4.md); what to try next is in
> [`BRAINSTORMING_4.md`](BRAINSTORMING_4.md); the results that survive are in
> [`FINDINGS_4.md`](FINDINGS_4.md).

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

## 2026-09-25 — what this experiment reads of the others, before its blueprint

- **Idea / question:** Experiment 4 is Experiment 3's rule with one condition added, on the same
  members and the same panel. `AGENTS.md`, *One experiment at a time*, lets an experiment read
  another's files once the request and the reason are written here first.
- **What we tried / considered:**
    - **Read, and why.** Experiment 3's files, all of them: this rule is Experiment 3's with a state
      added and this control is Experiment 3's control, so their choices are this design, not a
      contamination of it; and its findings, for the figures the design follows from, the 2009
      rebound above all, which the blueprint names as seen. Through `JOURNAL_3.md`, the fifty-one
      exclusions and the coverage, as Experiment 3 read them from Experiment 2. Experiment 1's
      files, the standing exception, and `RESULTS.md`, the shared record.
    - **Carried:** the members, the widened seed, the exclusions and their tests, the pool and its
      liquidity rank, the momentum column, the twenty names, the monthly re-strike, the lag, the
      fills, the costs and the 5% reserve, the test window, the sub-periods, and the handling of a
      run the engine cannot price. **Not carried:** the perturbation's cells and the predictions,
      which this blueprint fixes for itself.
- **Outcome / decision:** the look-across is the one above and no wider.
- **Open threads:** the exclusions and the coverage re-measured, and the bear months counted on the
  window, recorded here before the rule runs.

<!-- example: end -->

<!-- example: begin -->

## 2026-09-25 — the blueprint's settings, and its cold review, before its commit

- **Idea / question:** what the owner decided for `BLUEPRINT_4.md` beyond `BRAINSTORMING_4.md`, and
  what the blueprint critic's review changed, recorded before the blueprint is committed and before
  any rule.
- **What we tried / considered:**
    - **The owner's settings, 2026-09-25, from the options put to him:** for the stale repeated
      bars, *"End each at its last real bar (Recommended)"*; for the reserve, *"10% (Recommended)"*,
      where the entry above carried Experiment 3's 5% — this entry supersedes that line; for the
      perturbation, *"12 cells, pass at 10 (Recommended)"*.
    - **The blueprint critic's review**, cold, of the draft: thirteen objections, most serious first
      — the diagnostic arm left out of the trial count; a stale-bars check that did not define one
      book; perturbation cells whose bear-month book or control was undefined; what was known when
      the design was written, not said where each limb is fixed; a state never having to beat its
      simpler baseline; evidence against left out, row 33, the Paleologo chapter's 2016 crash, and
      Sarkar, Du & Vafai; no reason given for the ranking outside bear months, and a page slip; the
      analyzer's pool and timing not the rule's; shares and overlap missing beside the coefficients;
      an unpriced headline run given two outcomes; the list of changes that may not rescue it
      incomplete; and prediction 2 a lead the status depends on.
    - **The owner's decisions on the two that change the test:** for the arm, *"Count it: 68 trials
      (Recommended)"*; and *"Yes, as a kill-switch limb (Recommended)"*: the rule must beat momentum
      in every month on both Sharpe and CAGR over the window.
- **Outcome / decision:** the draft was revised on every point before its commit, and
  `BLUEPRINT_4.md` is the revised text.
- **Open threads:** the exclusions, the coverage, the bear month starts counted at the rule's
  timing, and the listings the stale-bars check ends, measured by the notebook's setup cells and
  recorded here before the rule cell holds code.

<!-- example: end -->

<!-- example: begin -->

## 2026-09-25 — before the rule: the exclusions, the coverage, the stale bars and the state

- **Idea / question:** what `BLUEPRINT_4.md` asks to be recorded before the rule runs.
- **What we tried / considered:** the notebook's setup and panel cells, run alone after the
  blueprint's commit and before the rule cell held code, from 07:34 to 07:36 on 2026-09-25. The
  register gives the same fifty-one exclusions as Experiments 2 and 3, none carrying two companies
  under one identifier. The panel is 6,390 dates by 1,437 positions, to 2026-06-01, and inside the
  test window the priced members hold at least 99.71% of the index's weight on every date, the
  lowest on 2003-09-02; no date falls below 95%. The stale-bars check ends nine listings, the nine
  Experiment 3's scan found, each at its last distinct bar, with the rows after it read as no price:
  `ABMD` at 2022-12-22, one row; `ATVI` at 2023-10-13, five; `CMA` at 2026-01-30, one; `CSC` at
  2017-04-03, 1,111; `SGEN` at 2023-12-14, six; `SNCR` at 2026-02-13, three; `SRCL` at 2024-11-01,
  four; `VMW` at 2023-11-21, three; and `ZIONO` at 2024-12-17, five. One file lacks the four bar
  columns and is not checked: `KN600`, the index the curator stages from the desk's returns, which
  no book holds. At the rule's timing the state is bear on 43 of the window's entries: its first
  day, 2002-07-30, where the index's two-year return read −36.41%, and the month starts of August
  2002 to September 2003 and December 2003, of October 2008 to September 2010, of April 2020, and of
  May and November 2023 — the analyzer's 42 month starts and the window's first day.
- **Outcome / decision:** the rule runs on this window, these exclusions, this check and this state,
  as the blueprint fixed them.
- **Open threads:** none before the run.

<!-- example: end -->

<!-- example: begin -->

## 2026-09-25 — the run, from a wiped working copy

- **Idea / question:** the rule, as `BLUEPRINT_4.md` fixed it, run end to end.
- **What we tried / considered:** the notebook ran in a wiped working copy from 07:41 to 09:26 on
  2026-09-25, after the analyzer, which reproduced its rows 1 to 38 exactly, and in the working copy
  from 07:37 to 09:24. All forty engine runs priced, in both. The two copies printed every figure
  the same but one line of the first cut, the interaction, +100.32 in the wiped copy and +100.31 in
  the working copy, where the fresh download's lack of `MIC` excludes it from the index in one and
  not the other.
- **Outcome / decision:** `FINDINGS_4.md` reports the wiped copy's run. The kill switch trips on
  prediction 1's Sharpe margin, +0.0084 where 0.03 was required, with its other two limbs silent,
  and criterion 3 reads five cells of twelve; claim 5 stays falsified, now for two designs.
- **Open threads:** what follows is the owner's to decide.

<!-- example: end -->
