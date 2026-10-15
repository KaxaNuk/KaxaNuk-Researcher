# Known-answer recipes

One recipe per model. Each gives the model, its true parameters, a seed and a size, the estimator
to check, the tolerance and why, and the failure to show. They are prose and formulas, written for
this skill: the notebook is written fresh from them, and no code is copied from anywhere.

**What every recipe shares.**

- **One generator for the main draw**, `numpy.random.default_rng(seed)`, made once. Each
  repetition takes its own seed, in the range the recipe names, and its own generator, made once.
- **Four standard errors** is the tolerance for one number: a correct method misses it by chance
  about once in 16,000 runs, so a raise is the method's and not the draw's. Many numbers checked at
  once take more: z such that 2·m·Φ(−z) is about 1/1,000, for m numbers, as recipe 4 says.
- **A changed size** takes the tolerance's formula again, never the figure printed here. The
  formulas are large-sample ones: a short size takes recipe 1's *At a short length*. A tolerance
  measured over seeded repetitions instead of by a formula — 4's PCA, 6, 7, 8 and 9's AUC — stays
  at the recipe's size for the pass, or is measured again at the new size, over the same seeds,
  before the plan, as *Step 1* of `SKILL.md` says. The band that decides the pass stays clear of
  any bound, below 1 for a persistence, and still catches the recipe's failure.
- **Verify raises unless** each failure misses as its recipe states: outside the tolerance, or past
  the failure's own threshold, which the recipe names.
- **The figures in brackets** — the pass on the recipe's seed, the failure's size — were checked by
  simulation on 2026-10-14, with NumPy 2.5.4, SciPy 1.18.1, scikit-learn 1.9.1 and hmmlearn 0.3.3.
  Another seed draws other numbers and the same picture. They are teaching computations on
  simulated data, never figures about a book, and are never said to the owner: the figures read
  are the notebook's own output, from the owner's run.
- **A source a recipe names** — Kendall (1954), in recipe 1 — is this skill's lead, named in the
  notebook as *a lead from the known-answer skill, not in your library*, and never cited as
  evidence.

## 1 · AR(1): a half-life

- **The model.** x_t = c + φ·x_{t−1} + ε_t, the ε_t independent and normal with volatility σ, and
  |φ| < 1, so the series is stationary. A deviation from the mean, c / (1 − φ), shrinks by φ each
  period; for 0 < φ < 1 it halves in h = ln(1/2) / ln φ periods, and for φ ≤ 0 it flips sign and
  has no half-life.
- **The truth.** φ = 0.95, so h = 13.51 periods; c = 0.01, a mean of 0.2; σ = 0.01. The first value
  is drawn from the stationary distribution — mean c / (1 − φ), variance σ² / (1 − φ²) — so no
  burn-in is needed. A mean far from zero against the series' spread is what lets the check catch
  a missing intercept: least squares without one reads φ̂ near 0.999.
- **Seed and size.** Seed 7; n = 50,000 observations.
- **The estimator.** The owner's: commonly least squares of x_t on x_{t−1} with an intercept, and h
  from φ̂; or a maximum-likelihood AR(1) fit. Checked on φ̂, then on ĥ.
- **The tolerance.** |φ̂ − φ| ≤ 4·√((1 − φ²) / n) = 0.0056, four of φ̂'s large-sample standard
  errors: φ̂ between 0.944 and 0.956. That band puts ĥ anywhere from 12.1 to 15.3, since h bends
  sharply as φ nears 1, so φ̂ is what is checked against the truth and ĥ is checked as a formula:
  Verify raises when φ̂ is not in (0, 1) before a half-life is taken, and when ĥ differs from
  ln(1/2) / ln φ̂ by more than rounding, 10⁻⁹ of it. The common approximation −ln 2 / (φ̂ − 1)
  reads 13.86 at the truth, against 13.51, inside that range: only the formula check catches it.
  (Seed 7: φ̂ = 0.953.)
- **The failure: too few observations.** The same method on n = 60, over 1,000 samples, seeds 1000
  to 1999. Least squares on an AR(1) whose mean is estimated is biased down in a short sample, by
  about (1 + 3φ) / n: Kendall (1954), "Note on Bias in the Estimation of Autocorrelation",
  *Biometrika* 41(3–4). (The median φ̂ is about 0.89 and the median half-life about 5.8 periods,
  under half the truth; about 5% of the samples land inside the band.) Medians, not means, for the
  half-life: a short sample sometimes gives φ̂ ≥ 1, and no half-life at all. Verify raises unless
  the median φ̂ falls outside the band. The prediction to ask for: does a short sample make the
  half-life look longer or shorter?
- **At a short length.** The tolerance above is a large-sample formula, and at the owner's own
  length it can stop checking anything. Once four standard errors reach 1 − φ, that is once
  n ≤ 16·(1 + φ) / (1 − φ), the band on φ̂ crosses 1, the half-life's band has no upper end, and a
  method with no intercept passes; Kendall's bias moves the centre as well. (A half-life of three
  months, φ = 0.794, over 120 months, as the Mathematical Finance course's S03 has it, the mean
  kept at 0.2, c = 0.2·(1 − φ), and σ at 0.01: four standard errors are 0.222 and 1 − φ is 0.206,
  so the band reaches 1.016, and least squares without an intercept, at 0.999, lands inside it in
  all of 1,000 samples, seeds 2000 to 2999.)
  Then one of two routes, said in the plan:
  - **(a) The pass on the long sample.** The recipe's n = 50,000, at the owner's φ, decides the
    pass; the owner's length is used only to show the failure, as the course's own known answer
    does: the middle and the 90-in-100 range of φ̂ and ĥ over 1,000 repetitions, seeds 2000 to
    2999, shown and not checked, beside the recipe's failure at n = 60, which is. (At φ = 0.794
    and 50,000: the tolerance 0.011; seed 7, 0.800; no intercept, 0.999.)
  - **(b) Against the bias, at the owner's length**, for least squares with an intercept, and only
    when n·(1 − φ) is at least 10: the mean φ̂ over 1,000 repetitions, seeds 2000 to 2999, within
    4 × their standard deviation / √1,000 of φ − (1 + 3φ) / n. (At 120 months: the mean 0.762
    against 0.766, the tolerance 0.008; no intercept, 0.999.) The mean of φ̂, which is always
    defined, not its median: Kendall's is a bias of the mean, and the median sits above it (at
    φ = 0.95 and n = 500, by 0.0023, outside a tolerance of 0.0020). Below n·(1 − φ) = 10 the
    first-order bias falls short — at φ = 0.95 and n = 60, by 0.015 against a tolerance of
    0.010 — and another estimator has a bias of its own: both take (a).

  Either way the band that decides the pass stays below 1 and catches a missing intercept; a plan
  whose band does not is changed before the run.

## 2 · Geometric Brownian motion: drift and volatility

- **The model.** dS = μ·S·dt + σ·S·dW, simulated exactly in logs:
  ln S_{t+Δ} − ln S_t = (μ − σ²/2)·Δ + σ·√Δ·Z, each Z an independent standard normal, so no
  discretisation error enters.
- **The truth.** μ = 0.08 and σ = 0.20 a year; Δ = 1/252, a trading day; S_0 = 100.
- **Seed and size.** Seed 11; R = 1,000 paths of T = 10 years, n = 2,520 steps each.
- **The estimators.** σ̂, the standard deviation of the log returns divided by √Δ; μ̂, their mean
  divided by Δ, plus σ̂²/2.
- **The tolerance.** For σ, on the first path: |σ̂ − σ| ≤ 4·σ / √(2n) = 0.011, σ / √(2n) being the
  standard error of a standard deviation from n normal draws. For μ, on the mean over the R paths:
  |mean of μ̂ − μ| ≤ 4·σ / √(T·R) = 0.008. One path's drift has a standard error of σ / √T = 0.063,
  as large as the drift itself, so a drift is checked over many paths, never on one. (Seed 11: σ̂ =
  0.2007 on the first path; the mean of μ̂, 0.082.)
- **The failure: too few years.** One path's drift. (Of the 1,000, about one in four lands within
  0.02 of 0.08.) Sampling the same ten years monthly instead of daily changes nothing: the mean log
  return divided by Δ is (ln S_T − ln S_0) / T, whatever happens in between, so the drift's error
  depends on the years, not on the number of observations. The same check catches the drag
  forgotten: the mean log return read as μ averages μ − σ²/2 = 0.06, outside the tolerance. Verify
  raises unless both hold: fewer than half the single paths within 0.02 of μ, and the drag-less
  estimate outside the tolerance.

## 3 · Regression: a beta

- **The model.** y_t = α + β·x_t + ε_t, with x and ε independent normal draws: a name's daily excess
  return on the market's.
- **The truth.** β = 1.2, α = 0; σ_x = 0.01 and σ_ε = 0.015 a day.
- **Seed and size.** Seed 23; n = 2,520 days. For the standard error, R = 500 samples, seeds 23 to
  522.
- **The estimator.** Least squares with an intercept: β̂, and the standard error it reports.
- **The tolerance.** |β̂ − β| ≤ 4·σ_ε / (σ_x·√n) = 0.12. The reported standard error is right when
  β̂ ± 1.96 standard errors covers β in about 95% of the R samples: between 91% and 99%, since the
  coverage's own standard error over 500 samples is about one point. (Seed 23: β̂ = 1.178; the
  coverage, 95.4%.)
- **The failure: overlapping windows.** A predictive regression with no relation at all, β = 0: the
  21-day forward return, the sum of days t + 1 to t + 21 of daily returns with volatility 0.01, on a
  persistent feature, an AR(1) with φ = 0.98; n = 2,520 days, seeds 5000 to 5499. Consecutive
  windows share 20 days, so the residuals are autocorrelated and the naive standard error is far
  too small. (The naive interval covers β = 0 in about 35% of the samples, and |t| > 2 in about
  65%: a signal found in noise. Newey-West errors with 20 lags bring the coverage to about 87%,
  nearer but still short.) Verify raises unless the naive coverage is under 80%. With a feature
  drawn fresh each day, the naive coverage stays about 95% (97% over 300 samples, seeds 9000 to
  9299): the overlap bites together with the persistence.

## 4 · Factor model: loadings

- **The model.** r_{i,t} = Σ_k B_{ik}·f_{k,t} + u_{i,t}, for N names and K factors: the factors
  normal, with volatilities σ_f and a correlation matrix, their covariance Σ_f; the u_{i,t}
  independent normal with volatility σ_u.
- **The truth.** N = 50, K = 3; σ_f = 0.010, 0.008 and 0.004 a day, factors 1 and 2 correlated 0.6,
  factor 3 with neither; σ_u = 0.015. The loadings are drawn once: B_{i1} uniform on 0.6 to 1.4, a
  market; B_{i2} and B_{i3} uniform on −1 to 1.
- **Seed and size.** Seed 29, drawing the loadings first, then the returns; T = 1,260 dates, five
  years.
- **The estimator, with the factor returns given:** each name's time-series regression on the K
  factors, with an intercept.
- **Its tolerance:** every loading within 4.5 standard errors, σ_u·√((Σ_f⁻¹)_kk / T): 0.24, 0.30
  and 0.48 for the three factors (one standard error each, 0.053, 0.066 and 0.106). The multiplier
  is z such that 2·m·Φ(−z) is about 1/1,000, m = N·K the number of loadings checked: 4.5 at 150,
  about 5.0 at 1,500. At four, with 150 loadings, a correct method would miss somewhere about one
  run in a hundred. (Seed 29: the largest miss, 2.2 standard errors. About one run in 1,000 misses
  somewhere by chance: four of 2,000 seeds, 29 to 2028, each drawing its own loadings.)
- **Its failure: an omitted factor.** The same regression without factor 2. Factor 2 moves with
  factor 1, so factor 1's loading takes up part of it, about 0.6 × 0.008 / 0.010 = 0.48 times
  B_{i2}. (About half the market loadings fall outside the tolerance.) Verify raises unless fewer
  than 90% are inside.
- **The estimator, by PCA,** when no factor returns are given: the first K eigenvectors of the
  returns' sample covariance. A component fixes neither its sign, nor its order, nor a rotation
  among components of similar size, so the check compares spaces, not columns: the smallest cosine
  of the principal angles between the span of B's columns and the span of those K eigenvectors —
  the smallest singular value of Qᵀ·V, Q an orthonormal basis of B's columns and V the
  eigenvectors.
- **Its tolerance:** at least 0.9. (Seed 29's loadings kept and the returns drawn again on seeds
  3100 to 3299, 200 samples at this size: never under 0.93.) A PCA that standardises each name
  first keeps B's span as its truth only when every name's variance is the same: rescale each row
  B_i so that B_i·Σ_f·B_iᵀ is equal across names, σ_u unchanged.
- **Its failure: too few dates.** T = 40, fewer dates than names: the sample covariance is
  singular, and the weakest factor sinks into the noise. (The smallest cosine falls to about 0.3,
  the median over the same 200 seeds.) Verify raises unless the median is under 0.9.

## 5 · A planted signal: its information coefficient

- **The model.** On each of T dates, for each of N names, a score z_{i,t} and a forward return
  y_{i,t}, jointly normal with correlation ρ, independent across names and dates. For jointly
  normal pairs the rank correlation is (6/π)·arcsin(ρ/2), so ρ = 2·sin(π·IC/6) plants a rank IC.
  The signal is reported as s_{i,t} = exp(2·z_{i,t}), skewed as a size is across a broad
  universe: a rank ignores a rising transform, so the planted rank IC stays exact, and a Pearson
  correlation on s does not.
- **The truth.** IC = 0.05, so ρ = 0.0524; N = 500 names and T = 240 dates, twenty years of months;
  z and y of unit variance, since a rank ignores scale.
- **Seed.** 37; repetitions on seeds 37 to 136, each drawing z, then y, then the failure's level.
- **The estimator.** The IC as the analyzer computes it: on each date, the rank correlation between
  the signal and the forward return; then the mean over dates (`data-analyzer-runs`, section 4).
- **The tolerance.** |mean IC − 0.05| ≤ 4 / √((N − 1)·T) = 0.012: one date's rank correlation has a
  standard error of about 1 / √(N − 1), and averaging T independent dates divides it by √T.
  (Seed 37: 0.053; over the 100 seeds, every one inside. A Pearson correlation in place of the
  rank read 0.018 to 0.031, every one outside: the skew is what lets the check tell the two apart,
  since on normal margins a Pearson correlation reads 0.052, inside.)
- **The failure: a pooled rank.** Add a level a_t that moves the whole signal on a date — the same
  for every name, normal with variance 3, as a ratio drifts when the whole market reprices — so
  that s = exp(2·(z + a_t)); then rank the signal and the return once over the whole panel,
  instead of within each date. The per-date IC is untouched, since a shift common to a date
  cancels inside it; the pooled one falls to about IC / √(1 + 3) = 0.025, half the truth. (Over the
  100 seeds, 0.017 to 0.032.) Verify raises unless the pooled value is outside the tolerance and
  the per-date one inside: the analyzer's first rule, per date and never pooled, seen to bite.

## 6 · Clusters with known members

- **The model.** Each name's daily return is λ_i·(m_t + g_{c(i),t} + u_{i,t}): m a market common to
  every name, g_c a factor shared within group c, u the name's own, all three independent normal
  with volatility 0.01. The scale λ_i alternates within each group, 0.5 and 2.0: quiet and loud
  names together.
- **The truth.** Three groups of ten names. The correlation is 2/3 within a group and 1/3 between
  groups, whatever the scales.
- **Seed and size.** Seed 53; T = 500 days; repetitions on seeds 53 to 152.
- **The estimators.** Hierarchical clustering, average linkage, on the distance √(2·(1 − ρ̂)), cut
  at three groups; or k-means on each name's series standardised, with three groups, or with k
  chosen by silhouette among 2 to 6.
- **The tolerance.** The groups are compared as partitions, by the adjusted Rand index, since a
  method's group numbers are arbitrary: at least 0.85. One name of the thirty astray scores about
  0.90 and two about 0.80, so at most one may be. (Both methods placed every name right in all 100
  samples, and the silhouette chose three groups in each of the first 20, seeds 53 to 72.)
- **The failure: raw returns into k-means.** The same k-means on unstandardised returns groups the
  names by how loud they are, not by what they move with. Between standardised series the squared
  distance is 2T·(1 − ρ), the correlation alone; between raw ones, volatility dominates. (The index
  falls to between 0.11 and 0.18.) Verify raises unless the raw k-means scores under 0.5. Too few
  days bites too: hierarchical clustering on the first 20 days of the same 100 samples averaged
  0.82, and fell as low as 0.29.

## 7 · A two-state regime

- **The model.** A hidden state s_t, calm or stressed, follows a Markov chain; the day's return is
  normal with the state's mean and volatility.
- **The truth.** Calm: mean 0.0005 and volatility 0.007 a day; stressed: mean −0.0010 and
  volatility 0.020. The chance of staying is 0.99 in calm and 0.97 in stress, so stress takes a
  quarter of the days in the long run, 0.01 / (0.01 + 0.03). The chain starts calm.
- **Seed and size.** Seed 43; n = 5,000 days, about 75 switches, 0.75 × 0.01 + 0.25 × 0.03 a day;
  repetitions on seeds 4300 to 4329. (76 on average over the 30, 58 to 96.)
- **The estimator.** A two-state Gaussian hidden Markov model fitted by EM — the owner's, or a
  library's — from several starts, the best likelihood kept. The states are matched to the truth
  by their volatility before any comparison: which one a fit calls first is arbitrary. A Gaussian
  mixture ignores persistence, so it is checked on its volatilities and shares only.
- **The tolerance.** One band per parameter, four times the spread of its own error over the 30
  samples: about 5.4% for the calm volatility, 9.5% for the stressed, 0.008 for the chance of
  staying calm and 0.02 for staying stressed. (The spreads, on fits to returns in percent from five
  starts, up to 500 iterations to a tolerance of 10⁻⁶: 1.4%, 2.4%, 0.002 and 0.0055.) Then a check
  over the repetitions: each parameter's mean error over the 30 seeds within four times its spread
  divided by √30 — about 1% for the calm volatility, 1.7% for the stressed, 0.0014 and 0.004 for
  the chances of staying — which catches a bias no single sample can.
- **The failure: a look-ahead.** The state on a date, as a rule could have known it, is the
  filtered probability, from the returns up to that date. With the true parameters it is right on
  most days, and no causal method does better but by chance. (About 95%, 0.936 to 0.962 over the
  30 samples; the method's own filter, with its fitted parameters, came within 0.003 of it every
  time.) The smoothed probability uses the returns after the date as well. (About 98%: at least
  1.8 points above, 2.8 on average.) Verify raises unless the owner's causal state is within one
  point of the true model's filter and the smoothed one more than a point above it: a state better
  than the true model's own filter has seen the future. A library's state probabilities are often
  the smoothed ones — hmmlearn 0.3.3's `predict_proba` scored about 98% over the 30 samples, within
  0.003 of the smoothed probabilities, checked by running it on 2026-10-14 — so read its
  documentation before taking them as what was known on the date.
- **A bias only the average shows.** With hmmlearn 0.3.3's defaults — its prior on the variances,
  `covars_prior`, among them — a fit on daily returns in decimals put the calm volatility 3.1% high
  on average over the 30 samples; the same fit on returns in percent, or with that prior set near
  zero, 0.1%. A single sample's band, 5.4%, lets it through, though it is 2.3 times one sample's
  spread; the check over the repetitions, about 1%, catches it: a reason to run them.
- **The same gap on real data.** On the strategy's own fitted signal, the filtered against the
  smoothed state is the analyzer's section 5 (`data-analyzer-runs`).

## 8 · GARCH(1,1): persistence, long-run variance and a forecast

- **The model.** r_t = σ_t·z_t, each z_t an independent standard normal, and
  σ_t² = ω + a·r_{t−1}² + b·σ_{t−1}², with a, b ≥ 0 and a + b < 1. A shock to the variance decays
  by a + b a day, so it halves in ln(1/2) / ln(a + b) days, and the variance returns to its
  long-run level, v = ω / (1 − a − b).
- **The truth.** a = 0.08 and b = 0.90, so a + b = 0.98 and the half-life is 34.3 days, as in the
  Mathematical Finance course's S03 practice market; v set to a volatility of 0.20 a year,
  v = 0.20² / 252, so ω = v·(1 − a − b) = 3.17 × 10⁻⁶. The recursion starts at v, and the first
  500 days are drawn and dropped.
- **Seed and size.** Seed 61; n = 10,000 days, forty years; repetitions on seeds 6100 to 6299.
- **The estimator.** Gaussian maximum likelihood, the recursion started at the sample variance:
  the owner's own, or a library's. Checked on â, b̂, â + b̂ and the long-run volatility, √(252·v̂),
  then on the half-life as a formula of â + b̂, as recipe 1 checks its own: Verify raises when
  â + b̂ is not in (0, 1).
- **The tolerance.** Four times the spread of each error over the 200 repetitions, since no simple
  formula gives these standard errors: 0.024 for a, 0.031 for b, 0.016 for a + b and 0.033 for the
  long-run volatility. The size is what keeps the band on a + b below 1: at 5,000 days it reached
  1.002, and the long-run variance had no upper end; at 10,000 it stops at 0.995. (Seed 61:
  â = 0.093, b̂ = 0.887, â + b̂ = 0.980, a long-run volatility of 0.202 and a half-life of 34.2
  days.)
- **The forecast, against the truth.** Each day's variance from the fitted parameters and the
  returns before it, set against the true σ_t² from day 251 on: the root mean square of
  σ̂_t² / σ_t² − 1 under 0.062, its mean over the 200 repetitions plus four of their standard
  deviations. An EWMA with λ = 0.94, started at the first 250 days' variance, is scored beside it.
  (Seed 61: 0.037, and the EWMA 0.162. Over the 200, the fit 0.003 to 0.053, the EWMA 0.127 to
  0.172, never under.) The owner's own forecaster — a network, say — is scored the same way, beside
  both; its tolerance is the plan's, since the recipe has not run it.
- **The forecast, as real data allows.** On real data the truth is unknown, and a forecast f_t is
  scored against r_t² by QLIKE, the mean of ln f_t + r_t² / f_t, lower being better. No forecast
  from the returns before the day beats the true variance but by its own fitting noise, at most
  0.0015 for the fit in sample; the EWMA scores 0.007 to 0.016 worse. A forecast that takes in the
  day's own return — the same EWMA with r_t in f_t — scores about 0.1 better, 0.092 to 0.104 over
  the 200 (seed 61: 0.101). Verify
  raises when the owner's forecast scores more than 0.01 better than the true variance: a forecast
  better than the truth has seen the future.
- **The failure: too short a sample.** The same fit on n = 500 days, two years, over 200 samples,
  seeds 6300 to 6499. (29% of the fits land inside all four bands; the half-life runs from 5.1 to
  107 days, 5th to 95th percentile, around 34.3; and 3 of the 200 put â + b̂ at 1, with no
  long-run variance at all.) Verify raises unless fewer than half land inside all four bands. A
  persistence near 1 bites too: with a = 0.05 and b = 0.945, a + b = 0.995, the long-run
  volatility's spread at 5,000 days was 2.4 times its spread at 0.98, over seeds 6500 to 6699, and
  the band on a + b reached 1.005.

## 9 · A logistic classifier: coefficients, AUC and calibration

- **The model.** Three features, independent standard normals, and a label y, 1 or 0, with
  P(y = 1 | x) = 1 / (1 + exp(−(β₀ + β·x))).
- **The truth.** β = (1.0, −0.5, 0.0), the third a feature with no effect; β₀ = −2.647, set so the
  base rate is 10%. The true score, β₀ + β·x, ranks better than any other; its AUC is about 0.772,
  by numerical integration.
- **Seed and size.** Seed 71; n = 20,000 to fit, then 20,000 more to test: the features of all
  40,000 drawn first, then their labels, the first 20,000 rows fitting; repetitions on seeds 71 to
  270.
- **The estimator.** The owner's: commonly logistic regression by maximum likelihood, with an
  intercept and no penalty. A library's default may add one — scikit-learn's `LogisticRegression`
  is penalised, C = 1.0, which moved the coefficients by about 0.001 at this size, well inside the
  tolerance, though not at a small n — so read its documentation.
- **The tolerance.** Each coefficient within four standard errors, the square roots of the
  diagonal of I⁻¹ / n, with I = E[p·(1 − p)·x̃·x̃ᵀ] at the truth and x̃ the features with a 1 for
  the intercept: 0.033 for β₀, then 0.028, 0.026 and 0.025, so bands of 0.13, 0.11, 0.10 and 0.10.
  The AUC, on the test draw, no more than 0.002 below the true score's on the same draw: the true
  score ranks best, so a fit can only lose. Calibration: the test draw cut into ten bins of 2,000
  by predicted probability, each bin's share of positives within five binomial standard errors,
  √(p̄·(1 − p̄) / 2,000), of its mean predicted probability p̄; five, not four, since ten bins are
  checked at once and the fitted coefficients add their own error. (Seed 71: −2.660, 1.024, −0.521
  and 0.042; the AUC 0.7707 against the true score's 0.7713; the worst bin 2.3 standard errors
  out. Over the 200: the largest coefficient miss 2.9 standard errors, the AUC at most 0.001 below,
  the worst bin 4.0.)
- **The failure: the base rate ignored**, two ways. Accuracy read as skill: at a threshold of 0.5
  the fit is right on about 90.2% of the test draw, and the rule that always says no on 90.0%, so
  accuracy cannot tell an AUC of 0.77 from one of 0.5. (Over the 200, the fit's accuracy was
  within 0.4 points of always no.) Probabilities from a balanced fit — class weights that make the
  two classes count equally, as scikit-learn's `class_weight="balanced"` does, or a resample to
  half and half: the slopes come back the same but for sampling noise, within 0.04 over the 200,
  and the intercept moves up by about ln(0.9 / 0.1) = 2.20, so the ranking and the AUC stay and
  every probability is too high. (The
  mean predicted probability about 0.41 against a base rate of 0.10; the worst bin 49 to 59
  standard errors out.) Verify raises unless the balanced fit's AUC passes and its calibration
  misses, and unless always no comes within one point of the fit's accuracy: a classifier can rank
  and still not give probabilities, and accuracy says neither.
