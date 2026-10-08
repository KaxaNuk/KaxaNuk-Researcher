# Paper Trading — step 7 of 8

The last step inside this repository, and the only one that runs on data the strategy has never
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
`FREEZE.json` with the commit, the date and the hash of each file. The security master is the one
file not taken from the commit: the provider's data, it is copied from disk, hashed like the rest
and kept out of git, on the machine that froze the book. The rule itself goes into
`paper_trading_N.py`, copied from the experiment's cells and committed first. Every module resolves
its paths from its own folder, so the copies read and write inside the book's folder alone: the
experiments under construction can change the shared modules, and a graduated book never moves.
A repository can hold several books on paper and several experiments under construction at once.

**`daily_update.py` runs every graduated book once a day**, after the market closes:

- refreshes the shared raw prices once, or reads them from a database another machine published;
- checks the newest day before any book reads it, and stops every book on a close with no fill
  price or a move no price can make — a book on broken data is worse than none. It reads that day
  alone: a security's file that ends before it, and a bad bar between two runs, pass unflagged;
- runs each frozen book: its frozen refinery, its frozen rule from the experiment's first day,
  and the engine — over the whole history, over the days after the experiment's window, and since
  the day it was frozen;
- writes the record — the book in force, the engine's daily values and statistics, what the book
  looked like that day — to local files, a DuckDB database, or both, as `Config/.env` says;
- flags every diagnostic outside the band registered below, every failed check, an input that
  lags the day, and a **restatement**: a past value the engine now prices differently, which is
  flagged and never overwritten;
- exits 0, 1 or 2 — clean, flagged, failed — so a scheduler can tell; a step that raises is a
  failed day, with its traceback in the day's log.

One rule in that contract is worth repeating, because it is the whole point of the stage: **a
paper-trading script re-fits nothing.** A run that tunes anything is a backtest wearing a costume,
and it re-introduces exactly the search that produces negative out-of-sample performance. The
freeze is what makes the rule checkable: a book that changed on paper has restarted its paper
record.

**Months on paper cannot show skill.** Proving a good information ratio takes years, not a
quarter, so the daily record is read for whether the book behaves like its backtest — turnover,
holdings, exposure, costs — and never for a good month. What it can show in months is the plumbing,
which is what this step exists to find before money does.

## Running it daily

Once an experiment has graduated and `Paper_Trading/promote.py N` has frozen it,
`Paper_Trading/daily_update.py` runs every frozen book once a day. Try it by hand first, from the
strategy's folder:

```bash
uv run python Paper_Trading/daily_update.py --dry-run
uv run python Paper_Trading/daily_update.py
```

The first refreshes the prices, unless `--skip-refresh` is given, then checks, runs and prices
everything and writes no record; the second writes the record. Running the same day twice replaces
that day's rows instead of adding to them.

**Where it reads and writes** is set in `Config/.env`:

| Line | Values | What it does |
| --- | --- | --- |
| `PAPER_TRADING_INPUT` | `provider` or `database` | `provider` downloads the day's prices here, with the data key; `database` reads the prices another machine published, with no download and no data key |
| `PAPER_TRADING_SINKS` | `local`, `database`, `local,database` | `local` writes the record as CSV files in `Paper_Trading/Record/`; `database` writes the same tables to the database |
| `PAPER_TRADING_DATABASE` | a file, or `postgres:<connection string>` | a DuckDB file, by default `Paper_Trading/paper_trading.duckdb`; or a PostgreSQL server, reached through DuckDB |
| `PAPER_TRADING_PUBLISH_DATA` | `true` or `false` | with the database sink, also writes the refreshed prices there, for the machines that read them |

Each has a flag that overrides it for one run: `--input`, `--sinks`; `--as-of` runs a past day and
`--book` one book. **A local record is not a backup**: the provider restates its history, so a
day's inputs cannot be fetched again as they were. Keep the database sink on, or back the folder
up.

**A book's frozen security master travels by hand.** It is the provider's data, so `.gitignore`
keeps it out of git, as it keeps the one in `Universe/`: it stays on the machine that froze the
book. Back it up with the record, and bring it across before the first run anywhere else — the run
checks every frozen file against its hash in `FREEZE.json`, and stops a book whose files are
missing or changed.

**Schedule it** after the US close, once the provider has the day. On Windows, once, in Command
Prompt; in PowerShell it starts `schtasks --%`, and in Git Bash `MSYS_NO_PATHCONV=1 schtasks`:

```bat
schtasks /Create /SC WEEKLY /D "MON,TUE,WED,THU,FRI" /ST 19:00 /TN "<strategy-name> daily update" /TR "cmd /c uv run --directory \"<full path of this folder>\" python Paper_Trading/daily_update.py >> \"<full path of this folder>\Paper_Trading\Logs\scheduled.log\" 2>&1"
```

On macOS or Linux, one line of `crontab -e`, in the machine's own time zone. `cron` does not read
your shell's `PATH`: give uv by its full path, which `command -v uv` prints.

```bash
0 19 * * 1-5 cd "<full path of this folder>" && "<full path of uv>" run python Paper_Trading/daily_update.py >> Paper_Trading/Logs/scheduled.log 2>&1
```

The run's log is in `Paper_Trading/Logs/`, one file per day, and its exit code says how the day
went: 0 clean, 1 flagged, 2 failed. A step that raises exits 2 with its traceback in the day's
log, so a day whose log does not end in `done, exit code` is one to read. The redirect keeps, in
`scheduled.log`, what the run prints outside that log — the download, and an error raised before
the log opens; the folder exists once the run has been tried by hand, as above. The licensed
engine checks its licence online: without the network a saved check stands in for 3 days from
Backtest Engine 0.67.0, 7 on 0.66.0, so the machine needs the network that often — and on its
first run on 0.67.0, which does not read the older saved check.

> **For the agent.** Registering a scheduled task changes the machine: give the command and let
> the user run it. Never read the record's figures back as your own: they are the engine's, and
> you quote them with the file they came from.

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

**In a new strategy, nothing has graduated and nothing has been tested.** The first candidate
arrives when an experiment's `FINDINGS_N.md` can evidence criterion 1.

<!-- example: begin -->

**Experiment 1 graduated on 2026-10-06, and is on paper as `Paper_Trading_1`.** It was rewritten on
2026-10-06: the KN US Equity Core members above their 50/200 golden cross, ranked and weighted by
63-day traded value, no weight above 20% and none below 1%, rebalanced when the held set changes,
and judged against the KN US Equity Core, then `SPY`, and against the same rule with the golden
cross switched off. It is still the experiment every later one is judged against.
**Its gate was written before the run**, in the plan the owner approved on 2026-10-05, whose
decisions [`../Experiments/Experiment_1/JOURNAL_1.md`](../Experiments/Experiment_1/JOURNAL_1.md)
records in his words. **Criteria 1 to 4 pass**, from
[`../Experiments/Experiment_1/FINDINGS_1.md`](../Experiments/Experiment_1/FINDINGS_1.md) and
[`../RESULTS.md`](../RESULTS.md); **criterion 3 at exactly its bar, and criterion 2 thinly** —
nine tenths of the excess return is factor exposure, and the selection that survives the third pass
is 2.70 points over the window. The owner signed criterion 5 the same day, knowing both.

<!-- example: end -->

When one does, record it here: which experiment, which variant, which criteria it clears, and —
above all — which it does not and why. **The blocking items are the content of this section, not the
passing ones.**

**`Paper_Trading_1/` is named for the experiment it would mirror.** It becomes Experiment 1's
frozen book if Experiment 1 graduates; a later experiment that graduates takes its own number, and
until one does, this folder holds the contract and nothing else.

<!-- example: begin -->

### Experiment 1: the gate, written before the run

**The criteria and the falsifier are the blueprint's.** They sit under *Success criteria* and *What
would falsify it* in
[`../Experiments/Experiment_1/BLUEPRINT_1.md`](../Experiments/Experiment_1/BLUEPRINT_1.md),
written before any rule was coded. Three of these rules are stated only here, and the blueprint states the one on timing too; all
four, word for word:

- On the twenty random books of criterion 2: "All 20 are published."
- On the index: "Unpriced benchmark names are dropped per date and the rest renormalised; the
  dropped share is published per year."
- On timing: "The shifted-entry timing arm is **not run**, and the findings say so."
- On a failure: "If 1 to 4 do not all pass, nothing is frozen. The failure is reported as loudly as
  a pass would be, in `FINDINGS_1.md`, `RESULTS.md` and `BITACORA.md`."

`FINDINGS_1.md` keeps the first three under *Attribution*. The last did not apply: criteria 1 to 4
all passed.

**The verdict, row by row.**

| # | Criterion | Verdict |
| --- | --- | --- |
| 1 | Beats the benchmarks **and its own control** | **Passes.** Net, over 2015-01-02 to 2026-06-01, a Sharpe of 0.842 against the KN US Equity Core's 0.713, `SPY`'s 0.743 and the control's 0.763; margins over the control of +0.080 of Sharpe and +0.60 points of CAGR, where +0.03 and +0.5 were asked; both measures beaten in 2015–2018 and 2019–2022, not in 2023–2026, where the control earned 51.85% a year against 40.44%: 2 of 3, the bar |
| 2 | Idiosyncratic alpha in **both** layers | **Passes, thinly.** The precondition holds: the first cut's benchmark reconciles with the index's own returns within 0.54 points a year, inside 1.0. First-cut selection +17.44 points, per asset as the library computes it; the factor model's idiosyncratic return +13.84 points, above all 20 random books, every one negative; the third pass's selection +2.70 points. Nine tenths of the excess return, 123.50 of 137.35 points, is factor exposure, 88.10 of it the market — a pass with the qualification the criterion exists to surface |
| 3 | Survives perturbation; trial count published | **Passes, at exactly its bar.** 6 of the 8 perturbed settings keep the sign of the margin over their own control on both Sharpe and CAGR, and all 8 beat the KN US Equity Core on Sharpe; the two that do not are the cross's other pairs, 20/100 and 100/300, ahead on Sharpe and behind on CAGR. The trial count is 107 books, published in `RESULTS.md`, with the 2015 window counted beside it. **The deflated Sharpe was not computed** |
| 4 | Costs and capacity modelled and stated | **Passes.** Turnover 3.09 times the book a year, one way; $97,180 of commission and $101,621 of slippage on $1,000,000 over the window; at the realistic commission, 20.75% and a Sharpe of 0.860. Capacity as a participation bound: at 1% of a name's 63-day traded value, a $238.6 million book for the worst trade and $39.5 billion for the median; not a model of market impact. A long-only book: no borrow cost to state |
| 5 | Explicit sign-off | **Given** by the owner, on 2026-10-06, after reading the rows above: *"Sign it"* |

### Paper_Trading_1 — Experiment 1, graduated

**Registered on 2026-10-06, before `daily_update.py` first ran the book, and never edited
afterwards: a later observation is a new line under it, dated.**

- **What it mirrors.** Experiment 1's rule as `experiment_1.ipynb` ran it, from `BLUEPRINT_1.md`: a
  KN US Equity Core member at the prior close, its 50-day average above its 200-day at the prior
  close, and an FMP fill price that day and the next — a name whose prices are about to stop is sold
  the day before; ranked and weighted by 63-day traded value, none above 20%, added in rank order
  while the smallest weight stays at or above 1%; re-struck when the held set changes; `MNKKQ`,
  `NE`, `PCP` and `RAI` excluded by name. Its control, the same rule with the golden cross off on
  the rule's own dates, is priced beside it every day. Its costs are the blueprint's: the commission
  setting 0.05 on the unadjusted price, 5 basis points of slippage and a 1% reserve, on $1,000,000.
  `Paper_Trading_1/paper_trading_1.py` carries the rule; `Paper_Trading_1/FREEZE.json` names the
  commit it was frozen at, the freeze date, 2026-10-06, and the hash of every frozen file.
- **The gate and the sign-off.** Criteria 1 to 4 pass, as the rows above say, criterion 3 at
  exactly its bar and criterion 2 thinly. **Signed by Arturo Aguilar, the owner, on 2026-10-06**,
  asked *"Criterion 5: do you sign Experiment 1 into paper trading, frozen as of 2026-10-06, with
  criterion 2 passing but thin?"* and answering *"Sign it"*. The deflated Sharpe was not computed,
  and he signed knowing it.
- **The bands**, which `BANDS` in `paper_trading_1.py` carries: holdings from 18 to 61, as
  `FINDINGS_1.md` measured over the backtest; the invested share of the targets at 1.0, as measured
  on every day; the largest weight up to 0.20, the rule's own cap, its lower end not banded; and no
  name held with its cross at 0 at the prior close, which never happened. The record keeps, with no
  band: effective names, the largest sector's share, the trade dates in the last 63 days, and
  whether the book traded that day.
- **The kill switch: the blueprint's falsifier, read on paper days.** The book is retired, never
  tuned, if over its paper days it misses its control by +0.03 of Sharpe or +0.5 points of CAGR, on
  either cost row: the record prices the headline row every day, and the realistic row is priced at
  each reading from the book's own weight files with its frozen engine module. **Read first at the
  review of 2027-10-06**, and at each anniversary after; before then no performance figure retires
  or promotes it, and the bands only flag. Proposed from the blueprint and **confirmed by the owner
  on 2026-10-06**: *"Confirm as proposed"*.
- **The review dates:** 2027-01-06, 2027-04-06 and 2027-07-06, each reading the record's behaviour
  — holdings, turnover, invested share, flags — and adding a dated line under this section; then
  2027-10-06, which reads the kill switch. **The period before production:** the first year on
  paper, to that review; nothing proposes production before it is read.
- **What the record cannot show.** Skill: a year of paper cannot show an information ratio, as
  *What a paper-trading run is* says. What the backtest already priced: the book is priced from the
  experiment's first day, and every figure before 2026-06-02 is the experiment's own window; the
  record reports the days after it and the days since the freeze apart. The cost of the cross in a
  rally like 2023 to 2026, where the control beat the rule by 11.4 points a year: one year of paper
  will not settle it. And the index as it is: the desk's files end on 2026-08-14, so until they are
  refreshed membership is held at that date and the book is priced against `SPY`, each day flagged.

**2026-10-06 — frozen, and its first run.** `promote.py 1` froze the book at commit `62256e6`, freeze
date 2026-10-06; the rule file, `paper_trading_1.py`, is not among the files `FREEZE.json` hashes,
and its SHA-256 at that commit is `47258101ddd4b5fb3736f32495e87fe6f8285f5f83c27977493a3f9a7fa0b33f`.
A first freeze at `1526262` was removed uncommitted when the plumbing test found the seed closing
every live name on 2026-09-24; the book was frozen again on the commit that fixed it, and an
attempt at the first run, stopped before it finished, left one line that was moved out of the
day's log. The first run, for 2026-10-05, the last close before the freeze, exited 1 — flagged, by
the two flags every day will carry until the desk's files pass 2026-08-14: membership held at that
date, and `SPY` in the index's place. It holds 30 names, the largest 14.4%, all four banded
diagnostics inside their bands. **The frozen book is the experiment's book**: on every one of the
1,381 rebalance dates to 2026-06-01, its weights and its control's equal the experiment's weight
files exactly, and the engine's daily values equal the experiment's headline runs on all 2,869
days. Paper days count from 2026-10-06.

**2026-10-06 — what the days after the window already show, read and set aside.** Over 2026-06-02
to 2026-10-05, days no stage of the experiment read, the engine has the book at a 24.9% drawdown
from 2026-06-22 to 2026-07-29, against 2.0% for `SPY` over the same dates: a sell-off in the
memory, chip and optical names that held about seven tenths of the book's weight — `MU`, `SNDK`,
`INTC` and `MRVL` fell 39% to 55%. Checked against the desk's own index returns, which agree with
the provider's prices to 3.5 basis points a day on average through 2026-08-14, it is the market,
not the data. It is not a paper day and it reads no kill switch; it is what a book with four fifths
of its weight in one sector does when that sector turns, and the reason the largest sector's share
is watched at each review although it has no band.

**2026-10-07 — two figures above, traced to the price files on disk.** The four falls, in the
dividend-and-split-adjusted close from 2026-06-22 to 2026-07-29: `MU` 1,211.19 to 739.00, −39.0%;
`INTC` 140.94 to 81.88, −41.9%; `MRVL` 307.78 to 163.40, −46.9%; `SNDK` 2,273.73 to 1,015.89,
−55.3%. `CTVA`'s fall in *The machinery, tested*: its close went from 77.65 on 2026-09-30 to 12.57
on 2026-10-01, −83.8%. The files are the provider's and are rewritten by the next download, which
restates the adjusted columns; these are the values of the download of 2026-10-06. No scheduled
day has run yet: the daily task is not registered on this machine, and the only day logged is
2026-10-05, the first run by hand.

**2026-10-07 — in this copy.** `Paper_Trading_1/paper_trading_1.py` carries the template's
docstring, the example's markers and the Analytics Factory's name where it said the desk, so it
differs from the SHA-256 registered above, and `Data/Curator/custom_calculations.py` from
`FREEZE.json`'s `shared_inputs`. The frozen security master is not shipped, the library versions are
not locked, and the frozen reader names the files `KN_US_Equity_Core_Holdings.csv` and
`_Returns.csv`, which the Analytics Factory ships as `KN_US_Equity_Benchmark_*`. So
`daily_update.py` stops the book here: it is a record, frozen on 2026-10-06, and the frozen copies
keep the comments they had then.

### What is frozen here

`Paper_Trading_1/` is the one book frozen here, by `promote.py 1` on 2026-10-06, and the one
`daily_update.py` ran in the strategy's own repository: its section is above, and its `FREEZE.json`
names the commit, the date and the hash of every file it froze. Its frozen security master is the
provider's data and is not in the repository: it stays on the machine that froze the book, and that
hash names the copy. The record, in `Paper_Trading/Record/`, is not in the repository either; both
are backed up by hand, or the record is also written to the database sink `Config/.env` can switch
on.

### The machinery, tested

**A book that graduates should not be the first to find the plumbing's faults**, so the daily
machinery was run on 2026-10-06 in a scratch clone of this repository before the freeze, and then
for the book's first day here. What the runs found, each fixed before the freeze was committed:

- **The paper book would have emptied when the files of KaxaNuk's Analytics Factory ended.** It read
  membership from the refinery, which carries none past 2026-08-14; it now holds the membership the
  Analytics Factory last wrote.
- **The seed closed every live name on its source's last date**, 2026-09-24, so the refinery read
  no price after it and the dry run found no 2026-10-05 in its calendar. A live listing's span is
  open now; no number of the experiment moved, which the refinery's re-run showed file by file.
- **A step that raised exited 1**, the code of a flagged day, which on a book flagged every day
  would hide a crash. It exits 2 now, with its traceback in the day's log; tested by injecting a
  failure.

**What has not been tested yet: the scheduled day itself.** Every run here read the price files
already on disk. The scheduled run downloads the day first, through `Data/curator.py`, which took
1 hour 37 minutes on the morning of 2026-10-06; the first scheduled day is read by hand, its log
checked for `done, exit code`.

**Found, and left as they are, for the owner:** the newest-day data checks read only the newest day,
so a price file that stops early, or a bad bar between two runs, passes unflagged — `CTVA`'s
unadjusted fall of 84% on 2026-10-01, held by neither series, did; a restatement is flagged again on
every later run, and the day the Analytics Factory's index reaches the day, every past benchmark
row, priced against `SPY` until then, will flag as one; and the frozen seed fixes the universe, so a
name that joins the index after the freeze can never be held.

<!-- example: end -->
