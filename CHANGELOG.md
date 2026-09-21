# Changelog for KaxaNuk-Researcher

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Releases are
tagged `vX.Y.Z`.

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
