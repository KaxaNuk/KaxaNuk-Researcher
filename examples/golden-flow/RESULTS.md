# Results

> **Executive summary of everything this repository has measured.**
>
> Experiment sections are compiled from the `FINDINGS_N.md` files and cite each one. **When a number
> changes, change it in `FINDINGS_N.md` first**, then update this file — a summary that leads its
> sources is how two numbers for the same book start to circulate.
>
> **One exception:** findings from step 3, `Data/analyzer.ipynb`, go straight into *Before any
> experiment* below: notebook outputs are stripped before committing, so a measurement that lives
> only in a cell output does not survive the commit.
>
> Every performance figure comes from the **KaxaNuk Backtest Engine**. There is no second backtest
> in this repository, by design.
>
> Until the first experiment reports, every table below except *Known limitations* is empty: the
> shape is fixed, the numbers arrive from the pipeline.

<!-- example: begin -->

> **In this example, what follows each template paragraph is Golden Flow's, measured.** Experiment 1
> ran on 2026-10-06 from a wiped working copy, with Backtest Engine 0.66.0 and Attribution Analysis
> 0.2.0. Every attribution figure comes from Attribution Analysis. A table whose row reads as an
> instruction is the template's shape, and Golden Flow's follows it.

<!-- example: end -->

## The project in three sentences

Does the benchmark book work, with its headline numbers. What attribution says about where the
return comes from. Which lever earned its place after the benchmark, and which was rejected.

<!-- example: begin -->

**The book works, in sample and net of costs, and most of why is the market.** It holds the KN US
Equity Core members whose 50-day average sits above their 200-day, ranked and weighted by 63-day
traded value, none above 20% and none below 1%. Over 2015-01-02 to 2026-06-01 it compounds at 20.33%
a year, for a Sharpe of 0.842 and a worst drawdown of −32.5%. The same rule with the golden cross
switched off earns 19.73%, 0.763 and −46.3%. The KN US Equity Core earns 13.05% and 0.713, and `SPY`
13.49% and 0.743.

**Attribution puts nine tenths of its excess return in factors, mostly the market, and names what
the golden cross does: it cuts beta.** The rule takes 10.39 points from beta, against its control's
22.15. Its idiosyncratic return is +13.84 points against the control's −9.48, above all twenty
random books. Once factors are stripped out, its selection is +2.70 points over the window:
positive, and thin.

**It was signed into paper trading on 2026-10-06, and nothing here is out of sample.** The golden
cross earned its margin in 2015 to 2022. It lost the 2023–2026 rally to its control by 11.4 points a
year. The paper book is retired, not tuned, if it misses its control by the blueprint's margins on
its paper days, read first on 2027-10-06.

<!-- example: end -->

---

## Before any experiment: what the data already says

Findings from step 3, `Data/analyzer.ipynb`: whether a candidate feature carries information, over
what horizon, and with which sign — and anything measured about the signal that does not need a
book. Cite the section each number came from.

**State the horizon and the overlap.** A coefficient over *h* days, measured every day, shares
*h − 1* days with the next one, so its dates are not independent observations. Beside any
coefficient or ratio, report the share of dates on which it had the sign the hypothesis expects.

| # | Measurement | Value | Dates with the expected sign | Section |
| --- | --- | ---: | ---: | --- |
| 1 | what was measured, over which horizon, on which pool | the number | for a coefficient or a ratio, the share of dates with the sign the hypothesis expects | the analyzer section |

<!-- example: begin -->

**Measured on 2026-10-06 by `Data/analyzer.ipynb`**, over the KN US Equity Core's members on each
date: 518 to 600 of them in the window, 803 securities in all. Every matrix is cut at 2026-06-01,
`ANALYSIS_END`.

The **pool** is the fifty most traded members on each date, the neighbourhood the rule selects from.
The **window** is 2015-01-02 to 2026-06-01, fixed by the universe notebook's coverage rule.
**Before** is 2002-01-02 to 2015-01-01, read for context. The expected sign is positive throughout.
Consecutive windows share 20, 62 and 251 days at the three horizons, so the dates are not
independent and the ratios overstate the evidence.

| # | Measurement | The window | Dates with the expected sign | Before the window | Section |
| --- | --- | ---: | ---: | ---: | --- |
| 1 | Mean pairwise correlation of daily returns, 787 members with 500 days in the window | 0.309 | — | | 2 |
| 2 | The cross as a state, 1 above and 0 below, information coefficient on the pool, 21 days | +0.0235 (IR 0.100) | 54.6% | −0.0010 | 4 |
| 3 | The same, 63 days | +0.0275 (IR 0.127) | 58.0% | −0.0138 | 4 |
| 4 | The same, 252 days | +0.0161 (IR 0.085) | 52.9% | −0.0053 | 4 |
| 5 | The trend distance `r_trend_50_200`, on the pool, 21 / 63 / 252 days | +0.0334 / +0.0333 / +0.0258 | 56.1% / 57.3% / 51.7% | −0.0002 / −0.0091 / −0.0162 | 4 |
| 6 | The traded-value rank `r_liquidity_rank`, on the pool, 21 days | +0.0327 (IR 0.161) | 56.8% | −0.0204 | 4 |
| 7 | The same, 63 days | +0.0526 (IR 0.247) | 62.0% | −0.0312 | 4 |
| 8 | The same, 252 days | **+0.0977 (IR 0.497)** | **73.6%** | **−0.0494** | 4 |
| 9 | The traded-value rank on every member, 252 days | +0.0250 (IR 0.257) | 54.6% | −0.0722 (IR −0.711) | 4 |
| 10 | Forward 21-day return on the pool, cross on against off | 1.45% against 1.27% | — | | 5 |
| 11 | Forward 21-day volatility on the pool, cross on against off | 28.8% against 32.4% | — | | 5 |
| 12 | Golden-cross members holding at least 1% of the cross members' traded value, median by year | 10 to 18 | — | | 5 |
| 13 | The largest single share of the cross members' traded value, median by year | 4.1% (2017) to 15.7% (2024) | — | | 5 |

**What it says, before any book.** In the window, both halves of the idea carry a small positive
coefficient in the pool the rule selects from, the traded-value rank more than the cross. The cross
separates volatility more than return. **Before the window, both are flat or negative**, the
traded-value rank strongly so across all members, as the three liquidity papers in `Bibliotheca/`
say. What the window shows is the window's: the experiment is judged on it by the owner's choice,
and the earlier years are not a test of it.

The index's own concentration rose across the window. The largest name's share of the cross members'
traded value nearly quadrupled from 2017 to 2024, which is what the 20% cap exists for.

<!-- example: end -->

---

## The experiments

Each experiment ranks its variants over **one window shared by all of them**, and those windows can
differ between experiments.

> **Compare a winner's Sharpe with its own experiment's control.** Windows can differ between
> experiments, so a winner is comparable to its own control row, not to another experiment's
> headline; `vs control` is the column to compare across experiments.

**Each row names the claim it moved**: the claim of `OBJECTIVE.md` its blueprint set out to move,
and the status it reached. A row that beats its benchmarks and moves no claim is a number, not a
finding.

| Exp | Book | CAGR | Sharpe | Max DD | Control Sharpe | vs control | Status | Claim moved | Findings |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| **1** | the benchmark rule, in five words | | | | — | — | **the benchmark** | the claim's number, and its new status | [`FINDINGS_1.md`](Experiments/Experiment_1/FINDINGS_1.md) |

<!-- example: begin -->

| Exp | Book | CAGR | Sharpe | Max DD | Control Sharpe | vs control | Status | Claim moved | Findings |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| **1** | KN US Equity Core members above the golden cross, ranked and weighted by 63-day traded value, cap 20%, floor 1%, on change | **20.33%** | **0.842** | −32.5% | 0.763 | **+0.080** | **the yardstick, and graduated**: criteria 1 to 4 pass, criterion 3 exactly at its bar; signed by the owner on 2026-10-06 into paper trading as `Paper_Trading_1` | 1, the signal, and 2, the sizing: **confirmed as a book**, on the KN US Equity Core, 2015 to 2026; 3, the construction: true by construction, measured only through claim 1's control | [`FINDINGS_1.md`](Experiments/Experiment_1/FINDINGS_1.md) |
| 1, earlier | an earlier version, on another index | 24.69% | 0.948 | −34.6% | 0.842 | +0.106 | replaced | the objective of its time; none of it carries over | not part of this example |

**The first row is the rewritten Experiment 1.** A name is eligible on a day when three things hold:

- it was a KN US Equity Core member the day before, mapped to its FMP symbol through the seed;
- its golden cross holds at the prior close: `r_trend_50_200` above zero, read as a state rather
  than a crossing;
- FMP has a fill price for it that day and the next. A name whose prices are about to stop is sold
  the day before, the owner's rule.

The eligible names are ranked and weighted by the refinery's `r_traded_value_sma_63d`, no weight
above 20%. They are added in rank order while the smallest weight stays at or above 1%, so the
bounds set the count: a median of 37 names a day, from 18 to 61. The book rebalances when the held
set changes, on 48.1% of trading days. Its control is the same rule with the golden cross off, the
same bounds and the rule's own rebalance dates.

**The window and the costs.** The window, 2015-01-02 to 2026-06-01, opens on the owner's floor:
members priced by FMP, this experiment's provider, held 92.97% of the index's weight that day, above
the 90% the coverage rule asks. Every book is net of `commission_cents=0.05` on the unadjusted
price, 5 basis points of slippage and a 1% cash reserve. The benchmarks are the KN US Equity Core,
engine identifier `KN_US_Equity_Core`, then `SPY`. The cash proxy is `BIL`.

**The second row is an earlier version of Experiment 1, on another index.** A rewrite keeps its
earlier version as a row, and its books count in the trials below. None of its numbers describes
this rule.

<!-- example: end -->

### Against the world

The same book measured against every benchmark it reports against, over one stated window.

<!-- example: begin -->

**2015-01-02 to 2026-06-01, net of costs**, from
[`FINDINGS_1.md`](Experiments/Experiment_1/FINDINGS_1.md). The engine counts the window as 11.81
years: 2,976 weekday steps after the first day, over 252. The calendar span is 11.41 years, so every
CAGR is the engine's.

| Book | CAGR | Volatility | Sharpe | Sortino | Max drawdown |
| --- | ---: | ---: | ---: | ---: | ---: |
| **The rule** | **20.33%** | 24.13% | **0.842** | 1.116 | −32.47% |
| The control, the cross removed | 19.73% | 25.86% | 0.763 | 1.011 | −46.32% |
| The rule's names, equally weighted | 14.53% | 20.12% | 0.722 | 0.967 | −30.19% |
| The rule, realistic commission | 20.75% | 24.13% | 0.860 | 1.138 | −32.18% |
| KN US Equity Core | 13.05% | 18.32% | 0.713 | 0.878 | −33.75% |
| `SPY` | 13.49% | 18.16% | 0.743 | 0.981 | −33.63% |

| Sub-period | Rule CAGR | Rule Sharpe | Control CAGR | Control Sharpe | Index Sharpe | `SPY` Sharpe |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2015 to 2018 | 9.02% | 0.530 | 7.86% | 0.468 | 0.438 | 0.493 |
| 2019 to 2022 | 16.82% | 0.619 | 9.05% | 0.295 | 0.518 | 0.549 |
| 2023 to 2026-06-01 | 40.44% | 1.483 | **51.85%** | **1.830** | 1.455 | 1.443 |

**Where the return comes from**, in points summed daily over the window. The book's weights and the
index's are held overnight:

| | The rule | The control | Equal weight |
| --- | ---: | ---: | ---: |
| First cut, Brinson-Fachler per asset: selection | **17.44** | | |
| Factor model: total excess | 137.35 | 120.81 | 80.01 |
| — of it, factor exposure | 123.50 | 130.28 | 110.05 |
| — of which the market | 88.10 | 88.08 | 88.06 |
| — of which beta | 10.39 | 22.15 | 5.59 |
| — idiosyncratic | **+13.84** | −9.48 | −30.03 |
| Third pass, on the residual: selection | **+2.70** | −0.27 | −0.80 |

The first cut's benchmark reconciles with the index's own returns within 0.54 points a year, inside
the blueprint's 1.0. All twenty random books have a negative idiosyncratic return, −84.50 to −3.77.

<!-- example: end -->

**Does it reproduce?** Re-run from a wiped working copy and state the drift. Curator output rebases
every dividend-adjusted column on a re-pull, so a Sharpe moving in the third decimal is that effect,
not a strategy change.

<!-- example: begin -->

**Experiment 1 ran from a wiped working copy.** Before any stage ran, every gitignored output of the
earlier version was moved aside, not deleted. Every number of this version above was produced from a
fresh download by this version's code ([`JOURNAL_1.md`](Experiments/Experiment_1/JOURNAL_1.md),
2026-10-06). A clone on another machine is the stronger test, and is still to be run.

<!-- example: end -->

### The trial count

**How many variants were ranked, in each experiment, plus any excluded run.** Published because a
reader cannot discount a best-of-N result without knowing N.

<!-- example: begin -->

**107 books**: 76 fixed by the blueprint before the rule was coded — 37 priced by two earlier
versions of the strategy and 39 in this run — and 31 priced in the run's first attempt, excluded
below and counted; plus one choice, the 2015 window, chosen after an earlier version's 2017–2026
result was heard. The deflated Sharpe is not computed.

This run's 39 are the rule, its control, the sixteen of the sweep, the equal-weight arm and twenty
random books. The first attempt's 31 were priced before the sell-at-t−1 rule. The cost rows and
sub-period windows re-price these books and add none; neither does a re-run of an identical book.

<!-- example: end -->

---

## What stands — reuse, do not rebuild

A result, a module or a method later work should start from rather than re-derive. One line each,
with its number.

<!-- example: begin -->

- **The control that differs in exactly one thing.** The same names, the same sizing, the rule's own
  dates, the golden cross off. On the KN US Equity Core it measures the cross at +0.60 points a
  year, +0.080 of Sharpe and 13.85 points of drawdown.
- **The random arm at the rule's turnover.** Twenty books draw the rule's count from the members on
  the rule's dates, sized by traded value under the cap. Every one has a negative idiosyncratic
  return, −84.50 to −3.77, so the rule's +13.84 is read against books that trade as it does.
- **Sell before a price series stops.** `portfolio_construction.exit_before_price_stops` makes a
  name tradable on t only if it is priced on t and on t+1. So a delisting or a gap at a corporate
  event triggers a re-strike at t−1, at a real price; the engine refuses any book that holds a name
  through a gap. One day of hindsight, applied to every book alike.
- **The reconciliation before the first cut, and weights held overnight.** The Brinson-Fachler
  benchmark is checked against the index's own returns before any pass is read. It caught an
  infinite return from a zero price and a one-day misalignment worth 6.94 points a year.
  `attribution_analysis.held_overnight` pairs the close of t−1 with day t's return.
- **The bounded weigher.** `portfolio_construction.bounded_book` sizes by score inside a cap and a
  floor and lets the bounds set the count, cutting the score at the prior close once.
- **The prior-close probe.** Experiment 1's notebook does not carry the probe: it checks the
  invariant that every holding had its cross at 1 at the prior close, and the paper book's band
  watches the rest. Bringing the probe back is an open item, lead 7 below.

<!-- example: end -->

## What is closed — do not re-propose without a new argument

Each rejected idea, with the number that rejected it. A negative result costs real work and stops
the next person repeating it; this list is where that value is stored.

<!-- example: begin -->

- **Equal weight as the better sizing.** Closed on the KN US Equity Core by 14.53% at a Sharpe of
  0.722, against 20.33% at 0.842, on the same names and dates.
- **The filter as a return-neutral drawdown shield.** Closed on the KN US Equity Core: the golden
  cross adds 0.60 points a year and 0.080 of Sharpe as well as 13.85 points of drawdown.
- **Attribution with each day's weights paired with that day's return.** Closed by Experiment 1's
  reconciliation. The pairing credits every book with the day's move its weights already hold, and
  it read the index 6.94 points a year above its own returns. Every pass pairs the close of t−1 with
  day t.
- **Ranking the whole universe by liquidity.** Closed by an earlier version's analyzer, on another
  index, where the rank across the whole panel read −0.104 at a year. On the KN US Equity Core the
  rank across every member reads +0.025 in the window and −0.072 before it, row 9 above.

<!-- example: end -->

### The uncomfortable one

The finding that qualifies the idea itself rather than a lever — the claim in `OBJECTIVE.md` that
turned out weaker than stated. Every honest project has one; write it here rather than letting it
sit in a findings file.

<!-- example: begin -->

**The last three years.** In 2023 to 2026 the same rule without the golden cross compounded at
51.85% for a Sharpe of 1.830, and the rule at 40.44% and 1.483. In the most concentrated,
momentum-led stretch of the window, the names the cross excluded rose fastest. The cross's whole
margin was earned in 2015 to 2022. Beside it, **nine tenths of the excess return is factor
exposure**, and the residual selection is 2.70 points over the window. The misaligned attribution
pass had put the idiosyncratic return at 61.02 points, more than four times the 13.84 that stands.
And the window was chosen after an earlier version's 2017–2026 result was heard: disclosed, and
counted.

<!-- example: end -->

## Open leads, ranked

The single highest-value run outstanding, and what it would settle. Then the next.

<!-- example: begin -->

1. **Paper days.** `Paper_Trading_1` is the only out-of-sample test this rule has. Its kill switch
   is read first on 2027-10-06, in [`Paper_Trading/BITACORA.md`](Paper_Trading/BITACORA.md).
2. **The 2023–2026 sub-period.** Whether the golden cross costs the most in a concentrated,
   momentum-led rally is a question for a new experiment, never a change to this one.
3. **The deflated Sharpe** of the rule against its 107 trials. Publishing the count is the minimum,
   not the answer.
4. **The shifted-entry timing arm**, not run by the gate written before the run, so timing skill is
   not separated from selection.
5. **The members FMP does not price** — 7.0% of the index's weight on the window's first day, none
   from 2023 — through a second provider, as a different universe.
6. **Carried from an earlier version, unanswered:** the eleven sector factor files, which carry no
   values; the last day of a delisted name, unaudited.
7. **The prior-close probe**, brought back into the experiment notebook: the golden cross flipped on
   sample dates must move nothing on those dates and move the day after.

<!-- example: end -->

## Excluded runs

Variants removed from the tables above rather than reported with a caveat. **A metric computed over
a truncated or rejected run does not belong in the same column as a complete one**, and excluding by
name with a reason is how that stays honest.

| Variant | Why |
| --- | --- |
| | what went wrong, how it was caught, and what now prevents it |

<!-- example: begin -->

| Variant | Why |
| --- | --- |
| The run's first attempt: 31 engine runs — the control over the window, its realistic-cost row and its three sub-periods; the rule's 2019–2022 and 2023–2026 sub-periods; five controls of the sweep, the 2% floor's among them, and the 2% floor setting; eighteen random books | Priced before the sell-at-t−1 rule. The engine refused the rule's own book on a 62-day gap in FMP's `AGN` file at a corporate event, and the owner's rule changed every book but two: the rule's and the control's 2023–2026 sub-periods came back identical, and the record reads them from this attempt's cache. Counted as trials; what was seen of them is listed in `JOURNAL_1.md` |
| The second run's attribution | The first cut's benchmark read an infinite return from `RAI`'s zero price, still in the index's holdings; no figure from it is quoted |
| The third run's attribution | Weights paired with the same day's return: the first cut's benchmark read 6.94 points a year above the index. Its figures are named in `JOURNAL_1.md` and `FINDINGS_1.md` as not the record |

Every engine run of the record was valued to the last day of its window.

<!-- example: end -->

## Known limitations

| # | Limitation | Effect |
| --- | --- | --- |
| 1 | **Nothing is out of sample** until a frozen book has days on paper after its freeze | Every number here is in-sample, and in-sample selection is what the deflation literature warns about |
| 2 | **A control arm differing in exactly one thing** — the same rule with one ingredient removed, on the rule's own rebalance dates — is missing from any experiment that claims a margin | Which lever earned that margin is inferred from per-lever rows, not measured |
| 3 | Classification buckets use today's labels, not point-in-time | Anything reclassified mid-window is misattributed before its move — the `current_*` prefix marks exactly this |
| 4 | Delisting exits use one day of hindsight | A position is sold on the last day it still has a fill price, knowable only the day after |
| 5 | Curator output is not reproducible across download dates | Dividend adjustment is computed from the present, so a re-pull rebases every adjusted column |
| 6 | The Deflated Sharpe Ratio has never been computed | The one number that would say whether a winner survives its own trial count |

<!-- example: begin -->

**Limitations 1, 2, 4 and 6 hold here, with qualifications.**

- **1.** Experiment 1 reached step 7 on 2026-10-06, and its paper days begin there. No rule, check
  or engine run of the experiment read a price after 2026-06-01.
- **2.** The control that differs in exactly one thing exists: the golden cross off, on the rule's
  own dates. With the equal-weight arm and the random books, it separates the filter, the sizing and
  the selection. What is missing is the shifted-entry timing arm, so timing is not separated from
  selection.
- **4.** The day of hindsight covers every exit before a price stops: a delisting, or a gap at a
  corporate event. A name is sold at t−1, the last day it is priced, which is knowable only the day
  after. It applies to every book alike, and the last row of a delisted name is unaudited.
- **6.** The deflated Sharpe of the rule against its 107 trials is not computed, and the sign-off
  was given knowing it.

Eight more, specific to this example:

| # | Limitation | Effect |
| --- | --- | --- |
| 7 | **Prices come from FMP alone**, this experiment's provider. A KN US Equity Core member FMP does not carry is dropped and counted in `Universe/Data_Issues.csv` | Lie 1 of `AGENTS.md`, accepted and quantified: the members FMP prices held 92.97% of the index's weight on 2015-01-02 and all of it from 2023; the first cut prices 94.1% of the index in 2015 and renormalises the rest |
| 8 | **The window was chosen after an earlier version's 2017–2026 result was heard** | A forking path, disclosed and counted beside the trial count; the data, not the owner, fixed the exact start, which fell on the owner's floor |
| 9 | **The index's holdings and returns files do not agree exactly** | Once aligned, the first cut's benchmark from the holdings reads 0.54 points a year above the returns file, inside the 1.0 tolerance |
| 10 | **The index files end 2026-08-14** | A paper day after it flags the input as stale and prices against `SPY` until KaxaNuk's Analytics Factory refreshes them |
| 11 | **Capacity is stated as a participation bound** | At 1% of a name's 63-day traded value the worst trade allows a $238.6 million book, the median $39.5 billion; a bound on participation, not a model of market impact |
| 12 | The eleven sector factor files carry no values | Sector attribution on the factor model reads zero, as it did for an earlier version |
| 13 | **Attribution points are daily returns summed**, not compounded | They compare within a table, not with a CAGR |
| 14 | **FMP's volume for `KLAC` is about ten times too high from 2026-05-13 to its 10-for-1 split of 2026-06-12** | Its traded value, the rule's score, is inflated over the window's last 13 trading days: `KLAC` re-entered the book on 2026-05-14 and reached 2.6% by 2026-06-01, from about 1.1%. Prices are right; found after the run and not corrected ([`FINDINGS_1.md`](Experiments/Experiment_1/FINDINGS_1.md), caveat 7) |

<!-- example: end -->

> **Under the bar in [`AGENTS.md`](AGENTS.md), most numbers above are a reason to run an experiment
> rather than a result.**
