# KaxaNuk Researcher

**A research companion you name and teach.** It keeps a library of what you have read, knows the
KaxaNuk Investment Lab and the KaxaNuk Strategy Template, and helps you write the hypothesis of
every strategy you build — with every claim pointing back to something you actually read. One
researcher per person, not per strategy; one repository per strategy.

This repository is one package: every KaxaNuk skill — the researcher's, the process's and each
Investment Lab library's — the strategy template, a strategy worked through it, and the
researcher's home.

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

`--target codex`, `cursor` or another agent in place of `claude`; Claude Code receives everything,
and [`SETUP.md`](SETUP.md) says what the others miss. The skills are then in every folder you open,
so **a strategy installs nothing of its own**; `apm update -g` brings every new version.

## The path

Five moves, each in a **new session**, in the folder the line names. Lost at any point: run `next`
in the folder, and it says which move is done and what comes next.

| | In | Run | It makes |
| --- | --- | --- | --- |
| 1 | anywhere | `init-researcher Ada` | your researcher's home, with the name you choose |
| 2 | the home | `interview` | seven questions, ten minutes; writes `RESEARCHER.md` and the agent file |
| 3 | the home | `apm install --target claude` | the researcher as an agent you call by name |
| 4 | the home | `init-strategy fcf-yield-quality` | your first strategy, one repository of its own, beside the home; its `SETUP.md` finishes the setup |
| 5 | the strategy, with the home added by `--add-dir` | `objective` | the strategy's claims, before any paper — then the order of work, A to H, in the template's README, which the strategy's links to |

The interview's questions on markets and the reading map cover investment research; a researcher
for another field answers *not sure yet* where it must and grows by reading.

**What a strategy needs from outside this package.** The researcher needs nothing more. A strategy
needs a key from a data provider the Data Curator reads — FMP, Sharadar or LSEG, from the provider
itself; the worked example uses FMP — before it can download anything, the worked example
included. Three of the Lab libraries are not public: the Backtest Engine and Attribution Analysis
each need a KaxaNuk licence, a welcome email with an index URL and a key, and Portfolio
Construction needs access to KaxaNuk's private `KaxaNuk/Portfolio-Construction` repository; ask
KaxaNuk for them. Without them a strategy still runs up to its portfolios — an equal-weight book
needs nothing more — and the backtest and attribution say what is missing and skip. Every key goes
in the strategy's `Config/.env`, which only you fill in and nobody commits; the strategy's own
`SETUP.md` says how.

In Claude Code, type a skill or a command with a slash, as `/init-strategy fcf-yield-quality`;
elsewhere, ask for it by name.

**Invite the researcher into a strategy** by opening your assistant in the strategy's folder and
adding the home to the session — `claude --add-dir <the home>`, `/add-dir`, or the desktop app's
add-folder button. The skills are already there; the invitation brings the library. The home's
`AGENTS.md` says how, and what loads.

---

## The skills and commands

Every one that writes shows its plan first and waits for your go.

| Skill | What it does |
| --- | --- |
| `read` | reads sources into the library — `Sources/` into `Knowledge/` at home; in a strategy, once `OBJECTIVE.md` has claims, into notes beside the PDFs in its `Bibliotheca/`. A script extracts a PDF by chapter; you pick the chapters that serve your questions; one note per chapter read. It carries the reading map, `references/reading-map.md`, that `interview` proposes the first works from |
| `query <question>` | answers from the library — concept pages, then the notes they cite, then your `Philosophy/`, then the sources; every claim cited, gaps named |
| `init-researcher`, `init-strategy`, `init-example` | make a folder — your home, a strategy, or the worked example `liquid-golden-cross` to read or run — copied by a script, byte for byte, after a plan and your go, never from memory. A file a strategy made before template 0.10.0 lacks comes back from the template: `init-strategy`'s script with `--only <path>`, which never overwrites |

| Command | What it does |
| --- | --- |
| `next [strategy]` | where you stand — at home or in a strategy — and the one thing to do next, with the command that does it; reads the folder, writes nothing |
| `interview` | seven questions that make the researcher yours; writes `RESEARCHER.md` and the agent that makes it callable by name. `interview force` starts over |
| `objective [strategy]` | drafts a strategy's `OBJECTIVE.md` — the idea and its claims — before any paper, then from the notes |
| `blueprint <N> [strategy]` | drafts `BLUEPRINT_N.md` — thesis, rules, predictions — every prediction citing a note or a measurement |
| `brainstorm <N> ["idea"] [strategy]` | appends a dated entry to `BRAINSTORMING_N.md` for the next thing to try |
| `challenge <N> [strategy]` | checks a finished experiment against its own blueprint |
| `audit [deep]` | reviews the library — links, duplicates, index, orphans, frontmatter, stale installs |
| `refresh-index` | rebuilds `Knowledge/INDEX.md` from what is on disk |
| `refine <path>` | a voice-preserving editor pass over one of your `Philosophy/` files |
| `teach <topic>` | tutors you on a topic from your library, one lesson per session |
| `update [check]` | brings a new version into your home — `apm update -g`, and what changed in the home's own files, shown as a diff |

How a researcher grows beyond the Lab — a tool, a project, a field of its own — is *Growing your
researcher* in the home's README: four moves, each with the file it changes.

**The Investment Lab skills**, which the assistant loads when the work calls for them — in a
strategy, in the order of its steps:

| Skill | What it covers |
| --- | --- |
| `experiment-lifecycle` | the process: the document architecture, the order of work, the notebook contract, the graduation gate |
| `universe-point-in-time` | step 2, the investable universe: the seed, the security master, the usable date |
| `data-curator-custom-calculations` | the Data Curator's `c_*` columns: naming, inputs, the `DataColumn` API |
| `data-analyzer-runs` | step 3's last block, the analyzer: whether a feature carries signal, before any book is built |
| `portfolio-construction-runs` | step 4, sizing a book with the Portfolio Construction library |
| `backtest-engine-runs` | pricing a book with the Backtest Engine, and reading its report |
| `attribution-analysis-runs` | running Attribution Analysis on a book, and getting its tables out |
| `alpha-decomposition` | reading attribution: is the signal doing anything, or is it a factor exposure |
| `paper-trading-gate` | step 7, graduation: the five criteria, how each is evidenced, what a paper-trading run may do |

**The house rules**: `how-we-work` (where work lands, changelogs, versions) and `bloom-code-lint`
with the Bloom Code, PEP 8, test-writing and filesystem-boundaries instructions, which apply to
every Python project on the machine where the agent receives them (`SETUP.md` step 1).
`bloom-code-lint` is the check to run by hand.

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
tests/                the tests of the skills' scripts and of the tools
tools/                check_repo.py, the repository's own checks;
                      sync_investment_lab_references.py, which regenerates experiment-lifecycle's
                      references and the template's generated files from the example; and the
                      three eval scripts, eval_run.py, eval_fixtures.py and eval_history.py
evals/                behavioural evals of the skills and commands, run by tools/eval_run.py;
                      evals/README.md says how
SETUP.md              the install, step by step — what an assistant follows when you paste the URL
apm.yml               the package: what apm install reads; it depends on nothing
pyproject.toml        the environment of the scripts and their tests
AGENTS.md, CLAUDE.md  the rules for changing this repository
CHANGELOG.md          one entry per version
LICENSE               MIT
.gitattributes        LF line endings everywhere, so a clone and scaffold.py see the bytes committed
.gitignore            what apm install and Python write per machine
```

**What this repository owns, and what a copy owns.** This repository owns what is written once and
copied or installed everywhere; a copy owns what its owner writes in it. A strategy made from the
template is its owner's from the first commit and never merges back; the skills keep updating with
`apm update -g`.

---

## Development

```bash
uv run --no-project --with pytest --with pypdf pytest -q
uvx ruff check .
(cd examples/liquid-golden-cross && uvx ruff check .)
uv run --no-project python tools/check_repo.py
uv run --no-project python .apm/skills/bloom-code-lint/scripts/bloom_code_check.py \
  .apm/skills/*/scripts tests tools examples/liquid-golden-cross \
  --local-package bloom_code_check
```

`tools/check_repo.py` finds what has shipped before without an error: versions that disagree, an
example that lost a heading of the template, markers left open, the section symbol, a skill
description APM would reject, `experiment-lifecycle`'s references or the template's generated
files out of step with the example, a path too long for Windows, a line of prose past 100
columns. The worked example is linted with its own ruff settings, and the last command checks
the Bloom Code style of the skills' scripts, the tests, the tools and the example. Each runs
through `uv` alone: no Python of your own is needed. They run on your machine before a commit;
there is no CI, so nothing runs them for you. The behavioural evals — what a skill or a command
does when a user runs it — are a separate run with its own cost; `evals/README.md` says how.

`AGENTS.md` has the rules for changing this repository: work lands on `main`, and a release is
tagged `vX.Y.Z` there. `CHANGELOG.md` has one entry per version.

---

## Licence

MIT, see [`LICENSE`](LICENSE).
