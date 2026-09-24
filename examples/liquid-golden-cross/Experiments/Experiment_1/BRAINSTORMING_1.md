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

<!-- example: begin -->

## 2026-09-23 — rewriting Experiment 1 to sell a broken cross fast

- **Idea / question:** the owner's: hold the twenty most traded stocks above their 50/200 cross,
  tested before outside this repository, and his lead on why the first design lost to its control —
  the 10% band keeps a name after its cross breaks, until enough of the rest of the book moves.
- **What we tried / considered:** measuring the lead before designing anything.
    - *The first design's book*, read from its weight file against the refined signal lagged a
      day: 9.6% of its 70,920 held name-days were in a stock already below its cross; after a break
      the book kept the name a median of 19 trading days, a mean of 29.1 and at most 147; and on
      74.9% of days it held at least one such name. This is the book's construction, read from the
      weight file, not a performance figure.
    - *The analyzer*, section 5, on the whole panel. As a 0/1 state inside the traded pool the cross
      ranks names at an information coefficient of 0.0066 over 21 days, positive on 51.8% of dates,
      −0.0011 over 63 and 0.0035 over 252 — a weak ranker. After a break, on 616 breaks, a name
      trails the rest of the pool by a mean 0.51% and a median 0.31% over 21 days, and 0.91% and
      1.04% over 63, below the pool 51.9% and 53.4% of the time.
    - *Trading every day* to a fresh top twenty: rejected, because ranking churn is noise the
      analyzer already measures as close to zero, and paying for it is what the band was for.
- **Outcome / decision:** the owner decided on 2026-09-23 to **rewrite Experiment 1** rather than
  open Experiment 2, knowing the template freezes a reported Experiment 1: the first design is kept
  at tag `v0.15.0` and as a row of `RESULTS.md`, and its runs count in the trials. The rewrite
  separates exits from entries — sell the day after the cross breaks, replace from the top of the
  ranking with the proceeds, and let ranking churn trade only once a month through a buffer of
  thirty. Twenty names, the owner's number. The benchmark stays the KN US Equity 600; the control
  becomes the same rule without the cross.
- **Open threads:** the break measurement is modest — half a point a month, on barely more than half
  the breaks — so the rewrite may not rescue claim 1, and the kill switch in the blueprint is
  written for that case. The desk's holdings now reach back to 2000, which would allow a
  twenty-four-year point-in-time window once the seed is widened to every name the index held.

<!-- example: end -->
