# Blueprint — Experiment 1

> **The hypothesis, fixed once written.** Thesis, the claim it moves, rules, predictions, success
> criteria, what would falsify it and key risks, recorded *before* any code runs.
>
> **This file does not change when results arrive.** A hypothesis edited after its test is no longer
> a hypothesis — that is the whole reason it is kept apart from the result. What the experiment
> actually produced is in [`FINDINGS_1.md`](FINDINGS_1.md); planning lives in
> [`BRAINSTORMING_1.md`](BRAINSTORMING_1.md), the running log in [`JOURNAL_1.md`](JOURNAL_1.md).
>
> Record the date it was written, and delete this blockquote.

---

## Experiment 1 — the first rule against the benchmark

<!-- example: begin -->

**Written 2026-09-23, before any rule was coded, and revised the same day after a cold review, still
before any rule was coded.** `liquid-golden-cross`.

**This blueprint replaces the one written on 2026-09-19** — thirty names, re-equalised whenever the
set moved by a tenth — which is kept at tag `v0.15.0` of the KaxaNuk Researcher and as a row of
`RESULTS.md`, and whose findings falsified claim 1. The owner decided the rewrite on 2026-09-23, as
`JOURNAL_1.md` records: this is Experiment 1's second design, on **the same window that falsified
the first**, and every run of the first counts in the trials below.

<!-- example: end -->

### Thesis

One paragraph: what book this rule produces, why it should beat the benchmark
`BRAINSTORMING_1.md` names, and why it is also a fair yardstick — sensible, liquid, low-complexity
— for judging whether any later idea adds value. **Be modest on purpose.** A first rule does not
assert its signal is the best of its kind, only that it is simple enough to be understood, liquid
enough to be traded, and stable enough to measure other things against.

<!-- example: begin -->

Own the twenty most traded US stocks in the KN US Equity 600 whose fifty-day average price is above
their two-hundred-day average, equally weighted, and **sell a name the day after its cross breaks**
instead of waiting for the rest of the book to move. The first design held a broken name for a
median of 19 trading days, and 9.6% of its name-days were in a stock already below its cross
(`BRAINSTORMING_1.md`, 2026-09-23).

**The economic reason offered is under-reaction.** Holders who trade on a calendar or a band — as
the first design did — sell a broken trend late, so its price keeps adjusting after the break; the
analyzer finds the drift that reason predicts, a broken name trailing the rest of the pool by a
median 0.31% over the next month and 1.04% over the next three (`RESULTS.md`, *Before any
experiment*). **Against it**: the same chapter that defines trend following finds a reversal in the
most recent month, so a name sold on a break may be sold at its low
([Paleologo (2021), ch. 5](../../Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/09_Understand_Factors.md));
and the two papers read for claim 1 find moving-average rules failing after the 1980s
([Sullivan, Timmermann & White (1999)](../../Bibliotheca/Papers/Sullivan_Timmermann_White_1999_Data_Snooping.md),
[LeBaron (1999)](../../Bibliotheca/Papers/LeBaron_1999_The_Stability_Of_Moving_Average_Rules.md)).

The rule is the owner's, tested before outside this repository, and simple on purpose: four moving
parts, no optimiser, every position among the most traded stocks in the United States. It should
beat the index because it holds the names the market trades most while their trend holds; it
should beat the same names without the cross only if selling fast is where the cross earns, which
is the question. **It asserts nothing about being the best trend rule**: as a 0/1 state the cross
ranks names at an information coefficient of 0.0066 over a month, positive on 51.8% of dates, and
the thesis is written knowing that.

<!-- example: end -->

### The claim this moves

Which claim of `OBJECTIVE.md`, by number, this experiment exists to move, the status it reaches if
the predictions below hold, and the one it reaches if they fail. **One claim.** An experiment that
could beat every benchmark and settle nothing is a measurement, not a test.

<!-- example: begin -->

**Claim 1, the signal**, falsified under the first design. What each outcome does to it, fixed now:

| Prediction 1, the control | The kill switch | Prediction 2, the arm | Claim 1 becomes |
| --- | --- | --- | --- |
| holds | silent | holds | **confirmed as a book, second design, on the window that falsified the first**: the status says both |
| holds | silent | fails | the same, with the mechanism unexplained: the cross earned, but not through exit speed |
| fails, or | trips | either | **falsified**, with the band's delay ruled out as the reason when the arm reproduces it |

Prediction 2 also speaks to **claim 4, the rebalancing**: the arm's result moves claim 4 from
*untested* to *measured* and no further. Its full test, the band as a curve, stays a new experiment,
as `OBJECTIVE.md` says.

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
  by `Data/hand_supplied.py`. The seed covers the index from 2017, which is where the window starts.
- **Signal:** the cross as a state — 1 when the 50-day simple moving average of the dividend and
  split adjusted close is above the 200-day, 0 when it is not; `r_trend_50_200` above zero.
- **Eligible:** a member with the cross at 1, a price and a fill price, **all at the prior close**.
- **Entry:** the eligible names not held, best first by `r_liquidity_rank`, the per-date percentile
  of 63-day average traded value, fill any open slot of twenty on the first day one is available.
- **Exit:** a holding is sold on the next trading day when, at the prior close, its cross is at 0,
  it has left the index, or it had no fill price. **No band delays an exit.** A security whose
  prices stop is sold by the engine at its last price instead: the one look-ahead `AGENTS.md`
  admits.
- **Replacement:** an entrant takes one twentieth, or the cash in hand split among the day's
  entrants when that is less; what is left waits in cash until the month's re-equalisation.
- **Drift:** a holding not traded keeps its weight drifted to the prior close; the engine trades
  every name to its target at the day's VWAP, so an untouched name may trade a few shares.
- **Ranking buffer and re-equalisation:** on the first trading day of each month, a holding still
  eligible but no longer among the top thirty eligible names by the ranking is sold and replaced,
  and every holding is set back to one twentieth. Between those days, ranking churn does not trade.
- **Excluded by name:** `MIC`, `CIT`, `FMC`, `LCI` and `PARA`, the blocking rows of
  `Universe/Data_Issues.csv`, as in the first design.
- **Sizing:** equal weight at one twentieth. No maximum weight beyond it, no risk model, no sector
  limit: **each is a lever a later experiment has to earn.**
- **Cash:** `SHY`, a short-Treasury fund, for any slot no stock fills.
- **Costs:** the first design's — the engine's commission setting of 0.1, which it charges as about
  eight cents a share, and 5 basis points of slippage — are **the cost row every verdict is read
  at**; a row at the realistic setting of 0.005 is reported beside it. Results are read net.
- **Window:** 2017-01-03 to 2026-06-01, the first design's, so the two compare.
- **Control:** the same rule without the cross. It **trades only on the rule's own trade dates**:
  on each of them it sells what has left the index or lost its fill price, fills its open slots
  from the top of the ranking, and on a first day of the month applies the buffer and
  re-equalises; on a date the rule sells a name for its cross, the control trades only if it has a
  sale of its own. The cross is the one difference.
- **Diagnostic arm:** twenty names with the first design's code, `select_rebalance_dates`, at a band
  of **15%**: at twenty names one swapped name is a tenth and two are a fifth, so 15% keeps the
  first design's behaviour — one swap waits, two trade. **It must reproduce the delay** measured in
  `BRAINSTORMING_1.md` — broken names held for days, not the rule's one — or its verdict on exit
  speed is void. A trial in the count, not a candidate.
- **Screens deliberately absent:** no market-cap screen, because ranking on traded value already
  selects large companies; no sector cap, because the concentration is measured in step 6; no
  volatility screen, because the cross is already one.

**Where the settings come from, said plainly.** Twenty is **the owner's number**, chosen outside
this repository on a measure not recorded: a tuned setting, which is why its curve is read below.
Thirty for the buffer is half as many again as the book, a convention, not a measurement. Monthly
re-equalisation keeps the first design's cadence — about nine rebalances a year — so the two differ
in the exit rule rather than in how often they re-equalise. None was chosen on the metric it is
judged by.

**The perturbation criterion 3 needs, fixed now.** One setting at a time around the rule, **each
cell priced beside its own control**, the same settings without the cross:

- the book size at 10, 15, 25 and 30, the buffer scaled to half as many again: 15, 23, 38 and 45;
- the buffer at 20 (none), 25 and 40;
- the re-equalisation never, and quarterly;
- the averages at 40 and 160, and at 60 and 250 days;
- the ranking's traded-value window at 21 and at 126 days, in place of 63;
- the whole rule acted on 5 and 21 trading days late, in place of one — the delay test
  `OBJECTIVE.md` names for claim 4.

Fifteen cells. **Criterion 3 is read as passed** if the rule's Sharpe margin over its control keeps
the rule's own sign in at least twelve of the fifteen, and each curve's direction is written down;
the best cell is never the answer.

**The trial count, fixed now:** the first design's thirteen engine runs, all counted; the owner's
earlier test, counted as one because its variants were not kept, so the count is a lower bound; and
this design's rule, its diagnostic arm and fifteen cells. **Thirty-one**, published in
`FINDINGS_1.md` beside the result, with every control, sub-period and random book listed by name as
diagnostics.

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
| 1 | The rule beats its control — the same twenty names, no cross — by **at least 0.03 of Sharpe and 0.5 points a year of CAGR**, net, at the headline cost row, over the window | analyzer section 5, the cross breaks (`RESULTS.md`, *Before any experiment*): a broken name trails the pool by a median 0.31% over 21 days and 1.04% over 63, below it on 51.9% and 53.4% of 616 breaks; the first design held a broken name a median of 19 days | either margin not reached |
| 2 | The diagnostic arm, with the first design's delay, earns **less than the rule**, net, at the headline cost row | the same two measurements: the band is a delay, and the delay falls on the names that break | the arm's CAGR at or above the rule's, with its delay reproduced |
| 3 | The rule's margin over its control is **largest in the sub-period 2020–2022**, which holds the window's two sharpest declines | the rule's mechanism: breaks cluster in declines, and analyzer section 5 finds forward volatility higher below the cross than above it | the largest margin falling in another sub-period |

**Watched, but not predicted.** These follow from the first design's result and are not a test of
the second: the rule against the index (the first design had a Sharpe of 0.861 against 0.774), its
beta (1.028) and its momentum loading. The number of trade dates and the turnover, which nothing
measured licenses a count for. Round trips — a name sold and bought back within five days, which is
the cross flickering around zero. **The beta of the rule and of its control**, side by side: a
filter-on book can beat a filter-off one through a beta that fell after declines, and a margin that
comes with a beta well below the control's is read as timing, not selection. All of it is reported
in `FINDINGS_1.md` whatever it is, with the cost drag.

<!-- example: end -->

### Success criteria

What the experiment has to show to count as a success, fixed now. At the least:

1. It beats the benchmark `BRAINSTORMING_1.md` names **and its own control** on risk-adjusted
   return, net, over the same window — criterion 1 of the gate in `Paper_Trading/BITACORA.md`.
2. Reproducible from a clean clone, through the pipeline, with no manual step.
3. A tradeable trigger frequency — not a rule that fires every day.
4. Every prediction above evaluated explicitly in `FINDINGS_1.md`, **including the ones that turn
   out wrong.**

**Success is necessary for graduation, not sufficient.** The gate's five criteria in
`Paper_Trading/BITACORA.md` decide it, and a person signs it.

<!-- example: begin -->

Here, in full: the rule beats the KN US Equity 600 on Sharpe, and beats its control by the margins
of prediction 1, net, at the headline cost row, over the window; the kill switch below is silent;
it reproduces from a wiped working copy; it trades on fewer days than it does not; and every
prediction above is evaluated in `FINDINGS_1.md`. Then the gate decides graduation, row by row, and
the owner signs or does not.

**The months after the window are held out.** The analyzer and every measurement above read a
panel that ended on 2026-06-01; nothing later has been looked at. The months from 2026-06-02 to the
day the book is frozen are the first data this rule meets unseen: they cannot pass or fail the gate
— months cannot show skill — but they are reported beside the verdict as the first check of the
book's behaviour against its bands, and of the freeze itself.

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
rule does not beat its control by the margins of prediction 1 over the whole window, **or** if its
Sharpe **and** its CAGR are not both above its control's, at the headline cost row, in at least two
of three sub-periods — 2017-01-03 to 2019-12-31, 2020-01-02 to 2022-12-30 and 2023-01-03 to
2026-06-01 — each priced by the engine as a window of its own, the rule entering on its first day
and its control held to that rule's trade dates.

**The changes that may not rescue it:** the book size of twenty, the buffer of thirty, the monthly
re-equalisation, the 50 and 200-day pair, the 63-day ranking window, the one-day lag, the window,
the five exclusions and the costs. The fifteen cells above read them as curves; picking one of those
cells after the result is a new experiment, and one more trial in the count.

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

Specifically, here:

- **Survivorship.** The seed keeps its delisted names, and the engine sells a delisted position at
  its last price. The window starts where the seed covers the index; before 2017 the seed would hold
  only names that later joined, which is survivorship in reverse.
- **Whipsaw.** A fast exit on a slow signal still trades the flicker: a name whose averages sit
  close together can cross and recross within a week. Round trips are counted, and their cost is in
  the net result.
- **The reversal.** A name that breaks has often just fallen, and the most recent month reverts
  ([Paleologo (2021), ch. 5](../../Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/09_Understand_Factors.md)):
  selling fast may sell the low. The delay cells of the perturbation are where it would show.
- **The literature argues against the family.** Moving-average rules failed after the 1980s in both
  papers read for claim 1 ([Sullivan, Timmermann & White (1999)](../../Bibliotheca/Papers/Sullivan_Timmermann_White_1999_Data_Snooping.md),
  [LeBaron (1999)](../../Bibliotheca/Papers/LeBaron_1999_The_Stability_Of_Moving_Average_Rules.md)),
  though on one index against cash rather than on a cross-section.
- **Timing, not selection.** A filter-on book can beat a filter-off one through a beta that fell
  after declines; the betas are read side by side.
- **Concentration.** Twenty names are a more concentrated book than thirty, and they lean towards
  technology; the effective number of names and the sector shares are reported, not constrained.
- **A rewrite is a second look at the same window.** The first design's result is known to whoever
  wrote this one. That is why the control, the margins, the kill switch and the trial count are
  fixed here, and why the held-out months are the first data this rule meets unseen.

<!-- example: end -->

### Open questions this experiment deliberately does not answer

Each is a later experiment, and each has to beat this one.

| # | Question | Why it is not answered here |
| --- | --- | --- |
| 1 | the question | why this experiment leaves it open |

<!-- example: begin -->

| # | Question | Why it is not answered here |
| --- | --- | --- |
| 1 | Does the **sign of a 150-day return** do the same work as the crossover? | [LeBaron (1999)](../../Bibliotheca/Papers/LeBaron_1999_The_Stability_Of_Moving_Average_Rules.md) gets the same means and variances from it, which would make the 50/200 form a convention rather than a mechanism |
| 2 | Does a **margin on the cross** — exit below −1%, enter above +1% — cut the whipsaw without the band's delay? | it is a fourth moving part, and it has to beat this book without it |
| 3 | Does **skipping the most recent month** improve the signal? | [Paleologo (2021), ch. 5](../../Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/09_Understand_Factors.md) puts a reversal in the zero-to-one-month window, which the 50-day average includes |
| 4 | What would **twenty-four years** say? | the desk's holdings reach back to 2000; widening the seed to every name the index held since then would start a point-in-time window in 2002, and the sample-length evidence says years matter more than any setting here |
| 5 | How much is **survivorship worth**, in this book? | the same rule on the survivors only, against this run, would price the bias rather than suffer it |

<!-- example: end -->
