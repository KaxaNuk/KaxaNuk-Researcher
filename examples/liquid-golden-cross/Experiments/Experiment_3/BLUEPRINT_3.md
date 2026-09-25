# Blueprint — Experiment 3

> **The hypothesis, fixed once written.** Thesis, the claim it moves, rules, predictions, success
> criteria, what would falsify it and key risks, recorded *before* any code runs.
>
> **This file does not change when results arrive.** A hypothesis edited after its test is no longer
> a hypothesis — that is the whole reason it is kept apart from the result. What the experiment
> actually produced is in [`FINDINGS_3.md`](FINDINGS_3.md); planning lives in
> [`BRAINSTORMING_3.md`](BRAINSTORMING_3.md), the running log in [`JOURNAL_3.md`](JOURNAL_3.md).
>
> Record the date it was written, and delete this blockquote.

---

## Experiment 3 — momentum proper, among liquid names

<!-- example: begin -->

**Written 2026-09-24, before any rule was coded.** `liquid-golden-cross`.

A new signal on the same names. After Experiment 1's two designs and Experiment 2 had failed their
kill switches, and claim 1 stood falsified on two windows, the owner chose momentum proper, in his
words "the 20 most-traded members ranked by their own 12-month return". This blueprint reads it,
as `BRAINSTORMING_3.md` records, as the twenty of the hundred most traded members that rose most
over the twelve months before the latest one: the skipped month and the hundred are the reading's,
not his. It moves claim 5 of `OBJECTIVE.md`, added the same day for it; the cross is in neither
the rule nor its control.

**Neither these years nor this signal on them is unseen.** The analyzer measured `r_momentum_12_1`
on both halves of the test window before this blueprint was written, after the owner had chosen it
(`RESULTS.md`, rows 19 to 30). The same liquid names without a signal have been priced on both:
the twenty most traded members earned 18.73% a year on 2017 to 2026 as Experiment 1's control, on
the 788-name seed at a 2% reserve, and 5.87% on 2002-07-30 to 2016-12-30 as Experiment 2's, each
on its own rule's dates and neither on this rule's (`RESULTS.md`). And step 6 had charged
Experiment 1's books with momentum on 2017 to 2026 before the choice: 12.75 points in the first
design, 15.44 in the second's rule against its control's 5.99. What this experiment tests is a
book, on years whose signal has been read; the signal's out-of-sample evidence is the published
record, not this run.

<!-- example: end -->

### Thesis

One paragraph: what book this rule produces, why it should beat the benchmark
`BRAINSTORMING_1.md` names, and why it is also a fair yardstick — sensible, liquid, low-complexity
— for judging whether any later idea adds value. **Be modest on purpose.** A first rule does not
assert its signal is the best of its kind, only that it is simple enough to be understood, liquid
enough to be traded, and stable enough to measure other things against.

<!-- example: begin -->

Own the twenty members of the KN US Equity 600 with the highest return over the twelve months
before the latest one, chosen from the hundred most traded, equally weighted, and re-strike the
whole book on the first trading day of each month. **The reason is slow reaction, not a premium
for risk:** the review this rests on finds risk-based explanations failing and leans to investors
underreacting to news, so that prices drift toward it
([Baltussen, Dom, Van Vliet & Vidojevic (2025)](../../Bibliotheca/Papers/Baltussen_Dom_VanVliet_Vidojevic_2025_Momentum_Factor_Investing.md),
pp. 27–28). The Paleologo chapter cited below is less sure: its author writes that momentum's
origins are not understood (p. 75), and reports two studies in which lower tail dependence, a crash
risk, makes momentum redundant (pp. 76–77), a claim its note keeps beneath a callout citing the
review's disagreement; the reason is chosen here, not settled. The review finds the standard
definition, the twelve months less the latest one held for a month (p. 5), paying after its
publication — 7.89 percent a year value-weighted in the United States over 1990–2024, t 2.07
(p. 8) — positive in all 31 countries with data since 1990 (p. 10), and paying in 61 years before
CRSP that nobody had tuned it to (pp. 10–11). The latest month is left out because over a month
returns reverse, and from a month to a year they continue
([Paleologo (2021), ch. 5](../../Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/09_Understand_Factors.md),
pp. 74–75). The analyzer finds it at a month in a pool of the hundred most traded: 0.0134 on 2002
to 2016 and 0.0304 on 2017 to 2026 (`RESULTS.md`, rows 19 and 23). **Against it:** the review's
figures are long-short spreads, its headline ones gross of costs (p. 11), and it does not study
transaction costs (pp. 26–27); this book holds the long leg alone, a fifth of a hundred of the
most traded names, re-struck monthly and net. The premium crashes at market reversals, 1929 and
2009 in the review's series (p. 8), when the previous year's losers rally (Paleologo, p. 77) —
losers this book does not short, and does not own either — and Paleologo names another crash in
early 2016, inside this window, in energy names that ran up two to three and a half times (p. 77).
On 2002 to 2016 the coefficient in that pool is below zero at a quarter and at a year, −0.0018 and
−0.0025 (rows 20 and 21): what it forecasts there looks spent within a quarter, and a delay loses
value at the rate of a signal's half-life
([Grinold & Kahn, ch. 13](../../Bibliotheca/Books/Grinold_Kahn_ND_Active_Portfolio_Management/16_The_Information_Horizon.md),
p. 353), which nothing here has measured: the month between re-strikes is the review's holding
period (p. 5), and the quarterly and late cells below are this experiment's only reading of what a
delay costs. And
[Sarkar, Du & Vafai (2019)](../../Bibliotheca/Papers/Sarkar_Du_Vafai_2019_Impacts_Of_Sector_And_Company_Size.md),
the one note on momentum among the largest companies, finds the factor significant for a
buy-and-hold portfolio of companies with sales above $1 billion (p. 10), with a negative
coefficient in every specification it prints (pp. 29, 30, 33 and 36), a sign its text never
discusses: a large-company book's return is tied to momentum, which is no evidence that it earns
the premium. The rule asserts nothing about being the best momentum rule; it asks whether the
ranking earns anything over the same pool's twenty most traded, on the same dates, net.

<!-- example: end -->

### The claim this moves

Which claim of `OBJECTIVE.md`, by number, this experiment exists to move, the status it reaches if
the predictions below hold, and the one it reaches if they fail. **One claim.** An experiment that
could beat every benchmark and settle nothing is a measurement, not a test.

<!-- example: begin -->

**Claim 5, momentum**, **measured**: the analyzer has read it, and no book has. If prediction 1
holds, the kill switch is silent, prediction 1's verdict is the same with every name filled at the
close, and the rule's Sharpe is above the index's, it moves to **confirmed as a book, for this
design, on the test window** — beating its benchmarks, as the vocabulary asks — quoted beside the
rule's margin over its control in each sub-period and on 2002 to 2016, and beside the analyzer's
rows 19 to 30, which were read before this blueprint. If prediction 1 fails or the kill switch
fires, it moves to **falsified**, for this design, on this window. It stays **measured**, and
`FINDINGS_3.md` says why, in three cases only: the rule or its control cannot be priced over the
test window; prediction 1 holds and the kill switch is silent, but the close fill changes
prediction 1's verdict; or all of that holds and the index's Sharpe is at or above the rule's.
Claim 1 is not moved: the cross is in neither book.

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
  by `Data/hand_supplied.py`, on the seed Experiment 2 widened to every listing the index held
  since 2000, read unchanged (`RESULTS.md`, *What stands*).
- **Exclusions:** exactly the names that fail Experiment 1's two tests — no price file, or an
  adjusted price that multiplies by more than six in a day — and those the universe notebook's
  identity check finds carrying two companies under one identifier, read from
  `Universe/Data_Issues.csv` as Experiment 2 read them: the same fifty-one names, listed in
  `JOURNAL_3.md` before the rule runs. If the file yields any other set, the difference and its
  reason are recorded there first, and no name is added or dropped once the rule has run. No name
  is excluded for a fall of any size: a fall is a return.
- **Pool:** on each rebalance date, the hundred members with the highest `r_liquidity_rank` at the
  prior close — the percentile of 63-day average traded value across every security in the panel,
  member or not — among the members with a price and a fill price at that close. A hundred makes
  the twenty its top fifth, the review's quintile (Baltussen et al., pp. 5–6); it is also the one
  pool size the analyzer measured, before this blueprint. A tie at the cut is broken by
  `main_identifier`, in alphabetical order, so every run draws the same pool.
- **Signal and selection:** of the pool, the twenty with the highest `r_momentum_12_1` at the
  prior close: the price 21 trading days before over the price 252 trading days before, less one,
  on the dividend-and-split-adjusted close (`Data/Refinery/custom_calculations.py`). A member with
  no value — fewer than 252 earlier days of prices, the column's warm-up — keeps its place in the
  pool and is not selectable; the hundred-and-first name does not take its place. A tie is broken
  as the pool's is.
- **Sizing and cash:** equal weight, one twentieth each. Any slot no name fills is held in `SHY`.
- **Timing:** the whole book re-struck, every name to one twentieth, on the first trading day of
  each month, whether or not a name changes; nothing trades between, and the weights drift. A
  window that does not open on a month start — the test's, on 2002-07-30 — is entered on its first
  trading day, then re-struck on each month start after it.
- **Lag:** one day. Every decision reads the prior close, on a window's first day too: the panel
  holds the closes before it. The engine fills at the day's VWAP, and at the day's close for the
  names fetched from Sharadar, which publishes no VWAP.
- **The fill convention, checked:** the rule and its control are priced again on the test window
  with every name filled at the day's close. If prediction 1's verdict differs between the two
  conventions, the experiment does not pass: its result would depend on how the dead names are
  filled.
- **Costs:** the engine's commission setting 0.1, 5 basis points of slippage and a 5% cash
  reserve, on $1,000,000: the cost row every verdict is read at. The reserve is 5% from the first
  run because this rule re-strikes the whole book every month, and in Experiment 2 one full
  re-equalisation on a rising day overdrew a 2% reserve and the engine stopped valuing the book
  (`RESULTS.md`, *Excluded runs*). A run that overdraws even so is not priced and is excluded by
  name, and it is not a pass: if the rule or its control is unpriced over the test window the
  experiment does not pass and claim 5 stays measured, and a sub-period or a cell with either of
  its runs unpriced counts against the rule. A different reserve after any run is a new experiment
  and one more trial, never a revision of this one. The setting 0.005 is reported beside the
  headline, as description.
- **Control:** the pool's twenty members with the highest `r_liquidity_rank` at the prior close,
  among those with a momentum value — the momentum ranking removed and nothing else: the pool, the
  warm-up, the lag, the sizing, the cash, the costs and the dates the same — re-struck on the rule's
  own dates. The owner chose on 2026-09-24, before any rule ran, that the control take only members
  with a momentum value, so that the ranking is its one difference. The same twenty without that
  restriction — the control with young listings, which can hold a member still inside the column's
  warm-up — is priced beside it over the test window as a diagnostic, never the verdict's control,
  and `FINDINGS_3.md` reports how often it held such a member and the gap between the two.
- **The null portfolio — description, never evidence:** the whole pool, one hundredth each, on the
  same dates.
- **Benchmark:** the KN US Equity 600, from the desk's own returns, staged as `KN600`.
- **Window — the test:** 2002-07-30, the cash proxy's first price, to 2026-06-01. The owner asked
  for 2002 to 2016 and 2017 to 2026; this is one window instead, which the kill switch reads in
  three sub-periods, the second opening in the year of the 2009 reversal, known when they were
  drawn. A silent kill switch does not say the rule beat its control on 2002 to 2016, since
  sub-period 1 may be lost: the rule and its control are also priced on 2002-07-30 to 2016-12-30
  as a window of its own, and `FINDINGS_3.md` reports that margin beside the verdict, as
  description; his second window is sub-period 3. Coverage on a date is the share of the index's
  weight, from the desk's holdings, in members with a price and a fill price that day, excluded
  names counted as unpriced. Experiment 2 measured it at 99.59% or more on every date from 2001 to
  2017, the years its run printed (`RESULTS.md`, *Known limitations*, row 7); nothing printed says
  what it is after 2017. It is measured again on every date of the test before any book is built,
  and recorded in `JOURNAL_3.md`; a date below 95% is listed in `FINDINGS_3.md`, never acted on.
  The window is fixed now.
- **Held out:** everything after 2026-06-01, for paper trading. No rule or engine run of this
  experiment reads it.
- **Screens deliberately absent:** the cross, which is claim 1's and would make this a third test
  of it; volatility scaling, a residual or industry-neutral rank and a short leg, each an open
  question below; a weight cap or a sector limit, each a lever a later experiment has to earn. A
  price floor is redundant in a pool of the hundred most traded.

**The perturbation, fixed now, each cell beside its own control on the test window**, the control
taking the cell's pool and book size and trading on the cell's own dates — for the three lookback
cells, the headline's control, and for the three pool cells too, since the twenty most traded of
any pool of fifty or more are the same twenty. The lookback at 6 months skipping 1, 126 trading
days with 21 left out; at 9 months skipping 1, 189 and 21; and at 12 months with no skip, 252 and
none — each computed in the notebook from the same adjusted close, as Experiment 1's perturbed
averages were, since the refinery carries one window; no cell costs a download. The pool at
50, 150 and 200 members. The book at 10 and 30 names. The book re-struck quarterly, on the first
trading day of January, April, July and October. The rule acted on 5 trading days late: each
decision read at the close before the headline's trade day — a month start, or the window's first
day — and filled on the fifth trading day after that trade day, its control reading the same close
and filling on the same day. The last two are the delay test of
[Grinold & Kahn, ch. 13](../../Bibliotheca/Books/Grinold_Kahn_ND_Active_Portfolio_Management/16_The_Information_Horizon.md)
(p. 353). Ten cells. **Criterion 3 of the gate in `Paper_Trading/BITACORA.md` is read as passed**
if, in at least eight of the ten, the rule's Sharpe and its CAGR are both above its control's.
Every other cell counts against it — one the rule ties or trails on either measure, one that could
not be priced, and a delay cell whatever a delay is expected to cost — whether or not the headline
passed.

**The trial count:** the forty-three `RESULTS.md` publishes, then this experiment's rule, one, and
its ten cells: **fifty-four**. The control, the control with young listings, and every sub-period,
fill-convention and realistic-cost run are listed by name in `FINDINGS_3.md` as diagnostics, and
the null portfolio's and the 2002-to-2016 window's runs as description, never evidence; none is a
trial. A change after any run to a setting under *What would falsify it* is a new experiment, and
one more trial.

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
| 1 | On the test window the rule beats its control by **at least 0.03 of Sharpe and 0.5 points a year of CAGR**, net, at the headline cost row, each margin read unrounded from the engine's figures. The margins are the ones `BLUEPRINT_1.md` fixed and `BLUEPRINT_2.md` carried, so three experiments are judged by one bar, and both are required | Analyzer section 5 (`RESULTS.md`): among the hundred most traded, a coefficient at 21 days of 0.0134 on 2002 to 2016, positive on 54.7% of 3,633 dates, and 0.0304 on 2017 to 2026, on 56.1% of 2,344 (rows 19 and 23); on month starts alone, where consecutive windows share only the days by which a month falls short of 21 trading days ([Grinold & Kahn, ch. 13](../../Bibliotheca/Books/Grinold_Kahn_ND_Active_Portfolio_Management/16_The_Information_Horizon.md), p. 365), 0.0140 on 56.1% of 173 and 0.0170 on 50.9% of 112 (rows 22 and 26); and the twenty highest above the pool's mean over the next 21 days by 0.14% and 0.83% on month starts, in 56.6% and 55.4% of them (rows 27 and 28). [Baltussen et al. (2025)](../../Bibliotheca/Papers/Baltussen_Dom_VanVliet_Vidojevic_2025_Momentum_Factor_Investing.md): the twelve months less the latest, held a month (p. 5), 7.89% a year value-weighted in the United States over 1990–2024, t 2.07 (p. 8), positive in all 31 countries since 1990 (p. 10). **Against it:** on 2002 to 2016 the coefficients at 63 and 252 days are −0.0018 and −0.0025 (rows 20 and 21); a long-only top quintile of the pool holds only the long leg of the review's spreads, whose headline figures are gross of costs (p. 11); a monthly re-strike pays turnover the analyzer's spread does not; and rows 27 and 28 carry no lag and no costs, in a pool that ranks non-members too, against its mean rather than its twenty most traded | either margin not reached |
| 2 | The rule beats the KN US Equity 600 on Sharpe over the test window | **A lead, not a licensed prediction.** No note and no analyzer section compares a long-only momentum book with this index: the review's winners beat its losers, not the market. Against it: the same liquid names without a signal trailed the index on 2002 to 2016, Experiment 2's control at 0.2556 against 0.4383, and matched it on 2017 to 2026, Experiment 1's control at 0.7748 against 0.7699, each on its own rule's dates, Experiment 1's at a 2% reserve (`RESULTS.md`) | the index's Sharpe at or above the rule's |
| 3 | From 2009-03-02 to 2009-12-31 the rule trails its control on return: its value on 2009-12-31 over its value at the close before 2009-03-02, read from the test run's daily series, is below the control's read the same way | [Baltussen et al. (2025)](../../Bibliotheca/Papers/Baltussen_Dom_VanVliet_Vidojevic_2025_Momentum_Factor_Investing.md): momentum's crash "around the market reversal in 2009" (p. 8); [Paleologo (2021), ch. 5](../../Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/09_Understand_Factors.md): in 2009 the previous year's losers rallied as the market rebounded (p. 77). Into the rebound the rule holds the names that fell least over the year before, and the control the most traded, that year's losers among them. Against it: the crash both describe came from the short leg (Paleologo, p. 77), which this book does not hold, and nothing read says how the long leg alone fared in 2009. The start, 2009-03-02, is drawn from the known history of 2009, not from either note, which date the rebound no closer than the year | the rule's return over those dates at or above its control's |

**Watched, but not predicted:** the betas of the rule and the control side by side; the momentum
line step 6 assigns each, and what is left of the rule's idiosyncratic return once it is out;
turnover a year and per re-strike, and the names changed each month; the weight in `SHY`; the
share of each book's weight in Sharadar names; the control with young listings beside the
control, and how often it held a member with no momentum value; the 2002-to-2016 window's margin;
and the null portfolio beside both. Nothing licenses a prediction about what a monthly re-strike
costs, so both cost rows are reported.

<!-- example: end -->

### Success criteria

What the experiment has to show to count as a success, fixed now. At the least:

1. It beats the benchmark `BRAINSTORMING_1.md` names **and its own control** on risk-adjusted
   return, net, over the same window — criterion 1 of the gate in `Paper_Trading/BITACORA.md`.
2. Reproducible from a clean clone, through the pipeline, with no manual step.
3. A tradeable trigger frequency — not a rule that fires every day.
4. Every prediction above evaluated explicitly in `FINDINGS_3.md`, **including the ones that turn
   out wrong.**

**Success is necessary for graduation, not sufficient.** The gate's five criteria in
`Paper_Trading/BITACORA.md` decide it, and a person signs it.

<!-- example: begin -->

Here, in full: prediction 1's margins on the test window; the kill switch below silent; the same
verdict with every name filled at the close; the rule beating the index on Sharpe; a run reproduced
end to end from a wiped working copy, with the Sharadar names' Curator at its recorded commit; the
rule trading on fewer days than it does not; and every prediction evaluated in `FINDINGS_3.md`.
Then the gate in `Paper_Trading/BITACORA.md` decides graduation, row by row, and the owner signs or
does not. If he signs, `Paper_Trading/promote.py 3` freezes the book as `Paper_Trading_3` — a
paper book takes its experiment's number — and `Paper_Trading/daily_update.py` tracks it from its
freeze date.

<!-- example: end -->

### What would falsify it

**One condition for the whole experiment, fixed now.** Each prediction above has its own falsifier;
this is the result under which the experiment as a whole has failed — usually a margin against its
control, or a result that holds in one sub-period and not in the others. Then **the
changes that may not rescue it**: every setting that could be moved once the result is in — a
holding count, a trigger, a window, a threshold — by name. Moving one after the result is a new
experiment, and one more trial in the count.

<!-- example: begin -->

**The kill switch: prediction 1's margins missed over the window, or an edge in fewer than two of
three sub-periods.** The experiment fails if the rule does not beat its control by both of
prediction 1's margins over the test window, **or** if fewer than two of the three sub-periods have
the rule's Sharpe and its CAGR both above its control's in that same sub-period, at the headline
cost row — 2002-07-30 to 2008-12-31, 2009-01-02 to 2016-12-30, and 2017-01-03 to 2026-06-01 — each
priced by the engine as a window of its own, the rule entering on its first day and its control
held to that rule's dates. The second opens in the year of the reversal prediction 3 is about; the
third is the window Experiment 1 ran on.

**The changes that may not rescue it:** the members, the widened seed, and the exclusions with
their tests and their fifty-one names; the pool of a hundred, its liquidity rank and the
tie-break; the momentum column, its 252-day lookback and its 21-day skip; the twenty names, equal
weight, and `SHY` for an unfilled slot; the re-strike on the first trading day of each month and
the entry on a window's first day; the one-day lag; which provider serves each name, how its fill
is made, and the two Curator versions; the control, the control with young listings and the null
portfolio; the benchmark; the commission setting 0.1, the 5 basis points, the 5% reserve and the
$1,000,000; the test window, its coverage rule and the hold-out after 2026-06-01; the sub-periods;
prediction 1's margins; and the perturbation's ten cells and its threshold of eight.

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

- **Crash risk at market reversals.** Momentum's crashes fall at reversals, 1929 and 2009
  ([Baltussen et al.](../../Bibliotheca/Papers/Baltussen_Dom_VanVliet_Vidojevic_2025_Momentum_Factor_Investing.md),
  p. 8), when the previous year's losers rally
  ([Paleologo, ch. 5](../../Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/09_Understand_Factors.md),
  p. 77). This book has no short leg, but it holds the year's winners into a rebound the losers
  lead. Prediction 3 measures it inside sub-period 2, which opens on 2009-01-02. A sub-period
  counts for the rule only if its Sharpe and its CAGR are both above its control's there; losing
  sub-period 2 and one other fires the kill switch, and so does missing prediction 1's margins over
  the whole window, whatever the sub-periods show.
- **Turnover and costs.** Every name is re-struck to one twentieth every month, and the review
  studies no transaction costs (pp. 26–27). `FINDINGS_3.md` reports turnover a year and per
  re-strike, the names changed, and commission and slippage at both cost rows; every verdict is
  read at the headline row. The 5% reserve is there for the same reason.
- **The liquidity rank's cross-section.** `r_liquidity_rank` is a percentile across every security
  in the panel, member or not. The pool takes members in its order, so non-members move the rank's
  value and never the pool; but the analyzer's pool is the hundred most traded securities, members
  or not (`RESULTS.md`, rows 19 to 30), a neighbour of this pool and not this pool.
- **The dead names are filled differently, and two Curator versions serve them.** The Sharadar
  names fill at the close and the rest at the day's VWAP (`RESULTS.md`, *Known limitations*, row
  9). The fill check prices the difference. `FINDINGS_3.md` reports, for the rule and the control
  alike, the share of weight in Sharadar names, and every name held on its last priced day with its
  weight, read from the engine's log: in Experiment 2 the notebook's check printed none where the
  log named six (`RESULTS.md`, *Open leads*, 2). The engine's exit at the last price spares
  whichever book holds a failing name to the end.
- **The test is of the book, not of the signal out of sample.** The analyzer measured the signal
  on both halves of the test window before this blueprint, and the owner chose it after step 6 had
  charged Experiment 1's books with momentum on 2017 to 2026. The signal's out-of-sample evidence
  is the published record — 61 years before CRSP and 31 countries since 1990 (Baltussen et al.,
  pp. 10–11) — and this run adds a book to it, not a new sample.
- **Fifty-four trials across three experiments**, on one universe whose years every experiment has
  read. The deflated Sharpe has never been computed (`RESULTS.md`, *Known limitations*, row 6); a
  pass here is the best of fifty-four, and `FINDINGS_3.md` publishes the count beside it.
- **The signal is a factor.** A book of the top of a momentum rank is long the momentum factor by
  construction, and step 6's factor model carries a momentum line: criterion 2 of the gate asks
  what is left of the rule's return once that line is out, and the honest product may be a cheaper
  momentum fund. The factor files begin on 2008-01-14 (`RESULTS.md`), so the test window is
  attributed from that date only: sub-period 1 for 2008 alone, and nothing before it.
- **Concentration.** Twenty names chosen on a year's return can crowd into whichever sector led the
  year and shun whichever led the fall; the crash Paleologo describes in early 2016 was concentrated
  in energy names that ran up two to three and a half times (p. 77). The desk's sector factor files
  are empty (`RESULTS.md`, *Open leads*, 5), so no sector reading is available here.
- **A lead against it, unread.** Lee & Swaminathan (2000), a lead in `Bibliotheca/BIBLIOGRAPHY.md`
  with no note, is listed there as finding heavily traded stocks' past winners reversing sooner —
  this rule's own names. Unread, it licenses nothing; it is named so the reading is not skipped.

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
| 2 | Does a long-short book, the pool's top fifth against its bottom fifth, earn what the long leg alone does not? | a short leg brings borrow cost, short rebate and margin, which the engine does not model (`AGENTS.md`, the five ways a backtest lies, row 4), and it is the leg momentum crashed on in 2009 (Paleologo, p. 77) |
| 3 | Does scaling each name by its own trailing volatility cut what a reversal costs? | a new moving part; Baltussen et al.'s stock-level scaling cut the long-short drawdown from −88.41% to −54.64% at a similar return (p. 26) |
| 4 | Does residual or industry-neutral momentum earn more? | residual momentum needs a factor model's residual in the refinery (Baltussen et al., p. 18); an industry-neutral rank needs point-in-time industries, and no rule selects on a `current_*` column |

<!-- example: end -->
