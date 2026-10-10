# Agents — how this repository is changed

This repository is the KaxaNuk Researcher: one APM package that carries every KaxaNuk skill,
instruction and command in `.apm/`, with its one agent, `blueprint-critic`, and the starting
points its `init-*` skills copy — `templates/strategy/`, `templates/researcher/`,
`templates/python-library/` and the worked examples, organised by kind as the templates are, one
folder each under `examples/<kind>/<name>/`: today one, `examples/strategy/golden-flow/`. Read this
before changing anything. The rules a researcher works by in its home are in
`templates/researcher/AGENTS.md`; the rules a strategy works by are in
`templates/strategy/AGENTS.md`, and a Python library's in `templates/python-library/AGENTS.md`.
This file is about changing the package.

## What lives where

| Path | What it is | Changed how |
| --- | --- | --- |
| `.apm/skills/`, `.apm/prompts/`, `.apm/instructions/`, `.apm/agents/` | every skill, command, instruction and agent an install receives: the researcher's, the process's (`experiment-lifecycle`, `alpha-decomposition`), each Lab library's, the house rules and `blueprint-critic`, deployed for the user with the skills | edited here, then tried by a project-scope install of an archive of the tree — LF endings, no ignored folders — from a short scratch folder, with the pinned APM, in a shell whose home is a short throwaway folder, because a skill installed for the user wins over a project skill of the same name: `uvx --from apm-cli==0.33.0 apm install <the archive> --target claude`, as `CONTRIBUTING.md`'s *Development* shows, and a new session there; before a release, that install deploys exactly 22 skills, 9 commands, 3 rules and 1 agent with no warning. Never `apm install -g <this folder>`, which on Windows stages the whole working tree, ignored folders included, at a depth past the path limit under HOME |
| the skills' `scripts/` | `scaffold.py`, `name_library.py`, `user_targets.py`, `extract.py`, `check_numbers.py`, `bloom_code_check.py`: what `init-*`, the install in `SETUP.md`, `interview`, `next`, `update`, `read`, `audit deep` and `bloom-code-lint` run for every user. `user_targets.py`, in `init-researcher`, puts the assistant in use on APM's list in `~/.apm/apm.yml` — an assistant missing from a list there loses its files to the next install or update without `--target` — and checks the researcher's files for it | nothing tests them: a change is tried by running the skill that uses it in a scratch folder before the commit — `user_targets.py` in a shell whose home is a throwaway folder, never against the real `~/.apm` |
| `.apm/skills/experiment-lifecycle/references/` | the experiment documents and notebook, as the example's with its own lines stripped | by hand, in the same commit as the example's change |
| the `Bibliotheca/` index and log, the drivers, modules, notebooks and experiment and paper-trading files in `templates/strategy/` | the example's with its own lines stripped | by hand, in the same commit as the example's change |
| `templates/strategy/` | the KaxaNuk Strategy Template, copied into every new strategy | a change here is a template release: its `pyproject.toml`, which declares its version, and `CHANGELOG.md` move together |
| `examples/strategy/golden-flow/` | one strategy worked through the template, the one worked example today | the same; it commits no `uv.lock`, so its library versions resolve when `uv sync` runs |
| `templates/researcher/` | the researcher's home, copied by `init-researcher` | its `apm.yml` version leads its `CHANGELOG.md`; `update` compares a home against it |
| `templates/python-library/` | the KaxaNuk Python Library Template, laid out like the KaxaNuk Data Curator, <https://github.com/KaxaNuk/Data-Curator>: copied by `init-python-library`, then named by its `name_library.py`, which only puts in the names, the holder and the one sentence the owner chose, and moves the package folder | a change here is a template release: the number in the first sentence of its `CHANGELOG.md`'s `## [Unreleased]` entry, *Started from the KaxaNuk Python Library Template X.Y.Z*, moves, and the root `CHANGELOG.md` says what changed — the rest of its `CHANGELOG.md`, and its `__version__`, 0.1.0, are the new library's own. A placeholder changed here changes `name_library.py` in the same commit, and a change to its dependency groups updates `TOOL_DISTRIBUTIONS` and `TOOL_IMPORT_NAMES` there; a change to its first-commit message, in `scaffold.py`'s `STARTING_POINTS`, updates `FIRST_COMMIT`. Ruff and the Bloom Code check, at 120, run in place; `uv sync`, the tests, the documentation and `uv build` only in a copy outside the repository, as `CONTRIBUTING.md` shows, never inside `templates/` |

**The strategy template and the example share every file the example does not mark.** A change to
the template's description of a file changes the example's copy in the same commit; only the lines
between `<!-- example: begin -->` and `<!-- example: end -->` — `# --- example: begin ---` in
Python, `# EXAMPLE-ONLY CELL` on a notebook cell — are the example's own, and every other line is
the same in both copies. A marker stands alone on its line, at column 0. The only exceptions are
these: the example's status banner in `AGENTS.md`; the `init-example` lines of `SETUP.md`; the body
of `OBJECTIVE.md`; the entries of `CHANGELOG.md`; the name and version in `pyproject.toml`; and,
whole, the example's `README.md`, which is its own as a strategy's is after `SETUP.md` step 5, the
example's seed CSV and every file only the example has — its notes, `Universe/seed.py` and a
frozen book's `FREEZE.json` with the files it hashes. `paper_trading_N.py` stays shared and
marked.

## Rules

- **A file of a starting point is never written from memory** — not by a skill, not by the script,
  not by an agent helping here. `scaffold.py` copies byte for byte; `name_library.py` then only puts
  the owner's names and words into a Python library's copy.
- **No Lab library's code in the package.** A skill is written from the library's documentation,
  its changelog and runs — never from its source, a wheel's contents, a clone or a source page its
  documentation site links to — and names only its public API: no private module, internal class,
  tolerance or copied pattern, and no account of which branch runs inside. A difference between
  the documentation and the library is settled by a run, and the skill says *checked on <build> by
  running it*. The same holds for an agent helping here, and for the Analytics Factory's files and
  KaxaNuk's research: none of it is copied into the package.
- **Every change carries its `CHANGELOG.md` entry**, and a version bump in the same commit: in
  `apm.yml` for the package at the root and for the home, in `pyproject.toml` for the strategy
  template and the example, and in the *Started from* sentence of the Python library template's
  `CHANGELOG.md`, whose changes the root's entry records. The entry opens with one plain
  sentence a newcomer understands — the line the researcher's weekly word on a new version quotes —
  and its *What to do differently* says what the owner says (*say `update` in your home*), never
  the `apm` command `update` runs for them. Tag `vX.Y.Z` on `main` once the release's commit is
  there, with the message `X.Y.Z: <that sentence>`.
- **Work lands on `main`**, as the `how-we-work` skill says: a branch and a pull request only for a
  change you want reviewed, deleted once merged. `main` is the only branch that stays, and
  `apm update -g` installs it as it stands, so nothing reaches `main` without its version.
- **Every KaxaNuk skill lives here.** A skill for a new Lab library is a folder in `.apm/skills/`;
  a change to a library's API changes its skill in the same release, and the worked example where
  it uses that library — with a new example version and a journal entry, re-run where a figure
  moves.
- **A new starting point** — valuation, M&A, a budget — is, as `python-library` is, a folder under
  `templates/` that `scaffold.py` copies, a kind in its `STARTING_POINTS`, and an `init-<kind>`
  skill that runs it as `init-strategy` does; a copy that takes names gets them from a script of
  that skill's that only puts them in, as `init-python-library`'s `name_library.py` does. Its
  `AGENTS.md` names it in a marker line that survives its setup,
  `<!-- kaxanuk-starting-point: <kind> -->`, alone at column 0, and carries a `## Next` table,
  *Done when* and *The next thing*, that `next` reads for any kind other than a strategy. No folder
  in it is named `Bibliotheca/`: that is a strategy's word only, and every skill that finds one
  reads the folder as a strategy.
- **A fork changes every line that names `KaxaNuk-Researcher`**, in either case —
  `git grep -i kaxanuk-researcher` finds them, `scaffold.py`'s `INSTALLED_PACKAGE_PATHS` included —
  and installs as the one researcher package on its user's machine. Two packages with skills or
  commands of the same names do not share a user: a `-g` install of the second replaces a
  same-named skill of the first, with a warning, and overwrites a same-named command silently. The
  last install wins.
- **Ruff and the Bloom Code check pass before any commit,** run as `CONTRIBUTING.md`'s
  *Development* section shows. There is no CI: nothing runs them for you.
- **Markdown you write or change is wrapped at 100 columns**, with no literal tab and LF line
  endings. A line inside a fenced code block, a table row, a line carrying a URL, the YAML
  frontmatter at the top of a file and a line copied verbatim from a strategy's fixed or
  append-only record — a blueprint, a journal entry, a registered gate section — may run longer.
  Never use the section symbol; write "section".
- **No secrets, no binaries.** The worked example, `golden-flow`, is the only strategy this
  repository names, as a curated copy; nothing in it is taken from a live strategy repository after
  the copy.

## When a Lab library or an Analytics Factory file changes

1. **Read the library's changelog** from the build its skill names as `library_version` to the new
   one, `[Unreleased]` aside: what changes for the install, a caller, a key or a trap, and its
   documentation — never its code. Copy names and behaviour only — a private index, host or key
   stays a `{SERVER}` placeholder.
2. **Record the new build** in the *Latest* column of
   `.apm/skills/next/references/investment-lab.md` — what `next`'s weekly check in a strategy
   compares the installed builds against — and, in the library's skill, a short *Changed in
   <build>* paragraph: from its changelog, not yet checked by a run.
3. **Check it by a run** before `library_version` moves: in a scratch copy of the worked example on
   a short path outside this repository, with the new build, every line that says *checked*,
   *verified* or *measured on <old build>* (`git grep -n "<old build>" .apm templates examples`),
   the example re-run from a wiped copy. Only then does `library_version` move, and the paragraph
   become the skill's own text.
4. **One release carries it all**: the skill and its `references/`, `investment-lab.md`, the
   template's `pyproject.toml` floor or `Config/.env.template` key with the example's copy, and,
   where a figure moves, a new example version with its journal entry, `FINDINGS_1.md` and
   `RESULTS.md`, and every skill that quotes the figure; the CHANGELOG's *What to do differently*
   names the build to install.
5. **An Analytics Factory change** — a folder, a file name, a header, a date order — changes
   `Data/hand_supplied.py` in the template and the example, which keeps reading the older names,
   `attribution-analysis-runs` and `investment-lab.md`; a frozen book's copy stays as it was.
6. **A library that replaces a hand-rolled stage** (the Data Refinery, the Data Analyzer) gets its
   own `*-runs` skill with a `library_version`, and the stage's seam file, `experiment-lifecycle`
   and `investment-lab.md` move with it.
7. **The worked example's seed follows its index.** When the KN US Equity Core's membership changes,
   rebuild `examples/strategy/golden-flow/Universe/Investable_Universe.csv` with its
   `Universe/seed.py`: the listings whose FMP symbol, verified or not, is the index's own ticker,
   departed names included, with their first and last price dates — tickers and dates only, never an
   ISIN, a name or any other vendor field. It is an example release, re-run where a figure moves;
   the frozen book keeps its seed as example 0.17.0 rewrote it, tickers and dates only; never
   restore the hashed original to satisfy `FREEZE.json`.
8. **A new worked example** — an ETF strategy, or one users ask for — is a folder of its own,
   `examples/<kind>/<name>/`, its kind the template it is worked through as `templates/<kind>/`
   names it — `examples/strategy/<name>/` for an ETF strategy — curated as `golden-flow` is: the
   template's shared lines, its own marked lines, a seed of tickers and dates only, and its own
   version and changelog. `init-example` offers it with nothing registered: `scaffold.py` finds
   every folder `examples/<kind>/<name>/` that holds a `README.md`, and shows for it the line that
   README marks, `<!-- kaxanuk-example: <one line> -->` alone at column 0, or else its first
   paragraph's first sentence — written to say, to a newcomer choosing, what the example shows.
