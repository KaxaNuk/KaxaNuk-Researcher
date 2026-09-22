---
source: John Wiley & Sons (2021). ISBN 9781119789796
citation: "Paleologo, G. A. (2021). Advanced Portfolio Management: A Quant's Guide for Fundamental Investors. Hoboken, NJ: John Wiley & Sons. ISBN 9781119789796."
local_copy: none
read: 2026-09-12, chapter 6, from Luna's library; brought here 2026-09-22 for claim 2
---

# Advanced Portfolio Management — 6. Use Effective Heuristics for Alpha Sizing

*Chapter 6, pages 84–109 of the PDF, from Luna's library, which read it whole: the four sections
that bear on claim 2. The chapter's others — the three conversions an expected return needs, and
factor-neutralising a set of alphas by regression — are not carried; this rule has no expected
returns to convert.*

## Why it is here

Claim 2 of [`OBJECTIVE.md`](../../../OBJECTIVE.md) — *equal weight across the 30 captures that
without a risk model.* Named in the objective as the source **against** the claim: on when a
signal's strength should set the size. Its companion is the same book's
[chapter 8](12_Understand_Your_Performance.md), on how to measure whether it does.

## The Sharpe ratio is an imperfect metric, imperfectly measured, and used anyway

- The Sharpe ratio is average return over return volatility, and the intuition is return measured
  in units of volatility (pp. 86–87).
- Practitioners use "information ratio" for the Sharpe ratio computed on residual returns, which
  the author calls the natural extension of the benchmark-relative definition to the many-factor
  case. Under perfect hedging a portfolio's returns are its idiosyncratic returns (pp. 87–88).
- Why it dominates: "the real scarce resource is not capital; it is risk". A high Sharpe, low
  risk-per-gross strategy can be levered up to an acceptable return (p. 88).
- His verdict: "Always think of volatility as an informative proxy of risk and imperfectly
  measured, and of the Sharpe Ratio as an imperfect, imperfectly measured, but useful, performance
  metric" (p. 88).

> **For claim 2:** any test of a weighting against equal weight will be read off a Sharpe ratio,
> and the chapter's first point is that the number is a proxy read through noise. The status
> vocabulary in `OBJECTIVE.md` already separates *confirmed as a book* from *confirmed as a
> factor*; for claim 2 the second reading is the one that counts, on the idiosyncratic return
> step 6 reports, because a weighting can raise a book's Sharpe by moving its beta.

## Four sizing rules, from ignoring risk to optimising against it

| Rule | Target net market value |
| --- | --- |
| Proportional | `κ α` |
| Risk parity | `κ α / σ` |
| Mean-variance | `κ α / σ²` |
| Shrinked mean-variance | `κ α / [p σ² + (1 − p) σ²_sector]` |

- The rules were chosen for simplicity, needing at most expected returns and volatilities; for
  practical relevance, being in wide use; and for being principled (p. 92).
- The proportional rule ignores volatility entirely; its simpler cousin, the 1/N rule, ignores
  conviction too, analysed in [DeMiguel et al., 2009] (p. 92).
- Risk parity equalises dollar idiosyncratic volatility across positions; mean-variance sizes
  inversely to idiosyncratic variance [Markowitz, 1959]; shrinkage blends the stock's variance with
  its sector's (pp. 92, Procedure 6.2 on p. 93).
- Stocks are assumed uncorrelated, which the author says is the appropriate framework for
  idiosyncratic returns since those are approximately uncorrelated (p. 91).

> **For claim 2:** this book is the 1/N rule the author sets aside in one line — proportional
> sizing with every conviction equal — and it is that because the rule has no conviction: the
> trend state is a yes or a no, and the liquidity ranking is a cut, not a forecast. So claim 2 is
> not a claim that equal weight beats sizing on a signal; it is the claim that the one thing the
> rule *could* size on, each stock's volatility, would not pay. The arm that tests it is the
> table's second row, a thirtieth divided by volatility, and the third is the control that should
> lose.

## The experiment: the simplest rule wins, and it is not because volatility is badly estimated

- Design: idiosyncratic returns for 1998 to 2019, Russell 3000 names with at least two million
  dollars of average daily volume over the prior month, split into one-month horizons. Alpha signals
  are generated within each sector with a five percent cross-sectional correlation to the following
  month's returns, either drawn from a normal distribution or as buy/sell signals of plus or minus
  one. Portfolios of fifty, one hundred and two hundred stocks, unit gross market value, Sharpe
  ratios averaged over many simulated alphas (pp. 94–95).
- Results for one-hundred-stock portfolios using predicted volatility (p. 95, Table 6.1):

| Method | Gaussian signal | Buy/sell signal | Relative loss |
| --- | --- | --- | --- |
| Proportional | 1.61 | 1.29 | — |
| Mean-variance, 75% shrink | 1.55 | 1.23 | −4% |
| Mean-variance, 50% shrink | 1.46 | 1.17 | −9% |
| Risk parity | 1.46 | 1.16 | −9% / −10% |
| Mean-variance, 25% shrink | 1.34 | 1.07 | −16% / −17% |
| Mean-variance | 1.07 | 0.83 | −34% / −35% |

- "The results are consistent across sectors and portfolio breadths" (p. 95).
- The obvious diagnosis is wrong. Repeating the test with perfect foresight of the coming month's
  realised volatility changes little; naive mean-variance still loses forty-six percent (p. 98,
  Table 6.2).
- The real mechanism is the interaction of expected-return error with dispersion in volatility
  across the universe. In a universe where all volatilities are twenty-five percent, a five percent
  forecast error costs `0.05/0.25² = 0.8` in misallocation; in a universe half at ten percent and
  half at forty, the same error costs `2.65`, a 332 percent increase, because low-volatility stocks
  are sized up and errors on them are expensive (pp. 98–99).
- A controlled simulation confirms it. With four thousand simulations of one hundred stocks over
  three years, variances estimated over sixty-three days, unit-variance portfolios (p. 99,
  Table 6.3):

| Dispersion of stock volatility | Proportional | Risk parity | Mean-variance | Mean-variance with exact volatility |
| --- | --- | --- | --- | --- |
| 0.0 | 3.5 | 3.5 | 3.5 | 3.5 |
| 7.8 | 3.5 | 3.4 | 3.0 | 3.1 |
| 18.0 | 3.4 | 3.0 | 2.1 | 2.1 |
| 33.8 | 3.3 | 2.5 | 1.1 | 1.2 |

- The recommendation: "Using target positions that are proportional to the forecasted expected
  returns of a stock beats other common methods" (p. 100, Insight 6.2).
- An earlier illustration makes the estimation-error point concrete: one hundred stocks with
  identical true volatilities, estimated on six months of daily returns and sized by mean-variance,
  produce an average mis-sizing of about nine percent, with eleven stocks mis-sized by more than
  twenty percent, and "the larger positions occur exactly where the error is bigger" (p. 94).

> **For claim 2:** the chapter's experiment is the nearest thing to evidence for claim 2 in the
> library, and it says the claim's edge shrinks where this book lives. Equal weight beat risk
> parity by about a tenth and mean-variance by a third on the author's signals, and the mechanism
> was not a bad volatility estimate but forecast error meeting a wide spread of volatilities.
> Thirty of the most traded names in the United States are a narrow universe in exactly that
> dimension, so the sizing experiment's prediction, fixed now, is the top rows of Table 6.3: risk
> parity within a few percent of equal weight, plain mean-variance below both, and a buy/sell
> signal — which is what a trend state is — losing more from sizing than a graded one. A gap
> larger than that is a finding against the mechanism, not for the weighting.

## Volatility targeting beats gross-market-value targeting in every cell tested

- The hypothesis and its mechanism: volatility is persistent and partly predictable while profit and
  loss is not, so cutting size when volatility spikes should preserve return while reducing risk
  (p. 102).
- The author states the way it could fail before testing: reducing size reduces the magnitude of
  profit and loss, and volatility spikes coincide with losses, so if profit and loss reverts, the
  chain runs volatility increase, loss, derisking, smaller gain on the rebound (pp. 102–103).
- Design: normal and buy/sell signals, one-month and three-month signal horizons, breadths of fifty,
  one hundred and two hundred, each sector, fifty simulations over 1998 to 2019 on US stocks, with
  both quantities targeted daily. Monthly targeting gave similar results (p. 103).
- "The results are very consistent: for every signal type, horizon, sector, and portfolio breadth,
  volatility targeting generates higher risk-adjusted returns" (p. 103).
- Gains at the one-month horizon range from about two to eleven percent by sector, largest in
  financials and technology, media and telecoms (p. 106, Tables 6.5 and 6.6).

> **For claim 2:** not claim 2's content, but the lever beside it. This book targets a gross of
> 98% invested and lets the filter decide the rest, and step 3 found the filter is mostly a
> volatility sorter — 28.7% forward volatility in an uptrend against 36.7% out of one — so the rule
> already does a crude version of what the chapter recommends, at the level of names rather than of
> the book. Sizing the whole book to a volatility target is a separate experiment, and the
> chapter's failure mechanism, derisking into a rebound, is the same one `OBJECTIVE.md` already
> names for the filter.

## The confidence band on a measured Sharpe ratio is wide enough to swallow most decisions

- The annualised Sharpe ratio is the daily one times the square root of two hundred and fifty-two;
  the weekly one times the square root of fifty-two (p. 107).
- The approximate ninety-five percent interval, citing [Lo, 2002], is the estimate plus or minus
  1.96 times `√[(1 + ½ SR²)/n]` (p. 107).
- The author's worked example: three years of daily returns, seven hundred and fifty-six trading
  days, daily Sharpe of 0.1. The standard error is 0.036 daily, and annualised the Sharpe ratio is
  1.6 with a standard error of 0.6, giving an interval of (0.4, 2.8) (pp. 107–108).

> **For claim 2:** the rule beats its equalised control by 0.030 of Sharpe over 9.4 years, and the
> author's example — a standard error of 0.6 on three years of daily data — is the scale of the band
> such a gap sits inside; nine years narrows it, not to a thirtieth. A sizing experiment judged on a
> Sharpe gap of that size would be judged on noise, which is why `AGENTS.md` asks for a parameter
> to be chosen on a property of the signal and for attribution before belief: the per-lever
> decomposition in step 6, not the headline ratio, is where claim 2's arm has to show its work.

## What it changes

- Puts claim 2 in the source's terms: equal weight is the 1/N rule, and the only sizing this rule
  could add is by volatility, so the arm that tests the claim is risk parity, with mean-variance as
  the control that should lose.
- Fixes the sizing experiment's prediction before it runs: risk parity within a few percent of
  equal weight and mean-variance below both, because the universe's volatility dispersion is
  narrow; a larger gap argues against the mechanism, not for the weighting.
- Names the mechanism a weighting has to beat — forecast error meeting volatility dispersion, not
  volatility estimation — and the author's negative control, perfect foresight of volatility, as
  the design to copy.
- Sets volatility targeting of the whole book aside as a lever of its own, with the same failure
  mode the objective names for the filter.
- Gives the confidence band that makes a 0.03 Sharpe gap unreadable, and sends claim 2's verdict
  to step 6's decomposition instead.
- It does not test equal weight on a buy-or-hold screen with no conviction, or any rule after
  costs, and its universe is three thousand names, not thirty.
