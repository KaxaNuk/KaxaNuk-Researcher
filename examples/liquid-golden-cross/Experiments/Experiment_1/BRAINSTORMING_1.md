# Brainstorming — Experiment 1

> **Forward-looking. Ideas, plans and what to try next** — the thinking done *before* a change,
> whether by hand or with the AI. Newest entries at the bottom.
>
> This is not the record of what happened; that is [`JOURNAL_1.md`](JOURNAL_1.md), which is
> append-only and dated. Nor is it the hypothesis — once an idea here is committed to, it is written
> into [`BLUEPRINT_1.md`](BLUEPRINT_1.md) and fixed.
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

## 2026-09-19 — choosing the benchmark

- **Idea / question:** what does this strategy have to beat before anyone believes it, and what do
  later experiments compare themselves against?
- **What we tried / considered:** four candidates.
    - *The KN US Equity 600 index itself.* The securities the rule picks from are its constituents,
      its daily holdings and daily returns are already in `Data/Curator/Benchmarks/`, and its return
      series reaches back to 2000, further than the book will ever run.
    - *The S&P 500, through an exchange-traded fund.* Transparent and liquid, but a different
      universe: a difference would mix the rule's effect with the gap between two indices.
    - *An equal-weighted version of our own universe.* Tempting, because the book is equally
      weighted too — but nobody holds it, so beating it proves nothing a person could have earned.
    - *Cash.* The weakest bar in the process, and the one that makes a long-only equity book look
      brilliant for being long equities.
- **Outcome / decision:** the **KN US Equity 600 index**, on the one property that decides such a
  choice — it is the universe the rule selects from, so the comparison isolates the rule rather
  than the choice of market. It is transparent, its constituents are the most traded stocks in the
  United States, and it is stable enough to compare against for twenty years. The engine prices it
  from a level series rebuilt from its own daily returns, staged into the market-data folder like
  any other identifier, because the engine prices everything from one directory.
- **A second yardstick, and the one that settles claim 1:** the same rule with the trend filter
  switched off — the thirty most traded stocks, equally weighted, rebalanced on the same band.
  Beating the index says the book worked; beating the filter-off book is the only thing that says
  the *filter* worked, and the objective's claim 1 is written about the filter. Both are variants
  inside Experiment 1 and both report in `FINDINGS_1.md`.
- **Open threads:** Experiment 1 is the declared benchmark for every later experiment, so its rules
  freeze once `FINDINGS_1.md` reports. The window is not settled here: the index's daily holdings
  begin in 2017, so the point-in-time run starts there and the 2002 run uses the same names
  throughout, which is a survivorship caveat rather than a second result.

<!-- example: end -->
