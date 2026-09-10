# KaxaNuk Researcher

**A research companion you name and teach.** It keeps a library of what you have read, knows the
KaxaNuk Investment Lab and the Research Process, and helps you write the hypothesis of every
investment strategy you build — with every claim pointing back to something you actually read.

One researcher per person, not per strategy. Your strategies live in their own repositories, copied
from the [KN Research Process template](https://github.com/KaxaNuk/KaxaNuk-Research-Process); the
researcher works in each strategy's `Bibliotheca/` — reading its sources into notes, drafting its
`OBJECTIVE.md` claims and its `BLUEPRINT_N.md` hypotheses — with your library as the contrast. What
it learns in a strategy stays there: it writes nothing back home unless you ask, so one experiment
never leaks into the researcher every strategy shares.

**There is almost no code here.** The researcher is a folder architecture, a set of skills, an
interview, and one script that turns a PDF into its chapters as text — extraction is deterministic,
so a script does it. The rest of the deterministic work — downloading data, computing signals,
pricing a book, attributing a return — is done by the Lab's libraries, which the researcher calls
and never imitates.

It is not tied to one assistant. The skills are authored once and built for Claude Code, Copilot,
Cursor, Codex, Gemini, OpenCode and Windsurf.

---

## Start

1. **Clone this repository under the name you give your researcher**, and open that folder in your
   agent:

   ```bash
   git clone https://github.com/KaxaNuk/KaxaNuk-Researcher.git Luna
   ```

   The skills are committed, so this works with nothing else installed.

2. **Run `/researcher-init`.** A short interview — who you are, what you invest in, how you want to
   be spoken to, what is never allowed, what you are reading for right now — writes
   `RESEARCHER.md`, the researcher's personality, and scaffolds any folder that is missing.
   
   ```bash
   /researcher-init
   ```

3. **Drop a paper or a book into `Sources/` and run `/read`.** For a book the researcher shows you
   its table of contents and asks which chapters serve which of your questions; it reads only
   those, proposes how to file them, waits for your go, and writes one note per chapter read into
   `Knowledge/`, linked to everything it relates to. The extraction is a script run with
   [`uv`](https://docs.astral.sh/uv/) — or `pip install pypdf` and plain `python`.

4. **Invite it to a strategy.** Point at it from here — `/blueprint D:\Research\Golden-Flow 1` —
   or open your assistant in the strategy's folder and add this one to the session, with
   `claude --add-dir <this folder>` or `/add-dir` once inside; the skills come along. There, the
   strategy's `Bibliotheca/` is its library: `/read` writes the notes beside the strategy's PDFs,
   each with its row in `BIBLIOGRAPHY.md`, and `/blueprint` drafts the hypothesis into
   `BLUEPRINT_N.md` with every prediction citing its note — each after a plan and your go. You
   review the diff and commit it, before the rule. Nothing is written here at home.

A skill is discoverable in a **new** session, never the one that installed it.

### Or add the researcher to a project you already have

The ten skills are an [APM](https://github.com/microsoft/apm) package, so with the `apm` CLI
installed — `pip install apm-cli`, or an installer from its page — they can be added beside
whatever else you are running:

```bash
apm install KaxaNuk/KaxaNuk-Researcher
```

Then run `/researcher-init`, which scaffolds `Sources/`, `Knowledge/`, `Philosophy/` and
`Projects/` wherever you ran it. If you would rather not use APM at all, `apm pack` turns this
repository into a plain plugin bundle — a `plugin.json` and the skills — that your agent can load
directly.

---

## What is in here

```
RESEARCHER.md         who the researcher is — name, owner, domains, voice, non-negotiables — and
                      what you are reading for; written by /researcher-init
AGENTS.md             the library's rules: what each folder is, who may write where, the skills
CLAUDE.md             two lines: @AGENTS.md and @RESEARCHER.md
CHANGELOG.md          every version of this repository, newest first
apm.yml               what this repository publishes, so the skills can be installed into a
                      project you already have. Nothing needs it to clone and run

Sources/              what you read: PDFs, papers, clippings. The researcher reads, never writes
  Books/                file by kind, and add your own kinds — the taxonomy is yours
  Papers/
  Clippings/            articles, transcripts and threads you collected, never your own writing
Extracts/             the text the script pulled out of your PDFs, one file per chapter;
                      regenerable, gitignored, never cited
Knowledge/            what the researcher read: one note per paper, one folder per book with a note
                      per chapter read, grouped by domain
  INDEX.md              the one index of the library — read first, always
  LOG.md                append-only record of every read, audit and refresh
Philosophy/           your voice: how you invest, what you believe. Read and cited, never edited
Projects/             what you asked for at home: lessons, anything in chat. Strategy work lives
                      in the strategy

.claude/skills/       the ten skills below. Edit them here — Claude Code reads only this
  read/scripts/         extract.py, the one script: a PDF's table of contents, and its
                        chapters as text
.agents/skills/       the same ten, mirrored: Copilot, Cursor, Codex, Gemini, OpenCode and
                      Windsurf read this one instead
```

**Directionality:** `Sources/ → Knowledge/ → Projects/`. `Philosophy/` is a side channel the
researcher cites but never generates from, so your judgement stays yours. Your library is
**private to you**: a person's clone is theirs, and nothing in `Sources/` should ever be pushed
anywhere public — the `.gitignore` keeps PDFs out by default. Anything you would not want read
does not go in the repository at all.

---

## The skills

Each one is a skill, so it works the same way on every harness in `apm.yml`. On those that support
slash commands — Claude Code, Cursor, Gemini, OpenCode, Windsurf — you also get it as `/name`.

| Skill | What it does |
| --- | --- |
| `/researcher-init` | the interview; writes `RESEARCHER.md` and scaffolds the folders |
| `/read` | reads the sources into the library — `Sources/` into `Knowledge/` at home; in a strategy, into notes beside the PDFs in its `Bibliotheca/`, each with its row in `BIBLIOGRAPHY.md`. A script extracts a PDF by chapter; the researcher shows you the table of contents, asks which chapters serve which of your questions, reads only those and writes one note per chapter read; plan, your go, then writes; contradictions flagged, never overwritten |
| `/query <question>` | answers from the library first, then `Philosophy/`, then the sources; every claim cited; gaps named |
| `/objective [strategy]` | drafts the strategy's `OBJECTIVE.md` in place — the main idea and its claims — from its notes and your library |
| `/blueprint [strategy] <N>` | drafts `BLUEPRINT_N.md` in place — thesis, rules, predictions — with every prediction citing a note or a measurement |
| `/brainstorm [strategy] <N>` | appends a dated entry to `BRAINSTORMING_N.md` for the next thing to try |
| `/teach <topic>` | a multi-session tutor grounded in your library |
| `/audit` | reviews the library at hand — broken links, duplicates, stale index, orphans, frontmatter; `deep` adds contradictions — and reports; one line in the log, never a fix on its own |
| `/refine <path>` | a voice-preserving editor pass over one of your `Philosophy/` files, diff first |
| `/refresh-index` | rebuilds the library's `INDEX.md` from what is on disk |

Questions about what your library says fire `query` on their own; the rest run when you name them.
Every one that writes shows its plan first and waits for your go.

In a strategy, the library skills work on that strategy's `Bibliotheca/` and the three strategy
skills write into its own files; the strategy's path can be left out when the session is open in
it. None of them writes here at home from there unless you ask for it by name.

They are yours to change. Edit a skill in `.claude/skills/`, then mirror it with
`cp -r .claude/skills/. .agents/skills/` so the other assistants get the same one. `/audit` tells
you if the two have drifted.

---

## How it fits with the rest of KaxaNuk

| | |
| --- | --- |
| [KaxaNuk-Research-Process](https://github.com/KaxaNuk/KaxaNuk-Research-Process) | the template every strategy is copied from — eight steps as folders, no code on `main`. Its `Bibliotheca/` is where the researcher works when invited |
| [KaxaNuk-APM](https://github.com/KaxaNuk/KaxaNuk-APM) | where KaxaNuk's packages will come from — the Data Curator's calculations, one skill per Lab module — once they teach research rather than linting. None is installed today |
| the Investment Lab | the platform that runs the deterministic parts, and — later — reads a strategy's `Bibliotheca/` to show what cites what |

---

## Credits and licence

MIT, see [`LICENSE`](LICENSE). The library architecture — sources compiled into a wiki with an
append-only log, the person's notes kept apart, plan-and-confirm before any write — adapts the
MIT-licensed *obsidian-vault-kit*; the notice is kept in `LICENSE`. This repository does not depend
on Obsidian or any viewer: the files are plain markdown, and the Investment Lab is where they will
be rendered.
