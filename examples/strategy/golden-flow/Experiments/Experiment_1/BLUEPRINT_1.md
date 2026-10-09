# Blueprint — Experiment 1

> **The hypothesis, fixed once written.** Thesis, the claim it moves, rules, predictions, success
> criteria, what would falsify it and key risks, recorded *before* any code runs.
>
> **This file does not change when results arrive.** A hypothesis edited after its test is no longer
> a hypothesis — that is the whole reason it is kept apart from the result. What the experiment
> actually produced is in [`FINDINGS_1.md`](FINDINGS_1.md); the running log, the thinking
> before this blueprint included, in [`JOURNAL_1.md`](JOURNAL_1.md).
>
> In a new strategy, record the date it was written and delete this blockquote.

<!-- example: begin -->

Versions such as 0.13.0 and 0.14.0 named below are Golden Flow's own earlier versions, on another
index, and are not in this copy; "the desk" is KaxaNuk's Analytics Factory; "the worked example"
means the package's earlier one.

<!-- example: end -->

---

## Experiment 1 — the first rule against the benchmark

<!-- example: begin -->

## Experiment 1 — the most-traded KN US Equity Core members in a golden cross, by traded value

**Written 2026-10-06, before any rule was coded.** Drafted with KaxaNuk-Researcher 0.31.0,
commit a680873.

**This blueprint replaces the one written on 2026-07-18** — the thirty most traded members of the
KN US Equity 600 in a golden cross, weighted by traded value, 2017 to 2026 — which is kept at tag
`0.14.0` and as a row of `RESULTS.md`. The owner decided the rewrite on 2026-10-05, as
`JOURNAL_1.md` records, and every book priced under the earlier designs counts in the trials below.

**Its fixed elements are the owner's; its predictions are not yet his.** The universe, the rule,
the control, the falsifier, the sweep, the gate's margins and the window are the plan the owner
approved on 2026-10-05. The thesis and the predictions were drafted afterwards from the analyzer and
the notes, unseen by the owner, under that go, and put to the `blueprint-critic` agent cold before
this commit; its objections, and what was done about each, are the journal entry of 2026-10-06
that precedes this file's commit.

<!-- example: end -->

### Thesis

One paragraph: what book this rule produces, why it should beat the benchmark
`JOURNAL_1.md` chose, and why it is also a fair yardstick — sensible, liquid, low-complexity
— for judging whether any later idea adds value. **Be modest on purpose.** A first rule does not
assert its signal is the best of its kind, only that it is simple enough to be understood, liquid
enough to be traded, and stable enough to measure other things against.

<!-- example: begin -->

Own the KN US Equity Core members the market trades most while their fifty-day average sits above
their two-hundred-day one, each in proportion to what it trades, none above a fifth of the book and
none below a hundredth.

**The economic reason the notes offer for the cross is a risk gate, not a return engine**: a name
falling through its averages is one the market is selling, and leaving it until the trend turns
cuts the drawdowns a book of the most traded names would otherwise ride through — the reading of
[Faber (2007)](../../Bibliotheca/Papers/Faber_2007_Quantitative_Approach_To_Tactical_Asset_Allocation.md),
whose filter is on asset-class indices rather than single names, and of
[Hurst, Ooi & Pedersen (2017)](../../Bibliotheca/Papers/Hurst_Ooi_Pedersen_2017_Century_Of_Evidence_On_Trend_Following.md),
whose books are volatility-scaled rather than liquidity-scaled. **The owner's gate asks for more
than that reading predicts**: a margin over the control in CAGR as well as in Sharpe. Nothing in
`Bibliotheca/` predicts the return limb; the analyzer gives it a sign and no size — the cross as a
state ranks the pool at +0.0235 over 21 days, +0.0275 over 63 and +0.0161 over 252, positive on
54.6%, 58.0% and 52.9% of dates, consecutive windows sharing 20, 62 and 251 days (`RESULTS.md`,
*Before any experiment*, rows 2 to 4). **A book that cuts drawdown at an equal return would confirm
the notes' reading and still falsify claim 1 as the owner wrote it**, and the findings will say so.

**For the sizing, the notes argue against it.** Weighting by traded value buys capacity and an
explanation a reader can repeat; the economic case that it also buys return is the attention
argument — the most traded names are where the market's money and information arrive first — and
no note in `Bibliotheca/` makes it. Against it,
[Amihud (2002)](../../Bibliotheca/Papers/Amihud_2002_Illiquidity_And_Stock_Returns.md),
[Datar, Naik & Radcliffe (1998)](../../Bibliotheca/Papers/Datar_Naik_Radcliffe_1998_Liquidity_And_Stock_Returns.md)
and
[Ibbotson, Chen, Kim & Hu (2013)](../../Bibliotheca/Papers/Ibbotson_Chen_Kim_Hu_2013_Liquidity_As_An_Investment_Style.md)
put the liquidity premium on the other side, and this repository's analyzer agreed with them on
the universes of earlier versions. On the KN US Equity Core, the traded-value rank is positive in
the pool inside the window and negative before it (`RESULTS.md` rows 6 to 9). Moving-average rules
are also the class
[Sullivan, Timmermann & White (1999)](../../Bibliotheca/Papers/Sullivan_Timmermann_White_1999_Data_Snooping_Technical_Trading_Rules.md)
deflate.

**It asserts nothing about being the best trend rule.** The owner skipped the seven questions
before any backtest, so the thesis carries none of his answers; they are listed under the open
questions.

<!-- example: end -->

### The claim this moves

Which claim of `OBJECTIVE.md`, by number, this experiment exists to move, the status it reaches if
the predictions below hold, and the one it reaches if they fail. **One claim.** An experiment that
could beat every benchmark and settle nothing is a measurement, not a test.

<!-- example: begin -->

**Claim 1, the signal**: that holding only members in a confirmed uptrend produces a better book
than the same rule without it. Its test is prediction 1; its status uses `OBJECTIVE.md`'s
vocabulary, fixed now:

| Prediction 1 (the control margins and the sub-periods) | Prediction 4 (both benchmarks) | Claim 1 becomes |
| --- | --- | --- |
| holds | holds | **confirmed as a book**, on the KN US Equity Core, 2015 to 2026 |
| holds | fails | the test passes and the status does not move: the vocabulary has no word for a better book that loses to its index, and the findings say it in a sentence |
| fails | either | **falsified** as written, on this universe and window |

**Claim 2, the sizing**, is tested by prediction 3: it becomes **confirmed as a book** if prediction
3 and prediction 4 hold, and **falsified** if prediction 3 fails. Claim 3 is true by construction
and is measured only through claim 1's control.

<!-- example: end -->

### Rules

- **Selection:** the eligibility condition, naming the column it reads.
- **Sizing:** the weighting scheme, and any bounds it sizes inside — a cap and a floor on each
  weight, and whether a capped name's excess goes to cash or to the other names. Named bounds are
  the design, and the control holds them too; every other constraint is switched off, a lever a
  later experiment has to earn.
- **Cash:** where the uninvested residual goes — a real, priced instrument, because the engine's
  weight file has no cash row.
- **Timing:** calendar, or event-driven on a stated trigger. Say what happens between triggers.
- **Lag:** how many days between the signal and the fill, and what the engine adds on top.
- **Control:** the same rule with exactly one ingredient removed — name which — trading on this
  rule's own rebalance dates, so that the ingredient is the only difference. A control left to find
  its own dates differs in when it trades as well.
- **Screens deliberately absent**, and why each is redundant under the rules above.

<!-- example: begin -->

- **Universe:** the KN US Equity Core's members as of each date, from the desk's daily holdings
  read by `Data/hand_supplied.py`, each index ticker renamed through the seed to the symbol FMP
  prices it under. A member FMP does not price is not in the universe; the share of the index's
  weight that costs is published per date in `Universe/Coverage.csv`.
- **Signal:** the golden cross as a state — 1 while the 50-day simple moving average of the
  dividend-and-split-adjusted close is above the 200-day, 0 otherwise; `r_trend_50_200` above zero.
  The 50/200 pair is the most widely known one and was never tuned.
- **Traded value:** `r_traded_value_sma_63d`, the 63-day simple average of the Curator's
  `c_daily_traded_value` — the day's unadjusted VWAP times its unadjusted volume, the dollars
  traded, falling back to split-adjusted figures only where the provider gave no unadjusted ones —
  so a dividend never scales it. 63 days is the Curator's own quarter, never tuned.
- **Eligible on day t:** a member at the close of t−1, with a 200-day history at t−1 (a value of
  `r_trend_50_200`), the cross at 1 at t−1, a traded value at t−1, and a fill price on t inside the
  span its symbol speaks for it.
- **Rank:** by traded value at the close of t−1, highest first.
- **Sizing, the bounds set the count:** each name's weight is its traded value over the sum of the
  held names' traded values, capped at **20%**, the excess spread over the uncapped names in
  proportion until no name is above the cap. Names are added in rank order while the smallest
  weight stays at or above **1%**; the book holds the last count that passed. No count is chosen.
- **Cash:** when fewer than five names are eligible the cap cannot place every dollar, and the rest
  is held in `BIL`. The engine also keeps a 1% cash reserve, as cash, to pay commission.
- **Timing:** the book is re-struck **only on the days its held set changes** — a name enters or
  leaves — and every weight is set back to its target that day. Between those days, weights drift
  with prices.
- **Lag:** signal, membership and rank at the close of t−1; the fill at t's dividend-adjusted VWAP.
  A security whose prices stop is sold by the engine at its last price: the one look-ahead
  `AGENTS.md` admits.
- **Excluded by name:** the blocking rows of `Universe/Data_Issues.csv` — `MNKKQ`, `NE` and `PCP`,
  whose priced history inside their span is shorter than the cross's 200 days, and `RAI`, whose
  adjusted price is zero or negative and moves more than sixfold in a day.
- **Costs:** the engine's `commission_cents` of **0.05**, measured on 2026-10-06 at $0.041 a share
  on SPY and $0.035 on KO bought once, and **5 basis points** of slippage — 0.14.0's cost model,
  unchanged — **$1,000,000** of starting capital, integer shares: the cost row every verdict is read
  at. A row at the realistic setting of **0.006**, measured the same day at $0.0049 a share on SPY
  and $0.0042 on KO, is reported beside it.
- **Window:** 2015-01-02 to 2026-06-01, the start fixed by the owner's coverage rule in
  `Universe/universe.ipynb` before any rule existed. Everything from 2026-06-02 is unseen until a
  book is frozen.
- **Control:** the same rule with the golden cross removed — the members with a 200-day history,
  ranked and weighted by traded value inside the same bounds — **trading only on the rule's own
  rebalance dates**. The history requirement is kept, so the cross's sign is the one difference.
- **Screens deliberately absent:** no sector limit, no risk model, no stop-loss, no valuation
  screen, no minimum history beyond the cross's 200 days. Each is a lever a later experiment has to
  earn, and the cross itself is the value-trap screen of claim 3.

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

**Predictions, fixed before the run.** Every source is a `Bibliotheca/` note or a row of
`RESULTS.md`, *Before any experiment*, which records `Data/analyzer.ipynb` by section; the pool
there is the fifty most traded members, the expected sign positive, and consecutive windows share
20, 62 and 251 days at the three horizons. **Three rows are predictions and five are leads**, each
lead counted as one: a lead is reported, not scored, and says what would license it.

| # | Prediction | Where it comes from | What would falsify it |
| --- | --- | --- | --- |
| 1 | **The golden cross earns its keep**: the book beats its control by at least +0.03 Sharpe and +0.5 points of CAGR over the window, and beats it — any margin — on both Sharpe and CAGR in at least 2 of the 3 sub-periods | analyzer section 4: the cross as a state on the pool, in the window, +0.0235, +0.0275 and +0.0161 over 21, 63 and 252 days, positive on 54.6%, 58.0% and 52.9% of dates (rows 2 to 4). A sign, not a size: no note predicts the CAGR limb | either margin missed over the window, or the control beaten on both measures in fewer than 2 sub-periods |
| 2 | **The cross is a drawdown control**: the book's maximum drawdown is shallower than its control's, and its volatility lower | analyzer section 5: forward 21-day volatility 28.8% with the cross on against 32.4% off, on the pool (row 11); [Faber (2007)](../../Bibliotheca/Papers/Faber_2007_Quantitative_Approach_To_Tactical_Asset_Allocation.md). Against it: [Han, Zhou & Zhu (2016)](../../Bibliotheca/Papers/Han_Zhou_Zhu_2016_Taming_Momentum_Crashes.md), on the cross as the slowest possible stop | the book's maximum drawdown deeper than the control's, or its volatility higher |
| 3 | **Weighting by traded value beats equal weight** on the same selection, on Sharpe | analyzer section 4: the traded-value rank on the pool, in the window, +0.0327, +0.0526 and +0.0977 over 21, 63 and 252 days, positive on 56.8%, 62.0% and 73.6% of dates (rows 6 to 8) — return coefficients, not risk-adjusted ones. Against it: [Ibbotson, Chen, Kim & Hu (2013)](../../Bibliotheca/Papers/Ibbotson_Chen_Kim_Hu_2013_Liquidity_As_An_Investment_Style.md), and row 9 before the window | the equal-weight arm's Sharpe at or above the book's |
| 4 | **Lead**: the book beats both benchmarks on Sharpe, net, over the window | no analyzer row measures a book's return or Sharpe against an index; it is half of success criterion 1 and is evaluated there | counted as a lead |
| 5 | **Lead**: the rule's selection — the cross and the ranking together — beats chance, the book's idiosyncratic return above at least 16 of the 20 random books' | the random books draw from every member with a fill (row 9's population, +0.0250 over a year in the window), so they differ from the book in the cross and the ranking at once; no row measures the two together | counted as a lead; it is part of gate criterion 2 |
| 6 | **Lead**: the bounds hold a few dozen names, and the 20% cap binds on few rebalance dates | rows 12 and 13 measure shares of all cross members' traded value, not of the held names' the rule normalises over; how many names the bounds hold and how often the cap binds are not measured before the run | counted as a lead; both are reported in section 3 of `experiment_1.ipynb` |
| 7 | **Lead**: the book re-strikes often, and the realistic commission row changes its CAGR little | [Novy-Marx & Velikov (2016)](../../Bibliotheca/Papers/NovyMarx_Velikov_2016_A_Taxonomy_Of_Anomalies_And_Their_Trading_Costs.md) says costs bite on high-turnover rules, and the engine's charges are measured (`JOURNAL_1.md`, 2026-10-06); this book's turnover is not | counted as a lead |
| 8 | **Lead**: most of the excess return is factor exposure — market and beta — rather than idiosyncratic, with momentum small, the factor model being close to blind to an absolute trend rule | read [Paleologo (2021)](../../Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/INDEX.md) on factors before predicting it | counted as a lead |

**Watched, not predicted:** the sign of every measurement before the window (`RESULTS.md` rows 2 to
9 are flat or negative there), and the survivorship cost — the 7% of the index FMP does not price
early in the window, concentrated in large dead companies — on the book's early years.

<!-- example: end -->

### Success criteria

What the experiment has to show to count as a success, fixed now. At the least:

1. It beats the benchmark `JOURNAL_1.md` chose **and its own control** on risk-adjusted
   return, net, over the same window — criterion 1 of the gate in `Paper_Trading/BITACORA.md`.
2. Reproducible from a clean clone, through the pipeline, with no manual step.
3. A tradeable trigger frequency — not a rule that fires every day.
4. Every prediction above evaluated explicitly in `FINDINGS_1.md`, **including the ones that turn
   out wrong.**

<!-- example: begin -->

1. It beats the KN US Equity Core and SPY on Sharpe, net, over the window, **and its own control**
   as prediction 1 states: by at least **+0.03 Sharpe and +0.5 points of CAGR** over the window, and
   on both measures in at least **2 of 3** sub-periods — the window's start to 2018-12-31, 2019 to
   2022, 2023 to 2026-06-01. The margins were set by the owner knowing that 0.14.0 beat its control
   by 1.2 points a year on another universe.
2. Reproducible from a wiped working copy, through the pipeline, with no manual step beyond the one
   `SETUP.md` names: dropping the desk's index and factor files in, unrenamed. This run is that run.
   A clone on another machine is the stronger test, and is what 1.0.0 waits for.
3. A tradeable trigger frequency, the template's "not a rule that fires every day": the book does
   not re-strike on more than four trading days in five over the window.
4. Every prediction and lead above reported explicitly in `FINDINGS_1.md`, **including the ones that
   turn out wrong.**

<!-- example: end -->

**Success is necessary for graduation, not sufficient.** The gate's five criteria in
`Paper_Trading/BITACORA.md` decide it, and a person signs it.

<!-- example: begin -->

Fixed now, as the owner approved them:

| # | Criterion | Passes when |
| --- | --- | --- |
| 1 | Beats the benchmarks and its control | success criterion 1 |
| 2 | Idiosyncratic alpha in both layers | Brinson-Fachler selection above zero (per asset, as the library computes it), the factor model's idiosyncratic return above zero, the third pass's selection above zero, and the book's idiosyncratic return above at least 16 of the 20 random books. **Precondition:** the first cut's benchmark return within 1.0 point a year of the engine's KN US Equity Core return — the tolerance the owner approved, wide enough for the members FMP does not price; if not, the two Brinson-Fachler rows read "not evidenced" |
| 3 | Survives perturbation | at least 6 of the 8 settings below keep the sign of the margin over their own control on both Sharpe and CAGR, and all 8 beat the KN US Equity Core on Sharpe |
| 4 | Costs and capacity stated | turnover; the frozen and the realistic commission rows; capacity as a participation bound — for the worst trade, the 1st percentile and the median, the largest book at which a trade stays within 1% and within 5% of the name's 63-day traded value. A bound, not an impact model |
| 5 | Sign-off | the owner's name and date in `BITACORA.md`, after 1 to 4 are evidenced |

**The sweep, one setting at a time, each priced with its own control on its own rule's dates:** cap
at 15% and at 25%; floor at 0.5% and at 2%; traded-value window of 21 and of 126 days
(`r_traded_value_sma_21d`, `r_traded_value_sma_126d`); the cross as 20/100 and as 100/300
(`r_trend_20_100`, `r_trend_100_300`), each with its own history requirement in the rule and its
control. How often the cap binds is not measured before the run; the findings report it beside the
two cap settings.

**The counterfactuals:** the rule's own selection equally weighted, on its own dates — the sizing
arm; twenty random books, each drawing on every rebalance date of the rule as many names as the rule
holds from the members with a fill that day, sized by traded value under the 20% cap with no floor
walk, replacing as many names as entered the rule's book that day — the selection baseline, for
the cross and the ranking together. **The shifted-entry timing arm is not run.**

**The trial count: 76 books**, and one choice that is not a book.

| Version | Books | Which |
| --- | ---: | --- |
| 0.13.0 | 23 | Experiment 1; Experiment 2's twelve and one excluded; Experiment 3's eight and one excluded, as `RESULTS.md` at tag `0.13.0` counts them |
| 0.14.0 | 14 | the nine reported, and the five random books of the third attempt, redrawn whole on every rebalance date and discarded as wrong by construction (`JOURNAL_1.md`, 2026-09-23) |
| 0.15.0 | 39 | the rule, its control, the sixteen of the sweep, the equal-weight arm and the twenty random books |

The cost rows and the sub-period windows re-price these books and add none; the commission
calibration and the test of the parallel workers priced one-stock books that are not the rule.
**The window is the choice**: a forking path, taken after 0.14.0's result was seen, listed here and
in `RESULTS.md`. The deflated Sharpe is not computed, and the sign-off says so.

<!-- example: end -->

### What would falsify it

**One condition for the whole experiment, fixed now.** Each prediction above has its own falsifier;
this is the result under which the experiment as a whole has failed — usually a margin against its
control, or a result that holds in one sub-period and not in the others. Then **the
changes that may not rescue it**: every setting that could be moved once the result is in — a
holding count, a trigger, a window, a threshold — by name. Moving one after the result is a new
experiment, and one more trial in the count.

<!-- example: begin -->

**The golden cross adds nothing on this universe** if prediction 1 fails: the book misses the
+0.03 Sharpe or the +0.5 points of CAGR over its control over the window, or beats the control on
both measures in fewer than 2 of the 3 sub-periods. This is the experiment's falsifier and reads the
backtest window; the paper book's own kill switch, which reads its days on paper, is registered in
`BITACORA.md` with the sign-off. **Proposed to the owner as the kill switch, for him to confirm,
change or refuse:** the same condition, failing on **either** cost row.

**The changes that may not rescue it:** the window and its sub-period boundaries; the 20% cap, the
1% floor and the five-name `BIL` rule; the 63-day traded-value window; the 50/200 pair; the trigger,
re-striking on a change of the held set; the 1% cash reserve; the 90% coverage rule that set the
start; the exclusions; the cost row. Moving any of them after the result is a new experiment, and
one more trial in the count.

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

- **Survivorship.** FMP prices only part of the index early in the window: the coverage rule opened
  it on 2015-01-02 at 92.97% of the index's weight, and the members missing are disproportionately
  the large dead companies a traded-value rule would have held. Lie 1, accepted by the owner,
  quantified, not removed.
- **Concentration.** Traded value concentrates in a few names: on the cross members, 10 to 18 names
  hold at least 1% of their traded value in a typical year, and the largest single share rose from
  4.1% in 2017 to 15.7% in 2024 (`RESULTS.md` rows 12 and 13). The 20% cap is what bounds the
  largest weight; effective N is measured in section 3 of `experiment_1.ipynb`.
- **The pool is narrower than the book.** The analyzer's pool is the fifty most traded members; the
  book's marginal names may fall outside what rows 2 to 8 describe.
- **The signal's known weakness**: a moving-average cross exits late — the slowest possible stop, in
  [Han, Zhou & Zhu (2016)](../../Bibliotheca/Papers/Han_Zhou_Zhu_2016_Taming_Momentum_Crashes.md)'s
  terms — and whipsaws where prices mean-revert, as
  [Kaminski & Lo (2014)](../../Bibliotheca/Papers/Kaminski_Lo_2014_When_Do_Stop_Loss_Rules_Stop_Losses.md)
  set out. The rule accepts both on simplicity grounds.
- **The sizing may be a constraint dressed as a signal.** Weighting by traded value carries no
  information about expected return unless the attention argument holds, and the notes argue it
  does not.
- **The signal may not be what earns the return.** A book of the most traded names is a large-cap,
  high-beta book by construction; attribution and the control are what separate the cross from
  that tilt.
- **The index's two files disagree.** The returns file predates the current holdings, so the first
  cut's benchmark may not reconcile with the engine's index return; criterion 2 states the
  tolerance before the run.
- **The window and the margins were set knowing earlier results.** The owner chose the window after
  seeing 0.14.0's 2017–2026 result and hearing of the worked example's falsification on 2002–2016,
  and the margins knowing 0.14.0's 1.2 points over its control. Both are disclosed, and counted.

<!-- example: end -->

### Open questions this experiment deliberately does not answer

Each is a later experiment, and each has to beat this one.

| # | Question | Why it is not answered here |
| --- | --- | --- |
| 1 | the question | why this experiment leaves it open |

<!-- example: begin -->

| # | Question | Why it is not answered here |
| --- | --- | --- |
| 1 | The seven questions before any backtest — why the edge exists; who is on the other side, and why they keep losing; risk premium or mispricing; how many independent bets a year; whether it survives costs, and how much capital it takes; when it fails, and whether the owner would hold it through that; how many ideas came before this one | the owner skipped them on 2026-10-05; none is answered for him |
| 2 | Does the rule hold before the window, 2002 to 2014? | the window is the owner's; the analyzer's reading before it is context, not a test |
| 3 | Would a member FMP does not price change the verdict? | a second provider is a different universe, and a later experiment |
| 4 | A hysteresis band, a different cap, a sector limit | each is a lever a later experiment has to earn against this one |
| 5 | Capacity beyond a participation bound | market impact is not modelled anywhere in this repository |

<!-- example: end -->
