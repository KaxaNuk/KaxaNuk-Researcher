---
source: Working paper, Erasmus School of Economics and Northern Trust Asset Management - Quantitative Strategies, October 2025. No journal, SSRN number, DOI or URL is printed in it
citation: "Baltussen, G., Dom, M. S., Van Vliet, B., & Vidojevic, M. (2025). Momentum factor investing: Evidence and evolution. Working paper, Erasmus School of Economics and Northern Trust Asset Management, October 2025."
local_copy: Bibliotheca/Papers/Baltussen_Dom_VanVliet_Vidojevic_2025_Momentum_Factor_Investing.pdf
read: 2026-09-22, the whole paper
---

# Baltussen, Dom, Van Vliet & Vidojevic (2025) — Momentum factor investing: Evidence and evolution

*The whole paper, from the extract: the abstract, sections 1 to 7, and Tables 1 to 5 with the
figure captions in the appendix, pages 1–47. The reference list was read only to check the years
the body cites and is not carried. Page numbers are the extract's page markers, the PDF's pages;
the paper's own printed numbers run one behind them.*

## Why it is here

Claim 1 of [`OBJECTIVE.md`](../../OBJECTIVE.md) — *among the most traded US stocks, those whose
50-day average is above their 200-day go on to earn more than those whose is not* — **falsified**
on `FINDINGS_1.md`'s numbers, the filtered book earning 1.12 points a year less than the same
names unfiltered on the same dates. The owner's reason for reading this paper, in his words: *what
the momentum loading means — attribution gave the book +12.75 points of momentum it never traded;
the review says whether that is a factor exposure or the trend filter in another name*. The
objective's *not that this is momentum* line rests on
[Paleologo (2021), chapter 5](../Books/Paleologo_2021_Advanced_Portfolio_Management/09_Understand_Factors.md)
— momentum is relative, trend following absolute — so the momentum literature is context for
claim 1 and never its evidence, and this note is read for where that line falls in the evidence;
its companions on the rule itself are
[Sullivan, Timmermann & White (1999)](Sullivan_Timmermann_White_1999_Data_Snooping.md) and
[LeBaron (1999)](LeBaron_1999_The_Stability_Of_Moving_Average_Rules.md).

## Momentum is past winners continuing to beat past losers, and every study in the lineage ranks stocks against each other

- Momentum is "the tendency of assets that have exhibited strong historical trends to continue
  those trends and hence outperform in the future — commonly summarized as 'winners keep winning,
  losers keep losing'" (p. 2). The word is the physicist's; the measure, from the first paper on,
  is a rank.
- Levy (1967) ranked 200 NYSE stocks by relative strength — "the stock's price change relative to
  a benchmark index" — and found the top tier over 26 weeks kept outperforming over the next 26
  (p. 4).
- De Bondt and Thaler (1985) were after long-term reversal, losers over three to five years beating
  winners over the next three, and found in passing that past-year winners beat past-year losers
  by 7.6 percent over the next year (p. 4).
- Jegadeesh and Titman (1993), JT throughout, ranked all NYSE and AMEX stocks on CRSP over
  1965–1989 by past 3-, 6-, 9- and 12-month returns, went long the winners and short the losers at
  zero cost, held for 3 to 12 months, and found abnormal returns the risk models of the time could
  not explain, robust across sub-periods (pp. 4–5).
- The review's own timeline "is by no means complete"; the authors "have therefore omitted the
  majority of academic studies written on momentum" (p. 5, footnote 1).

> **For claim 1:** every object in this lineage is a cross-section — a stock's return set against
> other stocks', the top of the rank held against the bottom — where our filter is a sign on one
> stock's own two averages, held until it flips, and nothing in the paper sorts a stock against its
> own past. The "trends" in the definition are the physicist's metaphor, not a trend rule.
> `OBJECTIVE.md` says the attribution's factors are relative ones, and this is the relative thing
> they are built on: the +12.75 points are measured against it, not against the filter.

## The standard definition is the past twelve months less the latest one, held for a month, and on the JT sample it earns 11.28 percent a year

- Winners and losers are defined "based on their price momentum over the previous 12 months
  excluding the current month and holding these portfolios for one month — we would argue the
  standard definition across most academic studies" (p. 5).
- Data are the monthly US returns of Jensen, Kelly and Pedersen (2023), from CRSP, for NYSE, AMEX
  and NASDAQ; quintile breakpoints are set on non-microcap stocks — market cap above the twentieth
  NYSE percentile — and every stock, microcaps included, is then assigned; value-weighted (VW) and
  equally weighted (EW) quintile returns are computed and the bottom subtracted from the top, the
  '5-1' (pp. 5–6).
- Over 1965–1989 the loser quintile returned 6.88 percent a year, rising monotonically to 18.16
  percent for winners; the 5-1 spread is 11.28 percent with a t-statistic of 3.50 (p. 6, Table 1
  p. 34).
- Equal weighting strengthens it to 13.38 percent (t 4.78), "indicating that momentum returns are
  even stronger under smaller caps", in line with Jegadeesh and Titman (2001) (p. 6).
- The spread is persistent across the JT years, with one small dip in the EW series in the
  mid-1970s (p. 6, Figure 2 p. 42).

> **For claim 1:** this recipe is what a momentum factor measures, so the +12.75 points in
> `FINDINGS_1.md` say how much the book resembled a twelve-month winners-minus-losers portfolio
> over the window, not whether a 50-over-200 condition earned anything. The book is equally
> weighted but holds the thirty largest names by traded value, which puts its exposure in the
> paper's VW column, the weaker one, rather than in the small-cap EW spread the paper finds
> strongest.

## The premium is sizable and significant before and after the JT sample, and it crashes at market reversals

- Fama and French (1996) find the three-factor model does not explain momentum; Carhart (1997) adds
  it as a fourth factor; Jegadeesh and Titman (2001) find it persists over 1990–1998 (p. 7).
- Post-JT, 1990–2024: 7.89 percent a year VW (t 2.07), "slightly below the results over the JT
  sample"; 10.00 percent EW (t 2.96). Pre-JT, 1927–1964: 9.13 percent VW (t 2.47); 7.14 percent EW
  (t 1.78), significant at the 10 percent level (p. 8).
- Over 1927–2024 the average is 9.24 percent VW and 9.75 percent EW (p. 8), with t-statistics of
  4.31 and 4.66 (Table 1, p. 34).
- The cumulative series shows "two significant 'out-of-sample' crashes — the first around the
  market reversal in 1929, the second around the market reversal in 2009", after which "momentum
  returns have been strong again, with especially strong returns in the last years of the sample
  since the 2020s" (p. 8, Figure 2 p. 42).
- "In other words, momentum is persistent over these sample periods, but is also exposed to crash
  risk" (p. 8).

> **For claim 1:** the book's window, January 2017 to June 2026, sits inside the years the paper
> calls momentum's strongest since its 2009 crash, so an 8 percent share of excess return from a
> loading the book never chose is what a book of recent winners collects in a good decade for the
> factor, and the same loading would carry the factor's return in a bad one. The crashes fall at
> market reversals, the event behind prediction 4's worst stretch, so a rebound hits this book
> twice: through the late-turning average, and through the exposure that came with it.

## It is positive in every one of 31 countries since 1990, and in the United States over 159 years

- Rouwenhorst (1998) found momentum across twelve European countries over 1980–1995. The authors
  replicate with the Jensen et al. (2023) global data, 46 countries over 1990–2024, value-weighted
  quintiles built per country and aggregated by market capitalisation (p. 9).
- World ex-US 7.57 percent a year, emerging markets 6.20 percent, the US 7.89 percent, the world
  7.77 percent; significant at 5 percent for the US and 1 percent for the rest; every universe
  shows the 2009 crash, and "recent returns have been strong, especially outside the U.S." (p. 10).
- Of the 31 countries with data since 1990 all have positive momentum returns, Portugal highest,
  "Japan having only slightly positive momentum returns"; 19 of the 31 have t-statistics above 1.96
  (p. 10, Figure 3 p. 43).
- Before CRSP: Baltussen, van Vliet and Van Vliet (2021) built 1866–1926 from CRSP's own source
  files, 1,488 stocks with hand-collected market capitalisations, "61 years of out-of-sample data -
  a period in length exceeding the original JT sample" (pp. 10–11). The 5-1 spread there is 8.18
  percent (t 2.77) VW and 7.67 percent (t 2.57) EW (p. 11, Table 2 p. 35).
- Over 1866–2024, 159 years, the spread averages 8.83 percent VW and 8.95 percent EW with
  t-statistics of 5.08 and 5.19; $1 in the winners-minus-losers portfolio grows to over $10,000 —
  "gross of transaction costs and management fees" (p. 11 and footnote 6, Table 2 p. 35).
- Momentum is also in high-yield corporate bonds, equity futures, government bonds, currencies and
  commodities, out of sample over 220 years: "momentum is an eternal feature of financial markets"
  (p. 12).

> **For claim 1:** none of this is evidence for the filter, and all of it is evidence that the
> factor the attribution charged 12.75 points to is real, long-lived and gross of costs. What the
> section lends the strategy is the shape of a fair test — the same sort, unchanged, run on
> sixty-one years nobody had tuned it to — which claim 1 has not had: the long window in
> `FINDINGS_1.md` holds membership fixed from 2017 and is the nearest thing so far.

## Post-publication decay is 1.24 points and insignificant; the data-mining estimate is 2.15 points and insignificant

- McLean and Pontiff (2016) find anomalies decay on average 58 percent over about 13 years after
  publication and attribute it to arbitrage. Data mining also implies out-of-sample decay, and the
  pre-1926 period separates the two: investors then "could not have traded on insights from future
  research" (p. 12).
- An OLS of the high-minus-low spread on dummies for 1990–2024 (post-publication), 1927–1964
  (pre-sample CRSP) and 1866–1926 (pre-CRSP) against 1965–1989 in sample. All four samples carry
  data mining in different degrees, "the in-sample period the most, the pre-CRSP period the least";
  only the post-publication period carries arbitrage (pp. 12–13).
- VW: 11.28 percent in sample; the combined coefficient for the three out-of-sample periods, "an
  estimate of the impact of data mining", −2.15 percent; post-publication decay −1.24 percent;
  t-statistics −0.21 and −0.24. EW data mining −6.24 percent, also insignificant (p. 13).
- Starting the post-publication period in 1994 instead does not change the conclusion (p. 13,
  footnote 7). "We find consistent evidence for the momentum premium over time, and fail to find
  significant out-of-sample or post-publication decay in momentum performance" (p. 13).

> **For claim 1:** here the momentum factor and the trend rule part company. The rule's precedent
> lost its return in the decade after publication, in both 1999 notes; the factor lost 1.24 points
> and no significance in the 35 years after its own. Were the loading the filter in another name
> the two would share a fate, so the momentum line reads as exposure to something that survived,
> sitting on top of a filter whose own contribution against the same names is −1.12 points a year.

## Across 4,096 ways of building the factor, every Sharpe ratio is positive

- Menkveld et al. (2024) show design freedom produces "non-standard errors"; Soebhag, Van Vliet and
  Verwijmeren (2024) find them substantial for factor returns and recommend specification checks
  (p. 14).
- Twelve binary choices, on 2×3 size–momentum double sorts: 30–70 versus 20–80 breakpoints; NYSE
  versus full-sample breakpoints; financials in or out; industry neutralisation or not; independent
  or dependent sorts; monthly or yearly (end of June) rebalancing; VW or EW; microcaps in or out;
  negative book-to-market in or out; sub-$5 stocks in or out; utilities in or out; and "banding
  portfolio returns and transaction costs", from Novy-Marx and Velikov (2019). Together, 4,096
  specifications (p. 14).
- Over 1972–2023 the Sharpe distribution is "well-positive across all 4,096 design choices": median
  0.61, range 0.38 to 0.94, t-statistics 2.74 to 6.78 (p. 15, Figure 5 p. 45). The average
  volatility of the double-sorted factor is 14.20 percent, so these correspond to an average
  long-short return of about 8.87 percent a year (p. 15, footnote 9).

> **For claim 1:** the discipline is the thing to copy — 4,096 versions reported as a distribution,
> none of them picked. When the 50 and 200 are swept, the number to publish is the curve's median
> and range, as `OBJECTIVE.md` already asks; a best-of-sweep is the nominal p-value the Sullivan
> note says not to believe. One of the twelve choices is a band on turnover, claim 4's device, here
> treated as a design choice with a cost attached rather than a setting.

## Momentum is in earnings, analyst revisions and news, and in the residual after the market, size and value are removed

- Chordia and Shivakumar (2006) and Jegadeesh and Livnat (2006) find it in standardised unexpected
  earnings (SUE); Chan, Jegadeesh and Lakonishok (1996) in six months of analyst revisions (REV6);
  Wang, Zhang and Zhu (2018) in firm news (NEWS) (p. 16).
- EW long-short returns are significant for all three, between 4.22 percent for NEWS and 8.61
  percent for SUE. VW is mixed: SUE 2.58 percent (t 2.41) over 1965–2024 decays to an insignificant
  1.15 percent post-JT; REV6 5.48 percent (t 2.73) since 1990; NEWS an insignificant 1.15 percent.
  "Fundamental momentum is most robustly present in analyst recommendations and stronger in smaller
  companies" (p. 17, Table 3 p. 36).
- Blitz, Huij and Martens (2011): "high exposures of stock returns to systematic risk factors —
  like market beta, size, and value — may lead to excessively high return variability in price
  momentum strategies", so they rank on residuals from the Fama–French three-factor model (p. 18).
- Residual momentum (RES MOM) over 1965–2024 returns 7.56 percent VW (t 5.50); its t-statistics
  exceed price momentum's post-JT, 3.45 against 2.07 VW and 6.54 against 2.96 EW, "as the
  volatility of the portfolios is materially reduced" (p. 18). Volatility 10.65 percent against
  21.21, maximum drawdown −44.97 against −88.41 percent (Table 5, p. 40).

> **For claim 1:** the filter is a condition on total price, the raw material of the momentum this
> section says carries market, size and value exposure with it — the mechanism by which a book that
> never ranks on past return ends up with a momentum line of +12.75 and a beta of 1.028 instead of
> the sub-one beta prediction 5 wanted. Residual momentum is what the filter would be with the
> market taken out before the sign is struck: a later experiment's variant, and the paper's evidence
> is that the residual version keeps the return and drops the variability.

## Nearness to the 52-week high earns nothing; the run-up to the high carries the momentum

- George and Hwang (2004) proposed nearness of the current price to its 52-week high as an anchor:
  investors hesitate to push a stock near its high higher on good news, and let one far from its
  high fall too little on bad news, "creating momentum-like effects" (p. 19).
- Büsing, Mohrschladt and Siedhoff (2024) split price momentum in two: MOM = P₁/P₀ =
  (P_high/P₀) × (P₁/P_high) = HTP × PTH, with P₀ the price at the start of month t−12, P₁ at the
  end of month t−1, PTH the price-to-high ratio and HTP the high-to-price ratio; HTP "contributes to
  over 80% of overall price momentum profits" (p. 19).
- Replicated: PTH long-short spreads are "small and insignificant", 0.17 percent VW since 1927
  (t 0.08) and 3.52 percent EW (t 1.42); HTP spreads are "sizable and significant across samples",
  9.05 percent VW since 1927 (t 5.35) (p. 19, Table 3 p. 37).
- Regressed on price momentum, PTH VW has an alpha of −5.43 percent (t −3.50) on a slope of 0.61
  (t 28.98), R² 0.42; HTP an alpha of 5.98 percent (t 3.86) on a slope of 0.33 (Table 4, p. 39).
- PTH is the riskiest series in the paper — volatility 19.94 percent, skewness −3.46, kurtosis
  33.39, maximum drawdown −98.72 percent VW — and "a sizable driver of momentum's crash risk",
  where HTP improves on price momentum in both volatility and drawdown (p. 25, Table 5 p. 40).

> **For claim 1:** this is the paper's nearest analogue to our signal and its least comfortable
> result: nearness to the 52-week high is a condition on a stock's own price path, as a 50-day
> average above a 200-day is, and sorted it earns nothing, loads 0.61 on price momentum and has a
> negative alpha once that loading is taken out — the pattern `FINDINGS_1.md` found, a positive
> momentum line beside a filter that costs 1.12 points a year against the same names unfiltered.
> The paper never tests a 50-over-200 condition, so this is a parallel and not a verdict. The
> measurement that would make it one is the momentum line of the equalised control, whose factor
> total the counterfactual table gives, 126.28 points, and whose momentum share it does not.

## Momentum is also in industries, networks and factors, two of which keep the latest month, and all of it loads on price momentum

- Moskowitz and Grinblatt (1999): long the stocks of past winning industries, short past losers.
  The authors compute it on the Fama–French 49 industries, VW peer returns excluding the stock
  itself, and "industry momentum does not exclude the returns of the prior month and hence includes
  the returns from months t−12 to t" (p. 20).
- Text-based peers (Hoberg and Phillips, 2018; the embeddings version of 2025, available since
  2000, the fifty most similar stocks) and shared-analyst networks (Ali and Hirshleifer, 2020)
  (pp. 20–21). VW: industry momentum 6.73 percent (t 4.52) since 1927; ETNIC 9.79 percent (t 1.93)
  since 2000; connected-analyst 7.55 percent (t 2.65) since 1983; EW spreads all above 10 percent
  with t-statistics from 2.53 to 8.16 (p. 21, Table 3 p. 38).
- Factor momentum (Gupta and Kelly, 2018; Ehsani and Linnainmaa, 2022; Arnott, Kalesnik and
  Linnainmaa, 2023) "captures part of the traditional price momentum effect"; built from 153
  factors as "the past 12 months of factor returns (hence not skipping the most recent month)":
  6.45 percent VW since 1927 (t 3.52), EW about double (pp. 21–22, Table 3 p. 38).
- Every alternative correlates positively with price momentum, 0.17 (connected analysts) to 0.77
  (industry) VW; in spanning regressions "each of the alternative momentum strategies load
  positively on price momentum, with all slope coefficients being highly statistically significant"
  (pp. 22–23, Table 4 p. 39).
- The equally weighted composite of all measures (EW ALL) returns 6.35 percent VW (t 5.43) with a
  spanning alpha of 1.76 percent (t 3.63) over price momentum; EW 9.65 percent (t 8.22), alpha 4.83
  (t 8.61). Value weighted, the anchor composite and factor momentum add nothing over price
  momentum (pp. 23–24).

> **For claim 1:** the Paleologo note expected the latest month inside the 50-day average to work
> against the signal; the paper's industry and factor measures keep that month and earn their
> premium, so for a single-stock condition the point is unsettled either way and the skip-a-month
> variant stays a later experiment rather than a fix to this one. The correlations are the caution
> for step 6: every measure here loads on the one price-momentum factor, so a model with a single
> momentum line can say the book carried continuation, not which kind.

## Momentum crashes, and scaling it by its own trailing variance halves the drawdown

- Barroso and Santa-Clara (2015) and Daniel and Moskowitz (2016) document the crash risk (p. 24).
  Price momentum VW over 1927–2024: volatility 21.21 percent, skewness −2.36, kurtosis 22.08,
  maximum drawdown −88.41 percent; EW −95.16 percent (p. 25, Table 5 p. 40). The pre-CRSP series
  shows the same profile, "suggesting crash risk is a persistent feature of traditional price
  momentum strategies" (p. 25).
- The alternative measures are generally less risky; PTH is the exception, and the EW composite of
  all measures runs at 11.57 percent volatility with a −56.84 percent drawdown (p. 25, Table 5
  p. 40).
- Following Barroso and Santa-Clara, the long-short return is scaled by realised variance over the
  previous 126 days, at factor level (RM MOM) and per stock, on each stock's own daily returns
  (RM MOM SL) (pp. 25–26).
- Drawdown falls from −88.41 to −49.37 and −54.64 percent. RM MOM's return rises from 9.24 to 17.87
  percent at a similar volatility, 20.48 percent; RM MOM SL keeps "a similar average return of
  9.36%" with volatility down to 15.33 percent — "a materially higher Sharpe ratio and a more normal
  return distribution" (p. 26, Table 5 p. 40).

> **For claim 1:** these drawdowns are a long-short factor's and the book has no short side; what
> carries over is the timing, at market reversals, and the remedy. The stock-level scaling is a
> time-series overlay on a cross-sectional exposure, which is what the filter is, and it bought its
> protection at a similar return, where the filter cut 2.2 points of volatility and 9.3 of drawdown
> against the plain control at a cost of 1.12 points a year against the equalised one. It also
> reads a 126-day variance, which can move inside the 23 trading days of the 2020 fall a 200-day
> average slept through — a lead for the next brainstorming entry, and the variance side is the one
> LeBaron found stable.

## Risk-based explanations fail; the authors lean to underreaction, and conclude momentum is eternal

- Persistence across 61 years of unique out-of-sample data makes data mining "highly unlikely".
  The paper does not study transaction costs; it cites Novy-Marx and Velikov (2016) and Israel and
  Moskowitz (2013) for the conclusions holding after them (pp. 26–27).
- Risk stories — investment-based (Liu and Zhang, 2008), liquidity (Sadka, 2006; Pástor and
  Stambaugh, 2003), conditional betas in adverse states (Kelly, Moskowitz and Pruitt, 2021) — have
  "some connection to the momentum premium" but their impact "is generally small"; Baltussen, van
  Vliet and Van Vliet (2021) find "downside risk cannot explain the momentum premium across 154
  years of risk events". "While these risk-based explanations offer partial insights, empirical
  evidence suggests they fail to explain the momentum factor premium" (p. 27).
- "Instead, a behavioral explanation seems more likely": Barberis, Shleifer and Vishny (1998),
  gradual incorporation of news; Daniel, Hirshleifer and Subrahmanyam (1998), overconfidence and
  overshoot; Hong and Stein (1999), newswatchers who underreact and momentum traders who amplify;
  Grinblatt and Han (2005), the disposition effect (pp. 27–28).
- Conclusion: momentum is "supported by robust and consistent empirical evidence across extensive
  time frames (spanning up to 159 years of data), diverse portfolio designs (including over 4,000
  different specifications), and global stock markets"; it has "demonstrated resilience against
  concerns of data mining and arbitrage, with little evidence of performance decay driven by
  arbitrage pressures"; "momentum is an eternal feature of financial markets" (p. 29).

> **For claim 1:** the paper's answer to what drives momentum is the second of the two mechanisms
> the Paleologo note asked the blueprint to choose between — slow reaction, not a premium for risk
> — and every model it names describes prices drifting toward news, not one stock's average
> crossing another. If the filter's reason is that same underreaction, the momentum line is where
> its return should appear, and it appeared there rather than in the filter's own contribution; if
> it is not, the paper offers no reason for a 50-over-200 condition to be paid. Either way
> *eternal* is said of the factor, and the objective is right to keep the momentum literature as
> context.

## What it changes

- The momentum loading is a factor exposure, not the filter in another name. The paper's momentum
  is a relative rank throughout and never tests a stock against its own averages (pp. 2, 5); its
  factor survived publication — decay −1.24 points, t −0.24 (p. 13) — where the rule's precedent
  in the two 1999 notes did not. The +12.75 points measure how much the book resembled a
  winners-minus-losers portfolio in the years the paper calls momentum's strongest since 2009
  (p. 8), and are window-dependent.
- The paper names the pattern `FINDINGS_1.md` found: an own-price-path condition, nearness to the
  52-week high, that earns nothing sorted, loads 0.61 on price momentum and has an alpha of −5.43
  once that loading is removed (p. 19, Table 4 p. 39). A parallel and not a verdict; the number
  that would decide it is the equalised control's momentum line, which the counterfactual run
  priced and the findings do not break out.
- Prediction 5's falsified beta limb has a mechanism: a condition on total price inherits the
  systematic exposures that moved the price, which is why Blitz et al. rank on residuals (p. 18).
  A residual-trend variant, the market taken out before the sign is struck, is a later experiment.
- The filter's trade — 1.12 points a year for 2.2 points of volatility and 9.3 of drawdown — now
  has a benchmark: stock-level variance scaling cut momentum's drawdown from −88.41 to −54.64
  percent and its volatility from 21.21 to 15.33 at a similar return (p. 26), on a 126-day signal
  that can turn inside a 2020-sized fall. A lead for `BRAINSTORMING_1.md`, not a change to this
  experiment.
- Any sweep of the 50 and 200 publishes its distribution, as the paper publishes 4,096 Sharpe
  ratios with a median and a range and no winner (p. 15); the turnover band is one of its twelve
  design choices (p. 14), which makes this claim 4's first source.
- The latest month inside the 50-day average is not settled by this paper: single-stock momentum
  skips it (p. 5), industry and factor momentum keep it and still pay (pp. 20, 22), so the
  skip-a-month variant remains a variant to run rather than a correction.
- It does not settle claim 1, and cannot: there is no moving average, no time-series test, no
  long-only book and no single-stock trend condition anywhere in it, and every number is a
  long-short quintile spread, gross of costs (p. 11). Claim 1 stays **falsified** on
  `FINDINGS_1.md`'s numbers; the paper's part is to say what the +12.75 was not.
