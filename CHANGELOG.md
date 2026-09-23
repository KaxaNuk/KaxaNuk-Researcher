# Changelog for KaxaNuk-Researcher

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Releases are
tagged `vX.Y.Z`.

## [0.13.1] - 2026-09-23
Every pull request asks for its review the moment it opens.
### Added
- **`.github/CODEOWNERS`** names Alan and Arturo as the owners of every path, so GitHub requests
  their review on every pull request as it opens. `main` requires one approval from someone other
  than the author, administrators included, with no force push and no deletion; a request that
  goes out by itself is what keeps a pull request from waiting unseen.

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
