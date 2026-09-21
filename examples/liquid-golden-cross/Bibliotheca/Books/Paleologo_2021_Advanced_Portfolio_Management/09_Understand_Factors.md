---
source: John Wiley & Sons (2021). ISBN 9781119789796
citation: "Paleologo, G. A. (2021). Advanced Portfolio Management: A Quant's Guide for Fundamental Investors. Hoboken, NJ: John Wiley & Sons. ISBN 9781119789796."
local_copy: none
read: 2026-09-12, chapter 5, from Luna's library; brought here 2026-09-19 for claim 1
---

# Advanced Portfolio Management — 5. Understand Factors

*Chapter 5, pages 56–83 of the PDF, from Luna's library, which read it whole: the three sections that
bear on claim 1. The chapter's others — country and industry factors, low volatility, short interest
and crowding, value — are not carried.*

## Why it is here

Claim 1 of [`OBJECTIVE.md`](../../../OBJECTIVE.md) — *among the most traded US stocks, those whose
50-day average is above their 200-day go on to earn more than those whose is not.* Named in the
objective as the source on why a trend rule is not a momentum rule.

## The author admits a selection filter and the possibility of overfitting

- Commercial vendors carry between fifty and one hundred factors (p. 57).
- He describes only those that seem "material, experimentally robust, investable, and
  interpretable", grouping them as the economic environment, the trading environment, technical
  factors, and company valuation (p. 58).
- On valuation factors specifically: a smaller subset exhibits "simplicity (elementary ratios),
  credibility (with a large out-of-sample history), and relevance in the events of large
  drawdowns", and "it is likely that this large set of factors is subject to the problem of
  overfitting" (p. 78).
- Two explanations compete for any non-zero factor return: compensation for risk, or a behavioural
  story in which returns come from investors' bounded rationality. He presents both, the first as
  more relevant to risk management, the second as an aid to interpretation (p. 57).

> **For claim 1:** the idea began from a belief — not to fight the trend — and a belief is not a
> mechanism. The blueprint has to say which of the chapter's two explanations the trend filter rests
> on, a premium for bearing a risk or investors' slowness to act on what prices already show,
> because `AGENTS.md` asks for the economic reason before the run and the two predict different
> failures. Of the author's four tests, the filter passes *investable* and *interpretable* by
> construction; *experimentally robust* is what Sullivan, Timmermann & White (1999) examine for
> moving-average rules, and nothing in this chapter does.

## Betting against beta: high-beta stocks underperform, and betas compress in a crisis

- A dollar-neutral portfolio long high-beta and short low-beta stocks does not earn the positive
  return the CAPM implies. The opposite trade does, a result known as betting against beta
  [Frazzini and Pedersen, 2014] (p. 63).
- The proposed mechanism is constraint-driven: investors who cannot short or lever seek return by
  buying high-beta stocks, bidding their prices up until intrinsic value reasserts itself (p. 63).
- It follows that beta factor returns are positive in a risk-on environment and negative in
  risk-off, so the factor reads as a barometer of risk appetite (p. 63).
- Beta compression: taking Russell 3000 constituents and plotting the interquartile range of
  estimated betas, the range falls sharply between September 2008 and January 2009, the acute phase
  of the financial crisis (p. 64, Figure 5.4). High exposure is therefore especially dangerous in a
  sudden derisking.

> **For claim 1:** a trend filter is likely to move the book's beta with the market. After a fall,
> the stocks still in an uptrend are likely the ones that fell least, which tend to be the low-beta
> ones; after a rally, the high-beta ones come back in. If so, part of whatever the filter-on book
> gains over the filter-off book is a beta that moved rather than a better selection. The blueprint
> should predict both books' betas, and step 6's beta factor should be read before the filter is
> credited with anything.

## Momentum is robust across markets, centuries and asset classes, and has a term structure

- Momentum is relative performance, distinct from trend following, which is absolute (p. 74).
- It has been observed in many equity markets with the notable exception of Japan, in equities,
  commodities and bonds [Asness et al., 2013], and over two centuries [Geczy and Samonov, 2016]
  (p. 74).
- Its term structure: the past zero to one month reverts, more strongly the shorter the window;
  one month to one year continues; beyond a year it reverts again [Novy-Marx, 2012] (pp. 74–75).
- The author is candid about the explanations: "Even a cursory read of the research on momentum
  will convince you that we don't understand the origins of momentum. We have complex,
  hard-to-falsify theories based on observational data" (p. 75).
- Risk-based explanations have emerged. A quantile plot of medium-term momentum returns, z-scored
  by trailing three-month volatility, shows a left tail heavier than normal, and this is extended by
  [Daniel and Moskowitz, 2016] (p. 76, Figure 5.10).
- A stronger claim: two studies define lower tail dependence, the probability a stock has a large
  loss when the market does, and show that treating it as a factor makes momentum redundant, with
  momentum's returns becoming insignificant once lower tail dependence is included
  [Chabi-Yo et al., 2018; Ruenzi and Weigert, 2018] (pp. 76–77).
- Momentum's losses come from its short side. In 2008 momentum was volatile but did not lose money;
  in 2009 the previous year's losers rallied as the market rebounded, and the short side produced
  the crash. Early 2016 saw another crash concentrated in energy names that ran up two to three and
  a half times in February and March (p. 77).
- A successful manager holds long momentum without trading it, because winners acquire positive
  loadings and shorts acquire negative ones (p. 78).

> **For claim 1:** the first bullet is why claim 1 is not a momentum claim. The filter compares a
> stock with its own past, so the evidence gathered for momentum — across markets, asset classes and
> two centuries — is evidence for a different rule and cannot be borrowed; this rule needs its own.
> Three consequences follow. If the term structure holds for a trend as it does for momentum, the
> 50-day average's latest month works against the signal, so a variant that skips it is a later
> experiment, not a change to this one. The book has no short side, so momentum's documented crash,
> a rally in the shorted losers, cannot hit it; its own bad period is the one `OBJECTIVE.md` names,
> sitting out the start of a rebound. And the stocks it holds are usually relative winners too, so
> step 6 will likely show a positive momentum loading that is not the filter's own work: what the
> filter adds beyond momentum is what the filter-off comparison measures.

## What it changes

- Claim 1 is a trend claim, now from a source rather than from the objective's own reasoning: the
  momentum literature is context for it, not evidence.
- Before the filter is credited, its book's beta has to be measured: a filter-on book can beat a
  filter-off one through a beta that fell after declines.
- The blueprint's first line on the signal is its mechanism — a risk premium, or a slow reaction —
  and not the belief the idea started from.
- Step 6 is predicted to show a positive momentum loading that is not the filter's contribution.
- The latest month inside the 50-day average is the first variant to try once the benchmark is
  frozen.
- It does not settle claim 1: the chapter tests no trend rule. Whether a moving-average filter earns
  anything, and whether that survives the search that found it, is for
  [Sullivan, Timmermann & White (1999)](../../Papers/Sullivan_Timmermann_White_1999_Data_Snooping.md)
  and [LeBaron (1999)](../../Papers/LeBaron_1999_The_Stability_Of_Moving_Average_Rules.md), both now
  read: robust in sample, and gone in the decade after. Brock, Lakonishok & LeBaron (1992) itself
  stays unread — both copies found are image scans with no text layer.
