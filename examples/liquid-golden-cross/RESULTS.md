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
> Every table below except *Known limitations* is empty by design: the shape is fixed, the numbers
> arrive from the pipeline.
> Delete this blockquote when the first one reports.

<!-- example: begin -->

> **In this example, everything below is `liquid-golden-cross`, measured.** Steps 1 to 6 are run,
> and the numbers are real: Experiment 1's second design, run 2026-09-23 and reproduced from a
> wiped working copy on 2026-09-24, with its first design kept as a row; Experiment 2, run
> 2026-09-24 and reproduced from a wiped working copy the same day; and Experiments 3 and 4, run
> on 2026-09-24 and 2026-09-25 from a wiped working copy.
> Step 7's gate has been *evaluated* against all four and none passes. One book is on paper
> without graduation, Experiment 4's, a candidate by the owner's decision since 2026-09-25, and
> apart from its days **nothing here is out of sample**. Which criteria each fails and why, and the
> book's registration, are in [`Paper_Trading/BITACORA.md`](Paper_Trading/BITACORA.md).

<!-- example: end -->

## The project in three sentences

Does the benchmark book work, with its headline numbers. What attribution says about where the
return comes from. Which lever earned its place after the benchmark, and which was rejected.

<!-- example: begin -->

**The book beats the index, and misses the margins it set itself against the same names without
its signal.** Holding the twenty most traded US stocks whose 50-day average sits above their
200-day, and selling each the day after its cross breaks, compounded at 17.87% against the index's
14.63% over 2017–2026, net of costs, at a Sharpe of 0.806 against 0.770. Against the same twenty
names without the cross it is ahead on Sharpe by 0.031 and **0.86 points a year behind** on CAGR,
so prediction 1's margins are not met, and it is ahead of them on both in one sub-period of three,
so it fails its kill switch. The first design, thirty names on a 10% band, lost to its control too,
by 1.12 points a year, and is kept at tag `v0.15.0`.

**Attribution says the cross trades beta for momentum, not for selection.** Against its control the
rule carries a beta of 1.067 to 1.238 and a momentum line of 15.44 points to 5.99, and keeps fewer
idiosyncratic points, 36.19 to 40.99: just above the top of five random twenty-name books. The
blueprint reads a Sharpe edge that comes with a lower beta as timing. On 2008 to 2016, in
Experiment 2, the cross leaves its book −7.93 idiosyncratic points against its control's 30.24.

**Nothing has earned a lever, and the one surprise did not survive new years.** The first design's
rebalancing, kept at twenty names on a 15% band as a diagnostic arm, reproduced its delay and
earned 1.65 points a year more than the fast exit, so exit speed is not why the cross loses.
Experiment 2 took that arm's design to 2002-07-30 to 2016-12-30, which it was not found on: **4.23%
a year at a Sharpe of 0.234, against its control's 5.87% and 0.256** and the index's 8.57% and
0.438, ahead of its control on both measures in none of three sub-periods. Set against its own
control on 2017 to 2026 for the first time, it trails there too, by 1.46 points a year. Claim 1
stays falsified, now on two windows.

**Momentum proper, on the same names, fails as well.** Experiment 3 held the twenty of the hundred
most traded members with the highest return over the twelve months before the latest one,
re-struck monthly, over 2002-07-30 to 2026-06-01: **10.81% a year at a Sharpe of 0.436, against its
control's 11.03% and 0.465** and the index's 10.99% and 0.568, ahead of its control on both
measures in one sub-period of three, 2017 to 2026. Attribution finds the ranking a momentum tilt,
44.78 points of the factor against the control's 16.77, that takes 5.59 idiosyncratic points away.

**Momentum held only outside bear markets comes closest, and still misses.** Experiment 4 keeps
Experiment 3's ranking except in a month that opens after a negative two-year return of the index,
when it holds the most traded twenty instead, the state Daniel and Moskowitz find before every one
of momentum's fifteen worst months: **11.61% a year at a Sharpe of 0.478, against its control's
10.53% and 0.469** and the index's 10.99% and 0.568. It leads its control by 1.08 points a year, in
two sub-periods of three, and beats the same ranking held in every month on both measures, and its
ranking now adds 8.84 idiosyncratic points where Experiment 3's took 5.59 away; but its Sharpe
margin, 0.0084, is short of the 0.03 every experiment here has been judged by, and five of its
twelve perturbation cells lead on both where ten were asked for. Claim 5 stays falsified, now for
two designs, and nothing graduates.

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

**Measured 2026-09-19 on 4,252,848 rows: 787 securities, 2001-01-02 to 2026-06-01.** The eligible
pool is the most traded five percent of each day's cross-section, which is where the rule selects
from.

| # | Measurement | Value | Dates with the expected sign | Section |
| --- | --- | ---: | ---: | --- |
| 1 | Mean pairwise correlation of daily returns | 0.303 | — | 2 |
| 2 | Information coefficient of `r_trend_50_200`, 21 days, eligible pool | 0.0112 | not measured | 4 |
| 3 | The same, 63 days | 0.0027 | not measured | 4 |
| 4 | The same, 252 days | −0.0060 | not measured | 4 |
| 5 | Information ratio at 21 days, eligible pool | 0.038 | not measured | 4 |
| 6 | Forward 21-day return, 50-day average above the 200-day | 1.20% | — | 5 |
| 7 | Forward 21-day return, 50-day average below the 200-day | 1.03% | — | 5 |
| 8 | Forward 21-day volatility, above | 28.7% | — | 5 |
| 9 | Forward 21-day volatility, below | 36.7% | — | 5 |

**The sign column arrived after this was measured.** Section 4 of the analyzer now writes the share
of dates on which the coefficient was positive, the sign the rule expects; the run of 2026-09-19
did not, so rows 2 to 5 carry none. The windows overlap: consecutive dates share 20 of 21 days at a
month and 251 of 252 at a year.

**Measured again 2026-09-23, on the same panel, which ended 2026-06-01**, for the second design of
Experiment 1: the refinery had not been re-run since, so nothing after the window's end was read.
The rows above reproduce — 0.0112, 0.0026, −0.0060 and 0.038 — and now carry their signs, and the
cross is measured as the rule reads it, a state of 1 or 0.

| # | Measurement | Value | Dates with the expected sign | Section |
| --- | --- | ---: | ---: | --- |
| 10 | Information coefficient of `r_trend_50_200`, 21 days, eligible pool, on 6,170 dates | 0.0112 | 53.2% | 4 |
| 11 | The same, 63 days, on 6,128 dates | 0.0026 | 51.4% | 4 |
| 12 | The same, 252 days, on 5,939 dates | −0.0060 | 47.6% | 4 |
| 13 | Information coefficient of the cross as a state, 21 days, eligible pool, on 6,066 dates | 0.0066 | 51.8% | 5 |
| 14 | The same, 63 days, on 6,024 dates | −0.0011 | 49.2% | 5 |
| 15 | The same, 252 days, on 5,835 dates | 0.0035 | 48.9% | 5 |
| 16 | A name whose cross breaks, against the rest of the eligible pool over the next 5 days: mean, median | −0.16%, −0.06% | 50.5% below the pool | 5 |
| 17 | The same over 21 days, on 616 breaks | −0.51%, −0.31% | 51.9% below the pool | 5 |
| 18 | The same over 63 days, on 609 breaks | −0.91%, −1.04% | 53.4% below the pool | 5 |

**What rows 16 to 18 measure, and what they do not.** A break is a name in the eligible pool whose
cross was at 1 the day before and is at 0 that day; its forward return runs from that day's close,
against the equal average of the pool on the same dates. The windows overlap as above, and a name
can break more than once. It is not what a rule that sells on the break earns: that rule sells at
the next day's VWAP and buys a replacement, not the pool. It is the most a rule that holds on after
a break can lose, and it is small — half a point a month, on barely more than half the breaks.

**Measured a third time on 2026-09-24**, in Experiment 1's reproduction from a wiped working copy,
on a fresh download through 2026-06-01 from which the refinery read 787 securities and 4,252,838
rows. Rows 1, 2 and 4 to 18 came back as printed, and row 3 at 0.0026, as on 2026-09-23; the
analyzer's Verify section ran its 8 checks. **Every row here describes the seed of 788 names.** The
one analyzer run on the seed Experiment 2 widened, for Experiment 3, is below; it does not replace
them.

**What it says.** The trend signal barely predicts return and strongly predicts volatility. An
information coefficient of 0.011 at one month is noise beside the 0.02 to 0.03 a working signal
shows; it decays to nothing by three months and turns negative at a year, on 5,939 dates. The
volatility difference is the opposite: 28.7 percent against 36.7 percent, on 208,111 observations,
in the direction the rule's own trades would take.

**What it licenses, and what it forbids.** It licenses a prediction that the book is defensive
rather than high-returning: lower volatility and a shallower drawdown than the index, with no
expectation of a higher return. It forbids treating the filter as a return signal, and a book built
on it has to be judged against the same thirty names without the filter, not against cash.

**The caveats it carries.** One security, `MIC`, has no file at all. Four more — `CIT`, `FMC`,
`LCI`, `PARA` — carry adjusted prices that multiply by more than six in a day, which is a bad print
rather than a return, and are excluded by name in the rule. 265 of the 788 have no prices when the
long window opens in 2002, and 76 series end early, every one of them a real delisting.

**Measured a fourth time on 2026-09-24, for Experiment 3, on the seed Experiment 2 widened**, after
the owner chose that experiment's signal and before its blueprint was written. The refinery wrote
1,453 files, 6,348,870 rows, with a new column, `r_momentum_12_1`: the price 21 trading days before
over the price 252 trading days before, less one, on the dividend-and-split-adjusted close, from
`Data/Refinery/custom_calculations.py`. The analyzer read 6,390 dates by 1,437 securities,
2001-01-02 to 2026-06-01 and nothing later, and its Verify section ran its 10 checks. **Rows 1 to
18 are not replaced:** the same run printed their measurements again on the widened panel, and they
differ — a mean pairwise correlation of 0.271 against row 1's 0.303, and, in the eligible pool of
a wider cross-section, `r_trend_50_200` at 21, 63 and 252 days at 0.0195, 0.0186 and 0.0086,
positive on 54.9%, 52.9% and 47.9% of dates, against rows 10 to 12's 0.0112, 0.0026 and −0.0060.
Those rows describe the 788-name seed and stand as they are at the KaxaNuk Researcher's `v0.18.0`;
*What is closed* cites them, and on the widened panel the same measurement is higher at every
horizon.

The pool below is the hundred securities with the highest `r_liquidity_rank` on each date, less any
without a momentum value. The rank is a percentile across every security present, index member or
not, so this pool is a neighbour of the one Experiment 3 selects from, the hundred most traded
members, and not the same. The sign the signal expects is positive. The two windows are the two
the experiments have used, 2002-07-30 to 2016-12-30 and 2017-01-03 to 2026-06-01. Consecutive
windows share 20 of 21 days at a month, 62 of 63 at a quarter and 251 of 252 at a year; on the
first trading day of each month alone, 21-day windows share only the days by which a month falls
short of 21 trading days.

| # | Measurement | Value | Dates with the expected sign | Section |
| --- | --- | ---: | ---: | --- |
| 19 | Information coefficient of `r_momentum_12_1`, 21 days, the hundred most traded, 2002 to 2016, on 3,633 dates | 0.0134 | 54.7% | 5 |
| 20 | The same, 63 days, on 3,633 dates | −0.0018 | 48.0% | 5 |
| 21 | The same, 252 days, on 3,633 dates | −0.0025 | 52.5% | 5 |
| 22 | Row 19 on the window's 173 month starts alone | 0.0140 | 56.1% | 5 |
| 23 | Information coefficient of `r_momentum_12_1`, 21 days, the hundred most traded, 2017 to 2026, on 2,344 dates | 0.0304 | 56.1% | 5 |
| 24 | The same, 63 days, on 2,302 dates | 0.0234 | 54.9% | 5 |
| 25 | The same, 252 days, on 2,113 dates | 0.0309 | 58.6% | 5 |
| 26 | Row 23 on the window's 112 month starts alone | 0.0170 | 50.9% | 5 |
| 27 | The twenty of the hundred with the highest `r_momentum_12_1`, against the hundred's mean over the next 21 days, on 173 month starts, 2002 to 2016: mean, median | +0.14%, +0.34% | 56.6% above the pool | 5 |
| 28 | The same on 112 month starts, 2017 to 2026 | +0.83%, +0.55% | 55.4% above the pool | 5 |
| 29 | Information coefficient of `r_momentum_12_1`, whole panel, 2002 to 2016, at 21, 63 and 252 days, on 3,633 dates each | 0.0163, 0.0075, 0.0078 | 57.1%, 56.0%, 62.6% | 5 |
| 30 | The same, 2017 to 2026, on 2,344, 2,302 and 2,113 dates | 0.0250, 0.0343, 0.0364 | 59.0%, 61.0%, 62.9% | 5 |

**What rows 27 and 28 measure, and what they do not.** On each month start, the twenty names of the
pool with the highest momentum, against the pool's equal average over the next 21 days, from that
day's close. No lag, no costs, no sizing: a measurement of the signal, never a return a book earned,
and set against the pool's mean rather than against its twenty most traded, the control Experiment
3 names.

**What it says.** Among the most traded, momentum at a month carries 0.0134 on 2002 to 2016, below
the 0.02 to 0.03 a working signal shows, and 0.0304 on 2017 to 2026, at its top; on month starts
alone, where the windows barely overlap, 0.0140 and 0.0170, the second positive in just over half
of 112 months. On 2002 to 2016 it is below zero at a quarter and at a year in this pool, where
across the whole panel it stays positive at every horizon in both windows. In the pool, at 63 and
252 days, the month-start readings are within 0.004 of the daily ones, with the same sign, and
still overlap.

**What it licenses, and what it forbids.** It licenses a prediction that the twenty with the
highest momentum beat the most traded twenty on the same dates, net, with the evidence against it
beside it: an edge of 0.14% a month before costs on 2002 to 2016, against which a monthly re-strike
pays its costs, and a signal that does not last a quarter on those years. It forbids reading a
book's result on either window as the signal out of sample: both were measured here before the
book was designed.

**Measured a fifth time on 2026-09-25, for Experiment 4, by market state**, after the owner chose
that experiment's design and fixed its state in `BRAINSTORMING_4.md`, and before its blueprint was
written. The state is Daniel & Moskowitz's bear market: the KN US Equity 600's own return over the
prior 504 trading days below zero, read from the desk's daily returns at each date's close. On
2002-07-30 to 2026-06-01, 42 month starts fall in it: August 2002 to September 2003 and December
2003, fifteen; October 2008 to September 2010, twenty-four; and April 2020, May 2023 and November
2023. The pool is rows 19 to 28's, and rows 35 to 38 set the twenty with the highest momentum
against the pool's twenty most traded, the control Experiments 3 and 4 name, rather than against its
mean. Each coefficient is read on the state's dates that have a 21-day forward return. The
analyzer's Verify section ran its 11 checks; rows 1 to 30 are unchanged.

| # | Measurement | Value | Dates with the expected sign | Section |
| --- | --- | ---: | ---: | --- |
| 31 | Information coefficient of `r_momentum_12_1`, 21 days, the hundred most traded, 2002 to 2016, in a bear state, 839 dates | −0.0362 | 45.2% | 5 |
| 32 | The same outside one, 2,794 dates | 0.0284 | 57.6% | 5 |
| 33 | The same, 2017 to 2026, in a bear state, 77 dates | 0.0442 | 55.8% | 5 |
| 34 | The same outside one, 2,288 dates | 0.0299 | 56.1% | 5 |
| 35 | The twenty of the hundred with the highest `r_momentum_12_1`, against the hundred's twenty most traded over the next 21 days, on the 39 bear month starts of 2002 to 2016: mean, median | −0.49%, −0.20% | 48.7% above | 5 |
| 36 | The same on the 134 month starts of 2002 to 2016 outside one | +0.24%, +0.48% | 56.7% above | 5 |
| 37 | The same on the 3 bear month starts of 2017 to 2026 | −1.26%, −2.28% | 33.3% above | 5 |
| 38 | The same on the 109 month starts of 2017 to 2026 outside one | +0.12%, +0.04% | 51.4% above | 5 |

**What it says.** On 2002 to 2016 the signal turns with the state: below zero in bear months,
−0.0362, and 0.0284 outside them, where rows 19 and 22 read 0.0134 and 0.0140 across both. Against
the twenty most traded the twenty highest trail by 0.49% a month in bear months and lead by 0.24%
outside them; against the pool's mean they read −0.32% and +0.27%. On 2017 to 2026 the state barely
occurs, three month starts, and outside it the lead over the twenty most traded is 0.12% a month, in
just over half the months.

**What it licenses, and what it forbids.** It licenses a prediction that momentum's twenty, held
only outside bear months and the twenty most traded inside them, beat the twenty most traded on the
same dates, net, with the evidence against it beside it: an edge before costs of 0.24% a month on
2002 to 2016 and 0.12% on 2017 to 2026, against which a monthly re-strike pays its costs, as
Experiment 3's did. It forbids reading the result as the state out of sample: the state was chosen
after Experiment 3's book lost the 2009 rebound, and it is measured here on the same years the book
will be tested on.

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
| **1** | twenty most traded above the cross, sold the day after it breaks | **17.87%** | **0.8057** | −32.20% | 0.7748 | **+0.031** | **fails its kill switch**; does not graduate | 1, the signal: stays **falsified**, exit speed ruled out; 4, the rebalancing: **measured**, on an engine-priced arm at a 15% band | [`FINDINGS_1.md`](Experiments/Experiment_1/FINDINGS_1.md) |
| 1, first design | thirty most traded, in an uptrend, on a 10% band | 17.85% | 0.861 | −30.54% | 0.831 | +0.030 | superseded, kept at tag `v0.15.0` | 1, the signal: **falsified** | `FINDINGS_1.md` at tag `v0.15.0` |
| **2** | the arm's design: twenty most traded above the cross, re-equalised when three names move, 2002–2016 | **4.23%** | **0.2340** | −53.32% | 0.2556 | **−0.0216** | **fails its kill switch**; does not graduate | 1, the signal: stays **falsified**, now on two windows | [`FINDINGS_2.md`](Experiments/Experiment_2/FINDINGS_2.md) |
| **3** | momentum among the most traded: the twenty of the hundred with the highest twelve-month return, re-struck monthly, 2002–2026 | **10.81%** | **0.4358** | −65.57% | 0.4647 | **−0.0289** | **fails its kill switch**; does not graduate | 5, momentum: **falsified**, for this design, on this window | [`FINDINGS_3.md`](Experiments/Experiment_3/FINDINGS_3.md) |
| **4** | the same ranking held only outside bear markets, the most traded twenty inside them, 2002–2026, at a 10% reserve | **11.61%** | **0.4779** | −67.13% | 0.4694 | **+0.0084** | **fails its kill switch**, on its Sharpe margin alone; does not graduate | 5, momentum: stays **falsified**, now for two designs | [`FINDINGS_4.md`](Experiments/Experiment_4/FINDINGS_4.md) |

**Three windows.** Experiment 1's two designs both run 2017-01-03 to 2026-06-01, net of costs. The
panel was refreshed on 2026-09-23 before the second ran, which rebases every adjusted column, so
compare each design with its own control and index row; the second design's reproduction, on a
fresh download through 2026-06-01, returned every engine figure to the digit. Experiment 2 runs
2002-07-30 to 2016-12-30, net of costs, on the seed widened to 1,500 identifiers and at a 5% cash
reserve where Experiment 1 held 2%: compare it with its own control row, never with Experiment 1's
headline. Experiment 3 runs 2002-07-30 to 2026-06-01 on Experiment 2's panel and reserve, and
Experiment 4 on the same window and panel at a 10% reserve, with a check that ends a listing at its
last distinct bar. In
Experiments 1 and 2 the control is the same book without the trend condition, trading on the rule's
own dates: in the first design, the equalised control; in Experiment 3 it is the same pool's twenty
most traded, without the momentum ranking, on the rule's dates, and in Experiment 4 the same.
**`vs control` is a Sharpe difference, and it hides the CAGR**: the first four books each earn less
than their control, by 0.86 points a year in the second design, 1.12 in the first, 1.64 in
Experiment 2 and 0.22 in Experiment 3; Experiment 4's earns 1.08 points more, at a Sharpe margin of
0.0084.

### The counterfactuals

Experiment 1's second design and its arms. Idiosyncratic points from the factor model, over the
same window:

| Arm | What it removes | CAGR | Sharpe | Beta | Idiosyncratic |
| --- | --- | ---: | ---: | ---: | ---: |
| The rule | — | 17.87% | 0.8057 | 1.067 | 36.19 |
| The control | the cross | 18.73% | 0.7748 | 1.238 | 40.99 |
| The diagnostic arm | the fast exit: the first design's rebalancing at twenty names, on a 15% band | 19.52% | 0.8773 | 1.093 | 50.02 |
| Random, five seeds | the ranking and the cross | 1.82% to 8.95% | 0.091 to 0.461 | not measured | −11.78 to 35.31, mean 22.4 |

The random books draw twenty names on the first trading day of each month from 2017-01-03, a day
on which the rule does not trade and the pool they draw from is empty, so each holds only `SHY`,
the cash proxy, until its second draw, on 2017-02-01: their weight files show it, and no cell
prints it. Every random figure above carries that month.

**The arm is the finding.** It reproduced the first design's delay, a broken name held a median of
28 days, and beat the rule on return, on Sharpe and on idiosyncratic points. **The random arm sets
the baseline**: the rule's 36.19 sits just above the random books' top, 35.31. In the first design
the random arm put genuine selection nearer 33 of 45.5 points, against a random mean of 12.5.

### Against the world, Experiment 1

| Book | CAGR | Volatility | Sharpe | Max drawdown |
| --- | ---: | ---: | ---: | ---: |
| The rule | 17.87% | 22.18% | 0.8057 | −32.20% |
| The rule, realistic costs | 18.36% | 22.17% | 0.8280 | −32.15% |
| The control, without the cross | 18.73% | 24.17% | 0.7748 | −41.83% |
| The diagnostic arm | 19.52% | 22.25% | 0.8773 | −32.36% |
| The KN600 index | 14.63% | 19.01% | 0.7699 | −33.75% |

The index's own row reads 14.71% and 0.774 at `v0.15.0`, over the window both designs asked for.
This design's row is read from the rule's run, valued from 2017-01-04, the rule's first trade. The
refresh is not why it moved: the index is staged from the desk's own daily returns, not from the
provider's prices, and the reproduction, on a download never refreshed, returned the same row. Two
candidates were not traced: a different first valued day, which the first design did not record,
and a change in the desk's index files between the designs, whose holdings began in 2017 at
`v0.15.0` and begin on 2000-01-03 now. The first design's long window, from 2002-07-30 at 10.29%
and a −60.7% drawdown, held its membership fixed and has no counterpart here: Experiment 2, below,
is the first point-in-time window before 2017.

**Does it reproduce? Yes, every engine figure to the digit.** The second design's run of
2026-09-23 reached the end of its Verify section: 14 checks on the book and its weight file, and 92
on the runs, 90 of them window checks on the 45 engine runs, each valued on at least 99% of its
window's trading days. On 2026-09-24 it was reproduced from a wiped working copy, as its
blueprint's success criteria ask, with one manual step they do not allow for: a fresh clone on its
788-name seed and a fresh download from FMP through 2026-06-01, made at the working copy's commit
`50ebdad`, which holds the design's code. The universe stage then stopped, because the desk had
moved its files that day and the index was not staged. By hand, the clone moved to `45a690f`, which
sorts the slot book by date, and took `Data/hand_supplied.py` from `d7d1816`, which reads the
desk's new layout; the curator ran again to stage the index, and every later stage ran in order,
every notebook headless to the end of its Verify section, which raised nothing, in the first run's
environment. Every engine figure, sub-period and perturbation cell, and every figure the
attribution library returned, came back to the digit. The first design was reproduced on
2026-09-22, to the data rather than to the digit, as `v0.15.0` records.

**What the reproduction moved.** The panel holds 771 positions, against 772 in the run of
2026-09-23, whose download, refreshed through that day, carried `MIC`. The notebook's own sum of
unpriced weight read 0.01 more for four of the random books, for a reason not traced. And **the
book's construction figures are corrected**: 290 exits and 310 entries, a mean one-way turnover of
6.0% a trade date and 1.99 times the book a year, where the second design's run of 2026-09-23
printed 462, 482, 8.8% and 2.9. Pandas had assembled the slot book's rows in the order the names
first appeared, and each of those figures compares a row with the one before;
`portfolio_construction.build_slot_book` now sorts them by date. The engine reads each trade date's
weights by its date, so no engine figure moved. The capacity figures moved with them: *What stands*
has the corrected ones.

**On the seed of 1,500, described.** Experiment 1's notebook reads the whole seed, and a copy made
after `v0.18.0` holds the one Experiment 2 widened. Run on it once, from a wiped working copy on
2026-09-24 and 25, it prints the rule at 19.18% and 0.8720 against its control's 19.71% and 0.8204:
Sharpe +0.052 and CAGR −0.52 points, ahead in one sub-period of three, the same verdict; the
perturbation reads 11 of 15 cells where the seed of 788 gave the twelve criterion 3 asked for.
Description, never evidence: `FINDINGS_1.md` has the rows, and the design's record stays the seed of
788's.

### Experiment 2: the arm's design, on 2002 to 2016

The rule is Experiment 1's diagnostic arm, its rules unchanged at a 5% cash reserve where the arm
ran at 2%: the twenty most traded members of the index above their 50/200 cross, the whole set
re-equalised only on a day it moves by three names or more. The seed is widened to every listing the
index held since 2000, 1,500 identifiers, 712 of them from Sharadar, which keeps the companies that
left the market and publishes no VWAP, so those names fill at the day's close. The priced members
hold 99.59% of the index's weight or more on every date from 2001 to 2017, the years the run
printed, and the test starts on 2002-07-30, the first date its coverage rule allows. Run 2026-09-24,
from 12:38 to 13:34; net of costs.

| Book, 2002-07-30 to 2016-12-30 | CAGR | Volatility | Sharpe | Max drawdown |
| --- | ---: | ---: | ---: | ---: |
| The rule | 4.23% | 18.08% | 0.2340 | −53.32% |
| The rule, realistic costs | 5.86% | 18.03% | 0.3251 | −50.90% |
| The rule, every fill at the close | 4.29% | 18.10% | 0.2368 | −53.09% |
| The control, without the cross | 5.87% | 22.97% | 0.2556 | −65.43% |
| The control, realistic costs | 6.55% | 22.95% | 0.2854 | −64.71% |
| The control, every fill at the close | 5.91% | 23.00% | 0.2571 | −65.29% |
| The KN600 index | 8.57% | 19.56% | 0.4383 | −55.37% |

**It trails its control and the index on both measures.** The rule minus its control: Sharpe
−0.0216, CAGR −1.64 points, where prediction 1 asked for +0.03 and +0.5. With every name filled at
the close the margins are −0.0202 and −1.63, the same verdict, so the result does not depend on how
the dead names are filled. At the realistic cost row the Sharpe margin is +0.0397 and the CAGR
margin −0.69 points. Beta to the index: the rule 0.841, the control 1.141. **The kill switch
trips**: the rule is ahead of its control on both Sharpe and CAGR in none of three sub-periods,
2002–2006, 2007–2011 and 2012–2016. The perturbation fails as well: the rule is ahead on both in 1
of 10 cells, the band at 40%, where the blueprint asked for eight. Prediction 3 held narrowly:
inside 2007 to 2009 the rule's deepest fall was −53.32% against the index's −53.97%, measured the
same way.

**On the years it was found on, described and never evidence.** The same rule and control, on the
widened panel at the 5% reserve, over 2017-01-03 to 2026-06-01: the rule 19.11% at 0.8827, the
control 20.57% at 0.8976, **Sharpe −0.0148 and CAGR −1.46 points**. It is the first margin ever
measured for this design against its own control. It does not reproduce the arm's 19.52% in
Experiment 1, which ran on the 788-name seed at 2%.

**Attribution, over 2008-01-14 to 2016-12-30**, bound by the factor files' first date, with 1,351
of the 1,352 identifiers the book and the index name priced. The factor model leaves the rule
**−7.93** idiosyncratic points and its control **30.24**: the cross's share is −38.17. The
Brinson-Fachler alpha against the index is −42.29 points, of which selection +6.33 and interaction
−48.84, per asset. 2002 to 2007, and with them the sub-period in which the rule trailed its control
most, are not attributed.

**Does it reproduce? Yes, every figure.** The run was made in the working copy the widened data
and the rule were built in, and reached the end of its Verify section: 21 checks on the books and
the weight file, and 70 on the runs, 68 of them window checks on the 34 engine runs. A complete run
at the same settings from 09:38 to 10:15 printed every engine figure the same and skipped the
attribution, because the desk had just moved its files; it is superseded, not excluded. A wiped
working copy ran it again from 21:49 to 22:28 and printed every figure the same, engine and
attribution, with the raw downloads Experiment 3's reproduction below names.

### Experiment 3: momentum among the most traded, on 2002 to 2026

A new signal on the same names, for claim 5: of the hundred most traded members of the index, the
twenty with the highest return over the twelve months before the latest one, equally weighted and
re-struck on the first trading day of each month, against the same pool's twenty most traded on the
same dates. The panel, the exclusions and the 5% reserve are Experiment 2's. Run 2026-09-24, from
20:16 to 21:49, from a wiped working copy, with the working copy the rule was built in printing
every figure the same; net of costs.

| Book, 2002-07-30 to 2026-06-01 | CAGR | Volatility | Sharpe | Max drawdown |
| --- | ---: | ---: | ---: | ---: |
| The rule | 10.81% | 24.80% | 0.4358 | −65.57% |
| The rule, realistic costs | 13.00% | 24.74% | 0.5253 | −64.82% |
| The rule, every fill at the close | 10.80% | 24.82% | 0.4349 | −65.94% |
| The control, without the ranking | 11.03% | 23.73% | 0.4647 | −66.55% |
| The control, realistic costs | 11.76% | 23.71% | 0.4960 | −65.73% |
| The control, every fill at the close | 11.10% | 23.72% | 0.4677 | −66.10% |
| The KN600 index | 10.99% | 19.34% | 0.5682 | −55.37% |
| The null, the whole pool | 9.38% | 20.17% | 0.4651 | −61.56% |

**It trails its control and the index.** The rule minus its control: Sharpe −0.0289, CAGR −0.22
points, where prediction 1 asked for +0.03 and +0.5. With every name filled at the close the
margins are −0.0329 and −0.30, the same verdict. At the realistic cost row the CAGR margin turns to
+1.23 points and the Sharpe margin to +0.0293, still short of 0.03, with the rule's Sharpe below the
index's; the blueprint reads every verdict at the headline row, where the rule paid $780,587.10 of
commission against the control's $350,769.30. Beta to the index: the rule 1.084, the control 1.180.
**The kill switch trips**: the rule is ahead of its control on both Sharpe and CAGR in one of three
sub-periods, 2017–2026, at 22.49% against 18.03%, and behind in 2002–2008 and 2009–2016. On
2002-07-30 to 2016-12-30 alone, as description, it trails by 2.84 points a year. The perturbation
fails as well: ahead on both in 3 of 10 cells — twelve months with no skip, a pool of fifty and a
quarterly re-strike — where the blueprint asked for eight; four cells' rules could not be priced
and count against it. Prediction 3 held: from 2009-03-02 to 2009-12-31 the rule gained 29.14%
against its control's 65.93%.

**Attribution, over 2008-01-14 to 2026-06-01**, with 1,350 of the 1,351 identifiers the books and
the index name priced. The ranking adds 28.01 points of the momentum factor, 44.78 against the
control's 16.77, and takes 5.59 idiosyncratic points away, 82.30 against 87.88. The Brinson-Fachler
alpha against the index is +121.27 points, of which selection +27.74 and interaction +95.22, per
asset.

**Does it reproduce? Yes: the record is the run from a wiped working copy.** A clone at the commit
that holds the notebook, every pipeline output wiped and rebuilt from the curator on, printed every
figure the working copy printed. It kept the raw downloads: the FMP files downloaded fresh in the
same clone that morning for Experiment 1's reproduction, and the Sharadar names re-curated from the
bulk tables that morning's fetch had cached. That download lacks `MIC`, which has no price inside
the window in either copy. The notebook reached the end of its Verify section: 30 checks on the
books and the weight file, and 70 on the runs, 64 of them window checks on the 32 engine runs it
priced. Two earlier runs stopped before the end and are superseded: the first at the null, refused
over `WCOEQ`, and the second at the pool 150 cell, where the notebook raised at a refusal it now
records; `JOURNAL_3.md` has both.

### Experiment 4: momentum outside bear markets, on 2002 to 2026

Claim 5's second design: Experiment 3's ranking — of the hundred most traded members, the twenty
with the highest twelve-month return, re-struck monthly — held only outside a bear month, one that
opens after the KN US Equity 600's return over the prior 504 trading days below zero, and the pool's
twenty most traded inside one. The control is Experiment 3's; the diagnostic arm is Experiment 3's
rule, the ranking in every month, which the kill switch asks the rule to beat. The reserve is 10%,
and a check ends nine listings at their last distinct bar, both chosen after Experiment 3's run; the
state was chosen after Experiment 3's book lost the 2009 rebound, and the blueprint says so. Run
2026-09-25, from 07:41 to 09:26, from a wiped working copy, with the working copy printing every
figure the same but one line of the first cut; net of costs.

| Book, 2002-07-30 to 2026-06-01 | CAGR | Volatility | Sharpe | Max drawdown |
| --- | ---: | ---: | ---: | ---: |
| The rule | 11.61% | 24.29% | 0.4779 | −67.13% |
| The rule, realistic costs | 13.52% | 24.23% | 0.5578 | −66.43% |
| The rule, every fill at the close | 11.57% | 24.30% | 0.4763 | −67.08% |
| The control, without the ranking | 10.53% | 22.43% | 0.4694 | −64.42% |
| The control, realistic costs | 11.23% | 22.42% | 0.5007 | −63.58% |
| The control, every fill at the close | 10.61% | 22.43% | 0.4729 | −63.90% |
| The arm, momentum in every month | 10.34% | 23.43% | 0.4414 | −63.33% |
| The KN600 index | 10.99% | 19.34% | 0.5682 | −55.37% |
| The null, the whole pool | 8.94% | 19.06% | 0.4692 | −59.44% |

**It leads its control on return and misses on Sharpe.** The rule minus its control: Sharpe +0.0084,
CAGR +1.08 points, where prediction 1 asked for +0.03 and +0.5; with every name filled at the close,
+0.0034 and +0.97, the same verdict; at the realistic cost row, +0.0571 and +2.29, both margins
cleared, with the rule's Sharpe still below the index's. Beta to the index: the rule 1.097, the
control 1.115, the arm 1.023. **The kill switch trips on that one limb**: the rule is ahead of its
control on both measures in two sub-periods of three, 2002–2008 and 2017–2026, and ahead of the arm
on both, +0.0364 and +1.26 points. The perturbation fails: ahead on both in 5 of 12 cells, where the
blueprint asked for ten; every cell priced. Over the 2009 rebound, all bear months, the rule gained
61.74%, the control 61.72% and the arm 27.23%; on 2002-07-30 to 2016-12-30 alone, as description,
the rule trails its control by 0.65 points a year.

**Attribution, over 2008-01-14 to 2026-06-01**, with 1,350 of the 1,351 identifiers the books and
the index name priced. The conditioned ranking adds 8.84 idiosyncratic points over the control,
92.55 against 83.71, and the state 13.49 over the arm's 79.06; the rule's momentum line is 52.02
against the control's 15.94, and of the 32.05 points of excess return it earns over its control,
36.08 are that line's. The Brinson-Fachler alpha against the index is +125.59 points, of which
selection +26.49 and interaction +100.32, per asset.

**Does it reproduce? Yes: the record is the run from a wiped working copy**, and the working copy
printed every figure the same but the first cut's interaction, +100.31, where the wiped copy drops
`MIC` from the index. The notebook reached the end of its Verify section: 41 checks on the books and
the weight file, and 82 on the runs, 80 of them window checks on its 40 engine runs, every one
priced.

### The trial count

**Sixty-eight trials**, the count `BLUEPRINT_4.md` fixed: Experiment 4's rule, its diagnostic arm
and its twelve cells, after the fifty-four that follow.

**Fifty-four trials**, the count `BLUEPRINT_3.md` fixed: Experiment 3's rule and its ten cells,
after the forty-three that follow.

**Forty-three trials**, the count `BLUEPRINT_2.md` fixed. First the thirty-one `BLUEPRINT_1.md`
fixed: the first design's thirteen engine runs, ten reported and three excluded; the owner's
earlier test, counted as one, so the count is a lower bound; and the second design's rule, its
diagnostic arm and fifteen perturbation cells. Then Experiment 2's rule, counted again because it
meets new years, its ten cells, and the revision that raised its cash reserve to 5%.

**Experiment 1's second design ran 45 engine runs**: the rule, the control, the arm, the rule at
realistic costs, six sub-period runs, thirty sweep runs for fifteen cells and their controls, and
five random books. Its reproduction ran the same 45 on the same books and adds no trial.
**Experiment 2 ran 34**: the rule and the control, both again at realistic costs and with every
fill at the close, six sub-period runs, the two runs on the window the design was found on, and
twenty for ten cells and their controls. **Experiment 3 ran 36**, thirty-two priced and four not:
the rule, the control, the control with young listings and the null; the rule and the control on
2002 to 2016 alone; both again at realistic costs and with every fill at the close; six sub-period
runs; and twenty for ten cells and their controls. **Experiment 4 ran 40**, every one priced: the
rule, the control, the arm and the null; the rule and the control on 2002 to 2016 alone; both again
at realistic costs and with every fill at the close; six sub-period runs; and twenty-four for twelve
cells and their controls. Every run that is not the rule, an arm or a cell is a diagnostic, except
Experiment 2's two runs on the window the design was found on, and Experiments 3's and 4's nulls
and their runs on 2002 to 2016, which are description. Further runs are
excluded by name, below. The deflated Sharpe was not computed.

<!-- example: end -->

---

## What stands — reuse, do not rebuild

A result, a module or a method later work should start from rather than re-derive. One line each,
with its number.

<!-- example: begin -->

- **The panels and the pipeline.** Experiment 1's, on the 788-name seed, read to 2026-06-01: 6,390
  dates by 771 positions from the reproduction's fresh download, 772 from the download refreshed
  through 2026-09-23, with the index's membership from its own holdings, 2000-01-03 to 2026-08-14.
  Experiment 2's, on the seed widened to 1,500 identifiers, 712 of them from Sharadar: 6,390 dates
  by 1,437 positions, whose priced members hold 99.59% of the index's weight or more on every date
  from 2001 to 2017, the years its run printed. Experiment 3 read it unchanged, and measured
  coverage over its whole window: 99.71% at the lowest, on 2003-09-02.
- **The cross's drawdown effect, in all three books.** −32.20% against its control's −41.83% in
  Experiment 1's second design, −30.54% against the plain control's −39.79% in the first, and
  −53.32% against −65.43% in Experiment 2, on 2002 to 2016. That is the one thing the trend
  condition demonstrably does.
- **The truncation check, now the Verify section.** It counted each of Experiment 1's 45 engine
  runs and Experiment 2's 34 against its window's trading days, two checks a run, after three runs
  of the first design had reported success while valuing a stub. It raised on Experiment 2's first
  run: ten of its engine runs stopped short, valuing 42.5% to 47.4% of their windows, and still
  returned a summary; five of them stopped on 2009-05-18, the day of the rule's cash error.
- **The random arm as a baseline.** Before calling a residual "alpha", price random books of the
  same shape. Their mean was 22.4 against the rule's 36.19 points in Experiment 1's second design,
  and 12.5 against 45.5 in the first; no part of the factor model reveals it.
- **A control on the rule's own trade dates, from the start.** Experiment 1's second design's
  control traded on 114 dates, every one of them the rule's; Experiment 2's on the rule's 109 and on
  no other; Experiment 3's on the rule's 288. In the first design, matching the dates moved the
  filter's measured cost from −0.77 to −1.12 points a year.
- **A check of the fill convention.** Experiment 2's dead names fill at the close and every other
  name at the day's VWAP. Pricing the rule and its control again with every name filled at the
  close moved the margins from −0.0216 and −1.64 to −0.0202 and −1.63, so the verdict does not
  depend on the mix. In Experiment 3 they moved from −0.0289 and −0.22 to −0.0329 and −0.30.
- **A weight file rounds down.** The engine refuses a column above full exposure, and rounding a
  fully invested book to six decimals pushed one to 1.000002. `write_weight_file` rounds every
  weight down and leaves the remainder in cash.
- **A slot book in date order.** `portfolio_construction.build_slot_book` sorts its rows by date.
  Pandas had assembled them in the order the names first appeared, so every figure that compares a
  row with the one before — exits, entries, turnover, capacity — compared dates that were not
  neighbours. The first dry run of the daily paper-trading machinery found it.
- **A run the engine cannot price is named, never read.** Experiment 3's notebook records a run the
  engine refuses, or one that stops valuing the book before its window ends, by name with the
  engine's reason, and counts it against the rule as its blueprint fixed; its Verify section checks
  each is named. Four of its cells' rules were such runs: two overdrew the 5% reserve in 2003, and
  two held `VMW` into a month start its file has no price for.
- **A check that ends a listing at its last distinct bar.** Experiment 4's notebook cuts every price
  file at the window's end, finds each listing's last bar whose unadjusted open, high, low and close
  differ from the bar before, and reads any rows after it that repeat those four values as no price,
  for its panel and for the engine's staged copy of the files. It ended nine listings, and the
  engine refused none of Experiment 4's 40 runs, where it refused two of Experiment 3's over `VMW`.
  It uses hindsight up to the window's end, which its blueprint names.
- **Capacity, read from the book.** Each trade against its name's 63-day average traded value: at 1%
  of a day's traded value the worst trade limits Experiment 1's second design to $91,546,647 and its
  median trade to $16,231,104,636, Experiment 2's rule to $3,851,439 and $106,111,907,
  Experiment 3's to $6,933,709 and $92,928,116, and Experiment 4's to $6,933,709 and $107,323,816.
  The worst trade binds. The second design's run of
  2026-09-23 printed $2,018,972 and $14,574,799,654, read from rows out of date order; the
  reproduction's figures replace them.

## What is closed — do not re-propose without a new argument

Each rejected idea, with the number that rejected it. A negative result costs real work and stops
the next person repeating it; this list is where that value is stored.

- **The 50/200 cross as a return signal.** Closed by an information coefficient of 0.0112 at a
  month and −0.0060 at a year, and by three books that each earn less than the same names without
  it: 1.12 points a year in Experiment 1's first design, 0.86 in its second, and 1.64 in
  Experiment 2, on 2002 to 2016, which trails by 1.46 on 2017 to 2026 too. It is a risk control,
  not an alpha source.
- **The slow exit as the cross's rescue.** Closed by Experiment 2. The first design's band at
  twenty names earned 1.65 points a year more than the fast exit in Experiment 1, but it had never
  been set against the same names without the cross. Set against them it trails by 1.64 points a
  year on 2002 to 2016, ahead on both measures in none of three sub-periods and in 1 of 10
  perturbation cells, and by 1.46 on the years it was found on. Its lead was over a worse book, not
  over its control.
- **Fast exits on this signal, on this window.** Closed by the second design: selling the day after
  the cross breaks earned 1.65 points a year less than holding on through the first design's band,
  at twenty names, with the band's delay reproduced. Acting 5 or 21 days late narrowed the rule's
  shortfall against its control, −0.543 and −0.496 points against −0.86, rather than widening it,
  though both late books targeted `TWTR` after its last price and the engine held that weight in
  cash. Do not re-propose a faster exit on the 50/200 cross without a new argument.
- **Momentum among the most traded, as a long-only book re-struck monthly, at the blueprint's cost
  row.** Closed for two designs. Experiment 3's, the ranking in every month: 0.22 points a year less
  than the same pool's twenty most traded over 2002 to 2026, ahead of them on both measures in one
  sub-period of three and in 3 of 10 cells, with a ranking that takes idiosyncratic return away.
  Experiment 4's, the ranking only outside bear markets: 1.08 points a year more, in two sub-periods
  of three and ahead of the ranking in every month, but 0.0084 of Sharpe where 0.03 was required,
  and 5 of 12 cells. Not closed by either: the same design at a measured cost row, where the
  realistic one clears both of prediction 1's margins in Experiment 4, +0.0571 and +2.29 points.
  That is a new experiment with its own blueprint, never a rescue of this one.
- **The filter as protection against fast crashes.** Closed by 2020 in the first design: no cash
  held at all through a 23-day fall. It steps aside from slow declines only.
- **This book as a defensive position.** Closed on 2017 to 2026 by a beta of **1.028** in the
  first design and **1.067** in the second: holding the most traded names in an uptrend is a
  full-beta equity position there. On 2002 to 2016 Experiment 2's book carried a beta of **0.841**
  and still fell 53.32% inside 2007 to 2009, against the index's 53.97%: a lower beta without the
  protection. Each is shallower in drawdown than its index, and that is a different claim.
- **This book as lower-volatility than the index, on 2017 to 2026.** Closed by 20.73% in the
  first design and 22.18% in the second, against the index's 19.01%: twenty or thirty names were
  more volatile than six hundred there. On 2002 to 2016 Experiment 2's book was the calmer, 18.08%
  against the index's 19.56%, and earned 4.23% a year against 8.57%: lower volatility, and no
  reward for it.

### The uncomfortable one

`OBJECTIVE.md` claim 1 says stocks whose 50-day average is above their 200-day "go on to earn more
than those whose is not". **On our own data, inside our own universe, they do not**, and neither
design built to rescue the claim rescued it. The owner's diagnosis, that the band sold broken names
too late, was tested with its own arm and came back the wrong way: the late seller earned more.
Experiment 2 then took that late seller to 2002 to 2016, which it was not found on, and set it
against the same names without the cross for the first time: it trails them there by 1.64 points a
year, and on the years it was found on by 1.46. The claim survives only in a weaker form: less
volatility and a shallower drawdown than the same names unfiltered, in all three books, for 0.86
to 1.64 points a year less return.

## Open leads, ranked

The single highest-value run outstanding, and what it would settle.

**None of these can turn a verdict**: every book tested earns less than its control. They bear on
how the books are read. What followed Experiment 2 the owner decided on 2026-09-24: Experiment 3,
momentum proper on the same liquid names, under a claim of its own, claim 5
([`BRAINSTORMING_3.md`](Experiments/Experiment_3/BRAINSTORMING_3.md)). It ran the same day and
tripped its kill switch. On 2026-09-25 the owner chose Experiment 4, claim 5's second design: the
ranking held only outside bear markets
([`BRAINSTORMING_4.md`](Experiments/Experiment_4/BRAINSTORMING_4.md)). It ran the next day and
tripped its kill switch on its Sharpe margin alone; what follows it is the owner's to decide.

1. **The cost row, measured.** The verdict on prediction 1 turns on it in two experiments in a row:
   Experiment 3's CAGR margin is −0.22 points at the commission setting 0.1 and +1.23 at 0.005, and
   Experiment 4 clears both margins at 0.005, +0.0571 and +2.29 points, and neither setting was
   measured from an executable schedule for these trades. A blueprint that fixes its cost row from
   one, before its run, would settle which describes the book. Highest value.
2. **Repeated bars, a data check nobody wrote.** Nine FMP files end in a run of bars repeating their
   last distinct one inside 2002 to 2026: `CSC`, `ABMD`, `ATVI`, `VMW`, `SGEN`, `SRCL`, `ZIONO`,
   `CMA` and `SNCR`, `CSC`'s from 2017-04-03 to 2021-09-10. `VMW`'s left two of Experiment 3's cells
   unpriced. Experiment 4's notebook ends each at its last distinct bar, and none of its runs was
   refused; a check at the curator or the universe stage would give every experiment the same.
3. **The check for names held on their last priced day.** In Experiment 2 it printed none, where the
   engine's log names six in the rule's run, `BR1`, `PD1`, `BUD1`, `NFS`, `UST1` and `DNA1`, each
   sold at its last price, all of them Sharadar names. In Experiment 3 it read the window's last day
   as a last price and listed the names held there, where the log names thirty-one; in Experiment 4
   it read the day of the engine's sale, where the weight is already zero, and printed none where
   the log names twenty-three. The check is what should read it, on the day before.
4. **The third pass, Brinson-Fachler on the residual.** Not run for any experiment; criterion 2 of
   the gate cannot pass without it.
5. **Attribution before 2008.** Factor files reaching back to 2002 would attribute Experiment 2's
   first sub-period, where the rule trailed its control most, and Experiment 3's years before 2008.
6. **Sector factor files with data.** The desk's eleven are empty, so the sector lines read zero in
   every experiment and no sector claim stands.
7. **What survivorship costs**: the same rule on FMP's survivors alone, against Experiment 2's run,
   would price it, and both sets of files now exist.
8. **Far more random books, and the percentile.** Five seeds span −11.78 to 35.31 points in
   Experiment 1, and the rule sits just above their top; Experiments 2 and 3 priced none.
9. **The band read as a curve**, claim 4's full test: Experiment 1's arm measured one setting of it
   net of costs, and Experiment 2 four settings against the control at twenty names, the rule's 15%
   and its cells at 10%, 30% and 40%, with no direction. Choose the band on turnover and
   persistence, never on the metric it will be judged by. A new experiment, not an edit to either.

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
| Long window, 0.5% cash reserve | Valued only to 2003-04-22 of 23.8 years. The book could not pay commission at a rebalance — "Cash error on 2003-04-23 with $-416.34" — and the engine returned success with a clean summary over the stub. Caught by comparing the valued window against the requested one; the reserve is now an argument every run states |
| Long window, 1% cash reserve | The same failure in a different decade, valued to 2009-06-01. Both are in the trial count |
| Point-in-time, 0.5% cash reserve | Cash error on day one, when the book is entirely in the cash proxy and commission has nothing to come from |
| Second design, the first attempt, 2026-09-23 | Stopped at the rule's engine run: the engine refused a weight column whose gross exposure was 1.000002, because rounding a fully invested twenty-name book to six decimals pushed it past one. It produced no figure. `write_weight_file` in `Experiments/backtest_engine.py` now rounds every weight down, and the remainder goes to cash |
| Experiment 3, four perturbation cells' rules, 2026-09-24 | Not priced, each counted against the rule as `BLUEPRINT_3.md` fixed. Lookback 6 months and book size 10 stopped valuing the book after 2003-02-28 and 2003-08-29, at cash errors of −$16,557.91 on 2003-03-03 and −$19,025.14 on 2003-09-02, a full re-strike overdrawing the 5% reserve. Pools 150 and 200 were refused: each held `VMW` into 2023-12-01, which its file has no price for, between VMware's last trade on 2023-11-21 and bars that repeat it. The notebook names each with the engine's reason and reports no figure from any |
| Experiment 2, the first run, at a 2% cash reserve, 08:48 to 09:25 on 2026-09-24 | It could not be priced. Ten of its engine runs stopped short, each valuing 42.5% to 47.4% of its window's trading days, and its Verify section raised. Five of them, the rule's among them, stopped at 2009-05-18; the other five were last valued between 2008-09-16 and 2009-05-22. Only the rule's cause is logged, by the debugging run of the headline rule that followed: on 2009-05-18 a full re-equalisation on a rising day overdrew the reserve, a cash error of −$4,939.68, and the engine valued no later day while still returning a summary of the stub. Why the other nine stopped was not logged. No figure from the run is reported, nor from the debugging run. The blueprint was revised once, to a 5% reserve, before the rule ran again |

The first three are the first design's, at `v0.15.0`, and count in its thirteen engine runs. The
fourth priced no book, so it is not counted among the trials. Experiment 3's four are among its
thirty-six engine runs, and each cell is one of its trials. The last one's engine runs are not
among Experiment 2's thirty-four; the revision it led to counts as a trial.

<!-- example: end -->

## Known limitations

| # | Limitation | Effect |
| --- | --- | --- |
| 1 | **Nothing is out of sample.** No experiment has reached step 7 | Every number here is in-sample, and in-sample selection is what the deflation literature warns about |
| 2 | **A control arm differing in exactly one thing** — the same rule with one ingredient removed, on the rule's own rebalance dates — is missing from any experiment that claims a margin | Which lever earned that margin is inferred from per-lever rows, not measured |
| 3 | Classification buckets use today's labels, not point-in-time | Anything reclassified mid-window is misattributed before its move — the `current_*` prefix marks exactly this |
| 4 | Delisting exits use one day of hindsight | A position is sold on the last day it still has a fill price, knowable only the day after |
| 5 | Curator output is not reproducible across download dates | Dividend adjustment is computed from the present, so a re-pull rebases every adjusted column |
| 6 | The Deflated Sharpe Ratio has never been computed | The one number that would say whether a winner survives its own trial count |

<!-- example: begin -->

**Limitation 1 holds here with three qualifications.** Step 7's gate has been evaluated, against
both designs of Experiment 1, against Experiment 2 and against Experiment 3, and none graduated, so
no experiment has reached paper trading and nothing here is out of sample. And the daily machinery
has run: on 2026-09-24, in the working copy Experiment 1's second design ran in, on that design
frozen there as a candidate only to test the plumbing, never committed. Those runs priced days after
2026-06-01, and no figure from them is read here;
[`Paper_Trading/BITACORA.md`](Paper_Trading/BITACORA.md) says what they showed. And one book is on
paper without graduation: Experiment 4's, frozen on 2026-09-25 as a candidate by the owner's
decision, whose months after 2026-06-01 are the first this example prices unseen;
`Paper_Trading/BITACORA.md` registers it, and nothing its record shows can graduate it.

**Limitation 2 no longer holds in this example.** Every experiment has a control arm differing in
exactly one thing, on the rule's own trade dates: the trend condition in Experiments 1 and 2, the
momentum ranking in Experiment 3. That is why this repository can say the cross costs 0.86 points
a year in Experiment 1's second design, 1.12 in its first and 1.64 in Experiment 2, and the ranking
0.22 in Experiment 3, instead of inferring it. Limitation 6 still stands, and has company: the
idiosyncratic share is measured against a five-seed random baseline in Experiment 1, which is a
floor on the honest figure rather than a deflated one, and against no random baseline in
Experiments 2 and 3.

Five more, specific to this example:

| # | Limitation | Effect |
| --- | --- | --- |
| 7 | **Experiment 1's seed never holds the whole index**: 39.8% of its members on 2000-01-03, and on no date through 2026-08-14 as many as 99% of them, by the universe runs of 2026-09-23 and 2026-09-24. Its share of the index's weight was not measured by any run recorded here | The rest of the index was never selectable, by any rule or arm of Experiment 1. Experiment 2 widened the seed to every listing the index held since 2000: its priced members hold 99.59% of the index's weight or more on every date from 2001 to 2017, the years its run printed |
| 8 | **Limitation 5, met: the refresh of 2026-09-23 rebased the adjusted prices** the first design ran on | The two designs sit on two downloads; compare each with its own control and index row. The index row moved too, 14.63% against 14.71% at `v0.15.0`, but not with the refresh: it is staged from the desk's own returns, and the second design's own two downloads, refreshed and fresh, gave the same engine figures, the index's included. A different first valued day, or a change in the desk's index files, may explain it; neither was traced |
| 9 | **Experiments 2 and 3 have two providers and two Curator versions.** The 712 names added fill at the close, from Sharadar through the Data Curator's `issues/31` branch at `8b54c2f`, built as 0.49.1; every other name at the day's VWAP, from FMP through 0.50.0 | The fill check prices the difference and the verdict does not change. To fetch those names a copy of this example needs a Sharadar key and a Data Curator with the Sharadar provider; the branch was the only version with it when Experiment 2 ran, and `JOURNAL_2.md` records how it was called |
| 10 | **Experiments 2 and 3 were reproduced from a wiped working copy that kept its raw downloads**: FMP files downloaded fresh through 2026-06-01 in that clone the same morning, and Sharadar names re-curated from the bulk tables that morning's fetch had cached | Every figure matched the working copy's. A reproduction that also fetches afresh would meet limitation 5: a later download rebases every adjusted column |
| 11 | **Nine FMP files end in bars that repeat their last distinct one**, `VMW`'s after a gap across a month start | Experiment 4's notebook ends each at its last distinct bar; no other stage or experiment does. Elsewhere the engine refuses a book that holds such a name on a date its file skips, as it refused two of Experiment 3's cells, and values one held across the repeated bars at a flat price |

<!-- example: end -->

> **Under the bar in [`AGENTS.md`](AGENTS.md), most numbers above are a reason to run an experiment
> rather than a result.**
