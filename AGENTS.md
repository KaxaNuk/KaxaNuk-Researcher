# Agents — how this repository is changed

This repository is the KaxaNuk Researcher: one APM package that carries every KaxaNuk skill,
instruction and command in `.apm/`, with its one agent, `blueprint-critic`, and the three starting
points its `init-*` skills copy — `templates/strategy/`, `templates/researcher/` and
`examples/liquid-golden-cross/`. Read this before changing anything. The rules a researcher works
by in its home are in `templates/researcher/AGENTS.md`; the rules a strategy works by are in
`templates/strategy/AGENTS.md`. This file is about changing the package.

## What lives where

| Path | What it is | Changed how |
| --- | --- | --- |
| `.apm/skills/`, `.apm/prompts/`, `.apm/instructions/`, `.apm/agents/` | every skill, command, instruction and agent an install receives: the researcher's, the process's (`experiment-lifecycle`, `alpha-decomposition`), each Lab library's, the house rules and `blueprint-critic`, deployed for the user with the skills | edited here, then tried by a project-scope install of the working tree from a short scratch folder, with the pinned APM — `uvx --from apm-cli==0.29.0 apm install <path to this repository> --target claude`, as the README's *Development* shows — and a new session there; before a release, that install deploys exactly 16 skills, 11 commands, 4 rules and 1 agent with no warning. Never `apm install -g <this folder>`, which on Windows stages the whole working tree, ignored folders included, at a depth past the path limit under HOME; when ignored folders make the scratch install fail too, copy the files `git ls-files` lists to a short folder and install that |
| the skills' `scripts/` | `scaffold.py`, `extract.py`, `bloom_code_check.py`: what `init-*`, `read` and `bloom-code-lint` run for every user | nothing tests them: a change is tried by running the skill that uses it in a scratch folder before the commit |
| `.apm/skills/experiment-lifecycle/references/` | the experiment documents and notebook, as the example's with its own lines stripped | by hand, in the same commit as the example's change |
| the `Bibliotheca/` index and log, the drivers, modules, notebooks and experiment and paper-trading files in `templates/strategy/` | the example's with its own lines stripped | by hand, in the same commit as the example's change |
| `templates/strategy/` | the KaxaNuk Strategy Template, copied into every new strategy | a change here is a template release: its `pyproject.toml`, which declares its version, and `CHANGELOG.md` move together |
| `examples/liquid-golden-cross/` | one strategy worked through the template | the same; it commits no `uv.lock`, so its library versions resolve when `uv sync` runs |
| `templates/researcher/` | the researcher's home, copied by `init-researcher` | its `apm.yml` version leads its `CHANGELOG.md`; `update` compares a home against it |

**The template and the example share every file the example does not mark.** A change to the
template's description of a file changes the example's copy in the same commit; only the lines
between `<!-- example: begin -->` and `<!-- example: end -->` — `# --- example: begin ---` in
Python, `# EXAMPLE-ONLY CELL` on a notebook cell — are the example's own, and every other line is
the same in both copies. A marker stands alone on its line, at column 0.

## Rules

- **A file of a starting point is never written from memory** — not by a skill, not by the script,
  not by an agent helping here. `scaffold.py` copies byte for byte.
- **Every change carries its `CHANGELOG.md` entry**, and a version bump in the same commit: in
  `apm.yml` for the package at the root and for the home, in `pyproject.toml` for the template and
  the example.
  Tag `vX.Y.Z` on `main` once the release's commit is there.
- **Work lands on `main`**, as the `how-we-work` skill says: a branch and a pull request only for a
  change you want reviewed, deleted once merged. `main` is the only branch that stays.
- **Every KaxaNuk skill lives here.** A skill for a new Lab library is a folder in `.apm/skills/`;
  a change to a library's API changes its skill in the same release.
- **A fork changes every line that names `KaxaNuk-Researcher`** — `git grep KaxaNuk-Researcher`
  finds them, `scaffold.py`'s `INSTALLED_PACKAGE_PATHS` included — and installs as the one
  researcher package on its user's machine. Two packages with skills or commands of the same names
  do not share a user: a `-g` install of the second replaces a same-named skill of the first, with
  a warning, and overwrites a same-named command silently. The last install wins.
- **Ruff and the Bloom Code check pass before any commit,** run as the README's *Development*
  section shows. There is no CI: nothing runs them for you.
- **Markdown you write or change is wrapped at 100 columns**, with no literal tab and LF line
  endings. A line inside a fenced code block, a table row, a line carrying a URL and the YAML
  frontmatter at the top of a file may run longer. Never use the section symbol; write "section".
- **No secrets, no binaries, no in-house strategy.** The worked example is the only strategy this
  repository names.
