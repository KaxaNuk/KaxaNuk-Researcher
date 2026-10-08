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
| `Philosophy/` | how you work, in `HOW-I-WORK.md`, and how you invest, in `HOW-I-INVEST.md` — your view, in your words; none until you or `philosophy` start one | write freely, or build them with `philosophy`; `refine` tidies them, diff first |
| `Philosophy/Evolution/` | one file per `philosophy` round: your answers that day, word for word | nothing to do — the record of how your view moved, never edited; it appears with your first round |
| `Sources/Papers/`, `Sources/Books/`, `Sources/Clippings/` | the PDFs and clippings you read | attach or name a file and the researcher copies it in, on your go — or drop it in yourself — then `read` |
| `Knowledge/` | the researcher's notes on what you read, with `INDEX.md` and `LOG.md` | written by `read`, on your go; ask it with `query` |
| `Studies/` | ideas, plans and decisions worked out from what you read | `study <subject>`; `study` alone lists them |
| `Lessons/` | lessons from `teach`, a folder per topic | appears with your first `teach <topic>` |
| `Briefs/` | your daily brief, one file a day — work, markets, portfolio — every figure quoted from a dated source, never advice | `brief setup` once — on the Claude desktop app it then comes on its schedule; `brief` writes today's now. Kept on this computer only, never in a saved version |
| `Portfolio/` | your holdings and the rules you hold them by, `holdings.csv` and `RULES.md` | `brief setup` starts both, empty, when you choose its portfolio part; you fill them. Kept on this computer only, never in a saved version |
| `AGENTS.md`, `CLAUDE.md` | the rules the researcher works by | nothing to do |
| `.apm/`, `apm.yml` | the researcher's agent and skill, installed for your user | nothing to do |
| `Extracts/` | text pulled out of the PDFs, for `read`; remade when needed, kept on this computer only | nothing to do |

**A copy off this computer.** Each go saves a dated version of what your researcher wrote, on this
computer only. For a private copy on GitHub, which a lost laptop does not take with it, say *keep a
copy*, or run `backup`; the PDFs, `Briefs/` and `Portfolio/` never go in it.

## The path

1. **Set up, once:** `interview`, if the install has not run it yet — two short questions about
   you, about three minutes: what you do and work on, what you'd like a hand with, why you are here
   and the researcher's voice. It writes `RESEARCHER.md`, the agent that makes your researcher
   callable by name and the skill that makes it present in every session, installs both for your
   user and saves a first version.
2. **Start learning.** Attach a PDF, or a text or Markdown file, in chat — or name one on your
   computer — and say *read it*: the researcher copies it into `Sources/Papers/`, `Sources/Books/`
   or `Sources/Clippings/` on your go. Save a Word document, an e-book or a web page as PDF first.
   The first `read` asks which question the source serves, in plain words, and keeps it as your
   question 1. For a book it asks which chapters serve your questions and reads only those; on your
   go it writes one note per chapter into `Knowledge/`. With nothing to read yet, `read` proposes a
   few works to start from.
3. **Write down how you work, or how you invest,** whenever you like: `philosophy`, a second
   interview, optional. It starts with why you do it, what you already believe and your rules — on
   investing, at your level, teaching as it asks — and adds what you typed, word for word, to
   `Philosophy/HOW-I-WORK.md` or `HOW-I-INVEST.md`, starting the file you lack, and your rules to
   `RESEARCHER.md`, on your go. Take it again after you have read, and see how your view moved.
4. **A daily brief,** if you want one: `brief setup` chooses the parts — your work, the markets you
   follow, your portfolio — the days and the time, and schedules it on the Claude desktop app;
   elsewhere `brief` writes the day's file when you run it. Each lands in `Briefs/`, every figure
   quoted from a dated source, never advice.
5. **Ask, and think things through.** `query <question>` answers from what you have read, every
   claim cited and every gap named; `study <subject>` works out an idea, a plan or a decision;
   `teach <topic>` gives a lesson a session.
6. **Start a strategy.** Read a finished one first: `init-example` copies `golden-flow` beside
   this folder — open `OBJECTIVE.md`, then `RESULTS.md`, then `Experiments/Experiment_1/`. Reading
   it needs nothing; running it needs a data provider's key, the Analytics Factory's files and the
   Lab's licences — its `SETUP.md` says how. Then `init-strategy <name>` makes your own, beside
   this folder too, from the KaxaNuk Strategy Template.

**Lost?** `next`, here or in a strategy, names the one next thing and the command for it — here,
for what you came for. **Stay current:** when a new version is out, your researcher says so in one
line, at most once a week; say `update` and it brings it — the package for every folder, and any
change to this home shown as a diff first. *Not now* waits a month; *stop reminding me* turns it
off. In Claude, type the commands with a slash, `/read`; anywhere else, ask for them by name.

## Working well with your researcher

- **One task per conversation**; start a new one when the subject changes.
- **Give it the file**, not a summary from memory: attach it, or say where it is.
- **Say *remember this*** when you want a rule kept; it goes in `RESEARCHER.md`, on your go — one
  about your holdings is yours to write, in `Portfolio/RULES.md`.
- **Ask it to argue the other side**, or what would change your mind.
- **Click the links**: every claim names its note, and a claim without one is a lead.
- **After an install or an update**, open a new conversation.

## The KaxaNuk Investment Lab

A strategy you build from here can use KaxaNuk's libraries. The Data Curator is open source and
free; its data provider's key comes from the provider. The Backtest Engine, Attribution Analysis and
Portfolio Construction — and the Data Refinery and the Data Analyzer when they ship — come together,
with their licences, in the KaxaNuk Investment Lab, which KaxaNuk sells; attribution also reads the
benchmark and factor model files of KaxaNuk's Analytics Factory, <https://www.kaxanuk.mx/analytics>.
Without the licences a strategy still runs up to its portfolios, and the rest says what is missing.
For a licence, access or those files, write to `lab@kaxanuk.mx`, saying which library and what it is
for, with *via KaxaNuk Researcher* in the subject — <https://www.kaxanuk.mx/lab> shows the Lab. To
report a problem with your researcher, write to the same address, with the versions it names when
you ask *which version are you?*

---

## In a strategy or another project

Open your assistant in the project's folder and call your researcher by name: it is there, and
reads this home when the work needs it. Add this folder to the session —
`claude --add-dir <this folder>`, `/add-dir` once inside, or the desktop app's add-folder button —
for it to read the library without asking each time. Work on a strategy lands in the strategy;
nothing comes back here unless you ask, and then as a source in `Sources/` that `read` files.

<details>
<summary><strong>The rules, loaded from the first line</strong></summary>

*Optional, and for Claude Code only.* Every skill reads `AGENTS.md` and `RESEARCHER.md` before it
works. To have them loaded from a session's first line in a strategy, Claude Code must read this
folder's `CLAUDE.md`, which imports both — and it reads `CLAUDE.md` from an added folder only when
this variable is in the environment before it starts. Set it once per machine, as a user variable,
then quit and reopen the assistant:

```bash
setx CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD 1
```

`export` it in your shell profile outside Windows; an `env` entry in `settings.json` is applied too
late for it. `/context` lists what loaded, under *Memory files*. Where the variable is not honoured
— the desktop app does not document it — a `CLAUDE.local.md` at the strategy's root holding one
line, this folder's `CLAUDE.md` by absolute path, `@D:/Research/Ada/CLAUDE.md`, loads it with the
strategy's own instructions. It is personal to the machine: add `CLAUDE.local.md` to the strategy's
`.gitignore`, and approve the external import the first time the assistant asks — declined, it
stays off.

</details>

## Growing your researcher

It grows four ways, each governed by a section of `AGENTS.md`:

1. **Knowledge of a tool or a project.** Put its documentation in `Sources/Clippings/` and run
   `read`, with a reading question that names it. *Joining other projects* says how a project's
   files reach `Sources/` and how they are cited.
2. **A repeatable procedure.** A skill or command of the home's own in `.apm/skills/<name>/` or
   `.apm/prompts/`, written as below, then
   `uvx --from apm-cli==0.33.0 apm install -g "<this folder>"` and a new session.
3. **What it reads for.** A line under *What you are reading for* in `RESEARCHER.md`, by hand or
   through `read`, which asks for your first. The paragraph after the folder table in *What each
   folder is, and who may write in it* says who writes that file.
4. **How it behaves.** Say *remember this*, anywhere, and your researcher adds the line under *How
   it speaks* or *Non-negotiables* in `RESEARCHER.md` on your go — or add it by hand; every skill
   and the agent read it first. The same paragraph governs it.

<details>
<summary><strong>Writing a skill or a command of your own (advanced)</strong></summary>

Only when you want a procedure of your own; nothing here is needed to use the researcher. Write it
the way KaxaNuk's own APM packages write theirs, under a name the package does not use:

- **A skill** is `.apm/skills/<name>/SKILL.md`: frontmatter `name`, matching the folder, a folded
  `description` that says when to use it and what it does not cover, and `metadata.version`; a
  body that says when it applies, then numbered steps, as `read` does. What it runs lives in its
  own `scripts/`, what it reads on demand in its own `references/`, named by its own directory.
- **A command** is one `.apm/prompts/<name>.prompt.md` with `description` and its `input` list, no
  `name` and no `metadata`: APM keeps only `description`, `input`, `allowed-tools`, `model` and
  `argument-hint` for a command, and warns on install for each key it drops. The body reads its
  inputs as `${input:name}`, which APM turns into the arguments each harness takes; the required
  input comes first and the optional ones after it, because an assistant binds them by position.
- **Frontmatter is the lossy part.** A harness takes the keys it knows and drops the rest — APM
  says which on install — and a dropped key is a rule that is not enforced: anything that must
  hold everywhere goes in the body or the description, not only in a key. A folded
  `description: >` keeps a colon from breaking the YAML; the agent's frontmatter, which APM does
  not rewrite, stays one line with no colon in it.
- **No instructions.** Nothing goes in `.apm/instructions/`: the house instructions are the
  package's, and one here would be rendered by `apm compile` over `AGENTS.md`, which is written by
  hand. With only skills, prompts and agents, `apm compile` leaves `AGENTS.md` and `CLAUDE.md`
  alone and writes a `GEMINI.md` that imports them, which git ignores.

</details>

<details>
<summary><strong>Installing and updating</strong></summary>

The skills and commands — `read`, `query`, `objective`, `blueprint` and the rest — are not in this
folder: they are installed once for your user and updated with
`uvx --from apm-cli==0.33.0 apm update -g`; `update`, run here, brings what changed in this home's
own files across. On a new machine, or after adding an assistant under `targets:` in
`~/.apm/apm.yml` and in this home's `apm.yml`, install this home yourself, once:

```bash
uvx --from apm-cli==0.33.0 apm install -g "<this folder>"
```

The home's own version in `apm.yml` is yours: `interview` sets it to 0.1.0, you bump it with each
entry you add to `CHANGELOG.md`, and `update` reads the *Brought to template* line there, never
this field. `CHANGELOG.md` holds the template's changelog, then this home's.

</details>

**Directionality:** `Sources/ → Extracts/ → Knowledge/ → Studies/, Lessons/`: studies and lessons
are built from the notes, and no note is ever built from a study. `Philosophy/` is cited, never
compiled into notes, so your judgement stays yours; its rounds in `Philosophy/Evolution/` are a
record of how your view moved, and the files you keep there, never a round, are what is cited as
your view. A brief is never cited: a figure in one enters the library only as a source in
`Sources/`.

---

## Licence

MIT, see [`LICENSE`](LICENSE).
