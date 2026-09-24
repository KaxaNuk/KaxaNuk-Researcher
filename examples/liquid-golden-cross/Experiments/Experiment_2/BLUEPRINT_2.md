# Blueprint — Experiment 2

> **The hypothesis, fixed once written.** Thesis, the claim it moves, rules, predictions, success
> criteria, what would falsify it and key risks, recorded *before* any code runs.
>
> **This file does not change when results arrive.** A hypothesis edited after its test is no longer
> a hypothesis — that is the whole reason it is kept apart from the result. What the experiment
> actually produced is in [`FINDINGS_2.md`](FINDINGS_2.md); planning lives in
> [`BRAINSTORMING_2.md`](BRAINSTORMING_2.md), the running log in [`JOURNAL_2.md`](JOURNAL_2.md).
>
> Record the date it was written, and delete this blockquote.

---

## Experiment 2 — the slow exit, on new years

<!-- example: begin -->

**Written 2026-09-24, before any rule was coded and before any price after the widening was
read, and revised the same day after the blueprint critic, still before either.**
`liquid-golden-cross`.

A confirmation, not a discovery: the design below is Experiment 1's diagnostic arm, found on 2017
to 2026, where it was one of thirty-one trials, in forty-five engine runs. This experiment runs its
rules unchanged, on a wider seed, with the dead names filled at the close.

**These years are not unseen.** The first design, the arm's timing at thirty names, was priced from
2002-07-30 on a fixed membership: 10.29% a year, a −60.7% drawdown, a negative alpha, and 27–40% in
cash through December 2008 and January 2009 (`RESULTS.md`; `FINDINGS_1.md` at tag `v0.15.0`). The
analyzer's rows 1 to 18 were measured on 2001 to 2026, these years included. What they have not
seen is this design at twenty names, point in time, against its own control.

<!-- example: end -->

### Thesis

One paragraph: what book this rule produces, why it should beat the benchmark
`BRAINSTORMING_1.md` names, and why it is also a fair yardstick — sensible, liquid, low-complexity
— for judging whether any later idea adds value. **Be modest on purpose.** A first rule does not
assert its signal is the best of its kind, only that it is simple enough to be understood, liquid
enough to be traded, and stable enough to measure other things against.

<!-- example: begin -->

Own the twenty most traded members of the KN US Equity 600 whose fifty-day average is above their
two-hundred-day average, equally weighted, and re-equalise the whole book only on a day on which
the target set differs from the day before by 15% of its names or more — three of a full twenty —
so a name whose cross breaks is held until a day on which the set moves that much at once. On 2017
to 2026 that slow exit earned more than selling on the break (19.52% a year against 17.87%, Sharpe
0.877 against 0.806; `../Experiment_1/FINDINGS_1.md`). **Nothing measured here explains it, and
nothing licenses an edge over the control.** The reversal in the most recent month is momentum's,
and the note on it says momentum's evidence cannot be borrowed for a trend rule
([Paleologo (2021), ch. 5](../../Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/09_Understand_Factors.md));
the analyzer finds a broken name drifting below the pool at 5, 21 and 63 days, not reverting
(`RESULTS.md`, rows 16 to 18). What it does license is a difference in volatility, 28.7% above the
cross against 36.7% below it (rows 8 and 9), which can lift a Sharpe and not a return.
**Against it:** the arm has never been priced against its own control, on any window. The two
controls on record traded on other dates, and both beat their rules: the same timing at thirty
names by 1.12 points a year, the fast exit at twenty by 0.86. A band is a delay, and a delay loses
a signal's value at the rate of its half-life, which nobody has measured here
([Grinold & Kahn, ch. 13](../../Bibliotheca/Books/Grinold_Kahn_ND_Active_Portfolio_Management/16_The_Information_Horizon.md)).
And the papers read for claim 1 find moving-average rules failing after the 1980s
([Sullivan, Timmermann & White (1999)](../../Bibliotheca/Papers/Sullivan_Timmermann_White_1999_Data_Snooping.md),
[LeBaron (1999)](../../Bibliotheca/Papers/LeBaron_1999_The_Stability_Of_Moving_Average_Rules.md)).
It asserts nothing about being the best trend rule; it asks whether the cross earns anything at
twenty names, on years it was not chosen on, against a control that differs in the cross alone.

<!-- example: end -->

### The claim this moves

Which claim of `OBJECTIVE.md`, by number, this experiment exists to move, the status it reaches if
the predictions below hold, and the one it reaches if they fail. **One claim.** An experiment that
could beat every benchmark and settle nothing is a measurement, not a test.

<!-- example: begin -->

**Claim 1, the signal**, falsified twice on 2017 to 2026. If prediction 1 holds **and** the kill
switch is silent, it moves to **confirmed as a book, for this design, on the test window
`JOURNAL_2.md` records**, quoted beside the same design's margin over its own control on 2017 to
2026, whatever its sign, and the two earlier falsifications. If either fails, it stays
**falsified**, now on two windows. No third status is available.

<!-- example: end -->

### Rules

- **Selection:** the eligibility condition, naming the column it reads.
- **Sizing:** the weighting scheme. Say which constraints are switched off, and that each one is a
  lever a later experiment has to earn.
- **Cash:** where the uninvested residual goes — a real, priced instrument, because the engine's
  weight file has no cash row.
- **Timing:** calendar, or event-driven on a stated trigger. Say what happens between triggers.
- **Lag:** how many days between the signal and the fill, and what the engine adds on top.
- **Control:** the same rule with exactly one ingredient removed — name which — trading on this
  rule's own rebalance dates, so that the ingredient is the only difference. A control left to find
  its own dates differs in when it trades as well.
- **Screens deliberately absent**, and why each is redundant under the rules above.

<!-- example: begin -->

- **Universe:** the KN US Equity 600's members as of each date, from the desk's daily holdings read
  by `Data/hand_supplied.py`, with the seed widened to every listing the index held since 2000.
- **Signal:** the cross as a state, `r_trend_50_200` above zero, from the refinery.
- **Selection:** of the members with the cross at 1, a price and a fill price, all at the prior
  close, the twenty with the highest `r_liquidity_rank`. Excluded by name are exactly the names
  that fail Experiment 1's two tests — no price file, or an adjusted price that multiplies by more
  than six in a day — and those the universe notebook finds carrying two companies under one
  identifier, listed in `JOURNAL_2.md` before the rule runs. No name is excluded for a fall of any
  size: a fall is a return.
- **Timing:** `portfolio_construction.select_rebalance_dates` at a band of 15%, as Experiment 1's
  arm ran it: each day's lagged target set is compared with the day before, and the whole book is
  re-equalised, one twentieth each, when the names that entered or left are 15% or more of that
  day's set: three names, so two swaps, when the set is full; one swap can be enough when fewer
  than twenty names qualify. Between rebalances nothing trades and the weights drift.
- **Sizing and cash:** equal weight at one twentieth; any slot no name fills is held in `SHY`.
- **Lag:** one day, `portfolio_construction.lag_eligibility`, on the selected set and its ranking
  together, as the arm ran it. The engine fills at the day's VWAP, and at the day's close for the
  names fetched from Sharadar, which publishes no VWAP.
- **The fill convention, checked:** the rule and its control are priced again on the test window
  with every name filled at the day's close. If prediction 1's verdict differs between the two
  conventions, the experiment does not pass: its result would depend on how the dead names are
  filled.
- **Costs:** the engine's commission setting 0.1, which it charges as about eight cents a share,
  5 basis points of slippage and a 2% cash reserve, on $1,000,000, as Experiment 1's arm ran: the
  cost row every verdict is read at. The setting 0.005 is reported beside it.
- **Control:** the same twenty most traded members without the cross, re-equalised on the rule's
  own rebalance dates, so the cross is the one difference.
- **Window — the test:** 2002-07-30, when the cash proxy starts, to 2016-12-30. Coverage on a date
  is the share of the index's weight, from the desk's holdings, in members with a price and a fill
  price that day, excluded names counted as unpriced. It is measured on every date before any book
  is built, and recorded in `JOURNAL_2.md`. The test starts on the first date on or after
  2002-07-30 with coverage of 95% or more — above the 92% Experiment 1's window opened on — and a
  later date below it is listed in `FINDINGS_2.md`, never acted on. If that first date is after
  2005-01-03, nothing is priced: the experiment is recorded as not testable on these data, and a
  shorter window is a new blueprint. Sub-period 1 runs from the start the journal records.
- **Window — the one it was found on:** 2017-01-03 to 2026-06-01, the same rule and control on the
  same widened panel and download as the test, reported beside it as description and never as
  evidence for it. It will not reproduce the arm's 19.52% in `FINDINGS_1.md`, and both figures are
  shown. Its margin over its own control is the first ever measured, on the window the design was
  chosen on, and is quoted with claim 1's status whatever its sign.
- **Screens deliberately absent:** as in Experiment 1.

**The perturbation, fixed now, each cell beside its own control on the test window**, the control
taking the cell's book size and delay and trading on the cell's own rebalance dates: the band at
10%, 30% and 40%, one, three and four swaps of a full book of twenty — 20% is not a cell, because
on a full book it trades on the same days as 15%; the book size at 10, 15, 25 and 30, the band at
three names of each, 30%, 20%, 12% and 10%, so that two swaps of a full book still trade; the
averages at 40 and 160, and at 60 and 250; the rule acted on 5 trading days late. Ten cells.
**Criterion 3 of the gate in `Paper_Trading/BITACORA.md` is read as passed** if the rule's Sharpe
and its CAGR are both above its control's in at least eight of the ten; a cell in which the rule
trails its control on either counts against it, whatever the test's own sign.

**The trial count:** the thirty-one `BLUEPRINT_1.md` fixed, which already hold the owner's earlier
test and the arm, then this experiment's rule, counted again because it meets new years, and its
ten cells. Every control, sub-period, fill-convention and description run is listed by name in
`FINDINGS_2.md` as a diagnostic, and Experiment 1's forty-five engine runs are quoted beside the
count, never as it.

<!-- example: end -->

### What this experiment should show

**Predictions, fixed before the run.** Each cites a `Bibliotheca/` note or a section of
`Data/analyzer.ipynb`, which measures the signal but builds no book. Getting these right is worth
more than a good Sharpe; getting them wrong is worth more than a bad one.

| # | Prediction | Where it comes from | What would falsify it |
| --- | --- | --- | --- |
| 1 | what the book should do | a `Bibliotheca/` note, or the analyzer section and its number | the observation that would refute it |

Note anything you are watching but cannot predict, because nothing licenses a prediction about it.
Costs usually belong here.

<!-- example: begin -->

**Predictions, fixed before the run.**

| # | Prediction | Where it comes from | What would falsify it |
| --- | --- | --- | --- |
| 1 | On the test window the rule beats its control by **at least 0.03 of Sharpe and 0.5 points a year of CAGR**, net, at the headline cost row, each margin read unrounded from the engine's figures. The margins are `BLUEPRINT_1.md`'s, carried unchanged so both experiments are judged by one bar; a Sharpe gap of 0.03 alone is within the noise `OBJECTIVE.md` names under claim 2, so the CAGR margin decides | **A lead, not a licensed prediction: the hypothesis under test.** No note and no analyzer section licenses a return edge for the cross over its control. Against it: both designs of Experiment 1 lost to their controls, by 1.12 and 0.86 points a year, and the cross as a state carries an information coefficient of 0.0066 at 21 days, positive on 51.8% of dates (`RESULTS.md`, row 13) | either margin not reached |
| 2 | The rule beats the KN US Equity 600 on Sharpe over the test window | **A lead: the arm's result on the window it was found on, carried to new years** — 0.877 against the index's 0.770 on 2017 to 2026 (`FINDINGS_1.md`); no note or analyzer section licenses it. Against it: the first design's long window from 2002-07-30, on a fixed membership, had a negative alpha (`FINDINGS_1.md` at `v0.15.0`), and the index's return includes members the book cannot hold | the index's Sharpe at or above the rule's |
| 3 | Over 2007-01-03 to 2009-12-31, the deepest fall of the test run's daily value, peak and trough both inside those dates, is shallower than the index's measured the same way | analyzer section 5: forward volatility of 28.7% above the cross against 36.7% below it, which `RESULTS.md` reads as licensing a shallower drawdown than the index (rows 8 and 9). Against it: the first design's long window "does not survive a 2008 as a drawdown shield" (`FINDINGS_1.md` at `v0.15.0`), and fast crashes are closed in `RESULTS.md` | a fall as deep as the index's, or deeper |

**Watched, but not predicted:** the betas of the rule and the control side by side — a margin that
comes with a much lower beta is timing, not selection; the number of rebalances and the turnover;
the weight in `SHY` through 2008 and 2009, which the first design held at 27–40% in December 2008
and January 2009 and so is no prediction here; the share of each book's weight in Sharadar names.

<!-- example: end -->

### Success criteria

What the experiment has to show to count as a success, fixed now. At the least:

1. It beats the benchmark `BRAINSTORMING_1.md` names **and its own control** on risk-adjusted
   return, net, over the same window — criterion 1 of the gate in `Paper_Trading/BITACORA.md`.
2. Reproducible from a clean clone, through the pipeline, with no manual step.
3. A tradeable trigger frequency — not a rule that fires every day.
4. Every prediction above evaluated explicitly in `FINDINGS_2.md`, **including the ones that turn
   out wrong.**

**Success is necessary for graduation, not sufficient.** The gate's five criteria in
`Paper_Trading/BITACORA.md` decide it, and a person signs it.

<!-- example: begin -->

Here, in full: prediction 1's margins on the test window, the kill switch below silent, the same
verdict under both fill conventions, the rule beating the index on Sharpe, a run reproduced from a
wiped working copy with the Curator branch at its recorded commit, the rule trading on fewer days
than it does not, and every prediction evaluated in `FINDINGS_2.md`. Then the gate decides
graduation, row by row, and the owner signs or does not.

<!-- example: end -->

### What would falsify it

**One condition for the whole experiment, fixed now.** Each prediction above has its own falsifier;
this is the result under which the experiment as a whole has failed — usually a margin against its
control, or a result that holds in one sub-period and not in the others. Then **the
changes that may not rescue it**: every setting that could be moved once the result is in — a
holding count, a trigger, a window, a threshold — by name. Moving one after the result is a new
experiment, and one more trial in the count.

<!-- example: begin -->

**The kill switch: no edge after costs in two of three sub-periods.** The experiment fails if the
rule does not beat its control by prediction 1's margins over the test window, **or** if fewer
than two of the three sub-periods have the rule's Sharpe and its CAGR both above its control's in
that same sub-period, at the headline cost row — from the start `JOURNAL_2.md` records to
2006-12-29, 2007-01-03 to 2011-12-30, and 2012-01-03 to 2016-12-30 — each priced by the engine as
a window of its own, the rule entering on its first day and its control held to that rule's
rebalance dates.

**The changes that may not rescue it:** the twenty names, the 15% band, the 50 and 200-day pair,
the 63-day ranking window, the one-day lag, the test window, its coverage rule and its 95%, the
sub-periods, the exclusions and their tests, which provider serves each name and how its fill is
made, the two Curator versions, the costs and the 2% cash reserve, and the perturbation's cells
and its threshold.

<!-- example: end -->

### Key risks

- **Survivorship and point-in-time integrity.** The universe must include delisted names; step 2
  quantifies how many.
- **The signal's known weakness** — slow exits, whipsaw, regime dependence — named here, and either
  handled by the rules above or accepted on simplicity grounds and left to a later experiment.
- **Concentration.** How the weighting concentrates, and which diagnostics measure it.
- **The signal may not be what earns the return.** If the book beats its benchmarks because of a
  factor exposure rather than the signal, the honest product is a cheaper factor fund. That is what
  step 6 exists to answer.

<!-- example: begin -->

- **The dead names are filled differently.** Sharadar has no VWAP, so for those names the fill is
  the close, which is also the mark, and the traded value that ranks them is the close times the
  volume. `FINDINGS_2.md` reports, for the rule and the control alike, the share of weight in
  Sharadar names, and every name held on its last priced day with its weight: the engine's exit at
  the last price spares whichever book holds a failing name to the end.
- **Coverage.** Even widened, the priced names may not hold the whole index in the early years;
  coverage on each date is reported. The unpriced weight is in names neither provider carries: the
  index's return, the desk's own, includes them and the book cannot hold them, so the gap bears on
  the comparison with the index more than on the one with the control.
- **Two Curator versions.** The dead names come from the Data Curator's issues/31 branch, 0.49.1
  with the Sharadar provider, at the commit `JOURNAL_2.md` records; every other name from 0.50.0.
  Before the rule runs, the first twenty names of the seed, in its order, that both providers carry
  are fetched from both, and the daily returns of their mark and fill are compared; the differences
  are recorded in `JOURNAL_2.md`.
- **A second look at these years.** Predictions 2 and 3 were written knowing the first design's
  long window, which is survivorship-affected, and the analyzer's measurements over 2001 to 2026;
  the figures that argue against each are named beside it.
- **The test is still one period.** Fifteen years is more than nine, and less than the
  sample-length evidence asks for a skill claim; a pass is a confirmation on years it was not
  chosen on, not a proof.

<!-- example: end -->

### Open questions this experiment deliberately does not answer

Each is a later experiment, and each has to beat this one.

| # | Question | Why it is not answered here |
| --- | --- | --- |
| 1 | the question | why this experiment leaves it open |

<!-- example: begin -->

| # | Question | Why it is not answered here |
| --- | --- | --- |
| 1 | Does the rule hold after 2026-06-01? | that is what paper trading is for, if it passes |
| 2 | Does a margin on the cross cut the whipsaw? | a new moving part |
| 3 | What does survivorship cost here? | the same rule on FMP's survivors alone, against this run, would price it |

<!-- example: end -->

<!-- example: begin -->

| # | Question | Why it is not answered here |
| --- | --- | --- |
| 1 | Does the rule hold after 2026-06-01? | that is what paper trading is for, if it passes |
| 2 | Does a margin on the cross cut the whipsaw? | a new moving part |
| 3 | What does survivorship cost here? | the same rule on FMP's survivors alone, against this run, would price it |
| 4 | What is the cross's half-life, and so what does the band cost? | a measurement of the signal, for the analyzer, not a book |
| 5 | Does ranking the liquid names on their twelve-month return instead of the cross earn more? | a different signal, momentum proper, and a new experiment with its own control |

<!-- example: end -->
