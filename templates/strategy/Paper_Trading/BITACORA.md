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

**Schedule it** after the US close, once the provider has the day. On Windows, from the strategy's
folder, once:

```bash
schtasks /Create /SC WEEKLY /D MON,TUE,WED,THU,FRI /ST 19:00 /TN "<strategy-name> daily update" /TR "cmd /c uv run --directory <full path of this folder> python Paper_Trading/daily_update.py >> <full path of this folder>\Paper_Trading\Logs\scheduled.log 2>&1"
```

On macOS or Linux, one line of `crontab -e`, in the machine's own time zone. `cron` does not read
your shell's `PATH`: give uv by its full path, which `command -v uv` prints.

```bash
0 19 * * 1-5 cd <full path of this folder> && <full path of uv> run python Paper_Trading/daily_update.py >> Paper_Trading/Logs/scheduled.log 2>&1
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

When one does, record it here: which experiment, which variant, which criteria it clears, and —
above all — which it does not and why. **The blocking items are the content of this section, not the
passing ones.**

**`Paper_Trading_1/` is named for the experiment it would mirror.** It becomes Experiment 1's
frozen book if Experiment 1 graduates; a later experiment that graduates takes its own number, and
until one does, this folder holds the contract and nothing else.
