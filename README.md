# KaxaNuk Researcher

[![CI](https://github.com/KaxaNuk/KaxaNuk-Researcher/actions/workflows/ci.yml/badge.svg)](https://github.com/KaxaNuk/KaxaNuk-Researcher/actions/workflows/ci.yml)

**A research companion you name and teach.** It keeps a library of what you have read, knows the
KaxaNuk Investment Lab and the KaxaNuk Strategy Template, and helps you write the hypothesis of every
strategy you build — with every claim pointing back to something you actually read. One researcher
per person, not per strategy; one repository per strategy.

This repository is everything that takes: every KaxaNuk skill — the researcher's, the process's
and each Investment Lab library's — the strategy template, a strategy worked through it, and the
researcher's home. One source of truth, versioned together, so one pull request can change a skill,
the template it describes and the example that shows it, and one `apm update -g` brings it to every
folder you work in.

---

## Install

Paste this into Claude or Codex:

```text
Please help me install this repo: https://github.com/KaxaNuk/KaxaNuk-Researcher
```

It follows [`SETUP.md`](SETUP.md): it checks that git and [`uv`](https://docs.astral.sh/uv/) are
there, and installs the package once, for your user. By hand, it is:

```bash
uv tool install apm-cli
apm install -g KaxaNuk/KaxaNuk-Researcher --target claude
```

`--target codex`, `cursor` or another agent in place of `claude`. The skills are then in every
folder you open, so **a strategy installs nothing of its own**; `apm update -g` brings every new
version. Then, in a new session:

1. **`init-researcher Luna`** — your researcher's home, with the name you choose.
2. **`researcher-init`**, in that home — a short interview that makes the researcher yours.
3. **`init-strategy fcf-yield-quality`** — your first strategy, one repository of its own.

---

## Three commands make every folder

| Command | How often | What it makes |
| --- | --- | --- |
| `init-researcher <name>` | once per person | the researcher's home: `RESEARCHER.md`, `Sources/`, `Knowledge/`, `Philosophy/`, `Projects/`. Then `researcher-init` there interviews you and names it |
| `init-strategy <name>` | once per strategy | a new strategy repository from the KaxaNuk Strategy Template, with its first commit. You publish it to GitHub yourself |
| `init-example` | when you want it | the worked example, `liquid-golden-cross`, in a folder of its own — or, with a path, one of its files into your strategy: `init-example Experiments/Experiment_1` |

Each is a skill: in Claude Code, type it as `/init-strategy fcf-yield-quality`; elsewhere, ask for it
by name. Each copies files with a script, byte for byte, after a plan and your go — never from
memory — so every folder made from the same version starts identical.

**Invite the researcher into a strategy** by opening your assistant in the strategy's folder and
adding the home to the session — `claude --add-dir <the home>`, `/add-dir`, or the desktop app's
add-folder button. The skills are already there; the invitation brings the library. The home's
`AGENTS.md` says how, and what loads.

---

## The skills and commands

Every one that writes shows its plan first and waits for your go.

| Skill | What it does |
| --- | --- |
| `read` | reads sources into the library — `Sources/` into `Knowledge/` at home; in a strategy, once `OBJECTIVE.md` has claims, into notes beside the PDFs in its `Bibliotheca/`. A script extracts a PDF by chapter; you pick the chapters that serve your questions; one note per chapter read |
| `query <question>` | answers from the library — concept pages, then the notes they cite, then your `Philosophy/`, then the sources; every claim cited, gaps named |
| `init-researcher`, `init-strategy`, `init-example` | make a folder, as above |

| Command | What it does |
| --- | --- |
| `researcher-init` | the interview; writes `RESEARCHER.md` and the agent that makes your researcher callable by name |
| `objective [strategy]` | drafts a strategy's `OBJECTIVE.md` — the idea and its claims — before any paper, then from the notes |
| `blueprint [strategy] <N>` | drafts `BLUEPRINT_N.md` — thesis, rules, predictions — every prediction citing a note or a measurement |
| `brainstorm [strategy] <N>` | appends a dated entry to `BRAINSTORMING_N.md` for the next thing to try |
| `challenge [strategy] <N>` | checks a finished experiment against its own blueprint |
| `audit [deep]` | reviews the library — links, duplicates, index, orphans, frontmatter, stale installs |
| `refresh-index` | rebuilds `Knowledge/INDEX.md` from what is on disk |
| `refine <path>` | a voice-preserving editor pass over one of your `Philosophy/` files |
| `teach <topic>` | a multi-session tutor grounded in your library |
| `update [check]` | brings a new version into your home — `apm update -g`, and what changed in the home's own files, shown as a diff |

**The Investment Lab skills**, which the assistant loads when the work calls for them — in a
strategy, in the order of its steps:

| Skill | What it covers |
| --- | --- |
| `experiment-lifecycle` | the process: the document architecture, the order of work, the notebook contract, the graduation gate |
| `universe-point-in-time` | step 2, the investable universe: the seed, the security master, the usable date |
| `data-curator-custom-calculations` | the Data Curator's `c_*` columns: naming, inputs, the `DataColumn` API |
| `portfolio-construction-runs` | step 4, sizing a book with the Portfolio Construction library |
| `backtest-engine-runs` | pricing a book with the Backtest Engine, and reading its report |
| `attribution-analysis-runs` | running Attribution Analysis on a book, and getting its tables out |
| `alpha-decomposition` | reading attribution: is the signal doing anything, or is it a factor exposure |

**The house rules**: `how-we-work` (issues, branches, changelogs, versions), `bloom-code-lint` with
the Bloom Code, PEP 8 and test-writing instructions, `apm-usage`, `initialize-apm`,
`devcontainer-aware-command-execution` and `propagate-mcp-env-vars`.

---

## What is in here

```
.apm/skills/          every skill: the researcher's, the Investment Lab's and the house rules'
.apm/prompts/         the commands
.apm/instructions/    the house style: Bloom Code, PEP 8, test writing, filesystem boundaries
templates/strategy/   the KaxaNuk Strategy Template — the eight steps as folders; its README is the
                      process, and the order of work a strategy follows
templates/researcher/ the researcher's home, empty
examples/liquid-golden-cross/
                      one strategy worked through every folder of the template
tests/                the tests of every script and of the checks
tools/                check_repo.py, the repository's own checks, run by CI; and the script that
                      regenerates experiment-lifecycle's references from the example
SETUP.md              the install, step by step — what an assistant follows when you paste the URL
apm.yml               the package: what apm install reads; it depends on nothing
```

The template and the example are ordinary folders: read them here, or make one with the commands
above. Only the example carries a strategy's own content, between example markers —
`<!-- example: begin -->` and `<!-- example: end -->` — beside the template's description of what
belongs in each file.

**What this repository owns, and what a copy owns.** This repository owns what is written once and
copied or installed everywhere; a copy owns what its owner writes in it. A strategy made from the
template is its owner's from the first commit and never merges back; the skills keep updating with
`apm update -g`.

---

## Development

```bash
uv run --group dev pytest
uvx ruff check .
python tools/check_repo.py
```

`tools/check_repo.py` finds what has shipped before without an error: versions that disagree, an
example that lost a heading of the template, markers left open, a path too long for Windows. CI runs
all three on every push and pull request.

`AGENTS.md` has the rules for changing this repository. Releases are tagged `vX.Y.Z` on `main` after
the merge, and `CHANGELOG.md` has one entry per version.

---

## Licence

MIT, see [`LICENSE`](LICENSE). The library architecture — sources compiled into a wiki with an
append-only log, the person's notes kept apart, plan-and-confirm before any write — adapts the
MIT-licensed *obsidian-vault-kit*; the notice is kept in `LICENSE`.
