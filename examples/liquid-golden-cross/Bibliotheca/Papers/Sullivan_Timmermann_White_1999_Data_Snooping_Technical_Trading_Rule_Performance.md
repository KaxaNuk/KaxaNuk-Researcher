---
source: The Journal of Finance, Vol. LIV, No. 5, October 1999, pages 1647–1691
citation: "Sullivan, R., Timmermann, A., & White, H. (1999). Data-Snooping, Technical Trading Rule Performance, and the Bootstrap. The Journal of Finance, LIV(5), 1647–1691."
local_copy: Bibliotheca/Papers/Sullivan_Timmermann_White_1999_Data_Snooping_Technical_Trading_Rule_Performance.pdf
read: 2026-09-19, the whole paper
---

# Sullivan, Timmermann & White (1999) — Data-Snooping, Technical Trading Rule Performance, and the Bootstrap

*The whole paper, from the extract: the abstract, sections I to VI and Appendix A. Appendices B and C
— White's propositions and the stationary bootstrap algorithm — were read and are not carried. Page
numbers are the extract's, the PDF's 1–45; the journal prints those pages 1647–1691.*

## Why it is here

Claim 1 of [`OBJECTIVE.md`](../../OBJECTIVE.md) — *among the most traded US stocks, those whose
50-day average is above their 200-day go on to earn more than those whose is not.* The objective
names this paper as the source **against** the claim: on whether moving-average rules survive the
search that found them, and the years after it. Its companion here is
[LeBaron (1999)](LeBaron_1999_The_Stability_Of_Moving_Average_Rules.md), which reaches the same
verdict from different data.

## Data-snooping is a survivorship bias across the rules investors tried, not one researcher's sin

- Data-snooping occurs when a set of data is used more than once for inference or model selection;
  any satisfactory result may then be due to chance rather than to merit in the method (p. 2).
- Jensen and Bennington (1970) called it selection bias: "given enough computer time, we are sure
  that we can find a mechanical trading rule which 'works' on a table of random numbers—provided of
  course that we are allowed to test the rule on the same table of numbers which we used to discover
  the rule" (quoted, p. 2).
- It "need not be the consequence of a particular researcher's efforts". Investors experiment over
  time across thousands of parameterizations; rules that happen to perform well receive more
  attention and become "serious contenders", unsuccessful ones are forgotten, and after a long
  sample only a small surviving set is cited as evidence of its own merits (pp. 2–3).
- Hence handling snooping by restricting attention to a small subset of rules "may not work in
  practice": the rules a prudent researcher inherits are the ones textbooks and the financial press
  promote, so "the financial community may effectively have acted as such a 'filter'" (p. 8).
- Brock, Lakonishok & LeBaron acknowledged this themselves: "numerous moving average rules can be
  designed, and some, without a doubt, will work. However, the dangers of data snooping are immense"
  (quoted, p. 2).

> **For claim 1:** `OBJECTIVE.md` defends the 50/200 pair by saying neither number was searched on
> our data. This section says that is not the defence it looks like — the pair reaches us already
> filtered, by a century of investors discarding windows that did not work — so claim 1's honest
> trial count does not start at one, and the blueprint should say the pair was inherited rather than
> chosen.

## The Reality Check p-value judges the best rule against the full universe it was drawn from

- White's (1999) Reality Check evaluates the distribution of a performance measure "giving
  consideration to the full set of models that led to the best-performing trading rule" (pp. 4–5).
- The null is that the best rule's performance is no better than the benchmark's. Taking the maximum
  over all *l* rules, "the Reality Check p-value incorporates the effects of data-snooping from the
  search over the *l* rules" (p. 6).
- The nominal p-value applies the same bootstrap to the best rule alone, ignoring the search; the
  difference between the two "will represent the magnitude of the data-snooping bias" (p. 13).
- No parameters are estimated: the parameterizations generate returns directly. On the full DJIA
  sample the number of daily predictions is 27,069. Signals take three values: 1 long, 0 neutral —
  out of the market — and −1 short (p. 5).
- The resampling is Politis and Romano's (1994) stationary bootstrap, 500 resamples, with a mean
  block length of 10; the results are not sensitive to that choice (p. 6, p. 44).

> **For claim 1:** the number this method produces cannot be computed for a single rule, which is
> what we run, but its accounting can be copied — when a later experiment sweeps the two windows,
> `AGENTS.md`'s requirement to publish the trial count is the same discipline in cheaper form, and a
> nominal p-value on the winning window is the number this paper says not to believe.

## The universe is 7,846 rules, and it spans a far larger space than the 26 it was built around

- 7,846 parameterizations drawn from previous academic studies and the technical analysis
  literature: filter rules, moving averages, support and resistance, channel breakouts and
  on-balance volume averages (p. 8). To be included, a rule "must have been in use in a substantial
  part of the sample period" (p. 9).
- Counts by family: filter rules 497, moving averages 2,049, support and resistance 1,220, channel
  breakouts 2,040, on-balance volume 2,040 (pp. 39–40).
- Moving-average windows are n = 2, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 125, 150, 200, 250, with
  105 fast–slow combinations, eight band values, four time-delay values and four holding periods
  (p. 39). Nine further rules pair a fast average of one, two or five days with a slow average of
  50, 150 or 200 days, so that the universe "encompass[es] all of BLL's trading rules" (p. 39).
- The benchmark for the mean return criterion is the "null" system, always out of the market; for
  the Sharpe ratio it is the risk-free rate, which the rules earn on neutral days (pp. 11–12).
- Span: the BLL universe's eigenvalues drop below 1.0 × 10⁻⁵ after only 11, while a 500-rule sample
  of the full universe keeps 196 above it — and "the data-snooping adjustment only accounts for
  snooping within the space spanned by the included rules" (p. 12).

> **For claim 1:** our rule's exact form, a 50-day fast average crossing a 200-day slow one, is one
> of the 105 fast–slow combinations inside this universe, but it is never reported on its own, so no
> p-value here is ours. The last bullet is the standing caution for any sweep we publish: an
> adjustment covers only the rules actually enumerated.

## In the 1897–1986 sample the best rules beat the benchmark after the adjustment, and the winners are the long moving averages

- "the results of BLL appear to be robust to data-snooping, and indeed there are trading rules that
  perform even better than the ones considered by BLL" — valid in all four subperiods (p. 37).
- Over 1897–1996 the best rule in the BLL universe is a 50-day variable moving average with a 0.01
  band at 9.4 percent annualized, Reality Check p-value 0.000; over the original 90 years, 10.11
  percent, p-value 0.000 (p. 13, p. 17).
- Subperiods 1 to 4, BLL universe, mean return with the Reality Check p-value: 9.52 (0.021), 13.90
  (0.000), 9.46 (0.000), 7.87 (0.004). The full universe's best: 16.48, 20.12, 25.51, 23.82, all
  0.000 (p. 17).
- "The BLL study identifies trading rules based on long moving averages (50-, 150-, and 200-day
  averages) as the best performers, but in the full universe of trading rules, the best-performing
  trading rules use much shorter windows of data typically based on two- through five-day averages"
  (p. 13).
- On the Sharpe ratio over 100 years, buy-and-hold returns 0.034, the best BLL rule 0.39 and the best
  full-universe rule 0.82 — but "the best model chosen from the BLL universe does not appear to be
  significant in several of the sample periods": subperiod 1 p = 0.147, subperiod 4 p = 0.051
  (p. 23, p. 24).

> **For claim 1:** in sample, the family claim 1 belongs to worked, and the windows that won are the
> ones our rule uses. Two gaps stop that being support: the comparison is against cash on one index,
> not against the same names with the filter off, and the rules are free to go short.

## A rule pickable in advance earns less, and the best rule's edge is 0.27 percent a trade

- The authors build a recursive rule that each day follows the signal of the rule with the greatest
  cumulative wealth to date, so "at each point in time only historically available information is
  exploited" (p. 21).
- Over 100 years it returns 14.9 percent against the ex post best rule's 17.2 percent, "reflecting
  the fact that investors could not have known ex ante the identity of the ex post best-performing
  trading rule" (p. 21).
- The best rule over 100 years, the five-day simple moving average, makes 6,310 trades averaging 4.3
  days and 0.29 percent each; long and short trades are balanced in number, but "the winning
  percentage is much higher for the long than for the short trades" and long trades earn "more than
  twice as large" an average profit — 0.39 against 0.19 percent (pp. 21–22).
- 6,310 trades over 100 years is 63.1 a year, giving "a break-even transaction cost level of 0.27
  percent per trade"; the authors cannot assess that number historically and say costs were likely
  higher early in the sample and lower by its end (p. 30).

> **For claim 1:** the half of these rules that earned least is the half a long-only book does not
> run, which is a reason claim 1 might survive where the paper's rules did not — and a prediction to
> write into `BLUEPRINT_1.md` rather than an assumption. The 0.27 percent break-even is what a
> daily-trading rule must clear; the 10 percent band exists to keep us far from that arithmetic, and
> `AGENTS.md` still wants the answer net.

## Implementing each signal one day late removes most of the return

- Closing prices may be stale, so following Ready (1997) the authors let a signal observed on day t
  be implemented on day t + 1, and rerun the bootstrap over the full universe and the 100-year
  sample (pp. 27–28).
- The best rule under delay is a variable moving average with a two-day fast average, a 75-day slow
  average and a 0.001 band; "the best rules in this experiment are of a longer duration than those
  where the trading signals are implemented immediately" (p. 28).
- Its mean return is 7.8 percent with a Reality Check p-value below 0.002 — "far less than the best
  from the standard experiment of 17.2 percent" (p. 28).
- Under the Sharpe ratio the best delayed rule scores 0.34 with a Reality Check p-value of 0.26,
  "suggesting that the best rule, according to the Sharpe ratio criterion, is no longer
  significant"; Ready (1997) finds price slippage accounts for a substantial part of these profits
  (p. 28).

> **For claim 1:** this is the result that touches our implementation directly, because the rule is
> struck on shifted data and fills at the next available price — the same one-day delay that cost
> this paper's best rule more than half its return and all of its Sharpe significance. The
> blueprint's prediction for the filter must be the delayed number, and the forward-return cut in
> `Data/analyzer.ipynb` has to be lagged the same way or it measures a book we cannot trade.

## Out of sample, 1987–1996 and the S&P 500 futures, nothing survives the adjustment

- The original data end in 1986, leaving a genuine 10-year postsample of 3,291 days; Lo and
  MacKinlay (1990) recommend exactly such an experiment (p. 29, p. 37).
- "The probability that the best-performing trading rule did not outperform the benchmark during
  this period is nearly 12 percent, suggesting that, at conventional levels of significance, there
  is scant evidence that technical trading rules were of any economic value during the period
  1987–1996" (p. 3).
- In 1987–1996 the BLL universe's best rule by mean return is a 200-day variable moving average with
  a 0.01 band: 8.63 percent, Reality Check p-value 0.154 against a nominal 0.055. The full
  universe's best is a filter rule at 14.41 percent, Reality Check p-value 0.341 against a nominal
  0.004 (p. 15, p. 17).
- On the Sharpe ratio the same period gives 0.28 with p = 0.721 for the BLL universe and 0.87 with
  p = 0.903 for the full universe (p. 24).
- "The five-day moving average rule selected from the full universe produces a mean return of 2.8
  percent with a nominal p-value of 0.322 for the period 1987 to 1996, indicating that the best
  trading rule, as of the end of 1986, did not continue to generate valuable economic signals in the
  subsequent 10-year period" (p. 30).
- On S&P 500 futures, 1984–1996, where costs are modest and shorting easy, the full universe's best
  rule earns 9.43 percent with a nominal p-value of 0.04, "but the fact that this trading rule is
  drawn from a wide universe of rules means that its effective data-snooping-adjusted p-value is
  actually 0.90"; on the Sharpe ratio the pair is 0.987 against 0.000 (p. 17, p. 24, p. 32).

> **For claim 1:** this decade is the closest thing in the literature to a fair test of the family
> claim 1 belongs to, and the rule the BLL universe selects in it is the 200-day average — ours, one
> leg of it. It came back insignificant once the search was counted, so the prior for claim 1 before
> we measure anything should be that the filter earns nothing, and `FINDINGS_1.md` has to report the
> filter-off comparison whichever way it falls.

## Three readings of the out-of-sample failure, one of them that the market changed

- The results "are completely reversed" out of sample and "the best-performing trading rule is not
  even statistically significant at standard critical levels" (p. 37).
- First reading: the out-of-sample period may not be representative, possibly because of 19 October
  1987. The authors resist it — the period is long, the results are robust to excluding 1987, and a
  one-day move of that size would if anything help, since some rules were short and earned 22
  percent in a day (pp. 37–38).
- Second: the 7,846 rules may themselves be a selection from a larger universe, biasing the adjusted
  p-value toward zero — but only if the omitted rules both fail to improve on the best rule and
  generate payoffs largely orthogonal to those included (p. 38).
- Third: "historically, the best technical trading rule did indeed produce superior performance,
  but ... more recently, the markets have become more efficient and hence such opportunities have
  disappeared" — matching cheaper computing power, lower transaction costs and increased liquidity.
  Ready (1997) reports a decline in these rules' predictive ability over 1990–1995 (p. 38).

> **For claim 1:** the third reading is the one that bites, because our universe is the 30 most
> traded US stocks — the names where cheaper computing, lower costs and deeper liquidity went
> furthest — and our data begins long after 1996. If the effect decayed, we are sampling the decayed
> end of it, and a filter-on book beating a filter-off book would be the surprise.

## What it changes

- Claim 1's trial count does not start at one. The 50 and 200 arrived pre-filtered by the investment
  community (pp. 2–3, 8), so `OBJECTIVE.md`'s line that nothing was searched on our data stops being
  a defence and becomes a fact to disclose.
- The prior on claim 1 moves against it. The nearest reported rule to ours, the 200-day variable
  moving average with a 1 percent band, is insignificant out of sample once the search is counted
  (p. 15, p. 17).
- The blueprint's prediction must be for the delayed signal, not the immediate one: a single day of
  implementation lag took the best rule from 17.2 to 7.8 percent and ended its Sharpe significance
  (p. 28).
- Being long-only is now a stated reason claim 1 might survive where these rules failed — the long
  trades won more often and earned more than twice the short trades (pp. 21–22) — and a prediction,
  not an assumption.
- The decay reading (p. 38) applies hardest to the most traded names, so the blueprint should predict
  a weaker filter in the recent sample than in any historical study, and `FINDINGS_1.md` should read
  the filter's return across subperiods rather than as one number.
- Costs are on the band's side but not settled: 0.27 percent break-even at 63 trades a year (p. 30)
  is the arithmetic a daily-trading rule faces, and ours trades far less.
- It does not settle claim 1: the paper never reports a 50-day-over-200-day crossover on its own,
  never applies a rule to a cross-section of stocks, and never uses a filter-off book as its
  benchmark — its benchmark is cash, on one index and one futures contract. Its p-values are not
  claim 1's, and claim 1 stays **untested**.
