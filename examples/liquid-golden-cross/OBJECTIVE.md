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
> fine-tuned the same day for claim 1 once its notes existed.** Claims 2 to 4 are still in the first
> pass: their evidence is the question that would settle them, and their sources are leads.
> **The status column was updated on 2026-09-20, once `FINDINGS_1.md` reported; no claim's wording
> changed, and the diff shows it** — a claim edited after its test is not a claim. A strategy of
> your own starts from `init-strategy`, never from here.

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
| **1. The signal** | among the most traded US stocks, those whose 50-day average is above their 200-day go on to earn more than those whose is not | **falsified** — they earn about the same, with less volatility; the filtered book earns **1.12 points a year less** than the same names unfiltered on the same dates, and the filter accounts for about 5 of its 45.5 idiosyncratic points ([`FINDINGS_1.md`](Experiments/Experiment_1/FINDINGS_1.md)) |
| **2. The sizing** | equal weight across the 30 captures that without a risk model | **untested** — the book is equal weighted and works, but no other weighting has been run against it |
| **3. The construction** | ranking by trading volume keeps every position in a stock that trades heavily enough to be exited in a day | **true by construction**, and **measured as the book's largest idiosyncratic source**: about 28 of the 45.5 points, against random books of the same shape. It was expected to cost return and it did not |
| **4. The rebalancing** | trading only when the book is 10% away from its target keeps most of the return at a fraction of the turnover | **untested** — the band fired 87 times in 9.4 years at 17.8% turnover each; no no-band arm has been priced |

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

**What would settle it — a lead.** A later experiment that proposes another weighting and has to
beat this one. Until then the claim is that equal weight is *sufficient*, not that it is best.

**Worth reading for it — leads, no note yet.** DeMiguel, Garlappi & Uppal (2009), already a lead in
Part 3, on how hard equal weighting is to beat out of sample. **Against it:** Paleologo (2021),
chapters 6 and 8, on when a signal's strength should set the size, and how to measure whether it
does.

### 3. The construction — the volume ranking

**This claim is true by construction, and is expected to cost return rather than add it.** Ranking
by trading volume is what makes every position one the desk can get in and out of. It also makes
this a book of the largest companies, since trading volume follows company size, and step 6 will
see that as a size exposure, not as skill.

**What is still open — a lead.** How much return the ranking gives up, and whether the trend filter
works as well among the most traded stocks as among the rest. A later experiment varies the cut and
reads it as a curve.

**Worth reading for it — leads, no note yet.** **Against it:** Amihud (2002), *Illiquidity and Stock
Returns: Cross-Section and Time-Series Effects*, on less traded stocks earning more; and Lee &
Swaminathan (2000), *Price Momentum and Trading Volume*, on heavily traded stocks earning less and
their past winners reversing sooner — the closest source to this pairing of volume and trend. **For
it, on costs:** Korajczyk & Sadka (2004), *Are Momentum Profits Robust to Trading Costs?*, on
liquidity-aware construction holding up after costs.

### 4. The rebalancing — the 10% band

**What would settle it — a lead.** Does trading only when the book is 10% away from its target keep
most of the return at a fraction of the turnover, net of costs? The engine answers it directly: the
same rule with no band, trading to the target on every check, against the band at 10%; then a sweep
of the band, read as a curve.

**Worth reading for it — leads, no note yet.** Grinold & Kahn, *Active Portfolio Management*,
chapters 14 and 16, on a no-trade band as wide as the costs of buying and selling, and on keeping
most of the value added at half the turnover. **Against it:** the same book's chapter 13 — a delayed
trade loses a signal's value at the rate of its half-life, and a band is a delay. Novy-Marx &
Velikov (2016), already a lead in Parts 4 and 5, on which cost-saving rules keep an anomaly's return
after costs.

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
  finding.
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
