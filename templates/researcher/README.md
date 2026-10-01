# A KaxaNuk researcher's home

This folder is your researcher's home: the library of what you read, your own voice, your studies
and the rules it works by. It was made from the
[KaxaNuk Researcher](https://github.com/KaxaNuk/KaxaNuk-Researcher). Once `interview` has named
your researcher, it proposes a paragraph about it to replace this one, on your go.

---

## Your folders

| Folder or file | What it holds | What you do with it |
| --- | --- | --- |
| `RESEARCHER.md` | who the researcher is: your name, its voice, your rules, what you are reading for | edit it whenever you like — it is yours. Add what the interview did not ask: your view as a sentence a test could answer, how long its edge might last, what would change your mind |
| `Philosophy/HOW-I-INVEST.md` | your own view of markets, in your words | write in it freely; the researcher reads and cites it, and never writes in it. `refine` tidies it, diff first |
| `Sources/Papers/`, `Sources/Books/`, `Sources/Clippings/` | the PDFs and clippings you read | drop a file in, then `read` |
| `Knowledge/` | the researcher's notes on what you read, with `INDEX.md` and `LOG.md` | written by `read`, on your go; ask it with `query` |
| `Studies/` | ideas, plans and decisions worked out from what you read | `study <subject>`; `study` alone lists them |
| `Lessons/` | lessons from `teach`, a folder per topic | appears with your first `teach <topic>` |
| `AGENTS.md`, `CLAUDE.md` | the rules the researcher works by | nothing to do |
| `.apm/`, `apm.yml` | the researcher's agent and skill, installed for your user | nothing to do |
| `Extracts/` | text pulled out of the PDFs, for `read`; regenerable, never committed | nothing to do |

The library is private: nothing in `Sources/` should ever be pushed anywhere public, and the
`.gitignore` keeps PDFs out. Clippings and the notes read from them are committed with the home, so
a home that holds a private project's material stays a private repository.

## First things to do

1. **First, once:** `interview`, if the install has not run it yet — four short steps, about five
   minutes. It writes `RESEARCHER.md`, the agent that makes your researcher callable by name and
   the skill that makes it present in every session, installs both for your user and commits.
2. **Read something.** Drop a paper or a book into `Sources/` and run `read`. For a book it shows
   the table of contents and asks which chapters serve which of your questions; it reads only
   those, shows the plan, waits for your go, and writes one note per chapter into `Knowledge/`.
3. **Ask.** `query <question>` answers from what you have read, every claim cited and every gap
   named.
4. **Think something through.** `study <subject>` for an idea that is not a strategy yet, or a
   plan or a decision; `teach <topic>` for a lesson a session.
5. **Start a strategy.** `init-strategy <name>` makes one beside this folder, from the KaxaNuk
   Strategy Template; the researcher is there when you open it.

**Lost?** `next`, here or in a strategy, says what is done and the one thing to do next. In Claude,
type these with a slash, `/read`; anywhere else, ask for them by name.

---

## In a strategy or another project

Open your assistant in the project's folder: the researcher is there, and reads this home when the
work needs it. Add this folder to the session — `claude --add-dir <this folder>`, `/add-dir` once
inside, or the desktop app's add-folder button — for it to read the library without asking each
time. For `CLAUDE.md`, `AGENTS.md` and `RESEARCHER.md` to load in full from the first line, set
this once per machine and reopen the assistant:

```bash
setx CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD 1
```

`export` it in your shell profile outside Windows. *The researcher's home* in `AGENTS.md` says how
to confirm it loaded. Work on a strategy lands in the strategy; nothing comes back here unless you
ask, and then as a source in `Sources/` that `read` files.

## Growing your researcher

It grows four ways, each governed by a section of `AGENTS.md`:

1. **Knowledge of a tool or a project.** Put its documentation in `Sources/Clippings/` and run
   `read`, with a reading question that names it. *Joining other projects* says how a project's
   files reach `Sources/` and how they are cited.
2. **A repeatable procedure.** A skill or command of the home's own in `.apm/skills/<name>/` or
   `.apm/prompts/`, then `apm install -g "<this folder>"` and a new session. *Where the skills, the
   commands and the agent live* says how one is written and where it deploys.
3. **What it reads for.** A line under *What you are reading for* in `RESEARCHER.md`. The
   paragraph after the folder table in *What each folder is, and who may write in it* says who
   writes that file.
4. **How it behaves.** A line by hand under *How it speaks* or *Non-negotiables* in
   `RESEARCHER.md`, which every skill and the agent read first. The same paragraph governs it.

## Installing and updating

The skills and commands — `read`, `query`, `objective`, `blueprint` and the rest — are not in this
folder: they are installed once for your user and updated with
`uvx --from apm-cli==0.32.0 apm update -g`; `update`, run here, brings what changed in this home's
own files across. On a new machine, or after adding an assistant under `targets:` in
`~/.apm/apm.yml`, install this home yourself, once:

```bash
uvx --from apm-cli==0.32.0 apm install -g "<this folder>"
```

The home's own version in `apm.yml` is yours: `interview` sets it to 0.1.0, you bump it with each
entry you add to `CHANGELOG.md`, and `update` reads the *Brought to template* line there, never
this field. `CHANGELOG.md` holds the template's changelog, then this home's.

**Directionality:** `Sources/ → Extracts/ → Knowledge/ → Studies/, Lessons/`: studies and lessons
are built from the notes, and no note is ever built from a study. `Philosophy/` is cited, never
compiled into notes, so your judgement stays yours.

**On Windows,** `git diff` prints a CRLF warning for files the researcher wrote; it is expected and
harmless, `.gitattributes` normalises on commit.

---

## Licence

MIT, see [`LICENSE`](LICENSE).
