# A KaxaNuk researcher's home

This folder is a researcher's home: its library of what you have read, your own voice, your
studies, and the rules it works by. It was made by `init-researcher` from the KaxaNuk Researcher, in
[KaxaNuk-Researcher](https://github.com/KaxaNuk/KaxaNuk-Researcher), which says what the
researcher is and how to install it. Once `interview` has named your researcher, it proposes the
paragraph that replaces this one, on your go.

---

## Working with it

**The researcher is yours:** it grows with what you believe, and the package brings only hints,
offered as options, that make a complex idea simple — never a position to adopt.

**What you can use it for**, with a strategy or without one:

- **A library you can ask.** `read` a paper, a book or a clipping into `Knowledge/`, against your
  own questions; `query` it later, every answer cited and every gap named.
- **Your studies.** `study <subject>` works out an idea that is not a strategy yet, or a plan or a
  decision with no repository of its own, from what you have read, and keeps it in `Studies/`;
  `study` alone lists them.
- **Lessons.** `teach <topic>` tutors you from your library, one lesson a session.
- **Strategies.** `init-strategy <name>` starts one from the KaxaNuk Strategy Template, a
  repository of its own, with this home invited in.
- **Any other project.** Invite the researcher in, as *In a strategy or another project* below
  says: it objects on evidence from your library, under that project's own rules.
- **A researcher that fits you.** Its questions, its voice, its rules, the tools it knows and
  commands of your own — *Growing your researcher* below says the four moves.

**First, once.** Open your assistant in this folder, in a new session, and run `interview`: seven
questions, about ten minutes. It writes `RESEARCHER.md` and the agent that makes your researcher
callable by name, deploys the agent for the assistant you are using and commits what it wrote — you
answer, give your go, and allow the commands your assistant asks about. Then open a new session.
On a new machine, or for another assistant, deploy the agent yourself — `codex`, `cursor` or
`copilot` in place of `claude`:

```bash
apm install --target claude
```

The skills and commands — `read`, `query`, `objective`, `blueprint` and the rest — are not in this
folder: they are installed once for your user, `apm install -g`, and updated with `apm update -g`;
`update`, run here, brings what changed in this home's own files across. The home's own version in
`apm.yml` is yours: `interview` sets it to 0.1.0, you bump it with each entry you add to
`CHANGELOG.md`, and `update` reads the *Brought to template* line there, never this field.

**At home.** Drop a paper or a book into `Sources/` and run `read`. For a book the researcher shows
the table of contents and asks which chapters serve which of your questions; it reads only those,
shows the plan, waits for your go, and writes one note per chapter into `Knowledge/` — and the
concept pages those chapters argue, every claim citing its note. `query` answers from what is here.

**In a strategy or another project.** Open your assistant in the project's folder and add this one
to the session — `claude --add-dir <this folder>`, `/add-dir` once inside, or the desktop app's
add-folder button — so the researcher brings its library. For `CLAUDE.md`, `AGENTS.md` and
`RESEARCHER.md` to load with it, set this once per machine and reopen the assistant:

```bash
setx CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD 1
```

`export` it in your shell profile outside Windows. *Checking an invitation* in `AGENTS.md` says how
to confirm it loaded. Work on a strategy lands in the strategy; nothing comes back here unless you
ask, and then as a source in `Sources/` that `read` files.

**Lost?** Run `next`, here or in a strategy: it reads the folder and says what is done and the one
thing to do next.

**On Windows,** `git diff` prints a CRLF warning for files the researcher wrote; it is expected and
harmless, `.gitattributes` normalises on commit.

---

## Growing your researcher

The researcher grows four ways, each governed by a section of `AGENTS.md`:

1. **Knowledge of a tool or a project.** Put its documentation in `Sources/Clippings/` and run
   `read`, with a reading question that names it. *Joining other projects* says how a project's
   files reach `Sources/` and how they are cited.
2. **A repeatable procedure.** A skill or command of the home's own in `.apm/skills/<name>/` or
   `.apm/prompts/`, then `apm install --target <agent>` and a new session. *Where the skills, the
   commands and the agent live* says how one is written and where it deploys.
3. **What it reads for.** A line under *What you are reading for* in `RESEARCHER.md`. The
   paragraph after the folder table in *What each folder is, and who may write in it* says who
   writes that file.
4. **How it behaves.** A line by hand under *How it speaks* or *Non-negotiables* in
   `RESEARCHER.md`, which every skill and the agent read first. The same paragraph governs it.

`teach` tutors you from the library and `study` works out what you will do with it; you teach the
researcher by these four moves.

---

## What is in here

```
RESEARCHER.md    who the researcher is, and what you are reading for — written by interview
AGENTS.md        the library's rules: folders, conventions, strategies and projects, plan first
CLAUDE.md        imports AGENTS.md and RESEARCHER.md
CHANGELOG.md     the template's changelog, then this home's; update adds the version it brings
apm.yml          what apm install deploys: the agent, and any skill or command of this home's own

Sources/         what you read — Books/, Papers/, Clippings/. The researcher reads, never writes
Extracts/        text pulled out of the PDFs, one file per chapter; regenerable, gitignored
Knowledge/       notes by domain, a folder per book, concept pages; INDEX.md and LOG.md
Philosophy/      your voice. HOW-I-INVEST.md is the page to write it in; cited, never generated
Studies/         your studies: an idea, a plan or a decision, a file each; written by study
Lessons/         teach's lessons, a folder per topic; the first teach creates it
.apm/agents/     your researcher as a callable agent, written by interview
.apm/skills/, .apm/prompts/  your researcher's own skills and commands, if you write any
```

**Directionality:** `Sources/ → Extracts/ → Knowledge/ → Studies/, Lessons/`: studies and lessons
are built from the notes, and no note is ever built from a study. `Philosophy/` is cited, never
compiled into notes, so your judgement stays yours. Anything else you ask for here is answered in
chat, or as a page you can share, unless you keep it as a study; strategy work lives in the
strategy. The library is private to you: nothing in `Sources/` should
ever be pushed anywhere public, and the `.gitignore` keeps PDFs out by default. Clippings and the
notes read from them are committed with the home, so a home that holds a private project's
material stays a private repository.

---

## Licence

MIT, see [`LICENSE`](LICENSE).
