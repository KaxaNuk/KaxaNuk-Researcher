---
source: "https://ssrn.com/abstract=3705001, printed at the foot of every page; working paper, Department of Finance and Real Estate, The University of Texas At Arlington, March 2019. The link was not opened: SSRN answers a bot check"
citation: "Sarkar, S. K., Du, Y., & Vafai, N. (2019). Impacts of Sector and Company Size on Effective Factor Investing: Evidence from U.S. Equity Market. Working paper, March 2019. https://ssrn.com/abstract=3705001, as printed in the paper."
local_copy: Bibliotheca/Papers/Sarkar_Du_Vafai_2019_Impacts_Of_Sector_And_Company_Size.pdf
read: 2026-09-22, the whole paper
---

# Sarkar, Du & Vafai (2019) — Impacts of Sector and Company Size on Effective Factor Investing: Evidence from U.S. Equity Market

*The whole paper, pages 1–41 of the extract: the abstract, sections I to V, the appendix's list of
variables, Figures 3-1 and 3-2, Tables 3-1 to 3-12 and the references. Page numbers are the
extract's page markers, the PDF's pages, which coincide with the numbers the paper prints at the
foot of each page. The tables arrive in the extract one cell per line and were read back onto the
row order their headers print; Tables 3-5 and 3-6, the two summaries of significant factors, lose
their column alignment in extraction and are read through the text on pages 18 and 19. No journal,
volume, DOI or working-paper number is printed anywhere in it.*

## Why it is here

Claim 3 of [`OBJECTIVE.md`](../../OBJECTIVE.md) — *ranking by trading volume keeps every position
in a stock that trades heavily enough to be exited in a day.* The owner's reason for the paper:
"what being a large-cap book does to the signal — the volume ranking makes this a book of the
largest companies; the paper says momentum holds there and size and value vanish". It also bears on
open lead 3 of [`RESULTS.md`](../../RESULTS.md), the eleven sector factors that read exactly zero
in the step-6 decomposition: the paper's central result is that, in a book of large companies,
sector exposures explain most of what market beta, size and value had seemed to. It is the first
note read for claim 3; the two other paper notes on the rule itself,
[Sullivan, Timmermann & White (1999)](Sullivan_Timmermann_White_1999_Data_Snooping.md) and
[LeBaron (1999)](LeBaron_1999_The_Stability_Of_Moving_Average_Rules.md), serve claim 1.

## The question is which factors hold in the long run once sectors, company size and the business cycle are controlled, and the design is a two-step regression

- The starting point: "identifying those factors that can generate long-term stable returns from
  those short term time-varying factors becomes the key question to be answered in factor investing
  research" (p. 4). Ang (2014) is cited for factor returns being "time-varying, market dependent"
  and liable to "underperform for a long time" (p. 4).
- One reason offered for temporary factor returns: "the performance of a known factor could be
  affected by unintended risk factors from industry groups (sectors), regions or countries" (p. 4).
  Company size, industry sectors, regional and country risks are "main sources of factor bias", the
  correlation between compensated and uncompensated factors (p. 8).
- Three questions "still left unanswered": how industry sectors affect the stability of common
  factors over a long horizon; how company size affects it; which factors generate stable long-term
  returns once sector and business-cycle interactions are controlled (p. 8). "The interaction
  between industry sectors and known factors is overlooked in the literature" (p. 8).
- Two hypotheses: "unintended sector exposures could explain some compensated factors like market
  beta since industries and sectors are compositions of the total market", and "firm-specific risks
  are compensated by sector exposures because firm specific risks are clustered in the same
  industry/sector" (p. 9). By example, "a company's market beta could be partially explained by the
  company's financial leverage or its industry" (p. 9).
- The design: a principal component analysis "for preliminary check"; a first-step regression of
  each portfolio's monthly return on the common factors, the macro controls and the microstructure
  variables; a second step adding the 17 sector variables to the same model (p. 12). Each is run
  with and without an intercept — "since risk free rate is included in the regression analysis the
  intercept should be an indicator of unexplained returns by the model" (p. 13) — and a recession
  dummy is then added to both steps (p. 14).
- Expected in advance: common factors significant in all three portfolios "except size factor in
  the large portfolio", and that once sectors are in "market risk, value factor and some other
  common factors may lose the explanatory power shown in the first-step regression, especially in
  small and medium-size portfolios" (p. 13).

> **For claim 3:** the paper's first hypothesis is claim 3's construction seen from the other side —
> whether what a factor model calls beta, size and value in a book of large companies is sector
> exposure wearing those names. Its instrument is a monthly time-series regression of a fixed
> portfolio, so nothing in it measures a ranking, a cost or a cross-section; what it can say is which
> loadings a large-cap book should expect, and which of them a step-6 decomposition should expect to
> reassign once its sector block does something.

## The data are 515 survivors of the S&P 500 and the Russell 3000, split by sales and held equal-share and unrebalanced over 324 months

- Constituents of the S&P 500 and the Russell 3000 screened "at year end of 2016", keeping the 515
  "with public monthly trading data available from January 1990 to December 2016"; the authors say
  it "is impossible for us to build a portfolio consisting of all current S&P500 companies and
  Russell 3000 companies since many constituent companies in two indices do not have available data
  for such a long time period" (p. 10). Monthly returns from CRSP through WRDS (p. 10).
- Size is by annual sales, not by market value: 354 "large size" companies with sales above $1
  billion, 93 "small" below $100 million, 68 "medium" between (p. 10). The abstract and the
  introduction call the 354 "large-cap" (p. 1, p. 4).
- Three "equal-share weighted buy-and-hold portfolios": Aggregate, the 515; Small-and-Medium, the
  161; Large, the 354. "Portfolios are not rebalanced after initial equal number of shares is added
  to the portfolio", so that returns come "purely" from price change "rather than returns caused by
  the change of the number of shares or market capitalization" (p. 10). The weighted average of the
  holdings' returns is the dependent variable (p. 10).
- The window is "a total 27 years test period starting from 1990 to 2006" once (p. 10) and January
  1990 to December 2016, 324 months, everywhere else (p. 4, p. 12, p. 15); 27 years matches the
  latter.

> **For claim 3:** the paper's "large" is sales above $1 billion, among names that were still index
> constituents in 2016 and were then held unrebalanced for 27 years; ours is the top 30 by traded
> value, re-ranked at every rebalance, delisted names retained. The two overlap without being the
> same thing — the paper never sorts on volume — so it speaks to the book's size character and not
> to the ranking, and its sample ends a year before this strategy's window opens. Its universe is
> also the survivor list `AGENTS.md`'s first lie warns about, by the authors' own account.

## The regressors are eight French factors, the yield curve and two credit curves, two microstructure variables, French's 17 sectors and an NBER recession dummy

- Common factors, monthly, from Ken French's data library: market risk, size (SMB), value (HML),
  profitability (RMW), investment (CMA), momentum, and short- and long-term reversal (p. 11). The
  momentum factor is written out as the two high prior-return portfolios minus the two low; the two
  reversal factors are printed with one identical formula, low minus high (p. 11). The profitability
  and investment factors are `RMW` and `CMA` in the text and `RWC`, `RWA` and `CMW` in equations 3.1
  to 3.4 (pp. 13–14).
- Controls: the yield curve, "10 years treasury yield minus three month T-bill rate"; the credit
  curve as two spreads, the AAA and the BBB corporate yield each over the three-month T-bill, from
  FRED (p. 11). The appendix defines the same three as spreads over the "risk free rate" (p. 24); the
  tables label them `T10YFF`, `AAA10Y` and `BAA10Y` (p. 29 onward), and the paper never says how the
  labels map to the definitions.
- Market microstructure: S&P 500 index volatility (`SP_vol`) and the Pástor–Stambaugh traded
  liquidity factor (`PS_VWF`), "the value-weighted return on the 10-1 portfolio from a sort on
  historical liquidity betas" (p. 11). Tables 3-7 to 3-12 also carry `PS_LEVEL` and `PS_INNOV`,
  which the text never defines; the number Tables 3-3 and 3-4 print under `SP_Vol` is the number
  Tables 3-7 and 3-10 print under `PS_INNOV` (p. 29, p. 33; p. 30, p. 36).
- Sectors: French's 17 industry groups — Food, Mines, Oil, Cloths, Durables, Chemicals, Consumers,
  Construction, Steel, Fabric Products, Machinery, Cars, Transportation, Utilities, Retails, Finance,
  Other — chosen over his 38 because 17 "could ensure model simplicity and avoid model over-fit with
  a dataset of 324 observations" (p. 12). They enter the second step as `Sector 1` to `Sector 17`
  (p. 13), one coefficient each in the tables; what a sector variable's monthly value is, the text
  does not say in words.
- The business cycle: a dummy `REC`, 1 in NBER recessions and 0 otherwise (p. 12).

> **For claim 3:** two of the paper's four blocks have no counterpart in the step-6 model — the
> risk-free rate and yield curve, and the credit spreads — and a third, the sectors, is the block that
> read zero. The paper's liquidity variable is a market-wide factor return, not a stock's own volume,
> so whatever it does or does not explain says nothing about whether ranking on traded value costs
> return; Amihud (2002) stays the lead for that.

## Before the regressions, the large-company portfolio's cumulative return trails the market premium, and four or five components drive the returns

- Cumulative monthly returns to December 2016: large-company portfolio 1.94%, small-company 16.96%,
  aggregate 11.16% (p. 15, Table 3-1 p. 27). Factor cumulatives over the same window: Mkt-Rf 6.68%,
  SMB 7.2%, HML 11.88%, RMW 0.48%, CMA 3.42%, momentum −4.59%, short-term reversal −1.02%, long-term
  reversal −0.23% (p. 15). "Apparently large-company portfolio underperormed market risk premium
  (Mkt-Rf) in this time period" (p. 15).
- How "cumulative monthly return" is computed is not stated; Figure 3-1's axis runs from −100% to
  40%, and its caption dates the series from January 1996 where its title says January 1990 (p. 25).
- Principal components of the 515 return series: 127 components with eigenvalue above 1 explain
  85.99% of the variance; the first five explain 31.09% — 15.77%, 8.4%, 2.7%, 2.3% and 1.85% — and
  "the rest components only contribute less than 2% of total variance" (pp. 15–16, Table 3-2 p. 28).
  "A preliminary conclusion from factor analysis is that four or five components may drive the major
  change of portfolio return" (p. 16); the PCA "did not tell us the economic meaning of these
  principal components" (p. 16).

> **For claim 3:** on the paper's own figures an equal-share book of the largest companies trailed
> the market premium over 27 years, the direction in which `OBJECTIVE.md` expected the ranking to
> cost return — but with the arithmetic behind the figure unstated, it is a direction and not a size.
> Our book beat its index over nine years; the windows do not overlap and neither number tests the
> other.

## In the first step, without sectors, most common factors are significant, momentum only in the large-company and aggregate portfolios and the credit curve only in the small-company one

- "Investment factors (CMA), reversal factor (both short-term and long-term), liquidity, and market
  volatility factors are insignificant in three portfolios across the board" (p. 17).
- Large-company portfolio, Table 3-3, without intercept: Mkt-RF 0.0093, SMB 0.0025, HML 0.0020, RMW
  0.0026, RF −0.0257, momentum −0.1674 and T10YFF −0.5303, all starred at 95%; CMA 0.0017 (p 0.094),
  the credit spreads, PS_VWF and SP_Vol not significant (p. 29). With the intercept the same set is
  starred and the intercept itself is 0.0084 with p 0.419 (p. 29).
- "These factors significant in large-company portfolio remain significant in small-company
  portfolio except momentum. Instead credit curve is significant in the contribution to
  small-company portfolio returns" (p. 17) — though Table 3-3 prints the small-company RMW at
  p 0.88, and p. 18 says profitability and value "do not play a role" there. The explanation
  offered: "small companies are more sensitive to credit cycle change while market momentum is
  mainly determined by large companies" (p. 17). In the aggregate "results are similar to the
  large-company portfolio except credit curve" (p. 17).
- The five conclusions drawn: most common factors significant except CMA; "momentum factor only
  affect returns of large-company portfolio, while credit curve only changes small-company portfolio
  returns"; liquidity and volatility "are not determinant factors"; the risk-free rate and yield curve
  "are important factors for all stocks"; value not significant in the small-company portfolio with
  an intercept (p. 17). "Three factors are company-size dependent: momentum, credit curve, and value
  factor" (p. 17).
- The small-company and aggregate first-step panels exist twice and do not agree. Table 3-3 prints
  the small-company Mkt-RF at 0.0090 (p 0.0000) and the aggregate at 0.0093 (p 0.0000); Tables 3-8
  and 3-9, both titled first-step, print −0.0045 (p 0.705) and 0.0029 (p 0.448), the same numbers as
  the second-step Tables 3-4, 3-11 and 3-12 for every common-factor row (p. 29; pp. 34–35; p. 30,
  pp. 37–38). Which set is the first step for those two portfolios the paper does not say. The
  large-company panel is the same in Tables 3-3 and 3-7 but for one p-value on RF, 0.0004 against
  0.0000 (p. 29, p. 33).

> **For claim 3:** without sectors the paper's large-company portfolio reads like `FINDINGS_1.md`'s
> factor table for ours — beta, size, value and momentum all present — and that is the reading the
> second step overturns. Since our sector block contributed nothing, the first step is in effect the
> model our attribution ran; and the large-company panel is the one whose two printed versions agree,
> which is why this note leans on it.

## In the second step, with sectors added, market beta and value lose significance in every portfolio and size everywhere but the small-company one; in the large-company portfolio only momentum, the rate terms and six sectors remain

- "In large-company portfolio size, value, market risk, profitability, and investment factor are
  insignificant, only momentum, yield curve and sectors (mines, fabrics, machinery, transportation,
  utilities and other) are significant when sector variables are introduced ... It implies that
  common factors could be explained by sector exposures in large company stock returns" (p. 18).

The large-company portfolio across the paper's four specifications, without intercept, coefficient
and p-value (Tables 3-3, 3-7, 3-4 and 3-10; p. 29, p. 33, p. 30, p. 36):

| Variable | First step | First step, with REC | Second step | Second step, with REC |
| --- | ---: | ---: | ---: | ---: |
| Mkt-RF | 0.0093 (0.0000) | 0.0090 (0.0000) | 0.0052 (0.216) | 0.0040 (0.282) |
| SMB | 0.0025 (0.0000) | 0.0030 (0.0000) | 0.0009 (0.155) | 0.0010 (0.116) |
| HML | 0.0020 (0.010) | 0.0020 (0.009) | 0.0005 (0.582) | 0.0010 (0.451) |
| RMW | 0.0026 (0.0003) | 0.0030 (0.0000) | 0.0003 (0.765) | 0.0000 (0.837) |
| CMA | 0.0017 (0.094) | 0.0020 (0.098) | −0.0001 (0.919) | 0.0000 (0.806) |
| RF | −0.0257 (0.0004) | −0.0270 (0.0000) | −0.0268 (0.0001) | −0.0280 (0.001) |
| FF_Momentum | −0.1674 (0.0000) | −0.1640 (0.0000) | −0.1167 (0.003) | −0.1060 (0.005) |
| T10YFF | −0.5303 (0.0000) | −0.5450 (0.0000) | −0.4868 (0.0000) | −0.4950 (0.0000) |
| REC | — | −0.0060 (0.242) | — | −0.0040 (0.392) |

- The six large-company sectors starred in the second step: Mines 0.0621 (p 0.010), Fabric Products
  0.1304 (0.032), Machinery 0.1710 (0.009), Transportation 0.1733 (0.004), Utilities 0.0946 (0.041)
  and Other −0.3823 (0.014); Durables, Construction and Steel sit between p 0.07 and 0.09 (p. 30).
  The with-intercept column agrees throughout, the intercept at 0.0112 with p 0.246 (p. 30).
- Small-company portfolio: "most common factors are insignificant except the size ... momentum
  factor again loses its significance but two credit curve variables (BAA10Y and AAA10Y) are both
  significant" (p. 18). In Table 3-4: SMB 0.0084 (p 0.0000), RF −0.4367 and T10YFF −4.3944 starred
  in both columns; BAA10Y 3.0639 (p 0.007) starred without the intercept and AAA10Y −4.6316
  (p 0.015) with it, each spread significant in one specification only; HML 0.0059 at p 0.031
  without the intercept, which the text does not mention; of the sectors, Oil starred in both
  columns and Consumers with the intercept (p. 30).
- Aggregate portfolio: "most common factors, except size, could be explained by sectors. At the same
  time momentum and yield curve factors remain significant" (p. 18): SMB 0.0026, RF −0.1231,
  momentum −0.0724 (p 0.042), T10YFF −1.4052, and Oil, Consumers, Machinery and Transportation
  starred (p. 30).
- The summary drawn: "when sector variables are added most common factors significant in the
  first-step regression lose explanatory power, especially those factors in the large-company
  portfolio and aggregate portfolio. The only exception is the size factor which remains significant
  in the small-company portfolio. Yield curve and risk free rate are two main determinants of returns
  for all three portfolios" (pp. 18–19). "When sectors are added to second-step regression market
  beta and value factor are not significant anymore for all three portfolios, implying market beta
  and value factor could be explained by sectors" (p. 19).

> **For claim 3, and open lead 3:** this is the result that bears on the sector puzzle. In a book of
> large companies the paper finds that adding sector series removes the significance of beta, size
> and value and leaves momentum, the rate terms and six sectors. If it transfers, the 83 market
> points and the 4 size and 3 value points in `FINDINGS_1.md` are partly sector exposure that the
> eleven zeros are hiding, and "plain market beta" is a label the sector block never got to contest.
> The technology weight moving between 15% and 45% is exactly the exposure a working sector block
> would price.

## Momentum is a determinant in the large-company portfolio and not in the small-company one; the size premium is the reverse

- "In the large-cap portfolio, the momentum effect on long term equity returns is robust, but the
  size and value effects disappear. In the small-cap portfolio the momentum, however, is not
  significant, but the size premium is recorded in long term returns" (p. 1).
- "A very important observation from the second-step regression analysis on three portfolios is:
  momentum factor is only significant in the large-company portfolio but in small-company portfolio
  the size and credit yield curve are two determining variables" (p. 19); a page earlier momentum
  "remain[s] significant in the aggregate portfolio" too (p. 18), and Table 3-4 stars it there
  (p. 30).
- "The fact that momentum factor only works in large-company portfolio and size factor only finds
  its place in small-company portfolio suggests that effectiveness of factor investing strategies
  varies with the company size and sectors" (p. 19).
- The sign. The large-company momentum coefficient is negative in every specification the paper
  prints — −0.1674 and −0.1728 in the first step, −0.1167 and −0.1221 with sectors, −0.1640 and
  −0.1060 with the recession dummy (p. 29, p. 30, p. 33, p. 36) — and in the aggregate, −0.0724 and
  −0.0942 (p. 30). The small-company coefficient is 0.0721 with p 0.51 (p. 30). The text reports
  significance and never the sign.
- The inference drawn in the conclusions: "an effective momentum strategy could only be implemented
  successfully through selecting large company stocks but it does not work with the small company
  stocks" (p. 22).

> **For claim 3:** the owner's reason for reading this — that momentum holds in the largest
> companies — is confirmed as a statistical fact and complicated by a sign. The paper's large-cap
> portfolio loads negatively on the momentum factor in every table, and the text never says so; ours
> contributes +12.75 points, which `FINDINGS_1.md` reads as a positive loading the book acquired by
> holding winners. What the paper supports is "a large-cap book's return is tied to the momentum
> factor", not "a large-cap book earns the momentum premium", and it is no evidence that our 12.75
> points are compensated.

## Market beta, size and value are largely explained by the risk-free rate, the yield curve and the sectors, which the authors read as risk clustering within industries

- "When industry sectors are included in the second-step regression, influences of three common
  factors: market beta, company size, and value factor are largely explained by the risk-free rate,
  yield curve, and industry sectors" (p. 1); "market beta is mostly explained by the change of risk
  free rate, yield curve, and industry sectors" (p. 1).
- The mechanism: "since risks, especially company characteristic risks are clustered within the same
  industry we argue that industry sector, a factor that incorporates both systematic risks and
  company characteristic risks, could significantly affect the efficiency of some common factors in
  long term return generation" (p. 9). In the conclusions, "the finding that sectors could also
  explain value effect in large company portfolio confirmed that risks are clustered within the same
  industry or sector, and some sector risks are not captured by common factors like market beta and
  company size" (p. 22).
- The rate terms are the constant: the risk-free rate and the 10-year term spread carry negative,
  starred coefficients for the large-company portfolio in all four specifications (table above), and
  "yield curve and risk free rate are two main determinants of returns for all three portfolios"
  (p. 19). One exception in the tables: with both an intercept and the recession dummy, RF's p-value
  is 0.148 in the first step and 0.055 in the second (p. 33, p. 36).
- What the finding licenses, in the authors' words: "the insignificance of market beta factor in
  second-step regression when sectors are added implies that a better risk adjusted return could be
  achieved through sector exposures (or sector rotation) rather than passive diversification using
  market index portfolio" (p. 22).

> **For claim 3:** `OBJECTIVE.md` wrote that step 6 "will see [the ranking] as a size exposure";
> this paper says a size loading on a large-cap book is what a model without sectors sees and what a
> model with them does not. `FINDINGS_1.md` found size at 4.11 points of 159.5, so the weaker reading
> already held; the paper explains why it should have. And the 28 points assigned to the ranking sit
> on a model with no rate term and no working sector block — the two things the paper says explain a
> large-cap book's beta — so they are provisional until at least one of those is in.

## The findings repeat when an NBER recession dummy is added, and the dummy itself is insignificant

- "Our findings will not be conclusive if business cycle variables are excluded in the two-step
  regression analysis" (p. 19).
- Large-company portfolio, first step with REC: "significant variables are the same as without the
  recession dummy variable: all common factors, market risk, size, value, investment and momentum
  factor are significant while the recession dummy does not affect the large companies' stock
  return" (p. 19). Table 3-7 prints CMA at p 0.098 and 0.106, not starred, and REC at −0.0060 with
  p 0.242 and 0.265 (p. 33). "The shape of the 10-year treasury curve is still significant ... which
  implies that in large portfolio Federal Reserve's monetary policy change is leading the business
  cycle change" (p. 19).
- Large-company portfolio, second step with REC: "recession dummy variable is not significant, only
  momentum and the 10-year treasury curve and sectors are significant"; the long-term return of the
  large-company portfolio "is mainly determined by sectors, momentum and 10-year treasury yield curve
  rather than common factors like market risk, size, value, and investment sentiment" (p. 20). The
  same six sectors are starred as without the dummy (p. 36).
- Small-company and aggregate: the text says the dummy is "not significant" in every case (p. 20,
  p. 21). Tables 3-8, 3-9, 3-11 and 3-12 print it starred in their without-intercept columns —
  −0.0280 with p 0.031 for the small-company portfolio, −0.0100 with p 0.022 for the aggregate — and
  unstarred with an intercept (p. 34, p. 35, p. 37, p. 38). The small-company text also lists
  "market risk" among the significant variables (p. 20) where Table 3-8 prints Mkt-RF at −0.0060
  with p 0.626 (p. 34).
- The reading: "all common factors, yield curve and credit curve on portfolio returns are less
  impacted by the business cycles which means a stable long term portfolio return could be realized
  by positioning the portfolio to these factor exposures" (p. 20).
- The count arrived at: "four factors: yield curve, risk free rate, momentum and sectors are main
  driving force of the large-company portfolio return, while in small-company portfolio the return is
  determined by five factors: yield curve, risk free rate, size, credit curve and sectors",
  "consistent with the result of principal component analysis that long term stock returns are
  driven by either four or five principal components" (p. 21).

> **For claim 3:** in the paper's sample, adding a recession dummy left a large-cap book's loadings
> where they were, which is a reason to expect the book's size and sector character to be a property
> of the construction and not of the decade it is measured in — with three caveats: the dummy is
> starred in two of the paper's own columns; it enters as a level shift, so the test is not whether
> the loadings change in a recession; and the only recession in our window, 2020, lies outside the
> paper's sample.

## The conclusions prescribe sector rotation and momentum for large-cap investing, and the yield and credit curves for small-cap

- "We conclude that for effective factor investing in large-cap portfolio, right sector rotation and
  market momentum strategies must be implemented, while in small-cap portfolio changes of yield curve
  and credit curve are determining factors" (p. 1).
- "It implies that an effective factor investing strategy could not ignore sector exposures with
  appropriate sector rotation" (p. 22); "the effectiveness of factor investing strategies could be
  undermined without proper consideration of sector exposures, size of company and the shape of
  credit curve. Factor timing and sector rotation is the key to a successful factor strategy
  implementation" (pp. 22–23).
- Neither reversal factor is significant anywhere: "both long term and short term reversal factors
  are not significant in any long run stock returns" (p. 22).
- On the small-company side, "investors may use credit quality as a signal to adjust their exposures
  to small company stocks" (p. 22).
- What is left to later work: "the future study on this topic may provide us more hints on this
  critical issue of effective factor investing" (p. 23). No rotation rule, no momentum rule and no
  portfolio built on either is tested; the prescriptions are inferred from the regressions.

> **For claim 3:** the paper's prescription for large-cap investing describes what this book does by
> accident — it rotates sectors with no rule, technology from 24% to 15% to 45%, and it carries
> momentum without trading it. `OBJECTIVE.md` claims neither as skill, and the paper gives no reason
> to start: its evidence is that these are where a large-cap book's return sits, not that a rule
> earns them, and it never prices a rule.

## What it changes

- Claim 3's status does not move: it is true by construction and the paper is not about the
  construction. What moves is the reading of "the book's largest idiosyncratic source". The paper
  says a large-cap book's return sits in sector exposure and in the rate and yield-curve terms (p. 1,
  pp. 18–19, p. 21) — the two parts of the step-6 model that were absent or read zero — so the 28
  points assigned to the ranking are provisional until one of them is in.
- `OBJECTIVE.md`'s expectation that step 6 "will see [the ranking] as a size exposure" should be
  rewritten, through `objective`, as a prediction that it will not once sectors are in: the paper's
  large-company size loading is starred without sectors (p. 29) and not with them (p. 30), and
  `FINDINGS_1.md` already found size at 4.11 points.
- Open lead 3 rises in value. The paper's central result is that sector series absorb what beta,
  size and value seemed to explain in large caps (p. 18, p. 22), so eleven sector zeros are not a
  cosmetic defect: they are the block this paper says would move the decomposition most, and the 83
  market points are provisional with them.
- The momentum loading is now doubly qualified: the book inherits it without trading it
  (`FINDINGS_1.md`), and the one paper read on large-cap momentum finds a significant negative
  coefficient it never remarks on (p. 29, p. 36). It is not evidence that the 12.75 points are a
  premium, and no prediction should cite it as such.
- A rate term belongs on the next attribution's checklist: the risk-free rate and the yield curve are
  starred for the large-company portfolio in every specification (p. 29, p. 30, p. 33, p. 36) and the
  step-6 model has neither. A lead for the attribution run, not a change to the rule.
- Amihud (2002) and Lee & Swaminathan (2000) stay the leads for whether the ranking costs return: the
  paper's liquidity variable is a market-wide factor, insignificant everywhere (p. 17), and it never
  sorts on volume.
- It does not settle claim 3, or anything about the ranking. It is a working paper — one sample of
  515 names that survived to 2016, one method, monthly, 1990 to 2016, unrebalanced buy-and-hold, with
  tables and text that disagree in the small-company and aggregate panels — and its "large" is sales
  above $1 billion, not traded value. Its headline holds in both printed versions of the large-company
  tables, which is why this note cites those by number; whether the sector zeros are the library, the
  files or the book is a question only the attribution run can answer.
