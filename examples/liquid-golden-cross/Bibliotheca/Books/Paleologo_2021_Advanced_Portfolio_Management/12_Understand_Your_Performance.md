---
source: John Wiley & Sons (2021). ISBN 9781119789796
citation: "Paleologo, G. A. (2021). Advanced Portfolio Management: A Quant's Guide for Fundamental Investors. Hoboken, NJ: John Wiley & Sons. ISBN 9781119789796."
local_copy: none
read: 2026-09-12, chapter 8, from Luna's library; brought here 2026-09-22 for claim 2
---

# Advanced Portfolio Management — 8. Understand Your Performance

*Chapter 8, pages 135–160 of the PDF, from Luna's library, which read it whole: the six sections
that bear on claim 2, and on how the counterfactual books of Experiment 1 are read. The chapter's
others — earnings trades and market impact at an event, and evaluating alternative data — are not
carried.*

## Why it is here

Claim 2 of [`OBJECTIVE.md`](../../../OBJECTIVE.md) — *equal weight across the 30 captures that
without a risk model.* Named in the objective as the source on how to measure whether a signal's
strength should set the size. Its companion is the same book's
[chapter 6](10_Use_Effective_Heuristics_for_Alpha_Sizing.md), on when it should; and the
counterfactual section of
[`FINDINGS_1.md`](../../../Experiments/Experiment_1/FINDINGS_1.md) is this chapter's machinery,
already run once.

## Total return is the wrong frame of reference

- The author's analogy: running while the Earth orbits the Sun at sixty-seven thousand miles an
  hour. In the Sun's frame his speed is indistinguishable from Usain Bolt's, which "obscures the
  vast difference in skill between the two of us" (p. 136).
- Total profit and loss lives in the Sun's frame; idiosyncratic profit and loss lives in the Earth's,
  and factor attribution is what moves between them (p. 136).
- Attribution is the sum over time of idiosyncratic plus factor profit and loss, with the factor
  part splitting into country, industry and style (p. 136).

> **For claim 2:** the frame for claim 2 is the idiosyncratic one, and it was fixed before the run
> — step 6 reports the book's excess return as 71% factor and 29% idiosyncratic — so a weighting
> proposed against equal weight is judged on what it does to the 45.5 idiosyncratic points, not to
> the 17.85% the book compounded at. A weighting that lifts the headline by adding beta has
> changed frames, not earned anything.

## A worked example where every level of attribution reverses the conclusion

- A US net-long book, four hundred long against one hundred short, has a total Sharpe ratio of 1.56,
  which "may be interpreted as a sign of skill, but it is of course mainly attributable to the
  market" (p. 137, Figure 8.1).
- Net of market and industry the returns are mediocre. But the idiosyncratic profit and loss is
  excellent, with a Sharpe ratio of 2.4, and the style profit and loss cancels the gain (pp. 137–138,
  Figure 8.2).
- One level further down, the culprit is momentum, confirmed by an average exposure of one hundred
  and twenty-four million dollars carrying thirty percent of factor variance (p. 139, Table 8.1).
- The author's reading is that this is good news, because factor risk and profit and loss can be
  managed, unlike the underlying skill (p. 137).

> **For claim 2:** Experiment 1 reads like the author's example with the signs changed. Its 0.861
> Sharpe is mostly market — 52% of the excess return is beta at 1.028 — and the largest style
> contributor is momentum, +12.75 points the book never traded for; the difference is that here
> the style paid rather than cancelled. The author's reading applies unchanged: the momentum is
> manageable and the skill is not, so a sizing arm that changed the momentum loading — heavier in
> the names that ran furthest, say — would be reported as a factor change, and the equal weight
> keeps that loading where the filter put it.

## Idiosyncratic performance decomposes into selection, sizing and timing

- The identity is `PnL(idio) = selection + sizing + timing`. Selection is being directionally right,
  sizing is being right about magnitude, timing is taking risk when the theses are better than
  average (p. 140).
- The method is counterfactual. Rewrite the position history as a matrix of dates and tickers, then
  equalise the gross value within each date keeping the sides, holding total gross value fixed; this
  is the cross-sectionally equalised strategy, which removes sizing (pp. 140–142).
- Equalising across dates as well gives the cross-sectional time-size-equalised strategy, which
  additionally removes timing; the two differ only in whether gross value can vary by date
  (pp. 146–147).
- The decomposition is then `PnL(idio) = [PnL(idio) − PnL(XSE)] + [PnL(XSE) − PnL(XSTSE)] +
  PnL(XSTSE)`, that is sizing, timing and selection (p. 148).
- Four caveats before running it: set a minimum position size so that dormant or illiquid positions
  are excluded, suggested at one million dollars in a book of five hundred million to a billion with
  seventy to eighty names; analyse idiosyncratic performance only; remember transaction costs are
  ignored; and consider equalising dollar idiosyncratic volatility rather than gross value
  (pp. 142–143).
- The author's summary of what is typically found: "There is anecdotal evidence that PMs have at
  best very little timing skill, moderately-positive-to-moderately-negative sizing skill, and
  primarily selection skills" (p. 148).
- The example book shows the long side improving under equal sizing and the short side getting
  worse, and he immediately warns against taking it at face value, listing luck explanations: an
  unforeseen litigation crash, an acquisition offer taken badly, an accounting scandal (p. 143).

> **For claim 2:** this identity is why claim 2 cannot be measured on the book as it stands. The
> cross-sectionally equalised book *is* this book — every position a thirtieth — so its sizing term
> is zero by construction, and what Experiment 1's six counterfactual arms measured is the
> remainder: selection against five random draws of the same shape, which put the baseline at
> about 12.5 of the 45.5 points, and the filter as a fourth term of the author's own. Timing is
> still open — the book goes to cash when fewer than thirty names qualify, and the time-equalised
> arm that would price that has not been run; prediction 6's second clause waits on it. Claim 2
> gets a number only when a weighting with a non-zero sizing term is priced beside this one, and
> the author's prior for that number is "moderately positive to moderately negative".

## Liquidity can invalidate the whole analysis

- The equal-sized counterfactual assumes a position can be built instantly. For books of several
  billion in gross value with as few as fifty assets, building even a liquid name can take months
  (p. 145).
- A significant share of a fundamental book's profit and loss is realised around earnings, and those
  positions cannot and should not be built quickly, since transaction costs would consume the alpha
  (p. 145).
- The refinement is to keep equal sizing but add a constraint that no more than a given percentage
  of daily volume is traded per day. With a fifty million dollar target and a two and a half million
  daily limit it takes twenty days to build and twenty to unwind; at one million a day the position
  is never fully built before the view changes (p. 146, Figure 8.5).
- The idealised analysis is still useful: "It shows the selection and sizing skill of a PM when the
  portfolio size is in itself not a concern. If these skills are there pro forma in a paper
  portfolio, but are not realized in the dollar portfolio, then we can be assured that this has to
  do with the deployment of the strategy — maybe its capacity is lower than we thought — or with the
  execution of the strategy itself" (p. 145).

> **For claim 2, and claim 3:** the counterfactuals assume every position can be built in a day,
> and the liquidity ranking is what makes that nearly true of this book — which is claim 3 earning
> its place in claim 2's measurement. The author's participation-rate replay is the check the
> paper-trading step would add: the same book built at no more than a stated share of each name's
> daily volume, at the capital intended. Below that capital the two books coincide, and the
> chapter says that where they part is deployment, not the rule.

## The information ratio is a hit rate times the square root of breadth

- With normally distributed residual returns of identical volatility and a hitting probability `p`
  of guessing the sign correctly, the annualised information ratio is
  `[2p − 1] × √(252 × effective number of stocks)` (p. 148).
- The effective number of stocks is the inverse of the Herfindahl index, the sum of squared gross
  value shares; it equals the actual count when positions are equal and less when concentrated
  (p. 149, Procedure 8.1).
- The consequence is that the hit rate needed is tiny. At fifty-one percent and seventy stocks the
  information ratio is 2.6; at 50.5 percent it is 1.3; a statistical arbitrage book with three
  thousand effective names reaches 8 at a hit rate of 50.5 percent (p. 149).
- "The power of diversification is great. It is not a skill: it is a skill multiplier" (p. 149).
- The limit is that hit rate is not independent of breadth. Beyond a threshold, coverage grows at
  the expense of accuracy, whether the manager stretches or hires, because coordination consumes
  the time budget for analysis (p. 149).
- The measurement problem is severe. Going from eighty to ninety effective positions should raise
  the information ratio by six percent, but the standard error on a yearly hit rate of 50.5 percent
  is 0.33 percent, "comparable to the edge of 0.5%". The probability of observing a lower
  information ratio despite the genuine increase is "only slightly less than 50%" (p. 150).
- His conclusion, paraphrasing Einstein: "increase diversification as much as you can, but not
  more" (p. 150).

> **For claim 2:** equal weight is the sizing that keeps the effective number of names at its
> maximum — thirty of thirty, as `FINDINGS_1.md` reports — so any other weighting spends breadth to
> buy conviction, and this rule has no conviction signal to spend it on. That is the cleanest
> statement of claim 2 the library offers. The measurement problem is its warning: a sizing gain
> of a few percent on thirty names over nine years is inside the error on the hit rate, so the
> sizing experiment should be written to detect a large effect or to report that it could not, and
> never to read a small one as a result.

## The exploratory sweep and the confirmatory test are not the same evidence

- Asked how significant a difference in a what-if Sharpe ratio is, the author calls it "a deep and
  still-open question" and gives two overlapping answers (p. 159).
- The first: as a manager with deep expertise, "your analysis is confirmatory (or dis-confirmatory)".
  You believe credit card data improves a revenue estimate, you add it to the score, and you check.
  "This is very different from an exploratory analysis, where you try many combinations" (p. 159).
- The second: "there are ways to assign a 'Sharpe haircut' to a backtested strategy", pointing to
  [White, 2000; Hansen and Lunde, 2005; Romano and Wolf, 2005; Harvey and Liu, 2015a,b;
  Harvey et al., 2016] (p. 159).

> **For claim 2:** the sizing experiment is confirmatory only if its arms and their predicted
> order are written before any is priced, as chapter 6's table lets them be; three weightings tried
> and the best kept is the exploratory case, and its Sharpe owes a haircut. The trial count
> `AGENTS.md` asks for is the cheap version of that haircut, and White (2000) in the author's list
> is the Reality Check that
> [Sullivan, Timmermann & White (1999)](../../Papers/Sullivan_Timmermann_White_1999_Data_Snooping.md)
> apply to moving-average rules.

## What it changes

- Fixes the frame claim 2 is judged in — the idiosyncratic return of step 6 — and says a weighting
  that lifts the headline by adding beta has changed frames, not earned anything.
- Reads Experiment 1's attribution as the author's worked example: mostly market, momentum the
  largest style, and manageable; the equal weight keeps the momentum loading where the filter put
  it.
- Shows why claim 2 has no number yet: the equalised book is this book, so its sizing term is zero
  by construction, and a weighting with a non-zero term has to be priced beside it.
- Names the arm still missing from the counterfactuals — the time-equalised book that prices the
  cash the filter holds — on which prediction 6's second clause waits.
- Puts claim 3 inside claim 2's measurement: the counterfactuals assume instant fills, and the
  liquidity ranking is what makes that nearly true.
- States claim 2 as breadth: equal weight keeps the effective number at thirty, and any other
  weighting spends breadth on a conviction this rule does not have.
- Warns that a small sizing gain on thirty names over nine years is inside the hit rate's error,
  and that a weighting chosen from several tried owes a haircut.
- It does not settle claim 2: it gives the machinery and the author's prior, not a result for an
  equal-weighted screen, and its books are fundamental long/short portfolios with hundreds of
  names.
