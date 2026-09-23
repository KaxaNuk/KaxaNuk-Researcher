---
name: experiment-lifecycle
description: >
  Load this skill whenever you start, structure, run or document a KaxaNuk Investment Lab strategy
  repository or one of its experiments. Use it when the user asks to start a strategy from the
  KaxaNuk Strategy Template, scaffold an Experiments/Experiment_N/ folder, write a blueprint,
  journal, brainstorming or findings file, update RESULTS.md or the changelog, or move a strategy
  through the order of work and the eight steps. It defines the document architecture, each file's
  contract, the notebook section contract and where each kind of logic goes, and points to the
  restrictions, the bar a new signal must clear and the graduation gate. It does NOT cover what
  another tool owns: step 1 (the KaxaNuk Researcher), `universe-point-in-time`,
  `data-curator-custom-calculations`, `data-analyzer-runs`, `portfolio-construction-runs`,
  `backtest-engine-runs`, `attribution-analysis-runs`, `alpha-decomposition`,
  `paper-trading-gate`, or branches and changelogs (`how-we-work`).
metadata:
  version: 0.8.1
---

# The research process — how a strategy repository is worked in

Every KaxaNuk Investment Lab strategy lives in its own repository, copied from the **KaxaNuk
Strategy Template**, which ships in `KaxaNuk/KaxaNuk-Researcher` as `templates/strategy/`. The
template is the shape and every file the process expects in it: six folders, the documents at the
root, and inside the folders each driver, module, notebook and document as a description of what
belongs there — a `.py` file as its docstring, a notebook as its markdown cells — to be filled in
with the strategy's own. The worked example beside it, `examples/liquid-golden-cross/`, works one
strategy, `liquid-golden-cross`, through the same files, with the strategy's own lines between
example markers. The fixed shape buys comparability and legibility: any experiment looks like any
other, every experiment is measured against the same declared benchmark, and a CIO reads the whole
state of a project from two files, `OBJECTIVE.md` and `RESULTS.md`.

Work in English: notebook narrative, documents, function names and comments.

**To start a new strategy, copy the template; never scaffold one by hand.** The owner runs
`init-strategy <name>`, from the KaxaNuk Researcher, which copies it into a new folder by script and
makes it a repository; the new folder's own `SETUP.md` owns the rest of the procedure. To work
inside a strategy repository, follow this skill. `references/structure.md` has the tree, what is
committed, and the steps to fill it in. **Do not name Obsidian, a deck, or any KaxaNuk in-house
strategy in a repository document.**

## 1. The eight steps

Steps 1 to 7 are the Investment Lab and live in the repository. Step 8 does not: a strategy leaves
the Lab when it is funded, outside the repository. Each stage owns its outputs and reads only from
the stage above it.

| # | Step | In plain words | It produces | It prevents | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | **Bibliotheca** | the idea and its claims first, then the literature that argues with them | a referenced hypothesis, dated | backtesting a hunch you cannot defend | `OBJECTIVE.md`, `Bibliotheca/` |
| 2 | **Universe** | the eligible list, rebuilt for each date rather than for today | a point-in-time membership table | survivorship bias | `Universe/` |
| 3 | **Data** | curation, then refinery, then analysis | a reproducible dataset, and evidence a feature carries signal | beautiful results from broken inputs | `Data/` |
| 4 | **Portfolio** | how much of what, and how often you change your mind | weights with position and turnover limits | a good signal in a book nobody could hold | `Experiments/Experiment_N/` |
| 5 | **Backtest** | the simulation, run by the Backtest Engine | a cost-aware track record | paper returns real trading would erase | `Experiments/Experiment_N/Backtest/` |
| 6 | **Attribution** | which part of the return did you actually earn? | factor and idiosyncratic breakdown | selling factor beta as alpha | `Experiments/Experiment_N/Attribution/` |
| 7 | **Paper trading** | a dress rehearsal on data nobody has seen | out-of-sample evidence | plumbing problems on day one of funding | `Paper_Trading/` |
| 8 | Production | real capital, real monitoring, a drawdown policy | a funded strategy with an owner | research that stays research | outside the repository |

**A stage that recomputes something an earlier stage produced has broken the process**, even when
the number matches: the next experiment computes it slightly differently and the two stop being
comparable. A step is finished when its output is reproducible from the step above by re-running
one command or one notebook.

The six Lab modules map one to one onto the stages: Data Curator (`Data/curator.py`), Data Refinery
(`Data/refinery.py`), Data Analyzer (`Data/analyzer.ipynb`), Portfolio Construction
(`Experiments/portfolio_construction.py`), Backtest Engine (`Experiments/backtest_engine.py`),
Attribution Analysis (`Experiments/attribution_analysis.py`). Four have libraries — the Data
Curator, Portfolio Construction, the Backtest Engine and Attribution Analysis — and two, the
Refinery and the Analyzer, are hand-rolled until theirs land; a hand-rolled stage says so in its
docstring and names the interface its library will replace. A skill says how each library is called:
`data-curator-custom-calculations`, `portfolio-construction-runs`, `backtest-engine-runs` and
`attribution-analysis-runs`, with `universe-point-in-time` for step 2, `data-analyzer-runs` for the
hand-rolled Analyzer, and `paper-trading-gate` for step 7. **Step 1 is the KaxaNuk
Researcher's**, `KaxaNuk/KaxaNuk-Researcher`, whose home `init-researcher` makes: its `objective`
drafts the claims, its `read` writes the notes in `Bibliotheca/`, and its `blueprint` drafts
`BLUEPRINT_N.md` with every prediction citing a note.

## 2. The control documents

Four files at the root carry the whole state. Everything else is code, or a note feeding one of
them.

| Document | Holds | Changes when |
| --- | --- | --- |
| `OBJECTIVE.md` | the main idea, the objective, the claims inside it with their status | the idea and the claims' wording almost never — a change there is a different strategy; each claim's evidence and status move as notes arrive (B) and as findings report (H) |
| `RESULTS.md` | the executive summary of every experiment, **compiled from the `FINDINGS_N.md` files and citing each** | a `FINDINGS_N.md` changes |
| `CHANGELOG.md` | every version, newest first, in the form `how-we-work` section 3 gives: `## X.Y.Z (YYYY-MM-DD)` and its five headings | any change-set lands |
| `AGENTS.md` | how work is done: workflow, who writes each document, restrictions, the bar, the five ways a backtest lies | the process changes |

`CLAUDE.md` is one line, `@AGENTS.md`. `README.md` says what the repository is and where each kind
of logic goes. `Paper_Trading/BITACORA.md` is the graduation gate — a contract, deliberately not
named `JOURNAL`, because a journal here is an append-only dated log.

**When a number changes, change it in `FINDINGS_N.md` first, then `RESULTS.md`.** One exception:
findings from step 3 go straight into `RESULTS.md`, because notebook outputs are stripped before
committing and a measurement living only in a cell output does not survive the commit.

## 3. The four files in every experiment

Each `Experiments/Experiment_N/` is one idea: four markdown files, a notebook, and three gitignored
output folders (`Portfolio/`, `Backtest/`, `Attribution/`, each kept by a `.gitkeep`).

| File | Holds | Who writes it | Changes when | Template |
| --- | --- | --- | --- | --- |
| `BLUEPRINT_N.md` | **the hypothesis** — thesis, rules, predictions, success criteria, risks | a person, or with the AI | **never, once written** | `references/blueprint-template.md` |
| `BRAINSTORMING_N.md` | **planning** — ideas, what to try, what was dropped | a person, or with the AI | thinking happens, before the work | `references/brainstorming-template.md` |
| `JOURNAL_N.md` | **the running log**, dated, oldest first | the AI, as work proceeds | append only; a correction is a new entry | `references/journal-template.md` |
| `FINDINGS_N.md` | **the latest results worth keeping** | the AI, from the journal | rewritten when a result changes; feeds `RESULTS.md` | `references/findings-template.md` |

`BLUEPRINT` is fixed so a result cannot reshape the question it was meant to answer. `JOURNAL` is
append-only so the path is recoverable. `FINDINGS` is rewritten so there is one current answer.
`BRAINSTORMING` looks forward so planning is never mistaken for history. **Every prediction in a
blueprint cites where it comes from** — a note in `Bibliotheca/` or a section of the analyzer — and
a prediction with no source is a lead to read first, not a prediction.

Repository-level history — the benchmark once the first entry of `BRAINSTORMING_1.md` has chosen it,
the data step, the architecture — belongs in `JOURNAL_1.md`, Experiment 1 being the declared
benchmark. Later journals point there. That brainstorming entry is the one step allowed before
`BLUEPRINT_1.md`: Experiment 1 *is* the benchmark, so choosing it cannot wait for the blueprint that
depends on it.

## 4. The notebook — one section contract, one cell that is the strategy

`experiment_N.ipynb` follows the same sections every time. `references/experiment-notebook.ipynb` is
the worked example's Experiment 1 notebook with its own cells stripped — markdown only, one cell per
section saying what that section computes — and is the file to copy.

| Section | Contains |
| --- | --- |
| Header · Position in the pipeline · What this notebook does not do | the claim, the standing warnings, the four shared modules |
| 0 · Setup | paths, and **the strategy's columns** — signal, mark price, fill price, commission price — the only strategy names in the notebook outside the rule |
| 1 · The panel | refined files to `dates x securities` matrices, renamed securities stitched into one position by ISIN |
| 2 · The rule | selection, sizing, timing; must produce `selected_matrix`, `REBALANCE_DATES`, `target_weights` with rows summing to **at most** 1.0; 2.1 asserts the invariants |
| 3 · Construction | the book's shape — invested share, trigger frequency, turnover, concentration, group drift; 3.1 writes the deliverables, `portfolio_weights.csv` with cash as a real priced position |
| 4 · Backtest | the KaxaNuk Backtest Engine, the only backtest anywhere; guarded import, reports and skips without a licence |
| 5 · Attribution | Brinson-Fachler, the factor model, and Brinson-Fachler again on the residual; guarded the same way |
| 6 · Counterfactuals | the arms that price who earned the idiosyncratic share: the same book with one choice removed, priced by the same engine |
| 7 · Verdict | what it concluded, in words |
| Handoff · Open items | what the next stage consumes; what this one left open |

**Two look-aheads are stated plainly and nowhere else:** the signal used on rebalance date *t* is
the one observed at *t-1* (the lag), and a delisting exit needs one day of hindsight, because a
position is sold on the last day it still has a fill price.

**Four modules beside the notebook are shared by every experiment**, one per Lab library:
`securities_panel.py` (the one panel loader), `portfolio_construction.py` (eligible set to weights,
one signature every scheme shares, the Portfolio Construction library called inside it one rebalance
date at a time where it is installed, constraints switched off by default as levers a later
experiment earns), `backtest_engine.py` (the one path from a weight file to a number),
`attribution_analysis.py` (shaping the hand-supplied inputs and the book's **daily** weights from
the backtest — the attribution library rejects a rebalance-only file — and saying what is missing
first). **A strategy column is named in exactly two kinds of place — a notebook's setup cell and the
rule — never in a shared module**, so a signal cannot become every later experiment's default
without anyone deciding it. Experiment 1 loads the panel through `securities_panel.py` like every
later experiment, so the comparison is on the rule and nothing else.

## 5. Where each kind of logic goes

**The prefix tells you which stage owns a column, and therefore which file to open.**

| Prefix | Built by | Scope |
| --- | --- | --- |
| `m_*` | the provider, via the Curator | raw market data — never edited |
| `c_*` | `Data/Curator/custom_calculations.py` | **one security's own history** |
| `r_*` | `Data/Refinery/custom_calculations.py` | **securities against each other, per date**, or anything fitted |
| `current_*` | `Data/refinery.py`, joined from the security master | today's classification — **not point-in-time**; group or report by it, never select on it |

A `c_*` column that needs other securities is misplaced. Widening the Curator's schema refetches
every identifier, so nothing tunable lives there: **a fitted column lives in the Refinery even when
it is per-security, because a sweep must never cost a download.** Its inputs — arithmetic with
nothing to tune — stay in the Curator.

## 6. Scaffolding

**A new strategy.** Follow the template's `SETUP.md` — the repository, `uv sync`, the credential
file; the skills are installed once for the user, not here — then work in this order. **It is an
index of *Starting your own strategy* in the template's README**, which is the source and says why
each part comes where it does; the parts are lettered A to H so they are never mistaken for the
eight steps. What this skill adds is the last column — which tool each part loads. The KaxaNuk
Researcher's `next` command reads a strategy against this list and names the part that comes next.

| | Part | Lands in | Load |
| --- | --- | --- | --- |
| A | The objective, **before any paper is read** | `OBJECTIVE.md` | the KaxaNuk Researcher, `objective` |
| B | The reading, for each claim; then the objective fine-tuned from the notes | `Bibliotheca/`, then `OBJECTIVE.md` | the Researcher, `read`, then `objective` |
| C | The investable universe, delisted names included | `Universe/Investable_Universe.csv` | `universe-point-in-time` |
| D | The data — curator, universe notebook, refinery, analyzer, in that order | `Data/`, and `RESULTS.md` for the analyzer's measurements | `data-curator-custom-calculations`, `universe-point-in-time`, `data-analyzer-runs` |
| E | The benchmark, then `BLUEPRINT_1.md` **before the rule** | `Experiments/Experiment_1/` | this skill; the Researcher, `brainstorm` and `blueprint` |
| F | The broad reading, and brainstorming | `Bibliotheca/`, `BRAINSTORMING_1.md` | the Researcher, `read` and `brainstorm` |
| G | The cycle — portfolio, backtest, attribution | the notebook, `FINDINGS_1.md` | `portfolio-construction-runs`, `backtest-engine-runs`, `attribution-analysis-runs`, `alpha-decomposition`; the Researcher, `challenge` |
| H | Every finished cycle, kept or rejected | `RESULTS.md` | this skill |

Then the gate — `Paper_Trading/BITACORA.md`, `paper-trading-gate` — or the next experiment.

Every file those parts name is in the template, and so in a strategy made from it: each a
description of what belongs in it, to be filled in — the drivers, modules, notebooks and experiment
files generated from the worked example with its own lines removed. A strategy made from a template
before 0.10.0 lacks the files inside the folders; bring one across with `init-example <path>` — it
copies from the example inside the KaxaNuk Researcher and never overwrites, so bring
`Universe/universe.ipynb` by its path — and delete what is the example's: everything between the
markers.

**A new experiment `N` inside an existing strategy:**

1. Create `Experiments/Experiment_N/` with `Portfolio/`, `Backtest/`, `Attribution/`, each holding a
   `.gitkeep`. The template's `.gitignore` already covers them.
2. Copy the four templates from `references/`, replacing `N`. **Write `BLUEPRINT_N.md` before any
   code**, stating the economic mechanism and citing every prediction's source. The blueprint
   template is the benchmark's; delete the sentences that only apply to Experiment 1.
3. Copy `references/experiment-notebook.ipynb` to `experiment_N.ipynb`. It too is the benchmark's:
   retitle it `Experiment N`, replace every `_1` in it with `_N`, and delete the sentences that
   only apply to Experiment 1. Then declare the experiment's columns in section 0; import the
   panel loader in section 1; write the rule in section 2.
4. Add a row to `RESULTS.md` when `FINDINGS_N.md` first reports, citing it. A new experiment is a
   MINOR bump in `CHANGELOG.md`, and the entry is part of the change-set.

## 7. Where the rules live

Every strategy repository carries its rules in `AGENTS.md`, committed on `main`, so they are there
whether or not the skills are installed. **This skill does not restate them**: a rule written twice
is two rules, and the copies drift. Read them where they are.

| Rule | Where |
| --- | --- |
| One experiment at a time, and its exceptions | `AGENTS.md`, *One experiment at a time* |
| The bar any new signal must clear | `AGENTS.md`, *The bar any new signal must clear* |
| Committed results, bad runs, binaries, Production, `Config/.env`, example markers | `AGENTS.md`, *Other standing rules* |
| The five ways a backtest lies, and what look-ahead costs a fitted signal | `AGENTS.md`, *Research integrity — the five ways a backtest lies* |
| What attribution must report | `AGENTS.md`, *What attribution must report*; reading it is `alpha-decomposition` |
| The graduation gate and its five criteria | `Paper_Trading/BITACORA.md`, in the template |
| What a version number means | `CHANGELOG.md`, *What a version number means here* |

## References

- `references/structure.md` — the template's tree, what is committed, and the steps to fill it in.
- `references/blueprint-template.md`, `brainstorming-template.md`, `journal-template.md`,
  `findings-template.md` — the four documents of an experiment, the blanks for Experiment N > 1;
  the template ships Experiment 1's, the same files under `Experiments/Experiment_1/`.
- `references/experiment-notebook.ipynb` — Experiment 1's notebook, markdown only, the blank for
  `experiment_N.ipynb`.

The four documents and the notebook are copies of Experiment 1's files in the worked example,
`examples/liquid-golden-cross/` in KaxaNuk-Researcher, with the example's own lines stripped — what
the template ships as Experiment 1, kept here for every experiment after it.
`uv run --no-project python tools/sync_investment_lab_references.py` there regenerates them, and
`tools/check_repo.py` fails when they differ; `references/structure.md` is kept by hand.
