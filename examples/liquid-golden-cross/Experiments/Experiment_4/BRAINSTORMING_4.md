# Brainstorming — Experiment 4

> **Forward-looking. Ideas, plans and what to try next** — the thinking done *before* a change,
> whether by hand or with the AI. Newest entries at the bottom.
>
> This is not the record of what happened; that is [`JOURNAL_4.md`](JOURNAL_4.md), which is
> append-only and dated. Nor is it the hypothesis — once an idea here is committed to, it is written
> into [`BLUEPRINT_4.md`](BLUEPRINT_4.md) and fixed.
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

## 2026-09-25 — momentum outside bear markets, claim 5's second design

- **Idea / question:** Experiment 3's book of the twenty with the highest twelve-month return
  trailed the pool's twenty most traded by 0.22 points a year over 2002-07-30 to 2026-06-01 and
  failed its kill switch, ahead in one sub-period of three (`RESULTS.md`). None of the three
  experiments passed the gate. The owner wants a book tracked daily by
  `Paper_Trading/daily_update.py`: what is tested next?
- **What we tried / considered:**
    - *Paper-tracking Experiment 3's rule as a labelled candidate.* Not taken: it would put a book
      on paper that failed the gate, which the gate exists to prevent.
    - *Stopping with three honest failures.* Not taken.
    - *A new design of claim 5 from the researcher's library.* Daniel & Moskowitz (2013), carried
      into `Bibliotheca/` for it on 2026-09-25: every one of the fifteen worst momentum months came
      after a negative two-year market return, and after a fall past winners are low-beta, defensive
      names that lag a rebound. Experiment 3 recorded that lag in 2009 — its twenty gained 29.14%
      from 2009-03-02 to 2009-12-31 against the most traded twenty's 65.93% — and **the paper was
      carried after that result was seen**, so the design is informed by it. The blueprint says so
      and counts the trial.
    - *What the book holds in a bear month.* The pool's twenty most traded, so the control stays
      Experiment 3's, the twenty most traded in every month, and the one difference is a ranking
      used only outside bear months. Cash would add a second difference, being out of the market;
      momentum at half size would add a moving part with a size of its own.
    - *Which series decides the state.* The KN US Equity 600's own daily returns, from the desk's
      files: the benchmark every experiment is judged against, known from 2000-01-03, so the state
      exists before the window opens. `SPY`, nearer the paper's value-weighted index, would tie the
      state to one more download.
    - *Which claim.* Claim 5, in a second design, as Experiment 2 was claim 1's; its wording does
      not change.
- **Outcome / decision:** the owner chose, on 2026-09-25, from the options put to him: *"Experiment
  4 first (Recommended)"*; in a bear month, *"The 20 most traded (Recommended)"*; *"Claim 5, a
  second design (Recommended)"*; and the state from *"The KN600's own returns (Recommended)"*. The
  state is the paper's, fixed here before the analyzer measures anything about it: the index's
  return over the prior 24 months negative, read at the prior close, with 24 months taken as 504
  trading days, as the refinery takes a year as 252. Everything else is Experiment 3's unless the
  blueprint says otherwise. A paper book takes its experiment's number, so it would be
  `Paper_Trading_4`, and only if the gate passes and the owner signs. The analyzer measures the
  signal by state next, then `BLUEPRINT_4.md`, then the critic, then the rule.
- **Open threads:** the market's variance, the paper's second forecasting variable, a lever a later
  experiment would have to earn; Cooper, Gutierrez & Hameed (2004), a lead on a three-year state;
  how many of the window's months are bear months, which the analyzer counts.

<!-- example: end -->
