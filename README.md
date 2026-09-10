# KaxaNuk Researcher

**A research companion you name and teach.** It keeps a library of what you have read, knows the
KaxaNuk Investment Lab and the Research Process, and helps you write the hypothesis of every
investment strategy you build — with every claim pointing back to something you actually read.

One researcher per person, not per strategy. Your strategies live in their own repositories, copied
from the [KN Research Process template](https://github.com/KaxaNuk/KaxaNuk-Research-Process); the
researcher works in each strategy's `Bibliotheca/` — compiling its sources, writing its notes,
drafting its `OBJECTIVE.md` claims and its `BLUEPRINT_N.md` hypotheses — with your library as the
contrast. What it learns in a strategy stays there: it writes nothing back home unless you ask, so
one experiment never leaks into the researcher every strategy shares.

**There is almost no code here.** The researcher is a folder architecture, a set of skills and an
interview. The deterministic work — downloading data, computing signals, pricing a book, attributing
a return — is done by the Lab's libraries, which the researcher calls and never imitates.

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
   be spoken to, what is never allowed — writes `RESEARCHER.md`, the researcher's personality, and
   scaffolds any folder that is missing.
   
   ```bash
   /researcher-init
   ```

3. **Drop a paper into `Sources/` and run `/compile`.** The researcher asks why you added it,
   proposes how to file it, waits for your go, and writes it into `Knowledge/` with a link to
   everything it relates to.

4. **Invite it to a strategy.** Point at it from here — `/blueprint D:\Research\Golden-Flow 1` —
   or open your assistant in the strategy's folder and add this one to the session, with
   `claude --add-dir <this folder>` or `/add-dir` once inside; the skills come along. There, the
   strategy's `Bibliotheca/` is its library: `/compile` fills `Bibliotheca/Knowledge/` from the
   strategy's papers, `/note` writes the notes, and `/blueprint` drafts the hypothesis into
   `BLUEPRINT_N.md` with every prediction citing its note — each after a plan and your go. You
   review the diff and commit it, before the rule. Nothing is written here at home.

A skill is discoverable in a **new** session, never the one that installed it.

### Or add the researcher to a project you already have

The eleven skills are an [APM](https://github.com/microsoft/apm) package, so with the `apm` CLI
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
RESEARCHER.md         who the researcher is — name, owner, domains, voice, non-negotiables;
                      written by /researcher-init
AGENTS.md             the library's rules: what each folder is, who may write where, the skills
CLAUDE.md             two lines: @AGENTS.md and @RESEARCHER.md
CHANGELOG.md          every version of this repository, newest first
apm.yml               what this repository publishes, so the skills can be installed into a
                      project you already have. Nothing needs it to clone and run

Sources/              what you read: PDFs, papers, clippings. The researcher reads, never writes
  Books/                file by kind, and add your own kinds — the taxonomy is yours
  Papers/
  Notes/                clippings and transcripts you collected, never your own writing
Knowledge/            what the researcher compiled: one article per idea, grouped by domain
  INDEX.md              the one index of the library — read first, always
  LOG.md                append-only record of every compile, audit and refresh
Philosophy/           your voice: how you invest, what you believe. Read and cited, never edited
Projects/             what you asked for at home: lessons, anything in chat. Strategy work lives
                      in the strategy

.claude/skills/       the eleven skills below. Edit them here — Claude Code reads only this
.agents/skills/       the same eleven, mirrored: Copilot, Cursor, Codex, Gemini, OpenCode and
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
| `/compile` | files the sources into the library — `Sources/` into `Knowledge/` at home, a strategy's `Bibliotheca/` papers into its `Bibliotheca/Knowledge/` — asks why each source is there, plans, waits for your go, then writes; contradictions flagged, never overwritten |
| `/query <question>` | answers from the library first, then `Philosophy/`, then the sources; every claim cited; gaps named |
| `/note [strategy] <source>` | writes a source note into the strategy's `Bibliotheca/` in the KN convention, and its line in `BIBLIOGRAPHY.md` |
| `/objective [strategy]` | drafts the strategy's `OBJECTIVE.md` in place — the main idea and its claims — from its notes and your library |
| `/blueprint [strategy] <N>` | drafts `BLUEPRINT_N.md` in place — thesis, rules, predictions — with every prediction citing a note or a measurement |
| `/brainstorm [strategy] <N>` | appends a dated entry to `BRAINSTORMING_N.md` for the next thing to try |
| `/teach <topic>` | a multi-session tutor grounded in your library |
| `/audit` | read-only review of the library at hand: broken links, duplicates, stale index, orphans; `deep` adds contradictions |
| `/refine <path>` | a voice-preserving editor pass over one of your notes, diff first |
| `/refresh-index` | rebuilds the library's `INDEX.md` from what is on disk |

Questions about what your library says fire `query` on their own; the rest run when you name them.
Every one that writes shows its plan first and waits for your go.

In a strategy, the library skills work on that strategy's `Bibliotheca/` and the four strategy
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
