# Objective

> **Step 1 of 8, with `Bibliotheca/`.** One idea, one objective, and the claims inside it with
> their status. The first thing a CIO reads and the last thing that changes: a change here means a
> *different* strategy, not a better version of this one.
>
> **Write it before any paper is read, and before anything is measured.** The claims table is a set
> of predictions; a claim written after the reading, or added after a result, is an observation
> wearing a hypothesis's clothes.
>
> Everything in italics below is guidance: replace it, keep the plain text, then delete this
> blockquote.

<!-- example: begin -->

> **This file is the worked example — `liquid-golden-cross`.** One strategy filled in, kept as the
> worked example so the shape can be read rather than imagined. **Drafted 2026-09-19 from the idea
> as it was first put, before any paper was read, any data downloaded or any rule coded, and
> fine-tuned the same day for claim 1 once its notes existed.** Claims 2 to 4 were fine-tuned on
> 2026-09-22, once their notes existed, the same way: their evidence rewritten from the notes,
> their wording untouched.
> **The status column was updated on 2026-09-20, once `FINDINGS_1.md` reported; no claim's wording
> changed, and the diff shows it** — a claim edited after its test is not a claim. A strategy of
> your own starts from `init-strategy`, never from here.
> **Claim 5 was added on 2026-09-24**, in the owner's words, for Experiment 3: a row in the claims
> table and a section of its own below. He chose it before the analyzer measured it; it was
> written after, once its notes had been read and step 6 had charged Experiment 1's books with
> momentum, as its section says. The main idea, claims 1 to 4 and every other line are unchanged,
> and the diff shows it. Its status moved on 2026-09-24, once `FINDINGS_3.md` reported; its
> wording did not.

## The main idea

**Own the 30 most traded US stocks whose 50-day average price is above their 200-day average,
equally weighted, and rebalance only when the book has moved 10% away from that list.**

The signal is a trend filter: a stock is eligible while its 50-day simple moving average is above
its 200-day one. The ranking is trading volume: of the eligible stocks, the 30 with the highest
average daily traded value are held. The sizing is equal weight, a thirtieth each, and a slot with
no eligible stock stays in cash. The book is rebalanced only when trading to the new top 30 would
turn over at least 10% of it. **None of it is clever, and that is deliberate** — each part can be
explained in a sentence, which is what lets step 6 say afterwards which of them earned the return.

## The objective

A rule the desk can run with real money in stocks it can always trade: it owns the most traded US
stocks while their trend is up, lets go of them when it turns, and trades no more than it has to.
The deliverable is not a Sharpe; it is a rule simple enough that when it works we can say *why*,
and when it fails we can say *which part* failed — the trend filter, the ranking, the sizing or the
band.

**The design constraint every experiment respects: radical simplicity.** Complexity is added one
lever at a time, and each addition must beat the simpler baseline to earn its place. This strategy
has four moving parts, no optimiser and no fitted model.

## The claims inside that sentence

They are tested separately and **their status is not the same.** This table is the only place a
reader sees which parts of the idea have survived contact with the data, so keep it honest.

| | Claim | Status |
| --- | --- | --- |
| **1. The signal** | among the most traded US stocks, those whose 50-day average is above their 200-day go on to earn more than those whose is not | **falsified, on two windows** — they earn less, with less volatility. On 2017 to 2026: in the first design, at tag `v0.15.0` of the KaxaNuk Researcher, the filtered book earns **1.12 points a year less** than the same names unfiltered on the same dates, and the filter accounts for about 5 of its 45.5 idiosyncratic points; the second design, which sells a broken cross the next day, earns 0.86 points a year less than its control and trips its kill switch, with exit speed ruled out as the reason ([`FINDINGS_1.md`](Experiments/Experiment_1/FINDINGS_1.md)). On 2002 to 2016, Experiment 2's book, the first design's band at twenty names, earns **1.64 points a year less** than its control, ahead of it on both Sharpe and CAGR in none of three sub-periods, and the cross's share of its idiosyncratic return over 2008 to 2016 is −38.17 points; on 2017 to 2026 the same rule trails its own control too, by 1.46 points a year ([`FINDINGS_2.md`](Experiments/Experiment_2/FINDINGS_2.md)) |
| **2. The sizing** | equal weight across the 30 captures that without a risk model | **untested** — the book is equal weighted and works, but no other weighting has been run against it |
| **3. The construction** | ranking by trading volume keeps every position in a stock that trades heavily enough to be exited in a day | **true by construction**, and **measured as the book's largest idiosyncratic source** in the first design, at tag `v0.15.0`: about 28 of its 45.5 points, against random books of the same shape. It was expected to cost return and it did not. The second design's findings do not break its 36.19 points down this way |
| **4. The rebalancing** | trading only when the book is 10% away from its target keeps most of the return at a fraction of the turnover | **measured** — in the first design the band fired 87 times in 9.4 years at 17.8% turnover each; in the second, at twenty names, a 15% band earned 1.65 points a year more, net, than selling each broken name the next day ([`FINDINGS_1.md`](Experiments/Experiment_1/FINDINGS_1.md)). The claim names a 10% band, and this evidence is at 15%, the setting that keeps the first design's behaviour at twenty names. *Measured* is the status `BLUEPRINT_1.md` fixed for that arm, reached on an engine-priced book rather than on the analyzer the vocabulary below names |
| **5. Momentum** | *"the 20 most-traded members ranked by their own 12-month return, the momentum proper"*, the owner's words of 2026-09-24, read, with the latest month left out as in the standard definition (Baltussen et al., p. 5), as: among the most traded US stocks, those with the highest return over the twelve months before the latest one go on to earn more than the most traded chosen without that ranking | **falsified, for Experiment 3's design, on 2002 to 2026** — added 2026-09-24, beside the main idea rather than inside it, and chosen before the analyzer measured it. Among the hundred most traded securities, its information coefficient at 21 days is 0.0134 on 2002 to 2016 and 0.0304 on 2017 to 2026, and on 2002 to 2016 it is below zero at 63 and 252 days ([`RESULTS.md`](RESULTS.md), rows 19 to 28). As a book, the twenty of the hundred most traded members with the highest return, re-struck monthly, earns **0.22 points a year less** than the pool's twenty most traded on the same dates over 2002-07-30 to 2026-06-01, net, and is ahead of them on both Sharpe and CAGR in one sub-period of three, 2017 to 2026; step 6 finds the ranking adds 28.01 points of the momentum factor and takes 5.59 idiosyncratic points away ([`FINDINGS_3.md`](Experiments/Experiment_3/FINDINGS_3.md)) |

Status vocabulary, so it means the same across strategies: **untested** · **measured** (the analyzer
says something; no book has been run) · **falsified** · **confirmed as a book** (it beats its
benchmarks through the engine) · **confirmed as a factor** (attribution assigns it the return) ·
**unexplained** (confirmed as a book, not as a factor — the usual state, and the interesting one) ·
**true by construction**.

### 1. The signal — the 50-day average above the 200-day

**The evidence read for it argues against it.** [Sullivan, Timmermann & White
(1999)](Bibliotheca/Papers/Sullivan_Timmermann_White_1999_Data_Snooping.md)
test 7,846 rules on the Dow with a bootstrap that judges the best rule against the whole universe it
came from: moving-average rules clear that bar over 1897–1986, and the best of them over 1987–1996 —
a 200-day average, one leg of ours — comes back at a p-value of 0.154 against a nominal 0.055.
[LeBaron (1999)](Bibliotheca/Papers/LeBaron_1999_The_Stability_Of_Moving_Average_Rules.md), one of
the authors of the 1992 study this idea inherits, finds the same reversal in his own data: a
buy-sell difference of 0.066% a day over 1897–1986 and −0.048% over 1988–1999, and a long-only
version that went from a Sharpe of 0.462 against buy-and-hold's 0.123 to −0.518 against 0.776.
[Paleologo (2021), chapter
5](Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/09_Understand_Factors.md) supplies
the definition the claim needs: momentum is relative and trend following absolute, so the momentum
literature is context here rather than evidence.

**The support is the one source that cannot be read.** Brock, Lakonishok & LeBaron (1992) is the
study both of the others examine. Both copies found of it are image scans with no text layer, so it
stays a lead and nothing is claimed on it.

**What the reading adds, none of it measured here.** The volatility difference between buy and sell
periods survived the decade in which the return difference did not, so a result on this book is
incomplete without its volatility beside its return. A long-only book may fare better than the rules
these papers test, whose long trades earned more than twice their short ones — a prediction for
`BLUEPRINT_1.md`, not an assumption. And one day of implementation lag took the best rule in one of
these studies from 17.2% to 7.8% a year, so the number the blueprint predicts is the lagged one.

**What would settle it.** Inside the most traded stocks, do the ones in an uptrend earn more over
the following months than the ones that are not? First in `Data/analyzer.ipynb`, on the lagged
signal, as the forward returns of the two groups, before any book; then as a book, against the same
30 most traded stocks with the filter switched off. Neither paper answers it: both test one index
against cash, never a cross-section of stocks, and neither reports a 50-day average crossing a
200-day one.

### 2. The sizing — equal weight

**The evidence read for it says what the claim is, and why it has no number yet.** [Paleologo (2021),
chapter 6](Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/10_Alpha_Sizing.md)
lists equal weight among its sizing rules as the 1/N rule — proportional sizing with every
conviction equal — and this rule has no conviction: the trend state is a yes or a no, and the
ranking is a cut. So the claim is not that equal weight beats sizing on a signal; it is that the one
thing the rule could size on, each stock's volatility, would not pay. In the author's own experiment
the proportional rule beat risk parity by about a tenth and mean-variance by a third on identical
signals, and the mechanism was forecast error meeting a wide spread of volatilities — a spread the
thirty most traded names compress, so the edge claim 2 defends is smaller here than there.
[Chapter 8](Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/12_Your_Performance.md)
says why no run so far measures it: the cross-sectionally equalised book *is* this book, so its
sizing term is zero by construction, and the counterfactuals of `FINDINGS_1.md` measured selection
and the filter, never sizing. [Grinold & Kahn, chapter
14](Bibliotheca/Books/Grinold_Kahn_ND_Active_Portfolio_Management/17_Portfolio_Construction.md)
gives the trade-off in its own terms: an equal-weighted screen is robust to a wild input and blind
to risk, and in Muller's test it earned the lowest average information ratio of four methods and the
steadiest.

**What would settle it.** A sizing experiment that prices the second row of Paleologo's table, a
thirtieth divided by volatility, beside this book, with plain mean-variance as the control that
should lose — judged on step 6's idiosyncratic return rather than on a Sharpe gap, because the gap
between this book and its equalised control is 0.03 and the confidence band on a nine-year Sharpe is
far wider than that. Its predictions are fixed in the chapter 6 note: risk parity within a few
percent of equal weight, mean-variance below both.

**Worth reading for it — a lead, no note yet.** DeMiguel, Garlappi & Uppal (2009), already a lead in
Part 3, on how hard equal weighting is to beat out of sample.

### 3. The construction — the volume ranking

**This claim is true by construction, and was expected to cost return rather than add it.** Ranking
by trading volume is what makes every position one the desk can get in and out of. It also makes
this a book of the largest companies, since trading volume follows company size, and the first pass
expected step 6 to see that as a size exposure, not as skill.

**The evidence read for it says what a book of the largest companies loads on, and it is not
size.** [Sarkar, Du & Vafai
(2019)](Bibliotheca/Papers/Sarkar_Du_Vafai_2019_Impacts_Of_Sector_And_Company_Size.md) regress a
354-name large-company portfolio on the French factors, the rate terms and seventeen sectors over
1990–2016: without the sectors, beta, size, value and momentum are all significant; with them, beta,
size and value lose significance, and what remains is momentum, the risk-free rate, the yield curve
and six sectors. Step 6 found size at 4.11 of 159.5 points and momentum at 12.75, which is the
paper's reading — with the caution that its large-cap momentum coefficient is negative in every
table and its text never says so, so it is no evidence that the 12.75 points are a premium. What the
paper adds to open lead 3 of `RESULTS.md` is weight: the block that read zero in step 6 is the block
the paper says explains most of a large-cap book's beta, so the 28 idiosyncratic points assigned to
the ranking are provisional until a sector block or a rate term is in the model.
[Paleologo (2021), chapter
8](Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/12_Your_Performance.md)
and [Grinold & Kahn, chapter
16](Bibliotheca/Books/Grinold_Kahn_ND_Active_Portfolio_Management/19_Transactions_Costs.md)
say what the ranking is for in the other claims' measurements: the counterfactuals assume every
position can be built in a day, and market impact grows with the square root of a trade's share of
daily volume, so the thirty most traded names are where both assumptions come closest to true.

**What is still open — a lead.** How much return the ranking gives up, and whether the trend filter
works as well among the most traded stocks as among the rest. A later experiment varies the cut and
reads it as a curve; the paper's liquidity variable is a market-wide factor, not a stock's own
volume, so it does not answer this.

**Worth reading for it — leads, no note yet.** **Against it:** Amihud (2002), *Illiquidity and Stock
Returns: Cross-Section and Time-Series Effects*, on less traded stocks earning more; and Lee &
Swaminathan (2000), *Price Momentum and Trading Volume*, on heavily traded stocks earning less and
their past winners reversing sooner — the closest source to this pairing of volume and trend. **For
it, on costs:** Korajczyk & Sadka (2004), *Are Momentum Profits Robust to Trading Costs?*, on
liquidity-aware construction holding up after costs.

### 4. The rebalancing — the 10% band

**The evidence read for it is the claim's own source, and it came with conditions the sentence
dropped.** Claim 4 is the rule of thumb of [Grinold & Kahn, chapter
16](Bibliotheca/Books/Grinold_Kahn_ND_Active_Portfolio_Management/19_Transactions_Costs.md)
— at least three-quarters of the value added for half the turnover — and the chapter attaches three
conditions: the bound is for prorating every trade toward an optimum, where this rule trades to the
full target or not at all; it is guaranteed under equality constraints only, and a long-only book at
a thirtieth each is the inequality case, where the authors keep 75 percent as experience rather than
proof; and it is a bound on incremental value added over a frontier, so the band has to be read as
that frontier. The band itself comes from [chapter
14](Bibliotheca/Books/Grinold_Kahn_ND_Active_Portfolio_Management/17_Portfolio_Construction.md),
where it sits on each stock's alpha and is as wide as its two costs, and where Leland's halving of
turnover "with effectively no change in risk" comes from trading to the boundary, not to the target
— two things the transplant changed. **Against it,** [chapter
13](Bibliotheca/Books/Grinold_Kahn_ND_Active_Portfolio_Management/16_The_Information_Horizon.md): a
band is a delay, a delay loses value at the half-life of the signal's forecasting power, and that
half-life has never been measured here; the analyzer's coefficients at 21, 63 and 252 days are the
raw material, on overlapping windows the chapter says overstate the evidence. The first datum is
already in `FINDINGS_1.md`, and it points the wrong way for the claim: the same names traded on the
rule's 87 dates earned more, net, than traded on 11.

**What would settle it.** Does trading only when the book is 10% away from its target keep most of
the return at a fraction of the turnover, net of costs? The engine answers it directly: the same rule
with no band, trading to the target on every check, against the band at 10%; then a sweep of the
band — 0%, 5%, 10%, 20%, 30% — read as the chapter's frontier of value added against turnover, with
an arm that trades to the edge of the band rather than to the target, the slope at 10% read as the
round-trip cost the band implies, and the delay test — the frozen book implemented one, five and
twenty-one days late — run before any band is chosen. A new experiment, not an edit to this one.

**Worth reading for it — a lead, no note yet.** Novy-Marx & Velikov (2016), already a lead in
Parts 4 and 5, on which cost-saving rules keep an anomaly's return after costs.

### 5. Momentum — the twelve-month return, the latest month left out

**Added on 2026-09-24, in the owner's words, and chosen before the analyzer measured it** — not
before step 6 had measured the momentum of Experiment 1's books, as the next paragraph says. After
Experiment 1's two designs and Experiment 2 had failed their kill switches, he chose, from the
options put to him: *"Experiment 3, then paper (Recommended) — A new idea on the same liquid names:
the 20 most-traded members ranked by their own 12-month return, the momentum proper. Blueprint and
critic first, then tested on 2002–2016 and 2017–2026. If it passes the gate and you sign, it's
frozen as Paper_Trading_1 and tracked daily."* A paper book takes its experiment's number, so it
would be `Paper_Trading_3`. The analyzer measured the signal after that choice, and this claim was
written after it ran. **It needs a claim of its own** because the main idea is the cross, and this
file says momentum is relative and trend following absolute, so the momentum literature is context
for claim 1 rather than evidence: a momentum book cannot move claim 1, and the literature that is
only context there is this claim's evidence. The main idea's sentence is not reworded, and this
claim is not inside it: it sits beside it, on the same liquid names. The line *not that this is
momentum*, under *What is not claimed*, is about the cross and stands.
[`BRAINSTORMING_3.md`](Experiments/Experiment_3/BRAINSTORMING_3.md) has what else was considered, a
new name and a new strategy among them.

**It was not chosen blind.** Step 6 had already charged Experiment 1's books with momentum on 2017
to 2026 — 12.75 points in the first design, 15.44 in the second's rule against its control's 5.99
— and the note on [Baltussen, Dom, Van Vliet & Vidojevic
(2025)](Bibliotheca/Papers/Baltussen_Dom_VanVliet_Vidojevic_2025_Momentum_Factor_Investing.md)
reads those years as momentum's strongest since its 2009 crash (p. 8). So the claim was written
after results, step 6's and the analyzer's, though before any book of its own: the book that tests
it runs on years whose momentum has been seen, and the published record is its out-of-sample
evidence.

**The evidence read for it.** Baltussen et al. give the standard definition, the past twelve months
less the latest one, held for a month (p. 5), and find it paying after its publication: 7.89
percent a year value-weighted in the United States over 1990–2024, t 2.07 (p. 8), positive in all
31 countries with data since 1990 (p. 10), and in 61 years before CRSP that nobody had tuned it to
(pp. 10–11). [Paleologo (2021), chapter
5](Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/09_Understand_Factors.md) gives
the term structure the skipped month rests on: the latest month reverts, one month to a year
continues (pp. 74–75). **Against it, in the same sources:** the paper's figures are long-short
spreads, its headline ones gross of costs (p. 11), and it does not study transaction costs
(pp. 26–27), whereas a book of the most traded names holds a long leg alone, net, and sits nearer
the paper's value-weighted column, the weaker, 7.89 percent against 10.00 equally weighted (p. 8);
and the premium crashes at market reversals, 1929 and 2009 in its series (p. 8), when the previous
year's losers rally (Paleologo, p. 77), and Paleologo names another crash in early 2016 (p. 77).
**Nor does the one note on momentum among the largest companies support it:**
[Sarkar, Du & Vafai (2019)](Bibliotheca/Papers/Sarkar_Du_Vafai_2019_Impacts_Of_Sector_And_Company_Size.md)
find a large-company portfolio's momentum coefficient negative in every specification they print
(pp. 29, 30, 33 and 36), which ties such a book's return to the factor and is no evidence that it
earns the premium.

**What the analyzer measured, after the choice.** On the seed Experiment 2 widened, among the
hundred most traded securities on each date ([`RESULTS.md`](RESULTS.md), rows 19 to 30): at 21
days, a coefficient of 0.0134 on 2002 to 2016, positive on 54.7% of 3,633 dates, and 0.0304 on 2017
to 2026, on 56.1% of 2,344 — the first below the 0.02 to 0.03 `RESULTS.md` reads as a working
signal's, the second at its top. On 2002 to 2016 it is below zero at 63 and 252 days, −0.0018 and
−0.0025; on 2017 to 2026 it holds, 0.0234 and 0.0309. On the first trading day of each month, the
twenty with the highest return beat the hundred's mean over the next 21 days by 0.14% on 2002 to
2016, median 0.34%, in 56.6% of 173 months, and by 0.83% on 2017 to 2026, median 0.55%, in 55.4%
of 112 — with no lag, no costs, and against the pool rather than against its twenty most traded.
The pool ranks every security present, index member or not, so it is a neighbour of the pool a
rule selects from, not the same one.

**What would settle it.** Among the hundred most traded members of the index, does a book of the
twenty with the highest twelve-month return, the latest month left out, earn more, net of costs,
than the twenty most traded of the same hundred on the same dates? That is Experiment 3,
[`BLUEPRINT_3.md`](Experiments/Experiment_3/BLUEPRINT_3.md), with its margins and its kill switch
fixed before the rule. It ran on 2026-09-24, and the claims table above has what it found.

**Worth reading for it — leads, no note yet.** **Against it:** Lee & Swaminathan (2000), already a
lead under claim 3, on heavily traded stocks' past winners reversing sooner — this claim's own
names. **For it, on costs:** Korajczyk & Sadka (2004), also there, on momentum profits after
trading costs; and Novy-Marx & Velikov (2016).

## What is not claimed

- **Not that the parameters are right, and not that they are untouched by search.** The 50 and 200
  days are the pair the idea was stated with; 30 names, the 10% band and the quarter-long volume
  window are round numbers. None was searched on our data — but [Sullivan, Timmermann & White
  (1999)](Bibliotheca/Papers/Sullivan_Timmermann_White_1999_Data_Snooping.md)
  show the search that matters was run by the investment community over a century, which kept the
  windows that worked, and that the 50-, 150- and 200-day averages are precisely the ones it kept.
  The trial count behind this pair does not start at one. Each parameter is still a curve a later
  experiment sweeps and publishes, and this line is a disclosure rather than a defence.
- **Not that the 50/200 form is special.** [LeBaron
  (1999)](Bibliotheca/Papers/LeBaron_1999_The_Stability_Of_Moving_Average_Rules.md) gets the same
  means and variances from the sign of a single 150-day return, so the crossover is a convention
  rather than a mechanism, and that signed return is the cheapest control arm for a later
  experiment.
- **Not that this is out of sample.** Nothing is, until an experiment reaches step 7.
- **Not that this is momentum.** The filter compares a stock with its own past, not with other
  stocks: that is trend following, which is absolute, where momentum is relative ([Paleologo 2021,
  chapter
  5](Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/09_Understand_Factors.md)). The
  momentum
  literature is not this claim's evidence, and step 6 may assign the book little of its return even
  if the filter works, because a factor model built on relative factors is close to blind to an
  absolute rule — [`AGENTS.md`](AGENTS.md), *What attribution must report*. If that happens, it is a
  finding. [Baltussen, Dom, Van Vliet & Vidojevic
  (2025)](Bibliotheca/Papers/Baltussen_Dom_VanVliet_Vidojevic_2025_Momentum_Factor_Investing.md)
  is the momentum evidence read as context: a relative rank throughout, with no test of a stock
  against its own averages, so the +12.75 momentum points step 6 reported measure how much the book
  resembled a winners-minus-losers portfolio in momentum's strongest years since 2009 — a factor
  exposure, not the filter in another name.
- **Not that the ranking adds return.** See claim 3. If the book beats its benchmark, the ranking is
  not where the outperformance came from, and `FINDINGS_1.md` has to say so.
- **Not that the book times the market.** When fewer than 30 stocks are in an uptrend the empty
  slots stay in cash, so in a broad fall the book is partly out of the market. That follows from the
  filter; it is not claimed as skill, and step 6's time-equalised book measures what it earned or
  cost.
- **Not that the filter protects in every fall.** A 200-day average turns late: the filter can hold
  a stock well into a decline and sit out the start of a rebound. Whether the fall it avoids is worth
  the rebound it misses is a prediction for `BLUEPRINT_1.md`, not an assumption. [LeBaron
  (1999)](Bibliotheca/Papers/LeBaron_1999_The_Stability_Of_Moving_Average_Rules.md) is the caution:
  his rule was in its buy state 81% of the time in its last decade and still lost to holding the
  index. Lead: Shu, Yu & Mulvey (2024), *Downside Risk Reduction Using Regime-Switching Signals*, on
  one slow index-or-cash rule that avoided 2020's fall and gave up its rebound.
- **Not that an uptrend forecasts anything for one stock.** Each claim is about the average of the
  selected set.

## Where each half is named

Slots: nothing is computed yet, and the names are proposals the data step confirms.

| Half | The column | The stage that owns it |
| --- | --- | --- |
| the signal | `r_trend_50_200`, the 50-day simple moving average over the 200-day, minus one; eligible when above zero | Refinery — its two windows are what a later experiment sweeps, and **a sweep must never cost a download** |
| the ranking | `r_liquidity_rank`, the per-date percentile of `c_dollar_volume_63d`, average daily traded value over about a quarter | Refinery, over a Curator column — the minimum the template ships |
| the sizing | none — equal weight is a rule, not a column | the rule cell of `Experiments/Experiment_1/experiment_1.ipynb` |
| the band | none — 10% is a setting of the rule | the same rule cell |

**The moving averages are per-security arithmetic and could sit in the Curator. They do not,
deliberately.** Their windows are exactly what an experiment sweeps, and widening the Curator's
schema forces a refetch of every identifier. Their input, the adjusted close, stays in the Curator,
where nothing about it is tunable.

<!-- example: end -->

---

## The five parts, and the job each does

| Part | Its job | The failure it prevents |
| --- | --- | --- |
| **The main idea** | one sentence somebody outside the team could repeat | a strategy nobody can explain is a strategy nobody can debug |
| **The objective** | the *capability* a finished version gives the desk, not a number | "a Sharpe of 1.2" is not something you can tell whether you have achieved |
| **The claims** | the sentence broken into parts testable separately, each with a status | a strategy that half works reads as working, unless the halves are listed |
| **What is not claimed** | what a reader might assume and would be wrong to | the reader assumes it anyway if you do not say |
| **The named columns** | which `c_*` or `r_*` column carries each half | attribution cannot say which half earned the return unless the halves have names |

---

**Where this stands, with every number and its caveats: [`RESULTS.md`](RESULTS.md).**
How work is done here, and the bar a result has to clear: [`AGENTS.md`](AGENTS.md).
