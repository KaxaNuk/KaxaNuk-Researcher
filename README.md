# KaxaNuk Researcher

**A research companion you name and teach.** It keeps a library of what you have read, knows the
KaxaNuk Investment Lab and the Research Process, and helps you write the hypothesis of every
investment strategy you build — with every claim pointing back to something you actually read.

One researcher per person, not per strategy. Your strategies live in their own repositories, copied
from the [KN Research Process template](https://github.com/KaxaNuk/KaxaNuk-Research-Process); the
researcher reads each strategy's `Bibliotheca/` and drafts its `OBJECTIVE.md` claims and its
`BLUEPRINT_N.md` hypotheses from those notes. It never writes into a strategy repository uninvited.

**There is almost no code here.** The researcher is a folder architecture, a set of commands and an
interview. The deterministic work — downloading data, computing signals, pricing a book, attributing
a return — is done by the Lab's libraries, which the researcher calls and never imitates.

---

## Start

1. **Clone this repository under the name you give your researcher**, and open that folder in
   Claude Code:

   ```bash
   git clone https://github.com/KaxaNuk/KaxaNuk-Researcher.git Luna
   ```

2. **Run `/researcher-init`.** A short interview — who you are, what you invest in, how you want to
   be spoken to, what is never allowed — writes `RESEARCHER.md`, the researcher's personality. It
   also offers to install KaxaNuk's core knowledge, the APM packages that teach the KN process and
   each Lab module (`pip install apm-cli` first, or say yes and it does it).

3. **Drop a paper into `Sources/` and run `/compile`.** The researcher proposes how to file it,
   waits for your go, and writes it into `Library/` with a link to everything it relates to.

4. **Point it at a strategy.** `/blueprint <path to a strategy repo> 1` drafts the first
   blueprint's thesis and predictions from that strategy's `Bibliotheca/` and your library — every
   prediction cites its note — into `Output/<strategy>/`. You copy it in, edit it, and commit it
   before the rule.

Skills installed by APM are discoverable in a **new** session.

---

## What is in here

```
RESEARCHER.md         who the researcher is — name, owner, domains, voice, non-negotiables;
                      written by /researcher-init
AGENTS.md             the library's rules: what each folder is, who may write where, the commands
CLAUDE.md             two lines: @AGENTS.md and @RESEARCHER.md
CHANGELOG.md          every version of this repository, newest first
apm.yml               the KaxaNuk packages the researcher learns from; `apm install` pulls them

Sources/              what you read: PDFs, papers, clippings. The researcher reads, never writes
Library/              what the researcher compiled: one article per idea, grouped by domain
  INDEX.md              the one index of the library — read first, always
  LOG.md                append-only record of every compile, audit and refresh
Notes/                your voice: how you invest, what you believe. Read and cited, never edited
  Private/              never read without your explicit permission
Output/               what you asked for: source notes, objective and blueprint drafts, lessons

.claude/commands/     the commands below
.claude/skills/       library-query, and whatever APM installs beside it
```

**Directionality:** `Sources/ → Library/ → Output/`. `Notes/` is a side channel the researcher
cites but never generates from, so your judgement stays yours. Your library is **private to you**:
a person's clone is theirs, and nothing in `Sources/` or `Notes/Private/` should ever be pushed
anywhere public — the `.gitignore` keeps PDFs and private notes out by default.

---

## The commands

| Command | What it does |
| --- | --- |
| `/researcher-init` | the interview; writes `RESEARCHER.md`, scaffolds the folders, offers to install the KaxaNuk packages |
| `/compile` | files what is in `Sources/` into `Library/` — plan first, your go, then write; contradictions flagged, never overwritten |
| `/query <question>` | answers from `Library/` first, then `Notes/`, then `Sources/`; every claim cited; gaps named |
| `/note <strategy> <source>` | writes a source note for a strategy's `Bibliotheca/` in the KN convention, to `Output/` |
| `/objective <strategy>` | drafts the strategy's `OBJECTIVE.md` — the main idea and its claims — from its notes and your library |
| `/blueprint <strategy> <N>` | drafts `BLUEPRINT_N.md` — thesis, rules, predictions — with every prediction citing a note or a measurement |
| `/brainstorm <strategy> <N>` | drafts a dated `BRAINSTORMING_N.md` entry for the next thing to try |
| `/teach <topic>` | a multi-session tutor grounded in your library |
| `/audit` | read-only review of the library: broken links, duplicates, stale index, orphans; `deep` adds contradictions |
| `/refine <path>` | a voice-preserving editor pass over one of your notes, diff first |
| `/refresh-index` | rebuilds `Library/INDEX.md` from what is on disk |

Questions about what your library says fire the `library-query` skill on their own.

---

## How it fits with the rest of KaxaNuk

| | |
| --- | --- |
| [KaxaNuk-Research-Process](https://github.com/KaxaNuk/KaxaNuk-Research-Process) | the template every strategy is copied from — eight steps as folders, no code on `main` |
| [KaxaNuk-APM](https://github.com/KaxaNuk/KaxaNuk-APM) | the packages the researcher learns from: the process, the Data Curator's calculations, one skill per Lab module as they land |
| the Investment Lab | the platform that runs the deterministic parts, and — later — reads a strategy's `Bibliotheca/` to show what cites what |

---

## Credits and licence

MIT, see [`LICENSE`](LICENSE). The library architecture — sources compiled into a wiki with an
append-only log, the person's notes kept apart, plan-and-confirm before any write — adapts the
MIT-licensed *obsidian-vault-kit*; the notice is kept in `LICENSE`. This repository does not depend
on Obsidian or any viewer: the files are plain markdown, and the Investment Lab is where they will
be rendered.
