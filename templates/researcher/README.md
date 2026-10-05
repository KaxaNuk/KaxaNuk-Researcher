# A KaxaNuk researcher's home

This folder is your researcher's home: the library of what you read, your own voice, your studies
and the rules it works by. It was made from the
[KaxaNuk Researcher](https://github.com/KaxaNuk/KaxaNuk-Researcher). Once `interview` has named
your researcher, it proposes a paragraph about it to replace this one, on your go.

---

## Your folders

| Folder or file | What it holds | What you do with it |
| --- | --- | --- |
| `RESEARCHER.md` | who the researcher is: your name, what you are here for, its voice, your rules, what you are reading for | edit it whenever you like — it is yours. Your first `read` adds your first reading question, on your go |
| `Philosophy/HOW-I-INVEST.md` | your view of investing, in your words | write freely, or build it with `philosophy`, at your level; `refine` tidies it, diff first |
| `Philosophy/Evolution/` | one file per `philosophy` round: your answers that day, word for word | nothing to do — the record of how your view moved, never edited; it appears with your first round |
| `Sources/Papers/`, `Sources/Books/`, `Sources/Clippings/` | the PDFs and clippings you read | drop a file in, then `read` |
| `Knowledge/` | the researcher's notes on what you read, with `INDEX.md` and `LOG.md` | written by `read`, on your go; ask it with `query` |
| `Studies/` | ideas, plans and decisions worked out from what you read | `study <subject>`; `study` alone lists them |
| `Lessons/` | lessons from `teach`, a folder per topic | appears with your first `teach <topic>` |
| `Briefs/` | your daily brief, one file a day — work, markets, portfolio — every figure quoted from a dated source, never advice | `brief setup` once — on the Claude desktop app it then comes on its schedule; `brief` writes today's now. Kept on this machine, never committed |
| `Portfolio/` | your holdings and the rules you hold them by, `holdings.csv` and `RULES.md` | `brief setup` starts both, empty, when you choose its portfolio part; you fill them. Kept on this machine, never committed |
| `AGENTS.md`, `CLAUDE.md` | the rules the researcher works by | nothing to do |
| `.apm/`, `apm.yml` | the researcher's agent and skill, installed for your user | nothing to do |
| `Extracts/` | text pulled out of the PDFs, for `read`; regenerable, never committed | nothing to do |

The library is private: nothing in `Sources/` should ever be pushed anywhere public, and the
`.gitignore` keeps PDFs out. Clippings and the notes read from them are committed with the home, so
a home that holds a private project's material stays a private repository. `Philosophy/` is
committed too, your rounds included: on a public remote, your goals and answers are public.
`Briefs/` and `Portfolio/` never leave this machine — the `.gitignore` keeps them out.

## Save a copy off this computer

This folder is a git repository. When the researcher commits for you — *Commit it for me*, after
a `philosophy` round, or the commit at the end of the interview — it saves a version **on this
computer only**: a broken or lost laptop takes your library with it. Learning a little git is worth
it, so your researcher is also kept somewhere else and can follow you to another computer:

1. Create an empty **private** repository on GitHub, or a service like it.
2. Connect this folder to it and send what you have — or ask your researcher to walk you through
   it:

   ```bash
   git remote add origin <the URL of your private repository>
   git push -u origin main
   ```

3. From then on, `git push` after a commit sends the new version too.

Keep that repository private: your sources, your notes and your answers in `Philosophy/` are in it.

## The path

1. **Set up, once:** `interview`, if the install has not run it yet — a few short questions about
   you, about three minutes: what you do, what you are here for, the researcher's voice and your
   rules. It writes `RESEARCHER.md`, the agent that makes your researcher callable by name and the
   skill that makes it present in every session, installs both for your user and commits.
2. **Start learning.** Drop a PDF, or a text or Markdown file, into `Sources/Papers/`,
   `Sources/Books/` or `Sources/Clippings/` and say *read it* — save a Word document, an e-book or a
   web page as PDF first. The first `read` asks which question the source serves,
   in plain words, and keeps it as your question 1. For a book it shows the table of contents and
   asks which chapters serve your questions; it reads only those, shows the plan, waits for your
   go, and writes one note per chapter into `Knowledge/`. With nothing to read yet, `read` proposes
   a few works to start from.
3. **Write down how you invest,** whenever you like: `philosophy`, a second interview, optional and
   pitched at what you already know. It starts with why you invest and what you already believe,
   teaches as it asks, and adds what you typed to `Philosophy/HOW-I-INVEST.md`, word for word, on
   your go. Take it again after you have read, and see how your view moved.
4. **A daily brief,** if you want one: `brief setup` chooses the parts — your work, the markets you
   follow, your portfolio — the days and the time, and schedules it on the Claude desktop app;
   elsewhere `brief` writes the day's file when you run it. Each lands in `Briefs/`, every figure
   quoted from a dated source, never advice.
5. **Ask, and think things through.** `query <question>` answers from what you have read, every
   claim cited and every gap named; `study <subject>` works out an idea, a plan or a decision;
   `teach <topic>` gives a lesson a session.
6. **Start a strategy.** `init-strategy <name>` makes one beside this folder, from the KaxaNuk
   Strategy Template; the researcher is there when you open it.

**Lost?** `next`, here or in a strategy, says what is done and the one thing to do next. **Stay
current:** `update` brings new skills and new versions of the researcher — it runs the package's
update for you and shows any change to your home as a diff first. In Claude, type these with a
slash, `/read`; anywhere else, ask for them by name.

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
3. **What it reads for.** A line under *What you are reading for* in `RESEARCHER.md`, by hand or
   through `read`, which asks for your first. The paragraph after the folder table in *What each
   folder is, and who may write in it* says who writes that file.
4. **How it behaves.** A line by hand under *How it speaks* or *Non-negotiables* in
   `RESEARCHER.md`, which every skill and the agent read first. The same paragraph governs it.

## Installing and updating

The skills and commands — `read`, `query`, `objective`, `blueprint` and the rest — are not in this
folder: they are installed once for your user and updated with
`uvx --from apm-cli==0.29.0 apm update -g`; `update`, run here, brings what changed in this home's
own files across. On a new machine, or after adding an assistant under `targets:` in
`~/.apm/apm.yml`, install this home yourself, once:

```bash
uvx --from apm-cli==0.29.0 apm install -g "<this folder>"
```

The home's own version in `apm.yml` is yours: `interview` sets it to 0.1.0, you bump it with each
entry you add to `CHANGELOG.md`, and `update` reads the *Brought to template* line there, never
this field. `CHANGELOG.md` holds the template's changelog, then this home's.

**Directionality:** `Sources/ → Extracts/ → Knowledge/ → Studies/, Lessons/`: studies and lessons
are built from the notes, and no note is ever built from a study. `Philosophy/` is cited, never
compiled into notes, so your judgement stays yours; its rounds in `Philosophy/Evolution/` are a
record of how your view moved, and `HOW-I-INVEST.md`, never a round, is what is cited as your
view. A brief is never cited: a figure in one enters the library only as a source in `Sources/`.

**On Windows,** `git diff` prints a CRLF warning for files the researcher wrote; it is expected and
harmless, `.gitattributes` normalises on commit.

---

## Licence

MIT, see [`LICENSE`](LICENSE).
