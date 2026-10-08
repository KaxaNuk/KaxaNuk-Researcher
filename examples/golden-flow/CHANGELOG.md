# Changelog

Every notable change to this repository, newest first. The format is
`## X.Y.Z (YYYY-MM-DD)` with `### Added / Changed / Deprecated / Fixed / Removed`, and
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) in its numbering.

## What a version number means here

This is a research repository, not a library, so there is no public API to version. What the team
depends on is **the results and the pipeline that produces them**, so that is what the number
tracks:

| Bump | Means | Triggered by |
| --- | --- | --- |
| **MAJOR** | **Published results are invalidated.** Anything quoted from an earlier version has to be re-derived before it can be repeated | Changing the universe, the date window, the backtest engine or its cost model, or the definition of an existing strategy. Removing a stage |
| **MINOR** | **New capability; existing results still stand** | A new experiment, signal, stage, diagnostic or document. Anything additive |
| **PATCH** | **Nothing about any result changes** | Bug fixes in tooling, documentation, repository hygiene, refactors that produce identical output |

Three conventions follow from reading it that way:

- **A result that changes is a MAJOR bump even if the code change was one line.** Severity is
  measured in what a reader has to throw away, not in the size of the diff.
- **Re-running the pipeline on refreshed data is not a version bump at all.** The strategy did not
  change; only the data did. Say so in the entry and leave the number alone.
- **While on `0.x`, a result-invalidating change bumps MINOR** — the standard pre-1.0 convention.

**1.0.0 is reserved** for the first strategy that reaches **paper trading** (step 7) with its
results reproduced from a clean clone. Until then the leading zero is doing real work: it says the
results are still moving.

## How to write an entry

One entry per change-set, newest at the top. Under the heading, **one sentence saying what a reader
has to do differently** — that is the part people actually read. Then the lists, each item written
for somebody who was not in the room:

- **Say what moved and why, not what file you touched.** "The regime model lives in the Refinery so
  a penalty sweep costs no download" is an entry; "updated custom_calculations.py" is a diff.
- **Name anything that invalidates a number**, and say which number.
- **A removal is a change-set too.** Deleting a stage that nobody could trace is worth an entry.

---

## 0.15.1 (2026-10-07)

**PATCH** — Golden Flow, copied into the KaxaNuk Researcher as its worked example. No number moves.

**What to do differently:** nothing to migrate. Copy it with `init-example`; the index and factor
files come from KaxaNuk's Analytics Factory, as `SETUP.md` says.

### Changed

- **The documents are shortened for a reader.** `README.md` says how to read the example and how
  to run it, states its rule, and shows how it uses the KaxaNuk Investment Lab and the Analytics
  Factory. Elsewhere, Golden Flow's lines sit between markers, after the template's guidance they
  answer.
- **`JOURNAL_1.md` starts on 2026-10-05.** It keeps every entry from then on, whole, except the
  2026-10-06 entry that retired the brainstorming file. Private names, a local path and a branch
  name are replaced in square brackets. A dated entry at the end records this copy.
- **Eighteen notes are carried, and five are kept only as leads.** Each carried note keeps *What it
  says* word for word. Its implication is rewritten and dated, after `FINDINGS_1.md` reported.
- **The code is Golden Flow 0.15.1's, with these differences:**
  - each shared module opens with the template's docstring; Golden Flow's own sentences about a
    module, where it has them, open its marked code as a comment;
  - each notebook keeps the template's markdown cells, with Golden Flow's paragraphs between
    markers; every code cell is Golden Flow's, starts `# EXAMPLE-ONLY CELL`, and has no outputs;
  - `Data/hand_supplied.py` reads the Analytics Factory's own file names,
    `KN_US_Equity_Benchmark_Holdings.csv` and `KN_US_Equity_Benchmark_Returns.csv`. They are
    byte-identical to the files Golden Flow read under the KN US Equity Core's name: md5
    `eba4bf64ffa8de5d650e4e2c4b21844d` and `1668b564582f1871d7e4a6f39896e50a`;
  - the Analytics Factory is named in place of Golden Flow's older name for it, in comments,
    docstrings and one message, and a line this made longer than 100 columns is rewrapped;
  - `Universe/seed.py` takes `--index-master` as a required argument and names no machine path.
    Its shorter docstring says it overwrites the committed seed, and ships to show how the seed was
    built;
  - `.gitignore`, `Config/.env.template`, `.gitattributes`, `LICENSE`, `CLAUDE.md` and
    `pyproject.toml` are the template's; `pyproject.toml` is named `golden-flow`, at 0.15.1;
  - no `uv.lock` is committed, so the library versions resolve when `uv sync` runs. The recorded
    figures were run on Backtest Engine 0.66.0 and Attribution Analysis 0.2.0.
- **Byte for byte:** the seed, `Universe/Investable_Universe.csv`, and in
  `Paper_Trading/Paper_Trading_1/` the frozen copies and `FREEZE.json`.
- **`Paper_Trading_1` is a record here, not a running book.** Its frozen security master is not
  shipped, and `Data/Curator/custom_calculations.py` and `paper_trading_1.py` no longer match the
  hashes registered for them. `daily_update.py` stops the book, as `Paper_Trading/BITACORA.md` says.

### Fixed

Golden Flow 0.15.1's own fixes, which this copy carries:

- **`FINDINGS_1.md` keeps the promises `Paper_Trading/BITACORA.md` made before the run.** It
  publishes all twenty random books — each drawing, on the rule's dates, as many index members as
  the rule holds. Each comes with its idiosyncratic return (the part no factor explains), its
  Sharpe and its CAGR (compound yearly return).
- **The sweep is published in full.** Each of its eight perturbed settings sits beside its control,
  with both margins. The golden cross is a 50-day average above the 200-day; a control is the same
  setting without it. Beside the cap rows, how often the cap binds: 620 of 1,408 rebalance dates at
  15%, 341 of 1,381 at 20% and 141 of 1,358 at 25%.
- **The timing arm is stated.** The shifted-entry timing arm was not run, so timing is not
  separated from selection.
- **11.81 years**, in `FINDINGS_1.md` and `RESULTS.md`, is labelled the engine's count: 2,976
  weekday steps after the first day, over 252. The window spans 11.41 calendar years.
- **`OBJECTIVE.md` quotes the owner with "top 35"**, as the journal records it, and then the answer
  that retired the count. The earlier quote had dropped the number without an ellipsis.

## 0.15.0 (2026-10-06)

**MINOR** — Experiment 1, on the KN US Equity Core, the Analytics Factory's index of about 600 names
a day. The rule holds the members in a golden cross, ranked and weighted by 63-day traded value,
none above 20% and none below 1%. Measured on 2026-10-06 from a wiped working copy, it compounds at
20.33% a year at a Sharpe of 0.842 over 2015-01-02 to 2026-06-01, net of costs. Its control made
19.73% at 0.763, and the KN US Equity Core 13.05% at 0.713. Nine tenths of the excess return is
factor exposure. The book passed criteria 1 to 4 of the paper-trading gate. The owner signed the
fifth the same day, and it went to paper trading as `Paper_Trading_1`.

**What to do differently:** quote every figure as in sample; `FINDINGS_1.md` sets each beside its
comparison.

### Added

- **`OBJECTIVE.md`**, from the owner's words: the idea and its three claims, the signal, the sizing
  and the construction.
- **`Bibliotheca/`**: the notes behind the claims.
- **The seed**, `Universe/Investable_Universe.csv`: the 896 listings that were KN US Equity Core
  members on some date from 2015-01-02.
- **The data stage**, run on 2026-10-06: 892 names asked of FMP through 2026-10-05, 809
  downloaded and 83 it does not carry; `CY` and `NBL` dropped by the universe notebook, their FMP
  prices contradicting their membership.
- **The drivers, the modules and three notebooks** — universe, analyzer and experiment. Each
  notebook ends in a Verify section that raises when a check fails.
- **Experiment 1's `BLUEPRINT_1.md`**, committed before the rule was coded, with its `JOURNAL_1.md`
  and `FINDINGS_1.md`.
- **`Paper_Trading_1`**, the book frozen on 2026-10-06. What it must show on paper, and when it is
  stopped, were registered in `Paper_Trading/BITACORA.md` before its first day.

### Provenance

Golden Flow is the KaxaNuk Investment Lab's reference strategy, worked in a repository of its own.
The KaxaNuk Strategy Template was first extracted from its version 0.9.0. This copy is curated from
its version 0.15.1, and every figure is as that version recorded it. Two earlier versions of
Golden Flow tested the thirty most traded names of another index. They are not part of this
example, but the 23 and 14 books they priced count in Experiment 1's trial count of 107 books.
