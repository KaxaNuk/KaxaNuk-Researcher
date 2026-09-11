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

**There is almost no code here.** The researcher is a folder architecture, a set of skills and
commands, an agent, an interview, and one script that turns a PDF into its chapters as text —
extraction is deterministic, so a script does it. The rest of the deterministic work — downloading
data, computing signals, pricing a book, attributing a return — is done by the Lab's libraries,
which the researcher calls and never imitates.

It is not tied to one assistant. Two skills, eight commands and one agent are authored once, in
`.apm/`, and `apm install` deploys them to Claude Code, Copilot, Cursor, Codex, Gemini, OpenCode or
Windsurf.

---

## Start

1. **Clone this repository under the name you give your researcher:**

   ```bash
   git clone https://github.com/KaxaNuk/KaxaNuk-Researcher.git Luna
   ```

2. **Install the skills and commands for your agent**, from inside that folder. The
   [APM](https://github.com/microsoft/apm) CLI is the one thing you need — `pip install apm-cli`,
   or an installer from its page:

   ```bash
   apm install --target claude
   ```

   `--target codex`, `cursor`, `copilot`, `gemini`, `opencode` or `windsurf` for the others; a
   bare `apm install` does all seven. It copies `.apm/` into your agent's own folders, which git
   ignores. Then open the folder in your agent — a skill is discoverable in a **new** session,
   never the one that installed it. Reading a PDF also needs [`uv`](https://docs.astral.sh/uv/),
   or `pip install pypdf`.

3. **Run `researcher-init`.** A short interview — who you are, what you invest in, how you want to
   be spoken to, what is never allowed, what you are reading for right now — writes
   `RESEARCHER.md`, the researcher's personality, scaffolds any folder that is missing, and writes
   the agent file that makes your researcher callable by name. Every question with options is a
   multiple choice, and when you have nothing to answer yet it proposes — the questions you might be
   reading for, drawn from what is already in `Sources/` — for you to pick or refuse. Run
   `apm install --target claude` once more afterwards to deploy the agent.

   ```bash
   researcher-init
   ```

4. **Drop a paper or a book into `Sources/` and run `read`.** For a book the researcher shows you
   its table of contents and asks which chapters serve which of your questions; it reads only
   those, proposes how to file them, waits for your go, and writes one note per chapter read into
   `Knowledge/`, linked to everything it relates to.

5. **Invite it to a strategy.** Point at it from here — `blueprint D:\Research\Golden-Flow 1` —
   or open your assistant in the strategy's folder and add this one to the session, with
   `claude --add-dir <this folder>` or `/add-dir` once inside; the skills come along. There, the
   strategy's `Bibliotheca/` is its library: `read` writes the notes beside the strategy's PDFs,
   each with its row in `BIBLIOGRAPHY.md`, and `blueprint` drafts the hypothesis into
   `BLUEPRINT_N.md` with every prediction citing its note — each after a plan and your go. You
   review the diff and commit it, before the rule. Nothing is written here at home.

### Or add the researcher to a project you already have

`.apm/` is an [APM](https://github.com/microsoft/apm) package, so the same skills and commands can
be installed beside whatever else you are running:

```bash
apm install KaxaNuk/KaxaNuk-Researcher --target claude
```

Then run `researcher-init`, which scaffolds `Sources/`, `Knowledge/`, `Philosophy/` and
`Projects/` wherever you ran it. If you would rather not use APM at all, `apm pack` turns this
repository into a plain plugin bundle — a `plugin.json`, the skills and the commands — that your
agent can load directly.

---

## What is in here

```
RESEARCHER.md         who the researcher is — name, owner, domains, voice, non-negotiables — and
                      what you are reading for; written by researcher-init
AGENTS.md             the library's rules: what each folder is, who may write where, the skills
CLAUDE.md             two lines: @AGENTS.md and @RESEARCHER.md
CHANGELOG.md          every version of this repository, newest first
apm.yml               what apm install reads here, and what this repository publishes so the
                      researcher can be installed into a project you already have

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
scripts/              extract.py, the one script: a PDF's table of contents, and its chapters as
                      text, one file per chapter
references/           note.md, the shape of every note the researcher writes

.apm/                 the researcher itself, the only copy of each part. apm install copies them
                      into your agent's folders, which git ignores
  skills/               the two the researcher reaches for on its own: read and query
  prompts/              the eight you start by name
  agents/               your researcher as a callable agent, written by researcher-init
```

**Directionality:** `Sources/ → Knowledge/ → Projects/`. `Philosophy/` is a side channel the
researcher cites but never generates from, so your judgement stays yours. Your library is
**private to you**: a person's clone is theirs, and nothing in `Sources/` should ever be pushed
anywhere public — the `.gitignore` keeps PDFs out by default. Anything you would not want read
does not go in the repository at all.

---

## The skills, the commands and the agent

Two are **skills** — capabilities the researcher reaches for on its own when the work calls for
them, and that you can also invoke by name. Eight are **commands** — tasks you start by name, with
arguments, each producing one thing. Both are authored once in `.apm/` and deployed by
`apm install`: skills to every harness in `apm.yml`, commands to every one but Codex, which has no
command primitive. On Codex, ask for a command by its file — *follow
`.apm/prompts/blueprint.prompt.md` for experiment 1*.

| Skill | What it does |
| --- | --- |
| `read` | reads the sources into the library — `Sources/` into `Knowledge/` at home; in a strategy, into notes beside the PDFs in its `Bibliotheca/`, each with its row in `BIBLIOGRAPHY.md`. A script extracts a PDF by chapter; the researcher shows you the table of contents, asks which chapters serve which of your questions, reads only those and writes one note per chapter read; plan, your go, then writes; contradictions flagged, never overwritten. Fires on its own when you ask to file or read a source |
| `query <question>` | answers from the library first, then `Philosophy/`, then the sources; every claim cited; gaps named. Fires on its own when you ask what your library says |

| Command | What it does |
| --- | --- |
| `researcher-init` | the interview; writes `RESEARCHER.md`, scaffolds the folders and writes the agent file |
| `objective [strategy]` | drafts the strategy's `OBJECTIVE.md` in place — the main idea and its claims — from its notes and your library |
| `blueprint [strategy] <N>` | drafts `BLUEPRINT_N.md` in place — thesis, rules, predictions — with every prediction citing a note or a measurement |
| `brainstorm [strategy] <N>` | appends a dated entry to `BRAINSTORMING_N.md` for the next thing to try |
| `teach <topic>` | a multi-session tutor grounded in your library |
| `audit` | reviews the library at hand — broken links, duplicates, stale index, orphans, frontmatter, stale installs; `deep` adds contradictions — and reports; one line in the log, never a fix on its own |
| `refine <path>` | a voice-preserving editor pass over one of your `Philosophy/` files, diff first |
| `refresh-index` | rebuilds `Knowledge/INDEX.md` at home from what is on disk; a strategy's `BIBLIOGRAPHY.md` is curated by hand |

Every one that writes shows its plan first and waits for your go.

In a strategy, the library skills work on that strategy's `Bibliotheca/`, and `objective`,
`blueprint` and `brainstorm` write into its own files; the strategy's path can be left out when
the session is open in it. None of them writes here at home from there unless you ask for it by
name.

### And the agent

`researcher-init` also writes `.apm/agents/<your researcher>.agent.md`, so the researcher is an
agent the harness can call by name rather than a way of configuring a session:

> ask Luna what we have read about momentum crashes

It carries its own tool boundary — read, search and the skills, and nothing that writes — and its
own short prompt, which points at `RESEARCHER.md` and `AGENTS.md` rather than copying them, so
there stays one source of truth. **It never writes**, and that is structural rather than a
preference: every skill or command that writes waits for your go, and an agent reporting back
cannot ask for one. When an answer needs a write it names the skill or command for you to run.

Claude Code, Copilot and Cursor enforce the tool list. Codex takes the agent but drops it, which is
why the rule is written into the prompt as well. Gemini and Windsurf have no agent primitive, so
there the researcher is its skills and commands, exactly as before.

They are yours to change. Edit a skill in `.apm/skills/`, a command in `.apm/prompts/` or the agent
in `.apm/agents/`, run `apm install --target <your agent>` again, and open a new session. `audit`
tells you if an installed copy has gone stale.

**Working on the skeleton itself.** This repository is the skeleton; your researcher is a clone of
it under its own name, and that clone versions everything — `RESEARCHER.md`, the agent,
`Knowledge/`. If you develop the skeleton in the same folder you use as your researcher, keep your
own files out of its commits with git's local, unshared ignores rather than `.gitignore`, which
every clone inherits: add `.apm/agents/`, `Knowledge/*/`, `Philosophy/*`, `Projects/*` and
`Sources/*/*` to `.git/info/exclude`, and mark the three templates the interview and the reads fill
in, so their local changes stay out of the index:

```bash
git update-index --skip-worktree RESEARCHER.md Knowledge/INDEX.md Knowledge/LOG.md
```

Undo it with `--no-skip-worktree` when a template itself has to change.

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
