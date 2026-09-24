# Brainstorming — Experiment 2

> **Forward-looking. Ideas, plans and what to try next** — the thinking done *before* a change,
> whether by hand or with the AI. Newest entries at the bottom.
>
> This is not the record of what happened; that is [`JOURNAL_2.md`](JOURNAL_2.md), which is
> append-only and dated. Nor is it the hypothesis — once an idea here is committed to, it is written
> into [`BLUEPRINT_2.md`](BLUEPRINT_2.md) and fixed.
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

## 2026-09-24 — confirming the slow exit on years it was not found on

- **Idea / question:** Experiment 1's second design sold a broken cross the day after it broke and
  lost to its control; its diagnostic arm — twenty names, the whole set re-equalised only on a day
  it moves by three names or more, so a broken name is held a median of 28 trading days — earned
  19.52% a year with a Sharpe of 0.877, against the fast exit's 17.87% and 0.806, and the index's
  14.63% and 0.770, over 2017 to 2026 (`../Experiment_1/FINDINGS_1.md`). Is that slow exit an edge,
  or the best of several books tried on one window?
- **What we tried / considered:**
    - *Freezing the arm as it stands.* Rejected: it was one of forty-five runs on the window that
      had already falsified claim 1 once, and choosing it after seeing it is a trial, not a result.
    - *The held-out months since 2026-06-01.* Too short: months cannot show skill.
    - *Years it was not found on.* The desk's holdings reach back to 2000, so the same rule can be
      run point in time from 2002, when the cash proxy starts, to 2016, the year before the window
      it was found on. The seed held only 64% of the index's weight in 2000 and 90% by 2016, because
      the names that left before 2017 were never in it; widening it to every listing the index held
      adds 712 names, and FMP carries almost none of them on this key — nineteen of a sample of
      twenty came back empty.
    - *The dead names from Sharadar*, through the Data Curator's Sharadar provider, on the library's
      issues/31 branch until it is released. Sharadar keeps the companies that left the market, and
      the desk's suffixed tickers, such as `AGN1`, are its convention for a reused ticker. It
      publishes no VWAP, so for those names the fill price is the day's close and the traded value
      the close times the volume — a difference in how they are filled, stated wherever it matters.
- **Outcome / decision:** the owner decided on 2026-09-24 to confirm the arm's design on 2002 to
  2016 as Experiment 2, with the seed widened and the dead names from Sharadar, and to take it to
  paper trading only if it passes its own gate. **The arm was never priced against its own
  control**: the first design, the same timing at thirty names, lost to its control by 1.12 points a
  year, so whether the cross earns anything at twenty is the open question, and the blueprint says
  so.
- **Open threads:** how much of the index's weight the priced names hold before 2017, once the dead
  names are in, decides where the window can start; the blueprint fixes that rule before anyone
  looks.

<!-- example: end -->
