---
source: https://people.brandeis.edu/~blebaron/wps/dowvoltt.pdf
citation: "LeBaron, B. (1999). The Stability of Moving Average Technical Trading Rules on the Dow Jones Index. Brandeis University and NBER, August 1999, revised November 1999. Link checked 2026-09-19."
local_copy: Bibliotheca/Papers/LeBaron_1999_The_Stability_Of_Moving_Average_Rules.pdf
read: 2026-09-19, the whole paper
---

# LeBaron (1999) — The Stability of Moving Average Technical Trading Rules on the Dow Jones Index

*The whole paper, pages 1–14 of the extract, references and Figure 1 included. Page numbers are the
extract's page markers. No journal, volume or DOI is printed anywhere in it; the title page gives
Brandeis University, NBER, and the two dates in the citation.*

## Why it is here

Claim 1 of [`OBJECTIVE.md`](../../OBJECTIVE.md) — *among the most traded US stocks, those whose
50-day average is above their 200-day go on to earn more than those whose is not.* The author is the
LeBaron of Brock, Lakonishok & LeBaron (1992), the study the objective names as the lead for this
claim, and this paper is his own re-examination of those rules on the ten years after their sample
ended. That 1992 paper is a scan with no text layer and cannot be read here, so this is the closest
the strategy has to evidence on moving-average rules, beside
[Sullivan, Timmermann & White (1999)](Sullivan_Timmermann_White_1999_Data_Snooping.md).

## The paper re-examines Brock, Lakonishok & LeBaron's rules on ten more years of the Dow

- Brock et al. (1992) — BLL throughout the paper — showed that moving-average rules on the Dow
  "had some predictive abilities in both conditional means and variances", and that the results were
  "relatively stable over their 90 year sample period" (p. 2).
- Sullivan, Timmerman & White (1999) had "demonstrated that while it appears unlikely that these
  rules were 'snooped' from the earlier sample, their forecasting performance over recent years has
  disappeared". This paper "corroborates and extends" that result, adding conditional variances,
  robustness checks and a comparison with other rules (p. 2).
- The data are the daily Dow Jones Industrials from January 1897 through February 1999, 24,645 days:
  BLL's series as a subset, plus another ten years after their 1986 stopping point (p. 3).
- The recent subsample starts in 1988, "to avoid the run up and crash of 1987 which would have a
  dramatic impact on such a short sample" (p. 3).
- The series exclude dividends, so "some care should be taken in using these series in evaluating
  long range performance" (p. 3).
- Daily mean return is 0.020 percent over 1897–1999(Feb), 0.015 percent over 1897–1986 and 0.056
  percent over 1988–1999(Feb) — "nearly 3 times the average over the century" (pp. 3–4, Table 1).

> **For claim 1:** this is a timing test on one index — days sorted into buy and sell — where claim
> 1 is a cross-sectional test among stocks, so nothing here tests claim 1 directly. What it does
> test is the half of the filter that has to be true first: that standing above a long average says
> anything at all about the next day's return.

## Conditional means: the buy-sell difference held for ninety years and reversed in the last ten

- The rule is a single moving average of the past N prices: a buy when the price is at or above the
  average, a sell when it is below, applied to the return from t to t + 1 (p. 4).
- One rule only, N = 150 days, "one of the most consistent performing rules historically". Brock et
  al. (1992) and LeBaron (1998) "have already shown that it works well over many different time
  periods", and LeBaron (1998) "shows that a wide range of rules from N = 50 to N = 200 generate
  similar results" (p. 4).
- Significance comes from a t-statistic and from p-values over 1000 bootstrap simulations of a
  geometric random walk drawn with replacement from the actual returns, which keeps the
  unconditional distribution and destroys all dependence (pp. 4–5).

| Sample | Buy-Sell (%) | Buy-All (%) | Sell-All (%) | Buy fraction |
| --- | --- | --- | --- | --- |
| 1897–1999(Feb) | 0.061 (4.60) [0.00] | 0.023 (2.22) [0.00] | −0.038 (−3.10) [1.00] | 0.622 |
| 1897–1986 | 0.066 (4.73) [0.00] | 0.026 (2.36) [0.00] | −0.040 (−3.09) [1.00] | 0.599 |
| 1988–1999(Feb) | −0.048 (−1.12) [0.84] | −0.009 (−0.37) [0.80] | 0.039 (0.922) [0.15] | 0.807 |

- Table 2, p. 5: daily percent, t-statistics in parentheses, bootstrap p-values in brackets. "For the
  entire sample, and the earlier subsample, the results confirm those of BLL" (p. 5).
- "In the later sample the results change dramatically. Not only is the buy return no longer
  significantly larger than the sell return, it is actually less than both the sell return, and the
  unconditional mean." The statistics "appropriately caution us that these are probably
  insignificant"; still, "there is no longer an important difference in conditional means" (p. 5).
- The buy fraction moves from 62 percent over the whole sample to "a dramatic 81%" in the last
  decade (p. 5).
- Figure 1 plots the buy-sell t-test over a 5-year rolling window: the recent difference is negative
  and "recording values that are historically small given the last 100 years of data", and the
  series "take long swings into the positive and negative regions" (p. 6, figure on p. 14).

> **For claim 1:** the strategy's precedent did not survive its own sample — on this index the sign
> flipped in the decade after 1986, the only genuinely out-of-sample decade the rule has been given.
> That the reversal is itself insignificant is the point: the honest reading is that the buy-sell
> difference is no longer measurable, not that it inverted, and `BLUEPRINT_1.md` should predict a
> cross-sectional spread small enough for that to be possible.

## Conditional variances: buy periods are less than half as volatile, and that has not changed

- Variance ratios (Table 3, p. 7): Buy/Sell 0.430, Buy/All 0.666 and Sell/All 1.548 over
  1897–1999(Feb); 0.451, 0.671 and 1.499 over 1897–1986; 0.516, 0.847 and 1.642 over 1988–1999(Feb).
- Two nulls are bootstrapped, the random walk again and a GARCH(1,1) fitted to the returns with its
  normalised residuals scrambled. Both give 1.00 on Buy/Sell and Buy/All and 0.00 on Sell/All:
  "none of the simulated models can generate a variance ratio as large as that in the data"
  (pp. 6–7).
- "In sharp contrast to table 2 the variance differences do not change going into the most recent 10
  year period. The ratio of the buy to sell variances is 0.51 in the last 10 year period which is
  very close to that for the entire sample" (p. 6).
- Mean absolute deviations, less sensitive to outliers, repeat the result exactly, "indicating that
  outliers in any of the subsamples were probably not the cause" (p. 7, Table 4).
- Against the leverage effect: conditioning on the sign of the previous day's return "does not
  eliminate the difference in volatility between buy and sell periods in either the full sample, or
  the recent subperiod" (pp. 7–8, Table 5).

> **For claim 1:** what outlived the original result is a volatility signal, not a return signal, and
> claim 1 is written as a return claim. `FINDINGS_1.md` therefore has to report the filter-on and
> filter-off books' volatilities beside their returns, or it will miss the only effect this paper
> found to be stable — and a book whose realised volatility falls when the filter is on is the beta
> tilt that
> [the Paleologo note](../Books/Paleologo_2021_Advanced_Portfolio_Management/09_Understand_Factors.md)
> predicts step 6 will find.

## The dynamic strategies: the rule beat buy-and-hold over the century and lost to it after 1988

- Annual Sharpe ratios for three strategies. Buy and Hold. Buy/Sell, long or short on the signal.
  Buy, long during buy periods and holding "a risk free asset earning a 3 percent return during sell
  periods", with zero variance assumed in the sell periods (p. 8, Table 6).

| Sample | Buy and Hold | Buy/Sell | Buy | Buy, on buy-period variance |
| --- | --- | --- | --- | --- |
| 1897–1999 | 0.123 | 0.286 | 0.382 | 0.462 |
| 1988–1999(Feb) | 0.776 | −0.053 | −0.495 | −0.518 |

- The last column uses the conditional variance during buy periods and "should be the true Sharpe
  ratio for this strategy" (p. 8).
- "For the entire sample the strategy does outperform buy and hold, and it would best be implemented
  by activating only during buy periods"; but "none of these results hold during the last 10 years
  … they are all negative as indicated buy the earlier results on conditional means" (p. 8).
- The long/short arm is for comparison only: "It is unlikely that this strategy would have been
  feasible over much of the time period since it would have been difficult to short the Dow" (p. 8,
  footnote 9).
- Using these rules to forecast conditional means "can be very dangerous in the current market. This
  danger is above and beyond the usual problems of transactions costs, and issues related to
  actually implementing a strategy" (p. 10).

> **For claim 1:** the Buy column is this strategy's own shape at index level — invested while the
> filter says up, in cash otherwise — and in the decade after the original study it scored −0.518
> against 0.776 for buy-and-hold, gross of costs and excluding dividends. A long-only trend rule can
> therefore be right about direction most of the time and still lose badly to holding, which is
> exactly what Experiment 1's filter-off benchmark exists to detect.

## Momentum: a 150-day return rule does the same work, so the moving average is not special

- A simpler signal: a buy at t if the price is at or above its level 150 days earlier, a sell
  otherwise — the past 150 days' return in place of the price against its average (p. 9).
- "It is clear that the moving average strategy is not looking for anything more complicated than a
  simple persistence in the returns series" (p. 9).
- Conditional means run side by side (Table 7, p. 9): over the full sample Buy-Sell is 0.061 percent
  (t 4.60) for the moving average and 0.056 percent (t 4.21) for momentum; over 1988–1999(Feb) it is
  −0.048 percent (t −1.12) and −0.122 percent (t −2.55). "The momentum strategy reverses signs as
  does the moving average, but it is actually significantly negative for the buy-sell difference"
  (p. 9).
- The variance ratios track too: Buy/Sell 0.430 for the moving average against 0.442 for momentum
  over the full sample, 0.516 against 0.622 over 1988–1999(Feb) (p. 10, Table 8).
- "These results suggest that these two technical rules may be very similar in practice, and there is
  nothing particularly special or important about the moving average representation" (p. 9).

> **For claim 1:** the paper's "momentum" is absolute, an index against its own past, so it does not
> disturb the objective's line between trend and relative momentum. What it disturbs is the form: if
> a signed 150-day return does the same work, the 50-over-200 crossover is a convention rather than a
> mechanism, and the cheapest control arm for a later experiment is the sign of a single long-window
> return, not another pair of averages.

## Conclusions: the data changed, and the rules were not tuned to the old sample

- The question the paper poses: "Has something about the dynamics of stock prices changed over the
  past 10 years, or was the original trend following strategy mined out of the previous 90 years of
  data?" Sullivan et al. (1999) "suggest that it was a change in the data, since their test attempts
  to adjust for data mining in the previous sample" (p. 10).
- "However, no test for data mining is perfect, as it depends on simulating the snooping process that
  might have been occurring" (pp. 10–11).
- BLL "were careful to use rules that had existed in the technical trading community for some time,
  and did not try to perform any extra parameter tuning over their samples. Some of these rules have
  been in use since the early part of the century." Given they were not tuned, "it looks impossible
  that the past 10 years could be a draw from any 10 year period in the 90 year history" (p. 11).
- Candidate causes: "technology, better price information, and lower transaction costs, or possibly a
  greater attention is now given to technical trading rules"; if traders traded the profits away,
  the volatility side deserves the same study (p. 11).
- The results in BLL "could have been replaced with simpler ones", and "in the nonstationary world
  suggested by these results, robustness may be a far greater virtue than previously thought"
  (p. 11).

> **For claim 1:** the objective's defence — that 50 and 200 were stated, not searched on our data —
> is precisely the defence BLL had, and this paper says it was a good defence that did not keep the
> result alive. So an unsearched parameter buys protection from data-snooping and none at all from
> non-stationarity, and the filter's economic reason has to be one that survives every trader
> knowing the rule.

## What it changes

- Claim 1 stays untested, and its nearest precedent now carries a documented failure out of sample:
  on the Dow the buy-sell difference went from 0.066 percent a day (t 4.73) over 1897–1986 to −0.048
  percent (t −1.12) over 1988–1999(Feb).
- The only effect this paper finds stable is the variance one, so `FINDINGS_1.md` must report
  volatility beside return for the filter-on and filter-off books, not return alone.
- The filter-off benchmark stops being a formality: the rule's long-only arm scored −0.518 against
  0.776 for buy-and-hold in the decade after the study, so beating nothing is not evidence.
- The 50-over-200 form is not privileged by this evidence — a signed 150-day return matched it on
  both means and variances — which makes it a convention to sweep and publish as a curve, not a
  mechanism to defend.
- The strategy's unsearched parameters defend it against snooping only; this paper's whole point is
  that a rule can be clean of snooping and still stop working.
- The figures are gross of transaction costs and exclude dividends, both of which flatter a rule that
  sits in cash against a benchmark that does not.
- It does not settle claim 1 in either direction: it tests one index rather than a cross-section,
  price against a single 150-day average rather than a 50-day against a 200-day, and an index rather
  than the 30 most traded stocks, and its last observation is February 1999. Whether the filter
  separates stocks inside the liquid universe is a question only `Data/analyzer.ipynb` can answer.
