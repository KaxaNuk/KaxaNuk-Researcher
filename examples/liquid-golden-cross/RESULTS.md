# Results

> **Executive summary of everything this repository has measured.**
>
> Experiment sections are compiled from the `FINDINGS_N.md` files and cite each one. **When a number
> changes, change it in `FINDINGS_N.md` first**, then update this file — a summary that leads its
> sources is how two numbers for the same book start to circulate.
>
> **One exception:** findings from step 3, `Data/analyzer.ipynb`, go straight into *Before any
> experiment* below: notebook outputs are stripped before committing, so a measurement that lives
> only in a cell output does not survive the commit.
>
> Every performance figure comes from the **KaxaNuk Backtest Engine**. There is no second backtest
> in this repository, by design.
>
> Every table below except *Known limitations* is empty by design: the shape is fixed, the numbers
> arrive from the pipeline.
> Delete this blockquote when the first one reports.

<!-- example: begin -->

> **In this example, everything below is `liquid-golden-cross`, measured.** Steps 1 to 6 are run and
> the numbers are real. Step 7's gate has been *evaluated* and the book fails it — but no paper
> trading has run, so **nothing here is out of sample**. Which criteria it fails and why is in
> [`Paper_Trading/BITACORA.md`](Paper_Trading/BITACORA.md).

<!-- example: end -->

## The project in three sentences

Does the benchmark book work, with its headline numbers. What attribution says about where the
return comes from. Which lever earned its place after the benchmark, and which was rejected.

<!-- example: begin -->

**The book works, but not for the reason it was built.** Holding the thirty most traded US stocks
whose 50-day average sits above their 200-day compounded at 17.85% against the index's 14.71% over
2017–2026, net of costs, with a shallower drawdown — but the same thirty names without the filter
earned **more**, so the trend condition bought drawdown rather than return. Against the control
that differs in exactly one thing, the filter costs **1.12 points a year**.

**Attribution says 71% of the excess return is factor exposure**, more than half of it plain market
beta, with a beta of 1.028 and a momentum loading the book acquired without trading it. Six
counterfactual books split the remaining 45.5 points three ways: **about 12.5 is what any
concentrated equally weighted book earns here, about 28 is the liquidity ranking, and about 5 is
the trend filter.**

**Nothing has earned a lever yet, and one published reading has been tightened.** The idiosyncratic
share is measured against a baseline of 12.5 rather than zero, so the honest figure for selection
is nearer 33 points than 45.5. Experiment 1 is the benchmark; the next experiment tests the
rebalancing band, which has never been tested at all.

<!-- example: end -->

---

## Before any experiment: what the data already says

Findings from step 3, `Data/analyzer.ipynb`: whether a candidate feature carries information, over
what horizon, and with which sign — and anything measured about the signal that does not need a
book. Cite the section each number came from.

<!-- example: begin -->

**Measured 2026-09-19 on 4,252,848 rows: 787 securities, 2001-01-02 to 2026-06-01.** The eligible
pool is the most traded five percent of each day's cross-section, which is where the rule selects
from.

| # | Measurement | Value | Section |
| --- | --- | ---: | --- |
| 1 | Mean pairwise correlation of daily returns | 0.303 | 2 |
| 2 | Information coefficient of `r_trend_50_200`, 21 days, eligible pool | 0.0112 | 4 |
| 3 | The same, 63 days | 0.0027 | 4 |
| 4 | The same, 252 days | −0.0060 | 4 |
| 5 | Information ratio at 21 days, eligible pool | 0.038 | 4 |
| 6 | Forward 21-day return, 50-day average above the 200-day | 1.20% | 5 |
| 7 | Forward 21-day return, 50-day average below the 200-day | 1.03% | 5 |
| 8 | Forward 21-day volatility, above | 28.7% | 5 |
| 9 | Forward 21-day volatility, below | 36.7% | 5 |

**What it says.** The trend signal barely predicts return and strongly predicts volatility. An
information coefficient of 0.011 at one month is noise beside the 0.02 to 0.03 a working signal
shows; it decays to nothing by three months and turns negative at a year, on 5,939 dates. The
volatility difference is the opposite: 28.7 percent against 36.7 percent, on 208,111 observations,
in the direction the rule's own trades would take.

**What it licenses, and what it forbids.** It licenses a prediction that the book is defensive
rather than high-returning: lower volatility and a shallower drawdown than the index, with no
expectation of a higher return. It forbids treating the filter as a return signal, and a book built
on it has to be judged against the same thirty names without the filter, not against cash.

**The caveats it carries.** One security, `MIC`, has no file at all. Four more — `CIT`, `FMC`,
`LCI`, `PARA` — carry adjusted prices that multiply by more than six in a day, which is a bad print
rather than a return, and are excluded by name in the rule. 265 of the 788 have no prices when the
long window opens in 2002, and 76 series end early, every one of them a real delisting.

<!-- example: end -->

---

## The experiments

Each experiment ranks its variants over **one window shared by all of them**, and those windows can
differ between experiments.

> **Compare a winner's Sharpe with its own experiment's control.** Windows can differ between
> experiments, so a winner is comparable to its own control row, not to another experiment's
> headline; `vs control` is the column to compare across experiments.

| Exp | Book | CAGR | Sharpe | Max DD | Control Sharpe | vs control | Status | Findings |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| **1** | the benchmark rule, in five words | | | | — | — | **the benchmark** | [`FINDINGS_1.md`](Experiments/Experiment_1/FINDINGS_1.md) |

<!-- example: begin -->

| Exp | Book | CAGR | Sharpe | Max DD | Control Sharpe | vs control | Status | Findings |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| **1** | thirty most traded, in an uptrend | **17.85%** | **0.861** | −30.5% | 0.831 | **+0.030** | **the benchmark** | [`FINDINGS_1.md`](Experiments/Experiment_1/FINDINGS_1.md) |

The control column is the **equalised** control — the same names with the filter off, trading on the
rule's own dates — because that is the arm differing in exactly one thing. Against the plain
control, which also trades a seventh as often, the Sharpe gap reads +0.048.

Window 2017-01-03 to 2026-06-01, 9.4 years, net of costs. The control is the same thirty names with
the trend filter switched off: it earns **more** (18.62% against 17.85%) at a worse Sharpe and a
9.3-point deeper drawdown. **The filter buys drawdown, not return.** Put on the rule's own
rebalance dates, so that it differs in one thing only, that control earns **18.97%** and the
filter's cost rises to **1.12 points a year**.

### The counterfactuals

Six more books, each removing one choice the rule makes. Idiosyncratic return, in percentage points
over the same window:

| Arm | What it removes | Idiosyncratic |
| --- | --- | ---: |
| The rule | — | 45.52 |
| The equalised control | the trend filter | 40.47 |
| The plain control | the filter, and 76 of the 87 rebalances | 32.09 |
| Random, five seeds | the liquidity ranking | −17.63 to 25.17, mean 12.5 |

**The random arm is why this matters.** A thirty-name book drawn at random earns positive residual
here too, so 45.5 is measured against roughly 12.5, not against zero. Genuine selection is nearer
**33 points**. Five seeds is five samples and the spread is 43 points wide, so the split is
indicative; what stands is that the rule sits above the random range's top.

### Against the world

| Book | CAGR | Volatility | Sharpe | Max drawdown |
| --- | ---: | ---: | ---: | ---: |
| The rule | 17.85% | 20.73% | 0.861 | −30.5% |
| The KN600 index | 14.71% | 19.01% | 0.774 | −33.8% |
| The rule, filter off | 18.62% | 22.91% | 0.813 | −39.8% |
| The rule, 2002-07-30 onward | 10.29% | 20.00% | 0.514 | −60.7% |

The long window starts 2002-07-30 rather than the blueprint's 2002-01-02: `SHY`, the cash proxy,
launched that day, and the engine cannot value a book whose cash has no price. Caveat 9 of
[`FINDINGS_1.md`](Experiments/Experiment_1/FINDINGS_1.md) carries it.

**Does it reproduce?** Within the same working copy, exactly: the notebook was re-run end to end on
2026-09-20 and every figure above came back identical — 17.85%, 0.8612, −30.54%, and 45.52
idiosyncratic points. From a wiped working copy on a fresh download, on 2026-09-22, to the data
rather than to the digit: the pipeline ran end to end with no manual step beyond the hand-supplied
index and factor files, every conclusion held, the filter-off control and the index came back to
every published decimal, and the rule moved by hundredths — 17.89%, 0.863, −30.55%, 45.44
idiosyncratic points, 86 rebalances against 87 — on a panel ten rows different, which is
limitation 5 below, measured. No figure above is changed by it;
[`FINDINGS_1.md`](Experiments/Experiment_1/FINDINGS_1.md) carries the re-run's figures beside
the published ones.

### The trial count

**Ten engine runs, all ten reported.** Four are strategy variants, specified before the engine ran:
the rule, the rule at realistic costs, the filter-off control, and the long window. **Six are
counterfactual arms** added on 2026-09-20 — the equalised control and five random books — whose
four possible outcomes were committed before they were priced, and none of which is a candidate for
the headline. **Three further runs are excluded by name**, below.

<!-- example: end -->

---

## What stands — reuse, do not rebuild

A result, a module or a method later work should start from rather than re-derive. One line each,
with its number.

<!-- example: begin -->

- **The panel and the pipeline.** 4.25M rows, 787 securities, 2001-01-02 to 2026-06-01, with the
  rank identity checked and the corrupted securities named. Any later experiment reads it unchanged.
- **The filter's drawdown effect.** −30.5% against the control's −39.8% on the same names, same
  sizing, same band. That is the one thing the trend condition demonstrably does.
- **The truncation check.** Three runs reported success while valuing a stub; comparing the valued
  window against the requested one caught all three. Every later experiment keeps it.
- **The random arm as a baseline.** Before calling a residual "alpha", price five random books of
  the same shape and subtract what they earn. Here that was 12.5 of 45.5 points — a quarter of the
  headline number — and no part of the factor model revealed it. Cheap, and every experiment that
  reports idiosyncratic return should run it.
- **The equalised control.** A control that differs in one thing has to match the rule's *trading*
  too, not only its selection. Matching dates moved the filter's measured cost from −0.77 to −1.12
  points a year.

## What is closed — do not re-propose without a new argument

Each rejected idea, with the number that rejected it. A negative result costs real work and stops
the next person repeating it; this list is where that value is stored.

- **The 50/200 filter as a return signal.** Closed by an information coefficient of 0.0112 at a
  month, −0.0060 at a year, and by the control beating the filtered book by 1.12 points a year. Do
  not re-propose it as an alpha source; it is a risk control.
- **The filter as protection against fast crashes.** Closed by 2020: no cash held at all through
  a 23-day fall. It steps aside from slow declines only.
- **This book as a defensive, low-beta position.** Closed by a beta of **1.028**, which falsified
  prediction 5 of `BLUEPRINT_1.md`: holding the most traded names in an uptrend is a full-beta
  equity position. It is shallower in drawdown than the index, and that is a different claim.
- **This book as lower-volatility than the index.** Closed by 20.73% against the index's 19.01%,
  which falsified prediction 1. Thirty names are more volatile than six hundred whatever the filter
  does; the filter's 2.2 points of volatility show only against the same thirty names unfiltered.

### The uncomfortable one

`OBJECTIVE.md` claim 1 says stocks whose 50-day average is above their 200-day "go on to earn more
than those whose is not". **On our own data, inside our own universe, they do not** — not by enough
to matter, and not once the same names are held without the filter. The claim survives only in a
weaker form: they earn about the same with less volatility and shallower drawdowns. The strategy is
defensible; the claim as written is not, and the next experiment should be an honest attempt to
kill it rather than to decorate it.

## Open leads, ranked

The single highest-value run outstanding, and what it would settle.

1. **Draw far more random books and report the percentile.** Five seeds put the baseline at 12.5
   points with a 43-point spread — enough to prove it is not zero, not enough to say what it is —
   and every share in the counterfactual table rests on it.
2. **The band, read as a curve**: 0%, 5%, 10%, 20%, 30%, everything else frozen. Claim 4 has never
   been tested, and the equalised control is the first evidence bearing on it — the same book at 87
   rebalances beat itself at 11, net of costs. Choose the band on turnover and persistence, never
   on the metric it will be judged by. A new experiment, not an edit to this one.
3. **The eleven sector factors read exactly zero** in the decomposition, which is not credible for
   a book whose technology weight moved between 15% and 45%. No sector claim stands until it is
   understood.
4. **Decompose the long window's −60.7% drawdown.** The nine-year and twenty-four-year records
   disagree about what this rule is.

<!-- example: end -->

## Excluded runs

Variants removed from the tables above rather than reported with a caveat. **A metric computed over
a truncated or rejected run does not belong in the same column as a complete one**, and excluding by
name with a reason is how that stays honest.

| Variant | Why |
| --- | --- |
| | what went wrong, how it was caught, and what now prevents it |

<!-- example: begin -->

| Variant | Why |
| --- | --- |
| Long window, 0.5% cash reserve | Valued only to 2003-04-22 of 23.8 years. The book could not pay commission at a rebalance — "Cash error on 2003-04-23 with $-416.34" — and the engine returned success with a clean summary over the stub. Caught by comparing the valued window against the requested one; the reserve is now an argument every run states |
| Long window, 1% cash reserve | The same failure in a different decade, valued to 2009-06-01. Both are in the trial count |
| Point-in-time, 0.5% cash reserve | Cash error on day one, when the book is entirely in the cash proxy and commission has nothing to come from |

<!-- example: end -->

## Known limitations

| # | Limitation | Effect |
| --- | --- | --- |
| 1 | **Nothing is out of sample.** No experiment has reached step 7 | Every number here is in-sample, and in-sample selection is what the deflation literature warns about |
| 2 | **No experiment has a control arm** differing in exactly one thing | Which lever earned a margin is inferred from per-lever rows, not measured |
| 3 | Classification buckets use today's labels, not point-in-time | Anything reclassified mid-window is misattributed before its move — the `current_*` prefix marks exactly this |
| 4 | Delisting exits use one day of hindsight | A position is sold on the last day it still has a fill price, knowable only the day after |
| 5 | Curator output is not reproducible across download dates | Dividend adjustment is computed from the present, so a re-pull rebases every adjusted column |
| 6 | The Deflated Sharpe Ratio has never been computed | The one number that would say whether a winner survives its own trial count |

<!-- example: begin -->

**Limitation 2 no longer holds in this example, and that is the one good piece of news in the
table.** Experiment 1 has a control arm differing in exactly one thing — the trend filter, on or
off, same universe, same sizing, same band **and the same rebalance dates** — which is why this
repository can say the filter costs 1.12 points a year instead of inferring it. Every other
limitation above stands as written, and limitation 6 now has company: the idiosyncratic share is
measured against a five-seed baseline, which is a floor on the honest figure rather than a
deflated one.

<!-- example: end -->

> **Under the bar in [`AGENTS.md`](AGENTS.md), most numbers above are a reason to run an experiment
> rather than a result.**
