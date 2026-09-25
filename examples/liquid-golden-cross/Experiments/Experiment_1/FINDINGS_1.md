# Findings — Experiment 1

> **Latest valuable results only.** This file is rewritten when a result changes, not appended to —
> the running history is in [`JOURNAL_1.md`](JOURNAL_1.md), and the hypothesis this tested is in
> [`BLUEPRINT_1.md`](BLUEPRINT_1.md).
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

**Experiment 1's second design ran end to end on 2026-09-23, was reproduced from a wiped working
copy on 2026-09-24, and does not graduate.** The rule holds the twenty most traded members of the
index above their 50/200 cross and sells a name the day after its cross breaks. It beats the index
on Sharpe, 0.806 against 0.770, and its control on Sharpe by 0.031. It earns **0.86 points a year
less** than its control, so the margins of prediction 1 are not met, and **the kill switch trips**:
the rule is ahead of its control on both Sharpe and CAGR in one sub-period of three. It is not a
candidate for the gate in `Paper_Trading/BITACORA.md`, which records the gate's rows anyway. The
reproduction returned every engine figure to the digit and corrected the book's construction and
capacity figures, which the first run had read from rows out of date order.

**The claim it moved: claim 1 of `OBJECTIVE.md`, the signal, stays falsified, and exit speed is
ruled out as the reason.** The diagnostic arm reproduced the first design's delay and earned 1.65
points a year more than the rule, not less. Selling a broken cross fast is not where the cross
earns. **Claim 4, the rebalancing, moves from untested to measured**, and no further, as the
blueprint fixed: at twenty names, a band of 15% beat the fast exit net of costs, on one window, as
one arm. The claim names a 10% band; 15% is the setting that keeps the first design's behaviour at
twenty names. *Measured* is the status the blueprint fixed for this arm, reached on an
engine-priced book rather than on the analyzer the vocabulary of `OBJECTIVE.md` names for it. The
band read as a curve is still a new experiment.

**The success criteria `BLUEPRINT_1.md` set, each answered.**

| # | Criterion | State |
| --- | --- | --- |
| 1 | Beats the index on Sharpe, and its control by the margins of prediction 1, net, at the headline cost row, over the window | **Not met.** Sharpe 0.8057 against the index's 0.7699 and the control's 0.7748, but CAGR 0.86 points a year below the control |
| 2 | The kill switch is silent | **Not met.** Both of its limbs fire: the whole-window margins, and one sub-period of three |
| 3 | Reproduces from a wiped working copy | **Shown, 2026-09-24, with one manual step.** A fresh clone of the working copy the design ran in, on its 788-name seed, and a fresh download from FMP through 2026-06-01, made with the clone at that copy's commit `50ebdad`, which holds the design's code. The universe stage, run next, stopped: the desk had moved its files that day, and the curator had not staged the index. By hand, the clone then moved to `45a690f`, the commit that sorts the slot book by date, and took `Data/hand_supplied.py`, which reads the desk's new layout, from `d7d1816`; the curator ran again to stage the index, and the universe, the refinery, the analyzer and the experiment ran in order, the notebooks headless, each to the end of its Verify section, in the first run's environment. The blueprint asks for no manual step, and this was one. Every engine figure, sub-period and perturbation cell, and every figure the attribution library returned, came back to the digit. The construction and capacity figures did not: `45a690f`'s sort corrected them, and *What the benchmark actually is* has the corrected ones |
| 4 | Trades on fewer days than it does not | **Met.** 311 trade dates in the window, 33.1 a year, and the invariant passed |
| 5 | Every prediction evaluated in this file | **Met.** Three rows below: one held, two failed |

**No run of this experiment has read the months after the window.** The data stages of 2026-09-23
did: that download was refreshed through 2026-09-23 and the universe and the refinery re-ran on it,
but the notebook cuts its panel at 2026-06-01. The reproduction's download stops at 2026-06-01. The
paper-trading machinery was tested on 2026-09-24 in the working copy the design ran in, on this
design frozen there as a candidate and never committed, and those runs priced days after
2026-06-01; no figure from them is read here. The blueprint reports those months beside the verdict
once a book is frozen, and nothing in this repository is frozen.

**The owner's decision, 2026-09-24.** The rule failed its kill switch, and the diagnostic arm did
better than the fast exit. He chose to confirm the arm's design on years it was not found on, before
2017, as Experiment 2: from the first date its blueprint's coverage rule allows, no earlier than
2002-07-30, to 2016-12-30, with the seed widened to every name the index held since 2000. It goes
to paper trading only if it passes its own gate.

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
read net, at the headline cost row, over 2017-01-03 to 2026-06-01.

| # | Prediction | Outcome | What it changed |
| --- | --- | --- | --- |
| 1 | The rule beats its control, the same twenty names without the cross, by at least 0.03 of Sharpe and 0.5 points a year of CAGR | **Failed.** Sharpe +0.031, which clears its margin; CAGR **−0.86 points**, on the wrong side of zero | Selling a break the next day did not make the cross a return signal. It still buys a steadier book rather than a richer one: volatility 22.18% against the control's 24.17%, drawdown −32.20% against −41.83% |
| 2 | The diagnostic arm, with the first design's delay, earns less than the rule | **Failed, the other way.** The arm reproduced the delay, holding a broken name a median of 28 days, on 6,510 of its 47,280 held name-days, and earned **1.65 points a year more**: 19.52% against 17.87%, Sharpe 0.8773 against 0.8057 | Exit speed is ruled out as the reason the first design lost to its control. The drift the analyzer measured after a break is small, and selling into it did not pay. The reversal `BLUEPRINT_1.md` named among its key risks fits that, and the delay cells of the perturbation point the same way, with the `TWTR` artefact of caveat 8 in both |
| 3 | The rule's margin over its control is largest in 2020–2022, which holds the window's two sharpest declines | **Held.** 2020–2022 is the only sub-period in which the rule is ahead on both measures: Sharpe 0.324 against 0.046, CAGR 8.5% against 1.4%. In the other two the control is ahead on both | The cross earns in the window's declines, as its mechanism says, and what it earns there does not pay for what it costs in the other two |

One held, two failed. **The second failure taught the most.** The rewrite was built on one
diagnosis, that the first design's band held broken names too long. The arm built to confirm that
diagnosis beat the rule it was meant to lose to. Only a prediction written down before the run
makes that a finding rather than a setting to tune.

### The kill switch

**It trips, on both limbs.** The blueprint fixed one condition for the whole experiment: the
margins of prediction 1 over the whole window, and the rule ahead of its control on both Sharpe and
CAGR in at least two of three sub-periods. Each sub-period was priced by the engine as a window of
its own, its control held to that rule's trade dates. The rule enters on the sub-period's second
trading day, the first the one-day lag allows: the engine valued the three rule books, and their
controls, from 2017-01-04, 2020-01-03 and 2023-01-04.

| Sub-period | Sharpe, the rule | Sharpe, the control | CAGR, the rule | CAGR, the control | Ahead on both |
| --- | ---: | ---: | ---: | ---: | --- |
| 1, 2017-01-03 to 2019-12-31 | 0.935 | 1.015 | 14.9% | 17.3% | no |
| 2, 2020-01-02 to 2022-12-30 | 0.324 | 0.046 | 8.5% | 1.4% | **yes** |
| 3, 2023-01-03 to 2026-06-01 | 1.366 | 1.929 | 30.7% | 40.5% | no |

**One of three.** The changes that may not rescue it are the blueprint's: the book size of twenty,
the buffer of thirty, the monthly re-equalisation, the 50 and 200-day pair, the 63-day ranking
window, the one-day lag, the window, the five exclusions and the costs. None was moved after the
result. The perturbation below reads each as a curve, not as a rescue.

<!-- example: end -->

## The book, priced by the engine

Record the date of the last full re-run from a wiped working copy, the engine version, and the
window. Then the book against every benchmark it reports against, and against the control its
blueprint names, on the rule's own rebalance dates: CAGR, volatility, Sharpe, Sortino, maximum
drawdown.

<!-- example: begin -->

**Run 2026-09-23, and reproduced from a wiped working copy on 2026-09-24**, with KaxaNuk Backtest
Engine 0.66.0 and Attribution Analysis 0.2.0, the versions installed on 2026-09-22 in the
environment both runs used; no cell prints them. The first run read to 2026-06-01 a download
refreshed through 2026-09-23; the reproduction, a fresh clone on a fresh download through
2026-06-01, returned each of this design's figures below to the digit. The window asked of the
engine is **2017-01-03 to 2026-06-01**. Of the runs over the whole window, it valued the rule, its
control, the rule at realistic costs and every perturbation cell and control from 2017-01-04, the
rule's first trade, over 2,364 trading days; the diagnostic arm and the five random books from
2017-01-03, over 2,365, because their weight files open on that day holding only `SHY`, the cash
proxy: the files show it, and no cell prints it. The index row is the rule run's benchmark, so it
too starts on 2017-01-04. The Verify section found every run valued on at least 99% of its window's
trading days. Costs are the blueprint's: the commission setting 0.1, which the engine charges in
dollars a share — every forced sale was charged $0.10 a share at it, $168.90 on 1,689 shares of
`TWTR` in the rule's run — and 5 basis points of slippage. The 2% cash reserve and the $1,000,000
are the notebook's, not the blueprint's. The blueprint's "about eight cents a share" is the first
design's figure, and neither run re-measured it. Results are net.

| Book | CAGR | Volatility | Sharpe | Max drawdown | Alpha | Information ratio | Commissions | Slippage | Trade dates |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **The rule** | **17.87%** | 22.18% | **0.8057** | −32.20% | 3.23% | 0.4798 | $76,911.00 | $37,862.98 | 311 |
| The control, without the cross | 18.73% | 24.17% | 0.7748 | −41.83% | 4.10% | 0.6456 | $25,513.20 | $12,133.10 | 114 |
| The diagnostic arm, the first design's rule at a 15% band | 19.52% | 22.25% | 0.8773 | −32.36% | 4.81% | 0.6380 | $51,451.00 | $23,581.40 | 41 |
| The rule, realistic costs | 18.36% | 22.17% | 0.8280 | −32.15% | 3.73% | 0.5175 | $3,944.74 | $38,942.00 | 311 |
| The KN600 index | 14.63% | 19.01% | 0.7699 | −33.75% | — | — | — | — | — |

The rule minus its control: **Sharpe +0.031, CAGR −0.86 points**. Beta to the index, from the
engine's daily series: **the rule 1.067, the control 1.238, the diagnostic arm 1.093**. Sortino is
not printed by the notebook, although the engine's report carries it; no Sortino figure is quoted
here. The control traded on 114 dates, every one of them a trade date of the rule. The arm's weight
file holds 41 dates, the first wholly in `SHY`, and its band chose the rest.

**The index's own row moved.** At `v0.15.0`, over the window that design also asked for, 2017-01-03
to 2026-06-01, the index read 14.71% and 0.774; here, read from the rule's run and valued from
2017-01-04, it reads 14.63% and 0.7699. The refresh of the panel is not among the causes: the
curator stages the index from the desk's own daily returns, not from the provider's prices, and the
reproduction, on a download that was never refreshed, returned this row to the digit. Two
candidates remain, and neither was traced: a different first valued day, since the first design's
findings do not record the day its run first valued the index; and a change in the desk's index
files between the two designs, whose holdings began in 2017 at `v0.15.0` and begin on 2000-01-03
in both runs of this one. Each design is read against its own index row.

### The first design, superseded

Kept at tag `v0.15.0` of the KaxaNuk Researcher, where its findings are whole: thirty names,
re-equalised whenever the set moved by a tenth, run on the panel before the refresh. Its headline
figures, as that tag records them:

| Book, first design | CAGR | Volatility | Sharpe | Max drawdown | Rebalances |
| --- | ---: | ---: | ---: | ---: | ---: |
| The rule | 17.85% | 20.73% | 0.861 | −30.54% | 87 |
| The equalised control, the filter off on the rule's dates | 18.97% | not reported | 0.831 | not reported | 87 |
| The plain control, the filter off on its own band | 18.62% | 22.91% | 0.813 | −39.79% | 11 |
| The KN600 index | 14.71% | 19.01% | 0.774 | −33.75% | — |

The filter cost 1.12 points a year against the equalised control. The rule's beta was 1.028, and
of its 45.52 idiosyncratic points about 5 belonged to the filter. Claim 1 was falsified on them.

### On the seed of 1,500, described

**Description, never evidence, and not the design's record.** This notebook reads the whole seed,
and a copy made after `v0.18.0` holds the 1,500 identifiers Experiment 2 widened it to. It was run
on them once, from a wiped working copy, from 22:28 on 2026-09-24 to 00:04 on 2026-09-25, to the end
of its Verify section: 14 checks on the book and 92 on its 45 engine runs. The panel holds 6,390
dates by 1,436 positions. Over the same window:

| Book, the seed of 1,500 | CAGR | Volatility | Sharpe | Max drawdown | Trade dates |
| --- | ---: | ---: | ---: | ---: | ---: |
| The rule | 19.18% | 22.00% | 0.8720 | −32.20% | 306 |
| The control, without the cross | 19.71% | 24.02% | 0.8204 | −41.43% | 114 |
| The diagnostic arm | 19.68% | 22.26% | 0.8840 | −32.09% | 42 |
| The rule, realistic costs | 19.66% | 22.00% | 0.8938 | −32.15% | 306 |
| The KN600 index | 14.63% | 19.01% | 0.7699 | −33.75% | — |

**The verdict does not change, and one row of the gate reads differently.** The rule minus its
control: Sharpe +0.052 and CAGR −0.52 points, against +0.031 and −0.86 on the seed of 788, so
prediction 1's margins are not met; the rule is ahead of its control on both measures in one
sub-period of three, the second, and the kill switch trips. The perturbation reads 11 of 15 cells
keeping the sign of the rule's Sharpe margin, where the blueprint asked for twelve and the seed of
788 gave twelve. The arm earns 0.50 points a year more than the rule, against 1.65. The factor
model, over 2017-01-04 to 2026-06-01 with 1,351 of the 1,399 identifiers the books name priced,
leaves the rule 44.07 idiosyncratic points and its control 50.75, against five random books' −4.42
to 23.22, mean 13.9; the rule's momentum line is 15.38 against the control's 5.19, and the betas are
1.062 and 1.232. The rows above this section stand as the design's, at `v0.18.0`; these are what a
copy made now prints.

<!-- example: end -->

## What the benchmark actually is, structurally

Rebalance frequency, turnover, holdings, concentration, invested share, and any structural tilt —
each with a reading of what a bad value would have meant.

<!-- example: begin -->

**The panel and the book, sections 1 to 3, as the reproduction of 2026-09-24 printed them.** The
panel read to 2026-06-01 holds 6,390 dates by 771 positions, with the index's membership known from
its holdings from 2000-01-03 to 2026-08-14. The run of 2026-09-23 read 772: the provider returned
nothing for `MIC` through 2026-06-01, and the refinery read 787 securities where the download
refreshed through 2026-09-23 gave it 788. The book passed all nine invariants of section 2.1, and
its weight file holds 99 identifiers by 311 trade dates, every column summing to one, with a cash
weight of 0.000 on the first date and on average.

Read in section 3 from the book's targets held forward between trade dates: its shape, not its
return.

| Property | Value | What a bad value would have meant |
| --- | --- | --- |
| Trade dates | 311 in the window, 33.1 a year, from 2017-01-04. The window holds 114 first trading days of a month, 2017-01-03 among them, on which the buffer is checked and the book re-equalised; how many of the 311 fall on one was not counted | A rule trading on most days would be a cost question, not an alpha one. The invariant that it trades on fewer days than it does not passed |
| Exits and entries | 290 exits, 310 entries | The fast exit is the design: every trade date that is not a first day of a month is an exit, a slot filled, or both |
| Round trips within five days | 1 | The whipsaw the blueprint feared, a name sold and bought back as its averages cross and recross, would show here. It barely happened |
| Mean one-way turnover per trade date | 6.0% | Small trades on many dates, rather than large trades on few |
| Annual turnover, target to target | 1.99 times the book | The first design's was 165%, so the fast exit trades more. The engine's realised turnover was not read |
| Holdings and effective positions | 20.0 and 20.0 | Equal by construction; a gap would mean hidden concentration |
| Mean invested share | 99.9%, lowest 0.0% before the first trade | A low figure would mean slots left empty. The weight file's cash row averages 0.000 |
| Held on a day the cross closed at 0 | 231 of 47,280 held name-days | The rule sells the next day, so each break costs one such day. The lagged measure, what the rule could see, is 0 |
| Broken name-days, the diagnostic arm | 6,510 of 47,280, a median of 28 days held after a break | The delay the arm had to reproduce, or its verdict on exit speed was void. The first design's median was 19 |
| Sector drift | Technology 26.2% in 2017, 13.6% in 2022, 45.1% in 2024, 50.0% in 2026; Healthcare 27.8% in 2022 | A flat line would mean the rotation is a label. The book leans on technology, as the blueprint said twenty names would, and nothing constrains it |

**The reproduction corrected four of these figures**: exits, entries and both turnover figures,
which the run of 2026-09-23 printed as 462, 482, 8.8% and 2.9 times. Pandas had assembled the slot
book's rows in the order the names first appeared in it, not in date order, and each of those
figures compares a row with the one before it, so it compared dates that were not neighbours.
`portfolio_construction.build_slot_book` now sorts the rows by date. Round trips read the rows in
sequence too, and came back 1 both times. The engine reads each trade date's weights by its date,
so no engine figure moved; holdings, invested share, the broken name-days and the sector drift read
the book laid on the window's calendar, and did not move either.

**Capacity, criterion 4 of the gate.** This measurement was added to section 3 after the
blueprint's commit and before the run. It measures construction, not a figure the blueprint
predicted: each trade is set against the name's 63-day average traded value on the day, and read
as the largest book at which that trade takes no more than the stated share of it.

| Share of a day's traded value | Worst trade | 1st percentile of trades | Median trade |
| --- | ---: | ---: | ---: |
| 1% | $91,546,647 | $146,012,883 | $16,231,104,636 |
| 5% | $457,733,236 | $730,064,416 | $81,155,523,178 |

**The worst trade binds.** At 1% of a day's traded value no trade exceeds its share while the book
is at most $91,546,647; the trade at the first percentile allows $146,012,883, and the median trade
$16,231,104,636. Which trade is the worst was not traced. The first design never modelled capacity.
The run of 2026-09-23 printed $2,018,972, $123,231,452 and $14,574,799,654 at 1%, and $10,094,858,
$616,157,261 and $72,873,998,268 at 5%: each trade is the change from the row before, so those
figures were read from rows out of date order too, and the reproduction's replace them.

<!-- example: end -->

## The trial count

How many variants were ranked to reach the book above, and every run excluded by name with its
reason. `RESULTS.md` compiles this: a reader cannot discount a best-of-N result without knowing N,
and the graduation sign-off says whether the deflated figure was also computed.

<!-- example: begin -->

### The perturbation, criterion 3

Fifteen cells, one setting at a time around the rule, each priced beside its own control: the same
settings without the cross, on the cell's own trade dates. Net, at the headline cost row. **The
rule itself** — 20 names, buffer 30, monthly, 50 and 200, 63 days, one day — reads Sharpe 0.806,
+0.031 over its control and −0.86 points of CAGR, on 311 trade dates; its CAGR margin is printed to
two decimals, the cells' to three.

| Cell | Sharpe | Sharpe over control | CAGR over control, points | Trade dates |
| --- | ---: | ---: | ---: | ---: |
| Book size 10 | 0.868 | −0.096 | −4.864 | 211 |
| Book size 15 | 0.857 | +0.045 | −0.234 | 267 |
| Book size 25 | 0.872 | +0.056 | +0.220 | 362 |
| Book size 30 | 0.862 | +0.042 | +0.240 | 417 |
| Buffer 20, none | 0.830 | +0.065 | −0.417 | 312 |
| Buffer 25 | 0.847 | +0.041 | −1.010 | 309 |
| Buffer 40 | 0.903 | −0.017 | −1.859 | 316 |
| Re-equalise never | 0.867 | −0.142 | −5.001 | 224 |
| Re-equalise quarterly | 0.877 | +0.123 | +1.146 | 244 |
| Averages 40 and 160 | 0.893 | +0.120 | +1.049 | 382 |
| Averages 60 and 250 | 0.867 | +0.092 | +0.660 | 259 |
| Ranking window 21 days | 0.875 | +0.036 | −0.558 | 302 |
| Ranking window 126 days | 0.856 | +0.087 | −0.142 | 318 |
| Acted on 5 days late | 0.819 | +0.043 | −0.543 | 310 |
| Acted on 21 days late | 0.773 | +0.035 | −0.496 | 312 |

**Each curve's direction, as the blueprint asked:**

- **Book size.** The Sharpe margin is negative at ten names and positive from fifteen to thirty.
  The CAGR margin is positive only at twenty-five and thirty.
- **Buffer.** The Sharpe margin shrinks as the buffer widens, from +0.065 with none to −0.017 at
  forty. The CAGR margin is negative at every width.
- **Re-equalisation.** Quarterly is the best cell of the fifteen on both margins, +0.123 and
  +1.146; never is the worst, −0.142 and −5.001; monthly sits between.
- **The averages.** Both neighbours beat the rule's own pair on both margins: 40 and 160 at +0.120
  and +1.049, 60 and 250 at +0.092 and +0.660.
- **The ranking window.** Both neighbours beat 63 days on both margins, and the CAGR margin stays
  negative at 21 and at 126.
- **The delay.** Acting 5 or 21 days late keeps the Sharpe margin positive, +0.043 and +0.035, and
  narrows the CAGR shortfall, −0.543 and −0.496. Acting late does not hurt the cross against its
  control, which is the diagnostic arm's finding seen from another side. Both delay books also
  targeted `TWTR` after its last price, and the engine left that weight in cash: caveat 8.

**Criterion 3 is read as passed, on its own rule**: 12 of 15 cells keep the sign of the rule's
Sharpe margin, and the blueprint asked for twelve. Read with the curves, the pass is of a Sharpe
margin that comes with a CAGR margin below zero in most cells. The rule's own pair of averages,
ranking window and lag each sit at the bottom of their curve on both margins. The best cell is
never the answer: picking one after the result is a new experiment, and one more trial.

### The count

**Thirty-one trials, the count the blueprint fixed.** The first design's thirteen engine runs, ten
reported and three excluded, all at `v0.15.0`. The owner's earlier test outside this repository,
counted as one because its variants were not kept, so the count is a lower bound. This design's
rule, its diagnostic arm and the fifteen cells of the perturbation.

**Forty-five engine runs in this design's notebook**, every one valued on at least 99% of its
window's trading days. The reproduction of 2026-09-24 ran the same forty-five on the same books and
adds no trial. By role:

| Role | Engine runs | Counted as |
| --- | ---: | --- |
| The rule | 1 | a trial |
| The control | 1 | a diagnostic |
| The diagnostic arm | 1 | a trial, never a candidate |
| The rule at realistic costs | 1 | a diagnostic: the same book at another cost row |
| The sub-periods: the rule and its control in each of three | 6 | diagnostics, the kill switch |
| The perturbation: fifteen cells and their fifteen controls | 30 | fifteen trials and fifteen diagnostics |
| Random books, five seeds | 5 | diagnostics |
| **All** | **45** | |

**The Verify section, section 8, raised nothing, in either run.** 14 checks on the book and its
weight file: the nine invariants of section 2.1, and five on the file read back from disk. 92 on
the runs: two window checks on each of the 45 engine runs, 90, and two on the attribution, that its
window lies inside the backtest's and that every arm has an idiosyncratic figure.

**No variant was selected on its result.** The rule, the control, the arm, the sub-periods, the
fifteen cells and the random books were fixed in `BLUEPRINT_1.md` or in the notebook before the
run. The deflated Sharpe was not computed.

**One run is excluded by name, with its reason.** The first attempt, on 2026-09-23, stopped at the
rule's engine run: the engine refused a weight column whose gross exposure was 1.000002, because
rounding a fully invested twenty-name book to six decimals pushed it past one.
`Experiments/backtest_engine.py`'s `write_weight_file` now rounds every weight down, and the
remainder goes to cash. The attempt produced no figure, so no table here holds one of its numbers.
It priced no book, so it is not counted among the thirty-one.

<!-- example: end -->

## Attribution — is this the signal, or a factor exposure wearing its name?

Brinson-Fachler: allocation, selection, interaction. The factor model: factor against idiosyncratic.
State the window, which is bound by the supplied files' coverage and is usually shorter than the
backtest.

**What it settles**, and **what it does not** — naming the counterfactual book that would settle
what is left: the same holdings with the signal off, positions equalised, a random draw at the same
sizes, entry dates shifted.

<!-- example: begin -->

**Window: 2017-01-04 to 2026-06-01**, the backtest's own, which the factor files cover. The book is
read daily as the engine held it, widened to the whole index at zero weight, with the five blocked
names dropped from both. 686 of the 1,399 identifiers the book and the index name have a price
series here, and the library prices only those.

**First cut, Brinson-Fachler**, summed daily over the window, in percentage points: alpha
**+52.14**, of which allocation **+0.11**, selection **+12.26** and interaction **+39.78**: most of
the active return falls into interaction, then selection, and next to none into allocation. This
library's first cut is per asset, not per group, so each line is about the weighting of names, not
of sectors. Read it as "the weighting did it", not as "the sectors did it".

**Second layer, the factor model**, in percentage points of the rule's 160.02 points of excess
return over the window:

| Source | Points |
| --- | ---: |
| Market | 87.39 |
| Momentum | 15.44 |
| Beta | 7.60 |
| Size | 6.86 |
| Residual volatility | 5.82 |
| Value | 0.71 |
| The eleven sector factors | 0.00 each |
| **All factors** | **123.82** |
| **Idiosyncratic** | **36.19** |

**What it settles.** The market is 87.39 of the rule's 160.02 points, at a beta of 1.067: a
full-beta equity book, as the first design was. Momentum is the largest style line, and the book
holds it without trading it.

### The counterfactuals, by arm

The factor model on every arm, each treated as the rule was. The random books are twenty names drawn
from the index's members with a price, equally weighted, on the first trading day of each month in
the window, 114 dates from 2017-01-03, and held between them. They remove the ranking and the cross
and keep the size, but not the rule's calendar: 2017-01-03 is not one of the rule's trade dates, and
each random book's weight file holds only `SHY`, the cash proxy, on it and first holds stocks on
2017-02-01, its second draw. The pool they draw from was empty that day; section 6 prints only its
range, 0 to 569 names per date, and the weight files show which day. That month in cash is in every
random figure below, the baseline's included. Points over the attribution window; *weight unpriced*
sums, over the window's days, the book's weight in names the library has no price series for.

| Arm | What it removes | Excess | Factors | Market | Momentum | Beta | **Idiosyncratic** | Weight unpriced |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| The rule | — | 160.02 | 123.82 | 87.39 | 15.44 | 7.60 | **36.19** | 46.90 |
| The control | the cross | 171.38 | 130.39 | 87.63 | 5.99 | 23.70 | **40.99** | 46.63 |
| The diagnostic arm | the fast exit | 173.30 | 123.28 | 87.23 | 11.99 | 8.31 | **50.02** | 40.68 |
| Random, seed 11 | the ranking and the cross | 95.73 | 71.06 | 84.58 | −2.65 | 3.63 | 24.67 | 39.53 |
| Random, seed 22 | the same | 107.71 | 72.53 | 85.23 | −3.21 | 0.15 | 35.18 | 39.48 |
| Random, seed 33 | the same | 109.91 | 81.50 | 85.61 | 0.70 | 8.89 | 28.41 | 39.35 |
| Random, seed 44 | the same | 115.30 | 79.99 | 86.68 | −4.60 | 11.00 | 35.31 | 39.24 |
| Random, seed 55 | the same | 63.96 | 75.74 | 86.09 | −4.97 | 5.60 | −11.78 | 40.05 |

The random books' idiosyncratic points run from −11.78 to 35.31, mean 22.4. The engine prices
seeds 11, 22, 33, 44 and 55 at CAGR 6.88%, 8.75%, 8.51%, 8.95% and 1.82%, and Sharpe 0.344, 0.461,
0.440, 0.455 and 0.091. The unpriced weight is the notebook's own sum, not the library's: for seeds
11, 22, 33 and 55 the reproduction printed 0.01 more than the run of 2026-09-23, which read 39.52,
39.47, 39.34 and 40.04, and why was not traced. Every other figure in the table came back to the
digit.

**Three readings, each from the table.**

- **The cross costs idiosyncratic return.** Without it the control keeps 40.99 points against the
  rule's 36.19. With the first design's delay the arm keeps 50.02. Neither the cross nor its fast
  exit adds to the residual.
- **The cross trades beta for momentum.** Against its control, the rule's beta line is 7.60 points
  against 23.70 and its momentum line 15.44 against 5.99. Its measured beta is 1.067 against the
  control's 1.238. The blueprint fixed how to read this before the run: a margin that comes with a
  beta well below the control's is timing, not selection. **The rule's Sharpe edge of 0.031 is read
  as timing.**
- **The random books set the baseline.** The rule's 36.19 sits just above their top, 35.31, and
  their mean is 22.4. Five draws are five samples: enough to say the baseline is not zero, not
  enough to place the rule in its distribution. Each starts with a month in cash, which the rule
  does not, and that month was not separated out.

**What it does not settle.** The third pass, Brinson-Fachler on the residual returns, has not been
run, so no group-level selection story exists for this book. The sector lines read zero because the
desk's eleven sector factor files are empty, so a sector tilt is not separated from the rest. Of
the counterfactuals `AGENTS.md` names, the signal off is the control, the random draw is the random
books, and shifted dates are the delay cells of the perturbation. Positions equalised within a date
are the rule itself, which is equal weight by construction and re-equalised monthly.

<!-- example: end -->

## What is open, ranked

The single highest-value run outstanding, and what it would settle.

<!-- example: begin -->

1. **Experiment 2: the arm's design on years before 2017**, which it was not found on, from the
   first date its blueprint's coverage rule allows, no earlier than 2002-07-30, to 2016-12-30, with
   the seed widened to every name the index held since 2000. The owner opened it on 2026-09-24. The
   arm was a diagnostic here, one trial of thirty-one, and it is a candidate only there; it reaches
   paper trading only by passing the gate on its own. It also puts 2008 inside a point-in-time
   window for the first time. Its blueprint comes before its rule. Highest value.
2. **The third pass, Brinson-Fachler on the residual.** Not run for either design, and criterion 2
   of the gate cannot pass without it.
3. **Sector factor files with data.** The desk's eleven are empty, and no sector claim stands until
   they are filled.
4. **Far more random books, and the rule's percentile among them.** Five draws span −11.78 to
   35.31 points, and the rule sits just above their top.
5. **The band read as a curve**, claim 4's full test, which the arm has measured at one setting
   only. A new experiment, its band chosen on turnover and persistence, never on the CAGR it will
   be judged by.

<!-- example: end -->

## Caveats

| # | Caveat | Effect |
| --- | --- | --- |
| 1 | what a reader must know before quoting a number above | what it does to that number |

<!-- example: begin -->

| # | Caveat | Effect |
| --- | --- | --- |
| 1 | **The seed never holds the whole index.** `Universe/Investable_Universe.csv` held 788 identifiers when this design ran, and when it was reproduced. The universe runs of 2026-09-23 and 2026-09-24 each found 39.8% of the index's members in it on 2000-01-03, and no date through 2026-08-14 on which it held 99% of them. No run recorded here measured its share of the index's weight | The rest of the index was never selectable, by the rule or by any arm. Every book here is drawn from the seed's part of the index, not all of it |
| 2 | **The desk's eleven sector factor files are empty** | The sector lines read 0.00, as in the first design, and a sector tilt is not separated from the other lines |
| 3 | **The attribution prices 686 of the 1,399 identifiers the book and the index name**, and leaves some of each book's weight unpriced: 46.90 for the rule and 39.24 to 46.90 across the arms, summed over the window's days | The first design found the engine's cash reserve among the unpriced weight. It applies to every arm alike, so the comparisons are more reliable than the levels |
| 4 | **After 2026-08-14, the desk's last holdings date, membership is held as it was that day** | It matters only for paper trading: the experiment's window ends 2026-06-01 |
| 5 | **The window is the one that falsified the first design** | A rewrite is a second look at the same years by someone who knew the first answer. The margins, the kill switch and the trial count were fixed before the run for that reason, and Experiment 2's years are the ones that answer it |
| 6 | **The run of 2026-09-23 read a panel refreshed through that day**, and a refresh rebases every adjusted column. The reproduction's fresh download stopped at 2026-06-01 | This design and the first sit on two downloads. Compare each with its own control and index row, not with the other design's. This design's two downloads gave the same engine figures, to the digit |
| 7 | **Costs are the blueprint's row**, the commission setting 0.1, charged at $0.10 a share on every forced sale in this run, with 5 basis points of slippage | Every verdict is read there. The realistic row, 0.005, charged $8.71 on 1,741 shares of `TWTR`, and reads 18.36% and 0.8280 against the headline's 17.87% and 0.8057 |
| 8 | **Delisting exits use one day of hindsight** | `TWTR` was sold at its last price on 2022-10-27 in 17 of the 45 runs: the rule, the diagnostic arm, the rule at realistic costs, sub-period 2's rule and 13 of the 15 perturbation cells, all but book size 10 and acting 21 days late. `IPG` was sold on 2025-11-26 in the run of random seed 11. The two delay books also targeted `TWTR` after its last price: a weight of 0.05 on 2022-11-01 acting 5 days late, and 0.047723, 0.047281 and 0.047419 on 2022-11-08, 2022-11-11 and 2022-11-16 acting 21 days late. The engine ignored those weights and left the capital in cash, so both delay cells, which the reading of exit speed leans on, carry a data artefact |
| 9 | **The engine valued two securities at a stale price in every random book**: an 89-day gap in `SRCL`'s adjusted close in four of the five, seeds 11 to 44, and a 12-day gap in `VMW`'s in all five | It touches the random baseline of 22.4, which is built from all five. No other run printed the warning |
| 10 | **Five random draws**, each holding only `SHY`, the cash proxy, until 2017-02-01, as its weight file shows | The baseline of 22.4 idiosyncratic points is indicative, and so is every reading measured against it. The month in cash is in each random book's figures and was not separated out |

<!-- example: end -->
