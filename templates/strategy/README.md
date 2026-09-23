# KaxaNuk Strategy Template

**A template for researching an investment strategy with the KaxaNuk Investment Lab.** Its eight
steps as a folder structure, with the conventions that let two people share a tool without
explaining it first. Building the data needs a data-provider key; the backtest and attribution,
steps 5 and 6, also need the licensed Backtest Engine and Attribution Analysis.

The universe is one CSV whose only required column is `main_identifier`, and every stage reads it
without knowing what is in it: **equities, ETFs, FX, crypto, commodities or futures all run the
same process.**

**To start a strategy, install the KaxaNuk skills once, for your user** — with
`uvx --from apm-cli` in front if `apm` is not on the path, and your assistant, such as `codex`, in
place of `claude`:

```bash
apm install -g KaxaNuk/KaxaNuk-Researcher --target claude
```

**Then ask Claude or Codex to run `init-strategy <strategy-name>`.** It copies this template into
one new folder named after the strategy and makes it a git repository; [`SETUP.md`](SETUP.md),
inside it, is what the assistant follows from there — the environment, the keys, the strategy's own
README — and it is written so a person can read it in two minutes too. The skills are installed for
your user, not in a strategy, so a strategy installs nothing. Issues and pull requests are welcome:
the process improves in public, the way KaxaNuk's open-source Data Curator did.

This template is the shape and every file the process expects in it: six folders, the documents at
the root, and inside the folders each driver, module, notebook and document as a description of
what belongs there — a `.py` file as its docstring, a notebook as its markdown cells. The same
files, worked through for one strategy, `liquid-golden-cross`, are the
[example](https://github.com/KaxaNuk/KaxaNuk-Researcher/tree/main/examples/liquid-golden-cross);
*What is in here* says what each file is for.

---

## Eight steps, one repo

Each stage owns its outputs and reads only from the stage above it. **Steps 1 to 7 are the KaxaNuk
Investment Lab, and this repository.** Step 8 is the one that leaves it.

| # | Step | In plain words | It produces | It prevents | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | **Bibliotheca** | the idea and its claims first, then the literature that argues with them | a referenced hypothesis, in the repo, dated | backtesting a hunch you cannot defend afterwards | `OBJECTIVE.md`, `Bibliotheca/` |
| 2 | **Universe** | the eligible list, rebuilt for each date rather than for today | a point-in-time membership table | survivorship bias — testing on the winners that survived | `Universe/` |
| 3 | **Data** | curation, then refinery, then analysis — in that order | a reproducible dataset, and the evidence a feature carries signal | beautiful results that came from broken inputs | `Data/` |
| 4 | **Portfolio** | how much of what, and how often you change your mind | a weighting scheme with position and turnover limits | a good signal in a portfolio nobody could hold | `Experiments/Experiment_N/` |
| 5 | **Backtest** | the simulation, run by the Backtest Engine | a performance curve and a cost-aware track record | paper returns that real trading would have erased | `Experiments/Experiment_N/Backtest/` |
| 6 | **Attribution** | which part of the return did you actually earn? | a factor and idiosyncratic breakdown of performance | selling factor beta as if it were alpha | `Experiments/Experiment_N/Attribution/` |
| 7 | **Paper trading** | a dress rehearsal on data nobody has seen yet | out-of-sample evidence and an operations checklist | finding the plumbing problems on day one of funding | `Paper_Trading/` |
| 8 | Production | real capital, real monitoring, a real drawdown policy | a funded, monitored strategy with an owner | research that stays research forever | **elsewhere** |

---

## The tools

Three jobs, one tool for each — either option does the job. Install once, use for every strategy.

| Job | What it is for | Pick one |
| --- | --- | --- |
| **Versions** | where your work lives, and how you get it back after you break it | [GitHub Desktop](https://desktop.github.com), or the [git](https://git-scm.com) command line |
| **Code and debug** | your pair for the parts you have not written before | [Claude](https://claude.ai/download), or [Codex](https://openai.com/codex) |
| **Read and run** | where you write and run Python; the free editions are enough | [PyCharm](https://www.jetbrains.com/pycharm/), or [VS Code](https://code.visualstudio.com) |

**On top of whichever assistant you pick, KaxaNuk's agent skills** teach it the six Lab modules
and this process — what each does, how it is called, and what it must never be asked to do. They are
one package, [`KaxaNuk/KaxaNuk-Researcher`](https://github.com/KaxaNuk/KaxaNuk-Researcher), and
**this repository installs none of them**: they are installed once for your user, by the command
above, and are there in every strategy; `apm update -g` keeps them current. Nothing here needs them
to be read; a filled-in repository is faster with them.

### A researcher beside the process

A researcher is a separate project, made once with `init-researcher`, a skill of the
[KaxaNuk Researcher](https://github.com/KaxaNuk/KaxaNuk-Researcher): a companion you name and
teach, one per person rather than per strategy, with its own library of what you have read — invite
it with `claude --add-dir <its folder>` and its library comes along; for its identity to load with
it, follow *In a strategy or another project* in the researcher's own README. It drafts the claims
in `OBJECTIVE.md` from your words before any paper is read. It writes the notes in `Bibliotheca/`
with `read`: a script pulls a book's table of contents out of the PDF, you pick the chapters that
serve a claim, and after a plan and your go it writes one note per chapter with its row in
`BIBLIOGRAPHY.md`; a note its own library already holds comes across without reading the PDF twice.
It then rewrites each claim's evidence from those notes, and drafts the hypothesis in each
`BLUEPRINT_N.md`, every prediction citing the note it came from. `brainstorm` drafts the entries of
`BRAINSTORMING_N.md` (E, F), `challenge` checks a finished cycle against its blueprint (G), and
`next` says at any moment which part comes next.

---

## Setup

**[`SETUP.md`](SETUP.md) is the whole of it, and nothing here repeats it** — so the two cannot
drift. It covers getting the repository, the one folder it has to live in, the environment, the keys,
and where the agent skills come from, each with the command an agent runs and the mistake it must
not make.

---

## Starting your own strategy

Once setup is done, work in this order. **These eight parts are lettered so they are never mistaken
for the eight steps above:** the universe, C, is step 2; the cycle, G, is steps 4 to 6. Every file
they name is already in your repository — `OBJECTIVE.md`, `RESULTS.md`, the seed
`Universe/Investable_Universe.csv` with only its `main_identifier` header, the drivers, the
notebooks, `BLUEPRINT_1.md` and its siblings — each a description of what belongs in it, to be
filled in; the example shows every one of them worked through. Ask your assistant to run `next` at
any moment: it reads the folder and says which part comes next.
**The objective comes before any paper**: reading with no claim to read for has no stopping
condition, and a claim written after the reading is an observation wearing a hypothesis's clothes.

- **A. The objective.** Write `OBJECTIVE.md` — the idea in one sentence, and the claims inside it,
  *before* any paper is read and before anything is measured. Each claim's evidence starts as the
  question that would settle it.
- **B. The reading.** Fine-tune the objective: read for each claim's question, the sources that
  argue against it included — one note per paper, one per chapter of a book, in `Bibliotheca/` —
  then rewrite each claim's evidence from the notes.
- **C. The universe.** Put your securities in `Universe/Investable_Universe.csv`, one row each and
  **delisted names included**: a list of today's names has already deleted everything that failed.
  `main_identifier` is the only required column; add whatever else your strategy groups by. The
  claims decide what the universe has to contain, which is why it comes after them.
- **D. The data.** Write your `c_*` and `r_*` columns into the two `custom_calculations.py`, fill
  in the Curator and Refinery drivers that call the libraries, and run the Universe and Data steps
  in this order: curator, then `universe.ipynb`, then refinery, then `analyzer.ipynb`. The universe
  notebook sits *between* the two Data commands, because it profiles what the curator downloaded
  and writes the master the refinery joins. The analyzer's measurements go straight into
  `RESULTS.md`.
- **E. The blueprint.** Choose the benchmark, then write `BLUEPRINT_1.md` before the rule.
  Experiment 1 is the benchmark, a real strategy with a real return, so choosing it is the first
  entry of `BRAINSTORMING_1.md`. Every prediction in the blueprint cites a `Bibliotheca/` note from
  B, or an analyzer measurement from D; a hypothesis edited after its test is not a hypothesis.
- **F. The broad reading.** Search for papers and brainstorm — the reading for what the blueprint
  left open, and `BRAINSTORMING_1.md` for what to try next.
- **G. The cycle.** Portfolio construction, backtest, attribution — until it is finished, rewriting
  `FINDINGS_1.md` as its results change.
- **H. The results.** Send every finished cycle to `RESULTS.md`, kept or rejected. The rejected
  result is reported as loudly as the promising one; *What is closed* is what stops the next person
  repeating it.

Then the gate in `Paper_Trading/BITACORA.md`, or Experiment 2, from E again.

---

## The documents

**Two files answer "is this worth anything?"** — [`OBJECTIVE.md`](OBJECTIVE.md) says what we are
trying to do, [`RESULTS.md`](RESULTS.md) says how far we got and what it cost.

| Document | What it holds |
| --- | --- |
| [`SETUP.md`](SETUP.md) | how to get this repository, where it must live, and the commands |
| [`OBJECTIVE.md`](OBJECTIVE.md) | the main idea, and the status of each claim inside it |
| [`RESULTS.md`](RESULTS.md) | the executive summary of every experiment, compiled from the `FINDINGS_N.md` files |
| [`CHANGELOG.md`](CHANGELOG.md) | every version, newest first, and what a version number means here |
| [`AGENTS.md`](AGENTS.md) | **how work is done** — the workflow, the restrictions, and the bar a result has to clear |

Four documents inside every `Experiments/Experiment_N/`, and the split between them is the whole
point: `BLUEPRINT` is frozen so a result cannot quietly reshape the question it was meant to answer,
`JOURNAL` is append-only so the path is recoverable, `FINDINGS` is rewritten so there is one current
answer, and `BRAINSTORMING` looks forward so planning is never mistaken for history. `Bibliotheca/`
has its index in `BIBLIOGRAPHY.md` and `Paper_Trading/` its gate in `BITACORA.md`.

---

## What is in here

What the template ships:

```
SETUP.md              how to get this repository and set it up - start here
OBJECTIVE.md          the idea, and the status of each claim inside it
RESULTS.md            every number this repository has measured
AGENTS.md             how work is done here: the workflow, and the bar a result must clear
CHANGELOG.md          every version, and what a version number means here
apm.yml               marks this as an APM project; it installs nothing — the skills are
                      installed once for your user
pyproject.toml        the environment: Python 3.13, the open-source libraries, uv-managed

Bibliotheca/          step 1
Universe/             step 2
Data/                 step 3
Experiments/          steps 4-6
Paper_Trading/        step 7
Config/               .env.template - copy to .env and fill in your keys
```

What goes in each folder — and this table is the only place it is written down, so it is the one
to keep current:

| Folder | Step | What belongs in it | Committed |
| --- | --- | --- | --- |
| `Bibliotheca/` | 1 | `BIBLIOGRAPHY.md`, the index of sources and the leads. `Papers/`, one note per paper, and `Books/`, one folder per book — its `INDEX.md` of chapters and one note per chapter somebody chose to read — each beside the PDF it came from. `LOG.md`, what was read here and when. `Notes/` for clippings and transcripts | the notes and the indexes — they are the reasoning. The PDFs and `Extracts/` are ignored: licensed material, and the extracts regenerate |
| `Universe/` | 2 | `Investable_Universe.csv`, **the seed**: one row per security, `main_identifier` the only required column, every other column yours. `universe.ipynb`, which profiles what the curator downloaded and writes `Security_Master.csv` and `Data_Issues.csv` | the seed and the notebook; the two outputs and `Provider_Cache/` are regenerated, so ignored |
| `Data/` | 3 | `curator.py`, `refinery.py`, `analyzer.ipynb` — the three drivers. `Curator/custom_calculations.py` for `c_*` columns and `Refinery/custom_calculations.py` for `r_*`. `Curator/Time_Series/`, `Benchmarks/`, `Factors/` and `Refinery/Time_Series/` for what is downloaded or dropped in by hand; `Analyzer/` for charts and the signal table | code only. **Every data file is ignored** — downloaded, derived or dropped in, all of it regenerable |
| `Experiments/` | 4–6 | The four shared modules — `securities_panel.py`, `portfolio_construction.py`, `backtest_engine.py`, `attribution_analysis.py`. One `Experiment_N/` per idea: `BLUEPRINT_N.md`, `BRAINSTORMING_N.md`, `JOURNAL_N.md`, `FINDINGS_N.md`, the notebook, and its `Portfolio/`, `Backtest/` and `Attribution/` output folders | the documents, the notebook with outputs stripped, the modules. The output folders are rebuilt by the notebook, so ignored |
| `Paper_Trading/` | 7 | `BITACORA.md`, what graduation means and the gate. `daily_update.py`. `Paper_Trading_N/paper_trading_N.py`, the frozen rule of anything that passed | everything |
| `Config/` | — | `.env.template`, copied to `.env` and filled in with a data-provider key and the two engine licences | the template. **`.env` never** — and it cannot be regenerated, so discarding all changes loses it |

**Every one of those files is in this template**, except `Bibliotheca/Papers/`, `Books/` and
`Notes/`, which appear with their first note: each as a description of what is expected in it — a
`.py` file as its docstring, a notebook as its markdown cells, a document as its prose — to be
filled in with the strategy's own.
The same files are worked through in the
[example](https://github.com/KaxaNuk/KaxaNuk-Researcher/tree/main/examples/liquid-golden-cross),
where the worked strategy's own lines sit beside that description between the example markers:
`<!-- example: begin -->` and `<!-- example: end -->` in Markdown, `# --- example: begin ---` in
Python, `# EXAMPLE-ONLY CELL` on a notebook cell. The `Bibliotheca/` index and log, the drivers,
the modules, the notebooks and the files of `Experiments/` and `Paper_Trading/` are generated from
the example with those lines removed, so the two cannot drift. To read the example, or run it,
copy it whole into a folder of its own:

```text
init-example
```

Never build on it: the seed in `Universe/` and everything between the markers is that strategy's.
A strategy made from a template before 0.10.0 lacks these files: `init-example <path>` brings one
across, and what is between its markers is then deleted.

---

## The six Lab modules

Six modules across steps 3 to 6, each reading the previous one's output, so you can enter the
pipeline wherever your work already is.

| Module | Step | What it does |
| --- | --- | --- |
| **Data Curator** | 3 | pulls raw market and fundamental data from any provider and aligns it on one calendar |
| **Data Refinery** | 3 | cleans, adjusts and reshapes the curated data into analysis-ready series |
| **Data Analyzer** | 3 | builds features and tests whether they carry signal, before you model anything |
| **Portfolio Construction** | 4 | turns a signal into weights, position limits and a rebalancing rule |
| **Backtest Engine** | 5 | runs the rules over history with costs and no look-ahead, and returns the track record |
| **Attribution Analysis** | 6 | splits the return into known factor exposure and the part that is actually yours |

**Two doors.** KaxaNuk's platform drives the same pipeline from a workspace instead of a terminal —
build a universe, download data, construct a portfolio, run a backtest and attribution, each step
tracked to completion. The other door is `pip install`: the open-source libraries are public on
[PyPI](https://pypi.org/project/kaxanuk.data-curator/) and [GitHub](https://github.com/KaxaNuk), no
account and no platform login required, and `uv sync` installs the Data Curator.

The **licensed** engines — Backtest Engine and Attribution Analysis — are deliberately absent from
`pyproject.toml`, so their index URLs and keys never enter version control. **Portfolio Construction**
is absent too: it is KaxaNuk's own library, not distributed publicly yet. Install each by hand, as the
`portfolio-construction-runs`, `backtest-engine-runs` and `attribution-analysis-runs` skills describe,
and **guard their imports**: a notebook that uses one reports what is missing and skips. Without
Portfolio Construction an equal-weight book still needs nothing but the eligible set; without the
engines the pipeline still builds its portfolios and produces no backtest or attribution results
until they are there.

---

## The conventions worth keeping

Everybody will have their own ideas, and that is the point of a template rather than a framework.
But when we want to share a tool, some names have to mean the same thing in both repositories.

### Where each kind of logic goes

**The prefix tells you which stage owns a column, and therefore which file to open.**

| Prefix | Built by | Scope | Change it when |
| --- | --- | --- | --- |
| `m_*` | the provider, via the Curator | raw market data | never — it is what arrived |
| `c_*` | `Data/Curator/custom_calculations.py` | **one security's own history** | you need a new per-security quantity |
| `r_*` | `Data/Refinery/custom_calculations.py` | **securities against each other, per date** | you need a rank, a breadth reading, or a column with a setting an experiment will sweep — a fitted model, or a window |
| `current_*` | `Data/refinery.py`, joined from the security master | **today's classification — not point-in-time** | you group or report by something new. Never select on it |

Two rules follow, and one exception worth knowing:

- **A `c_*` column that needs to see other securities is misplaced** and belongs in the Refinery.
- **Widening the Curator's schema forces a refetch of every identifier.** That is deliberate — it
  is what stops a folder holding a mix of schemas — but it means the Curator is the wrong home for
  anything you intend to tune.
- **So a column with a setting to sweep — fitted, or a window such as a twelve-month return's —
  lives in the Refinery even when it is per-security.** Its settings are exactly what an experiment
  sweeps, and **a sweep must never cost a download.** Its *inputs* — arithmetic with nothing to
  tune — stay in the Curator.

### The names

| Name | What it is |
| --- | --- |
| `Universe/Investable_Universe.csv` | the seed. One row per security; **`main_identifier` is the only required column**, and every other column is yours |
| `Universe/Security_Master.csv` | the seed plus what the provider knows, written by step 2 |
| `Universe/Data_Issues.csv` | what is wrong with the downloaded files, written by step 2 |
| `Data/Curator/Time_Series/` | one file per identifier: `m_*` and `c_*` |
| `Data/Refinery/Time_Series/` | the same rows plus `r_*` and `current_*` — **the panel every experiment reads** |
| `Experiments/Experiment_N/` | one folder per idea: `BLUEPRINT_N.md`, `BRAINSTORMING_N.md`, `JOURNAL_N.md`, `FINDINGS_N.md`, and the notebook |
| `Portfolio/portfolio_weights.csv` | the book, in the shape the Backtest Engine reads |

### The four shared modules

Everything specific to a strategy lives in its notebook, where a reader can see it. Four Python
modules in `Experiments/` are shared between experiments for one reason: **if they differed between
experiments, comparing experiments would be meaningless.** Here, each is a description of what it
must do; the example adds the code beneath it.

| Module | Owns |
| --- | --- |
| `securities_panel.py` | reading the refined files, stitching renamed securities into one position, pivoting to `dates x securities` |
| `portfolio_construction.py` | turning an eligible set into weights through one signature, one rebalance date at a time on a history cut before it — the Portfolio Construction library called inside it where it is installed |
| `backtest_engine.py` | writing the weight file, running the engine, reading results back — the book's daily weights among them — and aligning variants onto one window |
| `attribution_analysis.py` | shaping the hand-supplied index and factor files, and the book's daily weights from the backtest, into what the attribution library reads — it rejects a file with only the rebalance dates — widening the book to every benchmark constituent at zero weight so the benchmark is compared whole, and saying what is missing before it tries |

**A strategy column is named in exactly two kinds of place: a notebook's setup cell, and the rule.**
Never in a shared module, so a signal cannot become every later experiment's default without anyone
deciding it.

---

## Where the template and the example live

Both are folders of
[`KaxaNuk/KaxaNuk-Researcher`](https://github.com/KaxaNuk/KaxaNuk-Researcher), readable on
GitHub without installing anything:

| Folder | What it is |
| --- | --- |
| [`templates/strategy/`](https://github.com/KaxaNuk/KaxaNuk-Researcher/tree/main/templates/strategy) | this — the shape of the process and a description of every file in it. What `init-strategy` copies |
| [`examples/liquid-golden-cross/`](https://github.com/KaxaNuk/KaxaNuk-Researcher/tree/main/examples/liquid-golden-cross) | one strategy, `liquid-golden-cross`, worked through the same folders and files the process expects — the documents filled in as far as the work has reached, the later steps as descriptions until they are run, the strategy's own lines between example markers. Read it, whole in a folder of its own with `init-example`; never build on it |

Each strategy made from the template is its own repository, published by its owner — one per
strategy.

**[`AGENTS.md`](AGENTS.md) is next**: the workflow, the bar any new signal has to clear, and the
five ways a backtest lies.
