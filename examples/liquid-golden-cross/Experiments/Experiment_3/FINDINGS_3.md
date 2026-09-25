# Findings — Experiment 3

> **Latest valuable results only.** This file is rewritten when a result changes, not appended to —
> the running history is in [`JOURNAL_3.md`](JOURNAL_3.md), and the hypothesis this tested is in
> [`BLUEPRINT_3.md`](BLUEPRINT_3.md).
>
> **[`../../RESULTS.md`](../../RESULTS.md) is compiled from this file.** When a finding here
> changes, change it here first, then update the summary.

## Status

**Not yet run.** When it has: one line saying whether the rule beat the benchmark and its control
by what the blueprint required, and whether it is a candidate for the gate in
`Paper_Trading/BITACORA.md` — a success is necessary for graduation, not sufficient. Then **the
claim it moved**: the claim of `OBJECTIVE.md` the blueprint named, and the status it reached — or
why it reached none.

<!-- example: begin -->

**Experiment 3 ran end to end on 2026-09-24, from a wiped working copy, and it does not
graduate.** The rule is momentum proper among the most traded: of the hundred most traded members
of the index, the twenty with the highest return over the twelve months before the latest one,
equally weighted, re-struck on the first trading day of each month. On its test window, 2002-07-30
to 2026-06-01, it earns **10.81% a year at a Sharpe of 0.436, against its control's 11.03% and
0.465 and the index's 10.99% and 0.568**. It trails its control by **0.22 points a year**, where
prediction 1 asked for 0.5 points more, and **the kill switch trips**: the rule is ahead of its
control on both Sharpe and CAGR in one of three sub-periods, 2017 to 2026. It is not a candidate
for the gate in `Paper_Trading/BITACORA.md`; the gate's rows are below anyway.

**The claim it moved: claim 5 of `OBJECTIVE.md`, momentum, moves from measured to falsified, for
this design, on this window.** The blueprint fixed that status for a failed prediction 1 or a
tripped kill switch, and both happened. Beside it, as the blueprint fixed: on 2002-07-30 to
2016-12-30 alone the rule trails its control by **2.84 points a year**, 3.78% against 6.62%; in the
third sub-period, 2017 to 2026, it leads by 4.46, 22.49% against 18.03%. The analyzer's rows 19 to
30, read before the blueprint, measured a signal; this is the first book built on it, and it does
not beat the same names without it.

**The success criteria `BLUEPRINT_3.md` set, each answered.**

| # | Criterion | State |
| --- | --- | --- |
| 1 | Prediction 1's margins over the control on the test window, net, at the headline cost row | **Not met.** Sharpe −0.0289 and CAGR −0.22 points, where +0.03 and +0.5 were required |
| 2 | The kill switch is silent | **Not met.** Both of its limbs fire: the whole-window margins, and one sub-period of three |
| 3 | The same verdict with every name filled at the close | **Met.** At the close the margins are −0.0329 and −0.30 points: not met either way |
| 4 | The rule beats the index on Sharpe | **Not met.** 0.4358 against 0.5682 |
| 5 | A run reproduced end to end from a wiped working copy, with the Sharadar names' Curator at its recorded commit | **Met, with the downloads kept.** The record is the run from a wiped working copy, and the working copy the rule was built in printed every figure the same. The copy kept the morning's raw downloads: caveat 5 says which |
| 6 | Trades on fewer days than it does not | **Met.** 288 rebalances in 5,998 trading days, and the invariant passed |
| 7 | Every prediction evaluated in this file | **Met.** Three rows below: two failed, one held |

**No rule or engine run of this experiment has read the months after 2026-06-01.** The notebook
cuts its panel there.

### The gate, row by row

Every row is evidenced from this file. **Nothing graduates**, and no book of this experiment is
frozen.

| # | Criterion | Verdict | Evidence |
| --- | --- | --- | --- |
| 1 | Beats the benchmarks **and its own control** | **Fails** | Sharpe 0.4358 against the index's 0.5682 and the control's 0.4647; CAGR 10.81% against 10.99% and 11.03%. It trails both, on both measures, and the verdict is the same with every name filled at the close |
| 2 | Idiosyncratic alpha in **both** layers | **Fails** | Over 2008-01-14 to 2026-06-01 the factor model leaves the rule 82.30 idiosyncratic points and its control 87.88: the ranking's share is −5.59. What the ranking adds is the momentum line, 44.78 points against 16.77. The first cut's alpha against the index is +121.27 points, of which selection +27.74 and interaction +95.22, per asset. The third pass has not been run, and 2002 to 2007 are not attributed |
| 3 | Survives perturbation; trial count published | **Fails** | The rule is ahead of its control on both Sharpe and CAGR in 3 of 10 cells, where the blueprint asked for eight; four cells could not be priced and count against it, and with all four ahead it would read seven. The trial count is published: fifty-four, with this experiment's 36 engine runs listed by role. The deflated figure was not computed |
| 4 | Costs and capacity modelled and stated | **Met, capacity as a participation bound** | Turnover, target to target: 3.25 times the book a year, and 26.9% one-way per rebalance on average. Costs are charged on the unadjusted price at two rows, the blueprint's setting 0.1 and a realistic 0.005, with 5 basis points of slippage, and reported net: $780,587.10 of commission and $180,071.26 of slippage at the headline row. Capacity, from the book, measured as Experiment 1's was: at 1%, $6,933,709 for the worst trade, $27,864,836 at the first percentile of trades, $92,928,116 at the median; at 5%, $34,668,547, $139,324,178 and $464,640,582. It bounds participation and does not model market impact, and which trade is the worst was not traced |
| 5 | Explicit sign-off | **Not sought** | Criteria 1 to 3 block it, and the kill switch had already tripped |

**No decision of the owner's on what follows is recorded.** Nothing in this file recommends a
design.

<!-- example: end -->

## The predictions, evaluated

**Every prediction in the blueprint gets a row, including the ones that were wrong.** A falsified
prediction is worth more than a correct one: it says something about the strategy that nobody knew,
and it cost one run to find out.

| # | Prediction | Outcome | What it changed |
| --- | --- | --- | --- |
| 1 | as written in the blueprint | confirmed or falsified, with the number | what is now understood differently |

<!-- example: begin -->

**Every prediction in the blueprint gets a row, including the ones that were wrong.** All three are
read net, at the headline cost row, over the test window, 2002-07-30 to 2026-06-01.

| # | Prediction | Outcome | What it changed |
| --- | --- | --- | --- |
| 1 | The rule beats its control, the pool's twenty most traded members with a momentum value on the rule's own dates, by at least 0.03 of Sharpe and 0.5 points a year of CAGR | **Failed.** Sharpe **−0.0289** and CAGR **−0.22 points**: 0.4358 and 10.81% against 0.4647 and 11.03%. The verdict is the same with every fill at the close. At the realistic cost row the CAGR margin turns to +1.23 points and the Sharpe margin to +0.0293, still short of 0.03 | The ranking buys the momentum factor and no selection: over 2008 to 2026 its momentum line is 44.78 points against the control's 16.77, and its idiosyncratic points 82.30 against 87.88. Net of a monthly re-strike at 3.25 times the book a year, against the control's 0.91, the factor it buys does not pay for its trading at the headline row: the rule leads by 4.46 points a year on 2017 to 2026 and trails by 2.84 on 2002 to 2016 |
| 2 | The rule beats the KN US Equity 600 on Sharpe over the test window | **Failed.** 0.4358 against the index's 0.5682; CAGR 10.81% against 10.99% | The blueprint wrote this as a lead, not a licensed prediction. Twenty names chosen on a year's return are more volatile than six hundred, 24.80% against 19.34%, and earned less than the index, so the index is the harder bar on both measures |
| 3 | From 2009-03-02 to 2009-12-31 the rule trails its control on return | **Held.** The rule +29.14%, the control +65.93%, from the engine's daily series | Nothing read said how the long leg alone fared in the 2009 reversal; now it is measured here. Holding the previous year's winners into the rebound cost the rule 36.8 points against the most traded names in ten months. The crash both notes describe comes from the short leg, which this book does not hold, and the long leg alone still paid for it |

Two failed, one held. **The first failure taught the most.** The signal the analyzer measured is
there, and step 6 finds it: the rule carries far more momentum than its control. What it does not
do is earn, net, more than the same liquid names without it, on the whole window or in two of its
three sub-periods. The blueprint named the reasons against it — the long leg alone, a monthly
re-strike, costs the review does not study — and they are what the run shows.

### The kill switch

**It trips, on both limbs.** The blueprint fixed one condition for the whole experiment: prediction
1's margins over the test window, and the rule ahead of its control on both Sharpe and CAGR in at
least two of three sub-periods. Each sub-period was priced by the engine as a window of its own,
the book built from its first day the way the headline's was, and its control held to that rule's
rebalance dates.

| Sub-period | Trading days | Rebalances | Sharpe, the rule | Sharpe, the control | CAGR, the rule | CAGR, the control | Ahead on both |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1, 2002-07-30 to 2008-12-31 | 1,619 | 78 | −0.113 | −0.049 | −3.17% | −1.29% | no |
| 2, 2009-01-02 to 2016-12-30 | 2,014 | 96 | 0.488 | 0.639 | 9.60% | 13.17% | no |
| 3, 2017-01-03 to 2026-06-01 | 2,365 | 114 | 0.852 | 0.744 | 22.49% | 18.03% | yes |

**One of three.** The rule lost more than its control through 2008, trailed it through the rebound
and the years after, and led it on 2017 to 2026, the window Experiment 1 ran on. The changes that
may not rescue it are the blueprint's: the members, the widened seed and the fifty-one exclusions;
the pool of a hundred and its tie-break; the momentum column, its 252-day lookback and its 21-day
skip; twenty names at equal weight; the monthly re-strike; the one-day lag; the providers and their
fills; the control; the benchmark; the costs and the 5% reserve; the window, the sub-periods and
prediction 1's margins; and the perturbation's cells and its threshold. None was moved after the
result.

<!-- example: end -->

## The book, priced by the engine

Record the date of the last full re-run from a wiped working copy, the engine version, and the
window. Then the book against every benchmark it reports against, and against the control its
blueprint names, on the rule's own rebalance dates: CAGR, volatility, Sharpe, Sortino, maximum
drawdown.

<!-- example: begin -->

**Run 2026-09-24, from 20:16 to 21:49, from a wiped working copy**: a clone of this repository at
the commit that holds the notebook, every output of the pipeline wiped and rebuilt from the curator
on, with the downloads caveat 5 names kept. The working copy the rule was built in ran the same
notebook at the same time and printed every figure the same. KaxaNuk Backtest Engine 0.66.0 and
Attribution Analysis 0.2.0; the FMP names from Data Curator 0.50.0 and the Sharadar names from its
`issues/31` branch at commit `8b54c2f`, built as 0.49.1. The notebook reached the end of its Verify
section. The window asked of the engine is **2002-07-30 to 2026-06-01**, 5,998 trading days, and
every run the engine priced valued at least 99% of its own window's trading days. Costs are the
blueprint's: the commission setting 0.1, 5 basis points of slippage and a **5% cash reserve**, on
$1,000,000. Results are net.

| Book | CAGR | Volatility | Sharpe | Max drawdown | Alpha | Commissions | Slippage | Rebalances |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **The rule** | **10.81%** | 24.80% | **0.4358** | −65.57% | −0.18% | $780,587.10 | $180,071.26 | 288 |
| The control, without the ranking | 11.03% | 23.73% | 0.4647 | −66.55% | 0.03% | $350,769.30 | $91,366.46 | 288 |
| The rule, realistic costs | 13.00% | 24.74% | 0.5253 | −64.82% | 2.00% | $52,392.05 | $267,667.30 | 288 |
| The control, realistic costs | 11.76% | 23.71% | 0.4960 | −65.73% | 0.77% | $19,510.88 | $104,453.64 | 288 |
| The KN600 index | 10.99% | 19.34% | 0.5682 | −55.37% | — | — | — | — |
| The null, the whole pool | 9.38% | 20.17% | 0.4651 | −61.56% | −1.61% | $292,971.20 | $62,026.75 | 288 |

The rule minus its control: **Sharpe −0.0289, CAGR −0.22 points**. Beta to the index, from the
engine's daily series: **the rule 1.084, the control 1.180**. The notebook prints neither Sortino
nor the information ratio, although the engine's report carries both; no figure for either is
quoted here. The control and the null traded on the rule's 288 dates and on no other. The index row
is the rule run's benchmark.

**The null is description, never evidence.** It holds the whole pool, a hundredth each, and earned
9.38% at a Sharpe of 0.4651: the most traded hundred, equally weighted, trailed the index on return
and matched the control on Sharpe. Its weight file dropped `WCOEQ`, WorldCom, held on the first
rebalance with no price anywhere in the window, as `JOURNAL_3.md` records; that weight sat in cash
for a month.

**The control with young listings is the control.** It struck a name with no momentum value in
none of 288 rebalances, so its weights, and every figure the engine returned for it, equal the
control's. The owner's restriction, that the control take only members with a momentum value, did
not change the book.

### The fill convention, checked

Sharadar publishes no VWAP, so its names fill at the day's close, which is also their mark; every
other name fills at the day's VWAP. The blueprint made the experiment's pass depend on the verdict
not changing when every name is filled the same way.

| Book, every fill at the close | CAGR | Volatility | Sharpe | Max drawdown | Commissions | Slippage |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| The rule | 10.80% | 24.82% | 0.4349 | −65.94% | $775,941.40 | $179,219.94 |
| The control | 11.10% | 23.72% | 0.4677 | −66.10% | $354,475.20 | $92,764.88 |

**The same verdict.** At the close the margins are −0.0329 of Sharpe and −0.30 points of CAGR,
against −0.0289 and −0.22 with the two conventions mixed.

### The realistic cost row

At the setting 0.005 the rule earns 13.00% at a Sharpe of 0.5253, and its control 11.76% at
0.4960. **The cost row decides the sign of the CAGR margin**: +1.23 points there, −0.22 at the
headline. The Sharpe margin there, +0.0293, still falls short of 0.03, and the rule's Sharpe is
still below the index's 0.5682. Every verdict is read at the headline row, as the blueprint fixed,
and the commission setting is on its list of changes that may not rescue it. What the row shows is
how much of this book's shortfall is trading: at the headline setting the rule paid $780,587.10 of
commission against the control's $350,769.30, and at the realistic one $52,392.05 against
$19,510.88.

### 2002 to 2016, described

**Description, never evidence.** The owner asked for 2002 to 2016 and 2017 to 2026; the blueprint
made them one window, and priced his first as a window of its own. His second is sub-period 3.

| Book, 2002-07-30 to 2016-12-30 | CAGR | Volatility | Sharpe | Max drawdown | Alpha | Rebalances |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| The rule | 3.78% | 23.70% | 0.1596 | −65.57% | −4.79% | 174 |
| The control | 6.62% | 23.38% | 0.2833 | −66.55% | −1.95% | 174 |

The rule minus its control on these years: **Sharpe −0.1237, CAGR −2.84 points**, over 3,633
trading days. Experiment 2's control, the same twenty most traded on that rule's own dates, earned
5.87% over the same window.

<!-- example: end -->

## What the benchmark actually is, structurally

Rebalance frequency, turnover, holdings, concentration, invested share, and any structural tilt —
each with a reading of what a bad value would have meant.

<!-- example: begin -->

**The panel, the exclusions and the start, section 1.** The panel read to 2026-06-01 holds 6,390
dates by 1,436 positions in the wiped copy and 1,437 in the working copy, from a seed of 1,500
identifiers, 712 of them served by Sharadar, with the index's membership known from 2000-01-03 to
2026-08-14. The working copy excludes fifty-one identifiers by name, the ones `JOURNAL_3.md`
recorded before the rule; the wiped copy excludes the same fifty-one and `MIC`, caveat 5. The
priced members hold 99.71% of the index's weight at the lowest inside the test, on 2003-09-02, and
no date falls below 95%.

**The book, sections 2 and 3.** Every invariant of section 2.1 passed, twenty-three in all: seven
on each of the rule, the control and the null, and one on each of the rule and the control that
every name struck in had a momentum value at the prior close. The rule's weight file holds 376
identifiers by 288 rebalances, every column summing to one, with the cash proxy, `SHY`, at 0.000 on
every date: no slot went unfilled.

Read in section 3 from each book's targets held forward between rebalances: its shape, not its
return.

| Property | The rule | The control | What a bad value would have meant |
| --- | --- | --- | --- |
| Rebalances | 288 in the window, 12.1 a year | the same 288 | A rule trading on most days would be a cost question, not an alpha one. The invariant that it trades on fewer days than it does not passed |
| Mean one-way turnover per rebalance | 26.9% | 7.6% | The rule replaces about five of its twenty names a month; the most traded members change little between the same dates. The null turned over 5.4% |
| Annual turnover, target to target | 3.25 times the book | 0.91 | The engine's realised turnover was not read. The rule's turnover is what its $780,587.10 of commission is charged on |
| Mean invested share | 100.0%, lowest 100.0% | 100.0%, lowest 100.0% | A low figure would mean slots left empty. `SHY` holds any slot no name fills, and none was |
| Mean holdings | 20.0 | 20.0 | Equal by construction; a gap would mean hidden concentration |
| Mean weight in Sharadar names | 17.1% | 5.3% | The dead names fill at the close; the fill check prices what that does. The null held 14.5% |

**Capacity, criterion 4 of the gate**, measured as Experiment 1's was: each of the rule's trades
set against the name's 63-day average traded value on the day, and read as the largest book at
which that trade takes no more than the stated share of it.

| Share of a day's traded value | Worst trade | 1st percentile of trades | Median trade |
| --- | ---: | ---: | ---: |
| 1% | $6,933,709 | $27,864,836 | $92,928,116 |
| 5% | $34,668,547 | $139,324,178 | $464,640,582 |

**The worst trade binds.** At 1% of a day's traded value no trade of the rule's exceeds its share
while the book is at most $6,933,709. Which trade is the worst was not traced. It bounds
participation and does not model market impact.

### Watched, but not predicted

The blueprint named these and predicted none of them.

- **The betas, side by side.** The rule 1.084, the control 1.180, from the engine's daily series
  against the index. The rule is the calmer book on beta and the more volatile on its own, 24.80%
  against 23.73%.
- **The momentum line step 6 assigns each, and what is left.** 44.78 points to the rule, 16.77 to
  the control, over 2008 to 2026; the idiosyncratic points, 82.30 and 87.88. *Attribution* below.
- **Turnover.** 3.25 times the book a year and 26.9% per re-strike, against the control's 0.91
  and 7.6%. The names changed each month were not counted apart from the turnover.
- **The weight in `SHY`.** None: the cash proxy's target is 0.000 on every date for both books.
- **The share of each book's weight in Sharadar names**, from the engine's daily weights: the
  rule's mean 16.0%, highest 58.0%; the control's mean 5.0%, highest 24.2%.
- **The control with young listings beside the control.** Identical: it held a member with no
  momentum value on no rebalance, so the gap between the two is zero.
- **The 2002-to-2016 window's margin**: −2.84 points a year and −0.1237 of Sharpe, above.
- **The null beside both**: 9.38% at 0.4651, above.
- **Every name held on its last priced day.** The notebook's own check read each name's last price
  inside the panel, which ends on the test window's last day, so it listed the twenty names each
  book held on 2026-06-01 and none that left the market: caveat 6. The engine's log is the record.
  In the rule's run it sold thirty-one names at their last price, from `PHA` on 2003-04-15 to `XLNX`
  on 2022-02-11, and ignored the rule's target of 0.05 in `ROH` on its last priced day, 2009-04-01,
  leaving that capital in cash. The control's run names none. The null's names fifty-nine.

<!-- example: end -->

## The trial count

How many variants were ranked to reach the book above, and every run excluded by name with its
reason. `RESULTS.md` compiles this: a reader cannot discount a best-of-N result without knowing N,
and the graduation sign-off says whether the deflated figure was also computed.

<!-- example: begin -->

### The perturbation, criterion 3

Ten cells, fixed in the blueprint, one setting at a time around the rule, each priced beside its
own control, which takes the cell's pool, book size, frequency and delay and trades on the cell's
own dates. Net, at the headline cost row, over the test window. **The rule itself** — a hundred in
the pool, twenty names, twelve months less one, monthly, on time — reads Sharpe 0.436, −0.029 over
its control and −0.219 points of CAGR, on 288 rebalances.

| Cell | Sharpe | Sharpe over control | CAGR over control, points | Rebalances |
| --- | ---: | ---: | ---: | ---: |
| Lookback 6 months, skipping 1 | not priced | — | — | — |
| Lookback 9 months, skipping 1 | 0.349 | −0.116 | −2.575 | 288 |
| 12 months, no skip | 0.480 | +0.015 | +0.626 | 288 |
| Pool 50 | 0.500 | +0.035 | +0.147 | 288 |
| Pool 150 | not priced | — | — | — |
| Pool 200 | not priced | — | — | — |
| Book size 10 | not priced | — | — | — |
| Book size 30 | 0.426 | −0.025 | −0.293 | 288 |
| Quarterly | 0.455 | +0.007 | +0.908 | 96 |
| Acted on 5 days late | 0.435 | −0.054 | −0.716 | 287 |

**Four cells' rules could not be priced, and each counts against the rule**, as the blueprint
fixed; every control priced.

- **Lookback 6 months**: the engine stopped valuing the book after 2003-02-28, at a cash error of
  −$16,557.91 on 2003-03-03, a full re-strike overdrawing the 5% reserve.
- **Book size 10**: the same, after 2003-08-29, at a cash error of −$19,025.14 on 2003-09-02.
- **Pool 150 and pool 200**: refused. Each book held `VMW` into 2023-12-01, a month start its file
  has no price for: VMware last traded on 2023-11-21, and its file repeats that bar on 2023-11-24,
  2023-12-13 and 2023-12-15, so the engine does not read it as delisted.

**Each curve's direction, as the blueprint asked:**

- **The lookback.** The margins rise with the lookback: −0.116 and −2.575 at nine months, −0.029
  and −0.219 at the rule's twelve less one, +0.015 and +0.626 at twelve with no skip. Leaving the
  latest month out, which the review's definition does for its reversal, cost this pool return.
- **The pool.** Better narrower: +0.035 and +0.147 at fifty, below zero at the rule's hundred;
  one hundred and fifty and two hundred could not be priced.
- **The book size.** Thirty names trail as twenty do, −0.025 and −0.293; ten could not be priced.
- **The frequency.** Quarterly re-strikes lead on both, +0.007 and +0.908, on a third of the
  rebalances: less trading, less cost, at the headline row.
- **The delay.** Acting 5 days late widens both shortfalls, to −0.054 and −0.716: what the ranking
  forecasts loses value within a week, as a signal with a short half-life would.

**Criterion 3 is read as failed, on its own rule**: the rule is ahead of its control on both
Sharpe and CAGR in **3 of 10 cells** — twelve months with no skip, the pool of fifty and the
quarterly re-strike — and the blueprint asked for eight. Had all four unpriced cells priced and led,
the count would be seven. The best cell is never the answer: picking one after the result is a new
experiment, and one more trial.

### The count

**Fifty-four trials, the count the blueprint fixed**: the forty-three `RESULTS.md` published, then
this experiment's rule and its ten cells. The owner's earlier test outside this repository is
counted as one because its variants were not kept, so the count is a lower bound.

**Thirty-six engine runs in this experiment's notebook**: thirty-two priced, every one valued on at
least 99% of its window's trading days, and four not priced, each named with its reason. By role:

| Role | Engine runs | Counted as |
| --- | ---: | --- |
| The rule | 1 | a trial |
| The control | 1 | a diagnostic |
| The control with young listings | 1 | a diagnostic, identical to the control |
| The null, the whole pool | 1 | description, never evidence |
| 2002 to 2016: the rule and its control | 2 | description, never evidence |
| The rule and the control at realistic costs | 2 | diagnostics: the same books at another cost row |
| The rule and the control with every fill at the close | 2 | diagnostics: the fill convention |
| The sub-periods: the rule and its control in each of three | 6 | diagnostics: the kill switch |
| The perturbation: ten cells and their ten controls | 20 | ten trials and ten diagnostics; four rules not priced |
| **All** | **36** | |

**The Verify section, section 8, raised nothing.** 30 checks on the books and the weight file: the
twenty-three invariants of section 2.1, and seven on the file read back from disk and the dates the
control and the null trade on. 70 on the runs: two window checks on each of the 32 priced engine
runs, 64; one on each of the four not priced, that it is named with its reason; and two on the
attribution, that its window lies inside the backtest's and that both books have an idiosyncratic
figure.

**No variant was selected on its result.** Every book above was fixed in `BLUEPRINT_3.md` or in the
notebook before the run. The deflated Sharpe was not computed.

**Three earlier runs, each by name, none excluded: each is superseded.**

- **The first run, 18:26 to 18:52, in the working copy.** It stopped at the null, which the engine
  refused over `WCOEQ`; nothing after it ran. The rule and the control had printed the figures
  reported here, and no verdict was drawn from them. `JOURNAL_3.md` records the fix.
- **The second run, 18:56 to 20:13 in the working copy, and the wiped copy's first, 19:14 to
  20:09.** Both stopped at the pool 150 cell, where the notebook raised at the engine's refusal
  instead of recording it. Every engine figure the working copy's printed equals the run reported
  here; the wiped copy's wrote no notebook when it raised, and its figures were not read.
  `JOURNAL_3.md` records the change: a run the engine cannot price is named and counted against the
  rule, and the verdict cell names claim 5.

<!-- example: end -->

## Attribution — is this the signal, or a factor exposure wearing its name?

Brinson-Fachler: allocation, selection, interaction. The factor model: factor against idiosyncratic.
State the window, which is bound by the supplied files' coverage and is usually shorter than the
backtest.

**What it settles**, and **what it does not** — naming the counterfactual book that would settle
what is left: the same holdings with the signal off, positions equalised, a random draw at the same
sizes, entry dates shifted.

<!-- example: begin -->

**Window: 2008-01-14 to 2026-06-01**, bound by the factor files' first date; the backtest runs from
2002-07-30. **Sub-period 1 before 2008 lies outside it**, and with it the years in which the rule
lost most against its control. The book is read daily as the engine held it, widened to the whole
index at zero weight, with the excluded names dropped from both. 1,350 of the 1,351 identifiers the
two books and the index name have a price series here. The desk's files were read from the
Analytics Factory's folders.

**First cut, Brinson-Fachler**, the rule against the index, summed daily over the window, in
percentage points: alpha **+121.27**, of which allocation **−1.69**, selection **+27.74** and
interaction **+95.22**. This library's first cut is per asset, not per group, so each line is about
the weighting of names, not of sectors: read it as "the weighting did it".

**Second layer, the factor model**, on the rule and on its control, in percentage points summed
over the window:

| Source | The rule | The control |
| --- | ---: | ---: |
| Market | 90.79 | 91.96 |
| Beta | 16.69 | 14.70 |
| Momentum | 44.78 | 16.77 |
| Residual volatility | 2.94 | 5.55 |
| Size | −5.17 | −0.58 |
| Value | 3.34 | 3.16 |
| The eleven sector factors | 0.00 each | 0.00 each |
| **All factors** | **153.36** | **131.56** |
| **Idiosyncratic** | **82.30** | **87.88** |
| **Excess return** | **235.66** | **219.44** |

**What it settles.**

- **The ranking is a momentum tilt.** The rule's momentum line is 44.78 points against its
  control's 16.77: the ranking adds 28.01 points of the factor it is named after. The other lines
  take back 6.20 — size −4.59, residual volatility −2.61, market −1.17, beta +1.99, value +0.18 —
  and the idiosyncratic line 5.59, which leaves the 16.22 points of excess return the rule earns
  over its control on these years.
- **The ranking subtracts idiosyncratic return.** The control keeps 87.88 points the factor model
  cannot explain; the rule, which differs from it in the ranking alone, keeps 82.30. **The
  ranking's share is −5.59 points** over the eighteen years. Criterion 2 of the gate asks for
  idiosyncratic alpha from the signal, and the signal takes some away.
- **The honest product is the factor.** A book whose edge over its control is the momentum line is
  a momentum fund with a liquidity screen. The key risk the blueprint named, that the honest product
  may be a cheaper momentum fund, is what step 6 finds.

**What it does not settle.** The third pass, Brinson-Fachler on the residual returns, has not been
run. The attribution does not reach 2002 to 2007, where the rule trailed its control most. The
sector lines read 0.00 for both books, so the crowding into a year's leading sector the blueprint
named is not measured. Of the counterfactuals `AGENTS.md` names, the blueprint declared only the
signal off, which is the control. No random books were priced, so there is no baseline for either
book's idiosyncratic points beyond each other.

<!-- example: end -->

## What is open, ranked

The single highest-value run outstanding, and what it would settle.

<!-- example: begin -->

**None of these can turn the verdict**: the rule trails its control over the window and trips its
kill switch, and had all four unpriced cells led, criterion 3 would still read seven of ten. They
bear on how it is read. What follows it is the owner's to decide.

1. **Repeated bars, a data check nobody wrote.** Nine FMP files end in a run of bars repeating
   their last distinct one inside the test window: `CSC`, `ABMD`, `ATVI`, `VMW`, `SGEN`, `SRCL`,
   `ZIONO`, `CMA` and `SNCR`, `CSC`'s from 2017-04-03 to 2021-09-10. Two cells here could not be
   priced because of one of them. A check at the curator or the universe stage, fixed in a later
   blueprint before its run, would end each at its last distinct bar; which books of any experiment
   held one of the nine across a repeated bar is uncounted. Highest value.
2. **The reading this blueprint did not have.** The researcher's library holds Daniel & Moskowitz
   (2013), with a warning above the risk-based-explanations bullet of its Paleologo chapter 5 note:
   all fifteen of the worst momentum months followed a negative two-year market return. The copy
   carried into `Bibliotheca/` does not have that warning, and the blueprint named neither the
   paper nor the market state. Prediction 3 held without it; a note on it is the reading before any
   momentum experiment that follows.
3. **The cost row.** The rule's CAGR margin is −0.22 points at the setting 0.1 and +1.23 at 0.005,
   and neither setting was measured from an executable commission schedule for this book. A later
   blueprint that fixes its cost row from one, before its run, would say which describes the book.
4. **The check for names held on their last priced day.** It reads the panel's last day as a last
   price, so here it listed the names held at the window's end and none of the thirty-one the
   engine sold. It should skip a name whose last price is the window's last day.
5. **Attribution before 2008, and the third pass.** Factor files reaching back to 2002 would
   attribute sub-period 1, where the rule lost most; the residual pass has not been run for any
   experiment.

<!-- example: end -->

## Caveats

| # | Caveat | Effect |
| --- | --- | --- |
| 1 | what a reader must know before quoting a number above | what it does to that number |

<!-- example: begin -->

| # | Caveat | Effect |
| --- | --- | --- |
| 1 | **The dead names fill at the close.** Sharadar publishes no VWAP, so for its names the fill is the close, which is also the mark; every other name fills at the day's VWAP. The rule held a mean of 16.0% of its weight in Sharadar names, up to 58.0%, and the control 5.0%, up to 24.2% | The fill check prices both books with every name at the close: the margins move from −0.0289 and −0.22 to −0.0329 and −0.30, and the verdict does not change |
| 2 | **Two Curator versions.** The Sharadar names come from the Data Curator's `issues/31` branch at commit `8b54c2f`, built as 0.49.1, the only version with the Sharadar provider; every other name from 0.50.0 | As in Experiment 2: the mark agrees between providers where both carry a name, the fill does not, and caveat 1's check prices the difference |
| 3 | **Repeated bars in nine FMP files**, `VMW`'s after a gap: the file repeats VMware's last bar of 2023-11-21 on 2023-11-24, 2023-12-13 and 2023-12-15. The engine carried its last price across the gap in every run that loaded it, and refused the two runs that held it on 2023-12-01 | Two cells are not priced and count against the rule. No price file was changed and no name excluded: the exclusions stay the fifty-one. A book that held one of the nine across a repeated bar without a rebalance there was valued at a flat price until it sold |
| 4 | **Four cells not priced**: lookback 6 months and book size 10, which overdrew the reserve in 2003, and pools 150 and 200, refused over `VMW` | Criterion 3 counts each against the rule, as the blueprint fixed; all four led would read seven of ten, short of eight either way |
| 5 | **The wiped copy kept its raw downloads.** Its FMP files had been downloaded fresh through 2026-06-01, in the same clone, earlier on 2026-09-24 for Experiment 1's reproduction, and its Sharadar names were re-curated through the branch from the bulk tables that morning's fetch had cached. Every later stage was wiped and rebuilt. That download lacks `MIC`, which the working copy's refreshed download carries from 2026-06-26, after the window | The two copies print every figure the same. `MIC` is excluded by name in the wiped copy, 52 names, and has no price inside the window in the working copy, 51: neither book could hold it in either |
| 6 | **Delisting exits use one day of hindsight, and the notebook's check reads the window's end.** The engine sold thirty-one of the rule's names at their last price and ignored its target in `ROH` on its last priced day; the check listed instead the twenty names each book held on 2026-06-01, where the panel ends | The engine's exit at the last price spares whichever book holds a failing name to the end, here the rule far more than the control, which the log names none for. Whether each left the market by failure or by acquisition was not checked, so the direction of the effect on the rule's figures was not measured |
| 7 | **Costs are the blueprint's row**, the commission setting 0.1: $780,587.10 on the rule over the window, against the control's $350,769.30, with 5 basis points of slippage and a 5% cash reserve | Every verdict is read there. At the realistic row, 0.005, the rule leads its control by 1.23 points a year and +0.0293 of Sharpe, short of prediction 1's 0.03, and its Sharpe stays below the index's |
| 8 | **The attribution window starts on 2008-01-14** | 2002 to 2007 are not attributed; the idiosyncratic figures describe 2008 to 2026 alone |
| 9 | **The desk's eleven sector factor lines read 0.00** | A sector tilt, the concentration the blueprint named, is not separated from the other lines |
| 10 | **These years and this signal are not unseen.** The analyzer measured `r_momentum_12_1` on both halves of the window before the blueprint, and step 6 had charged Experiment 1's books with momentum on 2017 to 2026 before the owner chose it | The test is of a book, not of the signal out of sample, as the blueprint said. Only the rule against its own control met these years unseen |
| 11 | **Fifty-four trials across three experiments**, on one universe whose years every experiment has read | A pass here would have been the best of fifty-four; the deflated Sharpe has never been computed |
| 12 | **The blueprint did not read Daniel & Moskowitz (2013)**, which the researcher's library holds, with a warning its Paleologo chapter 5 note carries and the strategy's copy does not | Prediction 3, the 2009 rebound, was written from the review and Paleologo alone, and held; the market-state condition that paper names was not part of any prediction |

<!-- example: end -->
