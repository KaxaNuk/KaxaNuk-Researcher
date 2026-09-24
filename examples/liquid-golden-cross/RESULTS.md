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
> and the numbers are real: Experiment 1's second design, run 2026-09-23 and reproduced from a wiped
> working copy on 2026-09-24, with its first design kept as a row. Experiment 2 is open, and none of
> its results is reported here. Step 7's gate has been *evaluated* against each design of Experiment
> 1 and neither passes. No book is on paper, so **nothing here is out of sample**. Which criteria
> each fails and why is in [`Paper_Trading/BITACORA.md`](Paper_Trading/BITACORA.md).

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
blueprint reads a Sharpe edge that comes with a lower beta as timing.

**Nothing has earned a lever, and the one surprise is Experiment 2's to test.** The first design's
rebalancing, kept at twenty names on a 15% band as a diagnostic arm, reproduced its delay and earned
1.65 points a year more than the fast exit, so exit speed is not why the cross loses. Experiment 2
takes that arm's design to years before 2017, which it was not found on, from the first date its
blueprint's coverage rule allows, no earlier than 2002-07-30, to 2016-12-30, against the same names
without the cross; it is open. Claim 1 stays falsified, and nothing graduates.

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
analyzer's Verify section ran its 8 checks.

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

**One window, two downloads.** Experiment 1's two designs both run 2017-01-03 to 2026-06-01, net of
costs. The panel was refreshed on 2026-09-23 before the second ran, which rebases every adjusted
column, so compare each design with its own control and index row; the second design's reproduction,
on a fresh download through 2026-06-01, returned every engine figure to the digit. In every row the
control is the same book without the trend condition, trading on the rule's own dates: in the first
design, the equalised control. **`vs control` is a Sharpe difference, and it hides the CAGR**: each
book earns less than its control, by 0.86 points a year in the second design and 1.12 in the first.

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
candidates were not traced: a different first valued day, which the first design did not record, and
a change in the desk's index files between the designs, whose holdings began in 2017 at `v0.15.0`
and begin on 2000-01-03 now. The first design's long window, from 2002-07-30 at 10.29% and a −60.7%
drawdown, held its membership fixed and has no counterpart here: Experiment 2, open, is to be the
first point-in-time window before 2017.

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

### Experiment 2: open

The owner opened it on 2026-09-24, once the second design had failed its kill switch: the diagnostic
arm's design, its rules unchanged, on years before 2017, which it was not found on, from the first
date its blueprint's coverage rule allows, no earlier than 2002-07-30, to 2016-12-30, against the
same names without the cross, with the seed widened to every name the index held since 2000.
[`BLUEPRINT_2.md`](Experiments/Experiment_2/BLUEPRINT_2.md) is committed before its rule, and none
of its results is reported here.

### The trial count

**Thirty-one trials**, the count `BLUEPRINT_1.md` fixed: the first design's thirteen engine runs,
ten reported and three excluded; the owner's earlier test, counted as one, so the count is a lower
bound; and the second design's rule, its diagnostic arm and fifteen perturbation cells.

**Experiment 1's second design ran 45 engine runs**: the rule, the control, the arm, the rule at
realistic costs, six sub-period runs, thirty sweep runs for fifteen cells and their controls, and
five random books. Its reproduction ran the same 45 on the same books and adds no trial. Every run
that is not the rule, the arm or a cell is a diagnostic. One further attempt is excluded by name,
below. The deflated Sharpe was not computed.

<!-- example: end -->

---

## What stands — reuse, do not rebuild

A result, a module or a method later work should start from rather than re-derive. One line each,
with its number.

<!-- example: begin -->

- **The panel and the pipeline.** Experiment 1's, on the 788-name seed, read to 2026-06-01: 6,390
  dates by 771 positions from the reproduction's fresh download, 772 from the download refreshed
  through 2026-09-23, with the index's membership from its own holdings, 2000-01-03 to 2026-08-14.
- **The cross's drawdown effect, in both designs.** −32.20% against its control's −41.83% in
  Experiment 1's second design, and −30.54% against the plain control's −39.79% in the first. That
  is the one thing the trend condition demonstrably does.
- **The truncation check, now the Verify section.** It counted each of Experiment 1's 45 engine runs
  against its window's trading days, two checks a run, after three runs of the first design had
  reported success while valuing a stub.
- **The random arm as a baseline.** Before calling a residual "alpha", price random books of the
  same shape. Their mean was 22.4 against the rule's 36.19 points in Experiment 1's second design,
  and 12.5 against 45.5 in the first; no part of the factor model reveals it.
- **A control on the rule's own trade dates, from the start.** Experiment 1's second design's
  control traded on 114 dates, every one of them the rule's. In the first design, matching the dates
  moved the filter's measured cost from −0.77 to −1.12 points a year.
- **A weight file rounds down.** The engine refuses a column above full exposure, and rounding a
  fully invested book to six decimals pushed one to 1.000002. `write_weight_file` rounds every
  weight down and leaves the remainder in cash.
- **A slot book in date order.** `portfolio_construction.build_slot_book` sorts its rows by date.
  Pandas had assembled them in the order the names first appeared, so every figure that compares a
  row with the one before — exits, entries, turnover, capacity — compared dates that were not
  neighbours. The first dry run of the daily paper-trading machinery found it.
- **Capacity, read from the book.** Each trade against its name's 63-day average traded value: at 1%
  of a day's traded value the worst trade limits Experiment 1's second design to $91,546,647 and its
  median trade to $16,231,104,636. The worst trade binds. The second design's run of 2026-09-23
  printed $2,018,972 and $14,574,799,654, read from rows out of date order; the reproduction's
  figures replace them.

## What is closed — do not re-propose without a new argument

Each rejected idea, with the number that rejected it. A negative result costs real work and stops
the next person repeating it; this list is where that value is stored.

- **The 50/200 cross as a return signal.** Closed by an information coefficient of 0.0112 at a month
  and −0.0060 at a year, and by two books that each earn less than the same names without it: 1.12
  points a year in Experiment 1's first design and 0.86 in its second. It is a risk control, not an
  alpha source.
- **Fast exits on this signal, on this window.** Closed by the second design: selling the day after
  the cross breaks earned 1.65 points a year less than holding on through the first design's band,
  at twenty names, with the band's delay reproduced. Acting 5 or 21 days late narrowed the rule's
  shortfall against its control, −0.543 and −0.496 points against −0.86, rather than widening it,
  though both late books targeted `TWTR` after its last price and the engine held that weight in
  cash. Do not re-propose a faster exit on the 50/200 cross without a new argument.
- **The filter as protection against fast crashes.** Closed by 2020 in the first design: no cash
  held at all through a 23-day fall. It steps aside from slow declines only.
- **This book as a defensive position.** Closed on 2017 to 2026 by a beta of **1.028** in the first
  design and **1.067** in the second: holding the most traded names in an uptrend is a full-beta
  equity position there. Each is shallower in drawdown than its index, and that is a different
  claim.
- **This book as lower-volatility than the index, on 2017 to 2026.** Closed by 20.73% in the first
  design and 22.18% in the second, against the index's 19.01%: twenty or thirty names were more
  volatile than six hundred there.

### The uncomfortable one

`OBJECTIVE.md` claim 1 says stocks whose 50-day average is above their 200-day "go on to earn more
than those whose is not". **On our own data, inside our own universe, they do not**, and the design
built to rescue the claim did not rescue it. The owner's diagnosis, that the band sold broken names
too late, was tested with its own arm and came back the wrong way: the late seller earned more. The
claim survives only in a weaker form: less volatility and a shallower drawdown than the same names
unfiltered, in both designs, for 0.86 to 1.12 points a year less return.

## Open leads, ranked

The single highest-value run outstanding, and what it would settle.

**None of these can turn Experiment 1's verdict**: both of its designs earn less than their
controls. The first is a new experiment, with its own gate; the rest bear on how the books are read.

1. **Experiment 2: the arm's design on years before 2017**, which it was not found on, from the
   first date its blueprint's coverage rule allows, no earlier than 2002-07-30, to 2016-12-30,
   against the same names without the cross, with the seed widened to every name the index held
   since 2000. The owner opened it on 2026-09-24, and its blueprint is committed before its rule. It
   also puts 2008 inside a point-in-time window for the first time. Highest value.
2. **The third pass, Brinson-Fachler on the residual.** Not run for either design; criterion 2 of
   the gate cannot pass without it.
3. **Sector factor files with data.** The desk's eleven are empty, so the sector lines read zero in
   both designs and no sector claim stands.
4. **Far more random books, and the percentile.** Five seeds span −11.78 to 35.31 points, and the
   rule sits just above their top.
5. **The band read as a curve**, claim 4's full test: Experiment 1's arm measured one setting of it,
   net of costs. Choose the band on turnover and persistence, never on the metric it will be judged
   by. A new experiment, not an edit to Experiment 1.

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

The first three are the first design's, at `v0.15.0`, and count in its thirteen engine runs. The
fourth priced no book, so it is not counted among the trials.

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

**Limitation 1 holds here with two qualifications.** Step 7's gate has been evaluated, against both
designs of Experiment 1, and neither graduated, so no experiment has reached paper trading and
nothing here is out of sample. And the daily machinery has run: on 2026-09-24, in the working copy
Experiment 1's second design ran in, on that design frozen there as a candidate only to test the
plumbing, never committed. Those runs priced days after 2026-06-01, and no figure from them is read
here; [`Paper_Trading/BITACORA.md`](Paper_Trading/BITACORA.md) says what they showed.

**Limitation 2 no longer holds in this example.** Every experiment has a control arm differing in
exactly one thing, the trend condition, on the rule's own trade dates. That is why this repository
can say the cross costs 0.86 points a year in Experiment 1's second design and 1.12 in its first,
instead of inferring it. Limitation 6 still stands, and has company: the idiosyncratic share is
measured against a five-seed random baseline, which is a floor on the honest figure rather than a
deflated one.

Two more, specific to this example:

| # | Limitation | Effect |
| --- | --- | --- |
| 7 | **Experiment 1's seed never holds the whole index**: 39.8% of its members on 2000-01-03, and on no date through 2026-08-14 as many as 99% of them, by the universe runs of 2026-09-23 and 2026-09-24. Its share of the index's weight was not measured by any run recorded here | The rest of the index was never selectable, by any rule or arm of Experiment 1. Experiment 2's blueprint widens the seed to every listing the index held since 2000 |
| 8 | **Limitation 5, met: the refresh of 2026-09-23 rebased the adjusted prices** the first design ran on | The two designs sit on two downloads; compare each with its own control and index row. The index row moved too, 14.63% against 14.71% at `v0.15.0`, but not with the refresh: it is staged from the desk's own returns, and the second design's own two downloads, refreshed and fresh, gave the same engine figures, the index's included. A different first valued day, or a change in the desk's index files, may explain it; neither was traced |

<!-- example: end -->

> **Under the bar in [`AGENTS.md`](AGENTS.md), most numbers above are a reason to run an experiment
> rather than a result.**
