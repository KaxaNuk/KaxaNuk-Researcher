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

## 0.12.0 (2026-09-23)

**MINOR** — template 0.12.0, and Experiment 1's second design, fixed before any rule: the owner
rewrites it to sell a broken cross the day after it breaks. The first design's results stand until
the second reports, and stay at tag `v0.15.0` and as a row of `RESULTS.md` after it does.

**What to do differently:** set `KN_ANALYTICS_PATH` to the desk's folder. Nothing to re-derive yet:
the rule, the run and the findings follow this blueprint's commit.

### Added

- **The paper-trading machinery as code**: `promote.py`, `daily_update.py` and `record.py`, with
  `Data/hand_supplied.py` and `Data/curator.py --end-date`, as template 0.12.0 describes them.
- **The cross as a 0/1 state, and what a broken cross costs**, in section 5 of the analyzer, and in
  `RESULTS.md` rows 10 to 18, measured on the panel that ended on 2026-06-01; the rows 2 to 5 of
  2026-09-19 reproduce and now carry their signs. The analyzer stops at 2026-06-01: the months
  after it are held out.
- **Experiment 1's second design**: a `BRAINSTORMING_1.md` entry with the first design's delay —
  9.6% of its held name-days in a stock already below its cross, a median of 19 days after a break
  — and the owner's decision; a `JOURNAL_1.md` entry on the rewrite and on the band the first
  design's code applied; and a new `BLUEPRINT_1.md`, reviewed cold and revised before any rule:
  twenty names, sold the day after the cross breaks, a buffer of thirty and monthly
  re-equalisation, against the index and the same rule without the cross, with margins, a kill
  switch over three sub-periods, fifteen perturbation cells and a trial count of thirty-one.

### Changed

- **The universe notebook reads the desk's holdings** through `Data/hand_supplied.py`, and dates the
  point-in-time start by where the seed covers the index rather than by the file's first row.
- **`Experiments/attribution_analysis.py`** reads the desk's files through the same module.

## 0.11.0 (2026-09-23)

**MINOR** — template 0.11.0: the bar's three new items, the claim each experiment moves, and a
Verify section at the end of every notebook, here as code. Nothing about any result changes: every
published figure stands, and nothing was re-run.

**What to do differently:** nothing to re-derive. The next run of the analyzer writes the share of
dates with the expected sign, and the next run of any notebook stops at its Verify section if what
it wrote is wrong.

### Added

- **A Verify section in each of the three notebooks, as code that reads back what the notebook
  wrote and raises.** The universe's checks the master against the seed, the register's eight
  checks, and that a usable date exists; the analyzer's, the coefficient table's rows, that its
  figures are finite, and that no row counts more dates than the panel has forward returns for; the
  experiment's raises on the invariants of section 2.1, reads back `portfolio_weights.csv`, and
  counts each engine run's valued days against the trading days of the window it was asked for —
  at least 99% of them valued, and no more than five unvalued at the end — and checks the
  attribution window. The engine and attribution checks skip, as sections 4 and 5 do, without a
  licence. None has run yet.
- **Section 4 of the analyzer writes `overlap_days` and `share_expected_sign`** to
  `information_coefficient.csv`: the days consecutive windows share, and the share of dates on
  which the coefficient was positive, the sign the rule expects.
- ***What a correct run shows* in the README**, stage by stage, from the figures `RESULTS.md`,
  `FINDINGS_1.md` and `JOURNAL_1.md` recorded, the re-run's beside the published ones where they
  moved. No stage's duration was recorded, so none is given.
- **An entry in `JOURNAL_1.md`** recording why the blueprint's new sections are left unfilled.

### Changed

- **`AGENTS.md`** as template 0.11.0's, and, inside the markers under the bar, a note that item 9
  was learned after this run: the first control chose its own dates.
- **`BLUEPRINT_1.md` changed after its test, and only in its template text.** The three new
  sections carry the template's guidance and, inside the markers, a note that each was not written
  on 2026-09-19 and where its answer lives; the hypothesis inside the markers is unchanged.
- **`FINDINGS_1.md`'s status** names the claim the run moved: claim 1, the signal, to falsified, as
  `OBJECTIVE.md` records.
- **`RESULTS.md`**: the analyzer table has the sign column, *not measured* for the four coefficients
  and the ratio, since the run of 2026-09-19 did not compute it; the experiments table has *Claim
  moved*; limitation 2 says what the control is, as the template's, and is written as a condition on
  any experiment that claims a margin, so it no longer contradicts the control column of the
  experiments table.
- **Criterion 1 of `Paper_Trading/BITACORA.md`** says which control, as the template's.
- **`SETUP.md`'s note for the agent** pins APM 0.29.0, as the template's.
- **The README's example-only line** says the example is for reading and running, where it said
  *for reading and copying*: its lines are never copied into a strategy of one's own.

### Removed

- **`uv.lock`.** The example no longer commits one: its library versions resolve when `uv sync`
  runs. A strategy made from the template still commits its own, as `SETUP.md` says.

## 0.10.6 (2026-09-23)

**PATCH** — template 0.10.5: the template's files are the example's without its marked lines, kept
in step by hand. Nothing about any result changes.

**What to do differently:** nothing.

### Changed

- **`AGENTS.md`'s rule on marking this example's content**, inside the example markers, says a line
  left unmarked belongs in every new strategy too, and no longer names the sync tool.

## 0.10.5 (2026-09-23)

**PATCH** — template 0.10.4: `AGENTS.md`'s paragraphs on where the template and the example live are
one, `Bibliotheca/BIBLIOGRAPHY.md` names `Papers/` among the folders created on first use,
`apm.yml` is gone, and `SETUP.md` and `BIBLIOGRAPHY.md` are rewrapped at 100 columns. Nothing about
any result changes.

**What to do differently:** nothing.

### Changed

- **`AGENTS.md`'s two paragraphs on where the template and the example live are one**, as template
  0.10.4's: the example is for reading, nothing in a strategy is brought across from it, and what
  the template ships is *What is in here* in its README. *In this example*, between the markers, is
  unchanged.
- **`Bibliotheca/BIBLIOGRAPHY.md`** says `Papers/`, `Books/` and `Notes/` are directories created on
  the day there is something to put in them, so the template's generated copy names all three.
- **Four lines of `SETUP.md` and `Bibliotheca/BIBLIOGRAPHY.md` are rewrapped at 100 columns**, as
  the template's.
- **`SETUP.md`'s note on the example**, between the markers, says a file a strategy lacks comes
  from the template, never from here, and that the template's README says how; it pointed to the
  README for how to copy a file from here.

### Removed

- **`apm.yml`**, as template 0.10.4 removes it: a strategy installs nothing, and nothing read it.
  `SETUP.md` step 5 renames and versions `pyproject.toml` alone, and `.gitignore`'s header and
  *What "done" looks like* no longer name it. This example's version is in `pyproject.toml` and
  `uv.lock`.

## 0.10.4 (2026-09-23)

**PATCH** — template 0.10.3: work lands on `main`, the who-writes table, the log's header,
`SETUP.md`'s licence and researcher lines and `.gitattributes`; and this strategy's own lines in
`Bibliotheca/` and `AGENTS.md` marked, so the template's copies are generated from here. Nothing
about any result changes.

**What to do differently:** nothing.

### Added

- **`.gitattributes`**, `* text=auto eol=lf`, as template 0.10.3 carries.
- **A row for `Bibliotheca/LOG.md` in `AGENTS.md`'s who-writes table**, and the log's header says
  whoever reads or audits appends it, the researcher's `read` and `audit` themselves, and a past
  entry is never edited.

### Changed

- **Work lands on `main`**, as template 0.10.3 says: *How work reaches `main`* drops the issue,
  the branch and the pull request as a gate, and *The blueprint is committed before the rule* keeps
  the blueprint in a commit of its own, before the rule cell holds code.
- **`OBJECTIVE.md`'s "Changes when" cell** separates the idea and the claims' wording from each
  claim's evidence and status, as template 0.10.3 does.
- **`SETUP.md`** points to *In a strategy or another project* in the researcher's own README for
  its identity to load with it, says `LICENSE` names KaxaNuk as the holder, and says it is the
  first `---` line of `CHANGELOG.md` that is kept above.
- **`BLUEPRINT_1.md`** says, outside the markers, that each prediction cites a `Bibliotheca/` note
  or a section of `Data/analyzer.ipynb`.
- **`Bibliotheca/LOG.md`'s entries and `AGENTS.md`'s rule on marking this example's content sit
  inside example markers**, and `BIBLIOGRAPHY.md`'s Part 5 row on Sullivan, Timmermann & White
  reads as the template's — its note is linked from its Part 1 row — so the template's
  `BIBLIOGRAPHY.md` and `LOG.md` are generated from here with the rest.

## 0.10.3 (2026-09-22)

**PATCH** — four lines that were this strategy's, outside its markers, reached the template.
Nothing about any result changes.

### Changed

- **Experiment 1's counterfactuals sentence no longer points at cells below it**, and the
  notebook's first open item states its condition rather than this strategy's state.
  `BLUEPRINT_1.md`'s open questions get a placeholder table outside the markers, as its
  predictions already had. One line of `Paper_Trading/BITACORA.md` is re-wrapped.

## 0.10.2 (2026-09-22)

**PATCH** — `AGENTS.md` and `SETUP.md` follow template 0.10.0, which ships every file this example
works through as a description to fill in. Nothing about any result changes.

### Changed

- **`AGENTS.md` and `SETUP.md` no longer say a strategy takes its files from here** with
  `init-example <path>`: the template holds them, generated from this example with its marked lines
  removed. The example markers are now what that generation strips, so a line of the worked
  strategy left unmarked reaches every new strategy.

## 0.10.1 (2026-09-22)

**PATCH** — three chapter notes renamed so their paths stay under the 120 characters the
package's repository check allows once the example sits under a home folder; every link to them
rewritten. Nothing about any result changes.

### Fixed

- **Three note paths ran past the limit** the check enforces for Windows: Grinold and Kahn's
  chapter 16 note is now `19_Transactions_Costs.md`, and Paleologo's chapters 6 and 8 are
  `10_Alpha_Sizing.md` and `12_Your_Performance.md`. The book indexes, the notes that cross-link
  them and `OBJECTIVE.md` point at the new names; `Bibliotheca/LOG.md` records the rename.

## 0.10.0 (2026-09-22)

**MINOR** — every claim in `OBJECTIVE.md` now has a note behind it, the objective's evidence for
claims 2 to 4 is rewritten from those notes with no claim's wording changed, and Experiment 1 meets
its last success criterion: re-run from a wiped working copy on a fresh download, every conclusion
holding. No published figure changes.

**What to do differently:** read the objective's sections on claims 2, 3 and 4 before proposing
the sizing or the band experiment: each now names the arms, the predictions and the measurement
its notes ask for. Read the figures in `FINDINGS_1.md` with the error bar its re-run table gives:
a fresh download moves them at the second decimal. A copy made before this version can take the
new notes with `init-example Bibliotheca`.

### Added

- **Six notes for claims 2 and 4, carried from a researcher's library without re-reading the
  PDFs.** Grinold and Kahn's chapters 13, 14 and 16 — the band's own source, and the case against
  it — with the book's index, and Paleologo's chapters 6 and 8, on when a signal's strength should
  set the size and how to measure whether it does. Claim 4 had no note; claim 2 had two marked *to
  come*.
- **Two papers read whole.** Baltussen, Dom, Van Vliet and Vidojevic (2025), the momentum review,
  for claim 1 and the objective's *not that this is momentum* line: what the book's +12.75
  momentum points are, and are not. Sarkar, Du and Vafai (2019) for claim 3: what a book of the
  largest companies loads on once sectors are in the model, and why open lead 3 — the eleven
  sector factors reading zero — is more than a cosmetic defect.
- **A contradiction recorded.** The momentum review finds downside risk cannot explain the
  momentum premium, where Paleologo's chapter 5 carried two studies saying it makes momentum
  redundant; the older claim stays, under a callout naming the newer note.
- **`SETUP.md` names the hand-supplied files exactly** — the two benchmark files, their headers and
  date order, and the lower-case factor files with the four reserved `f_` names — because a file
  named otherwise is not found, or is counted as one more factor.
- **A re-run table in `FINDINGS_1.md`**, the published figures beside the ones a wiped copy on a
  fresh download returned on 2026-09-22, and a tenth caveat naming the drift.

### Changed

- **`OBJECTIVE.md`, claims 2 to 4, fine-tuned from the notes.** Claim 2 is stated as the 1/N rule
  on a signal with no conviction, with the arm that tests it and its predictions fixed. Claim 3
  records what the paper says a large-cap book loads on — not size — and that the 28 points
  assigned to the ranking are provisional until a sector block or a rate term is in the model.
  Claim 4 records the three conditions its rule of thumb came with, and the band sweep as a
  frontier with the delay test run first. The status column and every claim's wording are as they
  were.
- **Success criterion 1 of Experiment 1 is met, to the data.** The pipeline ran end to end from a
  wiped working copy with no manual step beyond the hand-supplied files; the filter-off control and
  the index came back to every published decimal, the rule within hundredths and one rebalance.
  `JOURNAL_1.md` has the run, `RESULTS.md`'s *Does it reproduce?* the answer, and the status
  banners say so.

## 0.9.0 (2026-09-22)

**MINOR** — the example runs as far as it can without the licensed engines and the hand-supplied
index, fetches profiles from FMP's current API, and sizes with every Portfolio Construction method
whose configuration has no required field; `SETUP.md` no longer describes an install a strategy
never runs, and the Data Curator floor is 0.50.0. No result changes.

**What to do differently:** in a copy made before this version, delete
`Universe/Provider_Cache/profiles.json` if the old cell filled it, so `universe.ipynb` fetches the
profiles again. Once a licensed engine is installed by hand, use `uv sync --inexact` and `uv run`,
never a bare `uv sync`.

### Added

- **Step 2 of `SETUP.md` warns that `uv sync` is exact.** It removes every package `uv.lock` does
  not name, so a bare `uv sync` uninstalls the Backtest Engine, Attribution Analysis or Portfolio
  Construction once any of them is installed by hand; `uv sync --inexact` and `uv run` keep them.
- **`SETUP.md` says the benchmark cannot be downloaded.** The KN600's holdings and returns, and the
  factor returns, are supplied by hand, and it says where each part of the example stops without
  them: `Data/curator.py` downloads every price, `universe.ipynb` writes the master and the issues
  file, and Experiment 1 stops in its first cell. Every number the example measured is in
  `RESULTS.md`.
- **`Experiments/Experiment_1/JOURNAL_1.md` records how the findings answered the challenge of
  2026-09-20.** `FINDINGS_1.md` and `RESULTS.md` were corrected after it — prediction 5
  falsified, the tally, caveat 9, the success criteria and the two closed predictions — and no
  entry said so. No result changes.

### Changed

- **Step 5 of `SETUP.md` gives a new strategy its own identity**: `pyproject.toml`'s name, both
  versions set to `0.1.0`, the template's changelog entries replaced by the strategy's first, and
  `uv lock` run before the commit.
- **`SETUP.md`'s Windows short-path advice gives the real reason**: deep paths inside the folder,
  such as `.venv/`, can pass Windows' path limit and fail with misleading errors. The old reason
  was an APM install a strategy no longer runs.
- **The code-style summary in `AGENTS.md` matches the Bloom Code instruction**: one item per line
  from three items, or from two on a line over the length limit, and the error message goes in
  `message`, not `msg`. It names `bloom-code-lint`, with `--max-line-length 100`, as the check.
- **`apm.yml`'s comment names one package** for every KaxaNuk skill, installed once for the user
  with `apm install -g KaxaNuk/KaxaNuk-Researcher --target <agent>`.
- **`SETUP.md` step 4 gives the install command with `--target claude`**, your assistant in place
  of `claude`, as `apm.yml` and the researcher package's `SETUP.md` do; it gave it bare.
- **`pyproject.toml` asks for `kaxanuk-data-curator>=0.50.0`**, the first version whose `main()`
  takes `data_block_providers`, which `Data/curator.py` passes. `uv.lock` already held 0.50.0; only
  the project's version and that floor moved in it.
- **`Universe/universe.ipynb` lists the eight checks it writes to `Data_Issues.csv`** instead of
  saying four, and says why internal gaps and identity conflict are not written.
- **`AGENTS.md`, `RESULTS.md` and `Paper_Trading/BITACORA.md` say "this example"** instead of the
  retired `example` branch. The example is a folder of the researcher package, and a strategy of
  your own starts with `init-strategy`.

### Fixed

- **Experiment 1 runs to the end without the licensed engines**: sections 4 to 6 report and skip,
  as the section contract says, instead of raising `ModuleNotFoundError`. Step 6 no longer imports
  the attribution library after printing that it was skipped, and the `as library` alias is gone.
- **`Experiments/portfolio_construction.py`: every sizing method but `equal_weight` failed.**
  `weigh()` now calls `kaxanuk.portfolio_construction.sizing.build_allocator(name=..., returns=...)`
  on a pyarrow table, allocates a `UniverseSnapshot` and reads
  `Weights.from_allocated(...).as_mapping()`. The rule cell hands `build_weights` the returns before
  the window too, so a returns-based method has history on the first rebalance. It passes no
  configuration and always a history, so the library still refuses the methods whose configuration
  has a required field: `mean_variance`, `constrained_mean_variance`, `black_litterman`, and the
  snapshot methods `feature_weighting` and `kn_index`.
- **`Universe/universe.ipynb` fetches profiles from FMP's `/stable/profile`**, one identifier per
  request, because the legacy `/api/v3/profile` refuses keys opened after 2025-08-31. The master's
  `exchange` column reads the stable field `exchange`.
- **`Data/curator.py` no longer ends in a `FileNotFoundError`** after every price has downloaded
  when the hand-supplied KN600 returns are absent: it stages the index only when the file is there,
  and says so when it is not. Its docstring no longer claims steps 1 to 5 run without the index.
- **`AGENTS.md` no longer says to delete the seed after `init-example`.** The template ships it
  header-only, so `init-example Universe` and `init-example Bibliotheca` are refused; bring
  `Universe/universe.ipynb` by its path. The `main` row of the branch table is now simply the
  strategy's finished work.
- **Experiment 1's section 6 marks its own figures.** The 45.5 of 159.5 idiosyncratic points and
  the book's four choices sit between example markers, so the notebook `experiment-lifecycle`
  ships for a new experiment no longer opens section 6 with this strategy's results.
- **`OBJECTIVE.md` no longer says to start a strategy of your own by deleting the example's lines**,
  which would delete every heading with them; a strategy of your own starts with `init-strategy`.
- **`Bibliotheca/BIBLIOGRAPHY.md` lists the leads `OBJECTIVE.md` names.** Brock, Lakonishok &
  LeBaron (1992), Amihud (2002), Lee & Swaminathan (2000), Korajczyk & Sadka (2004), Grinold &
  Kahn's chapters 13, 14 and 16, and Shu, Yu & Mulvey (2024) were named for claims 1, 3 and 4 and
  for what is not claimed, yet had no row, though `AGENTS.md` says a person adds the leads there
  and `read` and `blueprint` look for them there. Each is now in Part 1, with *No note yet*.
- **`RESULTS.md` gives the point-in-time window as 9.4 years**, as `FINDINGS_1.md` does, where it
  said 9.74; 2017-01-03 to 2026-06-01 is 3,436 days. No result changes.
- **`FINDINGS_1.md` gives the long window as 23.8 years**, as `RESULTS.md` does: 2002-07-30 to
  2026-06-01. It said 24.7. The journal entry of 2026-09-20 keeps its figure, and a new entry
  records the correction.
- **Prediction 1's verdict in `FINDINGS_1.md` reads *Falsified***, because its falsifier named the
  index alone; the filter-off control's 22.91% moves to *What it changed* as a new observation, as
  the challenge of 2026-09-20 asked. The tally and every number are unchanged.
- **The README calls the signal an uptrend, not *positive momentum*.** `OBJECTIVE.md` rules
  momentum out: the filter compares a stock with its own past, which is trend following, where
  momentum is relative.
- **"Less volatily", not a word, is gone** from claim 1's status in `OBJECTIVE.md` and from
  *The uncomfortable one* in `RESULTS.md`: both now say "with less volatility". No number changes.
- **The three notebooks are stored in nbformat's own form**: `universe.ipynb` and
  `analyzer.ipynb` declared nbformat 4.5 without the cell ids it requires, and most cells kept
  their source as one string, so the strip `experiment-lifecycle` prescribes rewrote all three
  and warned that a missing id will become an error. Each cell now has an id and its source as a
  list of lines, and stripping a notebook with no outputs changes nothing.

### Removed

- **`SETUP.md`'s wrapper-folder check and its paragraph**, since a strategy installs nothing. It
  lists only `.venv/`, `Config/.env` and per-machine assistant files as ignored, and `AGENTS.md` no
  longer points at the removed text.

## 0.8.1 (2026-09-21)

**PATCH** — one note's file name is shorter, so the example installs on Windows from a deep home
folder. No result changes.

**What to do differently:** nothing.

### Changed

- **`Bibliotheca/Papers/Sullivan_Timmermann_White_1999_Data_Snooping.md`** was the paper's full
  title, a 130-character path that took the installed copy past Windows' 260-character limit on a
  home folder more than about 60 characters deep: `apm install -g` failed with *checkout failed*.
  The note is unchanged; every link to it, and the log line that wrote it, name the new file.

## 0.8.0 (2026-09-21)

**MINOR** — the template and the worked example now ship inside the KaxaNuk Researcher,
`KaxaNuk/KaxaNuk-Researcher`, and a strategy is made with `init-strategy`. No result changes.

**What to do differently:** install the KaxaNuk skills once for your user —
`apm install -g KaxaNuk/KaxaNuk-Researcher` —
then start a strategy with `init-strategy <name>`, and bring a file of the example across with
`init-example <path>`, never with `git fetch`.

### Changed

- **The template and the example moved into the researcher package.**
  `KaxaNuk/KaxaNuk-Strategy-Template`, with its `main` and `example` branches, and
  `KaxaNuk/KaxaNuk-Researcher-Template` are retired. What `main` held is now
  `templates/strategy/` in `KaxaNuk/KaxaNuk-Researcher`, what `example` held is
  `examples/liquid-golden-cross/`, and the researcher's home is
  `templates/researcher/`. One repository now versions the process, the worked strategy
  and the skills that read them, so the three cannot drift apart between releases.
- **A strategy is made by `init-strategy`, not by *Use this template* or a clone.** The skill copies
  the template by a script, byte for byte, makes the folder a git repository and commits it once;
  publishing it to GitHub is the owner's, one repository per strategy. Step 1 of `SETUP.md` now says
  only that, and keeps the short-path warning for Windows and the git-identity fallback; the button,
  `gh repo create --template` and the plain clone with a fresh history are gone, with the two
  failure notes they needed.
- **A file of the example comes with `init-example <path>`**, which copies one path of the example
  into the strategy and never overwrites a file already there; the marked lines are deleted
  afterwards, as before. It replaces the README's `git fetch ... example` and `FETCH_HEAD` block.
  `init-example` with no path copies the whole example into a folder of its own. The README's branch
  table becomes a description of the two folders, and `AGENTS.md` says where they live instead of
  naming the two branches.
- **The skills are installed once for the user**, with `apm install -g`, and `apm update -g` keeps
  every strategy current; a strategy installs nothing, and step 4 of `SETUP.md` no longer keeps an
  in-repository install for a user with no researcher. A researcher is made once with
  `init-researcher`. Every link to the retired repositories — in the README, `SETUP.md`, `AGENTS.md`
  and `Bibliotheca/BIBLIOGRAPHY.md` — now points at the package on GitHub.
- **This folder is no longer called the `example` branch.** The README and `OBJECTIVE.md` call it
  the worked example, and the README drops the walk-through by `git log --reverse main..example`:
  `init-example` makes a new repository with one first commit, so there is no branch history to
  walk. `SETUP.md` says `init-example` makes the folder.
- **`uv.lock`** is locked again for the new version; only the project's own version line moved.

## 0.7.15 (2026-09-21)

**PATCH** — the agent skills come with the researcher, and this repository installs none. No result
changes.

**What to do differently:** do not run `apm install` here — invite your researcher, and the skills
come with it.

### Changed

- **The agent skills come with the researcher, and this repository installs none.** `apm.yml` no
  longer names the `kaxanuk` package, `apm-cli` leaves the `dev` dependency group, and step 4 of
  `SETUP.md` says where the skills come from instead of installing them. A researcher made from
  `KaxaNuk/KaxaNuk-Researcher-Template` installs every KaxaNuk package once, in its own home, and
  brings them into any strategy it is invited to — so a new version reaches every strategy with one
  `apm update` in that home, and a strategy never goes stale. `AGENTS.md` and the README say the
  same. For a user with no researcher, step 4 keeps the one command that installs them here.
- **`uv.lock`** is locked again without `apm-cli`; nothing the pipeline imports moved.

## 0.7.14 (2026-09-21)

**PATCH** — the process is called the **KaxaNuk Strategy Template**, the same as the repository. No
result changes.

**What to do differently:** say *KaxaNuk Strategy Template* where you said *KN Research Process*.

### Changed

- **One name, not two.** 0.7.9 kept the **KN Research Process** as the name of the process and gave
  the repository a different one, so a reader met two names for the same thing. The README,
  `SETUP.md`, `apm.yml`, `Bibliotheca/BIBLIOGRAPHY.md`, `Paper_Trading/BITACORA.md` and
  `Paper_Trading/daily_update.py` now say *KaxaNuk Strategy Template*, and so does the first commit
  `SETUP.md` has a new strategy make. The entries below keep the old name where they record what
  happened at the time.

### Removed

- **A comment in `Data/curator.py` about the curator's deprecated `market_data_provider`
  argument.** Nothing here passes it, so the comment described an interface this file never used.

## 0.7.13 (2026-09-21)

**PATCH** — the researcher's repository is `KaxaNuk/KaxaNuk-Researcher-Template`. No result
changes.

**What to do differently:** nothing. GitHub redirects the old name.

### Changed

- **The researcher's repository was renamed `KaxaNuk/KaxaNuk-Researcher-Template`**, and `AGENTS.md`
  and `Bibliotheca/BIBLIOGRAPHY.md` link it by that name. Like this repository, it is a template:
  what reads the notes and drafts the claims is a researcher made from it, which is how both files
  now put it.

## 0.7.12 (2026-09-21)

**PATCH** — the blueprint and the findings keep the template's headings outside the example
markers again, so the references in `experiment-lifecycle` regenerate without losing a section. No
result changes.

**What to do differently:** nothing.

### Fixed

- **Ten of the template's headings sat inside the worked strategy's example markers** on `example`:
  *Thesis*, *Rules* and *What this experiment should show* in `BLUEPRINT_1.md`, and seven sections of
  `FINDINGS_1.md`, whose *Status* had also lost its guidance. Regenerating the references in
  `experiment-lifecycle` stripped them as strategy content, 82 lines in all, so two references could
  not be regenerated. Each heading is back outside the markers with the template's guidance beneath
  it, and the strategy's own text follows in its own block, as *Key risks* always had it. The change
  only adds lines; not one line of the strategy's text changed, and stripping the fixed files
  reproduces the current references exactly.

- **`BLUEPRINT_1.md` changed after its test, and only in its template text.** The rule that a
  blueprint never changes protects the hypothesis; the hypothesis sits inside the markers and is
  byte for byte what it was. `JOURNAL_1.md` records the change and the check.
## 0.7.11 (2026-09-21)

**PATCH** — the Python project is named `kn-strategy-template`, like the repository and its `apm.yml`.
No result changes.

**What to do differently:** nothing. The project is virtual — `uv` never installs it as a package —
so the rename moves no file in `.venv`.

### Fixed

- **`pyproject.toml` still named the project `kn-research-process`** after the repository became
  `KaxaNuk-Strategy-Template` and `apm.yml` became `kn-strategy-template`. It now matches both.
  Found by `tools/check_release.py` in KaxaNuk-Agent-Skills, which treats the old name as retired
  everywhere but the changelog and the journals.
- **`uv.lock` recorded the project at 0.7.8** while `pyproject.toml` had moved to 0.7.10: 0.7.9 and
  0.7.10 bumped the version without locking again, so a fresh `uv sync` would have rewritten the
  lock and left a new clone with a modified file. Locked again here, name and version together.


## 0.7.10 (2026-09-20)

**PATCH** — the notebooks name a kernel that exists in the environment `SETUP.md` builds. No result
changes: the whole pipeline was re-run and every published number reproduced.

**What to do differently:** nothing. If you opened a notebook and were asked to pick a kernel, that
is what this fixes.

### Fixed

- **All three notebooks declared a kernel named `kn-research-process`.** Nothing in the template
  registers that name and `SETUP.md` never mentions it, so a new clone could not execute them: on
  the machine they came from it resolved to a *different repository's* virtual environment, which
  has no Backtest Engine, and the experiment notebook died at
  `import kaxanuk.backtest_engine.entities`. They now name `python3`, which this repository's own
  `.venv` registers.
- **The notebooks recorded Python 3.14.5**, which `pyproject.toml` forbids — it requires
  `>=3.12,<3.14`. They now record 3.13.15, the interpreter the environment actually builds. Every
  figure published before today was produced on that unsupported 3.14 environment.
- **`pyproject.toml` kept version 0.7.8 while `apm.yml` moved to 0.7.9.** The two have always moved
  together; 0.7.9 bumped only one of them. Both read 0.7.10 here.
- The experiment notebook's section-contract table lists **6 · Counterfactuals** and renumbers
  Verdict to 7, matching the sections the notebook has had since the counterfactual arms were added.

### Changed

- **The pipeline was re-run end to end on the supported interpreter**, reusing the downloaded
  curator data: universe notebook, refinery, analyzer, experiment. `Security_Master.csv` and
  `Data_Issues.csv` came back byte-identical, the refinery wrote the same 787 files over the same
  4,252,848 rows, all nine analyzer measurements matched, and all eleven weight files were identical
  byte for byte. Every engine figure reproduced: the rule 17.85% / 0.861 / −30.5%, the filter-off
  control 18.62% / 0.813 / −39.8%, the long window 10.29% / 0.514 / −60.7%, the index 14.71% /
  0.774 / −33.8%, the equalised control 18.97% / 0.831, and idiosyncratic points 45.5 / 40.5 with
  the random books spanning −17.6 to 25.2. **Nothing in `RESULTS.md` moved.**

## 0.7.9 (2026-09-20)

**PATCH** — the repository is now `KaxaNuk/KaxaNuk-Strategy-Template` and the skills come from
`KaxaNuk/KaxaNuk-Agent-Skills`. No result changes.

**What to do differently:** nothing, if you already cloned. GitHub redirects both old paths, so an
existing repository keeps installing and `git pull` keeps working; run
`git remote set-url origin https://github.com/KaxaNuk/KaxaNuk-Strategy-Template.git` when you want
the remote to say what it is. New pins should use the new paths.

### Changed

- **`apm.yml` fetches from `KaxaNuk/KaxaNuk-Agent-Skills/kaxanuk`.** "APM" read as Application
  Performance Monitoring and named the delivery mechanism rather than what the packages hold. The
  package names stay `kaxanuk-apm-*` — they are APM packages, and every published tag embeds that
  name. The project's own name here is `kn-strategy-template`.
- **The README, `AGENTS.md` and `SETUP.md` name both new repositories**, in prose, in the install
  instruction and in the `git fetch` that copies a file across from `example`. The old name said
  *process* where the artifact is a repository you copy, and collided with `KaxaNuk-Researcher`.
  The **KN Research Process** keeps its name: the process is not the repository.
- **The branch table names this branch's strategy `liquid-golden-cross`.** It still read
  `liquid-momentum`, the strategy `example` carried before it was restarted. The entries below and
  `JOURNAL_1.md` keep that name where they are recording what happened at the time.

## 0.7.8 (2026-09-17)

**PATCH** — step 6 compares the book with the whole benchmark, not the part of it the book holds. No
result changes.

**What to do differently:** before handing the book to the attribution library, add every benchmark
constituent it does not hold at zero weight, each with a price series. The engine's daily weights
name only what was held.

### Changed

* **`Experiments/attribution_analysis.py`, on `example`, widens the book to the
  benchmark.** The library prices only the securities named in the book's weight file, and the first
  cut computes the benchmark's return from those prices alone; the index's own return series never
  enters it. A book of 8 names inside a 788-name index was compared with the 7% of the index it
  overlapped: the benchmark return came out at 6% of the index's, and alpha about five times too
  large, most of the excess filed under interaction. With the other 780 names added at zero weight the
  benchmark return reached 98.9% of the index's, the rest being the held names' own returns. The run is
  recorded in `JOURNAL_1.md` on that branch.
* **The same module drops the engine's benchmark column** from the daily weights, which the engine
  returns at zero, and keeps the cash position.
* **The README's four shared modules** say that `attribution_analysis.py` widens the book to every
  benchmark constituent.

## 0.7.7 (2026-09-17)

**PATCH** — step 6's module says what the attribution library's loader actually accepts, checked by
running it against a strategy's own files. No result changes.

**What to do differently:** give every weight file a first header of `Ticker` or `date_column` —
nothing else loads, whatever the library's documentation says — and check that the four reserved
factor names are in lower case before an attribution run.

### Changed

* **`Experiments/attribution_analysis.py`, on `example`, names the one cell that
  decides whether a file loads**: the first header. `Ticker` means securities down and dates across,
  `date_column` means dates down and securities across, and any other name — `date`, `m_date`,
  whatever a provider used — raises before a number is read. The module said the hand-supplied files
  were both horizontal, and that a wrong orientation produced a transposed number rather than an
  error. Both were wrong.
* **The same module says what the factor directory has to look like**: every entry in it is read as a
  factor file, the factor's name is the file name up to the first dot, the date column comes first and
  its header may be empty, and the four reserved names — `f_market`, `f_total_factor_returns`,
  `f_total_excess_returns`, `f_idyo_returns` — are matched exactly and in lower case, so a file
  capitalised differently is attributed as an ordinary factor.
* **`JOURNAL_1.md` on that branch records the run** that settled all of it: both engines installed, a
  synthetic book priced, and the attribution run over a strategy's real benchmark and factor files. It
  also records a backtest that reported success while valuing 522 of 1305 days, because a book summing
  to one with no cash reserve cannot pay commission at a rebalance.

## 0.7.6 (2026-09-17)

**PATCH** — the tools are three jobs with a choice for each, not a fixed list. No result changes.

**What to do differently:** nothing, if you use GitHub Desktop, PyCharm and Claude. Otherwise pick
one tool per job — the git command line for GitHub Desktop, VS Code for PyCharm, Codex for Claude —
and follow the same steps.

### Changed

* **`README.md`'s *The tools* is three jobs, one tool for each, either option doing the job**:
  versions, in GitHub Desktop or the git command line; code and debug, in Claude or Codex; read and
  run, in PyCharm or VS Code, whose free editions are enough. It named GitHub Desktop and PyCharm as
  though there were no alternative. The APM packages leave the table for the paragraph below it:
  they come on top of whichever assistant is picked, not as a pick of their own.
* **`SETUP.md` offers the same choice wherever it names a tool**: step 1 clones with GitHub Desktop or
  `git clone`; *What "done" looks like* publishes a plain clone from GitHub Desktop or from the git
  command line, and opens the folder in PyCharm or VS Code and in Claude or Codex.

## 0.7.5 (2026-09-17)

**PATCH** — steps 4 and 6 describe the libraries as they now are: Portfolio Construction exists and is
called inside step 4's one signature, and Attribution Analysis, whose documentation is now public,
reads a daily book. No result changes.

**What to do differently:** in step 6, hand the attribution library the book's daily weights from the
backtest, never `Portfolio/portfolio_weights.csv`. In step 4, build a Portfolio Construction method one
rebalance date at a time, on a history cut before that date. If you trimmed `apm.yml` to some
packages, `universe` and `portfolio-construction` can now be named.

### Changed

* **`portfolio_construction.py` calls the Portfolio Construction library inside its one signature**
  where the library is installed, instead of being the seam a future library would replace. The
  library is KaxaNuk's own and not distributed publicly yet, so it stays out of `pyproject.toml` like
  the engines, installed by hand and imported behind a guard. Its methods that estimate from a returns
  history use whatever history they are built with, so the module builds one per rebalance date on
  the history before it.
* **The attribution reads the book's daily weights.** Attribution Analysis 0.2.0 rejects a weight file
  that is not a daily series once it spans a year, so `backtest_engine.py` reads the book's daily
  weights back from the engine and `attribution_analysis.py` shapes them. The README's four shared
  modules say so; on `example` the module descriptions and the notebook's
  handoff table do too.
* **`SETUP.md` step 4 and `apm.yml` list the published packages** — `common`, `universe`,
  `data-curator`, `portfolio-construction`, `backtest-engine`, `attribution-analysis` and
  `investment-lab` — in the order of the steps they serve.

## 0.7.4 (2026-09-17)

**PATCH** — the template reads in the order a newcomer needs it, and a repository made from it says
what comes after setup and stays true about itself. No result changes.

**What to do differently:** after setup, start at `OBJECTIVE.md`; the order after it is *Starting
your own strategy* in the template's README, which now follows *Setup* directly. In step 5, put the
README's status line in `AGENTS.md`'s banner and rename `name` and `author` in `apm.yml`, and commit
all four files together.

### Changed

* **`README.md` puts the newcomer's path first**: what the template is for and what it needs, the
  install line, the eight steps, *The tools*, *Setup*, *Starting your own strategy* and *The
  documents*; *What is in here*, *The six Lab modules* and *The conventions worth keeping* follow as
  reference for when the work reaches the universe and the data. The paragraph on `main` and
  `example` moves below the install line, and the first lines say that building the data needs a
  provider key and that steps 5 and 6 need the licensed engines.
* **The order of work says what it is before it starts.** Its eight items are named as the order of
  work, not the eight steps; the files it names are said to be on `example` before the list, not
  after; item 3 requires delisted names in the seed; item 5 is headed by the benchmark choice it
  asks for first.
* **`AGENTS.md` holds inside a strategy repository.** It pointed at a local `README.md` that step 5
  replaces, said `main` holds no strategy, and put issues on KaxaNuk's project. It now points at the
  template's README, says what `main` and `example` are on the template and in a strategy
  repository, states that `main` is never merged into `example`, and marks example content only on
  `example`. Its banner no longer says every file is a description on a branch whose folders hold
  `.gitkeep`.
* **Setup step 5 hands over a next step.** The strategy README it writes links to the order of work
  and names `OBJECTIVE.md` as next, and so does the agent's hand-over; step 5 also carries the
  status line into `AGENTS.md` and the owner's name into `apm.yml`, whose comment asking for that
  is gone.
* **`SETUP.md` is shorter before its first command**: the folder rule is two paragraphs, the skills
  step says what APM and a skill are, the keys step names each key, and the paragraph for somebody
  who needs no research process is one sentence.
* **`OBJECTIVE.md` marks all its guidance in italics** and has the fifth part its closing table
  lists, *Where each half is named*, which is where the `c_*` and `r_*` columns are now asked for.
* **`RESULTS.md`'s comparison rule says what to compare**: a winner's Sharpe with its own
  experiment's control, and `vs control` across experiments.
* **The six Lab modules are numbered by the step they belong to**, 3 to 6, not 1 to 6 beside a step
  table where step 1 is the Bibliotheca, and the licensed engines point at the skills that install
  them.

### Fixed

* **The two-command lines in `SETUP.md` step 5 and `README.md`'s fetch are split in two**: `&&` is a
  parse error in Windows PowerShell 5.1, which step 1 names as the shell the Claude app and Codex
  drive on Windows.
* **`SETUP.md` says `uv` uses Python 3.12 if it finds it**, and downloads 3.13 only if neither is
  there; `pyproject.toml` allows both.
* **`AGENTS.md` puts the benchmark in `JOURNAL_1.md` once `BRAINSTORMING_1.md` has chosen it**, and
  lets that entry come before `BLUEPRINT_1.md`, which is otherwise still the first commit on an
  experiment's branch; it named the journal as where the benchmark is chosen.
* **`RESULTS.md` says *Known limitations* is not empty**, and `.gitignore` and `AGENTS.md` point at
  files a strategy repository still has.

## 0.7.3 (2026-09-16)

**PATCH** — the public `example` is the worked strategy, and the documents stop contradicting each
other about it and about the order of work. No result changes.

**What to do differently:** read `example` as `liquid-momentum` worked through the process, its own
lines between example markers; copy the shape from it and delete what is the strategy's — the
fenced content, the seed, the notes under `Bibliotheca/Papers/` and the entries in
`Bibliotheca/LOG.md`. Set nothing up twice: a repository with `.venv/` is set up, with or without
`apm_modules/`.

### Changed

* **`example` holds `liquid-momentum`.** 0.7.0 said it held no strategy; it now carries one, worked
  through the process step by step, public beside `main`, so the shape can be read rather than
  imagined. `README.md`, `SETUP.md` and `AGENTS.md` describe the branch that way, name the example
  markers, and say what to strip when a file is brought across.
* **`OBJECTIVE.md`'s header says before any paper is read**, where it said before the backtest —
  the later deadline let the reading come before the claims — and its guidance names what a claim's
  evidence is at each step: the question that would settle it, then the notes, then `RESULTS.md`.
* **The researcher paragraph in `README.md` follows the order of work**: the claims are drafted from
  the owner's words before any paper, and their evidence rewritten from the notes afterwards. It
  said the claims were drafted from the notes.
* **The eight steps say which numbering they use.** Item 4 runs *process* steps 2 and 3 — Universe
  and Data — and item 5 cites a note from the reading in item 2, so the two numberings no longer
  read as one. Item 5 names the one entry that comes early: `BRAINSTORMING_1.md`'s benchmark
  choice, before `BLUEPRINT_1.md`, because Experiment 1 is the benchmark.
* **`experiment-lifecycle` is named with the package that carries it**, `investment-lab`, in
  `README.md` and `SETUP.md`; a reader who trims `kaxanuk` to a subset can now keep it. `apm.yml`,
  `README.md` and `SETUP.md` promise one skill package per Lab library *as each is written* — three
  of the six libraries have one today.
* **A column with a setting an experiment will sweep lives in the Refinery**, whether it is fitted
  or a window. `README.md`'s prefix table and its rule admitted only a rank, a breadth reading or a
  fitted model to `r_*`, and sent every other per-security quantity to the Curator — where a sweep
  costs a download.
* **Graduation criterion 3 demands what the process produces**: the trial count published beside
  the winner, and the sign-off saying whether the deflated figure was also computed. It demanded a
  deflated count no stage computes, and `FINDINGS_N.md` gains the section `RESULTS.md` compiles the
  count from. The step descriptions on `example` stop contradicting the README: the universe
  notebook talks to the provider too, a window to sweep lives in the Refinery, the null VWAP is one
  provider's habit rather than every provider's, `Universe/Charts/` is gone, and step 8 is funding,
  wherever the desk is.
* `example` takes the same text, and its notes, notebooks and journal stop
  saying the branch is private or that a filled-in copy is elsewhere.

### Fixed

* **The first-run test in `AGENTS.md` is `.venv/` alone.** It also named `apm_modules/`, so a
  repository whose owner answered *no* to the skills — which `SETUP.md` calls a working repository —
  was reported as not set up in every session. The same block says *the commands in it*, not *four
  commands*: the count depends on whether the clone and the README step are included.
* **`.gitignore` names `CLAUDE.local.md`** — the per-machine fallback KaxaNuk-Researcher's
  invitation describes, which holds an absolute path to one machine — and the folders the other
  APM targets write: `.gemini/`, `.opencode/`, `.windsurf/`. `SETUP.md` invites those targets and
  then says anything else in `git status` is a mistake.
* **`SETUP.md`'s example for a project that is not built from this template** no longer prefixes
  `apm` with `uv run`, which only works inside this repository's `.venv/`.
* **`SETUP.md`'s last paragraph points at the template's README** for the order of work, since
  step 5 replaces the strategy's README with one that links there.
* **`apm.yml` and `pyproject.toml` carry the changelog's number.** 0.7.1 and 0.7.2 left them at
  0.7.0.

---

## 0.7.2 (2026-09-16)

**PATCH** — the order a strategy is built in starts with the objective, before any paper. No result
changes.

**What to do differently:** start a strategy with `OBJECTIVE.md` — the idea and its claims — and
read for those claims before choosing the investable universe, which is now step 3 of the order
rather than the first thing done.

### Changed

* **`README.md`'s *Starting your own strategy* is the order of work, in eight steps.** The objective
  before any paper; the objective fine-tuned by reading for each claim, the sources that argue
  against it included; the investable universe; the data, in the order the Data stage already gave;
  `BLUEPRINT_1.md` before the rule, every prediction citing a note or an analyzer measurement; the
  broad reading and brainstorming; the cycle of portfolio construction, backtest and attribution
  until it is finished; and every finished cycle into `RESULTS.md`, kept or rejected. It listed the
  universe first, but the claims decide what the universe has to contain, and reading with no claim
  to read for has no stopping condition.
* **Step 1 of the eight is the idea and its claims first, then the literature that argues with
  them**, where it read *a literature review with a thesis at the end of it* — the order this change
  reverses. Its row names `OBJECTIVE.md` beside `Bibliotheca/`.
* **`SETUP.md`'s last paragraph** names the objective as the first thing to do, where it named the
  universe.
* `example` takes the same text, and its `BIBLIOGRAPHY.md` plain-words line
  to match.

---

## 0.7.1 (2026-09-11)

**PATCH** — what a `Bibliotheca/` holds, now that a researcher writes its notes a chapter at a
time. No result changes.

**What to do differently:** keep the PDFs beside their notes and let git ignore them, along with
`Bibliotheca/Extracts/`, where the researcher's script leaves a book's chapters as text. A book is
a folder — `Books/Author_Year_Title/INDEX.md` for the chapter table, one file per chapter read —
and `Bibliotheca/Knowledge/` is gone: the notes beside the sources are the library, `BIBLIOGRAPHY.md`
is its index and `Bibliotheca/LOG.md` its record. The files themselves are on
`example`.

### Added

* **`AGENTS.md` says who writes a note:** a person, or a researcher with `read`, after a plan and a
  go; whoever writes a note adds its row to `BIBLIOGRAPHY.md`. It was the one step-1 document the
  table did not name.
* **`.gitignore` keeps the PDFs and the extracts out**, as step 1's own section. Licensed material
  is not redistributed by a clone, and the extracts regenerate with one command.

### Changed

* **`README.md`'s `Bibliotheca/` row describes the folder as it is now** — notes beside their PDFs,
  a book as a folder of chapters, `LOG.md` — and its researcher section says what the companion
  actually does here rather than that it is being built. `KaxaNuk/KaxaNuk-Researcher` 0.3.0 is the
  version that writes these notes.

---

## 0.7.0 (2026-09-10)

**MINOR** — `main` is the shape and nothing else: six folders and the documents at the root. Every
file the process expects inside those folders moved to the public `example` branch, unchanged.

**What to do differently:** `main` no longer ships `Experiment_1`, the drivers, the notebooks or the
shared modules. Bring a file across from `example` when you need it — `README.md` gives the one
command — or let the `experiment-lifecycle` skill scaffold an experiment.

### Removed

* **Everything below the six folders**, moved to `example` as it was: `Bibliotheca/`'s index,
  `Knowledge/`, `Notes/`, `Papers/` and `Books/`; `Universe/`'s seed and notebook; `Data/`'s three
  drivers, the two `custom_calculations.py` and the data directories; `Experiments/`' four shared
  modules and `Experiment_1/`; `Paper_Trading/`'s gate and scripts. `Config/.env.template` stays,
  because setup needs it. A reader opening `main` now sees the shape in one screen, and a reader
  who wants the files finds all of them on one branch rather than half here and half there.

### Changed

* **`README.md`'s *What is in here* is the one place the folder contents are written down** — a
  table per folder saying which step owns it, what belongs in it and what is committed. The old
  tree listed files that are no longer on `main`.
* **`README.md`'s Setup section is a pointer to `SETUP.md`**, with no commands of its own. Two
  copies of the same commands had already started to differ.
* **`example` is public, in this repository, beside `main`.** `README.md`, `SETUP.md` and
  `AGENTS.md` said it was private; it holds no strategy, so there was nothing to keep private. A
  strategy worked end to end still stays in KaxaNuk's own repositories.

---

## 0.6.0 (2026-09-06)

**MINOR** — one prompt sets a strategy up from nothing. *Please help install
`https://github.com/KaxaNuk/KaxaNuk-Research-Process`* is now enough for an agent with no other
context, and the manifest names one package so the template cannot go stale.

**What to do differently:** the skills command is `uv run apm install --target claude` (or `codex`),
not a bare `apm install`, and there is nothing to install by hand before `uv sync` — not even Python.

### Changed

* **`SETUP.md` was run as an agent would run it, and rewritten where it broke.** Handed only the
  URL, an agent does not know the strategy's name — it now asks, and decides the root from what the
  current folder holds. `apm` lives inside `.venv/` and is not on a fresh terminal's path, so every
  skills command is `uv run apm …`. The fresh-history sequence is given in PowerShell as well as
  bash, because that is what the Claude app and Codex drive on Windows. A first commit on a machine
  that has never committed fails for want of a git identity; the agent asks for one and sets it for
  the repository only. Prerequisites shrink to git and uv, each with its one-line installer — `uv`
  downloads Python 3.13 itself. A hand-over paragraph says what the agent reports and where it stops.
* **`apm.yml` names one package, `kaxanuk`.** It is every KaxaNuk package under one name, and it
  resolves transitively — verified. The template listed four packages by hand and was already stale:
  `attribution-analysis` had shipped and a fresh install missed it. Replace the line with the packages
  you want if you want fewer.
* **The skills question has an answer when the request already gave one.** *Install it and the
  skills* is consent and the agent runs it; a bare *set this up* still gets asked. `AGENTS.md` and
  `SETUP.md` say the same rule.
* **A plain clone ends with no remote, and `SETUP.md` now says so** — GitHub Desktop, *Add existing
  repository*, *Publish*. The user's to do, not the agent's.

---

## 0.5.1 (2026-09-06)

**PATCH** — documentation. `SETUP.md` says what a finished setup actually leaves behind.

**What to do differently:** commit `uv.lock`. `uv sync` writes it, the template ships without one on
purpose, and your repository keeps it — it pins the versions a result came from.

### Fixed

* **The "what done looks like" check said `git status` would be clean; a real run leaves `uv.lock`
  untracked.** Running the file end to end from a fresh clone is what caught it, which is the reason
  the check is in `SETUP.md` at all.

---

## 0.5.0 (2026-09-06)

**MINOR** — the repository now carries its own setup instructions and declares which agent skills it
wants. No result changes; nothing in the pipeline moved.

**What to do differently:** set a strategy up from [`SETUP.md`](SETUP.md) rather than from a prompt
held in another repository. `apm install` needs no arguments, and it is a question you get asked
rather than a step you have to run.

### Added

* **`SETUP.md` — the whole of setup in one file**, written so an agent can follow it end to end:
  getting the repository (the template button, `gh repo create`, or a plain clone with a fresh
  history), the one-folder rule, `uv sync`, the credential copy, and — last, and as a question — the
  agent skills. It replaces the `start-a-strategy` prompt that lived in `KaxaNuk/KaxaNuk-APM`, on the
  rule that **the instruction to install a thing belongs with that thing**. A bootstrap you can only
  reach after installing the tool it bootstraps is a bootstrap that gets pasted from a URL.
* **`apm.yml`, committed.** It names the KaxaNuk packages this repository wants, so `apm install`
  takes no arguments and nobody types a package name. It carries no `targets` key on purpose: the
  template serves Claude Code, the Claude app, Codex and Cursor alike, so the target is set on the
  machine or passed per command.

### Changed

* **`.gitignore` stops ignoring `apm.yml`**, and says why: the manifest is a declaration, like
  `pyproject.toml`, while everything APM downloads and writes — `apm_modules/`, `.claude/`,
  `apm.lock.yaml` — is build output, ignored the way `.venv/` is. **A clean `git status` after a full
  setup is the test** that the split is right.
* **`AGENTS.md` opens with a *First run* block**, before anything about branches. An agent that finds
  no `.venv/` or `apm_modules/` offers `SETUP.md` instead of starting work in a repository that has
  not been set up, and the two rules it must not get wrong are restated there: never print a value
  from `Config/.env`, and ask before installing the skills.
* **`README.md`'s Setup section is three commands and a link.** One source, so the two cannot drift.
* **Python is `>=3.12,<3.14`, and 3.13 is the one to install.** The ceiling is the Backtest
  Engine's: it is documented for 3.12 or 3.13, and every performance figure here comes from that
  engine, so a version it cannot be installed beside is a version that cannot finish the pipeline.
  The Data Curator allows 3.12 to 3.14, which leaves 3.13 as the version that satisfies both. Ruff
  targets `py313` to match. Widen it when the engine supports 3.14.
* **`SETUP.md` says to clone somewhere short on Windows.** APM stages downloads several directories
  below the root, so a deep synced path fails part-way through with `WinError 3: The system cannot
  find the path specified`. The same install from a short path succeeds, which is why the message is
  worth naming: it reads like a missing file, not like a path-length limit.

---

## 0.4.1 (2026-09-05)

**PATCH** — documentation. `README.md` now states the setup order and the layout it has to produce.
No result and no file in the pipeline changed.

**What to do differently:** set a strategy up in **one** folder. The clone is the root; `uv sync`,
`apm init` and `apm install` all run in it, and the agent tooling lands beside the process folders
rather than in a directory above them.

### Changed

* **`README.md` gains an ordered Setup** — the repository named after the strategy, cloned, then
  `uv sync`, `apm init -y --target claude`, `apm install KaxaNuk/KaxaNuk-APM/common`, then the
  credential file. The order is a dependency: `apm-cli` arrives with the `dev` group, so the
  environment has to exist before APM can be initialised.
* **The setup section shows the root it should produce**, and names the failure it is there to
  prevent: a wrapper folder holding the clone. Initialising APM in an empty wrapper writes a second
  `apm.yml`, a second `.claude/` and a `requirements-dev.txt` that only exists because the wrapper
  has no `pyproject.toml` — and Claude opened at the wrapper reads that empty setup and never sees
  the research tree.
* **"The tools" moved above "Setup"**, so the README reads install-once, then set-one-strategy-up,
  then start it. The APM paragraph says where the packages land rather than only how the CLI
  arrives.

---

## 0.4.0 (2026-09-04)

**MINOR** — `main` becomes a description-only template. **There is no code on it any more:** every
file is a short statement of what is expected in it.

**What to do differently:** nothing on `main` runs. Read it to learn the shape, fill it in with your
own idea, or read the `example` branch KaxaNuk keeps beside `main` for one strategy worked end to
end.

### Added

* **`LICENSE` — MIT**, the Data Curator's licence, so the template can be public, forked and
  contributed to without friction. `main` lives at `KaxaNuk/KaxaNuk-Research-Process`.
* **The tools, and a researcher beside the process.** `README.md` names the four tools — GitHub
  Desktop, PyCharm, Claude, and the APM packages through which Claude learns the six modules — and
  points at `KaxaNuk/KaxaNuk-Researcher`, a companion that reads a strategy's `Bibliotheca/` and
  drafts the hypothesis in each blueprint from it.
* **Attribution in two layers and a third pass.** `AGENTS.md` now says what each layer answers:
  Brinson-Fachler names the lever that moved, the factor model separates compensated tilts from
  idiosyncratic alpha, and Brinson-Fachler on the residual says whether the Sharpe survives once
  the factor turns. The notebook, the module and the gate say the same.

### Removed

* **All executable code.** The Curator and Refinery drivers, the four shared experiment modules,
  the two calculation modules and every notebook code cell are now docstrings and markdown. A template whose example code has to be
  deleted before you can start is a template that gets started by deleting things.
* **The nine Bibliotheca notes and the lockfile** — they belong to a filled-in repository, and they
  are on `example`.
* **The dev container** and its Docker build context. Setting the environment up is two commands,
  and a container that has to be rebuilt whenever the process changes is a second thing to maintain.

### Changed

* **Every remaining file describes what is expected in it**, in the same shape: what the stage is in
  plain words, what it produces, what it prevents, and the sections it owes. Learn the shape once.
* **`README.md` rewritten around the eight steps**, each with its plain-words sentence, its output
  and the failure it prevents, plus the six Lab modules mapped one per stage and the conventions
  worth keeping when two people share a tool.
* **`AGENTS.md` cut roughly in half.** The five ways a backtest lies are one table — the lie, what
  the process does, what it still does not do. Everything the README covers was removed rather than
  restated.
* **The source-note convention moved to `Bibliotheca/BIBLIOGRAPHY.md`**, next to the notes it
  governs. Its Part 0 keeps the lineage the process descends from, as provenance rather than notes.
* **`Universe/Investable_Universe.csv` requires only `main_identifier`** — the name the Data Curator
  asks a provider for. Every other column is yours, so an equity, ETF, FX, crypto or futures seed
  runs the same process.
* **`Config/.env.template` carries the Data Curator's provider keys**, not one.
* **Joined classification columns are prefixed `current_`**, not suffixed `_current`, so every column
  family is a prefix, and the prefix alone says which stage owns a column and whether it is
  point-in-time.
* **Bibliotheca notes carry their four fields as frontmatter**, so a tool can index what cites
  what, and **blueprint predictions cite a note or a measurement** — never nothing.

## 0.3.0 (2026-09-04)

**MINOR** — the template stops being US-equity-shaped, gains a fourth shared module, and splits into
two branches: `main` is the process with nothing in it, `example` is one strategy worked end to end.

**What to do differently:** the universe is now a CSV whose only required columns are `ticker` and
`name`, so the repository is multi-asset by default. Name your signal in two places —
`ELIGIBILITY_COLUMN` in `Data/analyzer.ipynb` and `SIGNAL_COLUMN` in the experiment notebook — and
the benchmark rule runs without being written.

### Added

* **`Experiments/portfolio_construction.py`** — step 4, behind one swappable signature: given the
  securities eligible today and a returns history already cut off before today, return weights
  summing to **at most** one. `equal_weight` and `inverse_volatility` ship; a minimum-variance
  optimiser, hierarchical risk parity, or a call into the KaxaNuk Portfolio Construction library are
  the same shape, so swapping one is one line in the rule cell.
* **`Experiments/attribution_analysis.py`** — step 6, split out of the engine so the two KaxaNuk
  libraries live in one module each. It owns the shaping of hand-supplied index data into the tables
  the library auto-detects, and reports which of its four inputs are missing before it tries. Getting
  that layout wrong makes the loader read the attribution transposed rather than fail, which is why
  the shaping is not left in a notebook.
* **A benchmark rule that works out of the box.** Section 2 of the experiment notebook holds
  everything the signal calls eligible, equally weighted, cash for the rest — event-driven, one day
  of lag. It runs as soon as `SIGNAL_COLUMN` is set, because a benchmark you have to write before you
  can measure anything is a benchmark that never gets written.
* **A run order that is stated in seven places.** `README.md` numbers the six commands, and every
  file in the pipeline says where it sits in that order in its first paragraph, so wherever you land
  you know what must have run before it.
* **The branching model, written down.** `main` (the template), `example` (one strategy, for reading)
  and `issues/<number>` cut from `main` and merged back into it — one per issue on the GitHub
  Project, opened before the branch because the issue is where the reasoning lives.
* **Example markers.** `# --- example: begin ---`, `<!-- example: begin -->` and
  `# EXAMPLE-ONLY CELL` mark any line that belongs to a worked example rather than to the process, so
  the two branches can be told apart by reading rather than by diffing.
* **A step-3 findings section in `RESULTS.md`.** Notebook outputs are stripped before committing, so
  a measurement that lived only in a cell output did not survive the commit. Findings from the Data
  stage now have a durable home.

### Changed

* **`Universe/Investable_Universe.csv` requires only `ticker` and `name`.** Every stage reads it
  without knowing what is in it, so a crypto, FX or futures seed runs the same pipeline. The 787-row
  US-equity seed is gone.
* **`Data/curator.py` rewritten** — 851 lines to 652, and the reduction is the smaller half of it.
  Work is handed out one identifier at a time through a plain thread pool with thread-local
  providers, replacing a chunked worker scheme, a shared mutable tally object and a lock-guarded
  progress counter; `download_identifier` now returns an outcome string instead of mutating shared
  state. An empty universe file is reported as a sentence rather than a traceback.
* **`Data/refinery.py` deletes refined files for securities no longer in the universe.** Leaving
  them was the worst kind of bug this stage can have: every cross-sectional column is computed over
  the securities present, so a stale file carries ranks taken against a universe that no longer
  exists, and anything reading the directory silently averages two incompatible cross-sections. It
  produced a plausible number and no error.
* **The daily return moved from the Refinery to the Curator**, as `c_return_1d`. It is a function of
  one security's own history, so it was in the wrong stage.
* **`Data/refinery.py` joins whatever the security master classifies by**, reporting and skipping a
  column the master does not carry instead of joining it in as nulls. The `sector`/`industry`
  hard-coding is gone; the `_current` suffix rule that made it safe stays.
* **The shared modules are renamed for what they hold**: `panel.py` is now `securities_panel.py` and
  `engine.py` is now `backtest_engine.py`, joined by the two new modules — so `Experiments/` reads as
  panel in, weights, engine out, attribution.
* **`securities_panel.py` names no classification column in `BASE_PANEL_COLUMNS`.** Classification is
  optional and discovered from the files, and a missing column raises a readable error naming it
  rather than failing inside `read_csv`.
* **`Universe/universe.ipynb` rewritten**, from 49 cells to 20, and no longer equity-shaped. It now
  answers the question everybody forgets: **when does each security become usable?** A five-year
  warm-up moves the honest start of a backtest by five years, and nothing else in the pipeline says
  so.
* **`Data/analyzer.ipynb` rewritten** around the information-coefficient table, with the two
  questions any signal owes an answer to written into its header: does it separate anything, and if
  it is fitted, what is look-ahead worth?
* **`AGENTS.md` cut from 624 lines to about 380.** Everything the README covers — the eight steps,
  the column convention, setup, credentials, the shared modules — was removed rather than restated.
  Versioning moved here, to the file that already explained it.
* **`README.md` rewritten as the entry point**: six numbered steps that run the pipeline, a
  walkthrough of the eight process steps in the order to do them, and one table saying where each
  kind of logic goes. **The run order is stated as a dependency**, because the universe notebook sits
  between two Data commands and running the refinery early does not fail — it silently drops columns.
* **The invariant that weights sum to 1.0 is now "at most 1.0".** A strategy that can go to cash
  cannot satisfy the stricter form, and the engine already parks the residual in a real, priced
  instrument.
* **The bar in `AGENTS.md` gains a clause:** never choose a parameter on the metric it will be judged
  by. Choose it on a property of the signal — persistence, coverage, turnover — and publish the
  sweep.

### Removed

* `stage_supplied_price_series` and its engine-column fallbacks from the Curator. It staged a
  hand-supplied index price series into the market-data directory; machinery kept for a file that
  does not exist teaches the reader to keep machinery for files that do not exist. The drop-zone
  directories and the *what is missing* report stay.
* The `sector_sample` download mode, and the 787-row US-equity universe with it.

## 0.2.0 (2026-09-03)

**MINOR** — additive. The Bibliotheca gains the two books whose method the process runs, and the
lineage the process descends from.

### Added

* **Part 0 of `Bibliotheca/BIBLIOGRAPHY.md` — where the process comes from.** Fifteen questions the
  field asked in order, who answered each, what it settled, and which step or rule of this process
  descends from it. Provenance, not notes.
* **Two book notes**: Paleologo (2021) — total PnL as an idiosyncratic series plus a factor series,
  selection, sizing and timing by counterfactual books, and why a factor model built on relative
  factors is blind to an absolute rule; and Grinold & Kahn (2000) — the information coefficient, the
  fundamental law, and the information horizon behind the analyzer's decay chart.
* Part 5 states the one control with no paper behind it — look-ahead — rather than citing a weak fit.

---

## 0.1.0 (2026-09-03)

**MINOR** — the template instantiated. No strategy, no data, no result: the KN Research Process with
nothing in it yet.

### Added

* The eight-step **KN Research Process** as a folder structure, steps 1-7 inside the repository and
  step 8 outside it. Each stage owns its outputs and reads only from the stages above it.
* **Four control documents at the root** — `OBJECTIVE.md`, `RESULTS.md`, `CHANGELOG.md`, `AGENTS.md`
  — with stated contracts, plus `README.md` and a one-line `CLAUDE.md`.
* **`Experiments/Experiment_1/`**, the benchmark slot, with its four per-experiment files and a
  notebook whose section contract leaves exactly one cell — the rule — to the strategy.
* The two shared modules, `Experiments/securities_panel.py` and `Experiments/backtest_engine.py`, and the Data stage's
  three blocks.
* `Universe/universe.ipynb` and the 787-row `Universe/Investable_Universe.csv` seed.
* `Bibliotheca/` with the note convention and **seven research-integrity notes**, one per control
  `AGENTS.md` claims.
* `Paper_Trading/BITACORA.md` with the five-criterion graduation gate, and two skeleton scripts
  carrying their contracts as docstrings.
* Dev container, `Config/.env.template`, Ruff configuration and `.gitignore`.

### Provenance

Extracted from **Golden-Flow 0.9.0** (commit `10a0d6b`), the KaxaNuk Investment Lab's reference
implementation, on 2026-09-03. Everything specific to that strategy was removed; everything the
process itself needs was kept.
