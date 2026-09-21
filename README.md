# KaxaNuk Researcher

[![CI](https://github.com/KaxaNuk/KaxaNuk-Researcher/actions/workflows/ci.yml/badge.svg)](https://github.com/KaxaNuk/KaxaNuk-Researcher/actions/workflows/ci.yml)

**A research companion you name and teach.** It keeps a library of what you have read, knows the
KaxaNuk Investment Lab and the KaxaNuk Strategy Template, and helps you write the hypothesis of every
strategy you build — with every claim pointing back to something you actually read. One researcher
per person, not per strategy; one repository per strategy.

This repository is everything that takes: the researcher's skills and commands, the strategy
template, a strategy worked through it, and the researcher's home — one source of truth, versioned
together, so one pull request can change a skill, the template it describes and the example that
shows it. The skills for each Investment Lab library live in
[KaxaNuk-Agent-Skills](https://github.com/KaxaNuk/KaxaNuk-Agent-Skills), and come with this package.

**To install, paste this into Claude or Codex:**

```text
Please help me install https://github.com/KaxaNuk/KaxaNuk-Researcher
```

It follows [`SETUP.md`](SETUP.md). Your first ten minutes, in four commands:

1. **Install once:** `apm install -g KaxaNuk/KaxaNuk-Researcher` — then open a new session.
2. **`init-researcher Luna`** — your researcher's home, with the name you choose.
3. **`researcher-init`**, in that home — a short interview that makes the researcher yours.
4. **`init-strategy fcf-yield-quality`** — your first strategy, one repository of its own.

---

## Install once, for your user

You need [`uv`](https://docs.astral.sh/uv/) and git. Then, once per machine:

```bash
uv tool install apm-cli
apm install -g KaxaNuk/KaxaNuk-Researcher --target claude
```

`--target codex`, `cursor` or another agent in place of `claude`. The package brings `kaxanuk`, every
Investment Lab package from KaxaNuk-Agent-Skills, with it. The skills are now in every folder you
open — your researcher's home and every strategy — so **a strategy installs nothing of its own**.
When either repository changes, one command brings every change to every folder, then a new
session:

```bash
apm update -g
```

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

---

## What is in here

```
.apm/skills/          read and query, which the researcher reaches for on its own; init-researcher,
                      init-strategy and init-example, which you run by name
.apm/prompts/         the ten commands
templates/strategy/   the KaxaNuk Strategy Template — the eight steps as folders; its README is the
                      process, and the order of work a strategy follows
templates/researcher/ the researcher's home, empty
examples/liquid-golden-cross/
                      one strategy worked through every folder of the template
tests/                the tests of scaffold.py, extract.py and the checks
tools/check_repo.py   the repository's own checks, run by CI
SETUP.md              the install, step by step — what an assistant follows when you paste the URL
apm.yml               the package: what apm install reads, and its one dependency, kaxanuk
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
