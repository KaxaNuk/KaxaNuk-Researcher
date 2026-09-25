# Brainstorming — Experiment 3

> **Forward-looking. Ideas, plans and what to try next** — the thinking done *before* a change,
> whether by hand or with the AI. Newest entries at the bottom.
>
> This is not the record of what happened; that is [`JOURNAL_3.md`](JOURNAL_3.md), which is
> append-only and dated. Nor is it the hypothesis — once an idea here is committed to, it is written
> into [`BLUEPRINT_3.md`](BLUEPRINT_3.md) and fixed.
>
> Keeping the two apart is what stops planning being mistaken for history.

**Entry format:**

```
## YYYY-MM-DD — short topic

- Idea / question:
- What we tried / considered:
- Outcome / decision:
- Open threads:
```

---

The first entry is usually *choosing the benchmark*: what should every future experiment be measured
against, which candidates were considered, and the one property that decided between them — a
benchmark is chosen for being transparent, liquid and stable, not for being clever.

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

<!-- example: end -->
