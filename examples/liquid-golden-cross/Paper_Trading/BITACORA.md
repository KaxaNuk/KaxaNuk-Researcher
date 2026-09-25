# Paper Trading — step 7 of 8

The last step inside the Investment Lab, and the only one that runs on data the strategy has never
seen.

**In plain words:** a dress rehearsal on data nobody has seen yet. **It produces** out-of-sample
evidence and an operations checklist. **It prevents** finding the plumbing problems on day one of
funding.

A backtest tells you what a rule *would* have done; paper trading tells you what it *does* — on live
prices, with live universe changes, and with the delistings and corporate actions a historical file
has already tidied up.

Step 8, Production, is not here: a strategy leaves this repository when it is funded — real
capital, real monitoring, a real drawdown policy, step 8 of the KaxaNuk Strategy Template — and
where that is depends on whose desk it is.

> **This file is the gate, not a log.** `JOURNAL_N.md` means an append-only dated record inside an
> experiment folder; this document is a contract — what graduation means and what has to be true
> before it happens — so it carries a different name to keep the two from being confused.

## What graduation means

An experiment is **promoted**, not copied. `Paper_Trading/Paper_Trading_N/` mirrors the
`Experiment_N` it came from, so the lineage of a paper-traded book is never in question. The
experiment notebook stays where it is — it remains the record of how the rule was chosen.

## The gate

Strong backtest results are necessary and **not sufficient**. All five must hold.

| # | Criterion | Why it is on the list |
| --- | --- | --- |
| 1 | **Beats the benchmarks on risk-adjusted return** — above every benchmark it reports against, *and* above its own control row, over the same window. The control is the one its blueprint names: the same rule with one ingredient removed, trading on the rule's own rebalance dates | A strategy that only beats the index on raw return is usually just carrying more risk, and one that beats only a control trading on other dates has been compared on two things at once |
| 2 | **Attribution shows idiosyncratic alpha in both layers** — selection in the Brinson-Fachler cut, a residual the factor model cannot explain, and a selection story that survives the third pass on residual returns | If the return decomposes entirely into known factors, the honest product is a cheaper factor fund, not this |
| 3 | **Conclusions survive parameter perturbation, and the trial count is published beside the winner** | A result that appears at one threshold and vanishes at the next is a sweep artefact. Read the direction across a sweep, never the single best cell. Publishing N is the minimum — the five ways a backtest lies in [`../AGENTS.md`](../AGENTS.md), row 3 — and the sign-off states whether the deflated figure was also computed |
| 4 | **Costs and capacity are modelled and stated** — turnover, commission, and any assumption the engine does *not* model, borrow cost above all | The gap between a backtest and a fill is where strategies die |
| 5 | **Explicit sign-off** | Graduation is a decision, not a threshold that trips automatically |

Every criterion is evidenced from the experiment's `FINDINGS_N.md` and from
[`../RESULTS.md`](../RESULTS.md). **If it cannot be evidenced from those, it has not been met.**

### Criterion 2 is evaluable here, and that is not universal

This stack has a real attribution stage, so "is this selection, or a factor tilt?" is a question
with an answer rather than an admission. Repositories built on stacks without step 6 have to
substitute a beta-matched control book or an explicit regression on the market, and name the
substitute in the sign-off. **Here there is no substitute to name, which means there is also no
excuse.**

Expect a *pass with a qualification* rather than a clean pass. A book whose excess return is roughly
half factor exposure and half idiosyncratic has passed criterion 2 and has also been told exactly
how much of it is not the idea — which is what the criterion exists to surface, not a reason to
soften it.

## What a paper-trading run is

Unlike an experiment, this stage is **not** a notebook. It is a script that runs on a schedule,
because the question is no longer "what would this have done" but "what does it hold today, and
how is it doing".

**A graduated book is the strategy, frozen.** `promote.py N` runs once, after the sign-off: it
copies byte for byte, from the commit that graduated, every file the book needs to go from raw
prices to a priced book into `Paper_Trading_N/`, in the strategy's own layout, and writes
`FREEZE.json` with the commit, the date and the hash of each file. The rule itself goes into
`paper_trading_N.py`, copied from the experiment's cells and committed first. Every module resolves
its paths from its own folder, so the copies read and write inside the book's folder alone: the
experiments under construction can change the shared modules, and a graduated book never moves.
A repository can hold several books on paper and several experiments under construction at once.

**`daily_update.py` runs every graduated book once a day**, after the market closes:

- refreshes the shared raw prices once, or reads them from a database another machine published;
- checks the newest day before any book reads it, and stops every book on a close with no fill
  price or a move no price can make — a book on broken data is worse than none;
- runs each frozen book: its frozen refinery, its frozen rule from the experiment's first day,
  and the engine, twice — over the whole history, and since the day it was frozen;
- writes the record — the book in force, the engine's daily values and statistics, what the book
  looked like that day — to local files, a DuckDB database, or both, as `Config/.env` says;
- flags every diagnostic outside the band registered below, every failed check, an input that
  lags the day, and a **restatement**: a past value the engine now prices differently, which is
  flagged and never overwritten;
- exits 0, 1 or 2 — clean, flagged, failed — so a scheduler can tell.

One rule in that contract is worth repeating, because it is the whole point of the stage: **a
paper-trading script re-fits nothing.** A run that tunes anything is a backtest wearing a costume,
and it re-introduces exactly the search that produces negative out-of-sample performance. The
freeze is what makes the rule checkable: a book that changed on paper has restarted its paper
record.

**Months on paper cannot show skill.** Proving a good information ratio takes years, not a
quarter, so the daily record is read for whether the book behaves like its backtest — turnover,
holdings, exposure, costs — and never for a good month. What it can show in months is the plumbing,
which is what this step exists to find before money does.

## Before a book's first day

Each graduated book gets a section in *Current status*, written and committed before
`daily_update.py` first runs it, and never edited afterwards — a later observation is a new line
under it, dated:

- the experiment it mirrors, the variant, the commit and the freeze date;
- the gate, row by row, and the sign-off: a person's name and date;
- **the bands**: for each diagnostic `daily_update.py` reads, the range `FINDINGS_N.md` measured
  over the backtest, which the book's `BANDS` carries too;
- **the kill switch**: the result that retires the book instead of tuning it;
- the review dates, and the period it has to be watched before anyone proposes production;
- what the record cannot show, said before anyone is tempted to read it there.

## Current status

**Nothing has graduated. Nothing has been tested.** This is the template; the first candidate
arrives when an experiment's `FINDINGS_N.md` can evidence criterion 1.

<!-- example: begin -->

**In this example the gate has been tested**, against both designs of Experiment 1 and against
Experiments 2, 3 and 4, and none graduated: the rows are below. One book is on paper,
`Paper_Trading_4/`, Experiment 4's, as a candidate the owner chose to track without graduation: its
section below registers it before its first day, and *What is frozen here* says what else this
folder holds. The daily machinery has been run outside this repository, on a candidate frozen only
to test it: *The machinery, tested* below says what that showed, and why none of its figures is
read.

<!-- example: end -->

When one does, record it here: which experiment, which variant, which criteria it clears, and —
above all — which it does not and why. **The blocking items are the content of this section, not the
passing ones.**

**`Paper_Trading_1/` is named for the experiment it would mirror.** It becomes Experiment 1's
frozen book if Experiment 1 graduates; a later experiment that graduates takes its own number, and
until one does, this folder holds the contract and nothing else.

<!-- example: begin -->

### In this example: the gate run on Experiment 1's second design, and the answer is no

**Experiment 1's second design does not graduate.** It is the owner's rule, the twenty most traded
names above their 50/200 cross, sold the day after the cross breaks, and it was written to reach
paper trading if it passed. It failed its own kill switch first, and the gate says the same, row by
row. Every row is evidenced from
[`../Experiments/Experiment_1/FINDINGS_1.md`](../Experiments/Experiment_1/FINDINGS_1.md) and
[`../RESULTS.md`](../RESULTS.md).

| # | Criterion | Verdict | Evidence |
| --- | --- | --- | --- |
| 1 | Beats the benchmarks **and its own control** | **Fails** | Sharpe 0.8057 beats the index's 0.7699 and the control's 0.7748, but the rule earns **0.86 points a year less** than its control, where its blueprint required 0.5 points more, and it is ahead of the control on both Sharpe and CAGR in one sub-period of three. A pass on Sharpe alone is the single-metric pass this gate exists to catch |
| 2 | Idiosyncratic alpha in **both** layers | **Partly** | The factor model leaves 36.19 of the rule's 160.02 points of excess return unexplained, just above the top of five random twenty-name books, −11.78 to 35.31. But the control keeps 40.99 without the cross, so the signal subtracts idiosyncratic return rather than adding it, and the rule's Sharpe edge comes with a beta of 1.067 against the control's 1.238, which the blueprint reads as timing, not selection. The first cut is per asset in this library, so its selection of 12.26 points is not the group-level story the criterion asks for, and the third pass on residual returns has not been run |
| 3 | Survives perturbation; trial count published | **Passes, on its own rule** | 12 of 15 cells keep the sign of the rule's Sharpe margin over its control, where the blueprint asked for twelve. The trial count is published: thirty-one, as the blueprint fixed it, with this design's 45 engine runs listed by role. What passes is a Sharpe margin of +0.031 that comes with a CAGR margin below zero, and the deflated figure was not computed |
| 4 | Costs and capacity modelled and stated | **Met, capacity as a participation bound** | Turnover, target to target: 1.99 times the book a year, and 6.0% one-way per trade date on average. Costs are charged on the unadjusted price at two rows, the blueprint's commission setting of 0.1 and a realistic 0.005, with 5 basis points of slippage, and reported net: $76,911.00 of commission and $37,862.98 of slippage at the headline row. Capacity is stated from the book, as the largest book at which a trade takes no more than a share of the name's 63-day average traded value. At 1%: $91,546,647 for the worst trade, $146,012,883 at the first percentile of trades, $16,231,104,636 at the median. At 5%: $457,733,236, $730,064,416 and $81,155,523,178. The turnover and capacity figures are the reproduction's of 2026-09-24: the run of 2026-09-23 printed 2.9 times the book a year and $2,018,972 for the worst trade at 1%, read from the slot book's rows out of date order. It is a bound on participation, not a model of market impact, and which trade is the worst was not traced |
| 5 | Explicit sign-off | **Not sought** | Criteria 1 and 2 block it, and the kill switch had already tripped |

**On the seed of 1,500, described.** The notebook reads the whole seed, and run once on the seed
Experiment 2 widened it prints the same verdict, the rule 0.52 points a year behind its control and
ahead in one sub-period of three, with criterion 3 at 11 of 15 cells, one short of the twelve. The
rows above are the design's record, on the seed of 788.

### In this example: the gate run on Experiment 2, and the answer is no

**Experiment 2 does not graduate either.** It is Experiment 1's diagnostic arm, its rules
unchanged at a 5% cash reserve: the twenty most traded members of the index above their 50/200
cross, the whole set re-equalised only on a day it moves by three names or more, tested on
2002-07-30 to 2016-12-30, years it was not found on, with the seed widened to every listing the
index held since 2000. It was written to reach paper trading only by passing this gate, and it
failed its own kill switch first: ahead of its control on both Sharpe and CAGR in none of three
sub-periods. Every row is evidenced from
[`../Experiments/Experiment_2/FINDINGS_2.md`](../Experiments/Experiment_2/FINDINGS_2.md) and
[`../RESULTS.md`](../RESULTS.md).

| # | Criterion | Verdict | Evidence |
| --- | --- | --- | --- |
| 1 | Beats the benchmarks **and its own control** | **Fails** | Sharpe 0.2340 against the index's 0.4383 and the control's 0.2556; CAGR 4.23% against 8.57% and 5.87%. It trails both, on both measures, and the verdict is the same with every name filled at the close |
| 2 | Idiosyncratic alpha in **both** layers | **Fails** | Over 2008-01-14 to 2016-12-30 the factor model leaves the rule −7.93 idiosyncratic points and its control +30.24: the cross's share is −38.17. The first cut's alpha against the index is −42.29 points, of which selection +6.33 and interaction −48.84, per asset. The third pass has not been run, and 2002 to 2007 are not attributed |
| 3 | Survives perturbation; trial count published | **Fails** | The rule is ahead of its control on both Sharpe and CAGR in 1 of 10 cells, where the blueprint asked for eight. The trial count is published: forty-three, with this experiment's 34 engine runs listed by role. The deflated figure was not computed |
| 4 | Costs and capacity modelled and stated | **Met, capacity as a participation bound** | Turnover, target to target: 1.84 times the book a year, and 24.3% one-way per rebalance on average. Costs are charged on the unadjusted price at two rows, the blueprint's setting 0.1 and a realistic 0.005, with 5 basis points of slippage, and reported net: $265,535.20 of commission and $32,182.15 of slippage at the headline row. Capacity, from the book, measured as Experiment 1's was: at 1%, $3,851,439 for the worst trade, $7,019,368 at the first percentile of trades, $106,111,907 at the median; at 5%, $19,257,197, $35,096,840 and $530,559,534. It bounds participation and does not model market impact, and which trade is the worst was not traced |
| 5 | Explicit sign-off | **Not sought** | Criteria 1 to 3 block it, and the kill switch had already tripped |

Its blueprint also asked for a run from a wiped working copy: made on 2026-09-24, it printed every
figure the same. No book of Experiment 2 is frozen.

### In this example: the gate run on Experiment 3, and the answer is no

**Experiment 3 does not graduate either.** It is momentum proper on the same liquid names, claim 5
of `OBJECTIVE.md`: of the hundred most traded members of the index, the twenty with the highest
return over the twelve months before the latest one, equally weighted, re-struck on the first
trading day of each month, tested on 2002-07-30 to 2026-06-01 against the same pool's twenty most
traded on the same dates. It was written to reach paper trading, as `Paper_Trading_3`, only by
passing this gate, and it failed its own kill switch first: ahead of its control on both Sharpe and
CAGR in one sub-period of three. Every row is evidenced from
[`../Experiments/Experiment_3/FINDINGS_3.md`](../Experiments/Experiment_3/FINDINGS_3.md) and
[`../RESULTS.md`](../RESULTS.md).

| # | Criterion | Verdict | Evidence |
| --- | --- | --- | --- |
| 1 | Beats the benchmarks **and its own control** | **Fails** | Sharpe 0.4358 against the index's 0.5682 and the control's 0.4647; CAGR 10.81% against 10.99% and 11.03%. It trails both, on both measures, and the verdict is the same with every name filled at the close |
| 2 | Idiosyncratic alpha in **both** layers | **Fails** | Over 2008-01-14 to 2026-06-01 the factor model leaves the rule 82.30 idiosyncratic points and its control 87.88: the ranking's share is −5.59, and what it adds is the momentum line, 44.78 points against 16.77. The first cut's alpha against the index is +121.27 points, of which selection +27.74 and interaction +95.22, per asset. The third pass has not been run, and 2002 to 2007 are not attributed |
| 3 | Survives perturbation; trial count published | **Fails** | The rule is ahead of its control on both Sharpe and CAGR in 3 of 10 cells, where the blueprint asked for eight; four cells' rules could not be priced and count against it. The trial count is published: fifty-four, with this experiment's 36 engine runs listed by role. The deflated figure was not computed |
| 4 | Costs and capacity modelled and stated | **Met, capacity as a participation bound** | Turnover, target to target: 3.25 times the book a year, and 26.9% one-way per rebalance on average. Costs are charged on the unadjusted price at two rows, the blueprint's setting 0.1 and a realistic 0.005, with 5 basis points of slippage, and reported net: $780,587.10 of commission and $180,071.26 of slippage at the headline row. Capacity, from the book: at 1%, $6,933,709 for the worst trade, $27,864,836 at the first percentile of trades, $92,928,116 at the median; at 5%, $34,668,547, $139,324,178 and $464,640,582. It bounds participation and does not model market impact, and which trade is the worst was not traced |
| 5 | Explicit sign-off | **Not sought** | Criteria 1 to 3 block it, and the kill switch had already tripped |

Its run was made from a wiped working copy, as its blueprint asked, and the working copy printed
every figure the same. No book of Experiment 3 is frozen, and `Paper_Trading_3/` does not exist.

### In this example: the gate run on Experiment 4, and the answer is no

**Experiment 4 does not graduate either, and it came closest.** It is claim 5's second design:
Experiment 3's ranking held only outside bear markets, the most traded twenty inside them, at a 10%
reserve, with a check that ends a listing at its last distinct bar, tested on 2002-07-30 to
2026-06-01 against the pool's twenty most traded and required to beat the ranking held in every
month. It was written to reach paper trading, as `Paper_Trading_4`, only by passing this gate, and
it failed its own kill switch first, on one limb: its Sharpe margin over its control, 0.0084 where
0.03 was required. Every row is evidenced from
[`../Experiments/Experiment_4/FINDINGS_4.md`](../Experiments/Experiment_4/FINDINGS_4.md) and
[`../RESULTS.md`](../RESULTS.md).

| # | Criterion | Verdict | Evidence |
| --- | --- | --- | --- |
| 1 | Beats the benchmarks **and its own control** | **Fails** | CAGR 11.61% against the index's 10.99% and the control's 10.53%: ahead of both. Sharpe 0.4779 against the index's 0.5682 and the control's 0.4694: behind the index, and ahead of the control by 0.0084, short of the 0.03 the blueprint required. The verdict is the same with every name filled at the close |
| 2 | Idiosyncratic alpha in **both** layers | **Partly** | Over 2008-01-14 to 2026-06-01 the factor model leaves the rule 92.55 idiosyncratic points and its control 83.71: the ranking's share is +8.84, and the state's, against the arm, +13.49. The first cut's alpha against the index is +125.59 points, of which selection +26.49 and interaction +100.32, per asset. The third pass has not been run, no random books were priced, and 2002 to 2007 are not attributed |
| 3 | Survives perturbation; trial count published | **Fails** | Ahead of its control on both Sharpe and CAGR in 5 of 12 cells, where the blueprint asked for ten; every cell priced. The trial count is published: sixty-eight, with this experiment's 40 engine runs listed by role. The deflated figure was not computed |
| 4 | Costs and capacity modelled and stated | **Met, capacity as a participation bound** | Turnover, target to target: 3.06 times the book a year, 25.3% one-way per rebalance, 77.7% where the state turns. $882,137.50 of commission and $216,577.57 of slippage at the headline row; the realistic row, 0.005, reported beside it. Capacity at 1%: $6,933,709 for the worst trade, $29,839,031 at the first percentile, $107,323,816 at the median; at 5%, $34,668,547, $149,195,153 and $536,619,080. It bounds participation and does not model market impact |
| 5 | Explicit sign-off | **Not sought** | Criteria 1 and 3 block it, and the kill switch had already tripped |

Its run was made from a wiped working copy, as its blueprint asked. No book of Experiment 4 is
frozen, and `Paper_Trading_4/` does not exist.

### Paper_Trading_4 — Experiment 4, on paper as a candidate, not graduated

**Registered on 2026-09-25, before `daily_update.py` first ran the book, and never edited
afterwards: a later observation is a new line under it, dated.**

- **What it mirrors.** Experiment 4's rule as `experiment_4.ipynb` ran it, from `BLUEPRINT_4.md`: of
  the hundred most traded members of the KN US Equity 600, the twenty with the highest return over
  the twelve months before the latest one, re-struck on the first trading day of each month, and in
  a month that opens after a negative two-year return of the index, the pool's twenty most traded
  instead; the stale-bars check; and its control, the pool's twenty most traded, beside it every
  day. Its costs are the blueprint's: the commission setting 0.1, 5 basis points of slippage and a
  10% reserve, on $1,000,000. `Paper_Trading_4/paper_trading_4.py` carries the rule;
  `Paper_Trading_4/FREEZE.json` names the commit it was frozen at, the freeze date, 2026-09-25, and
  the hash of every frozen file.
- **The gate, and the exception.** It did not pass: criteria 1 and 3 fail, and 2 is partly met, as
  the rows above say, and no sign-off graduates it. **The owner decided on 2026-09-25 to track it on
  paper as a candidate**, from the options put to him — *"Paper-track Exp 4 as a candidate
  (Recommended)"* — so that the months after its test window become the unseen test its blueprint
  named. That is an exception to *What graduation means*, recorded here by name: this book is not a
  production candidate, nothing its record shows can graduate it, and a book reaches production only
  through an experiment that passes this gate.
- **The bands**, which `BANDS` in `paper_trading_4.py` carries: holdings at 20.0 on every day, as
  `FINDINGS_4.md` measured over the backtest; the invested share of the targets from 0.95 to 1.0,
  where the findings measured 100.0% on every day — the floor is a choice. The record keeps, with no
  band: effective names, the largest sector's share, the bear state at the prior close, the number
  of listings the stale-bars check ends, the trade dates in the last 63 days, and whether the book
  traded that day.
- **The kill switch: behaviour, never a month's return.** The book is retired, never tuned, if in
  any calendar month a data check or a frozen-input check stops it on more than five trading days,
  or its holdings leave their band on more than five. No performance figure alone retires it or
  promotes it: at each review the owner reads the record and writes a dated decision here.
- **The review dates:** 2026-12-31, 2027-03-31, 2027-06-30 and 2027-09-30. Each adds a dated line
  under this section: the book and its control since 2026-06-02, the first day the experiment never
  read, and since the freeze, from the record; the quarter's flags; and whether any month opened in
  a bear state. **The period before production:** none applies; this book is not a candidate for it.
- **What the record cannot show.** Skill: a year of paper cannot show an information ratio, as *What
  a paper-trading run is* says. Whether the state works: it was bear on 43 of the 288 entries of the
  backtest, and on none since November 2023, and a record with no bear month says nothing about it.
  What the backtest already priced: every figure before 2026-06-02 is the experiment's own window.
  And the index as it is: the desk's files end on 2026-08-14, so until they are refreshed membership
  and the state are held at that date and the book is priced against `SPY`, each day flagged.

### What is frozen here

`Paper_Trading_4/` is the one book frozen here, by `promote.py 4` on 2026-09-25, and the one
`daily_update.py` runs: its section is above, and its `FREEZE.json` names the commit, the date and
the hash of every file it froze. `Paper_Trading_1/paper_trading_1.py` still carries Experiment 1's
second design's rule in the form a frozen book takes, to show that form: nothing here froze it, its
`BANDS` are not registered here, and `daily_update.py` does not run it. The data stages processed
the months after 2026-06-01 when Experiment 1's download was refreshed through 2026-09-23; no rule
or engine run of Experiment 4 read them before the freeze.

### The machinery, tested

**A book that graduates should not be the first to find the plumbing's faults**, so the daily
machinery was run on 2026-09-24 in the working copy Experiment 1's second design ran in, outside
this repository, on that design frozen there as a candidate. The freeze was never committed there,
and nothing graduated: the gate above says why it could not. What the runs showed:

- **A dry run**, then **a real run for 2026-09-23**, writing the record to local files and to a
  DuckDB database. The two records are identical: 7,566 rows of performance, 102 of statistics, 40
  of books, 8 diagnostics, 2 flags and 1 run. It exited 1, flagged, and the two flags say why: the
  desk's holdings and the index's returns end on 2026-08-14, so membership is held at that date and
  the book is priced against `SPY` until the desk's files reach the day.
- **The same day again**: the row counts did not change.
- **The lock** refused a second run, with exit 2.
- **A restatement.** Frozen again, the book priced the past differently; the run flagged the
  restatement and overwrote nothing.

**The faults those runs found**, each fixed in this repository's code before any book depends on
it: the slot book's rows were out of date order, which also corrected Experiment 1's construction
and capacity figures; a window now prices only the listings it holds; a refused engine run stops
the book with the engine's reason; the band is read with a billionth of tolerance; and the record
replaces a day's flags and holdings whole on a re-run.

**What the runs cannot show.** They priced days after 2026-06-01, the months Experiment 1's
blueprint held out for a frozen book. No figure from them is read or reported here, and none would
count: the book was frozen to test the plumbing, not to start a paper record.

### What comes next

**The arm, on years it was not found on, failed too.** The diagnostic arm, twenty names on the
first design's rebalancing at a 15% band, reproduced the first design's delay and earned 1.65
points a year more than Experiment 1's rule. Experiment 2 took its design to 2002 to 2016 and set
it against the same names without the cross for the first time: it trails them there by 1.64
points a year, and on the years it was found on by 1.46.

**Momentum proper, on the same names, failed as well.** Experiment 3 ranked the hundred most traded
by their twelve-month return and held the top twenty: 0.22 points a year behind the same pool's
twenty most traded over 2002 to 2026, ahead of them in one sub-period of three, with a ranking that
adds the momentum factor and takes idiosyncratic return away.

**Held only outside bear markets, it came within one margin.** Experiment 4 led the same control by
1.08 points a year, in two sub-periods of three, and beat the ranking held in every month on both
measures, with a ranking that now adds idiosyncratic return; its Sharpe margin, 0.0084, is short of
the 0.03 the gate's first criterion was read against, and its perturbation reads five cells of
twelve. At the realistic commission both margins clear, and the verdict is read at the blueprint's.
Nothing is a candidate now, and no decision of the owner's on what follows is recorded.

**The first design's gate run**, thirty names on a 10% band, failed criteria 1 and 3 and met 2 and
4 only in part. It is kept at tag `v0.15.0` of the KaxaNuk Researcher.

**What the exercise is worth teaching.** A rule rewritten to fix the mechanism the first run blamed
failed its own test, and the arm built to confirm the blame beat it. Taken to years it was not
found on, and set against a control it had never faced, the arm failed its own test in turn. The
kill switches, the arm and the controls were all written down before the runs, which is what makes
each a result rather than a reason to tune the rule until it passes. A new signal on the same
names, chosen after all of it, failed the same way: a signal the analyzer can measure is not yet a
book that beats the same names without it, net.

<!-- example: end -->
