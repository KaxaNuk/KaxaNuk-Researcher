# Agents — how this repository is changed

This repository is the KaxaNuk Researcher: one APM package whose skills and commands are in `.apm/`,
and the three starting points its `init-*` skills copy — `templates/strategy/`,
`templates/researcher/` and `examples/liquid-golden-cross/`. Read this before changing anything.

## What lives where

| Path | What it is | Changed how |
| --- | --- | --- |
| `.apm/skills/`, `.apm/prompts/` | the skills and commands every installed researcher receives | edited here, then `apm install -g <this folder>` to try them, and a new session |
| `.apm/skills/init-strategy/scripts/scaffold.py` | the one script the three `init-*` skills run | with its tests in `tests/`, which pass before any commit |
| `templates/strategy/` | the KaxaNuk Strategy Template, copied into every new strategy | a change here is a template release: its `apm.yml`, `pyproject.toml` and `CHANGELOG.md` move together |
| `examples/liquid-golden-cross/` | one strategy worked through the template | the same, and its `uv.lock` records the project version: `uv lock` after a bump |
| `templates/researcher/` | the researcher's home, copied by `init-researcher` | its `apm.yml` version leads its `CHANGELOG.md`; `update` compares a home against it |

**The template and the example share every file the example does not mark.** A change to the
template's description of a file changes the example's copy in the same commit; only the lines
between `<!-- example: begin -->` and `<!-- example: end -->` — `# --- example: begin ---` in Python,
`# EXAMPLE-ONLY CELL` on a notebook cell — are the example's own.

## Rules

- **A file of a starting point is never written from memory** — not by a skill, not by the script,
  not by an agent helping here. `scaffold.py` copies byte for byte.
- **Every change carries its `CHANGELOG.md` entry**, and a version bump in `apm.yml` in the same
  commit: the package's at the root, the template's, the example's or the home's in its own folder.
  Tag `vX.Y.Z` on `main` after the merge.
- **Issues before branches, pull requests into `main`**, as the `how-we-work` skill in
  KaxaNuk-Agent-Skills says.
- **The Lab's skills are not edited here.** `experiment-lifecycle`, `alpha-decomposition` and each
  library's skill live in KaxaNuk-Agent-Skills; this package depends on them through `kaxanuk`.
- **Markdown is wrapped at 100 columns.** Never use the section symbol; write "section".
- **No secrets, no binaries, no in-house strategy.** The worked example is the only strategy this
  repository names.
