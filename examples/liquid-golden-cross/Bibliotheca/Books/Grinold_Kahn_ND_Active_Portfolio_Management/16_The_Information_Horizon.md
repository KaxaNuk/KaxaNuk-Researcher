---
source: No publisher, year, ISBN, DOI or URL is printed in this copy. The PDF carries the title page, the contents and the body of the second edition, and no copyright page; the latest work it cites is dated 1999
citation: "Grinold, R. C., & Kahn, R. N. (n.d.). Active Portfolio Management: A Quantitative Approach for Providing Superior Returns and Controlling Risk (2nd ed.). No publisher or year is printed in this copy."
local_copy: none
read: 2026-09-16, chapter 13, from Luna's library; brought here 2026-09-22 for claim 4
---

# Active Portfolio Management — 13. The Information Horizon

*Chapter 13, pages 352–379 of the PDF, from Luna's library, which read it whole: the four sections
that bear on claim 4. The chapter's others — diversifying or hedging one signal with its own old
score, and the note on an investor's horizon — are not carried.*

## Why it is here

Claim 4 of [`OBJECTIVE.md`](../../../OBJECTIVE.md) — *trading only when the book is 10% away from
its target keeps most of the return at a fraction of the turnover.* Named in the objective as the
source **against** the claim: a delayed trade loses a signal's value at the rate of its half-life,
and a band is a delay. Its companions for the claim are the same book's
[chapter 14](17_Portfolio_Construction.md), where the band comes from, and
[chapter 16](19_Transactions_Costs_Turnover_and_Trading.md), where the turnover rule of thumb does.

## The information horizon is the half-life of forecasting power, and it is intrinsic to the strategy

- "There is a time dimension to information." For most signals the arrival rate is fixed and the
  shelf life is what matters: "Is this a fast signal that fades in 3 or 4 days, or is it a slow
  signal that retains its value over the next year? The latest is not necessarily the greatest"
  (p. 352).
- The macro analysis works on a strategy's returns, and "has the advantage of requiring only the
  returns, not a detailed knowledge of the inner workings of the strategy" (p. 352).
- The chapter's insights: "The information horizon should be defined as the half-life of the
  information's forecasting ability"; "A strategy's horizon is an intrinsic property. Time averages
  or time differences can change performance, but they will not change the horizon"; and "Lagged
  signals or scores and past returns can improve investment performance" (p. 353).
- Delaying implementation, as when a procrastinating investment committee uses the May portfolio
  in June, reduces the information ratio, and the half-life is the delay at which it halves. "The
  half-life is a remarkably robust characteristic of the strategy. Attempts to improve the signal
  using its temporal dimensions may improve performance, but they will have little or no effect on
  the strategy's half-life!" (p. 353).
- In one strategy the information ratio's half-life is 1.2 years; since value added goes with the
  square of the information ratio, its half-life is 0.6 year, and "We can delay implementation of
  the recommended trades for more than 6 months and still realize 50 percent of the value added"
  (pp. 353–354). Another strategy has a very short half-life (p. 354).

> **For claim 4:** the band is a delay whose cost is set by a number nobody has measured here — the
> half-life of this rule's forecasting power. Step 3 has the raw material: the trend signal's
> information coefficient is 0.0112 at a month, 0.0027 at a quarter and −0.0060 at a year
> ([`RESULTS.md`](../../../RESULTS.md), *Before any experiment*), which says whatever it forecasts
> is gone inside a quarter; the liquidity ranking's horizon has never been measured at all. The
> chapter's own test is cheap and engine-priced — the frozen book implemented one, five and
> twenty-one days late, and the delay at which its information ratio halves — and it belongs in the
> band experiment's blueprint before any band is swept, because a band wider than the half-life
> allows is throwing value away and a band narrower than it is paying costs for nothing.

## Mixing the current and lagged portfolios helps unless their correlation equals the decay

- Manager Now runs a strategy with an information ratio of 1.5 and Manager Later holds Now's
  portfolios one month late, with 1.20, both at 4 percent active risk. If the correlation of their
  active returns is below 0.80, the decay of the information ratio, hiring both adds value; above
  it, the sponsor should go short Later to hedge Now (pp. 354–355).
- At a correlation of 0.7 the best mix is 81.5 percent Now and 18.5 percent Later; at 0.85 it is
  118.5 percent long Now and 18.5 percent short Later (p. 355). There is no gain at exactly 0.8 and
  modest gains either side (p. 356).
- In general the best combination of past portfolios makes the correlation between the current and
  the previous combined portfolio equal to the decay rate of the information ratio, which amounts
  to weighting the innovations in each period's portfolio (pp. 356–357).
- "This application of information analysis can quickly help a manager determine if she or he is
  leaving any information on the table": at a correlation of 0.5, a mix of 33 percent lagged and 67
  percent current portfolio gives an information ratio of 1.59, and the same weights can be applied
  to the inputs (p. 357).
- "This optimal mix of Now and Later will improve performance although it will not change the
  horizon" (p. 358). The appendix proves that any mixture of past strategies whose information
  ratios decay exponentially decays at the same rate, assuming equal active risk across lags and
  covariances that depend only on the interval between them (pp. 369–371).

> **For claim 4:** a book held inside a band *is* a mix of Now and Later — between triggers it is
> the last target, drifted, and at a trigger it jumps to the current one — so the chapter says two
> things about it at once. The mix cannot change the rule's horizon, which is why the band cannot
> be what makes the signal work; and whether the mix costs or adds depends on how the correlation
> of the current and lagged books compares with the decay. The first datum is already in
> [`FINDINGS_1.md`](../../../Experiments/Experiment_1/FINDINGS_1.md): the same names traded on the
> rule's 87 dates earned more, net, than traded on 11, which is the direction the chapter predicts
> when the band is wider than the decay warrants.

## A prediction that comes true may still be incidental

- Alphas arriving monthly and useful for two months predict 2 percent for March, and March delivers
  2 percent: "It would seem that the prediction has come true and we can ignore the old information
  ... Not so! ... That 2 percent return may have been incidental" (pp. 362–363).
- Adding the previous period's return as a predictor gives a rule "called 'settling old scores'",
  which corrects the previous score by what the return has already revealed (p. 363).
- Past returns also feed future scores: "With a momentum signal, higher past returns generally mean
  higher future scores. With a value signal, large past returns tend to imply lower future scores",
  and one remedy regresses the scores on prior returns and keeps the residual (p. 364).
- In the appendix's binary example, monthly residual volatility 6 percent and forecast standard
  deviation 4 percent, the current forecast alone has an information coefficient of 0.125 and the
  previous one 0.0833; combined they give 0.1334, and adding last month's residual return, useless
  alone, gives 0.1335. "When the forecast horizon is shorter than the information horizon, treat the
  older forecasts like forecasts from a different source. Past realized returns may also improve
  the forecast" (pp. 377–378).

> **For claim 4:** two cautions for the band sweep. A rebalance that is followed by a gain is not
> evidence that the band fired at the right time, any more than March's 2 percent proved the March
> forecast; the sweep is read as a curve across band settings, never as the months in which one
> setting looked right. And the trend score is itself a function of past returns — a moving average
> is nothing else — so part of its measured information coefficient is the returns' own serial
> behaviour, and the horizon measured from it is the horizon of that behaviour, not of any view.

## Longer return horizons first gain and then lose correlation, and overlapping intervals double count

- Correlating a monthly score with returns over longer horizons gains as the returns reflect more
  of the information and loses as volatility grows; "The signal has its highest predictive power
  when the horizon is about twice the half-life of the signal" (pp. 365–366).
- "Measuring the IC each period ahead has the benefit of avoiding double counting by using the
  dreaded 'overlapping intervals'" (p. 365).

> **For claim 4:** the analyzer's coefficients at 21, 63 and 252 days are measured on overlapping
> forward windows, which the chapter says overstate the evidence by counting the same return
> several times. The band experiment should measure the coefficient month by month ahead — one
> month, two, three — on the frozen signal, because that curve *is* the half-life, and the
> half-life is what licenses a band width. Nothing in this repository has that curve yet.

## What it changes

- Gives the band a cost in the source's terms: a band is a delay, a delay loses value at the
  signal's half-life, and value added halves twice as fast as the information ratio.
- Names the measurement the band experiment needs before any sweep: the frozen book implemented
  one, five and twenty-one days late, and the delay at which its information ratio halves.
- Reads the equalised control's result — more rebalances, more return, net — as the sign the
  chapter predicts when a band is wider than the decay warrants.
- Warns that a rebalance followed by a gain proves nothing about the band, and that a
  moving-average score carries the returns' own serial behaviour in its information coefficient.
- Asks for the coefficient by month ahead rather than on overlapping windows, which is the curve
  the half-life is read from.
- It does not give a half-life for a trend signal, a liquidity ranking or any named strategy: the
  number is this repository's to measure.
