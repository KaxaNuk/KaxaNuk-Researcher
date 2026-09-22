---
source: No publisher, year, ISBN, DOI or URL is printed in this copy. The PDF carries the title page, the contents and the body of the second edition, and no copyright page; the latest work it cites is dated 1999
citation: "Grinold, R. C., & Kahn, R. N. (n.d.). Active Portfolio Management: A Quantitative Approach for Providing Superior Returns and Controlling Risk (2nd ed.). No publisher or year is printed in this copy."
local_copy: none
read: 2026-09-16, chapter 16, from Luna's library; brought here 2026-09-22 for claim 4
---

# Active Portfolio Management — 16. Transactions Costs, Turnover, and Trading

*Chapter 16, pages 449–480 of the PDF, from Luna's library, which read it whole: the four sections
that bear on claim 4. The chapter's last, on trading as its own optimisation and on limit orders,
is not carried; execution is outside this repository's scope.*

## Why it is here

Claim 4 of [`OBJECTIVE.md`](../../../OBJECTIVE.md) — *trading only when the book is 10% away from
its target keeps most of the return at a fraction of the turnover.* Named in the objective as the
source **for** the claim: keeping most of the value added at half the turnover. The claim as
written is this chapter's rule of thumb, transplanted; the note records the conditions the rule
came with.

## Transactions costs can consume half a good manager's return

- Active U.S. equity managers underperform the S&P 500 by 1 to 2 percent a year on average, which,
  "as Jack Treynor has argued, ... can only be due to transactions costs", against the 2 to 3
  percent of active return typical managers seek (p. 449).
- The studies behind it: Lakonishok, Shleifer and Vishny (1992) found underperformance of 1.3
  percent equal-weighted and 2.6 percent capitalisation-weighted for 341 managers over 1983 to
  1989; Malkiel (1995) found 43 basis points for active equity mutual funds over 1982 to 1991 in a
  naïve analysis, and 1.83 percent once funds that disappeared before 1991 were included (p. 449).
- "Who cares about a 1 or 2 or even 5 percent cost if you expect the stock to double?
  Unfortunately, expectations are often wrong", and "winner or loser, you still pay transactions
  costs"; "A top-quartile manager with an information ratio of 0.5 may lose roughly half her
  returns because of transactions costs" (p. 449).
- Costs are commissions, the smallest and easiest to measure, the bid/ask spread, roughly the cost
  of trading one share, market impact and opportunity cost (pp. 450–451). Market impact "must be
  discovered through trading", and because no one can trade many shares and one share under
  identical conditions, "Market impact is the financial analog of the Heisenberg uncertainty
  principle. Every trade alters the market" (p. 451).

> **For claim 4:** this is the reason claim 4 exists at all — a rule turning over 165% a year, as
> [`FINDINGS_1.md`](../../../Experiments/Experiment_1/FINDINGS_1.md) reports, is a rule whose
> return costs can halve. Two of the chapter's four costs are in the engine, commission and a
> slippage charge; impact and opportunity cost are not, so the band's saving is measured here on
> the smaller half of what a band saves in life, and the sweep should say so beside every number.

## Market impact comes from informed trading and inventory risk, and grows with the square root of size

- "There is no CAPM or Black-Scholes model of trading" (p. 451). A liquidity supplier cannot tell
  whether a manager is informed, so "The larger and more urgent the trade, the more likely it is
  that the manager is informed, and the higher the price concession the liquidity supplier will
  demand"; even without informed traders, the supplier charges for holding inventory until opposing
  trades arrive (p. 452).
- Wagner (1993) found among 20 managers that the most aggressive information trader realised very
  large short-term returns offset by very large costs, while the slowest often had negative
  short-term returns with small or negative costs, having supplied liquidity (p. 453).
- The inventory risk model makes the time to clear proportional to the trade's share of daily
  volume, the risk the volatility over that time, and the impact a price for that risk, which is
  consistent with the rule of thumb "that it costs roughly one day's volatility to trade one day's
  volume" (pp. 454–456).
- Market impact "should increase as the square root of the amount traded", which agrees
  "remarkably well" with the bids Loeb (1983) collected for blocks of different sizes; the total
  cost therefore "increases as the 3/2 power of the amount traded" (p. 456). A simple calibration
  sets typical trades at about 2 percent round trip (p. 456).
- Structural models, like BARRA's with submodels for volatility, trading volume and intensity, and
  elasticity, avoid the poor quality, coverage and timeliness of purely empirical estimates, and
  price risk separately for buys and sells and for exchange and over-the-counter stocks
  (pp. 457–458).

> **For claim 4, and claim 3:** the impact the engine does not charge is the cost the liquidity
> ranking is there to keep small — one day's volatility to trade one day's volume, and the thirty
> most traded names are where a rebalance is the smallest share of a day's volume. That is claim 3
> doing claim 4's work. The band sweep should carry, per setting, the largest share of daily volume
> any rebalance would have traded at the capital the strategy is meant for, because a band that
> saves commission while concentrating trades into bigger blocks may cost more on the chapter's
> 3/2 power than it saves.

## Implementation shortfall measures the whole cost, and cheaper measures miss the largest part

- The implementation shortfall compares "the returns to a paper portfolio with the returns to the
  actual portfolio", where "The paper portfolio is the manager's desired portfolio, executed as soon
  as he or she has devised it, without any transactions costs"; the difference includes commissions,
  spread, market impact and the opportunity cost of trades that never executed, and "Wayne Wagner
  has estimated that such opportunity costs often dominate all transactions costs" (p. 453).
- Comparing executions with the day's volume-weighted average price "measures market impact
  extremely crudely and misses opportunity costs completely. The method simply ignores trade orders
  that don't execute", and traders "can easily game VWAP" (p. 454).
- Tick-by-tick data are censored: they "show trades, not orders placed, and certainly not orders
  not placed because the cost would be too high. Realized costs will underestimate expected costs",
  and the thinly traded assets that cost most are the ones least observed (p. 454).

> **For claim 4:** the engine fills every trade at the next day's volume-weighted average price and
> charges commission on the unadjusted one, which is the chapter's crude measure with a cost model
> on top, not a shortfall. Every net figure in this repository is net of a model, and the band's
> saving is a saving inside that model; the paper-trading step is where the shortfall itself would
> first be measured, and until then the sweep's costs are estimates that the chapter says run low.

## Half the turnover keeps at least three-quarters of the value added

- A strategy needing 80 percent turnover a month should not be dismissed: "We may be able to add
  considerable value with the strategy if we restrict turnover to 40 percent, 20 percent, or even 10
  percent per month" (pp. 458–459). Turnover is defined as the smaller of purchase and sales
  turnover, which leaves out contributions and withdrawals (p. 460).
- The value added attainable at each level of turnover rises and flattens, and prorating every
  trade toward the optimum gives a lower bound: "You can achieve at least 75 percent of the
  (incremental) value added with 50 percent of the turnover", which "implies that a strategy can
  retain at least 87 percent of its information ratio with half the turnover", an implication the
  authors call loose (p. 461).
- Scheduling the best trades first beats the bound (pp. 461–462). Where the slope of the
  value-added frontier equals the round-trip cost is the optimal turnover, and if costs exceed the
  slope at zero turnover the manager should not trade (p. 463).
- The slope implies a cost, so an ad hoc policy such as "no more than 20 percent turnover per
  quarter" can be checked: if costs are thought to be about 2 percent but the slope at the limit is
  about 4.5 percent, "something is awry", and the fixes are a higher cost estimate, a higher
  turnover limit, or alphas scaled back toward zero; "This type of analysis serves as a reality
  check on our policy and the overall investment process" (p. 464).
- On the S&P 100 with random, benchmark-neutral alphas scaled so the optimum has 3.2 percent alpha
  at 4 percent active risk, starting from 20 random equal-weighted stocks, 50 percent of the optimal
  turnover captures 86.8 percent of the incremental value added with an implied round-trip cost of
  1.90 percent, and 20 percent captures 59.0 percent at 5.12 percent; the gain from picking the best
  trades is largest at 20 percent, and "reasonable levels of round-trip costs (about 2 percent) do
  not call for large amounts of turnover" (pp. 464–465).
- With inequality constraints such as no short sales, "You are not guaranteed three-quarters of the
  value added for one-half the turnover. Nevertheless, in our experience, 75 percent is still a
  reasonable lower bound"; and turnover spent moving a portfolio back inside its constraints is
  unavailable for new alphas (p. 466).
- Costs of 1.42 percent for half the stocks and 2.26 percent for the rest, taken into account,
  "barely affected portfolio alphas or risk, but did reduce transactions costs by about 30 percent"
  (p. 467).

> **For claim 4:** claim 4 is this rule of thumb, and the chapter attaches three conditions to it
> that the objective's sentence does not carry. The bound is for prorating every trade toward an
> optimum, and this rule does not prorate — it trades to the full target or not at all. It is
> guaranteed under equality constraints only, and a long-only book at a thirtieth each is the
> inequality case, where the authors keep 75 percent as experience rather than proof. And it is a
> bound on *incremental* value added over a frontier, which means the band sweep must be read as
> that frontier: value added against turnover across 0%, 5%, 10%, 20% and 30%, with the slope at
> 10% read as the round-trip cost the band implies and checked against the cost the engine charges.
> The first point on that frontier is already priced — the same names at 87 rebalances beat
> themselves at 11, net — and it says the frontier is still rising where the band sits, which is
> the opposite of what the claim expects.

## What it changes

- Gives the objective's claim 4 its source, and the three conditions the source attached to it:
  prorated trades, equality constraints, and a bound on incremental value added over a frontier.
- Turns the band sweep into the chapter's frontier — value added against turnover — and its 10%
  point into an implied round-trip cost that can be checked against the engine's.
- Reads the equalised control's result, more turnover and more return, as the frontier still rising
  at 10%, against the claim.
- Records that the engine charges two of the chapter's four costs, so every net figure here is net
  of a model that runs low, and that the liquidity ranking is what keeps the missing two small.
- Asks the sweep to report, per band, the largest share of a day's volume any rebalance would have
  traded at the intended capital.
- It does not price a band on a screen, or give measured costs for any market or period beyond a
  calibration of about 2 percent round trip.
