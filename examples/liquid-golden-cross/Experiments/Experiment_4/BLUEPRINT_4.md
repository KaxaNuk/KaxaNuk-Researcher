# Blueprint — Experiment 4

> **The hypothesis, fixed once written.** Thesis, the claim it moves, rules, predictions, success
> criteria, what would falsify it and key risks, recorded *before* any code runs.
>
> **This file does not change when results arrive.** A hypothesis edited after its test is no longer
> a hypothesis — that is the whole reason it is kept apart from the result. What the experiment
> actually produced is in [`FINDINGS_4.md`](FINDINGS_4.md); planning lives in
> [`BRAINSTORMING_4.md`](BRAINSTORMING_4.md), the running log in [`JOURNAL_4.md`](JOURNAL_4.md).
>
> Record the date it was written, and delete this blockquote.

---

## Experiment 4 — momentum, outside bear markets

<!-- example: begin -->

**Written 2026-09-25, before any rule was coded, and revised the same day after a cold review by the
blueprint critic, before its commit.** `liquid-golden-cross`.

Claim 5's second design. Experiment 3's book of the twenty of the hundred most traded members with
the highest twelve-month return trailed the pool's twenty most traded by 0.22 points a year over
2002-07-30 to 2026-06-01, ahead of them in one sub-period of three, and failed its kill switch
(`RESULTS.md`). The owner chose on 2026-09-25, as `BRAINSTORMING_4.md` records, to hold momentum's
twenty only outside a bear market — the KN US Equity 600's return over the prior 24 months below
zero — and the pool's twenty most traded inside one; and, as `JOURNAL_4.md` records, a 10% cash
reserve, a check that ends a listing at its last distinct bar, twelve perturbation cells, and a
state that has to beat momentum in every month. It moves claim 5 of `OBJECTIVE.md` again; the cross
is in neither the rule nor its control.

**This design was chosen after its weak spot was seen, and three things were known when it was
written.** First, on 2017 to 2026 the state covers three month starts, so there the rule is
Experiment 3's almost month for month, and Experiment 3's rule led its control in that sub-period on
both measures, 0.852 against 0.744 and 22.49% against 18.03% (`FINDINGS_3.md`): sub-period 3 is
expected to count for the rule, and the kill switch's sub-period limb turns on sub-periods 1 and 2,
which hold the bear months the state removes and in both of which Experiment 3's rule trailed.
Second, the rule and the diagnostic arm differ only in bear months, and over 2009-03-02 to
2009-12-31, all bear months, Experiment 3 measured the arm's book at +29.14% against the bear-month
book's +65.93%: the kill switch's limb against the arm is partly known. Third, the four cells
Experiment 3 could not price — lookback 6 months and book size 10, which overdrew a 5% reserve in
2003, and pools 150 and 200, refused over `VMW` — return here, and the 10% reserve and the
stale-bars check, both chosen after that run, remove those causes. The paper the state comes from
was carried into `Bibliotheca/` after Experiment 3 reported, and the analyzer measured momentum by
state before this blueprint (`RESULTS.md`, rows 31 to 38). What this experiment tests is whether the
rule, written down now with its margins and its kill switch, clears them net; the unseen test is
paper trading, if it passes.

<!-- example: end -->

### Thesis

One paragraph: what book this rule produces, why it should beat the benchmark
`BRAINSTORMING_1.md` names, and why it is also a fair yardstick — sensible, liquid, low-complexity
— for judging whether any later idea adds value. **Be modest on purpose.** A first rule does not
assert its signal is the best of its kind, only that it is simple enough to be understood, liquid
enough to be traded, and stable enough to measure other things against.

<!-- example: begin -->

Own the twenty members of the KN US Equity 600 with the highest return over the twelve months before
the latest one, chosen from the hundred most traded, equally weighted and re-struck on the first
trading day of each month — **except in a month that opens after a negative two-year market**, when
the book holds the same pool's twenty most traded instead. **Why momentum pays at all** is
Experiment 3's reason, investors underreacting to news, which the review behind claim 5 leans to
over risk ([Baltussen et al.
(2025)](../../Bibliotheca/Papers/Baltussen_Dom_VanVliet_Vidojevic_2025_Momentum_Factor_Investing.md),
pp. 27–28). **Why it is left out after a fall** is Daniel and Moskowitz's: in their US sample, 1927
to 2013, every one of the fifteen worst momentum months came when the market's return over the prior
24 months was negative ([Daniel & Moskowitz
(2013)](../../Bibliotheca/Papers/Daniel_Moskowitz_2013_Momentum_Crashes.md), p. 15); after a fall
past winners are low-beta, defensive names, betas below 0.5 against the past losers' above 3 (pp. 6,
16), and a rebound leaves them behind; in bear markets momentum behaves like a written call on the
market (p. 7), whose shape the paper does not find outside them (pp. 23–24); and with the bear
indicator, the bear-market alpha is "−1 basis point per month" against an unconditional intercept of
1.9 percent a month (p. 21). The paper's crashes are in the short leg (p. 15), which this book does
not hold, but the lag is in the long leg: Experiment 3's twenty gained 29.14% over the 2009 rebound
against the most traded twenty's 65.93%. The analyzer, in a neighbour of this pool, finds the signal
turning with the state on 2002 to 2016: a coefficient at a month of −0.0362, positive on 45.2% of
dates, in bear months, and 0.0284, on 57.6%, outside them, each an average of daily 21-day windows
that share 20 of 21 days; and the twenty highest trailing the twenty most traded by 0.49% a month on
39 bear month starts, and leading them by 0.24% on 134 others (`RESULTS.md`, rows 31, 32, 35 and
36). **Against it:** on 2017 to 2026 the coefficient in a bear state is 0.0442, positive on 55.8% of
77 dates (row 33), the opposite of 2002 to 2016's sign; outside bear months the lead before costs is
small, 0.24% a month on 2002 to 2016 and 0.12% on 2017 to 2026 (rows 36 and 38), and a monthly
re-strike pays turnover the analyzer's lead does not; the state barely occurs after 2010, so there
the rule is Experiment 3's; the paper's evidence is long-short deciles of every common share, before
costs, and its dynamic strategy is fitted in sample (pp. 26–30, 47–48); its second forecasting
variable, the market's variance, is not used; it finds no risk explanation for the crash state
(p. 46) and tests no behavioural one; [Paleologo (2021), ch.
5](../../Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/09_Understand_Factors.md)
records a crash in early 2016, in energy names, which falls in no bear month here, and a 2008 in
which momentum was volatile but did not lose money, while October to December 2008 are bear months
here (p. 77); and [Sarkar, Du & Vafai
(2019)](../../Bibliotheca/Papers/Sarkar_Du_Vafai_2019_Impacts_Of_Sector_And_Company_Size.md) find a
large-company portfolio's momentum coefficient negative in every specification they print (pp. 29,
30, 33 and 36), which `OBJECTIVE.md` reads as no support for claim 5. The rule asserts nothing about
being the best momentum rule; it asks whether the ranking, used only outside bear months, earns
anything over the pool's twenty most traded, net, on the same dates, and more than the same ranking
used in every month.

<!-- example: end -->

### The claim this moves

Which claim of `OBJECTIVE.md`, by number, this experiment exists to move, the status it reaches if
the predictions below hold, and the one it reaches if they fail. **One claim.** An experiment that
could beat every benchmark and settle nothing is a measurement, not a test.

<!-- example: begin -->

**Claim 5, momentum**, **falsified, for Experiment 3's design, on 2002 to 2026**. If prediction 1
holds, the kill switch is silent — which asks the rule to beat the diagnostic arm as well —
prediction 1's verdict is the same with every name filled at the close, and the rule's Sharpe is
above the index's, it moves to **confirmed as a book, for this design — the ranking held outside
bear months, a design chosen after this window's result was seen — on the test window**, quoted
beside Experiment 3's falsification, beside the rule's margin over its control in each sub-period,
and beside rows 31 to 38, read before this blueprint. If prediction 1 fails or the kill switch
fires, it stays **falsified**, now for two designs on this window. Its status does not move, and
`FINDINGS_4.md` says why, in three cases only: the rule or its control cannot be priced over the
test window; prediction 1 holds and the kill switch is silent, but the close fill changes prediction
1's verdict; or all of that holds and the index's Sharpe is at or above the rule's. Claim 1 is not
moved: the cross is in neither book.

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

- **Carried from Experiment 3, unchanged:** the universe, the KN US Equity 600's members as of each
  date on the widened seed; the exclusions, the fifty-one names Experiment 1's two tests and the
  identity check give, read from `Universe/Data_Issues.csv` and listed in `JOURNAL_4.md` before the
  rule runs; the pool, the hundred members with the highest `r_liquidity_rank` at the prior close
  among those with a price and a fill price, a tie broken by `main_identifier`; outside a bear
  month, the twenty of them with the highest `r_momentum_12_1` at the prior close, a member with no
  value keeping its place in the pool and not selectable; one twentieth each, and `SHY` for a slot
  no name fills; the whole book re-struck on the first trading day of each month, and a window
  entered on its first trading day; one day of lag; fills at the day's VWAP, and at the close for
  the names fetched from Sharadar; and the fill convention checked by pricing the rule and its
  control again with every name at the close, the experiment not passing if prediction 1's verdict
  differs.
- **The state:** the KN US Equity 600's level is compounded from the desk's daily returns, read by
  `Data/hand_supplied.py`, on the desk's own dates. On each rebalance date the level at the last
  desk date before it, over the level 504 desk dates earlier, less one, is the index's return over
  the prior 24 months — the paper's window (p. 20), a year taken as 252 trading days as the refinery
  takes it — and **the month is a bear month when it is below zero**. The book changes with the
  state only at a re-strike. The index's returns begin on 2000-01-03, so the state is known before
  the window opens. The bear month starts inside the window, counted this way, are listed in
  `JOURNAL_4.md` before the rule runs; the analyzer, which read the state at each date's close, a
  day later, counted 42.
- **Selection in a bear month:** the control's own book — the pool's twenty members with the highest
  `r_liquidity_rank` at the prior close among those with a value in the headline's `r_momentum_12_1`
  — so in a bear month the rule and its control hold the same book. In a perturbation cell, it is
  that cell's control's book, at the cell's pool and size.
- **Stale bars, a data check fixed now:** every price file is first cut at 2026-06-01, so the check
  reads nothing held out. A listing's last distinct bar is its last row whose unadjusted open, high,
  low and close, `m_open`, `m_high`, `m_low` and `m_close` as the Curator prints them, are not all
  equal to the row before it. When one or more rows follow it and every one of them repeats those
  four values exactly, those rows are read as no price, whatever the gaps between their dates: the
  listing ends at its last distinct bar, for the panel the rule reads and for the files the engine
  prices from, which then sells a holding at that bar's price as it sells any listing that stops
  trading. A run whose last row is the window's last trading day is not read as an ending, since the
  listing may trade on. The Curator's files are not changed; the notebook stages the engine's copy.
  **The check uses hindsight** beyond the one day `AGENTS.md` names for a delisting exit: it ends a
  listing on the evidence of rows up to the window's end, years later for `CSC`, whose repeated run
  lasts from 2017-04-03 to 2021-09-10. It excludes no name, applies to the rule and its control
  alike, and the listings it ends are listed in `JOURNAL_4.md` before the rule runs; Experiment 3's
  scan found nine inside the window, `VMW` among them (`RESULTS.md`, *Known limitations*, row 11).
- **Costs:** the engine's commission setting 0.1, 5 basis points of slippage and a **10% cash
  reserve**, on $1,000,000: the cost row every verdict is read at. The reserve is 10% because in
  Experiment 3 a full monthly re-strike overdrew 5% in two cells' rules in 2003, by $16,557.91 and
  $19,025.14 (`RESULTS.md`, *Excluded runs*): the owner chose it after that result and before any
  run of this experiment. The setting 0.005 is reported beside the headline, as description.
- **Control:** Experiment 3's control, the pool's twenty members with the highest `r_liquidity_rank`
  at the prior close among those with a momentum value, re-struck on the rule's own dates: the
  conditioned ranking removed and nothing else — the pool, the warm-up, the lag, the sizing, the
  cash, the costs, the data check and the dates the same.
- **The diagnostic arm, momentum in every month:** Experiment 3's rule, the ranking used in every
  month, at this experiment's reserve and with its data check, on the rule's dates. It prices what
  the state does; the kill switch asks the rule to beat it; it is never the verdict's control; and,
  a design of its own at this reserve, it counts as a trial. No result of it reopens Experiment 3's
  verdict.
- **The null portfolio — description, never evidence:** the whole pool, one hundredth each, on the
  same dates.
- **Benchmark:** the KN US Equity 600, from the desk's own returns, staged as `KN600`.
- **Window — the test:** 2002-07-30 to 2026-06-01, Experiment 3's, read by the kill switch in the
  same three sub-periods; the rule and its control are also priced on 2002-07-30 to 2016-12-30 as a
  window of its own, as description. Coverage is measured again on every date of the test before any
  book is built and recorded in `JOURNAL_4.md`, and a date below 95% is listed in `FINDINGS_4.md`,
  never acted on. The window is fixed now.
- **Held out:** everything after 2026-06-01, for paper trading. No rule, check or engine run of this
  experiment reads it.
- **A run the engine cannot price** — refused, or valuing the book only partway through its window —
  is named with the engine's reason. If it is the rule's or its control's run over the test window,
  the experiment does not pass and claim 5's status does not move; if it is a sub-period's or a
  cell's run, it counts against the rule. A name held with no price anywhere in a run's window is
  dropped from that run's weight file, its weight left in cash.
- **Screens deliberately absent:** the cross, claim 1's; the market's variance, the paper's second
  state variable; volatility scaling, a short leg, a residual or industry-neutral rank; a weight cap
  or a sector limit — each a lever a later experiment has to earn.

**The perturbation, fixed now, each cell beside its own control on the test window**, the control
taking the cell's pool, book size and delay and trading on the cell's own dates, and the rule
holding that control's book in a bear month; the state stays at its 504 days in every cell but the
two that move it, and the control never reads it. The state's window at 252 desk dates, twelve
months, and at 756, thirty-six — the window Cooper, Gutierrez and Hameed (2004) used, cited by the
Daniel and Moskowitz note (p. 5) and not held in `Bibliotheca/` — the 756-day cell reading the
504-day state until 756 desk dates of the index exist, at the end of 2002. The lookback at 6 months
skipping 1, 9 months skipping 1, and 12 months with no skip, the cell's column ranking the rule
outside bear months, and the headline's `r_momentum_12_1` deciding "a momentum value" for the
control and for the rule's bear-month book, as Experiment 3's lookback cells took the headline's
control. The pool at 50, 150 and 200 members; the book at 10 and 30 names; the book re-struck
quarterly, on the first trading day of January, April, July and October; and the rule acted on 5
trading days late, each decision read at the close before the headline's trade day and filled on the
fifth trading day after that trade day, its control reading the same close and filling on the same
day. Twelve cells. **Criterion 3 of the gate in `Paper_Trading/BITACORA.md` is read as passed** if,
in at least ten of the twelve, the rule's Sharpe and its CAGR are both above its control's. Every
other cell counts against it — one the rule ties or trails on either measure, one that could not be
priced, and a delay cell whatever a delay is expected to cost — whether or not the headline passed.

**The trial count:** the fifty-four `RESULTS.md` publishes, then this experiment's rule, the
diagnostic arm, and the twelve cells: **sixty-eight**. The control, and every sub-period,
fill-convention and realistic-cost run are listed by name in `FINDINGS_4.md` as diagnostics, and the
null portfolio's and the 2002-to-2016 window's runs as description, never evidence. A change after
any run to a setting under *What would falsify it* is a new experiment, and one more trial.

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
| 1 | On the test window the rule beats its control by **at least 0.03 of Sharpe and 0.5 points a year of CAGR**, net, at the headline cost row, each margin read unrounded from the engine's figures — the margins every experiment here has been judged by, and both are required | Analyzer section 5 (`RESULTS.md`), in a neighbour of this pool — the hundred most traded securities, members or not, less those with no momentum value, on a panel that still holds the repeated bars this rule's panel ends — with the state read at each date's close, a day later than the rule reads it: outside bear months the twenty highest lead the twenty most traded over the next 21 days by 0.24% a month on 134 month starts of 2002 to 2016, in 56.7% of them, and by 0.12% on 109 of 2017 to 2026, in 51.4% (rows 36 and 38); in bear months they trail by 0.49% on 39 (row 35); the coefficient at a month is −0.0362, positive on 45.2% of dates, in bear months and 0.0284, on 57.6%, outside them on 2002 to 2016, daily 21-day windows sharing 20 of 21 days (rows 31 and 32). [Daniel & Moskowitz (2013)](../../Bibliotheca/Papers/Daniel_Moskowitz_2013_Momentum_Crashes.md): every one of the fifteen worst momentum months after a negative two-year market (p. 15); a bear-market alpha of −1 basis point a month against an unconditional 1.9 percent (p. 21). **Against it:** Experiment 3's book trailed this control by 0.22 points a year over this window; the lead outside bear months is before costs and lag, and a monthly re-strike pays more turnover than the control's; on 2017 to 2026 the bear-state coefficient is positive, 0.0442 (row 33), and the state barely occurs, so on most of sub-period 3 the rule is Experiment 3's | either margin not reached |
| 2 | The rule beats the KN US Equity 600 on Sharpe over the test window | **A lead, not a licensed prediction.** No note compares a long-only momentum book with this index; what would license it is a measurement the analyzer has not made — the twenty highest outside bear months against the index's own return over the next 21 days — or a note on a long-only momentum index against its market, which `Bibliotheca/` does not hold. Against it: Experiment 3's book read 0.4358 against the index's 0.5682, and the same liquid names without a signal 0.4647 (`RESULTS.md`) | the index's Sharpe at or above the rule's |
| 3 | The rule beats the diagnostic arm, momentum in every month, on both Sharpe and CAGR over the test window: the state earns its place. **Partly known in advance, and a limb of the kill switch**: `FINDINGS_4.md` reports it as a condition met or missed, never as a prediction that held | Daniel & Moskowitz: momentum returns are low after a negative two-year market (pp. 15, 26); rows 31 and 35: in the neighbour pool the signal is below zero in those months and the twenty highest trail the twenty most traded; Experiment 3's 2009 rebound, all bear months, measured the arm's book at +29.14% against the bear-month book's +65.93%. **Against it:** a switch between the two books at the state's turns re-strikes more of the book; after 2010 the state covers three month starts; row 33 | the rule's Sharpe or its CAGR at or below the arm's |

**Watched, but not predicted:** the betas of the rule, its control and the arm side by side; the
momentum line step 6 assigns each, and what is left of the rule's idiosyncratic return once it is
out; turnover a year and per re-strike, and on the re-strikes where the state turns; the bear month
starts in each sub-period; the weight in `SHY`; the share of each book's weight in Sharadar names;
whether either book held a listing past the last distinct bar the check ends it at; the 2002-to-2016
window's margin; and the null portfolio beside all three. Nothing licenses a prediction about what a
monthly re-strike costs, so both cost rows are reported.

<!-- example: end -->

### Success criteria

What the experiment has to show to count as a success, fixed now. At the least:

1. It beats the benchmark `BRAINSTORMING_1.md` names **and its own control** on risk-adjusted
   return, net, over the same window — criterion 1 of the gate in `Paper_Trading/BITACORA.md`.
2. Reproducible from a clean clone, through the pipeline, with no manual step.
3. A tradeable trigger frequency — not a rule that fires every day.
4. Every prediction above evaluated explicitly in `FINDINGS_4.md`, **including the ones that turn
   out wrong.**

**Success is necessary for graduation, not sufficient.** The gate's five criteria in
`Paper_Trading/BITACORA.md` decide it, and a person signs it.

<!-- example: begin -->

Here, in full: prediction 1's margins on the test window; the kill switch below silent, the rule
beating the diagnostic arm on both measures among its limbs; the same verdict with every name filled
at the close; the rule beating the index on Sharpe; a run reproduced end to end from a wiped working
copy, with the Sharadar names' Curator at its recorded commit; the rule trading on fewer days than
it does not; and every prediction evaluated in `FINDINGS_4.md`. Then the gate in
`Paper_Trading/BITACORA.md` decides graduation, row by row, and the owner signs or does not. If he
signs, `Paper_Trading/promote.py 4` freezes the book as `Paper_Trading_4` and
`Paper_Trading/daily_update.py` tracks it from its freeze date.

<!-- example: end -->

### What would falsify it

**One condition for the whole experiment, fixed now.** Each prediction above has its own falsifier;
this is the result under which the experiment as a whole has failed — usually a margin against its
control, or a result that holds in one sub-period and not in the others. Then **the
changes that may not rescue it**: every setting that could be moved once the result is in — a
holding count, a trigger, a window, a threshold — by name. Moving one after the result is a new
experiment, and one more trial in the count.

<!-- example: begin -->

**The kill switch: prediction 1's margins missed over the window, an edge in fewer than two of three
sub-periods, or a state that does not beat momentum in every month.** The experiment fails if the
rule does not beat its control by both of prediction 1's margins over the test window; **or** if
fewer than two of the three sub-periods have the rule's Sharpe and its CAGR both above its control's
in that same sub-period, at the headline cost row — 2002-07-30 to 2008-12-31, 2009-01-02 to
2016-12-30, and 2017-01-03 to 2026-06-01, Experiment 3's — each priced by the engine as a window of
its own, the rule entering on its first day and its control held to that rule's dates; **or** if the
rule's Sharpe or its CAGR over the test window is at or below the diagnostic arm's. The first two
sub-periods hold the window's bear months and the third holds three: sub-period 3 is expected to
count for the rule, as the opening of this blueprint says, so the sub-period limb turns on the first
two.

**The changes that may not rescue it:** the members, the widened seed, and the exclusions with their
tests and their fifty-one names; the pool of a hundred, its liquidity rank and the tie-break; the
momentum column, its 252-day lookback and its 21-day skip, and a member with no value keeping its
place in the pool and not selectable; the state — its series, the index's own returns on the desk's
dates, its 504-day window, its threshold at zero and its reading at the prior close — and what the
book holds in a bear month; the twenty names, equal weight, and `SHY` for an unfilled slot; the
monthly re-strike and the entry on a window's first day; the one-day lag; which provider serves each
name, how its fill is made, the two Curator versions, and the close-fill condition on prediction 1's
verdict; the stale-bars check, its fields, its equality, its reading of gaps and its cut at
2026-06-01; dropping a name held with no price anywhere in a run's window, its weight left in cash;
a sub-period or cell run the engine cannot price counting against the rule; the control, the
diagnostic arm and its limb of the kill switch, and the null portfolio; the benchmark; the
commission setting 0.1, the 5 basis points, the 10% reserve and the $1,000,000; the test window, its
coverage rule and the hold-out after 2026-06-01; the sub-periods; prediction 1's margins; and the
perturbation's twelve cells, their definitions and the threshold of ten.

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

- **The design follows its own evidence.** The state was chosen after Experiment 3's book lost the
  2009 rebound, in months this state covers, and measured on the years it will be tested on; the
  reserve and the stale-bars check were chosen after Experiment 3's four cells could not be priced.
  A pass here is weaker evidence than its margins suggest: the trial count, sixty-eight, is
  published beside it, and the unseen test is paper trading.
- **A rare state.** The analyzer counted forty-two of the window's month starts, thirty-nine of them
  in 2002–2003 and 2008–2010, both seen, and three after 2010. What the state is worth rests on two
  episodes, and on 2017 to 2026 the rule is Experiment 3's almost month for month.
- **The analyzer's pool and timing are not the rule's.** Rows 31 to 38 read the state a day later
  than the rule, in a pool that ranks non-members and drops names with no momentum value before
  taking the hundred, on a panel that still holds the repeated bars. A month whose first day turns
  the state is classified differently by the two.
- **Crashes the state does not cover.** The Paleologo chapter's early-2016 crash, in energy names,
  falls in no bear month here, and the state takes no account of the market's variance.
- **Switching costs.** A turn of the state re-strikes the book from one twenty to another, on top of
  the monthly re-strike. `FINDINGS_4.md` reports turnover on those re-strikes apart.
- **Turnover and costs.** Every name is re-struck to one twentieth every month, and the paper
  reports no turnover and charges no costs (pp. 47–48). Every verdict is read at the headline row,
  at which Experiment 3's rule paid $780,587.10 of commission against its control's $350,769.30. The
  10% reserve is held by every book.
- **The dead names are filled differently, and two Curator versions serve them**, as in Experiment
  3; the fill check prices the difference, and `FINDINGS_4.md` reports the Sharadar share of each
  book and every name the engine sold at its last price, from the engine's log.
- **The stale-bars check reads only a file's end, with hindsight.** A run of repeated bars inside a
  listing's life, or a gap without repeats, is not caught by it; the engine carries the last mark
  across an interior gap and refuses a rebalance on a date a held name has no price, and such a run
  is named and counts against the rule.
- **The signal is a factor.** Experiment 3's ranking added 28.01 points of the momentum factor and
  took 5.59 idiosyncratic points away over 2008 to 2026. Criterion 2 asks what is left of this
  rule's return once the momentum line is out; the factor files begin on 2008-01-14, so 2002 to 2007
  are not attributed.
- **Concentration.** The desk's sector factor files are empty (`RESULTS.md`, *Open leads*), so no
  sector reading is available.
- **A lead against it, unread.** Lee & Swaminathan (2000), a lead in `Bibliotheca/BIBLIOGRAPHY.md`
  with no note, is listed as finding heavily traded stocks' past winners reversing sooner — this
  rule's own names.

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
| 2 | Does the market's variance, the paper's second state variable, add to the bear state? | a second moving part; the paper's weighting by both is fitted in sample (pp. 26–30) |
| 3 | Does a three-year state, Cooper, Gutierrez & Hameed's, do better? | a source with no note here; the 36-month cell is a perturbation of this rule, not a test of that paper |
| 4 | Does a long-short, volatility-scaled or residual momentum book earn what the long leg alone does not? | each is Experiment 3's open question, and each a new moving part |

<!-- example: end -->
