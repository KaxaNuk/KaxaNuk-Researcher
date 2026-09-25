# Findings — Experiment 2

> **Latest valuable results only.** This file is rewritten when a result changes, not appended to —
> the running history is in [`JOURNAL_2.md`](JOURNAL_2.md), and the hypothesis this tested is in
> [`BLUEPRINT_2.md`](BLUEPRINT_2.md).
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

**Experiment 2 ran end to end on 2026-09-24, and it does not graduate.** The rule is Experiment 1's
diagnostic arm, its rules unchanged, at a 5% cash reserve where the arm ran at 2%: the twenty most
traded members of the index above their 50/200 cross, the whole set re-equalised only on a day it
moves by three names or more. On its test window, 2002-07-30 to 2016-12-30, it earns **4.23% a year
at a Sharpe of 0.234, against its control's 5.87% and 0.256 and the index's 8.57% and 0.438**. It
trails its control by **1.64 points a year**, where prediction 1 asked for 0.5 points more, and
**the kill switch trips**: the rule is ahead of its control on both Sharpe and CAGR in none of the
three sub-periods. It is not a candidate for the gate in `Paper_Trading/BITACORA.md`; the gate's
rows are below anyway.

**The claim it moved: claim 1 of `OBJECTIVE.md`, the signal, stays falsified, now on two windows.**
The blueprint left no third status, and none is claimed. Beside it, as the blueprint fixed: on 2017
to 2026, the window the design was found on, the same rule priced on this panel trails its own
control too, by 0.0148 of Sharpe and **1.46 points a year**. It is the first time this design has
been priced against its own control, on any window. The two earlier falsifications stand: the first
design lost 1.12 points a year to its control, and the second design 0.86
(`../Experiment_1/FINDINGS_1.md`).

**The success criteria `BLUEPRINT_2.md` set, each answered.**

| # | Criterion | State |
| --- | --- | --- |
| 1 | Prediction 1's margins over the control on the test window, net, at the headline cost row | **Not met.** Sharpe −0.0216 and CAGR −1.64 points, where +0.03 and +0.5 were required |
| 2 | The kill switch is silent | **Not met.** Both of its limbs fire: the whole-window margins, and none of three sub-periods |
| 3 | The same verdict under both fill conventions | **Met.** With every name filled at the close the margins are −0.0202 and −1.63 points: not met either way |
| 4 | The rule beats the index on Sharpe | **Not met.** 0.2340 against 0.4383 |
| 5 | A run reproduced from a wiped working copy, with the Curator branch at its recorded commit | **Met, with the downloads kept.** A wiped working copy, run on 2026-09-24 from 21:49 to 22:28, printed every figure of the run of 12:38; it kept the morning's raw downloads, caveat 5 |
| 6 | Trades on fewer days than it does not | **Met.** 109 rebalances in 3,633 trading days, and the invariant passed |
| 7 | Every prediction evaluated in this file | **Met.** Three rows below: two failed, one held narrowly |

**No rule or engine run of this experiment has read the months after 2026-06-01.** The notebook
cuts its panel there, and the window the design was found on ends there.

### The gate, row by row

Every row is evidenced from this file. **Nothing graduates**, and no book of this experiment is
frozen.

| # | Criterion | Verdict | Evidence |
| --- | --- | --- | --- |
| 1 | Beats the benchmarks **and its own control** | **Fails** | Sharpe 0.2340 against the index's 0.4383 and the control's 0.2556; CAGR 4.23% against 8.57% and 5.87%. It trails both, on both measures |
| 2 | Idiosyncratic alpha in **both** layers | **Fails** | Over 2008-01-14 to 2016-12-30 the factor model leaves the rule −7.93 idiosyncratic points and its control +30.24: the cross's share is −38.17. The first cut's alpha against the index is −42.29 points, of which selection +6.33 and interaction −48.84, per asset. The third pass has not been run; it would split a negative residual, not reverse it |
| 3 | Survives perturbation; trial count published | **Fails** | The rule is ahead of its control on both Sharpe and CAGR in 1 of 10 cells, where the blueprint asked for eight. The trial count is published: forty-three, with this experiment's 34 engine runs listed by role. The deflated figure was not computed |
| 4 | Costs and capacity modelled and stated | **Met, capacity as a participation bound** | Turnover, target to target: 1.84 times the book a year, and 24.3% one-way per rebalance on average. Costs are charged on the unadjusted price at two rows, the blueprint's setting 0.1 and a realistic 0.005, with 5 basis points of slippage, and reported net: $265,535.20 of commission and $32,182.15 of slippage at the headline row. Capacity, from the book, as the largest book at which a trade takes no more than a share of the name's 63-day average traded value: at 1%, $3,851,439 for the worst trade, $7,019,368 at the first percentile of trades, $106,111,907 at the median; at 5%, $19,257,197, $35,096,840 and $530,559,534. It bounds participation and does not model market impact, and which trade is the worst was not traced |
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
read net, at the headline cost row, over the test window, 2002-07-30 to 2016-12-30.

| # | Prediction | Outcome | What it changed |
| --- | --- | --- | --- |
| 1 | The rule beats its control, the same twenty most traded members without the cross on the rule's own rebalance dates, by at least 0.03 of Sharpe and 0.5 points a year of CAGR | **Failed.** Sharpe **−0.0216** and CAGR **−1.64 points**, both on the wrong side of zero: 0.2340 and 4.23% against 0.2556 and 5.87%. The verdict is the same with every fill at the close, and at the realistic cost row, where the Sharpe margin is +0.0397 and the CAGR margin −0.69 points | The cross earns no return over its control at twenty names on years the design was not chosen on, and it earned none on the years it was: −1.46 points there. What it buys is a calmer book: volatility 18.08% against 22.97%, a maximum drawdown of −53.32% against −65.43%, a beta of 0.841 against 1.141 |
| 2 | The rule beats the KN US Equity 600 on Sharpe over the test window | **Failed.** 0.2340 against the index's 0.4383; CAGR 4.23% against 8.57% | The arm's lead over the index on 2017 to 2026 did not carry to the earlier years. The first design's long window, with its negative alpha, pointed this way, and the rule's alpha against the index here is −4.34% |
| 3 | Over 2007-01-03 to 2009-12-31, the deepest fall of the rule's daily value, peak and trough both inside those dates, is shallower than the index's measured the same way | **Held, narrowly.** −53.32% against −53.97%, from the engine's daily series | The lower volatility the analyzer measured above the cross shows as a book less volatile than the index, 18.08% against 19.56%, and barely as a shallower fall. The slow exit kept the book invested through 2008: a mean of 0.6% in `SHY` over 2008 and 2009 |

Two failed, one held by less than a point. **The first failure taught the most.** The design was
chosen for its lead over the fast exit on 2017 to 2026, and that lead had never been set against
the same names without the cross. Set against them, it trails on the years it was found on and on
the fourteen years before them. The blueprint wrote the lead down as a lead, not as a licensed
prediction, and the run treated it as one.

### The kill switch

**It trips, on both limbs.** The blueprint fixed one condition for the whole experiment: prediction
1's margins over the test window, and the rule ahead of its control on both Sharpe and CAGR in at
least two of three sub-periods. Each sub-period was priced by the engine as a window of its own,
the book built from its first day the way the headline's was, and its control held to that rule's
rebalance dates.

| Sub-period | Trading days | Rebalances | Sharpe, the rule | Sharpe, the control | CAGR, the rule | CAGR, the control | Ahead on both |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1, 2002-07-30 to 2006-12-29 | 1,115 | 27 | 0.511 | 0.686 | 7.99% | 12.21% | no |
| 2, 2007-01-03 to 2011-12-30 | 1,260 | 63 | −0.243 | −0.206 | −5.77% | −6.63% | no: ahead on CAGR only |
| 3, 2012-01-03 to 2016-12-30 | 1,258 | 23 | 0.911 | 0.875 | 11.72% | 12.50% | no: ahead on Sharpe only |

**None of three.** In sub-period 2, which holds 2008, the rule lost less than its control and still
trailed it on Sharpe; in sub-period 3 it led on Sharpe and trailed on CAGR. The changes that may not
rescue it are the blueprint's: the twenty names, the 15% band, the 50 and 200-day pair, the 63-day
ranking window, the one-day lag, the test window, its coverage rule and its 95%, the sub-periods,
the exclusions and their tests, which provider serves each name and how its fill is made, the two
Curator versions, the costs and the 5% cash reserve, and the perturbation's cells and its
threshold. None was moved after the result.

<!-- example: end -->

## The book, priced by the engine

Record the date of the last full re-run from a wiped working copy, the engine version, and the
window. Then the book against every benchmark it reports against, and against the control its
blueprint names, on the rule's own rebalance dates: CAGR, volatility, Sharpe, Sortino, maximum
drawdown.

<!-- example: begin -->

**Run 2026-09-24, from 12:38 to 13:34**, with KaxaNuk Backtest Engine 0.66.0 and Attribution
Analysis 0.2.0, the FMP names from Data Curator 0.50.0 and the Sharadar names from its `issues/31`
branch at commit `8b54c2f`, built as 0.49.1. It ran in the working copy the widened data and the
rule were built in, and **was reproduced from a wiped working copy the same day, from 21:49 to
22:28**, every figure the same. The notebook reached the end of its Verify section in both. The
window asked of the engine is **2002-07-30 to 2016-12-30**, 3,633 trading days, and every run over
it valued at least 99% of them. The rule's first rebalance, on 2002-07-30, holds only cash: the
one-day lag leaves it no set on the window's first day. Costs are the revised blueprint's: the
commission setting 0.1, which the engine charged at $0.10 a share — $73.40 on 734 shares of `BR1`,
sold at its last price in the rule's run — with 5 basis points of slippage and a **5% cash
reserve**, on $1,000,000. The blueprint's "about eight cents a share" is the first design's figure,
and this run did not re-measure it. Results are net.

| Book | CAGR | Volatility | Sharpe | Max drawdown | Alpha | Commissions | Slippage | Rebalances |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **The rule** | **4.23%** | 18.08% | **0.2340** | −53.32% | −4.34% | $265,535.20 | $32,182.15 | 109 |
| The control, without the cross | 5.87% | 22.97% | 0.2556 | −65.43% | −2.70% | $135,357.30 | $16,051.15 | 109 |
| The rule, realistic costs | 5.86% | 18.03% | 0.3251 | −50.90% | −2.71% | $14,898.49 | $36,398.02 | 109 |
| The control, realistic costs | 6.55% | 22.95% | 0.2854 | −64.71% | −2.02% | $7,115.60 | $16,954.92 | 109 |
| The KN600 index | 8.57% | 19.56% | 0.4383 | −55.37% | — | — | — | — |

The rule minus its control: **Sharpe −0.0216, CAGR −1.64 points**. Beta to the index, from the
engine's daily series: **the rule 0.841, the control 1.141**. The notebook prints neither Sortino
nor the information ratio, although the engine's report carries both; no figure for either is
quoted here. The control traded on the rule's 109 dates and on no other. The index row is the rule
run's benchmark.

### The fill convention, checked

Sharadar publishes no VWAP, so its names fill at the day's close, which is also their mark; every
other name fills at the day's VWAP. The blueprint made the experiment's pass depend on the verdict
not changing when every name is filled the same way, so the rule and its control were priced again
with every fill at the close.

| Book, every fill at the close | CAGR | Volatility | Sharpe | Max drawdown | Commissions | Slippage |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| The rule | 4.29% | 18.10% | 0.2368 | −53.09% | $268,545.00 | $32,507.81 |
| The control | 5.91% | 23.00% | 0.2571 | −65.29% | $135,657.00 | $16,127.86 |

**The same verdict.** At the close the margins are −0.0202 of Sharpe and −1.63 points of CAGR,
against −0.0216 and −1.64 with the two conventions mixed. Prediction 1 fails under both, so the
result does not depend on how the dead names are filled.

### The realistic cost row

At the setting 0.005, charged at half a cent a share — $3.87 on 774 shares of `BR1` — the rule earns
5.86% at a Sharpe of 0.3251, and its control 6.55% at 0.2854. The rule's Sharpe margin there,
**+0.0397**, clears 0.03; its CAGR margin, **−0.69 points**, does not clear zero. Every verdict is
read at the headline row, as the blueprint fixed: the realistic row narrows the rule's shortfall
and does not close it, and the rule's Sharpe there is still below the index's 0.4383.

### The window it was found on, described

**Description, never evidence.** The same rule and control, on the same widened panel and download
and at the 5% reserve, over 2017-01-03 to 2026-06-01, 2,365 trading days. The arm's row is
Experiment 1's, as its findings record it.

| Book, 2017-01-03 to 2026-06-01 | CAGR | Volatility | Sharpe | Max drawdown | Alpha | Rebalances |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| The rule, on this panel | 19.11% | 21.65% | 0.8827 | −31.26% | 4.40% | 42 |
| The control, without the cross | 20.57% | 22.92% | 0.8976 | −34.05% | 5.86% | 42 |
| Experiment 1's diagnostic arm, `FINDINGS_1.md` | 19.52% | 22.25% | 0.8773 | −32.36% | 4.81% | 41 |

The rule minus its control on this window: **Sharpe −0.0148, CAGR −1.46 points**, the first margin
ever measured for this design against its own control. It does not reproduce the arm's 19.52%, as
the blueprint said it would not: this run holds the widened seed, the Sharadar names and a 5%
reserve, where the arm ran on the 788-name seed at 2%. The engine sold `TWTR` at its last price on
2022-10-27 in the rule's run here, as it did in Experiment 1. This run did not print the index's
row for this window.

<!-- example: end -->

## What the benchmark actually is, structurally

Rebalance frequency, turnover, holdings, concentration, invested share, and any structural tilt —
each with a reading of what a bad value would have meant.

<!-- example: begin -->

**The panel, the exclusions and the start, section 1.** The panel read to 2026-06-01 holds 6,390
dates by 1,437 positions, from a seed of 1,500 identifiers, 712 of them served by Sharadar, with
the index's membership known from its holdings from 2000-01-03 to 2026-08-14. Fifty-one identifiers
are excluded by name, by Experiment 1's two tests: the 47 with no price file, and `CIT`, `FMC`,
`LCI` and `PARA`, whose adjusted price multiplies by more than six in a day. None carries two
companies under one identifier; `JOURNAL_2.md` lists them all. The priced members hold 99.59% of
the index's weight or more on every date from 2001 to 2017, the years section 1 prints, and 99.71%
at the lowest inside the test, on 2003-09-02. No date after the start falls below 95%, so **the
test starts on 2002-07-30**, the first date the coverage rule allows.

**The book, sections 2 and 3.** Both books passed every invariant of section 2.1, fifteen in all:
eight on the rule and seven on the control, which does not read the cross. The rule's weight file
holds 217 identifiers by 109 rebalances, every column summing to one, with the cash proxy, `SHY`,
at 1.000 on the first date and 0.011 on average.

Read in section 3 from each book's targets held forward between rebalances: its shape, not its
return.

| Property | The rule | The control | What a bad value would have meant |
| --- | --- | --- | --- |
| Rebalances | 109 in the window, 7.6 a year, the last on 2016-11-16 | the same 109 | A rule trading on most days would be a cost question, not an alpha one. The invariant that it trades on fewer days than it does not passed |
| Mean one-way turnover per rebalance | 24.3% | 7.2% | The rule swaps the names whose cross moved; the control's set, the most traded members alone, moves little between the same dates |
| Annual turnover, target to target | 1.84 times the book | 0.54 | The engine's realised turnover was not read. The rule's turnover is what its $265,535.20 of commission is charged on |
| Mean invested share | 99.9%, lowest 0.0% on the first date | 100.0%, lowest 0.0% | A low figure would mean slots left empty. `SHY` holds any slot no name fills |
| Mean holdings | 20.0 | 20.0 | Equal by construction; a gap would mean hidden concentration |
| Held on a day the cross closed at 0 | 7,927 of 72,574 held name-days | 27,310 of 72,640 | The band's delay: the rule holds a broken name until the set moves by three at once. The control never reads the cross |
| Mean weight in Sharadar names | 13.6% | 8.1% | The dead names fill at the close; the fill check prices what that does |

**Capacity, criterion 4 of the gate**, measured as Experiment 1's was: each of the rule's trades
set against the name's 63-day average traded value on the day, and read as the largest book at
which that trade takes no more than the stated share of it.

| Share of a day's traded value | Worst trade | 1st percentile of trades | Median trade |
| --- | ---: | ---: | ---: |
| 1% | $3,851,439 | $7,019,368 | $106,111,907 |
| 5% | $19,257,197 | $35,096,840 | $530,559,534 |

**The worst trade binds.** At 1% of a day's traded value no trade of the rule's exceeds its share
while the book is at most $3,851,439; the trade at the first percentile allows $7,019,368, and the
median trade $106,111,907. Which trade is the worst was not traced. It bounds participation and
does not model market impact.

### Watched, but not predicted

The blueprint named these and predicted none of them.

- **The betas, side by side.** The rule 0.841, the control 1.141, from the engine's daily series
  against the index. The blueprint read a margin that comes with a much lower beta as timing, not
  selection. There is no margin to read: the lower beta came with a lower return.
- **The rebalances and the turnover.** 109 for each book; the rule turns over 1.84 times a year
  target to target and the control 0.54, and the engine charged the rule $265,535.20 of commission
  against the control's $135,357.30.
- **The weight in `SHY` through 2008 and 2009**, from the engine's daily weights: the rule's mean
  0.6%, highest 9.9%, and a mean of 6.2% in December 2008 and January 2009; the control's 0.0%
  throughout. The first design held 27–40% then. Slots left empty were rare, and the book stayed
  invested through the fall.
- **The share of each book's weight in Sharadar names**, from the engine's daily weights: the
  rule's mean 12.9%, highest 53.2%; the control's mean 7.7%, highest 24.2%.
- **Every name held on its last priced day.** The notebook's own check, which reads the engine's
  daily weight on each name's last priced day, printed none for either book. The engine's log in
  the same run names six in the rule's run, each sold at its last price with the proceeds left in
  cash until the next rebalance: `BR1` on 2006-03-31 for $67,428.21, `PD1` on 2007-03-19 for
  $93,689.41, `BUD1` on 2008-11-17 for $46,199.81, `NFS` on 2008-12-31 for $42,373.32, `UST1` on
  2009-01-05 for $43,182.52 and `DNA1` on 2009-03-26 for $41,006.53. Two targets of the rule fell
  on a name's last priced day, a weight of 0.05 in `BRL` on 2008-12-22 and in `HK1` on 2011-08-25,
  and the engine ignored both and left that capital in cash. All eight are Sharadar names. The
  control's run names none. The weights of the six on their last day were not printed, and the
  check was not changed after the run: caveat 6.

<!-- example: end -->

## The trial count

How many variants were ranked to reach the book above, and every run excluded by name with its
reason. `RESULTS.md` compiles this: a reader cannot discount a best-of-N result without knowing N,
and the graduation sign-off says whether the deflated figure was also computed.

<!-- example: begin -->

### The perturbation, criterion 3

Ten cells, fixed in the blueprint, one setting at a time around the rule, each priced beside its
own control: the same most traded members without the cross, taking the cell's book size and delay
and trading on the cell's own rebalance dates. Net, at the headline cost row, over the test window.
**The rule itself** — 20 names, a 15% band, 50 and 200, 63 days, one day — reads Sharpe 0.234,
−0.022 over its control and −1.641 points of CAGR, on 109 rebalances.

| Cell | Sharpe | Sharpe over control | CAGR over control, points | Rebalances |
| --- | ---: | ---: | ---: | ---: |
| Band 10%, one swap | 0.105 | −0.172 | −4.654 | 1,069 |
| Band 30%, three swaps | 0.239 | −0.078 | −2.950 | 20 |
| Band 40%, four swaps | 0.677 | +0.278 | +2.288 | 5 |
| Book size 10, band 30% | 0.362 | −0.028 | −3.253 | 34 |
| Book size 15, band 20% | 0.300 | +0.011 | −1.329 | 67 |
| Book size 25, band 12% | 0.199 | −0.010 | −1.191 | 176 |
| Book size 30, band 10% | 0.223 | −0.044 | −2.087 | 224 |
| Averages 40 and 160 | 0.307 | +0.038 | −0.647 | 143 |
| Averages 60 and 250 | 0.244 | −0.003 | −1.322 | 79 |
| Acted on 5 days late | 0.251 | −0.005 | −1.423 | 109 |

**Each curve's direction, as the blueprint asked:**

- **The band.** No direction. The margins are worst at 10%, −0.172 and −4.654; better at the rule's
  15%; worse again at 30%, −0.078 and −2.950; and positive only at 40%, +0.278 and +2.288. The 40%
  cell re-struck its book five times in the fourteen years, the fewest of any cell, and is the cell
  least like the rule's own trading. The engine sold nine names at their last price in its rule's
  run, from `EXPEA` in 2003 to `EMC1` in 2016, and each left its proceeds in cash until the next of
  those five rebalances.
- **Book size.** The CAGR margin is negative at every size, from −3.253 at ten names to −1.191 at
  twenty-five. The Sharpe margin is positive only at fifteen, +0.011.
- **The averages.** Both neighbours beat the rule's own pair on both margins: 40 and 160 at +0.038
  and −0.647, 60 and 250 at −0.003 and −1.322. The CAGR margin stays negative at both.
- **The delay.** Acting 5 days late narrows both margins a little, to −0.005 and −1.423: acting late
  does not hurt the cross against its control, as in Experiment 1. The late book also targeted
  names after their last price, and the engine left those weights in cash: caveat 7.

**Criterion 3 is read as failed, on its own rule**: the rule is ahead of its control on both Sharpe
and CAGR in **1 of 10 cells**, the band at 40%, and the blueprint asked for eight. A cell in which
the rule trails its control on either measure counts against it. None of the rule's own settings is
the best of its curve on either margin, and the best cell is never the answer: picking one after
the result is a new experiment, and one more trial.

### The count

**Forty-three trials, the count the blueprint fixed.** The thirty-one `BLUEPRINT_1.md` fixed, which
already hold the owner's earlier test outside this repository and the arm; then this experiment's
rule, counted again because it meets new years; its ten cells; and the revision that raised the
cash reserve to 5%, one more. The owner's earlier test is counted as one because its variants were
not kept, so the count is a lower bound.

**Thirty-four engine runs in this experiment's notebook**, every one valued on at least 99% of its
window's trading days. Experiment 1's forty-five are quoted beside the count, never as it. By role:

| Role | Engine runs | Counted as |
| --- | ---: | --- |
| The rule | 1 | a trial |
| The control | 1 | a diagnostic |
| The rule and the control at realistic costs | 2 | diagnostics: the same books at another cost row |
| The rule and the control with every fill at the close | 2 | diagnostics: the fill convention |
| The sub-periods: the rule and its control in each of three | 6 | diagnostics: the kill switch |
| The window it was found on: the rule and its control | 2 | description, never evidence |
| The perturbation: ten cells and their ten controls | 20 | ten trials and ten diagnostics |
| **All** | **34** | |

**The Verify section, section 8, raised nothing.** 21 checks on the books and the weight file: the
fifteen invariants of section 2.1, and six on the file read back from disk and the control's dates.
70 on the runs: two window checks on each of the 34 engine runs, 68, and two on the attribution,
that its window lies inside the backtest's and that both books have an idiosyncratic figure.

**No variant was selected on its result.** Every book above was fixed in `BLUEPRINT_2.md` or in the
notebook before the run. The deflated Sharpe was not computed.

**Two earlier runs, each by name.**

- **Excluded: the first run, at a 2% cash reserve, 08:48 to 09:25 on 2026-09-24.** It could not be
  priced. Ten of its engine runs stopped short, each valuing 42.5% to 47.4% of its window's trading
  days, and its Verify section raised, naming them with the days each left unvalued at the end. Set
  on the window's calendar, five stopped at 2009-05-18, their last valued day 2009-05-15: the rule,
  the rule with every fill at the close, sub-period 2's rule, and the band 10% and band 30% cells'
  rules. The other five were last valued on other days: the book-size-30 cell's control on
  2008-09-16, the averages 40 and 160 cell's rule on 2009-04-20, book size 10's on 2009-05-05, book
  size 15's on 2009-05-13, and the 5-days-late cell's on 2009-05-22. Only the rule's cause is
  logged, by the debugging run of the headline rule that followed: on 2009-05-18 a full
  re-equalisation on a rising day overdrew the reserve, a cash error of −$4,939.68, and the engine
  valued no later day while still returning a summary of the stub. The run's own log holds only the
  Verify section's message, so why the other nine stopped is not recorded, and `BLUEPRINT_2.md`'s
  revision, which says every run that crossed that date stopped there, is not what the log shows. No
  figure from the run is reported, nor from the debugging run. Its engine runs are not among the
  thirty-four; the revision it led to is counted as a trial.
- **Superseded, not excluded: a complete run at 5%, 09:38 to 10:15.** Every engine figure it
  printed equals the run reported here, and its Verify section raised nothing: 21 checks on the
  books and 68 on 34 engine runs. Step 6 was skipped, because the desk had just moved its files
  and the notebook found none where the old layout kept them. `Data/hand_supplied.py` now reads
  both layouts, and the run of 12:38 is the record because it carries the attribution.

<!-- example: end -->

## Attribution — is this the signal, or a factor exposure wearing its name?

Brinson-Fachler: allocation, selection, interaction. The factor model: factor against idiosyncratic.
State the window, which is bound by the supplied files' coverage and is usually shorter than the
backtest.

**What it settles**, and **what it does not** — naming the counterfactual book that would settle
what is left: the same holdings with the signal off, positions equalised, a random draw at the same
sizes, entry dates shifted.

<!-- example: begin -->

**Window: 2008-01-14 to 2016-12-30**, bound by the factor files' first date; the backtest runs from
2002-07-30. **Sub-period 1 and all of 2007 lie outside it**, and with them the sub-period in which
the rule trailed its control most, 7.99% a year against 12.21%. The book is read daily as the
engine held it, widened to the whole index at zero weight, with the fifty-one excluded names dropped
from both. 1,351 of the 1,352 identifiers the book and the index name have a price series here,
where Experiment 1's attribution priced 686 of 1,399: the widened seed carries nearly every name
the index held. The desk's files were read from the Analytics Factory's folders.

**First cut, Brinson-Fachler**, the rule against the index, summed daily over the window, in
percentage points: alpha **−42.29**, of which allocation **+0.23**, selection **+6.33** and
interaction **−48.84**. The shortfall falls almost wholly into interaction. This library's first
cut is per asset, not per group, so each line is about the weighting of names, not of sectors. Read
it as "the weighting did it", not as "the sectors did it".

**Second layer, the factor model**, on the rule and on its control, in percentage points summed
over the window:

| Source | The rule | The control |
| --- | ---: | ---: |
| Market | 4.81 | 5.30 |
| Beta | 7.25 | −10.55 |
| Momentum | 0.70 | 4.72 |
| Residual volatility | −4.49 | −2.52 |
| Size | 0.22 | −7.17 |
| Value | 3.13 | 3.16 |
| The eleven sector factors | 0.00 each | 0.00 each |
| **All factors** | **11.61** | **−7.06** |
| **Idiosyncratic** | **−7.93** | **30.24** |
| **Excess return** | **3.68** | **23.18** |

**What it settles.**

- **The cross subtracts idiosyncratic return.** The control keeps 30.24 points the factor model
  cannot explain; the rule, which differs from it in the cross alone, keeps −7.93. **The cross's
  share is −38.17 points** over the nine years. Criterion 2 of the gate asks for idiosyncratic
  alpha, and the rule's residual is negative.
- **The cross changes the book's factor mix, not its reward.** Against its control the rule's
  beta-factor line is 7.25 points against −10.55, its size line 0.22 against −7.17 and its momentum
  line 0.70 against 4.72, and its measured beta is 0.841 against 1.141. The rule's 3.68 points of
  excess return are 11.61 of factors and −7.93 of residual; the control's 23.18 are −7.06 and
  30.24.

**What it does not settle.** The third pass, Brinson-Fachler on the residual returns, has not been
run; it would split a negative residual, not reverse it. The attribution does not reach 2002 to
2007. The sector lines read 0.00 for both books, as in Experiment 1, so a sector tilt is not
separated from the rest. Of the counterfactuals `AGENTS.md` names, the blueprint declared only the
signal off, which is the control, and it settles which way the cross points. No random books were
priced, so there is no baseline for the rule's −7.93 points beyond the control's.

<!-- example: end -->

## What is open, ranked

The single highest-value run outstanding, and what it would settle.

<!-- example: begin -->

**None of these can turn the verdict**: the rule trails its control on both windows and trips its
kill switch. They bear on how it is read. What follows it is the owner's to decide.

1. **The check for names held on their last priced day.** It printed none where the engine's log
   names six in the rule's run. The blueprint's key risk is read from the log here; the check is
   what should read it.
2. **Attribution before 2008.** Factor files reaching back to 2002 would attribute sub-period 1,
   where the rule trailed its control most.
3. **The third pass, Brinson-Fachler on the residual**, not run for either experiment.
4. **The engine's order of sales and purchases on a rebalance day**, which overdrew the 2% reserve.
   The library's maintainers can say whether a day's sales settle before its purchases.
5. **What survivorship costs**, the blueprint's third open question: the same rule on FMP's
   survivors alone, against this run, would price it, and both sets of files now exist.

<!-- example: end -->

## Caveats

| # | Caveat | Effect |
| --- | --- | --- |
| 1 | what a reader must know before quoting a number above | what it does to that number |

<!-- example: begin -->

| # | Caveat | Effect |
| --- | --- | --- |
| 1 | **The dead names fill at the close.** Sharadar publishes no VWAP, so for its names the fill is the close, which is also the mark; every other name fills at the day's VWAP. The rule held a mean of 12.9% of its weight in Sharadar names, up to 53.2%, and the control 7.7%, up to 24.2% | The fill check prices both books with every name at the close: the margins move from −0.0216 and −1.64 to −0.0202 and −1.63, and the verdict does not change |
| 2 | **`m_volume` is empty in the Sharadar files**, and no file from either provider carries the unadjusted VWAP, `m_vwap`. The Curator's `c_*` columns, which the rule and the engine read, are populated: its traded value falls back to the split-adjusted VWAP and volume where the unadjusted pair is missing | Nothing priced here reads the unadjusted volume. A reader who wants a dead name's unadjusted volume does not have it in these files |
| 3 | **Two Curator versions.** The Sharadar names come from the Data Curator's `issues/31` branch at commit `8b54c2f`, built as 0.49.1, the only version with the Sharadar provider; every other name from 0.50.0. Twenty names both providers carry, `A` to `AES`, were fetched from both and compared, daily returns, 2002-07-30 to 2026-06-01 | The mark agrees: a median daily gap of 0.00 to 2.82 basis points, a correlation of 0.9978 or more. The fill does not, as expected of a close against a VWAP: a median gap of 45.9 to 80.0 basis points, a correlation of 0.74 to 0.88. Caveat 1's check prices that difference |
| 4 | **Coverage.** The priced members hold 99.59% of the index's weight or more on every date from 2001 to 2017, the years the run printed, and 99.71% at the lowest inside the test. The rest is in members without a price and a fill price that day, the fifty-one excluded names counted among them | The index's return, the desk's own, includes them and no book here can hold them, so the gap bears on the comparison with the index more than on the one with the control |
| 5 | **Reproduced from a wiped working copy that kept its raw downloads.** Its FMP files had been downloaded fresh through 2026-06-01, in the same clone, earlier on 2026-09-24 for Experiment 1's reproduction; its Sharadar names were re-curated through the branch from the bulk tables that morning's fetch had cached. That download lacks `MIC` | Every figure is the same in both runs. `MIC` has no price inside either window in the working copy and is excluded by name in the wiped one, so neither book could hold it |
| 6 | **Delisting exits use one day of hindsight, and the rule held six names to their last priced day**: `BR1`, `PD1`, `BUD1`, `NFS`, `UST1` and `DNA1`, which the engine sold at that price. It ignored the rule's targets in `BRL` and `HK1` on their last priced day and left the capital in cash. The control's run names none, and the notebook's own check printed none for either book | The engine's exit at the last price spares whichever book holds a failing name to the end, here the rule alone. Whether each of the eight left the market by failure or by acquisition was not checked, so the direction of the effect on the rule's figures was not measured |
| 7 | **The delay cell targeted names after their last price**: `BUD1` on 2008-11-20, `BRL` on 2008-12-30, `NFS` on 2009-01-05, `UST1` on 2009-01-09 and `HK1` on 2011-09-01, each at 0.05, besides `NFS` and `UST1` on their last day | The engine ignored those weights and left the capital in cash, so the delay cell, which the reading of exit speed leans on, carries a data artefact, as it did in Experiment 1 |
| 8 | **Costs are the blueprint's row**, the commission setting 0.1, charged at $0.10 a share: $265,535.20 on the rule over the window, against the control's $135,357.30, with 5 basis points of slippage and a 5% cash reserve | Every verdict is read there. The realistic row, 0.005, reads 5.86% and 0.3251 against the headline's 4.23% and 0.2340, and leaves the rule 0.69 points a year behind its control |
| 9 | **Two figures for the index's fall.** The engine's summary gives the index a maximum drawdown of −55.37% over the test window; measured inside 2007 to 2009 from the daily series paired with the rule's, as prediction 3 is, it is −53.97%. The gap was not traced | Prediction 3 holds on the blueprint's measure, −53.32% against −53.97%, and would hold by more against −55.37% |
| 10 | **The attribution window starts on 2008-01-14** | Sub-period 1 and 2007 are not attributed; the idiosyncratic figures describe 2008 to 2016 alone |
| 11 | **The desk's eleven sector factor lines read 0.00** | A sector tilt is not separated from the other lines |
| 12 | **These years are not unseen.** The first design's long window priced them from 2002-07-30 on a fixed membership, and the analyzer's rows 1 to 18 were measured on 2001 to 2026 | Predictions 2 and 3 were written knowing both, with the figures that argued against each named beside it. Only the rule against its own control met these years unseen |
| 13 | **The blueprint's 92% was withdrawn.** `BLUEPRINT_2.md` sets its 95% coverage threshold "above the 92% Experiment 1's window opened on". That 92%, the 788-name seed's share of the index's weight in 2017, came from an entry of `JOURNAL_1.md` that a later entry withdrew on 2026-09-24: no run printed it | The threshold and its measured result do not depend on it: the lowest coverage inside the test was 99.71%, on 2003-09-02, and the test starts on 2002-07-30 either way. The blueprint stays as written |

<!-- example: end -->
