# Blueprint — Experiment 1

> **The hypothesis, fixed once written.** Thesis, rules, predictions, success criteria and key
> risks, recorded *before* any code runs.
>
> **This file does not change when results arrive.** A hypothesis edited after its test is no longer
> a hypothesis — that is the whole reason it is kept apart from the result. What the experiment
> actually produced is in [`FINDINGS_1.md`](FINDINGS_1.md); planning lives in
> [`BRAINSTORMING_1.md`](BRAINSTORMING_1.md), the running log in [`JOURNAL_1.md`](JOURNAL_1.md).
>
> Record the date it was written, and delete this blockquote.

---

## Experiment 1 — the declared benchmark

<!-- example: begin -->

**Written 2026-09-19, after step 3 and before any rule was coded.** `liquid-golden-cross`.

<!-- example: end -->

### Thesis

One paragraph: what book this rule produces, and why it is a fair yardstick — sensible, liquid,
low-complexity — for judging whether any later idea adds value. **Be modest on purpose.** The
benchmark does not assert its signal is the best of its kind, only that it is simple enough to be
understood, liquid enough to be traded, and stable enough to measure other things against.

<!-- example: begin -->

Own the thirty most traded US stocks whose fifty-day average price sits above their two-hundred-day
average, equally weighted, and hold a short-Treasury fund in any slot no stock qualifies for. The
book this produces is a large, liquid, long-only equity portfolio that steps out of a name when its
trend turns and steps back when it returns. It is a fair yardstick for three reasons and no others:
it has four moving parts and no optimiser, so a later idea's contribution cannot hide in it; every
position is in one of the most heavily traded stocks in the United States, so it could be held at
size; and its signal is slow, so the book is stable enough to measure other things against. **It
asserts nothing about being the best trend rule.** Step 3 has already measured the signal's
information coefficient at 0.0112 over a month and −0.0060 over a year, which is not the profile of
a return engine, and the thesis is written knowing that.

<!-- example: end -->

### Rules

- **Selection:** the eligibility condition, naming the column it reads.
- **Sizing:** the weighting scheme. Say which constraints are switched off, and that each one is a
  lever a later experiment has to earn.
- **Cash:** where the uninvested residual goes — a real, priced instrument, because the engine's
  weight file has no cash row.
- **Timing:** calendar, or event-driven on a stated trigger. Say what happens between triggers.
- **Lag:** how many days between the signal and the fill, and what the engine adds on top.
- **Screens deliberately absent**, and why each is redundant under the rules above.

<!-- example: begin -->

- **Selection:** a security is eligible on a date when `r_trend_50_200` is above zero — its 50-day
  simple moving average above its 200-day, both on the dividend-and-split adjusted close. Of those,
  the thirty with the highest `r_liquidity_rank`, the per-date percentile of average daily traded
  value over 63 days, are held. In the point-in-time window a security must also be in the index
  that day, from its published daily holdings; in the long window, where no dated membership
  exists, the list is the seed throughout — a survivorship caveat, not a second result.
- **Excluded by name:** `MIC`, which has no price file, and `CIT`, `FMC`, `LCI` and `PARA`, whose
  adjusted prices multiply by more than six in a single day. That is a bad print rather than a
  return, and it would inflate a 200-day average for a year. All five are blocking rows in
  `Universe/Data_Issues.csv`.
- **Sizing:** equal weight, one thirtieth each. Every constraint is switched off: no maximum weight,
  because one thirtieth is already the cap; no risk model; no sector limit. **Each is a lever a
  later experiment has to earn by beating this book without it.**
- **Cash:** the uninvested residual buys `SHY`, a short-Treasury fund, priced like any other
  holding. The engine's weight file has no cash row, so cash that is not an instrument is cash that
  pays no commission and earns no yield — neither of which is true in life.
- **Timing:** event-driven. The target book is recomputed every trading day, and a rebalance fires
  only when moving to it would trade at least **10% of the book** — three names of thirty at equal
  weight, with price drift counted. Between triggers nothing is traded and the weights drift with
  prices.
- **Lag:** the eligible set used on date *t* is the one observed at *t−1*, applied in
  `portfolio_construction.lag_eligibility`. The engine fills at the next trading day's VWAP on the
  total-return basis and charges commission on the unadjusted VWAP, so the signal and the fill are
  never the same price.
- **Costs, stated rather than defaulted:** 0.1 cents per share of commission, which is the engine's
  ceiling, plus 5 basis points of slippage. Results are read net.
- **Window:** the point-in-time run is 2017-01-03 to 2026-06-01, which is where the index's own
  holdings begin. The long run is 2002-01-02 to 2026-06-01 on the fixed list; the universe is deep
  enough to fill the book from 2001-10-22, and 265 of the 788 have no prices at its start.
- **Screens deliberately absent:** no market-cap screen, because ranking on traded value already
  selects large companies; no sector cap, because the concentration a top-thirty-by-volume book
  carries is a property to measure in step 6 rather than a thing to constrain before it is seen;
  no volatility screen, because step 3 shows the trend filter is already one.

<!-- example: end -->

### What this experiment should show

**Predictions, fixed before the run.** Each should come from `Data/analyzer.ipynb`, which measures
the signal but builds no book. Getting these right is worth more than a good Sharpe; getting them
wrong is worth more than a bad one.

| # | Prediction | Where it comes from | What would falsify it |
| --- | --- | --- | --- |
| 1 | what the book should do | a `Bibliotheca/` note, or the analyzer section and its number | the observation that would refute it |

Note anything you are watching but cannot predict, because nothing licenses a prediction about it.
Costs usually belong here.

<!-- example: begin -->

**Predictions, fixed before the run.**

| # | Prediction | Where it comes from | What would falsify it |
| --- | --- | --- | --- |
| 1 | The book's annualised volatility is **below the index's**, by a visible margin rather than a rounding | analyzer section 5: forward 21-day volatility 28.7% when the 50-day is above the 200-day, 36.7% when it is below, on 208,111 observations | the book's annualised volatility at or above the index's over the shared window |
| 2 | The book does **not** beat the same thirty names without the filter by more than **1 percentage point a year, net** | analyzer section 4: information coefficient 0.0112 at a month, 0.0027 at a quarter, −0.0060 at a year | a filter-on book beating filter-off by more than 1 point a year net |
| 3 | Maximum drawdown is **shallower than the index's** | [LeBaron (1999)](../../Bibliotheca/Papers/LeBaron_1999_The_Stability_Of_Moving_Average_Rules.md): buy-period variance is 43% of sell-period variance over the full sample and 52% in the last decade | a drawdown as deep as or deeper than the index's |
| 4 | The book's **worst stretch relative to the index is a rebound**, not a decline | [LeBaron (1999)](../../Bibliotheca/Papers/LeBaron_1999_The_Stability_Of_Moving_Average_Rules.md), whose long-only arm scored −0.518 against buy-and-hold's 0.776 in a decade it was in its buy state 81% of the time; a 200-day average turns late | the book's worst relative stretch falling in a market decline instead |
| 5 | Step 6 shows a **positive momentum loading that is not the filter's own doing**, and a beta below one | [Paleologo (2021), ch. 5](../../Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/09_Understand_Factors.md): a book of winners acquires momentum loading without trading it | a momentum loading at or below zero, or a beta at or above one |
| 6 | The filter **spends time in cash** in 2008–09 and early 2020, and that cash is where the drawdown difference comes from | the rule itself: fewer than thirty names qualify when most trends are down | the book fully invested throughout both episodes |

**Watched, but not predicted.** Turnover and total cost: the band's trigger count depends on how
often the top thirty churns, which nothing measured so far licenses a number for. The count, the
realised turnover and the cost drag are reported in `FINDINGS_1.md` whatever they are.

<!-- example: end -->

### Success criteria

As the benchmark, Experiment 1 does not need to win. It needs to be a **fair, stable yardstick**:

1. Reproducible from a clean clone, through the pipeline, with no manual step.
2. A tradeable trigger frequency — not a rule that fires every day.
3. Net-of-cost results reported against every benchmark it declares.
4. Every prediction above evaluated explicitly in `FINDINGS_1.md`, **including the ones that turn
   out wrong.**

**Graduation: not applicable.** The benchmark's job is to be the thing others are measured against,
so it stays in the Lab even if it scores well.

### Key risks

- **Survivorship and point-in-time integrity.** The universe must include delisted names; step 2
  quantifies how many.
- **The signal's known weakness** — slow exits, whipsaw, regime dependence — accepted here on
  simplicity grounds and attacked in a later experiment.
- **Concentration.** How the weighting concentrates, and which diagnostics measure it.
- **The signal may not be what earns the return.** If the book beats its benchmarks because of a
  factor exposure rather than the signal, the honest product is a cheaper factor fund. That is what
  step 6 exists to answer.

<!-- example: begin -->

Specifically, here:

- **Survivorship.** The seed keeps its 82 delisted names, and the engine sells a delisted position
  at its last price — the one deliberate look-ahead this process admits to, because nobody knows a
  price is the last one. The long window is worse than that: with no dated membership before 2017
  it holds the 2017–2026 list throughout, so companies that died before 2017 are absent and
  companies that listed later are present from the start. **Every figure from the long window
  carries that caveat, and the point-in-time window is the one that counts.**
- **Whipsaw, which is this signal's known weakness.** A 200-day average turns late in both
  directions; prediction 4 is where it is expected to cost the most.
- **Concentration.** Thirty equally weighted names drawn from the most traded end of the market
  will lean towards technology and towards large companies. The effective number of names and the
  sector shares are reported in `FINDINGS_1.md` rather than constrained here.
- **The filter may not be what earns anything.** Step 3 has already said the signal is closer to a
  volatility sorter than a return predictor. If the book looks good, prediction 2 and the
  filter-off comparison are what decide whether the filter did it — and step 6 decides whether a
  factor did.
- **One provider, and its errors.** Five securities are excluded by name for missing or impossible
  prices. Four of them were found only because the analyzer looked; a sixth of the same kind would
  be found the same way, which is not a guarantee.

<!-- example: end -->

### Open questions this experiment deliberately does not answer

Each is a later experiment, and each has to beat this one.

<!-- example: begin -->

| # | Question | Why it is not answered here |
| --- | --- | --- |
| 1 | Does the **sign of a 150-day return** do the same work as the crossover? | [LeBaron (1999)](../../Bibliotheca/Papers/LeBaron_1999_The_Stability_Of_Moving_Average_Rules.md) gets the same means and variances from it, which would make the 50/200 form a convention rather than a mechanism. The cheapest control arm there is |
| 2 | Does **skipping the most recent month** improve the signal? | [Paleologo (2021), ch. 5](../../Bibliotheca/Books/Paleologo_2021_Advanced_Portfolio_Management/09_Understand_Factors.md) puts a reversal in the zero-to-one-month window, which the 50-day average includes |
| 3 | Is **10%** the right band? | It was chosen as a round number. A sweep read as a curve, with the trial count published, is a later experiment. Grinold & Kahn's chapters 14 and 16 are the theory it would be read against, and they are still a lead with no note, so nothing may be claimed on them here |
| 4 | What does the **liquidity ranking cost** in return? | Claim 3 of `OBJECTIVE.md` says it is expected to cost rather than add; measuring it means varying the cut, which changes the book |
| 5 | How much is **survivorship worth**, in this book, in this sample? | The same rule on the survivors only, against this run, would price the bias rather than suffer it — and would be runnable by anyone on free data |

<!-- example: end -->
