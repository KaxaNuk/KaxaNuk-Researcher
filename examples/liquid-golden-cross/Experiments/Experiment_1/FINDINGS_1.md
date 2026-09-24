# Findings — Experiment 1

> **Latest valuable results only.** This file is rewritten when a result changes, not appended to —
> the running history is in [`JOURNAL_1.md`](JOURNAL_1.md), and the hypothesis this tested is in
> [`BLUEPRINT_1.md`](BLUEPRINT_1.md).
>
> **[`../../RESULTS.md`](../../RESULTS.md) is compiled from this file.** When a finding here
> changes, change it here first, then update the summary.

## Status

**Not yet run.** When it has: one line saying whether the benchmark is adopted, and the reminder
that the benchmark is not a graduation candidate — its job is to be the thing others are measured
against. Then **the claim it moved**: the claim of `OBJECTIVE.md` the blueprint named, and the
status it reached — or why it reached none.

<!-- example: begin -->

**Adopted as the benchmark, 2026-09-20; its last criterion answered 2026-09-22.** It is a tradeable
and stable yardstick, and that is the whole of its job. The benchmark is not a graduation
candidate, and it would not be one on these numbers: **the filter costs 1.12 points a year against
the control that differs from it in exactly one thing**, and what it buys is a shallower drawdown
rather than a higher return.

**The claim it moved: claim 1 of `OBJECTIVE.md`, the signal, to falsified.** The filter-off
comparison of prediction 2, put on the rule's own dates, is what moved it. Claim 3 keeps its
status, true by construction, and gains a measurement from the counterfactuals below.

**The four criteria `BLUEPRINT_1.md` set, each answered.**

| # | Criterion | State |
| --- | --- | --- |
| 1 | Reproducible from a clean clone, through the pipeline, with no manual step | **Met, to the data.** Re-run on 2026-09-22 from a wiped working copy on a fresh download, every stage headless and no manual step beyond the hand-supplied index and factor files: every conclusion held, the filter-off control and the index came back to every published decimal, and the rule moved within what a re-pull moves — 17.89% against 17.85%, Sharpe 0.863 against 0.861, 86 rebalances against 87 — on a panel ten rows different. *Re-run from a wiped working copy* below has every figure; the published ones stand as the record of the 2026-09-20 run |
| 2 | A tradeable trigger frequency — not a rule that fires every day | **Met.** 87 rebalances in 9.4 years, 9.2 a year, at 17.8% one-way turnover each |
| 3 | Net-of-cost results reported against every benchmark it declares | **Met.** Every row of *The book, priced by the engine* is net, against the index, the filter-off control and the equalised control |
| 4 | Every prediction evaluated explicitly, including the ones that turn out wrong | **Met.** Six rows: three confirmed, two falsified, one split |

Adoption stands on all four. What the re-run adds is the size of the drift a fresh download
produces, which is the honest error bar on every figure below.

<!-- example: end -->

## The predictions, evaluated

**Every prediction in the blueprint gets a row, including the ones that were wrong.** A falsified
prediction is worth more than a correct one: it says something about the strategy that nobody knew,
and it cost one run to find out.

| # | Prediction | Outcome | What it changed |
| --- | --- | --- | --- |
| 1 | as written in the blueprint | confirmed or falsified, with the number | what is now understood differently |

<!-- example: begin -->

**Every prediction in the blueprint gets a row, including the ones that were wrong.**

| # | Prediction | Outcome | What it changed |
| --- | --- | --- | --- |
| 1 | Volatility below the index's | **Falsified.** 20.73% against the index's 19.01% | The prediction was written from a per-security measurement and tested against a 600-name index. Thirty names are more volatile than six hundred whatever the filter does. Against the book it is actually a variant of, the filter-off control at 22.91%, the filter removes 2.2 points of volatility, which is what the analyzer said it would: a new observation, not this prediction's verdict |
| 2 | Does not beat the filter-off book by more than 1 point a year | **Confirmed, and then confirmed harder.** −0.77 points a year against the plain control; **−1.12** against the equalised one | An information coefficient of 0.0112 produced exactly what it should: no return edge. The equalised control, added 2026-09-20, is the comparison that differs in one thing only, and the filter looks worse against it |
| 3 | Drawdown shallower than the index's | **Confirmed.** −30.5% against −33.8%, and −39.8% for the control | The filter's value is drawdown, not return: 9.3 points shallower than the same thirty names unfiltered |
| 4 | The worst relative stretch is a rebound, not a decline | **Confirmed.** Worst 63-day stretch −12.5 points, ending 2023-02-06, while the index rose 11.1% | LeBaron's failure mode reproduced on a different market and a different rule. A late-turning average sells into the bottom and buys back above it |
| 5 | Positive momentum loading, beta below one | **Falsified.** Momentum contributes +12.75 points, as predicted; beta is **1.028**, and the falsifier fires on either limb | The book inherits momentum without trading it, as predicted. It does not inherit low beta: holding the most traded names in an uptrend is a full-beta position, not a defensive one |
| 6 | Holds cash in 2008–09 and early 2020 | **Split.** 27–40% cash through December 2008 and January 2009; **no cash at all in 2020** | The filter steps aside from slow declines and sleeps through fast ones. The 2020 fall took about 23 trading days; a 200-day average cannot turn in that time |

Three confirmed, two falsified, one split. **The first falsification taught the most**: prediction 1
was a portfolio-level claim built from a security-level measurement, and no amount of care in the
backtest would have surfaced that if the prediction had not been written down first. The second was
a verdict word: prediction 5's falsifier fires on either limb, and a beta of 1.028 fires it — it was
recorded as *split* until the challenge of 2026-09-20 read it back against the blueprint.

<!-- example: end -->

## The book, priced by the engine

Record the date of the last full re-run from a wiped working copy, the engine version, and the
window. Then the book against every benchmark it reports against, and against the control its
blueprint names, on the rule's own rebalance dates: CAGR, volatility, Sharpe, Sortino, maximum
drawdown.

<!-- example: begin -->

Run 2026-09-20 with KaxaNuk Backtest Engine 0.66.0. Costs are those frozen in `BLUEPRINT_1.md`:
`commission_cents=0.1`, which the engine charges as about **$0.083 a share**, plus 5 basis points
of slippage and a 2% cash reserve. Results are net.

| Book | Window | CAGR | Volatility | Sharpe | Max drawdown | Alpha | Rebalances | Costs |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **The rule** | 2017-01-03 → 2026-06-01 | **17.85%** | 20.73% | **0.861** | −30.54% | 3.14% | 87 | $106,000 |
| The rule, realistic costs | same | 18.34% | 20.72% | 0.885 | −30.40% | 3.63% | 87 | $36,800 |
| **Filter off**, the control | same | 18.62% | 22.91% | 0.813 | −39.79% | 3.91% | 11 | $20,300 |
| The KN600 index | same | 14.71% | 19.01% | 0.774 | −33.75% | — | — | — |
| The rule, long window | 2002-07-30 → 2026-06-01 | 10.29% | 20.00% | 0.514 | **−60.74%** | −0.70% | 307 | $624,000 |

**The long window is the sobering one.** Over 23.8 years the same rule compounds at 10.29% with a
60.7% drawdown and a negative alpha. Whatever the filter does in a nine-year sample dominated by
one direction, it does not survive a 2008 as a drawdown shield.

### Re-run from a wiped working copy, 2026-09-22

The same pipeline, from `init-example` into an empty folder, on a fresh download the same day, with
the same engine version and the same frozen costs. **No published figure above is changed by it**:
the numbers moved for a known reason — a fresh pull rebases every adjusted column, limitation 5 of
`RESULTS.md`, and this panel is ten rows short of the published one — and a committed result is not
edited to agree with a new run. What moved, and by how much, is the error bar on the table above.

| Book | Published | Re-run | Moved |
| --- | --- | --- | --- |
| The rule: CAGR, Sharpe, max drawdown, rebalances | 17.85%, 0.861, −30.54%, 87 | 17.89%, 0.863, −30.55%, 86 | one rebalance, and hundredths |
| The rule, realistic costs | 18.34%, 0.885, −30.40% | 18.38%, 0.887, −30.42% | hundredths |
| Filter off, the control | 18.62%, 0.813, −39.79%, 11 | 18.62%, 0.813, −39.79%, 11 | nothing |
| The KN600 index | 14.71%, 0.774, −33.75% | 14.71%, 0.774, −33.75% | nothing |
| The rule, long window | 10.29%, 0.514, −60.74%, 307 | 10.28%, 0.514, −60.74%, 307 | 0.01 of a point |
| The equalised control | 18.97%, 0.831 | 18.96%, 0.831 | 0.01 of a point |
| The filter's cost a year: plain, equalised | −0.77, −1.12 | −0.73, −1.07 | 0.04 and 0.05 |
| Factor model: market, momentum, idiosyncratic | 83.33, 12.75, 45.52 | 83.42, 12.69, 45.44 | hundredths; the sectors 0.00 again |
| Random books, five seeds: idiosyncratic | −17.63 to 25.17, mean 12.5 | −13.98 to 29.45, mean 11.1 | the most, as draws from a shifted pool would |

Every conclusion in this file survives the re-run: the filter costs return and buys drawdown, the
book is a full-beta position with a momentum loading it never traded, the sector factors read zero,
and the rule's idiosyncratic return sits above the random range's top. The one thing the re-run
does not let a reader keep is the third decimal.

<!-- example: end -->

## What the benchmark actually is, structurally

Rebalance frequency, turnover, holdings, concentration, invested share, and any structural tilt —
each with a reading of what a bad value would have meant.

<!-- example: begin -->

| Property | Value | What a bad value would have meant |
| --- | ---: | --- |
| Rebalances | 87 in 9.4 years, 9.2 a year | A rule firing weekly would make this a transaction-cost question, not an alpha one |
| One-way turnover per rebalance | 17.8% | The band is doing its job: it fires at 10% and the set has moved 18% by then |
| Annual turnover | 165% | High for a "slow" signal, and the reason costs matter here |
| Holdings / effective positions | 30.0 / 30.0 | Equal by construction; a gap would mean hidden concentration |
| Mean invested share | 100%, lowest 0% on day one | A persistently low figure would mean the eligibility column is not what the analyzer measured |
| Sector drift | Technology 23.7% (2017) → 15.0% (2022) → 45.4% (2024) | A flat line would mean the rotation is a label rather than a behaviour |

<!-- example: end -->

## The trial count

How many variants were ranked to reach the book above, and every run excluded by name with its
reason. `RESULTS.md` compiles this: a reader cannot discount a best-of-N result without knowing N,
and the graduation sign-off says whether the deflated figure was also computed.

<!-- example: begin -->

**Ten engine runs, all ten reported.** Four are variants of the strategy — the rule, the rule at
realistic costs, the filter-off control, and the long window — specified in `BLUEPRINT_1.md` and
`BRAINSTORMING_1.md` before the engine ran. **Six are counterfactual arms**, added on 2026-09-20 to
decompose the idiosyncratic share: the equalised control and five random books. None of the six is
a candidate for the headline and none could become one — a random book and a book that trades on
another book's dates are diagnostics. They are counted here because a reader cannot discount what
they cannot see.

**No variant was selected on its result.** The four strategy variants were fixed before the engine
ran; the six arms were specified, with all four of their possible outcomes written down, in the
commit that preceded the run.

**Three runs are excluded by name, with their reason:** the long window at a 0.5% cash reserve
(truncated at 2003-04-22), at 1% (truncated at 2009-06-01), and the first point-in-time run at 0.5%
(cash error on day one). In each the engine reported success while valuing only the stub. They are
excluded because a run that stops valuing the book partway summarises cleanly over what it did
value, which is the most dangerous kind of wrong number.

<!-- example: end -->

## Attribution — is this the signal, or a factor exposure wearing its name?

Brinson-Fachler: allocation, selection, interaction. The factor model: factor against idiosyncratic.
State the window, which is bound by the supplied files' coverage and is usually shorter than the
backtest.

**What it settles**, and **what it does not** — naming the counterfactual book that would settle
what is left: the same holdings with the signal off, positions equalised, a random draw at the same
sizes, entry dates shifted.

<!-- example: begin -->

**Window: 2017-01-03 → 2026-06-01**, the same as the backtest here, because the factor files cover
2008 onwards. For the long window the attribution would be clipped to 2008 and is not reported.

**First cut, Brinson-Fachler**, summed daily over the window, in percentage points: alpha **+47.1**,
of which allocation **−0.7**, selection **+8.2**, interaction **+39.7**.

This library's first cut is **per asset, not per group**. The book and the index hold the same
securities, so a return difference *inside* a group has nowhere to land, and the active return
falls into allocation and interaction rather than into selection. Read it as "the weighting did it",
not as "the sectors did it".

**Second layer, the factor model**, in percentage points of the book's 159.5 points of excess
return over the window:

| Source | Points | Share |
| --- | ---: | ---: |
| Market | 83.33 | 52% |
| Momentum | 12.75 | 8% |
| Residual volatility | 7.09 | 4% |
| Size | 4.11 | 3% |
| Value | 3.38 | 2% |
| Beta | 3.36 | 2% |
| **All factors** | **114.01** | **71%** |
| **Idiosyncratic** | **45.52** | **29%** |

**What it settles.** Seventy-one percent of the book's excess return is compensated factor
exposure, and more than half of the whole is plain market beta — the book's beta is **1.028**, so
it is a full-beta equity position. Momentum is the largest style contributor at 8%, which the book
acquired without trading it: it holds winners by construction. **Twenty-nine percent, 45.5 points,
is idiosyncratic** — of which about 12.5 is what any concentrated equally weighted book earns in
this window, so roughly 33 points are genuine selection. The counterfactual section below is where
that division comes from.

**What the 45.5 points are, settled by counterfactual.** Six more books were priced to find out —
the section below. The short answer: **roughly a quarter of it is not selection at all**, most of
the rest is the liquidity ranking, and about a ninth is the trend filter.

The eleven sector factors all came back at exactly 0.00 points, which is not credible for a book
whose technology weight moved between 15% and 45%. Treated as unexplained; the sector files' role
in this library's decomposition needs checking before any sector claim is made from them.

## The counterfactuals — who earned the idiosyncratic share

Run 2026-09-20. Six more books, each removing exactly one of the choices the rule makes and keeping
the rest. **The predictions for all four possible outcomes were committed before the engine ran**,
in the notebook's section 6 and in the commit that added it.

| Arm | What it removes | CAGR | Sharpe | Excess | Factors | **Idiosyncratic** |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| The rule | — | 17.85% | 0.861 | 159.53 | 114.01 | **45.52** |
| **The equalised control** | the trend filter | **18.97%** | 0.831 | 166.75 | 126.28 | **40.47** |
| The plain control | the filter, and 76 of the 87 rebalances | 18.62% | 0.813 | 158.88 | 126.78 | **32.09** |
| Random, 5 seeds | the liquidity ranking | 3.29% to 9.42% | 0.17 to 0.48 | 67 to 109 | 61 to 85 | **−17.63 to 25.17** |

**The equalised control is the one the published comparison should have used.** The plain control
fires 11 times against the rule's 87, so it differs in two things, not one: it also trades a
seventh as often and drifts far further into whatever has been winning. Forcing it onto the rule's
own dates leaves the trend condition as the only difference — and it **earns more than the plain
control**, 18.97% against 18.62%.

**So the filter costs more than this file first reported.** Against the plain control it was
**−0.77** points a year. Against the control that differs in exactly one thing it is **−1.12**.
Removing the confound made the filter look worse, not better. The −0.77 figure is not withdrawn —
it is the right number for the comparison it describes — but −1.12 is the one claim 1 is about.

**The 45.5 idiosyncratic points break into three parts:**

| Part | Points | Share | What it is |
| --- | ---: | ---: | --- |
| Baseline | ~12.5 | 27% | what this decomposition assigns to *any* equally weighted thirty-name book from this index. The random books' mean. **Not selection** |
| The liquidity ranking | ~28 | 62% | what separates the equalised control from a random draw |
| The trend filter | ~5 | 11% | what separates the rule from the equalised control |

**The prediction that failed is the important one.** The random books were predicted to land near
zero. They did not: their mean idiosyncratic contribution is **+12.5 points**, with a spread from
−17.6 to +25.2. A concentrated equally weighted book earns residual in this window whatever it
holds, so **45.5 overstates genuine selection by roughly a quarter**, and the honest figure is
nearer 33. Nothing in the factor model says so on its own; only the random arm does.

**What it does not settle.** Five seeds is five samples, and the spread is 43 points wide, so the
baseline of 12.5 carries real uncertainty and every share above is indicative. The rule's 45.5 sits
above the random range's top, which is the claim that survives: **the rule's idiosyncratic return
is outside what a random book of the same shape produced in five tries.** A proper test would draw
far more and report the percentile.

**One honest oddity.** The equalised control trades on dates the *filtered* book chose, which is
information it would not have on its own. It is a diagnostic, not a strategy, and it cannot be
proposed as one.

<!-- example: end -->

## What is open, ranked

The single highest-value run outstanding, and what it would settle.

<!-- example: begin -->

1. **Draw far more random books and report the percentile.** Five seeds put the baseline at 12.5
   points with a 43-point spread: enough to prove it is not zero, not enough to say what it is.
   Everything the counterfactual section concludes rests on that number. Highest value.
2. **The band, read as a curve** — 0%, 5%, 10%, 20%, 30%, everything else frozen. Claim 4 has never
   been tested, and the equalised control is the first evidence bearing on it: the same book at 87
   rebalances beat itself at 11, net of costs, which suggests 10% may be too wide. Choose the band
   on turnover and persistence, never on the CAGR it will be judged by. **A new experiment, not an
   edit here** — the rule froze when this file first reported.
3. **The sector factors reading zero.** Until that is understood, no sector attribution claim
   stands.
4. **The long window's −60.7% drawdown**, decomposed. The nine-year and twenty-four-year records
   disagree about what this rule is, and the disagreement is the interesting part.

<!-- example: end -->

## Caveats

| # | Caveat | Effect |
| --- | --- | --- |
| 1 | what a reader must know before quoting a number above | what it does to that number |

<!-- example: begin -->

| # | Caveat | Effect |
| --- | --- | --- |
| 1 | **The long window holds membership fixed**, because the index's own holdings begin in 2017 | Companies that died before 2017 are absent and later listings are present from the start. Every long-window number is survivorship-affected and indicative only |
| 2 | **Costs are the blueprint's frozen figure**, about $0.083 a share | Roughly twenty times a real retail rate. The realistic-cost row shows the difference: +0.49 points of CAGR in the short window |
| 3 | **The 2% cash reserve** is an engine requirement, not a strategy choice | The book is 98% invested throughout; a smaller reserve truncates the long run |
| 4 | **Five securities are excluded by name** — `MIC`, `CIT`, `FMC`, `LCI`, `PARA` | Four carry impossible prints. `PARA` alone contributed 160 points to the index's reconstructed return in one day before it was excluded from the attribution as well |
| 5 | **Delisting exits use one day of hindsight** | Load-bearing here: the universe retains 82 delisted names, and `TWTR` was force-sold at its last price in the run |
| 6 | **Attribution reconstructs the benchmark from weights and prices** and never reads the index's own return series | The reconstructed index return is higher than the published one; the decomposition's shares are more reliable than its levels |
| 7 | **The attribution runs on the invested 98% of the book.** The engine's daily weights carry a `CASH_RESERVE` column with no price series, and the library prices only what it can name | Found on 2026-09-20 while building the counterfactuals. It applies identically to every arm, so the comparisons stand, and it reproduces the published 45.52 exactly — but the cash reserve is dropped rather than carried at a zero return, and that was never stated |
| 8 | **The idiosyncratic points are measured against a baseline of about 12.5, not against zero** | A random thirty-name book earns residual in this window too. Any figure in this file that calls a raw idiosyncratic number "alpha" should be read net of that baseline |
| 9 | **The long window starts 2002-07-30, where `BLUEPRINT_1.md` declared 2002-01-02** | `SHY`, the cash proxy, launched on 2002-07-30, and a book whose cash has no price is a book the engine cannot value, so the notebook clips the start to the earliest priceable date. Seven months of the declared window are in no long-window figure. The clip is deliberate and in the code; it was simply never written down, and the challenge of 2026-09-20 found it by reading the blueprint's window against this table's |
| 10 | **A fresh download moves the figures at the second decimal.** The re-run of 2026-09-22 from a wiped copy ran on a panel ten rows short of the published one and fired one rebalance fewer | Every figure in this file carries roughly that error bar: hundredths of a point of CAGR and Sharpe, a few points on the random arms, nothing on the filter-off control or the index. The published figures are the 2026-09-20 run's and are not edited to match |

<!-- example: end -->
