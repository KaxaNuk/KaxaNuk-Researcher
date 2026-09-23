# A KaxaNuk researcher's home

This folder is a researcher's home: its library of what you have read, your own voice, and the
rules it works by. It was made by `init-researcher` from the KaxaNuk Researcher, in
[KaxaNuk-Researcher](https://github.com/KaxaNuk/KaxaNuk-Researcher), which says what the
researcher is and how to install it. Replace this paragraph with one about your researcher once
`researcher-init` has named it.

---

## Working with it

**First, once.** Open your assistant in this folder, in a new session, and run `researcher-init`: a
short interview that writes `RESEARCHER.md` and the agent file that makes your researcher callable
by name. Then deploy the agent for the assistant you use — `codex`, `cursor` or `copilot` in place
of `claude` — and open a new session:

```bash
apm install --target claude
```

The skills and commands — `read`, `query`, `objective`, `blueprint` and the rest — are not in this
folder: they are installed once for your user, `apm install -g`, and updated with `apm update -g`.

**At home.** Drop a paper or a book into `Sources/` and run `read`. For a book the researcher shows
the table of contents and asks which chapters serve which of your questions; it reads only those,
shows the plan, waits for your go, and writes one note per chapter into `Knowledge/` — and the
concept pages those chapters argue, every claim citing its note. `query` answers from what is here.

**In a strategy.** Open your assistant in the strategy's folder and add this one to the session —
`claude --add-dir <this folder>`, `/add-dir` once inside, or the desktop app's add-folder button —
so the researcher brings its library. For `CLAUDE.md`, `AGENTS.md` and `RESEARCHER.md` to load with
it, set this once per machine and reopen the assistant:

```bash
setx CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD 1
```

`export` it in your shell profile outside Windows. *Checking an invitation* in `AGENTS.md` says how
to confirm it loaded. Work on a strategy lands in the strategy; nothing comes back here unless you
ask.

**Lost?** Run `next`, here or in a strategy: it reads the folder and says what is done and the one
thing to do next.

---

## What is in here

```
RESEARCHER.md    who the researcher is, and what you are reading for — written by researcher-init
AGENTS.md        the library's rules: folders, conventions, strategies and projects, plan first
CLAUDE.md        imports AGENTS.md and RESEARCHER.md
CHANGELOG.md     the template's changelog, then this home's; update adds the version it brings
apm.yml          what apm install deploys here: the agent, from .apm/agents/

Sources/         what you read — Books/, Papers/, Clippings/. The researcher reads, never writes
Extracts/        text pulled out of the PDFs, one file per chapter; regenerable, gitignored
Knowledge/       notes by domain, a folder per book, concept pages; INDEX.md and LOG.md
Philosophy/      your voice. HOW-I-INVEST.md is the page to write it in; cited, never generated
Projects/        what you ask for at home — lessons from teach, anything asked in chat
.apm/agents/     your researcher as a callable agent, written by researcher-init
```

**Directionality:** `Sources/ → Extracts/ → Knowledge/ → Projects/`. `Philosophy/` is cited, never
compiled into notes, so your judgement stays yours. The library is private to you: nothing in
`Sources/` should ever be pushed anywhere public, and the `.gitignore` keeps PDFs out by default.

---

## Licence

MIT, see [`LICENSE`](LICENSE). The library architecture — sources compiled into a wiki with an
append-only log, the person's notes kept apart, plan-and-confirm before any write — adapts the
MIT-licensed *obsidian-vault-kit*; the notice is kept in `LICENSE`.
