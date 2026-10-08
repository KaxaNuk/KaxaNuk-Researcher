# Findings — Experiment 1

> **Latest valuable results only.** This file is rewritten when a result changes, not appended to —
> the running history is in [`JOURNAL_1.md`](JOURNAL_1.md), and the hypothesis this tested is in
> [`BLUEPRINT_1.md`](BLUEPRINT_1.md).
>
> **[`../../RESULTS.md`](../../RESULTS.md) is compiled from this file.** When a finding here
> changes, change it here first, then update the summary.

## Status

**Until the first run, *Not yet run*.** After it: one line saying whether the rule beat the
benchmark and its control by what the blueprint required, and whether it is a candidate for the
gate in `Paper_Trading/BITACORA.md` — a success is necessary for graduation, not sufficient.
Then **the claim it moved**: the claim of `OBJECTIVE.md` the blueprint named, and the status it
reached — or why it reached none.

<!-- example: begin -->

**Experiment 1 ran end to end on 2026-10-06, from a wiped working copy, and passed criteria 1 to 4
of the gate written before the run, and the owner signed criterion 5 the same day.** On
2015-01-02 to 2026-06-01, net of costs, the most-traded KN US Equity Core members in a golden cross,
weighted by traded value inside a 20% cap and a 1% floor, **compound at 20.33% a year at a Sharpe
of 0.842 and a worst drawdown of −32.5%**, against **19.73%, 0.763 and −46.3%** for the same rule
with the cross removed, and **13.05% and 0.713** for the KN US Equity Core and **13.49% and 0.743**
for `SPY`. The rule leads its control by **+0.080 of Sharpe and +0.60 points of CAGR**, where the
blueprint required +0.03 and +0.5, and beats it on both measures in **2 of 3** sub-periods — 2015
to 2018 and 2019 to 2022 — while the control wins 2023 to 2026.

**The claim it moved: claim 1 of `OBJECTIVE.md`, the signal, is confirmed as a book** on the KN US
Equity Core, 2015 to 2026, because predictions 1 and 4 both held, as the blueprint's table fixes.
**Claim 2, the sizing, is confirmed as a book**: prediction 3 held — traded-value weighting beats
the same names equally weighted, 0.842 against 0.722 — and so did prediction 4. Claim 3 is true by
construction and is measured only through claim 1's control. None of the three is out of sample.

**The success criteria `BLUEPRINT_1.md` set, each answered.**

| # | Criterion | State |
| --- | --- | --- |
| 1 | Beats the KN US Equity Core and `SPY` on Sharpe, and its control by +0.03 Sharpe and +0.5 points of CAGR over the window and on both measures in 2 of 3 sub-periods | **Met.** 0.842 against 0.713 and 0.743; +0.080 and +0.60 over the control; 2015–2018 and 2019–2022 to the rule, 2023–2026 to the control |
| 2 | Reproducible from a wiped working copy, with no manual step beyond `SETUP.md`'s drop-in of the Analytics Factory's files | **Met.** Every gitignored output of the earlier version was moved aside before the run; the seed, the download, the universe, the refinery, the analyzer and this notebook ran headless end to end, and the notebook reached the end of its Verify section, 113 checks |
| 3 | Re-strikes on no more than four trading days in five | **Met.** 1,381 of 2,869 trading days, 48.1% |
| 4 | Every prediction and lead reported, including the wrong ones | **Met.** Three predictions and five leads, below |

**No rule, check or engine run of this experiment read a price after 2026-06-01.** The notebook
cuts every matrix there; the download through 2026-10-05 serves the paper book alone.

**Where each figure comes from.** The engine's and the attribution library's figures are the run's
saved tables, `Backtest/` and `Attribution/`. The book's shape — rebalance dates, holdings,
effective positions, the largest weight, how often a cap binds, turnover and the sector drift — was
recomputed on 2026-10-07 from the engine's weight files, and every figure agrees. The
reconciliation's two levels, the coverage by year, the capacity bounds and the misaligned pass are
as the notebook printed them on 2026-10-06; its outputs are not kept.

### The gate, row by row

Every row is evidenced from this file and from `RESULTS.md`, as the gate in
`Paper_Trading/BITACORA.md` requires. Criterion 5 is the owner's.

| # | Criterion | Verdict | Evidence |
| --- | --- | --- | --- |
| 1 | Beats the benchmarks **and its own control** | **Passes** | Sharpe 0.842 against the KN US Equity Core's 0.713, `SPY`'s 0.743 and the control's 0.763; CAGR margin +0.60 points over the control; the control beaten on both measures in 2015–2018 (9.02% and 0.530 against 7.86% and 0.468) and 2019–2022 (16.82% and 0.619 against 9.05% and 0.295), not in 2023–2026 (40.44% and 1.483 against 51.85% and 1.830) |
| 2 | Idiosyncratic alpha in **both** layers | **Passes; every limb positive, none large** | The precondition holds: the first cut's benchmark earns 14.85 points a year against the index's own 14.31, a gap of 0.54 inside the 1.0 tolerance. First-cut selection +17.44 points over the window, per asset as the library computes it; the factor model's idiosyncratic return +13.84 points; the third pass's selection +2.70 points; the idiosyncratic return above all 20 random books, every one of them negative, −84.50 to −3.77. The interaction term, not selection, carries most of each Brinson-Fachler pass: 77.05 of 96.87 points in the first, 40.67 of 43.71 in the third |
| 3 | Survives perturbation; trial count published | **Passes, at its bar** | 6 of the 8 settings keep the sign of the margin over their own control on both Sharpe and CAGR — the bar was 6 — and all 8 beat the KN US Equity Core on Sharpe; the two that do not are the cross's other pairs, 20/100 and 100/300, both ahead on Sharpe and behind on CAGR. The trial count: 107 books. The deflated Sharpe was not computed |
| 4 | Costs and capacity modelled and stated | **Met, capacity as a participation bound** | Turnover 3.09 times the book a year, one way, target to target; commission $97,180 and slippage $101,621 at the headline row; at the realistic commission setting the CAGR is 20.75% and the Sharpe 0.860. Capacity: at 1% of a name's 63-day traded value, $238.6 million for the worst trade, $360.1 million at the 1st percentile, $39.5 billion at the median; at 5%, $1.19 billion, $1.80 billion and $197.5 billion. A bound on participation, not a model of market impact |
| 5 | Explicit sign-off | **Given** | by the owner, on 2026-10-06, after reading the rows above: *"Sign it"*; recorded in `BITACORA.md` and `JOURNAL_1.md` |

<!-- example: end -->

## The predictions, evaluated

**Every prediction in the blueprint gets a row, including the ones that were wrong.** A falsified
prediction is worth more than a correct one: it says something about the strategy that nobody knew,
and it cost one run to find out.

| # | Prediction | Outcome | What it changed |
| --- | --- | --- | --- |
| 1 | as written in the blueprint | confirmed or falsified, with the number | what is now understood differently |

<!-- example: begin -->

| # | Prediction | Outcome | What it changed |
| --- | --- | --- | --- |
| 1 | The golden cross earns its keep: +0.03 Sharpe and +0.5 points of CAGR over the control, and both measures in 2 of 3 sub-periods | **Held.** +0.080 of Sharpe and +0.60 points of CAGR; 2 of 3 sub-periods. **The CAGR margin is 0.10 points above its bar**, and the control won the last sub-period by 11.4 points a year | claim 1 is confirmed as a book on this universe, by a margin the CAGR limb barely clears; the cross's edge was earned in 2015 to 2022, and in the 2023–2026 rally the names it excluded rose faster |
| 2 | The cross is a drawdown control: a shallower maximum drawdown and lower volatility than the control | **Held.** −32.5% against −46.3%, 24.1% against 25.9% | the notes' reading of a trend filter as a risk gate is what the book shows most strongly: 13.85 points of drawdown |
| 3 | Traded-value weighting beats equal weight on Sharpe | **Held.** 0.842 against 0.722, and 20.33% against 14.53% a year | the liquidity papers' premium on the illiquid side does not show among the most traded members in this window, as the analyzer's rows 6 to 8 suggested |
| 4 | Lead: the book beats both benchmarks on Sharpe | **Reported: it does**, 0.842 against 0.713 and 0.743, and in every sub-period | — |
| 5 | Lead: the rule's selection beats chance | **Reported:** it does. The rule's idiosyncratic return, +13.84 points, is above all 20 random books, whose own run from −84.50 to −3.77 at Sharpes of 0.330 to 0.782 | — |
| 6 | Lead: the bounds hold a few dozen names, and the cap binds on few rebalance dates | **Reported:** a median of 37 names a day, 18 to 61; the cap binds on 341 of 1,381 rebalance dates, 24.7% — none before 2018, 11 in 2018, none in 2019, then 26 to 89 in each full year from 2020, as the largest names' share of traded value grew | the bounds set the count as designed; the cap is not rare, and it binds on the very names the market concentrated in |
| 7 | Lead: the book re-strikes often, and the realistic commission row changes its CAGR little | **Reported:** 48.1% of trading days; the realistic row adds 0.43 points of CAGR and 0.018 of Sharpe | — |
| 8 | Lead: most of the excess return is factor exposure | **Reported:** it is. Of the factor model's 137.35 points of excess return, 123.50 are factor exposure, 88.10 of them the market, and 13.84 are idiosyncratic | — |

<!-- example: end -->

## The book, priced by the engine

Record the date of the last full re-run from a wiped working copy, the engine version, and the
window. Then the book against every benchmark it reports against, and against the control its
blueprint names, on the rule's own rebalance dates: CAGR, volatility, Sharpe, Sortino, maximum
drawdown.

<!-- example: begin -->

Run 2026-10-06 with KaxaNuk Backtest Engine 0.66.0 over **2015-01-02 to 2026-06-01**, 2,869
trading days: 11.81 years as the engine counts them — 2,976 weekday steps after the first day, over
252 — against a calendar span of 11.41 years, so every CAGR here is the engine's, a little below one
taken over calendar years. Costs as `BLUEPRINT_1.md` fixed them: `commission_cents=0.05` on the
unadjusted price, measured at $0.035 to $0.041 a share; 5 basis points of slippage; a 1% cash
reserve; $1,000,000 of starting capital; integer shares. Every row is net, and every engine run was
valued to the last day of its window.

| Book | CAGR | Volatility | Sharpe | Sortino | Max drawdown | Alpha vs index | Information ratio |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **The rule** | **20.33%** | 24.13% | **0.842** | 1.116 | −32.47% | +7.28% | 0.665 |
| The control, the cross removed | 19.73% | 25.86% | 0.763 | 1.011 | −46.32% | +6.68% | 0.653 |
| The rule's names, equally weighted | 14.53% | 20.12% | 0.722 | 0.967 | −30.19% | +1.47% | 0.297 |
| The rule, realistic commission | 20.75% | 24.13% | 0.860 | 1.138 | −32.18% | +7.70% | 0.692 |
| The control, realistic commission | 19.92% | 25.86% | 0.770 | 1.020 | −46.23% | +6.87% | 0.665 |
| KN US Equity Core | 13.05% | 18.32% | 0.713 | 0.878 | −33.75% | | |
| `SPY` | 13.49% | 18.16% | 0.743 | 0.981 | −33.63% | | |

**By sub-period**, each priced on its own window, the book struck again on its first day:

| Sub-period | Rule CAGR | Rule Sharpe | Control CAGR | Control Sharpe | Index Sharpe | `SPY` Sharpe |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2015 to 2018 | 9.02% | 0.530 | 7.86% | 0.468 | 0.438 | 0.493 |
| 2019 to 2022 | 16.82% | 0.619 | 9.05% | 0.295 | 0.518 | 0.549 |
| 2023 to 2026-06-01 | 40.44% | 1.483 | 51.85% | 1.830 | 1.455 | 1.443 |

**The sweep, criterion 3**: each setting moves one of the rule's parameters and is priced with its
own control, the cross removed, on its own rule's dates. The KN US Equity Core's Sharpe is 0.713.

| Setting | Sharpe | Control | Margin | CAGR | Control | Margin | Both kept |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Cap 15% — binds on 620 of 1,408 rebalance dates | 0.874 | 0.789 | +0.085 | 20.47% | 19.92% | +0.55 | yes |
| Cap 25% — binds on 141 of 1,358 | 0.819 | 0.760 | +0.059 | 20.17% | 19.86% | +0.30 | yes |
| Floor 0.5% | 0.799 | 0.758 | +0.042 | 18.24% | 18.18% | +0.07 | yes |
| Floor 2% | 0.920 | 0.831 | +0.088 | 23.60% | 23.12% | +0.48 | yes |
| Traded value over 21 days | 0.803 | 0.708 | +0.096 | 19.49% | 18.34% | +1.15 | yes |
| Traded value over 126 days | 0.859 | 0.775 | +0.084 | 20.41% | 19.93% | +0.48 | yes |
| Cross 20/100 | 0.818 | 0.753 | +0.064 | 18.66% | 19.51% | −0.85 | no |
| Cross 100/300 | 0.797 | 0.774 | +0.023 | 19.71% | 20.04% | −0.32 | no |

The rule's own cap, 20%, binds on 341 of its 1,381 rebalance dates. Margins are computed before
rounding, so a margin can differ by 0.001 from the difference of the two printed Sharpes.

<!-- example: end -->

## What the book actually is, structurally

Rebalance frequency, turnover, holdings, concentration, invested share, and any structural tilt —
each with a reading of what a bad value would have meant.

<!-- example: begin -->

| Measure | Value | What a bad value would have meant |
| --- | ---: | --- |
| Rebalance dates | 1,381 of 2,869 trading days, 48.1% | a rule firing every day is a cost question; this one fires about every other day, because the count moves with the bounds |
| Holdings | median 37 a day, 18 to 61; by year from 46 in 2015 to 23 to 27 from 2023 | the count shrinks as traded value concentrates |
| Effective positions | 19.0 on average | thirty-seven names behaving like nineteen |
| Largest weight | 15.0% on average, the cap at 20% binding on 24.7% of rebalance dates | the cap is a working bound, not a formality |
| Invested share | 100% throughout | fewer than five eligible names never happened |
| Turnover | 3.09 times the book a year, one way | priced honestly by the engine at both cost rows |
| Sector, today's labels, indicative | Technology from 19.9% of the book in 2015 to 60.7% in 2026 | **the book became a technology book**, as the index's traded value did |

<!-- example: end -->

## The trial count

How many variants were ranked to reach the book above, and every run excluded by name with its
reason. `RESULTS.md` compiles this: a reader cannot discount a best-of-N result without knowing N,
and the graduation sign-off says whether the deflated figure was also computed.

<!-- example: begin -->

**107 books.** 23 priced by the first earlier version and 14 by the second, both on another index,
as the blueprint counts them; 39 in this version's run; and **31 priced in the first attempt of this
run, before the sell-at-t−1 rule**, excluded by name in `RESULTS.md` and counted. The engine priced
45 of this run's 47 weight files in the second run; the other two, the rule's and the control's
2023–2026 sub-periods, came back identical to the first attempt's and were read from its cache, as
the third and fourth runs read all 47 while two attribution errors were fixed; a repeat of an
identical book adds no trial. The window is the one choice counted beside the books. The deflated
Sharpe was not computed.

<!-- example: end -->

## Attribution — is this the signal, or a factor exposure wearing its name?

Brinson-Fachler: allocation, selection, interaction. The factor model: factor against idiosyncratic.
State the window, which is bound by the supplied files' coverage and is usually shorter than the
backtest.

**What it settles**, and **what it does not** — naming the counterfactual book that would settle
what is left: the same holdings with the signal off, positions equalised, a random draw at the same
sizes, entry dates shifted.

<!-- example: begin -->

Run 2026-10-06 with KaxaNuk Attribution Analysis 0.2.0 over **2015-01-02 to 2026-06-01**, the
backtest's own window, on the rule, its control and the equal-weight arm in three passes, and the
factor model on the twenty random books. **Points are daily returns summed over the window**, not
compounded, so they are comparable within a table and not with a CAGR. The book's weights are its
targets **held overnight** — the close of t−1 earns day t's return — and so are the index's; the
index's holdings drop the members FMP does not price on each date and renormalise the rest. The
share of the whole index the first cut prices: 94.1% in 2015, 96.3% in 2016, 97.4% in 2017, 98.1%
in 2018, 99.1% in 2019, 99.7% in 2020, 99.9% in 2021, and, rounded, all of it from 2022.

**The precondition first.** The first cut's benchmark, built from the holdings, earns 14.85 points
a year against the KN US Equity Core's own returns file at 14.31 over the same days: a gap of
**0.54**, inside the blueprint's 1.0. The third run's attempt missed by 6.94, because weights struck
at a day's close were paired with that same day's return; `JOURNAL_1.md` records the fix and what
the misaligned pass had shown.

### First cut — Brinson-Fachler, per asset

Every asset is its own group, as the library computes it, so *allocation* is the bet on a name and
*selection* the return earned inside it.

| The rule, summed over the window | Points |
| --- | ---: |
| Book | 265.90 |
| Benchmark | 169.04 |
| **Active** | **96.87** |
| Allocation | 2.38 |
| **Selection** | **17.44** |
| Interaction | 77.05 |

**Most of the active return is interaction**: the book held heavy weights in the names that then
rose, which a per-asset decomposition does not split cleanly into choosing and sizing. Selection is
positive and the smaller part.

### Second layer — the factor model

| Points over the window | The rule | The control | Equal weight |
| --- | ---: | ---: | ---: |
| Market | 88.10 | 88.08 | 88.06 |
| Momentum | 11.31 | 8.01 | 9.00 |
| Beta | 10.39 | 22.15 | 5.59 |
| Size | 9.15 | 8.00 | 4.66 |
| Residual volatility | 4.81 | 4.96 | 1.30 |
| Value | −0.25 | −0.93 | 1.44 |
| The eleven sector factors | 0.00 | 0.00 | 0.00 |
| **Total excess** | **137.35** | 120.81 | 80.01 |
| Factor | 123.50 | 130.28 | 110.05 |
| **Idiosyncratic** | **13.84** | −9.48 | −30.03 |

The factor model covers 99% of each book. **Nine tenths of the rule's excess return is factor
exposure, and most of that is the market.** Against its control, the cross **more than halves
the beta exposure**, 10.39 points against 22.15, adds a little momentum, and turns the idiosyncratic
return from −9.48 to +13.84: the control earns more from factors and loses it in the residual.
Against equal weight, traded-value sizing adds beta and size and turns −30.03 into +13.84. The
eleven sector factors carry nothing, as they did for the earlier version: the files hold no values.

**The random books**, each drawing the rule's count from the members on the rule's dates and sizing
by traded value under the cap, at the rule's turnover:

| | Idiosyncratic, points | Sharpe | CAGR |
| --- | ---: | ---: | ---: |
| **The rule** | **+13.84** | **0.842** | **20.33%** |
| Random 01 | −47.11 | 0.372 | 7.34% |
| Random 02 | −84.50 | 0.330 | 6.55% |
| Random 03 | −55.43 | 0.384 | 8.01% |
| Random 04 | −43.57 | 0.466 | 9.51% |
| Random 05 | −3.77 | 0.731 | 14.70% |
| Random 06 | −44.82 | 0.544 | 10.71% |
| Random 07 | −37.99 | 0.519 | 10.27% |
| Random 08 | −43.18 | 0.496 | 10.59% |
| Random 09 | −26.84 | 0.547 | 10.96% |
| Random 10 | −11.19 | 0.666 | 13.80% |
| Random 11 | −13.28 | 0.782 | 15.19% |
| Random 12 | −36.49 | 0.501 | 9.85% |
| Random 13 | −59.46 | 0.465 | 9.22% |
| Random 14 | −39.88 | 0.501 | 10.78% |
| Random 15 | −59.87 | 0.562 | 12.15% |
| Random 16 | −23.97 | 0.565 | 11.09% |
| Random 17 | −11.86 | 0.617 | 12.57% |
| Random 18 | −23.05 | 0.770 | 15.76% |
| Random 19 | −22.69 | 0.593 | 11.65% |
| Random 20 | −47.85 | 0.421 | 8.22% |

All 20 are below the rule; the bar was 16. Every random book's idiosyncratic return is negative;
the highest is −3.77, random 05, and the best Sharpe and CAGR belong to two other books, 11 and 18.

### Third pass — Brinson-Fachler on the residual

| Points over the window | The rule | The control | Equal weight |
| --- | ---: | ---: | ---: |
| Book's residual | 13.84 | −9.48 | −30.03 |
| Index's residual | −29.87 | −29.87 | −29.87 |
| Active | 43.71 | 20.39 | −0.16 |
| Allocation | 0.35 | 0.21 | −0.02 |
| **Selection** | **2.70** | −0.27 | −0.80 |
| Interaction | 40.67 | 20.45 | 0.66 |

**Once factor exposure is stripped out, the rule's selection is +2.70 points over the window** —
positive, and small; the control's and equal weight's are negative. What is left is again mostly
interaction.

### What attribution says

**The book is a market-and-trend book with a thin residual edge.** Nine tenths of its excess return
is the factors a full-beta, large-cap book in a rising decade earns, and the question the third
pass answers — whether the Sharpe survives once those factors turn — reads **barely**: 2.70 points
of residual selection over the window. What the golden cross does, attribution says plainly: **it
cuts the beta the control takes** to less than half, 10.39 against 22.15 points, which is the
drawdown prediction 2 saw, and it converts a negative residual into a positive one. Each limb of
criterion 2 is positive and the gate passes it as written; **none of them is large**, and the
misaligned third run had shown them larger: first-cut selection 24.46, idiosyncratic 61.02,
residual selection 7.65.

**Timing was not priced.** The shifted-entry timing arm, which the gate named as not run, was not
run: nothing here separates choosing the names from choosing the day they enter.

<!-- example: end -->

## What is open, ranked

The single highest-value run outstanding, and what it would settle.

<!-- example: begin -->

1. **Paper days.** Nothing here is out of sample; the paper book is what can show the rule's
   behaviour on days it never saw.
2. **The 2023–2026 sub-period**, which the control won by 11.4 points a year: whether the cross
   costs the most in a concentrated, momentum-led rally is the question the next experiment can ask.
3. **The deflated Sharpe** of the winner against its 107 trials.
4. **The members FMP does not price** — 7% of the index early in the window — through a second
   provider, as a different universe.

<!-- example: end -->

## Caveats

| # | Caveat | Effect |
| --- | --- | --- |
| 1 | what a reader must know before quoting a number above | what it does to that number |

<!-- example: begin -->

| # | Caveat | Effect |
| --- | --- | --- |
| 1 | **Survivorship from FMP only**: the members FMP does not price held up to 7.0% of the index's weight in 2015, at most 0.12% in 2022, on its first 37 trading days, and none from 2023 | the early years are measured on a slightly survivor-biased index; the first cut's benchmark is renormalised over the priced members |
| 2 | **Two changes after the blueprint**: the sell-at-t−1 rule, the owner's, after the engine refused a 62-day gap in `AGN`; and the attribution's one-day alignment, caught by the blueprint's own precondition | neither moves a parameter the blueprint names; both are recorded in `JOURNAL_1.md`, with what had been seen first |
| 3 | **One day of hindsight** in every exit before a price stops — a delisting or a corporate event | the leak `AGENTS.md` names, applied to every book alike |
| 4 | **The window is a forking path**, and the margins were set knowing the earlier version's 2017–2026 result | disclosed and counted |
| 5 | Classification is today's, `current_*` | the sector table is indicative |
| 6 | The index's holdings and returns files disagree slightly | the first cut reconciles within the blueprint's 1.0-point tolerance once its weights are aligned |
| 7 | **The provider's volume for `KLAC` is about ten times too high from 2026-05-13**, the 21 trading days before its 10-for-1 split of 2026-06-12, while its price stays unsplit, so its traded value — the rule's score — is inflated over the window's last 13 trading days. Found after the run, by the paper book's first-day checks | `KLAC` re-entered the book on 2026-05-14, having dropped out on 2026-05-07 at about 1.1%, and reached 2.6% on 2026-06-01. Its prices are right and the engine priced them; the weights of those days were chosen on a bad input. Not corrected: the rules are frozen, and the frozen book carries it |

<!-- example: end -->
