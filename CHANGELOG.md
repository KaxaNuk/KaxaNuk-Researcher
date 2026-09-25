# Changelog for KaxaNuk-Researcher

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Releases are
tagged `vX.Y.Z`.

## [0.25.1] - 2026-09-25
The worked example stops publishing provider data: the security master `promote.py 4` froze into
`Paper_Trading_4/` — company names, ISINs, sectors and industries from FMP's profiles — left the
repository, as the master in `Universe/` never entered it. `.gitignore` keeps every book's copy
out, in the template and the example; the copy stays where the book was frozen, unchanged, its hash
in `FREEZE.json` still matching; and the example's `daily_update.py` checks every frozen file
against that hash and stops a book whose files are missing or changed. Strategy template 0.13.1,
example 0.18.1, `paper-trading-gate` 0.2.1; no frozen byte, rule or number moved. Earlier commits
still hold the file.

**What to do differently:** run `uvx --from apm-cli==0.29.0 apm update -g`. A copy of the example
made from now on has no frozen master: bring it across by hand from the machine that froze the book
before its daily run there. In a strategy of your own, add the template's `.gitignore` line, and
`git rm --cached` a frozen master already committed.
### Changed
- **`.gitignore`**, in the template and the example, keeps
  `Paper_Trading/*/Universe/Security_Master.csv` out of git.
- **The example's `daily_update.py`** checks each file `FREEZE.json` hashes before a book runs, and
  stops a book with `unfrozen-input` when one is missing or not the copy frozen; `promote.py` says
  the master stays on the machine when it freezes a book.
- **`paper-trading-gate`**, `SETUP.md` and `Paper_Trading/BITACORA.md` in the template and the
  example, and the docstrings of `promote.py` and `daily_update.py`, say the master is copied from
  disk, stays out of git and travels by hand.
### Removed
- **`examples/liquid-golden-cross/Paper_Trading/Paper_Trading_4/Universe/Security_Master.csv`**
  from the repository.

## [0.25.0] - 2026-09-25
The first two moves need nothing typed but answers and a go. `init-researcher` brings the package
to its newest version with `apm update -g` before it copies, so a home is always made from the
newest template with every command current, and hands over in two plain steps. `interview` deploys
the agent for the assistant it runs in and commits what it wrote, on the one go it already asks
for: the owner's go on its preview is their review, and the commit records it. The newcomer's path
in the README is four moves where it was five, and `SETUP.md` says the same. Home template 0.13.0;
`init-researcher` 0.3.0.

**What to do differently:** run `uvx --from apm-cli==0.29.0 apm update -g`, then `update` in your
home for the new paragraph of its README. A home whose interview already ran needs nothing else.
### Changed
- **`init-researcher`** runs `uvx --from apm-cli==0.29.0 apm update -g --yes` on the go, before the
  copy, and says the version installed; when the update fails it goes on with the version
  installed, naming it. Its plan says the assistant may ask to allow two commands, and it hands
  over as two numbered steps: open the folder in a new session, type `/interview`.
- **`interview`** deploys the agent with `apm install --target <this assistant>` and commits the
  files it wrote, by name, on the same go — asking for a git identity when the commit needs one,
  never inventing it — and its hand-over opens with the new session where the agent answers by
  name.
- **The README's path** is four moves; **`SETUP.md`**'s step 2 deploys the agent by hand only on a
  new machine or for another assistant.

## [0.24.0] - 2026-09-25
A researcher's home has `Studies/`, and a command to write in it: `study`. A study is the owner's
own work from the library — an idea that is not a strategy yet, or a decision, a plan or a brief
with no repository of its own — drafted from the owner's words, with every claim from the library
linked to its note and anything from outside it marked as not checked. A synthesis page says what
the library holds; a study says what the owner will do about it. The `Projects/` that 0.18.0
removed had no rule but *anything you ask for*; a study has a contract: one way from the notes,
words only, and it moves out, staying as the record, when it needs code or data or becomes a
strategy. The README opens with what the researcher is for, with a strategy or without one, and how
it grows with its owner. Home template 0.12.0; `read` 0.7.3, `query` 0.6.1, `init-researcher`
0.2.2; no strategy template, example or Lab skill changed.

**What to do differently:** run `uvx --from apm-cli==0.29.0 apm update -g`, then `update` in your
home: it brings `AGENTS.md`, `README.md` and the empty `Studies/` across and, on your go, moves what
a `Projects/` still holds into `Studies/`, at the same depth, so its links into `Knowledge/` still
resolve. Then by hand, if you like: `Studies/` among the places your agent never writes, `study`
among what it names, and a state on the first line of each file that moved. `study` appears in a
new session.
### Added
- **`study [subject]`**, the twelfth command: asks what you want to work out, walks the library for
  what supports it, what argues against it and the simpler rival, names the gaps as leads, and on
  your go writes one study in `Studies/`, whose first line gives its state — *idea*, *active*,
  *parked*, *closed* or *moved to `<path>`*. With no subject it lists the studies and offers the
  open ones and the reading questions that feed a decision no study works out yet. A revision
  starts from the notes written since the study's date and keeps every line you wrote. Home only.
- **`Studies/` in the home template**, empty, with its row in `AGENTS.md`'s folder table and a
  section *Studies* that is its contract.
- **What you can use it for**, at the top of the README and of the home's *Working with it*: a
  library you can ask, your studies, lessons, strategies, any other project, and a researcher that
  grows with you, each with the command that does it.
### Changed
- **`update`** moves what a home's `Projects/` holds beyond its lessons into `Studies/`, one
  `git mv` per file or folder, never onto one that exists, where it left it for the owner; and
  brings `Studies/.gitkeep` to a home without the folder.
- **`interview`**'s agent never writes in `Studies/` and names `study` for a write; its hand-over
  offers `study`.
- **`read`** never writes in `Studies/`, and its report names an open study a new note bears on,
  with the `study` that would revise it.
- **`query`** names a study that bears on a question as the owner's work, never as evidence, and
  never modifies one.
- **`audit`** reports a study's broken links, a link into `Extracts/` or to a PDF, and a first line
  with no state, and never touches `Studies/`.
- **`next`** offers `study` at home once its checklist is done; **`init-researcher`** names the
  empty `Studies/` in its plan.
- **The release check** deploys 12 commands.

## [0.23.0] - 2026-09-25
The worked example puts a book on paper for the first time: Experiment 4's, momentum held only
outside bear markets, as a candidate the owner chose to track without graduation, so that the
months after its test window become the unseen test its blueprint named. The exception is recorded
by name in the example's gate document, with the book's bands, kill switch, review dates and what
its record cannot show registered before its first day; `promote.py 4` froze it, and
`daily_update.py` runs it every day, to local files, a DuckDB database or both. Example 0.18.0; no
skill, command, rule, agent or template changed.

**What to do differently:** run `uvx --from apm-cli==0.29.0 apm update -g`, so that `init-example`
copies the example with its paper book; in a copy, schedule `Paper_Trading/daily_update.py` as its
`SETUP.md` says.
### Added
- **The example's first paper book**, `Paper_Trading/Paper_Trading_4/`: the frozen rule, its
  control, the frozen modules and `FREEZE.json`, run daily by `daily_update.py`.
- **Its registration** in the example's `Paper_Trading/BITACORA.md`, written before its first day:
  the exception to graduation, the bands, a kill switch on behaviour, quarterly reviews, and what a
  year of paper cannot show.

## [0.22.0] - 2026-09-25
The worked example opens and reports Experiment 4, claim 5's second design: the same momentum
ranking held only outside bear markets, a negative two-year return of the index, after which Daniel
and Moskowitz find every one of momentum's fifteen worst months. It earns 11.61% a year at a Sharpe
of 0.478 over 2002-07-30 to 2026-06-01, 1.08 points a year ahead of the same pool's twenty most
traded and ahead of the ranking held in every month, but 0.0084 of Sharpe ahead where 0.03 was
required: it fails its kill switch, and nothing graduates. It was run from a wiped working copy.
Example 0.17.0; no skill, command, rule, agent or template changed.

**What to do differently:** run `uvx --from apm-cli==0.29.0 apm update -g`, so that `init-example`
copies the example with Experiment 4. Its analyzer's new rows read the desk's index returns, as the
experiments' membership already does.
### Added
- **Experiment 4 in the example**, from brainstorming to findings, with its blueprint committed
  before any rule, reviewed cold by the blueprint critic and revised on every point; a check that
  ends a listing at its last distinct bar, so that no run was refused; and a diagnostic arm the
  rule has to beat, so that the state earns its place against its simpler baseline.
- **Daniel & Moskowitz (2013)** in the example's `Bibliotheca/`, carried from a researcher's
  library, with the warning its home note carried above the Paleologo chapter it contradicts.
- **Momentum by market state** in the example's analyzer.
### Fixed
- **Experiment 3's notebook** names its own blueprint and reserve in the comment above its costs.

## [0.21.0] - 2026-09-25
The worked example reports Experiment 3. Momentum proper on the same liquid names — of the hundred
most traded members of the index, the twenty that rose most over the twelve months before the latest
one, re-struck monthly — earns 10.81% a year at a Sharpe of 0.436 over 2002-07-30 to 2026-06-01,
against the same pool's twenty most traded at 11.03% and 0.465, and fails its kill switch; claim 5
is falsified for that design, and nothing graduates. It was run from a wiped working copy, and
Experiment 2 was reproduced from one, every figure the same. Example 0.16.0; no skill, command,
rule, agent or template changed.

**What to do differently:** run `uvx --from apm-cli==0.29.0 apm update -g`, so that `init-example`
copies the reported example. Quote Experiment 1 from its record on the seed of 788, at `v0.18.0`:
the example's `FINDINGS_1.md` now describes what its notebook prints on the widened seed, the same
verdict with one perturbation cell fewer keeping its sign.
### Added
- **Experiment 3's findings**, in the example: the predictions, the kill switch, the book, its
  capacity, the perturbation with four cells the engine could not price, each counted against the
  rule as the blueprint fixed, the trial count of fifty-four, and an attribution that finds the
  ranking a momentum tilt with less idiosyncratic return than its control. The gate's rows, the
  results record and the objective's claim 5 follow from them.
- **Experiment 1 on the seed of 1,500, described**, in the example's `FINDINGS_1.md`, so the
  figures a copy made now prints are on record.
### Changed
- **Experiment 2's reproduction** from a wiped working copy is recorded, and its blueprint's fifth
  success criterion met.
### Fixed
- **Experiment 3's notebook** names a run the engine cannot price instead of stopping at it, and
  its verdict cell names claim 5.

## [0.20.0] - 2026-09-24
The worked example opens Experiment 3 before its rule, and the interview offers three more hints.
Experiment 3 tests momentum proper on the same liquid names — of the hundred most traded members of
the index, the twenty that rose most over the twelve months before the latest one — against the same
pool's twenty most traded, as claim 5 of the example's objective, added for it. Its blueprint is
committed, reviewed cold and revised, before any rule; the refinery gains the twelve-month return,
and the analyzer measures it. The interview offers three more hints and asks no more questions:
question 5 offers a clause naming who keeps taking the other side of the trade, and four ways an
edge's shelf life might run, the one that follows from where the owner says the edge comes from
listed first; question 3 folds *Add one of mine* and *Change or drop one* into one option and offers
a rule in the slot it frees. Home template 0.11.0. Example 0.15.0.

**What to do differently:** in a home, run `update`; then, by hand in `RESEARCHER.md`, add the rule
*Every design is challenged before it runs, and every idea tried is counted* if you want it. To be
offered the new hints, run `interview force`: every answer you keep is written back verbatim. To
study Experiment 3 before its result, run `init-example` after `uvx --from apm-cli==0.29.0 apm
update -g`.
### Added
- **Experiment 3's blueprint, brainstorming entry and first journal entry**, in the example,
  before any rule: the twenty of the hundred most traded members with the highest twelve-month
  return before the latest month, re-struck monthly, against the pool's twenty most traded with a
  momentum value, on 2002-07-30 to 2026-06-01, with a kill switch over three sub-periods, ten
  perturbation cells and a trial count of fifty-four.
- **Claim 5 in the example's objective**, momentum among the most traded, in the owner's words, with
  the note that it was chosen before the analyzer measured it and written after.
- **`r_momentum_12_1` in the example's refinery**, and its measurement in the analyzer: rows 19 to
  30 of `RESULTS.md`, on the widened panel.
- **Question 5 offers the other side of the trade**: after the testable sentence, a clause the owner
  may fill or leave — *…and ___ keeps taking the other side because ___* — the other side as the
  reading map's anatomy of an idea gives it, who sells to you and what keeps them doing it. Its
  blanks are never filled for the owner, and a clause left blank is left out.
- **Question 5 offers the shelf life as four options**, in its one message, the owner's own words
  as welcome: outlasts publication, a risk someone is paid to carry; shrinks as others learn it, a
  mistake others repeat or information; lasts while the obstacle does, others cannot take the other
  side; comes and goes. The option that follows from the `Edge from?` pick comes first. They are
  the package's own hint, not the deck's, which asks only whether an edge is paid risk or
  mispricing: no option names a work, and the reading map is unchanged.
- **A rule offered in question 3**: *Challenge my design before it runs, and count every idea I
  try*, written under *Non-negotiables* as *Every design is challenged before it runs, and every
  idea tried is counted*. The home's `RESEARCHER.md` offers it beside the fourth (home template
  0.11.0), never as a default.
### Changed
- **Question 3's rules keep four options**, the question tool's limit: *Add one of mine* and
  *Change or drop one* are one option, *Add, change or drop one*, and a rule typed under *Other* is
  its line.
- **A shelf life picked from the options** is written to `RESEARCHER.md` by its label, with any
  words the owner added; `Philosophy/HOW-I-INVEST.md` takes only their own words, as before.

## [0.19.0] - 2026-09-24
The worked example runs and reports Experiment 2, on a seed widened to every listing the index held
since 2000. Experiment 1's diagnostic arm, its design taken to 2002-07-30 to 2016-12-30 with the
names that left the market fetched from Sharadar, trails the same names without its cross by 1.64
points a year and fails its kill switch, so nothing graduates and claim 1 stays falsified, now on
two windows. The example's universe changed: Experiment 1's figures stand at `v0.18.0`, on the
788-name seed. Example 0.14.0; no skill, command, rule, agent or template changed.

**What to do differently:** run `uvx --from apm-cli==0.29.0 apm update -g`, so that `init-example`
copies the new example. Quote Experiment 1's figures from `v0.18.0`, on the 788-name seed: a copy
made now holds the widened seed, and no recorded run gives what Experiment 1 prints on it. To fetch
Experiment 2's names, a copy needs a Sharadar key and a Data Curator with the Sharadar provider, as
the example's `SETUP.md` says.
### Added
- **Experiment 2's run and findings**: its blueprint revised once, to a 5% cash reserve, after its
  first run could not be priced; its journal's later entries, its notebook and `FINDINGS_2.md`; and
  the gate's rows in `BITACORA.md`. It has not been reproduced from a wiped working copy.
### Changed
- **The example's seed is widened** to every listing the index held since 2000: 1,500 identifiers,
  712 of them marked `sharadar` in its `provider` column.
- **The example's `RESULTS.md`, `OBJECTIVE.md`, README and `AGENTS.md`** are compiled from both
  experiments' findings, and the README names Experiment 1's rows as the 788-name seed's, at
  `v0.18.0`.

## [0.18.0] - 2026-09-24
The worked example reports Experiment 1's second design and opens Experiment 2, and a researcher's
home keeps its lessons in `Lessons/`. Experiment 1's second design is run, reported and reproduced
from a wiped working copy: it beats the index on Sharpe, earns 0.86 points a year less than the same
names without its cross, and fails its kill switch, so nothing graduates. Experiment 2, its
diagnostic arm's design on years before 2017, is committed as a blueprint before its rule. A new
home has no `Projects/`: `teach` writes to `Lessons/<topic>/`, and anything else asked for at home
is answered in chat. Home template 0.10.0, strategy template 0.13.0, example 0.13.0,
`init-researcher` 0.2.1, `read` 0.7.2, `attribution-analysis-runs` 0.2.9.

**What to do differently:** run `uvx --from apm-cli==0.29.0 apm update -g` and open a new session.
In a home, run `update`: it brings `AGENTS.md` and `README.md` across and, on your go, moves each
`Projects/Teach/<topic>/` to `Lessons/<topic>/`. In a strategy, take the template's 0.13.0 files by
hand, as its entry lists them. Quote the example's Experiment 1 exits, entries, turnover and
capacity from its reproduction of 2026-09-24, never from its run of 2026-09-23.
### Added
- **Experiment 1's second design, reported** in `FINDINGS_1.md`, `RESULTS.md` and the gate's rows,
  and reproduced from a wiped working copy on 2026-09-24, with one manual step, every engine and
  attribution figure to the digit, on the 788-name seed.
- **Experiment 2 in the worked example, before its rule**: its brainstorming, a blueprint reviewed
  cold by `blueprint-critic`, the first entry of its journal, and its findings, not yet run. None of
  its results is in this release.
- **A second price provider**: in the example's `Data/curator.py`, `--provider sharadar`, for the
  names FMP does not carry, through the Data Curator's `issues/31` branch until a release carries
  it; in the strategy template, a line of the Curator stage's contract for names the first provider
  does not carry.
### Changed
- **A home has no `Projects/`** (home template 0.10.0). `teach` keeps each topic in
  `Lessons/<topic>/`; `update` offers, on the owner's go, to move a home's `Projects/Teach/<topic>/`
  there and to remove a `Projects/` left empty; `interview`, `init-researcher` 0.2.1 and `read`
  0.7.2 name `Lessons/` where they named `Projects/`.
- **The desk's folders**: the strategy template, the example and `attribution-analysis-runs` 0.2.9
  name the Analytics Factory's `Benchmark Portfolios/` and `Factor Models/`, read first, and the
  older `Benchmarks/` and `Factors/`, still read where those are absent.
- **The findings template's status**, in `experiment-lifecycle`'s reference and the strategy
  template, asks whether the rule beat the benchmark and its control by what its blueprint required,
  and whether it is a candidate for the gate.
- **The README's `paper-trading-gate` row** names the freeze, the daily run and its record.
### Fixed
- **The example's slot book is in date order**, which corrects Experiment 1's exits, entries,
  turnover and capacity as its run of 2026-09-23 printed them; no engine figure moved. The faults
  the paper-trading machinery's first runs found are fixed with it: a window prices only the
  listings it holds, a refused engine run stops the book with the engine's reason, a band is read
  with a billionth of tolerance, a stale lock is removed, and the record replaces a day's flags and
  holdings whole on a re-run.

## [0.17.0] - 2026-09-23
The researcher is its owner's, and grows with what they believe. The interview asks what pulls the
owner to markets and how they like to invest, puts the view that leads as one testable sentence
with a shelf life, and asks the smallest test that could kill it; its rules are offered as ones
many researchers start with, to keep, change or add to, with a fourth to keep or leave. The reading
map gains Section 02 of the bootcamp deck, *Where Alpha Comes From*, as hints that `interview`,
`objective` and `blueprint` offer as questions, never as a position to adopt. Home template 0.9.0,
`read` 0.7.1.

**What to do differently:** run `uvx --from apm-cli==0.29.0 apm update -g` and open a new session.
In a home, run `update`: it brings the new line of `README.md` across; then, by hand in
`RESEARCHER.md`, add the fourth non-negotiable if you want it. To be asked the new questions, run
`interview force`: every answer you keep is written back verbatim. In a strategy, `objective` now
offers each claim its source of edge, other side, test and kill switch, and `blueprint` asks the
seven questions before any backtest and the kill switch; answer what you like and skip the rest.
### Added
- **Section 02 in the reading map** (`read` 0.7.1), pages 55 to 60 of the deck, as hints: the five
  sources of edge and the question each asks, the six places ideas come from and how each fools
  you, seven questions before any backtest, an idea's anatomy — the claim, the source of edge, the
  other side, the test, the kill switch — and the three discussion questions.
- **`interview` asks how the owner likes to invest**: `Your method`, a fourth question in question
  4 — rules I can write down and test; judgment, case by case; judgment designs it, rules run it;
  not sure yet. It places nothing on the map and never leads.
- **Question 5 proposes the view as one testable sentence** — if this holds, I would measure that,
  because of this source of edge — for the owner to edit or refuse, and asks how long they would
  give the edge; question 6 asks the smallest test that could kill the belief beside what they
  would see if they were wrong. What they keep is written verbatim.
- **A fourth rule, offered**: a strategy graduates only against criteria written down beforehand,
  never on a good month. `interview` writes it when picked; the home's `RESEARCHER.md` offers it.
- **`objective` offers each claim its anatomy**, and **`blueprint` asks the seven questions before
  any backtest and names the kill switch in the falsifying condition** — asked, never required.
### Changed
- **The interview's rules are the owner's**: question 3 states three rules many researchers start
  with, never "KaxaNuk's three", keeps the fact that in a KaxaNuk strategy the numbers come from
  the Lab's libraries, and is multi-select — keep the three, add the fourth, add one of mine,
  change or drop one.
- **`Edge from?` takes the deck's five sources of edge** in four options — paid for a risk others
  avoid; a mistake others repeat; others cannot take the other side; something I see or do better
  — with *not sure yet* typed under Other, which counts as *Not sure yet*.
- **Question 2 asks what about markets pulls the owner in**, the puzzle they most want to
  understand, which question 6 can take as a reading question.
- **The home** (template 0.9.0): `RESEARCHER.md`'s non-negotiables guidance offers the three as a
  start and the fourth to add; `README.md` says in one line that the researcher is yours, growing
  with what you believe, with the package's hints to make complex ideas simple.

## [0.16.0] - 2026-09-23
Paper trading gets its machinery, and Experiment 1 can graduate. A graduated book is the strategy
frozen: `promote.py` copies every file it needs, byte for byte, into `Paper_Trading_N/`, and
`daily_update.py` runs every frozen book each day — refresh, check, rule, engine — and keeps the
record in CSV files, a DuckDB database or both, set in `Config/.env`. The benchmark is now what
`BRAINSTORMING_1.md` names; Experiment 1 is the first rule tested against it, and a rewrite of it
is written down as one. The desk's index and factor files are read in place, in their own names.
The worked example's Experiment 1 is being rewritten: its second blueprint is committed here,
before any rule. Strategy template 0.12.0, example 0.12.0.

**What to do differently:** run `uvx --from apm-cli==0.29.0 apm update -g` and a new session. In a
strategy, take the template's 0.12.0 files by hand, as its entry lists them. Put the desk's folder
in `KN_ANALYTICS_PATH` rather than renaming its files into `Data/Curator/`; a drop-in copy must now
keep the desk's names and headers. Name the benchmark in `BRAINSTORMING_1.md` and hold Experiment 1
to it like any other experiment. When an experiment graduates, write its rule into
`paper_trading_N.py`, commit, run `promote.py N`, register the book in `BITACORA.md` before its
first day, and schedule `daily_update.py` as `SETUP.md` shows.
### Added
- **The daily run of a paper book**, in the template as contracts and in the example as code:
  `Paper_Trading/promote.py` freezes a graduated experiment into `Paper_Trading_N/` with
  `FREEZE.json`; `daily_update.py` refreshes the prices once, checks the newest day, runs each
  frozen book's refinery, rule and engine over the whole history and since the freeze, and exits
  0, 1 or 2; `record.py` keeps six keyed tables, upserted, with a restatement flagged and never
  overwritten, in local CSV files, a DuckDB file, or a PostgreSQL server through DuckDB. Four
  `PAPER_TRADING_*` settings and `KN_ANALYTICS_PATH` join `Config/.env.template`; `duckdb` and
  `pyarrow` join `pyproject.toml`; `.gitignore` ignores each day's output.
- **`Data/hand_supplied.py`**, the one reader of the desk's index holdings, index returns and factor
  files, in place from `KN_ANALYTICS_PATH` or from the drop zones, in the desk's own names and
  headers; the Curator's index staging, the universe notebook, the experiment and
  `attribution_analysis.py` read through it.
- **`Data/curator.py --end-date`**, with a resume by the date each file was fetched through and a
  retry on a request that hangs, so paper trading can refresh through the day.
- **`BITACORA.md` *Before a book's first day***: the section each graduated book gets, committed
  before its first run — bands, kill switch, review dates, what the record cannot show. SETUP's
  *Paper trading, daily* says how to run, configure and schedule it.
- **In the example**: the analyzer measures the cross as a 0/1 state and what a name earns after
  its cross breaks; Experiment 1's second blueprint, its brainstorming and journal entries, and the
  measurements in `RESULTS.md` it cites.
### Changed
- **The benchmark is named in `BRAINSTORMING_1.md`** — an index, an ETF or an equal-weight book of
  the universe — and Experiment 1 is the first rule tested against it, able to graduate. Its rules
  still freeze once its findings report; a rewrite the owner decides is written down as one. The
  template's `AGENTS.md`, README, blueprint, journal, notebook and `BITACORA.md`,
  `experiment-lifecycle` 0.10.0, `paper-trading-gate` 0.2.0 and `blueprint` say so.
- **`paper-trading-gate` 0.2.0** covers the freeze, the daily run and the registration before day
  one; it still never declares graduation, computes a number or re-fits.
- **`attribution-analysis-runs` 0.2.8** says the desk's files are read as shipped.
- **`Experiments/backtest_engine.py`** takes the benchmark as an argument, for a paper window past
  the index's last date.

## [0.15.0] - 2026-09-23
A blueprint now meets a critic before the go, and the bar it is held to asks for more: a control
that differs in exactly one thing, one falsification condition fixed before the rule, and the
horizon and overlap beside every ratio. Each experiment names the claim it moves, every notebook
ends in a Verify section that raises, a figure is quoted only from the file that owns it, and APM
is pinned at 0.29.0. Home template 0.8.2, strategy template 0.11.0, example 0.11.0.

**What to do differently:** run `apm --version`; on anything but 0.29.0, run
`uv tool install apm-cli==0.29.0` first, as `SETUP.md` now pins it, and never `apm self-update`.
Then `uvx --from apm-cli==0.29.0 apm update -g` and a new session, which brings the new agent,
`blueprint-critic`. In a home, run `update`: it brings `AGENTS.md` and `.gitignore` across; change
the second non-negotiable in `RESEARCHER.md` by hand, as the home's changelog shows, and
`git rm --cached` any PDF already committed outside `Sources/`. In a strategy, the next
`BLUEPRINT_N.md` names the claim it moves, a *Control* line in *Rules* and *What would falsify it*,
with the changes that may not rescue it; its `FINDINGS_N.md` and the *Claim moved* column of
`RESULTS.md` say which claim moved; a coefficient or ratio carries its horizon, its overlap and the
share of dates with the expected sign; and each notebook ends in a Verify section. A strategy made
from an earlier template takes the new sections by hand, as the template's 0.11.0 entry lists them.
### Added
- **`blueprint-critic`, the package's first agent**, in `.apm/agents/`. It reads a draft blueprint
  cold, with the strategy's bar, `OBJECTIVE.md`, the notes cited and *Before any experiment*, and
  returns objections only, each with the line and the evidence; it writes nothing and the owner
  decides. `blueprint` hands it the draft before the go, and reviews the draft itself against the
  same seven items where no subagent can be called. `SETUP.md`'s done check looks for it, and the
  README and `AGENTS.md` name it.
- **Three items at the end of a strategy's bar**, so the first eight keep their numbers: a control
  on the rule's own rebalance dates, one falsification condition and the changes that may not
  rescue it, and the horizon and overlap beside the share of dates with the expected sign. The
  blueprint gains *The claim this moves*, a *Control* line and *What would falsify it*; the
  findings and `RESULTS.md` say which claim moved (`experiment-lifecycle` 0.9.0,
  `paper-trading-gate` 0.1.1).
- **A Verify section at the end of every notebook**, which reads back what the notebook wrote and
  raises, and counts the days the engine valued against the window's trading days, never a fixed
  floor. In the example it is code, and skips where no licensed engine is installed; nothing has
  run it end to end yet. The example's analyzer writes `overlap_days` and `share_expected_sign`,
  and its README says, stage by stage, what a correct run shows, from recorded figures only.
- **`query`'s *Numbers*** (0.6.0): a performance figure is quoted only from `FINDINGS_N.md`,
  `RESULTS.md` or the analyzer section it cites, named beside it, never recomputed, rounded,
  combined or carried to another strategy. `read` (0.7.0) and its `note.md` keep a paper's figure
  the paper's.
- **Four more checks in `audit`**: a note whose `read` field does not say what was read, a claim
  status outside the template's vocabulary, a strategy's own performance figure found in neither
  its findings nor `RESULTS.md`, and, under `deep`, a part of `BIBLIOGRAPHY.md` whose sources only
  agree.
- **`library_version`** in the frontmatter of `backtest-engine-runs` 0.1.6,
  `attribution-analysis-runs` 0.2.7 and `portfolio-construction-runs` 0.2.4: the build each was
  written against, to compare with the installed one before trusting a trap. `references/api.md`
  lists the `portfolio_stats` keys the example reads, and says their risk-free rate and
  annualisation are not verified.
### Changed
- **APM is pinned at 0.29.0** in the README, `SETUP.md`, `update` and the strategy template's
  `SETUP.md`, and every command in the README, `SETUP.md` and `update` that runs APM names
  `apm-cli==0.29.0` itself, `uvx --from apm-cli==0.29.0 apm ...`, so a newer `apm` on the path
  cannot run it. Measured on Windows: 0.29.0 installs this package cleanly; from 0.29.1 on, APM
  stages a package under about 148 more characters of folders, the worked example's longest paths
  pass the 260-character limit, and the install fails with `WinError 3` or `WinError 206`. `update`
  checks the version first and installs 0.29.0 before the update.
- **A change to the package is tried by a project-scope install** of the working tree from a short
  scratch folder with the pinned APM, the `git ls-files` copy the fallback; before a release, 16
  skills, 11 commands, 4 rules and 1 agent install with no warning. `AGENTS.md` names the lines the
  100-column rule exempts, forbids a literal tab, says what a second package with a same-named
  skill or command does, and points to the home's and a strategy's own rules. The README says what
  the researcher will not do. `.gitignore` ignores what the copilot target writes in `.github/`.
- **The commands follow the template more closely.** `objective`, `audit` and `next` accept a
  note, `RESULTS.md` or the findings that measured a claim, or nothing for a claim true by
  construction; `blueprint` reads the strategy's bar and lists what the draft lacks before the go;
  `challenge` always checks the trial count the findings owe, and quotes the git log as the
  evidence the blueprint came first; `next` recognises the worked example and sends the owner to
  `init-strategy`; `interview` and `update` copy a missing home file with `scaffold.py --only`.
- **The home** (template 0.8.2): interview's one write to `Philosophy/HOW-I-INVEST.md` is named; a
  strategy with no claims reads nothing in; the hypothesis non-negotiable matches `AGENTS.md`;
  `read` proposes questions when *What you are reading for* is empty; the primitives table names
  all 16 skills, 11 commands, the agent and the house instructions; `.gitignore` ignores every PDF
  and `.env` files.
- **`data-analyzer-runs`** (0.2.0) matches the notebook: its section table ends in *7 · Verify*,
  with what that section reads back and raises on, and section 4 reports the share of dates with the
  expected sign and the overlap, *h − 1* days, beside the IR.
- **The writing commands refuse the worked example**: `objective`, `blueprint`, `brainstorm` and
  `challenge` stop in it, and `audit` reports there without appending to its log, each with the
  test `next` uses and naming `init-strategy` for a strategy of one's own.
- **A blueprint is filled when it carries its *Written* line.** `blueprint`, `challenge` and
  `next`'s part E test for the `**Written YYYY-MM-DD, before any rule was coded.**` line
  `blueprint` writes, where each had its own test; `blueprint`'s draft replaces each heading's
  guidance paragraph. `blueprint-critic` objects only to what the draft wrote, not to the
  template's guidance or, in the worked example, to anything outside the example's own lines.
- **`next` and `challenge` follow the claim the blueprint names.** `next`'s part H and `challenge`'s
  closure check read the claim under *The claim this moves* and the status `FINDINGS_N.md` says it
  reached, against `OBJECTIVE.md` and the *Claim moved* column of `RESULTS.md`; a blueprint that
  names none falls back to the statuses in `OBJECTIVE.md`. `backtest-engine-runs`' *Read the run
  before believing it* points to the experiment notebook's Verify section, and the worked example's
  99% and five-day rule.
- **`read`** documents what `extract.py` reports — the extract folder's slug, `OUTLINE.md`, a
  chapter *not written* or *thin*, exit 1 as a mistake in the command — and warns that a text
  clipping in a strategy is committed. The three `init-*` skills (0.2.0) say what to do when a git
  step fails.
### Fixed
- **`scaffold.py` refuses a copy too deep for Windows** without long paths: a plan whose longest
  path would reach 260 characters, or whose deepest folder 248, exits 1 with nothing written,
  naming the path and the longest destination that fits, where it failed partway with a traceback.
  `init-researcher`, `init-strategy` and `init-example` say so.
- **`next`** leaves an untracked source under `Sources/` to its own row, sends a home that is not a
  git repository to the commands that finish it, and names a worked example one level down as the
  example, for reading.
- **`read`** counts a section of angle-bracketed slots as empty, stops with `interview` in a home
  not yet interviewed, and never takes a `.gitkeep` for a source; `note.md` names a source with no
  author or no printed year by its organisation or project and `ND`, as the worked example does.
- **`audit`** exempts a paper's figure quoted in any of the strategy's documents through a note it
  cites, matches a figure at the precision quoted, takes a *No note yet* row for a lead, reports
  missing local copies once, *on this machine*, and audits a strategy alone when no home is in the
  session. Its one log line is named as the one write made without a go, there and in the home's
  `AGENTS.md`.
- **`update`'s `check`** reports a dirty tree as a line instead of stopping, and a home at or
  ahead of the template's version is current, with nothing proposed for removal.
- **`init-researcher`'s plan** names every file the script copies. The worked example's README
  says it is for reading and running, not copying.
- **`scaffold.py --only`** refuses an absolute path, or one that leads outside the starting point
  or the destination, and writes nothing.
- **`scaffold.py` without git** keeps the copy, exits 0 and prints the git commands left to run,
  where it ended in a traceback; git's output is decoded as UTF-8 and printed safely, and a failed
  `git init` or `git add` prints the commands that finish the job.
- **`extract.py`'s help** named the extract folder by the PDF's stem, where the script writes a
  slug, and did not say that a command argparse rejects exits 2.

### Removed
- **The worked example's `uv.lock`.** The example resolves its library versions when `uv sync`
  runs; a strategy made from the template still commits its own lock, as its `SETUP.md` says.

## [0.14.4] - 2026-09-23
The package's own `.gitattributes` leaves it.

**What to do differently:** nothing. A clone on Windows now takes its line endings from git's own
setting, so `scaffold.py` copies what the clone holds; the researcher home, the strategy template
and the example keep their `.gitattributes`, so a new home or strategy still commits LF.
### Removed
- **`.gitattributes`** at the root, and its row in the README's file map.

## [0.14.3] - 2026-09-23
The repository's own tests and tools leave it: what stays is the package users install, and the
two starting points, kept in step by hand. Strategy template 0.10.5, example 0.10.6.

**What to do differently:** before a commit, run ruff and the Bloom Code check as the README's
*Development* shows. Keep the template's copy of a shared file in step with the example's by hand,
in the same commit. Before a release that changes a skill, a command or a script, walk the
newcomer's path by hand in a scratch folder. The tests and the tools stay in the history at
`v0.14.2`.
### Removed
- **`tests/`**, 145 tests of the skills' three scripts and of the two tools.
- **`tools/check_repo.py`**, which checked versions, headings, markers, the section symbol, skill
  descriptions, generated files, path length and width before a commit.
- **`tools/sync_investment_lab_references.py`**, which generated the template's shared files and
  `experiment-lifecycle`'s references from the worked example.
- **The pytest settings and the dev dependencies** in `pyproject.toml`, and the pytest and coverage
  lines in `.gitignore`.
### Changed
- **`AGENTS.md`** says the template's shared files and `experiment-lifecycle`'s references change
  by hand, in the same commit as the example's; the skills' scripts are tried by running their
  skill in a scratch folder; ruff and the Bloom Code check pass before a commit.
- **`experiment-lifecycle` 0.8.3** says its references are kept in step with the example by hand.
- **The README's *Development*** lists the two checks that remain and what is done by hand.

## [0.14.2] - 2026-09-23
The behavioural evals leave the package: they ran once, cost about $30 a run, and needed a tool
nobody on the team had installed. A release that changes a skill is checked by walking the
newcomer's path by hand instead.

**What to do differently:** before a release that changes a skill or a command, walk the path in a
scratch folder — `init-researcher`, `interview`, `next`, `init-strategy`, and `read` on one
clipping. The evals stay in the history at `v0.14.1`, to restore the day a release needs them.
### Removed
- **`evals/`**, its 13 cases, 48 triggering requests and README; **`tools/eval_run.py`,
  `eval_fixtures.py` and `eval_history.py`**; and their 74 tests. Their one run, the pilot of
  0.12.0, found three real faults in `blueprint`, `brainstorm`, `challenge` and `query`, all fixed
  then; no run followed through 0.13.0, 0.14.0 and 0.14.1, and the cases covered none of the
  commands those releases changed.
### Changed
- **The README's *Development*** says how a release that changes a skill is checked, and its file
  map and `AGENTS.md` no longer name the evals.

## [0.14.1] - 2026-09-23
Kept clean and to the point: what nothing used is gone, every test can fail, and every eval can
run. Home template 0.8.1, strategy template 0.10.4, example 0.10.5.

**What to do differently:** `apm update -g`, then a new session. In a strategy made from an
earlier template, delete `apm.yml`: a strategy installs nothing, and nothing read it. In a home,
`update` lists the two blockquotes of `Knowledge/INDEX.md` and `Knowledge/LOG.md` to bring
across by hand.
### Removed
- **`.github/CODEOWNERS`.** It asked for a review when a pull request opened; work lands on `main`
  directly, so it had nothing to do.
- **The obsidian-vault-kit notice**, from `LICENSE`, the home's `LICENSE` and both READMEs:
  `LICENSE` is the MIT licence alone.
- **`apm.yml` from the strategy template and the worked example.** `SETUP.md` step 5 renames and
  versions `pyproject.toml` alone, and `tools/check_repo.py` reads a strategy's version there.
- **17 of the 18 eval cases that needed a shell**: the `init-example`, `init-strategy` and
  `init-researcher` copy cases, `read`'s extraction cases and their four quality cases. None had
  ever run, nine could not start for want of a history, and the team has no host whose sandbox
  runs a shell. The three `init-*` skills keep their triggering evals, and their scripts keep
  their unit tests. With them go the runner's `--no-shell` flag and the four fixtures only they
  used, and `contract/query/cites-notes`, whose graders now sit in `quality/query/claims-trace`,
  the same run.
- **`evals/findings/2026-09-22-pilot.md`**, the record of one past run; it stays in the history at
  `v0.14.0`.
- **Tests that repeated another test**, each covered by the test that stays, and the tests of the
  fixtures and the flag that went with the shell cases.
- **From the README**: the *Three commands make every folder* section, which repeated *The path*;
  the maintainers' paragraph on example markers; *Forking this package*, now one rule in
  `AGENTS.md`; the history of where the skills came from.
### Changed
- **Tests that could not fail now can.** Four Bloom Code tests passed with or without the code
  they name; each now breaks when that code does. New tests cover what a user relies on and
  nothing tested: `scaffold.py` copies byte for byte, finds a user-scope install, copies one file
  with `--only` and writes nothing before a refusal; `extract.py` writes a whole paper with its
  page markers and exits 3 for `--chapters` with no outline; the sync tool renames Experiment 1's
  documents to Experiment N. Each was checked by breaking the code in a scratch copy.
- **Every eval case runs**: `init-researcher`'s refusal when a home exists no longer needs a
  shell; the cases with a home beside the strategy check that the home is read; `clipping-at-home`
  checks the clipping is read rather than finding its name in the prompt; a regex that could not
  match a namespaced command is fixed. `evals/README.md` describes the 13 cases and 9 fixtures
  that exist, and its example commands run.
- **A file a strategy made before template 0.10.0 lacks comes back from the template**, through
  `init-strategy`'s script with `--only`, which never overwrites: in the README, `blueprint`,
  `brainstorm`, `experiment-lifecycle` 0.8.2, `data-curator-custom-calculations` 0.3.3 and
  `universe-point-in-time` 0.1.7, which sent the owner to the example and to deleting its lines by
  hand. `init-example` 0.1.4 copies a worked file into a folder of its own, to read beside yours,
  never into a strategy.
- **The home**: `Knowledge/INDEX.md` and `LOG.md` name the synthesis page `query` keeps; a
  version-history clause leaves the strategy table in `AGENTS.md`.
- **The strategy template**: `AGENTS.md` says in one paragraph where the template and the example
  live; the README's researcher paragraph names the command for each part of the order of work;
  `tools/check_repo.py`'s width check reads `templates/strategy/`.
- **Smaller**: `extract.py` says *no chapter written* where it wrote the outline; `SETUP.md` names
  the four agents that take the researcher's agent; `how-we-work` says a strategy tags the version
  its `pyproject.toml` declares; `tools/check_repo.py` reads a folder's version from `apm.yml`
  where it has one and from `pyproject.toml` otherwise; `evals/README.md` no longer documents the
  two grader types no case uses.

## [0.14.0] - 2026-09-23
The final cleaning before a newcomer meets the package: work lands on `main` without a pull
request per change, the loose ends of two closed pull requests are settled, the path from install
to first strategy is checked sentence by sentence, and the way a researcher grows beyond the
KaxaNuk Lab is written down. Home template 0.8.0, strategy template 0.10.3, example 0.10.4.

**What to do differently:** commit on `main`; open a branch and a pull request only for a change
you want reviewed. `apm update -g`, then a new session. In a home, run `update`: it brings the
home's files to template 0.8.0 and lists what is yours to edit by hand — the first
non-negotiable, the table heading *The strategies and projects it works on*, and the home's own
version in `apm.yml`. To teach your researcher a tool or a project, read *Growing your
researcher* in the home's README.
### Added
- **Growing your researcher**, a section of the home's README: a tool's or a project's
  documentation into `Sources/Clippings/`, then `read`; a skill or command of the home's own; a
  line under *What you are reading for*; a line by hand under *How it speaks* or *Non-negotiables*.
  The package README, the interview's hand-over and `next` point to it. *Joining other projects*
  in the home's `AGENTS.md` says who copies a project's files — the researcher names them and gives
  the command, the owner runs it, so `Sources/` stays the owner's — and how a clipping is named
  and a private repository cited. `read`'s `note.md` gives the convention for a tool's
  documentation as a source.
- **`next` knows more states.** A project the researcher joined through `--add-dir`, which is
  neither a home nor a strategy, is recognised and sent to *Joining other projects*, never to an
  `init-*` command; a home or strategy one folder down is named. At home it checks a clean tree
  first, skips `.gitkeep`, and lets the owner drop a *Find first* work that cannot be found; in a
  strategy, a claim carried into the blueprint as a lead counts at B, and a missing engine or
  attribution licence skips G rather than blocking it.
- **A home is committed.** The interview's hand-over, `read`'s close and `next`'s first check at
  home say to review the diff and commit; `SETUP.md` step 2 says what done looks like.
- **`update` compares in both directions** and reads `includes` and `dependencies` in `apm.yml`,
  so a home that ran it four times no longer keeps what the template dropped; the template's
  `RESEARCHER.md` and `HOW-I-INVEST.md` headings and the `INDEX.md` and `LOG.md` blockquotes come
  back as lines to edit by hand. `audit` checks a home's own skills and commands for a stale
  install.
- **The interview** proposes the home README's opening paragraph, sets the home's `apm.yml` version
  to 0.1.0, which is the owner's from then on, and says who holds `LICENSE`.
- **A strategy-side command with no home in the session** — `objective`, `blueprint`,
  `brainstorm`, `challenge` — works from the strategy alone and says so; `challenge` says it covers
  the graduation gate. `read` never offers `scaffold.py` into a strategy made from another
  template, and appends to a `LOG.md` only if it exists.
- **`tools/check_repo.py` checks width**: no line of markdown prose past 100 columns in `.apm/`,
  `templates/researcher/`, `README.md`, `SETUP.md` and `AGENTS.md`, with its tests. 236 lines in
  the Lab skills and their references were rewrapped to pass it, no word changed.
- **Three eval fixtures and three contract cases**: `blueprint` and `read` in a strategy with the
  home beside it, and `read` on a markdown clipping at home. The strategy fixtures without a home
  now test the no-home fallback on purpose.
- **`.github/CODEOWNERS`** names Alan and Arturo as the owners of every path, so a pull request,
  when one is opened, asks for their review at once. Taken over from pull request #11, which closed
  unmerged.
- **"Forking this package"** in the README: what a fork keeps, the three places that name this
  package, and one researcher package per user until two are tested side by side.
### Changed
- **Work lands on `main`.** `how-we-work` 0.3.0, this repository's `AGENTS.md` and the strategy
  template drop the issue, the branch and the pull request as a gate for every change: each
  change-set is committed on `main` with its changelog entry, and a branch is for a change someone
  wants reviewed, deleted once merged. A blueprint is committed in a commit of its own before the
  rule, which keeps the control without a branch.
- **The numbers rule names the engines the project names** — in a KaxaNuk strategy the Lab's
  libraries — in `RESEARCHER.md`, the interview, the agent it writes, the home's `AGENTS.md`,
  `query` and `objective`, so a researcher invited into a project on another stack is not told to
  distrust that project's own engine.
- **The home reads as a researcher's, not only an investor's**: *What it changes* in a note is
  measured against the owner's question; *The strategies and projects it works on*; *How it cites*
  in any other project; `HOW-I-INVEST.md` may take other headings. The README says the interview
  and the reading map cover investment research, and `read` names the map's ten papers only when
  Finance is a domain.
- **`query` 0.5.0** writes a kept synthesis page's index line and a log entry on the same go, and
  may name a work on a *Find first* line or already in `Sources/`.
- **`experiment-lifecycle` 0.8.1** describes the template as it has been since 0.10.0 — every file,
  each a description to fill in — and `references/structure.md` is at template 0.10.3.
- **Where things land**: `init-strategy` runs from the home and the strategy lands beside it, as
  `SETUP.md` and the README now say; the three `init-*` skills say how a fork passes `--package`;
  `scaffold.py` leaves cache folders behind, with tests.
- **The README** lists `evals/` and `.github/`, the eval scripts under `tools/`, and says the four
  house instructions are machine-wide for Claude Code and Copilot. `AGENTS.md` gives a route for
  trying a change that does not stage the working tree under HOME.
- **`tools/check_repo.py`** reads a folder's `uv.lock` only when git tracks it, and leaves the
  example's `CHANGELOG.md` out of the headings check: the template and the example move together
  but take their own version numbers.
### Fixed
- **`experiment-lifecycle` section 6** had a sentence cut mid-clause since 0.11.0; the paragraph is
  restored.
- **Smaller slips**: `next [strategy]` in the README; `interview` lists four agent targets, not
  `opencode`; `update`'s migration text is only for a home from before 0.7.0; the Data Curator
  skill compiles with `uv run --no-project`; the reading map sends a book to `Sources/Books/`;
  `note.md`'s Paleologo path; the home's example path is `fcf-yield-quality`, not a folder of the
  maintainer's; `evals/README.md` counts ten other commands.
### Removed
- **`docs/superpowers/`**, the eval work's design, plan and Windows notes, which 0.12.0 and 0.13.0
  shipped to every install because the package installs whole. They stay in the history at
  `v0.12.0` and `v0.13.0`. Taken over from pull request #9, which closed unmerged, with the
  addendum it added to `evals/findings/2026-09-22-pilot.md`: the blueprint surface re-run on the
  merge of 0.11.0, F-01 and F-03 holding on what `main` ships.

Left for later, as leads: a weight-matched null and a one-ingredient control in the template's
bar, a read-only `gate` command, evals for `interview`, `next` and `update`, `update` building its
URL from the installed package, and the legacy paths for homes before 0.7.0 and strategies before
0.7.15 and 0.10.0, which leave together at 1.0.0.

## [0.13.0] - 2026-09-23
The interview is `interview`, and the example researcher is no longer named after a real one.

**What to do differently:** run `interview` where you ran `researcher-init`; `apm update -g`
removes the old command and deploys the new one. In a home, `update` brings the wording across.
### Changed
- **`researcher-init` is renamed `interview`.** Two commands that were the same two words in
  either order — `init-researcher` makes the home, `researcher-init` filled it — were the first
  thing newcomers mixed up. The command is unchanged inside; every place that named it — the
  README, `SETUP.md`, `init-researcher` 0.1.2, `next`, `audit`, the reading map, the home's own
  files (home 0.7.3) and the evals — says `interview`.
- **The example researcher is `Ada`**, in the README, `SETUP.md`, `init-researcher`, the
  interview, the home's `AGENTS.md`, the eval fixtures and their tests, where it was the
  maintainer's own researcher's name. The worked example's `Bibliotheca/` keeps its provenance
  lines as they were written: they record which library its notes were carried from.

## [0.12.0] - 2026-09-23
Behavioural evals for the skills and commands, from issue #3, and the three fixes their pilot
found — merged from `issues/3` with the eval suite extended to the two skills 0.11.0 added.

**What to do differently:** `blueprint`, `brainstorm` and `challenge` take the experiment number
first: `blueprint 1`, `brainstorm 2 "an idea"`, `challenge 1 D:\Research\Golden-Flow`.
`apm update -g` brings it; in a home, `update` brings the example in `AGENTS.md` across.
### Added
- **`evals/`**: triggering requests for every skill, contract cases for `read`, `query`,
  `blueprint` and the three `init-*` skills, quality cases judged against written criteria, the
  pilot's findings, and `tools/eval_run.py`, `eval_fixtures.py` and `eval_history.py` with their
  tests, run by Claude Code's `claude plugin eval` against a real install of the working tree.
  `evals/README.md` says how; `docs/superpowers/` holds the design, the plan and the Windows notes.
  Two triggering entries are new here, for `data-analyzer-runs` and `paper-trading-gate`.
### Fixed
- **`blueprint`, `brainstorm` and `challenge` bound the experiment number to the strategy's
  path** (F-01): the optional strategy was declared first, and a harness binds arguments by
  position, so `/blueprint 1` read `1` as the path. The experiment comes first now, and
  `brainstorm` quotes a multi-word idea. Home 0.7.2.
- **`query` named works from memory** where the reading map has none (F-02): outside the map it
  now names only the kind of source. `query` 0.4.1.
- **`blueprint` deleted the template's blockquote when it wrote** (F-03), against its own text:
  the blockquote stays whole, its last line addressed to the owner.
- **The eval runner's fixture folder collided with the case's `FIXTURE` file on Windows**: the
  two names differed only by case, so every fixture case was refused as runner-written and five
  tests failed here. The folder is `fixture-files/`.

## [0.11.0] - 2026-09-22
The path is shorter to follow: a `next` command says where you stand, the order of work is
lettered so it is never mistaken for the eight steps, the interview shows its shape first, and the
two stages that had no skill — the analyzer and the paper-trading gate — have one.

**What to do differently:** run `apm update -g`, then open a new session; in a home, run `update`
to bring `AGENTS.md`'s lettered order of work across. When lost, run `next`.
### Added
- **The `next` command** — where the owner stands, at home or in a strategy, and the one thing to
  do next with the command that does it. It reads the folder against a checklist — the interview,
  the agent, the sources without a note at home; setup, then the order of work A to H in a
  strategy — and writes nothing. The README, the home's README and `researcher-init`'s hand-over
  point to it.
- **`data-analyzer-runs`**, the skill for the last block of step 3, `Data/analyzer.ipynb`, the one
  Lab module still hand-rolled and until now without a skill: the notebook's sections and what each
  measures, the information coefficient per date and on the eligible pool, the rank identity, the
  separation of return from volatility, what look-ahead costs a fitted signal, and where the
  numbers go — `RESULTS.md` first, then a blueprint's predictions by section number. Written from
  the worked example's notebook and nothing else.
- **`paper-trading-gate`**, the skill for step 7: the five criteria of `Paper_Trading/BITACORA.md`,
  how each is evidenced from `FINDINGS_N.md` and `RESULTS.md`, the usual way each fails, the
  promotion, the contract of the two scripts — a paper-trading run re-fits nothing — and what the
  assistant never decides: graduation is a person's signature.
### Changed
- **The order of work is lettered A to H**, in the template's README, the home's `AGENTS.md`,
  `experiment-lifecycle` and the commands that cite it, so *item 5* can no longer be read as
  *step 5*: the universe is C and step 2, the cycle is G and steps 4 to 6. The sentence *items are
  not steps* was the symptom. Template 0.10.2, home 0.7.1, `experiment-lifecycle` 0.8.0, `read`
  0.6.1, `universe-point-in-time` 0.1.5.
- **`researcher-init` shows the interview at a glance before question 1** — a table of the seven
  questions, what each asks, why, and where it lands — numbers every question *n of 7*, names the
  five things question 2 may cover so the owner is not left with a blank line, and hands over as a
  numbered list of what happens next, `next` last. The questions themselves and every rule around
  them are unchanged.
- **The README opens with the path**: five moves, each in a new session, in the folder the line
  names, with what each makes; and the tables list `next` and the two new skills.
### Notes
- **Two sources checked for this version, both leads, neither read into a library:** Gong (2026),
  *AI Agents in Financial Markets: Architecture, Applications, and Systemic Implications*,
  arXiv 2603.13942, whose five governance principles — bounded autonomy, traceability, diversity by
  design, embedded intervention, supervisory co-evolution — describe what this package already does
  by construction (plan-first, the go, every claim cited, nothing trades, the other side always
  named) and name what `next` adds: supervisory observability of where the work stands; and Packt's
  *Building AI Agents for Finance* (2026), whose chapter 11 evaluation harness is the shape of
  what issue #3 proposes for these skills and commands. The new primitives are in that issue's
  scope: two triggering cases each, and the contract check for `next`.

## [0.10.1] - 2026-09-22
`check_repo` names a deleted example notebook, and the template stops inheriting four of the
worked strategy's lines.
### Fixed
- **`tools/check_repo.py` crashed on an example notebook deleted from the working tree**: the
  marker check read it as an empty text and JSON refused it, so the finding that names the
  missing file never appeared. A tracked notebook that is not on disk is now skipped there, and
  the template check reports it.
- **Four lines of the worked example reached every new strategy** through the generated files
  (template 0.10.1, example 0.10.3); `experiment-lifecycle`'s reference notebook and blueprint
  template change with them.

## [0.10.0] - 2026-09-22
The strategy template ships every file its README names, generated from the worked example, from
the proposal in pull request #1.
### Added
- **`tools/sync_investment_lab_references.py` regenerates the template's files** — the drivers, the
  shared modules, the notebooks, Experiment 1's documents and the paper-trading files, eighteen in
  all, as its `TEMPLATE_FILES` lists them — from the worked example with its own lines removed, the
  way it already regenerated `experiment-lifecycle`'s references: a `.py` file comes out as its
  docstring, a notebook as its markdown cells, a document as its prose. Only the files that differ
  are written, and a missing example file stops the run with its name. **`check_repo.py` fails
  when a template file differs** from what the example says (template 0.10.0).
- **Tests for the sync tool's stripping**: the Python example block, blank lines kept around a
  removed block, adjacent blocks, the transform by suffix, the mapping against the example, and
  stale detection.
### Changed
- **A marker must stand alone at column 0, and markers inside notebook cells are checked too.**
  `check_repo.py` reads the marker strings from the sync tool and reports an indented marker, one
  with trailing whitespace, or a broken pair inside a notebook cell: the sync tool would not strip
  it, and the example's lines would reach every new strategy.
- **A removed example block no longer merges blank lines across the whole file**, so Python kept
  outside a block keeps PEP 8's two blank lines between definitions.
- **`init-example <path>` is for a strategy made before template 0.10.0**, which lacks the files. A
  strategy made now has nothing to bring across: `init-example` 0.1.2, `init-strategy` 0.1.2,
  `experiment-lifecycle` 0.7.4, `data-curator-custom-calculations` 0.3.1,
  `universe-point-in-time` 0.1.4, and the `blueprint` and `brainstorm` commands say so.

## [0.9.2] - 2026-09-22
No CI: the checks run on the maintainer's machine, as `AGENTS.md` always asked.
### Removed
- **The GitHub Actions workflow** and the README's badge. The five checks are unchanged and still
  pass before any commit, by hand, as the README's *Development* section shows; GitHub no longer
  runs them on every push, and nobody who forks or watches the repository sees a workflow run.

## [0.9.1] - 2026-09-22
Three paths in the example that failed the repository's own check.
### Fixed
- **Three chapter notes in `examples/liquid-golden-cross` had paths over 120 characters**, which
  `tools/check_repo.py` refuses because a home folder on Windows pushes them past the path limit;
  they are renamed, with every link to them rewritten and the rename logged in the example's
  `Bibliotheca/LOG.md`.

## [0.9.0] - 2026-09-22
The worked example's bibliography covers every claim, its Experiment 1 meets its last success
criterion, and its setup guide names the files it cannot download.
### Added
- **Six notes carried and two papers read in `examples/liquid-golden-cross`**, so every claim in
  its `OBJECTIVE.md` has a note behind it: Grinold and Kahn's chapters 13, 14 and 16 for the
  rebalancing band, Paleologo's chapters 6 and 8 for the sizing, the momentum review of Baltussen,
  Dom, Van Vliet and Vidojevic (2025) for the signal, and Sarkar, Du and Vafai (2019) for the
  construction. The example's own changelog, 0.10.0, has the detail.
### Changed
- **The example's `OBJECTIVE.md` is fine-tuned for claims 2 to 4** from those notes, with no
  claim's wording changed, as the order of work says a fine-tuning pass does.
- **The example's `SETUP.md` states the exact names, headers and date order of the hand-supplied
  benchmark and factor files**, and the four reserved factor names, because a file named otherwise
  is not found, or is silently counted as one more factor.
- **The example's Experiment 1 meets success criterion 1, to the data.** Its pipeline was re-run
  from a wiped working copy on a fresh download with no manual step beyond the hand-supplied
  files; every conclusion held, the filter-off control and the index came back to every
  published decimal, and the rule moved within hundredths and one rebalance. `FINDINGS_1.md`
  carries the re-run's figures beside the published ones, which stand.

## [0.8.2] - 2026-09-22
Two lines the first testers would have missed.
### Fixed
- **`SETUP.md` asks for a global git identity before anything is made.** Every folder the three
  commands make starts as a git repository with a first commit, and on a machine whose identity is
  set only per repository the commit stopped, as it did on the maintainer's own; the script's
  recovery message and the skill's instruction to ask were right, but the stop was avoidable.
- **The README's three steps name the agent deploy.** Step 2 said to run `researcher-init` in the
  home but not the `apm install --target <agent>` there that deploys the researcher as an agent
  called by name; `SETUP.md`, `init-researcher` and the home's README already said it.

## [0.8.1] - 2026-09-22
What `apm update -g` does to the retired packages, as it did on a real machine.
### Fixed
- **`update` and the 0.8.0 upgrade note say what the update really does to the eight retired
  `KaxaNuk/KaxaNuk-Agent-Skills` packages**: it removes what they deployed, and every skill and
  command of this package stays deployed, but `apm deps list -g` may keep naming them as orphaned,
  because their folders stay under `~/.apm/apm_modules/`. That is harmless; `apm prune` and
  `apm uninstall -g` do not reach them in APM 0.29.

## [0.8.0] - 2026-09-22
A package for teaching: four leftovers of the old per-repository setup are gone, the researcher's
interview places you in the history of investment research, and every Lab skill now matches the
worked example's code.

**What to do differently:** run `apm update -g`, then open a new session. The update removes the
deployed copies of the removed skills and command, and the eight orphaned
`KaxaNuk/KaxaNuk-Agent-Skills` packages an install from before 0.7.0 still carries
(`apm deps list -g` lists them). In a home, run `update`, and deploy the agent with
`apm install --target <agent>`.
### Added
- **A reading map for `read`**, `references/reading-map.md`: Section 01, *The Evolution of
  Investment Research*, of KaxaNuk's Investment Research Bootcamp, session 02, distilled. The ten
  papers of the two dated timelines; where each stance and each commonly held belief sits, who
  tested it and its other side; the pairs the deck sets against each other; the six acts with the
  arc's 21 questions and their works; *Nothing is discarded*; KaxaNuk's position; and Act VII's four
  open problems. Every work is as the deck gives it, and each one is a lead, never a citation.
- **`backtest-engine-runs` lists what the engine is called with**: the `entities.Configuration`
  fields, the three price roles and the CSV input handlers the worked example runs on engine
  0.66.0. It also records that `commission_cents=0.1` was charged about $0.083 a share.
- **A root `.gitattributes`** (`* text=auto eol=lf`), so a Windows clone checks out the bytes that
  were committed.
- **Tests for every check in `tools/check_repo.py`** and for
  `tools/sync_investment_lab_references.py`.
### Changed
- **`researcher-init` 0.7 asks seven questions**, in the owner's language from the first (Spanish
  or English): language and name; what you do; the researcher's name, domains, voice and rules in
  one call; how you see markets, three questions whose options are the reading map's stances
  and their papers; where you stand in the evolution of investment research, who tested it and who
  disagrees; what you are reading for, each question with what it feeds and what would change your
  mind; and *Find first*, the works to put in `Sources/`. There are no strategy questions. A re-run
  keeps what the owner wrote, and `Philosophy/HOW-I-INVEST.md` takes only what the owner typed. It
  also names the home: `apm.yml` gets the researcher's slug, a description and the owner as
  author, so a home no longer carries the name `kaxanuk-researcher`.
- **`read` and `query` use the map.** `read` names the *Find first* works when `Sources/` has
  nothing left to read, and after each read the map's other side of what was read; a note's
  citation never comes from the map. `query` names the missing work when it would close a gap.
- **`update` reads what is new before it installs it**: the newest `CHANGELOG.md` and
  `templates/researcher/` from GitHub `main`, and the installed version from `apm deps list -g`.
  It compares each of the home's own files — `AGENTS.md`, `CLAUDE.md`, `README.md` in substance,
  `LICENSE`, `apm.yml`'s comments only, `.gitignore` and `.gitattributes` — and runs
  `apm update -g --yes`, since the owner's go is the confirmation. It then adds a *Brought to
  template X.Y.Z* entry to the home's `CHANGELOG.md`, so the next `update` reports only newer
  versions; the rest of the home's history is left as it is.
- **`how-we-work` 0.2.3 is written for one package.** A release takes one `vX.Y.Z` tag, pushed
  after the merge, and runs `uv lock` where a `uv.lock` is committed. The root CHANGELOG keeps Keep
  a Changelog. Where a repository's `AGENTS.md` makes issue branches a recommendation, as a
  strategy's does, they are suggested, never a gate.
- **The engine skills install and run through `uv`.** `backtest-engine-runs` 0.1.4 and
  `attribution-analysis-runs` install with `uv pip install` from the repository root, so the
  licensed package lands in the strategy's `.venv`, and every CLI call runs through `uv run`;
  `init excel` is only for a project outside a Strategy Template repository.
  `backtest-engine-runs` also says the weight file sums to exactly one, with the residual in the
  cash proxy, and that `cash_reserve_percentage` cures a truncated run (the example needed 2%).
- **`data-curator-custom-calculations` calls `main()` with `data_block_providers`** (Data Curator
  0.50.0 or later), as the worked example does, instead of the deprecated per-kind providers, and
  says each data block a run reads, dividends and splits included, is mapped to a provider there,
  and that one provider can serve them all.
- **`universe-point-in-time` 0.1.3** lists the impossible-daily-move check the worked example
  writes to `Data_Issues.csv`, calls `Data/refinery.py` and `Data/analyzer.ipynb` the worked
  example's, since the template ships neither, and gives `init-example Universe/universe.ipynb` to
  a strategy that has only the seed.
- **`experiment-lifecycle` 0.7.3 and the `blueprint` and `brainstorm` commands describe a strategy
  as `init-strategy` makes it**: it installs nothing, the skills are installed once for the user,
  `Experiments/` holds `Experiment_1/` with three empty output folders, and the header-only seed is
  never deleted; `Universe/universe.ipynb` is brought by its path. The skill's references are
  called copies of the worked example's Experiment 1, not files the template ships. Notebooks are
  stripped with `uv run --group notebook jupyter nbconvert`, because a bare `uv sync` leaves
  nbconvert out, and the skill's references are regenerated with `uv run --no-project python`, as
  `AGENTS.md` says. `references/structure.md` names template 0.9.0 and the files it ships inside
  its folders.
- **`init-strategy` gives the real reason for a short path on Windows**: deep paths inside the
  folder, such as `.venv/`, break tools later with misleading errors such as `WinError 3`.
- **SETUP.md says what each `--target` receives at user scope**: Claude Code and Copilot
  everything; Cursor, Gemini, OpenCode and Windsurf the skills and commands without the
  instructions; Codex the skills only, and runs a command by naming its file in the package.
- **The README says what a strategy needs from outside the package** (a data provider's key for
  FMP, Sharadar or LSEG, the Backtest Engine and Attribution Analysis licences, access to the
  private Portfolio Construction repository) and what runs without them. Its tree lists every
  top-level file but itself.
- **The README's Development section and `AGENTS.md` run exactly what CI runs**, each through `uv`:
  the tests, ruff, ruff on the worked example, `tools/check_repo.py` and the Bloom Code check. CI
  now lints the worked example and checks its Bloom Code style too.
- **Markdown is wrapped at 100 columns** where it is written or changed; the house-style
  instructions, `bloom-code-lint`, the README, SETUP.md and `AGENTS.md` are rewrapped, their words
  unchanged but for BLOOM012's description, under Fixed.
- **The starting points move with it**: the strategy template and the worked example to 0.9.0, the
  researcher's home to 0.7.0. Their own changelogs say what changes in a strategy and in a home.
### Removed
- **`devcontainer-aware-command-execution`.** No KaxaNuk starting point has a dev container, yet
  the skill told the assistant in every folder to look for `.devcontainer/devcontainer.json` and
  run `docker ps` before its first shell command.
- **`propagate-mcp-env-vars`**, its script and its tests. No manifest here or in the starting
  points declares an MCP server; the skill assumed a per-project `.mcp.json` and a
  `.devcontainer/.env`, and its `apm install --mcp` advice was wrong for the APM in use. CI and
  `tests/conftest.py` no longer name it.
- **The `initialize-apm` command.** It set APM up per repository with `pip`, a
  `requirements-dev.txt` and one `apm install` per dependency, a layout a strategy no longer has.
  APM is installed once with `uv tool install apm-cli`, and this package with `apm install -g`.
- **`apm-usage`**, a one-link skill that framed APM as a project's dependencies. The APM commands a
  learner runs are in SETUP.md, which now links APM's own reference.
- **`metadata.version` in the commands' frontmatter.** APM keeps only `description`, `input`,
  `allowed-tools`, `model` and `argument-hint` for a command, and printed a *dropped: metadata*
  warning for each one on install. The versions live in this changelog.
- **`apm-cli` from the development group** in `pyproject.toml`: APM is a tool installed once, not a
  dependency of this repository's environment.
### Fixed
- **`teach` receives its topic.** Its body read empty backticks where `${input:topic}` belonged.
- **`init-strategy`, `init-example`, `init-researcher` and `read` run `scaffold.py` with
  `uv run --no-project python`.** SETUP.md installs no Python, and on Windows a bare `python` is
  the Microsoft Store alias. `bloom-code-lint` 0.1.1 runs its checker the same way, with the
  project's ruff line length (100 in a strategy) instead of 120. Its BLOOM013 hint and the
  `data-curator-custom-calculations` template name the error message `message`, not `msg`, as the
  strategy's `AGENTS.md` does.
- **`scaffold.py` run from a checkout copies that checkout's starting points**; it looked one
  folder too low and silently copied an installed package's. A new strategy, home or example now
  starts on branch `main` whatever `init.defaultBranch` says, and when the first commit fails the
  script prints the `git commit` that finishes it.
- **`alpha-decomposition` 0.3.4 prices a counterfactual with the worked example's functions**
  (`securities_panel.expand_to_identifiers`, then `backtest_engine.write_weight_file`,
  `build_configuration` and `run_backtest`), not `to_engine_frame` and `run_variant`, which never
  existed, and says what `eligible_matrix` is.
- **`portfolio-construction-runs` 0.2.2 describes the module the example ships**:
  `weigh(selected, history, method, maximum_weight)`, one cut in `build_weights`, and its
  `maximum_weight` and `minimum_holdings` constraints. `ConstructionSettings`,
  `build_target_weights` and `risk_lookback_days` are gone. It says which methods `weigh` builds,
  those whose configuration has no required field, and that the rest need a weigher of their own.
- **`backtest-engine-runs` 0.1.4 and `attribution-analysis-runs` 0.2.5 guard the import with
  `importlib.util.find_spec`**, as `portfolio-construction-runs` and the worked example do, not
  with a `try` around `from kaxanuk… import …`, which Bloom Code rejects (BLOOM003).
- **`attribution-analysis-runs` 0.2.5 computes returns from
  `m_close_dividend_and_split_adjusted`**, the basis the backtest marks on; a split-adjusted column
  dropped every dividend from the attribution.
- **`data-curator-custom-calculations` 0.3 knows the strategy template's layout**: `c_*` columns go
  in `Data/Curator/custom_calculations.py`, selected among the columns `Data/curator.py` requests,
  never in `Config/`; a cross-sectional or swept column is an `r_*` column in the Refinery, computed
  by the worked example's `Data/refinery.py`, which the template does not ship.
- **`backtest-engine-runs` says KaxaNuk Strategy Template** where it still said KN Research
  Process.
- **`audit`'s frontmatter rule applies to a source note or a book's `INDEX.md` only**, so concept
  and synthesis pages are not reported twice, and its note on stale installs no longer writes an
  input placeholder that APM rewrote on install.
- **`read` no longer says the template ships its Bibliotheca files "on `main`"**: the template is a
  folder inside this package.
- **The `python-test-writing` instruction's example declares `-> None`** on its test methods, as
  Bloom Code requires.
- **`tools/check_repo.py` checks a non-ASCII path** (`git ls-files -z`, decoded as UTF-8) instead
  of skipping it, measures a one-line skill description, and fails on one it cannot read.
- **`tools/sync_investment_lab_references.py` writes only the references that differ**, says so
  when none do, and stops with the file's name when a worked-example document is missing instead
  of writing an empty reference.
- **Tests**: `bloom_code_check`'s ASCII-output test no longer fails in a temporary folder with a
  non-ASCII path, and the scaffold test checks that the first commit really exists.
- **`LICENSE` names the `read` and `query` skills and the `audit`, `refine`, `refresh-index` and
  `teach` commands**, not a `compile` command that does not exist.
- **`experiment-lifecycle`'s notebook reference no longer carries the worked example's figures.**
  Section 6, *Counterfactuals*, marked the example's 45.5 of 159.5 points and its four choices as
  the template's description; they are now the example's own lines. The skill's section table
  lists 6 · Counterfactuals and 7 · Verdict, as the notebook does.
- **`experiment-lifecycle` says to retitle a copied experiment notebook**: `experiment_N.ipynb` is
  copied from Experiment 1's, so it is retitled `Experiment N`, every `_1` becomes `_N`, and the
  sentences that only apply to the benchmark go, as they already did in the blueprint.
- **`tools/sync_investment_lab_references.py` writes `experiment-notebook.ipynb` in nbformat's
  own form**, keys sorted and ending in a newline, and the worked example's notebooks carry the
  cell ids nbformat 4.5 requires, so stripping a notebook copied from the reference, or from the
  example, changes nothing.
- **`blueprint` and `brainstorm` give Experiment N > 1 its blank file**: the `experiment-lifecycle`
  skill's `references/` template, copied into `Experiment_N/`. The `init-example` command they gave
  copies `Experiment_1/`'s file, which the owner already has, so it was refused.
- **`init-strategy` restores a lost template file from the template**, not with `init-example`,
  which copies the worked example's filled-in version: `scaffold.py strategy . --only <path>`.
- **The strategy template's README, step 4 of its and the worked example's `SETUP.md`,
  `experiment-lifecycle`'s `structure.md` and `scaffold.py`'s missing-package message give the
  install command with `--target`**, as this package's SETUP.md does; they gave it bare, and a bare
  `apm install -g` on a machine with no agent folder deploys to Copilot and `.agents/`.
- **`update` compares `LICENSE` too, and records the template version it brought** as a *Brought
  to template X.Y.Z* entry at the top of the home's `CHANGELOG.md`, so the next `update` no longer
  reports the same versions again.
- **`researcher-init` keeps the tag policy and the strategy rows on a re-run under `force`**, which
  the home's 0.7.0 upgrade note now names; a plain re-run stops on a filled `RESEARCHER.md`.
- **`extract.py` stops on a password-protected PDF with its message** instead of a traceback:
  pypdf returns, rather than raises, when the empty password fails, so the check never fired.
- **`extract.py` opens the AES-encrypted PDFs publishers ship**: `read` 0.6.0 declares
  `pypdf[crypto]`, without which pypdf stopped with a `DependencyError` traceback on an AES-256 PDF
  and silently lost an AES-128 PDF's outline. A file that is not a PDF stops with a message, not a
  traceback.
- **`read` carries `--depth 2` into the extraction of a book whose depth 1 is parts.** Without it,
  `--chapters` counts the parts, and a chapter chosen from the depth-2 outline extracted a part or
  stopped with *no chapter at this depth*.
- **`read` extracts only the chapters chosen from a book with no outline.** `extract.py` refused
  `--split` with `--chapters`, so a shorter split renumbered the chapters from 1 and overwrote
  `OUTLINE.md`. `--split` now names the whole book and goes with `--chapters` or `--all`; `--split`
  alone is refused.
- **`read` says the extract's page markers are PDF pages**, not the numbers printed in the book: a
  note cites them, a book's `INDEX.md` says by how much the printed numbers differ, and `--split`
  takes PDF pages. It said the markers were the page numbers, so a book with front matter was cited
  off by its length.
- **`bloom-code-lint` 0.1.1 counts each call of a chain on the line of its method**, so a pandas
  chain split one call per line passes BLOOM012; it counted every call on the chain's first line,
  where no line break could clear it.
- **`bloom-code-lint` and the Bloom Code instruction say what BLOOM012 counts**: every call that
  starts on a line, nested or side by side, at most two (one under `--strict`). The message called
  `a(x) + b(y) + c(z)` "more than one nested call"; what the checker reports is unchanged.

## [0.7.1] - 2026-09-21
A shorter, more focused researcher interview.
### Changed
- **`researcher-init` is shorter.** The interview drops the strategy and tag-policy questions; tags
  default to loose, and the strategies table starts empty — strategies are added when the researcher
  is invited into one, not at setup. Language defaults to English. The remaining eight questions
  focus on who you are, how you invest and what you're reading for.

## [0.7.0] - 2026-09-21
Every KaxaNuk skill is in this package. One install and one `apm update -g` bring them all to every folder.
### Added
- **The Investment Lab skills**, from KaxaNuk-Agent-Skills at its commit `3b8f76c`, unchanged but for the lines that named the package they came from: `experiment-lifecycle` and `alpha-decomposition`, the process; `universe-point-in-time`, `data-curator-custom-calculations`, `portfolio-construction-runs`, `backtest-engine-runs` and `attribution-analysis-runs`, one for each library; and the house rules, `how-we-work`, `bloom-code-lint`, `apm-usage`, `devcontainer-aware-command-execution`, `propagate-mcp-env-vars`, the `initialize-apm` command and the Bloom Code, PEP 8, test-writing and filesystem-boundaries instructions. The tests of `bloom_code_check.py` and `propagate_mcp_env_vars.py` came with them.
- **`tools/sync_investment_lab_references.py`** regenerates `experiment-lifecycle`'s references from the worked example on disk instead of from GitHub, and **`check_repo.py` fails when they differ**, so the skill and the example cannot drift apart.
### Changed
- **The package depends on nothing.** `KaxaNuk/KaxaNuk-Agent-Skills/kaxanuk`, which was unpinned, is gone from `apm.yml`; a skill and the template it describes now change in one pull request. After `apm update -g`, `apm deps list -g` shows the KaxaNuk-Agent-Skills packages as orphaned; the `update` command says so.
- **CI checks Bloom Code with the repository's own `bloom-code-lint`**, over every skill's scripts, the tests and the tools, instead of fetching the checker.
- `AGENTS.md`, the README, `researcher-init`, `update`, the strategy template's README (template 0.8.1) and the home's `AGENTS.md` (home 0.6.1) name one package.

## [0.6.6] - 2026-09-21
The README says how to install once.
### Changed
- **One *Install* section** replaces the prompt in the introduction and *Install once, for your user*: the prompt to paste into Claude or Codex, the two commands by hand, then the first three commands in a new session.
### Removed
- **The root `uv.lock`**, which nothing read: CI runs with `--no-project`. It is ignored from now on. The worked example keeps its own, which pins the versions its results were run with.

## [0.6.5] - 2026-09-21
The README's install section gives both ways in.
### Changed
- ***Install once, for your user* starts with the prompt to paste into Claude or Codex**, what the assistant then does, and that `SETUP.md` is what it follows; the commands by hand come second. The prompt reads the same everywhere it appears: *Please help me install this repo: https://github.com/KaxaNuk/KaxaNuk-Researcher*.

## [0.6.4] - 2026-09-21
`extract.py`, the script `read` runs, has tests and the house style. What it writes is unchanged.
### Changed
- **`extract.py` follows Bloom Code**, like every other script here: no nested functions or reassigned names, one item per line, imports as modules, a dataclass where a tuple was returned. Its outlines, console output and extracts were compared byte for byte, before and after, on two books from a real library, with both engines and with `--split`: identical.
### Added
- **Tests for `extract.py`**: chapters from an outline and their front matter, `--chapters` and `--split` parsing and their errors, text cleaning, slugs, and a ten-page PDF built in the test for the outline and for a PDF with no text layer. CI runs them and checks the script's style.

## [0.6.3] - 2026-09-21
The repository checks itself, locally and on every push.
### Added
- **`tools/check_repo.py`**, with tests: the package and each starting point declare one version across `apm.yml`, `CHANGELOG.md`, `pyproject.toml` and `uv.lock`; every heading of a template document is in the example's copy, so the two cannot drift apart as they did on two branches; the example's markers open and close in order; no section symbol; skill descriptions within APM's limit; no path over 120 characters.
- **CI** on every push and pull request: the tests, ruff, `check_repo.py`, and the Bloom Code style of the scripts, with the checker fetched from KaxaNuk-Agent-Skills. A badge in the README.

## [0.6.2] - 2026-09-21
The install works from a deep home folder on Windows.
### Fixed
- **`apm install -g` failed with *checkout failed*** when the user's home folder was more than about 60 characters deep: one note in the worked example had a 130-character path, which took the installed copy past Windows' 260-character limit. The note is renamed `Sullivan_Timmermann_White_1999_Data_Snooping.md` (example 0.8.1); the longest path in the repository is now 116 characters. Found by installing into an empty, deliberately deep home.
### Added
- **`SETUP.md` gives the fallback,** `git config --global core.longpaths true`, for a path that is still too long.
- **`apm.yml` says why `kaxanuk` is unpinned.** APM warns about it on every install; a semver range does not resolve against KaxaNuk-Agent-Skills' tags today, and a literal tag would freeze the Lab's skills.

## [0.6.1] - 2026-09-21
A new user can install from the URL alone.
### Added
- **`SETUP.md`**, what an assistant follows when it is given only this repository's URL: the two tools, the one install for the user, then `init-researcher`, `researcher-init` and `init-strategy`, each in a new session, with the Windows short-path warning and the rule that a git identity is asked for, never invented.
### Changed
- **The README opens with the prompt to paste and the first ten minutes in four commands,** before the reference tables.
- **`researcher-init`, step 5,** says the skills are already installed for the user, and that `apm install` in the home deploys only the agent.

## [0.6.0] - 2026-09-21
The KaxaNuk Researcher is one repository and one package: its skills and commands, the three commands that make every folder, and the strategy template, its worked example and the researcher's home they copy. Versions up to 0.5.6 are in `KaxaNuk/KaxaNuk-Researcher-Template`'s `CHANGELOG.md`; the strategy template's history is in `templates/strategy/CHANGELOG.md`.
### Added
- **`init-researcher`, `init-strategy` and `init-example`**, skills the owner runs by name. Each copies a starting point into a new folder with `init-strategy`'s `scripts/scaffold.py` — byte for byte, never from memory — after a plan and the owner's go, and makes it a git repository with its first commit. `init-example <path>` copies one file or folder of the worked example into an existing strategy: a file already there with the same content is skipped, and one with other content stops the copy. The script finds the package beside itself, under `apm_modules/`, or under `~/.apm/` where `apm install -g` puts it, and has unit tests.
- **`templates/strategy/`**, the KaxaNuk Strategy Template at 0.8.0, from `KaxaNuk/KaxaNuk-Strategy-Template`'s `main`; **`examples/liquid-golden-cross/`**, its worked example at 0.8.0, from that repository's `example` branch; **`templates/researcher/`**, the researcher's home at 0.6.0, from `KaxaNuk/KaxaNuk-Researcher-Template`. All three are ordinary folders, and the template and the example no longer live on two branches kept in step by hand — 0.7.14 reached one and not the other. A strategy's `Bibliotheca/BIBLIOGRAPHY.md` and `LOG.md` ship empty in the template.
### Changed
- **The researcher is a package installed once for the user.** `read`, `query` and the ten commands were copied into every home, so each home carried code it could not safely edit and every version arrived by a git merge. Now `apm install -g KaxaNuk/KaxaNuk-Researcher` puts every KaxaNuk skill — this package's and, through its dependency on `KaxaNuk/KaxaNuk-Agent-Skills/kaxanuk`, every Investment Lab package's — in every folder the owner opens; `apm update -g` brings each new version everywhere; and a strategy installs nothing.
- **`scripts/extract.py` and `references/note.md` live in the `read` skill's folder,** and the skills name them by *this skill's directory*.
- **Files a strategy lacks come from the package.** `read` copies the empty bibliography and log from the template with `scaffold.py --only`; `blueprint` and `brainstorm` give `init-example Experiments/Experiment_1/...` instead of fetching a branch of the template's repository.
- **`update`** runs `apm update -g`, and compares the home's `AGENTS.md`, `CLAUDE.md` and `.gitignore` with `templates/researcher/`, showing what changed rather than merging. For a home from before this release it is the migration: it removes the home's copies of the skills, commands, script and reference, empties `apm.yml`'s dependencies, and installs the package for the user, keeping the agent and any skill the owner wrote.
- **`researcher-init`** checks for the skills at user scope; **`audit`** compares installed copies under `~/.claude/` with the packages under `~/.apm/apm_modules/`.
### What to do differently
- **Install once:** `uv tool install apm-cli`, then `apm install -g KaxaNuk/KaxaNuk-Researcher --target <your agent>`.
- **A home from before this release runs `update` once.** Until then it keeps working on the copies it has.
- **A new strategy is `init-strategy <name>`**, not *Use this template*; the example is `init-example`.
