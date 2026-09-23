# Setup

Everything needed to go from nothing to a researcher you can talk to and a first strategy. It is
written so an agent — Claude, Codex, Cursor — can follow it end to end when all it was told is
*please help me install this repo: `https://github.com/KaxaNuk/KaxaNuk-Researcher`*, and so a
person can read it in two minutes.

**Nothing is cloned.** This repository is a package: it is installed once for your user, and its
commands then make every folder you need.

## What you need first

Two tools. Python is **not** one of them — `uv` fetches what it needs itself.

| Tool | Windows | macOS and Linux |
| --- | --- | --- |
| [git](https://git-scm.com) | `winget install --id Git.Git -e` — or install GitHub Desktop, which brings it | `xcode-select --install` on macOS; your package manager on Linux |
| [uv](https://docs.astral.sh/uv/) | `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |

Open a **new** terminal after installing either, so it is on the path. `git --version` and
`uv --version` both answering is the whole check.

Then tell git who you are, once, if you never have: every folder the commands make starts as a git
repository with a first commit, and the commit stops until git has a name and an email.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

## Step 1 — Install the package, once per machine

```bash
uv tool install apm-cli
```

If `apm --version` then says *command not found*, run `uv tool update-shell` and open a new
terminal. Then, with the target being the assistant you actually use — `claude`, `codex`, `cursor`,
`copilot`, `gemini`, `opencode` or `windsurf`:

```bash
apm install -g KaxaNuk/KaxaNuk-Researcher --target claude
```

That installs the researcher's skills and commands and, with them, every KaxaNuk Investment Lab
skill, for your user: every folder you open has them, and no folder installs anything of its own.

**Claude Code receives all of it:** the skills, the commands and the four instructions — Bloom
Code, PEP 8, test writing and filesystem boundaries. The instructions land in `~/.claude/rules/`,
so they apply to every Python project you open on that machine, not only a strategy. Copilot
receives the same, its instructions merged into `~/.copilot/copilot-instructions.md`. Cursor,
Gemini, OpenCode and Windsurf get the skills and the commands but not the instructions. Codex gets
the skills only: no instructions and no commands, so there a command is run by naming its file in
the package. For `interview` in step 2, ask Codex to *follow
`~/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/prompts/interview.prompt.md`*.

**On Windows, if the install fails with *checkout failed* or `WinError 3`,** a path went past
Windows' 260-character limit. Let git use long paths, once, then install again:

```bash
git config --global core.longpaths true
```

> **For the agent.** Run both without asking: installing is what you were asked to do. The target
> is the assistant you are. It may be run from any folder — `-g` writes to the user's home, never to
> the folder you are in. Then say the one thing that matters: **the skills appear in a new session,
> not this one.** The remaining steps happen there.

**What "done" looks like:** for Claude Code, `~/.claude/skills/` holds `init-researcher`,
`init-strategy`, `init-example`, `read` and `query` among others, and `~/.claude/commands/` holds
`interview.md` and `next.md`.

---

## Step 2 — Make your researcher, once per person

In a **new** session of your assistant, opened in the folder that should hold your work — short on
Windows, `D:\Research`, never a deep synced path such as `C:\Users\<you>\OneDrive\...`:

```text
init-researcher Ada
```

with the name you will call it. It shows a plan, waits for your go, and makes `Ada/` — the
researcher's home — as a git repository. Open **that folder** in a new session and run:

```text
interview
```

a short interview — seven questions, in your language — that writes `RESEARCHER.md` and the agent
that makes your researcher callable by name. Then `apm install --target claude` in that folder,
once — `codex`, `cursor` or `copilot` in its place; Gemini, OpenCode and Windsurf take no agent,
and the researcher there is its skills and commands — deploys the agent.

> **For the agent.** If a commit fails for want of a git identity, ask the user for the name and
> email — never invent them — and set them in that repository only. One researcher per person: if a
> home already exists, say where it is and do not make a second.

**What "done" looks like:** `RESEARCHER.md` with no angle-bracketed slot left,
`.apm/agents/<slug>.agent.md`, `.claude/agents/<slug>.md` after the install, a clean `git status`,
and a private remote if you want a backup. On Windows, `git diff` prints a CRLF warning for the
files the researcher wrote; it is expected and harmless — `.gitattributes` normalises them on
commit.

---

## Step 3 — Make a strategy, once per strategy

From your home, in a new session:

```text
init-strategy fcf-yield-quality
```

It makes `fcf-yield-quality/` beside the home — `D:\Research\fcf-yield-quality`, for example — from
the KaxaNuk Strategy Template, as a git repository with its first commit. Open that folder in a new
session; its own `SETUP.md` builds the environment and the keys, and its `README.md` says what to
fill in, in order — `OBJECTIVE.md` first. To bring your researcher's library along, add its home to
the session: `claude --add-dir <the home>`; for its identity to load with it, follow *In a strategy
or another project* in the home's README.

To see a finished strategy first:

```text
init-example
```

---

## Updating

```bash
apm update -g
```

brings every new version — of the researcher and of the Lab's skills — to every folder at once.
Then open a new session.

APM's own reference, for any error it prints: <https://microsoft.github.io/apm/llms.txt>.
