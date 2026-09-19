# Setup

Everything needed to go from nothing to a researcher you can talk to. It is written so an agent —
Claude, Codex, Cursor — can follow it end to end when all it was told is *please help me install
`https://github.com/KaxaNuk/KaxaNuk-Researcher`*, and so a person can read it in two minutes.

**If the folder you are in already contains `RESEARCHER.md`, `AGENTS.md` and `.apm/`, you have the
repository:** check the two tools below, then skip to step 2.

## What you need first

Two tools. Python is **not** one of them — `uv` fetches what it needs itself.

| Tool | Windows | macOS and Linux |
| --- | --- | --- |
| [git](https://git-scm.com) | `winget install --id Git.Git -e` — or install GitHub Desktop, which brings it | `xcode-select --install` on macOS; your package manager on Linux |
| [uv](https://docs.astral.sh/uv/) | `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |

Open a **new** terminal after installing either, so it is on the path. `git --version` and
`uv --version` both answering is the whole check.

> **For the agent, before anything else.** If you were given only the URL, you are missing two
> things and must ask for the first: **the researcher's name** — what the user will call it, and the
> name of its folder, so `Luna`, not `KaxaNuk-Researcher` — and **where to put it**, which defaults
> to the folder you are in. Then decide the root by looking at that folder, and say which folder you
> chose:
>
> - it is **empty** → it is the root;
> - it already holds `RESEARCHER.md`, `AGENTS.md` and `.apm/` → the repository exists, go to step 2;
> - it holds `apm.yml`, `apm_modules/` or `.claude/` **without** those → **stop**: that is a wrapper
>   somebody prepared by hand, and the section below says why and what to delete;
> - it holds anything else → the root is `<name>/` inside it, which step 1 creates; say so.
>
> Every command from step 2 on runs **in the root**. Never a level above it.

---

## The rule: one folder is the researcher

Clone into one folder, open that folder, and run every command in it: nothing installed a level
above it, nothing nested a level below. What setup writes there — `apm_modules/`, `apm.lock.yaml`,
and `.claude/` or, for Codex, `.agents/` and `.codex/` — is ignored.

**The failure to avoid is a wrapper folder**: APM set up in an empty folder with the repository put
inside it. An agent opened at the wrapper never sees `RESEARCHER.md` or the skills. If you have that
layout, delete the wrapper's `apm.yml`, `apm.lock.yaml`, `apm_modules/` and `.claude/`, then move
the repository folder up and open it directly.

---

## Step 1 — Get the repository

**On Windows, clone somewhere short.** `D:\Research\...` is fine; a deep synced path such as
`C:\Users\<you>\OneDrive\Documents\Projects\...` is not. APM stages its downloads several levels
below the root, so a path that starts too deep fails part-way through with
`WinError 3: The system cannot find the path specified` — a real failure with a misleading message.

From the folder that will hold the researcher, with its name in place of `Luna`:

```bash
git clone https://github.com/KaxaNuk/KaxaNuk-Researcher.git Luna
```

If the root is an empty folder you are already in, clone into it instead — the `.` keeps git from
making another folder inside it:

```bash
git clone https://github.com/KaxaNuk/KaxaNuk-Researcher.git .
```

Then, from the root, rename the template's remote, so that `origin` is free for a repository of your
own and the template's updates still come with `git pull upstream main`:

```bash
git remote rename origin upstream
```

**Your library is private.** What you read, what the researcher writes and how you invest end up in
this folder. If you back it up on GitHub, make that repository **private**; `Sources/` keeps PDFs
out of git by default, and anything you would not want read does not go in the folder at all.

> **For the agent.** `git clone … .` refuses a non-empty directory. That is deliberate — it is what
> stops a wrapper folder from being created by accident. Go back to the root decision rather than
> around it.

---

## Step 2 — Install the researcher into your assistant

The researcher is two skills, eight commands and an agent, authored once in `.apm/`.
[APM](https://github.com/microsoft/apm), the Agent Package Manager, copies them into the folders
your assistant reads. Unlike a strategy's skills, **this step is not optional**: without it the
folder is a library with nobody to read it.

Install APM once per machine, through `uv`:

```bash
uv tool install apm-cli
```

If `apm --version` then says *command not found*, run `uv tool update-shell` and open a new
terminal. Then, from the root, with the target being the assistant you actually use:

```bash
apm install --target claude
```

```bash
apm install --target codex
```

Other targets — `cursor`, `copilot`, `gemini`, `opencode`, `windsurf` — are listed in `apm.yml`; a
bare `apm install` does all seven. What they write is ignored.

> **For the agent.** Run this without asking: installing the researcher is what you were asked to
> do. The target is the assistant you are — `claude` if you are Claude Code, `codex` if you are
> Codex. Say that the skills and commands become discoverable in a **new** session, not this one.

---

## Step 3 — Check that a PDF can be read

The `read` skill turns a PDF into its chapters with one script. It declares its own dependency, so
`uv` fetches it on first run and there is nothing to install. From the root:

```bash
uv run scripts/extract.py --help
```

It answering is the whole check.

---

## Step 4 — Let the researcher come with you into other folders

Optional, and only for Claude Code. When the researcher is invited into a strategy or another
project — `claude --add-dir <this folder>` — its skills come along on their own, but its
`CLAUDE.md`, `AGENTS.md` and `RESEARCHER.md` load only if this variable is set before the assistant
starts. Once per machine, on Windows:

```powershell
setx CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD 1
```

On macOS and Linux, `export CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` in the shell profile.
Then quit and reopen the assistant. *Checking an invitation* in [`AGENTS.md`](AGENTS.md) says how to
confirm it worked, and the fallback when it did not.

> **For the agent.** This changes the user's environment, so **ask first**, in one sentence, and
> take *no* or *later* as the answer it is.

---

## What "done" looks like

From the root:

```bash
git status
```

**It should be clean.** Everything the commands produced — `apm_modules/`, `apm.lock.yaml`,
`.claude/` — is ignored. **Anything showing up means something was written in the wrong place.**

Then open **this folder** — not a parent of it — in a **new** session of your assistant, and run
`researcher-init`: a short interview that names the researcher, writes `RESEARCHER.md` and makes it
callable by name. On Codex, which has no commands, ask it to *follow
`.apm/prompts/researcher-init.prompt.md`*.

> **For the agent — the hand-over.** Say the absolute path of the root, that it is the whole
> researcher and the folder to open, the target the skills were installed for and that they appear
> in a new session, whether the variable in step 4 was set, and that the next step is
> `researcher-init` in that new session. Then stop. The interview is a different request.

---

## Next

`researcher-init`, then a paper or a book into `Sources/` and `read`. The
[README](README.md) walks through both, and [`AGENTS.md`](AGENTS.md) says how the library is worked.
