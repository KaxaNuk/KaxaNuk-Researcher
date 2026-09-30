# KaxaNuk Researcher

**A research companion you name and teach.** It keeps a library of what you read, answers from it
with every claim pointing back to a source, helps you work out your ideas, and walks you through
building an investment strategy with the KaxaNuk Investment Lab. One researcher per person; it
works in any language.

## Install — three steps, no coding

1. Open **Claude** (the desktop app or Claude Code), **Codex** or **Gemini**.
2. Paste this line and send it:

   ```text
   Please help me install this repo: https://github.com/KaxaNuk/KaxaNuk-Researcher
   ```

3. Answer its questions. It asks your language first, then everything happens in the same
   conversation:
   - it installs what it needs — allow the commands it asks about, that is all you do;
   - it asks what you want to call your researcher, and where to keep it — a folder with that
     name, `C:\Research\Ada` for example;
   - it asks four short questions about you and how you see markets, about five minutes;
   - it shows you your researcher's folders, what each one is for, and what to do next.

Then open your researcher's folder in a **new** conversation and say hello, by its name.

### Instalación en español

1. Abre **Claude** (la app de escritorio o Claude Code), **Codex** o **Gemini**.
2. Pega esta línea y envíala:

   ```text
   Please help me install this repo: https://github.com/KaxaNuk/KaxaNuk-Researcher
   ```

3. Responde sus preguntas. Primero te pregunta el idioma — elige *Español* — y todo sigue en la
   misma conversación: instala lo necesario (solo permite los comandos que te pida), te pregunta
   el nombre de tu investigador y dónde guardarlo, te hace cuatro preguntas cortas, unos cinco
   minutos, y te explica sus carpetas y qué hacer después.

Después abre la carpeta de tu investigador en una conversación **nueva** y salúdalo por su nombre.

## What you can use it for

| You want to | Say or type | You get |
| --- | --- | --- |
| keep what you read, and ask it later | `read`, then `query <question>` | a note for each paper or chapter you chose; answers that cite them and name what is missing |
| work out an idea, a plan or a decision | `study <subject>` | a study in `Studies/`: your words, what your library says for and against, and what to check next |
| build a strategy | `init-strategy <name>`, then `objective`, `blueprint`, `challenge` | a folder of its own on the KaxaNuk Strategy Template, every claim before any test, every number from the Lab's engines |
| learn a topic | `teach <topic>` | a lesson a session from what you have read, with a quiz |
| know what to do next | `next` | where you stand, and the one thing to do next |
| see the process worked end to end | `init-example` | `liquid-golden-cross`, one strategy through every step, to read or run |

In Claude, type these with a slash, `/read`; anywhere else, ask for them by name. **It grows with
you**: it reads for your questions, speaks in your voice and keeps your rules, all written in its
own folder, where you can edit them. The package brings only hints, offered as options — never a
position to adopt.

**Lost at any point?** Type `next` in the folder you are in.

---

## For developers and advanced users

### Installing by hand

```bash
uv tool install apm-cli==0.29.0
uvx --from apm-cli==0.29.0 apm install -g KaxaNuk/KaxaNuk-Researcher --target claude
```

`--target codex`, `gemini`, `cursor` or another in place of `claude`; Claude Code receives
everything, and [`SETUP.md`](SETUP.md) says what the others miss. The skills are then in every
folder you open, so **a strategy installs nothing of its own**; `uvx --from apm-cli==0.29.0 apm
update -g` brings every new version. **APM stays at 0.29.0, and every command that runs it names
that version**: from 0.29.1 on, the install fails on Windows with `WinError 3` or `WinError 206`.
Never run `apm self-update`. Then, in a new session, `init-researcher Ada` makes the home and runs
the interview. [`SETUP.md`](SETUP.md) is the whole path, step by step.

### The path after the install

| | In | Run | It makes |
| --- | --- | --- | --- |
| 1 | anywhere | `init-researcher Ada` | the researcher's home, named after it, and then the interview: four short steps that write `RESEARCHER.md`, the agent and the researcher's skill, install them for your user and commit. The install in [`SETUP.md`](SETUP.md) runs this for you |
| 2 | the home | `init-strategy fcf-yield-quality` | your first strategy, one repository of its own, beside the home; its `SETUP.md` finishes the setup |
| 3 | the strategy | `objective` | the strategy's claims, before any paper — then the order of work, A to H, in the template's README, which the strategy's links to |

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

**The researcher is in every folder** once the interview has run: open your assistant in a
strategy's folder, or any other project's, and it is there, by name, on whichever assistant APM
deploys to. Add the home to the session — `claude --add-dir <the home>`, `/add-dir`, or the desktop
app's add-folder button — for it to read the library without asking each time. The home's
`AGENTS.md` says how, and what loads.

---

## The skills and commands

Every one that writes shows its plan first and waits for your go.

| Skill | What it does |
| --- | --- |
| `read` | reads sources into the library — `Sources/` into `Knowledge/` at home; in a strategy, once `OBJECTIVE.md` has claims, into notes beside the PDFs in its `Bibliotheca/`. A script extracts a PDF by chapter; you pick the chapters that serve your questions; one note per chapter read. It carries the reading map, `references/reading-map.md`, that `interview` proposes the first works from |
| `query <question>` | answers from the library — concept pages, then the notes they cite, then your `Philosophy/`, then the sources; every claim cited, gaps named |
| `init-researcher`, `init-strategy`, `init-example` | make a folder — your home, a strategy, or the worked example `liquid-golden-cross` to read or run — copied by a script, byte for byte, after a plan and your go, never from memory. A file a strategy made before template 0.10.0 lacks comes back from the template: `init-strategy`'s script with `--only <path>`, which never overwrites |
| `interview` | four short steps that make the researcher yours; writes `RESEARCHER.md`, the agent that makes it callable by name and the researcher's skill that puts it in every folder, installs them for your user, commits, and ends with a map of the home's folders. `init-researcher` runs it straight after making the home; `interview force` starts over |
| `next [strategy]` | where you stand — at home or in a strategy — and the one thing to do next, with the command or skill that does it; reads the folder, writes nothing |

| Command | What it does |
| --- | --- |
| `objective [strategy]` | drafts a strategy's `OBJECTIVE.md` — the idea and its claims — before any paper, then from the notes |
| `blueprint <N> [strategy]` | drafts `BLUEPRINT_N.md` — thesis, rules, predictions — every prediction citing a note or a measurement |
| `challenge <N> [strategy]` | checks a finished experiment against its own blueprint |
| `audit [deep]` | reviews the library — links, duplicates, index, orphans, frontmatter, stale installs |
| `refresh-index` | rebuilds `Knowledge/INDEX.md` from what is on disk |
| `refine <path>` | a voice-preserving editor pass over one of your `Philosophy/` files |
| `study [subject]` | works out an idea, a plan or a decision from your library and keeps it in `Studies/` — every claim linked to its note, anything from outside it marked as not checked; with no subject, lists your studies |
| `teach <topic>` | tutors you on a topic from your library, one lesson per session |
| `update [check]` | brings a new version into your home — `uvx --from apm-cli==0.29.0 apm update -g`, and what changed in the home's own files, shown as a diff |

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
| `paper-trading-gate` | step 7, graduation: the five criteria, how each is evidenced, the freeze, and the daily run and its record |

**The house rules**: `how-we-work` (where work lands, changelogs, versions) and `bloom-code-lint`
with the Bloom Code, PEP 8, test-writing and filesystem-boundaries instructions, which apply to
every Python project on the machine where the agent receives them (`SETUP.md` step 1).
`bloom-code-lint` is the check to run by hand.

**One agent**, deployed for your user with the skills: `blueprint-critic` reads a drafted
`BLUEPRINT_N.md` cold, before your go, against the strategy's `AGENTS.md`, `OBJECTIVE.md`, the
notes the draft cites and what the analyzer measured, and returns objections only — each with the
line and the evidence. It never writes and never proposes a thesis; you decide what stands.
`blueprint` hands it the draft before asking for your go, and you can ask for it by name.

---

## What it will not do

The researcher's part is **the hypothesis**, and it stops where the numbers start.

- **It computes no number.** Not a return, a Sharpe, a drawdown or an attribution: every number
  about a book comes from the engines the project names — in a strategy, the KaxaNuk Backtest
  Engine and Attribution Analysis. It quotes those numbers from `FINDINGS_N.md` and `RESULTS.md`,
  naming the file.
- **It does not write the record.** `JOURNAL_N.md`, `FINDINGS_N.md`, `RESULTS.md` and
  `CHANGELOG.md` belong to whoever ran the experiment; `challenge` may append one entry to
  `JOURNAL_N.md`, on your go, and nothing more.
- **It does not write `OBJECTIVE.md` before your words.** `objective` drafts the idea and its
  claims from what you tell it, before any paper is read; with nothing from you, there is nothing
  to draft.
- **It cites no source that has no note.** A source in a `BIBLIOGRAPHY.md` without a note is a lead,
  and nothing is claimed on its authority.

---

## What is in here

```
.apm/skills/          every skill: the researcher's, the Investment Lab's and the house rules'
.apm/prompts/         the commands
.apm/instructions/    the house style: Bloom Code, PEP 8, test writing, filesystem boundaries
.apm/agents/          the one agent, blueprint-critic
templates/strategy/   the KaxaNuk Strategy Template — the eight steps as folders; its README is the
                      process, and the order of work a strategy follows
templates/researcher/ the researcher's home, empty
examples/liquid-golden-cross/
                      one strategy worked through every folder of the template
SETUP.md              the install, step by step — what an assistant follows when you paste the URL
apm.yml               the package: what apm install reads; it depends on nothing
pyproject.toml        the ruff settings for the skills' scripts
AGENTS.md, CLAUDE.md  the rules for changing this repository
CHANGELOG.md          one entry per version
LICENSE               MIT
.gitignore            what apm install and Python write per machine
```

**What this repository owns, and what a copy owns.** This repository owns what is written once and
copied or installed everywhere; a copy owns what its owner writes in it. A strategy made from the
template is its owner's from the first commit and never merges back; the skills keep updating with
`uvx --from apm-cli==0.29.0 apm update -g`.

---

## Development

```bash
uvx ruff check .
(cd examples/liquid-golden-cross && uvx ruff check .)
uv run --no-project python .apm/skills/bloom-code-lint/scripts/bloom_code_check.py \
  .apm/skills/*/scripts examples/liquid-golden-cross
```

Ruff lints the skills' scripts, the worked example with its own settings, and the last command
checks the Bloom Code style of both. Each runs through `uv` alone: no Python of your own is needed.
They run on your machine before a commit; there is no CI, so nothing runs them for you. Nothing else
is automated: the template and the example are kept in step by hand, as `AGENTS.md` says.

To try a change to a skill, a command, an instruction or the agent, install the working tree at
project scope, from a short scratch folder, with the APM the package is pinned to — never `-g` of
the working tree:

```bash
mkdir -p D:/tmp/check
cd D:/tmp/check
uvx --from apm-cli==0.29.0 apm install "<path to this repository>" --target claude
```

with the path to your clone in place of the placeholder, and any short folder of your own in place
of `D:/tmp/check`. Open a new session in that folder. If the working tree carries ignored folders
deep enough to fail the install, copy the files `git ls-files` lists to a short folder and install
that instead.

**Before a release, do the same with the commit to be tagged.** It should deploy exactly 18 skills,
9 commands, 4 rules and 1 agent, with no warning. Then, if the release changes a skill, a command
or a script, walk the newcomer's path by hand in that folder — `init-researcher`, which runs
`interview`, then `next`, `init-strategy`, and `read` on one clipping — once in Spanish, and once
on an assistant with no question tool, such as Codex. Delete the folder afterwards. A newer APM is
adopted only when this install passes with it, on Windows.

`AGENTS.md` has the rules for changing this repository: work lands on `main`, and a release is
tagged `vX.Y.Z` there. `CHANGELOG.md` has one entry per version.

---

## Licence

MIT, see [`LICENSE`](LICENSE).
