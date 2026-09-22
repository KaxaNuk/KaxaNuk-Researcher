---
source: No publisher, year, ISBN, DOI or URL is printed in this copy. The PDF carries the title page, the contents and the body of the second edition, and no copyright page; the latest work it cites is dated 1999
citation: "Grinold, R. C., & Kahn, R. N. (n.d.). Active Portfolio Management: A Quantitative Approach for Providing Superior Returns and Controlling Risk (2nd ed.). No publisher or year is printed in this copy."
local_copy: none
read: 2026-09-16, chapter 14, from Luna's library; brought here 2026-09-22 for claims 4 and 2
---

# Active Portfolio Management — 14. Portfolio Construction

*Chapter 14, pages 380–423 of the PDF, from Luna's library, which read it whole: the four sections
that bear on claims 4 and 2. The chapter's others — scaling, trimming and neutralising alphas,
alternative risk measures, and dispersion across accounts — are not carried; this rule has no
alphas to scale. Page 380 is the divider of Part Four.*

## Why it is here

Claim 4 of [`OBJECTIVE.md`](../../../OBJECTIVE.md) — *trading only when the book is 10% away from
its target keeps most of the return at a fraction of the turnover.* Named in the objective as the
source **for** the claim: a no-trade band as wide as the costs of buying and selling. Read also for
claim 2 — *equal weight across the 30 captures that without a risk model* — because this is the
chapter where the book puts a screen beside an optimiser and reports what each delivered.

## Implementation guards against poor research, and every constraint is a modified alpha

- "Good implementation can't help poor research, but poor implementation can foil good research."
  Of the inputs, "we can measure only the current portfolio with near certainty"; the covariances
  and costs are noisy, and "The alphas are often unreasonable and subject to hidden biases"
  (p. 381).
- "Many of the procedures used in portfolio construction are, in fact, indirect methods of coping
  with noisy data", and "Implementation schemes are, in part, safeguards against poor research"
  (p. 382).
- Managers add restrictions, such as sector neutrality, position limits and no benchmark bets, to
  make construction robust, but "There is another way to reach the same final portfolio: simply
  adjust the inputs", since any constrained result equals an unconstrained optimisation with
  modified alphas and a matching risk aversion (p. 383).
- In a Major Market Index example with random alphas and an active risk aversion of 0.0833, the
  unconstrained optimum shorts American Express and Coca-Cola and puts almost 18 percent in 3M; with
  no short sales and holdings capped at 5 percent above benchmark, those two are not held and 3M
  sits exactly 5 percent above benchmark. The equivalent modified alphas have a standard deviation
  of 0.57 percent against 2.00 percent for the originals (pp. 384–385).
- "We can replace any portfolio construction process, regardless of its sophistication, by a
  process that first refines the alphas and then uses a simple unconstrained mean/variance
  optimization to determine the active positions" (p. 385). The text reads the example as
  constraints that "effectively shrank the IC by 62 percent, a significant reduction. There is
  value in noting this explicitly, rather than hiding it under a rug of optimizer constraints"
  (p. 386).

> **For claim 2:** in the chapter's terms equal weight is the most modified alpha there is — a
> thirtieth each, whatever the signal said — and this rule chose it knowing that: its signal is a
> yes-or-no state and its ranking a cut, so there is no conviction to size on and nothing for the
> shrinkage to destroy. That is the honest form of claim 2. A later weighting has to show it
> recovers information the equal weight threw away, and the chapter's warning is that a constraint
> hides its cost unless somebody measures it.

## Transactions costs make the scale of alpha matter, and they must be amortised over the holding period

- "Any klutz can juggle two rubber chickens. The juggling becomes complicated when the third
  chicken enters". The claim that estimating costs is as important as forecasting returns "is an
  overstatement", since "Perfect information regarding returns is much more valuable than perfect
  information regarding transactions costs" (pp. 389–390).
- Without costs a wrong alpha scale can be offset by the risk aversion, one knob; with costs "We
  therefore must be precise in our choice of scale, to correctly trade off between the hypothetical
  alphas and the inevitable transactions costs" (p. 390).
- Two stocks each with a 4 percent annual alpha and $0.75 costs to buy or sell: one gains $2 in 6
  months, repeated four times, for a profit of $2 over two years and a 1 percent annual return; the
  other gains $8 in 24 months for a profit of $6.50 and 3.25 percent a year. "The annualized
  transactions cost is the round-trip cost divided by the holding period in years" (pp. 390–391).

> **For claim 4:** the band is what sets this book's holding period, so the chapter's unit is the
> one the band sweep should report in: the round-trip cost divided by the years a name is held, per
> band setting. [`FINDINGS_1.md`](../../../Experiments/Experiment_1/FINDINGS_1.md) has the two
> ends of it — 165% annual turnover, and a cost line that is $106,000 at the frozen commission and
> $36,800 at a realistic one — and the same annual alpha nets three times as much at a two-year
> hold as at six months in the chapter's example, which is the size of what a band can move.

## Practical details: risk aversion from the information ratio, and revision only when alphas leave a band

- The active risk aversion follows from the information ratio and the desired active risk: an
  information ratio of 0.5 and 5 percent active risk give 0.05, and "we must be careful to verify
  that our optimizer is using percents and not decimals" (p. 392).
- A higher aversion to specific than to common-factor risk reduces bets on single stocks, "the (to
  be determined) biggest losers", and pushes multiple portfolios toward the same names (p. 392).
  Stocks outside the benchmark enter it at zero weight, and benchmark stocks without forecasts get
  benchmark-neutral alphas of zero (pp. 392–393).
- Revise "Whenever you receive new information", but a manager who underestimates costs and changes
  alphas often will churn, and "A crude but effective cure is to revise the portfolio less
  frequently"; shorter horizons carry more noise, and "the transactions costs stay the same, whether
  we are reacting to signal or noise" (p. 393).
- A stock's marginal contribution to value added should lie between minus its sale cost and its
  purchase cost, which puts a no-trade band around each alpha as wide as the two costs combined,
  1.25 percent at costs of 0.50 and 0.75 percent (pp. 394–395).
- Leland (1996) shows for a 60/40 allocation that the optimal policy trades back to the edge of a
  no-trade region, and "Trading only to the boundary, not to the target allocation, cuts the
  turnover and transactions costs roughly in half, with effectively no change in risk over time"
  (p. 395). The after-cost information ratio falls with both the one-way cost and a shorter
  half-life of the signals, because costs are paid and because "the transactions costs makes us
  less eager; we lose by intimidation" (p. 396).

> **For claim 4:** this is where the objective's band comes from, and the transplant changed it in
> two ways the band experiment has to know about. The chapter's band sits on each stock's alpha and
> is as wide as its two costs; ours sits on the whole book's turnover, at a round 10%, with no cost
> in its width. And Leland's saving comes from trading *to the boundary*, where our rule, when it
> fires, trades all the way to the target — so the halving of turnover "with effectively no change
> in risk" is not a result this book inherits, only one it can test. Trading to the edge of the
> band is an arm the sweep should include, and the 87 rebalances at 17.8% one-way turnover each
> are what it would be measured against.

## Four construction methods fed the same good alphas; quadratic programming was highest and steadiest on average

- Screens are simple and robust, since "Wild estimates of positive or negative alphas will not
  alter the result", but they ignore all but rankings and "Risk control is fragmentary at best. In
  our consulting experience, we have come across portfolios produced by screens that were
  considerably more risky than their managers had imagined" (pp. 397–398).
- Stratification is "glorified screening", and "When a portfolio manager says he uses stratified
  sampling, he wants the listener to (1) be impressed and (2) ask no further questions"; "Often,
  little substantive research underlies the selection of the categories, and so risk control is
  rudimentary" (pp. 398–399).
- A linear program uses all the alpha information but controls risk only through characteristics,
  which "should not work at cross purposes with the alphas" (pp. 399–400). A quadratic program
  handles alpha, risk and costs together, but a 500-stock universe needs 500 volatilities and
  124,750 correlations, and "It is a fear of garbage in, garbage out that deters managers from using
  a quadratic program" (p. 400).
- "This fear is warranted": estimation errors largely cancel in measuring risk, but in optimisation
  "the optimizer ... will take advantage of opportunities that appear in the noisy estimates of
  covariance but are not present in reality". With true market volatility of 17 percent, errors
  within 1 percent cost little, errors beyond 3 percent become significant, especially
  underestimates, and an estimate of 12 percent "leads to a negative value added"; the lesson is
  "it is vital to have good estimates of covariance. Rather than abandon the attempt, try to do a
  good job" (pp. 401–402).
- Muller (1993) fed alphas made of each S&P 500 stock's next-year return plus noise, at an
  information coefficient of 0.1, to four methods, ignoring costs; the law predicts an information
  ratio of 2.24. Portfolios formed in January 1984 and rebalanced in January 1985, January 1986 and
  May 1987, at three risk aversions, gave average ex post information ratios of 0.86 for an
  equal-weighted screen, 1.10 for a capitalisation-weighted screen, 1.27 for stratification and
  1.88 for the quadratic program, with standard deviations of 0.27, 0.79, 0.89 and 0.40, and
  minimums of 0.50, −0.53, 0.33 and 0.98 (pp. 402–403).
- Stratification had the single highest ratio, 2.82, "but no consistency over time"; none of the
  methods reached 2.24 on average, partly because "constraints can effectively reduce the
  information coefficient and hence the information ratio" (p. 404).

> **For claim 2:** this rule is the chapter's first row — an equal-weighted screen — and the
> chapter's verdict on it is claim 2's known trade-off: robust to a wild input, blind to risk. In
> Muller's test that row earned the lowest average information ratio, 0.86 of a predicted 2.24,
> and the steadiest, with the smallest spread and the second-highest floor; the optimiser earned
> twice as much on average and came with the covariance warning attached. What the test cannot say
> is which row this book is in, because its alphas were built from the future at a known skill and
> ours are a trend state and a liquidity cut. A sizing experiment that prices the quadratic row
> against this one, on this signal, is the measurement — and step 3 already reports a mean pairwise
> correlation of 0.303 across the universe, which is the covariance such an optimiser would be fed.

## What it changes

- Names the origin of the 10% band, and the two ways the transplant changed it: the chapter's band
  is per stock and as wide as its costs, and its saving comes from trading to the boundary, not to
  the target.
- Adds an arm to the band experiment: trade to the edge of the band rather than to the full target.
- Gives the unit the band sweep should report costs in — round-trip cost over the holding period in
  years, per band setting.
- Puts claim 2 in the chapter's terms: equal weight is a fully modified alpha, chosen because the
  signal has no conviction to size on, and a screen's blindness to risk is the cost it accepts.
- Records Muller's test as the shape of what a sizing experiment would compare — an equal-weighted
  screen at 0.86 and steady, an optimiser at 1.88 and dependent on its covariance — with the
  caveat that it was run on alphas built from the future.
- It does not test a band on a screen, or any method after costs.
