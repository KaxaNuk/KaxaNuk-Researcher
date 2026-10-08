# Setup

From nothing to a researcher you can talk to, in one conversation. This file is written for the
assistant — Claude, Codex, Gemini, Cursor — that was told only *please help me install this repo:
`https://github.com/KaxaNuk/KaxaNuk-Researcher`*. A person can read it in two minutes, but does not
need to: the assistant runs every command.

> **For the agent, read this first.**
>
> - **Ask the language before anything else**, in Spanish and English together — *¿En qué idioma
>   prefieres que hablemos? / Which language would you like to use?* — *Español*, *English*, or
>   another. From then on every message, question and explanation is in that language.
> - **Never ask whether to install.** The line the user pasted is the go: once the language is
>   chosen, install what is missing and the package, and go straight on, saying in one line what
>   each step does. Their assistant's own prompt to allow a command is the only thing they answer.
> - **The user may never have used a terminal.** Plain words, one question at a time, and you run
>   every command yourself; never ask them to type one. Say in one sentence what each step does,
>   and that their assistant may ask them to allow a command — allowing it is all they do.
> - **One conversation, start to finish.** Steps 1 to 6 run here, one after the other, stopping
>   only for the user's answers. The skills installed in step 2 appear only in a new session, so
>   steps 3 to 6 follow the package's files by their installed path, as the table below gives.
> - **Nothing is cloned.** This repository is a package: it is installed once for the user, and
>   its files then make every folder they need.

**The files you follow**, once step 2 has installed the package. `~` is the user's home folder —
`$HOME` in a shell, `C:\Users\<user>` on Windows — and the paths are the same on every assistant:

| For | Follow or run |
| --- | --- |
| steps 3 and 4, the researcher's home | `~/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/skills/init-researcher/SKILL.md` |
| the copy it makes | `~/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/skills/init-strategy/scripts/scaffold.py` |
| step 5, the interview | `~/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/skills/interview/SKILL.md` |
| step 6, `read`, only if the user brings a document now | `~/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/skills/read/SKILL.md` |
| step 6, `philosophy`, only if the user takes it now | `~/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/skills/philosophy/SKILL.md` |
| step 6, `init-example`, only if the user asks for the worked example now | `~/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/skills/init-example/SKILL.md` |
| step 6, `study`, only if the user starts the study now | `~/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/prompts/study.prompt.md` |

---

## Step 0 — The language

Ask it, as the box above says. That is the whole step.

## Step 1 — Two tools, and a name for git

Two tools. Python is **not** one of them — `uv` fetches what it needs itself. Check both with
`git --version` and `uv --version`, and install whichever is missing, without asking:

| Tool | Windows | macOS and Linux |
| --- | --- | --- |
| [git](https://git-scm.com) | `winget install --id Git.Git -e --accept-source-agreements --accept-package-agreements` | `xcode-select --install` on macOS; the package manager on Linux |
| [uv](https://docs.astral.sh/uv/) | `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |

On macOS, `xcode-select --install` opens a dialog: ask the user to click *Install* and to say when
it has finished; `xcode-select -p` printing a folder confirms it. A tool just installed is not on
this shell's path yet, so call it by its full path for the rest of the conversation: `uv` and `uvx`
in `$HOME/.local/bin/` — in PowerShell, `& "$HOME/.local/bin/uv"` — and git at
`C:\Program Files\Git\cmd\git.exe` on Windows. A command that runs git itself, APM and
`scaffold.py` among them, finds it when `C:\Program Files\Git\cmd` is put first on the path in
that same command.

Every folder the researcher makes keeps dated versions of its files, each signed with a name and
an email. If `git config --global user.name` prints nothing, ask the user for both in plain words —
*a name and an email to sign the versions your researcher saves* — **never invent them**, and set
them:

```bash
git config --global user.name "<their name>"
git config --global user.email "<their email>"
```

## Step 2 — Install the package

```bash
uv tool install apm-cli==0.33.0
uvx --from apm-cli==0.33.0 apm install -g KaxaNuk/KaxaNuk-Researcher --target <the assistant you are>
```

The target is the assistant you are: `claude`, `codex`, `gemini`, `cursor`, `copilot`, `opencode`
or `windsurf`. Run both without asking: installing is what you were asked to do. `-g` installs for
the user, whatever folder you are in. Every command that runs APM names `apm-cli==0.33.0` itself;
*Troubleshooting* below says why, and what to do if the install fails. Tell the user in one line
that the researcher is installed, and go straight on.

## Step 3 — The researcher's name, and where it lives

Follow `init-researcher` from its installed path, from its step 2, with the language already
chosen. Its own questions take the name, then the place and the go in one.

## Step 4 — Make the home

`init-researcher` goes on, on that go: it skips its update — the package was installed a minute
ago — and copies the researcher's home with `scaffold.py`, its first version saved.

## Step 5 — The interview

Follow `interview` from its installed path, in the same conversation, with the new folder as the
home: two questions about the user — what they do and work on, at work and on their own, what
they'd like a hand with, then the researcher's voice and why they are here — in the user's
language; the domains and the projects are proposed from what they say. Nothing about how they
invest is asked here. It writes `RESEARCHER.md`, the agent that makes the researcher callable by
name and the skill that puts it in every session, installs them for the user and saves a first
version — the user answers and gives one go.

## Step 6 — Hand over

The interview's own hand-over ends the conversation: who the researcher is and that it is in every
folder, where its home is, what the user can ask it for — one short line a use, and a link to
`USE-CASES.md` — the one next thing for what they came for, and *not sure what's next? say `next`*;
then one question, `Start?`, whose options start each thing they came for. On *Now*, under either
label, *Show me the worked example*, *Start the study* or *I have a document*, follow that skill or
command from its installed path, in this conversation.

**What "done" looks like:** the home holds `RESEARCHER.md` with no angle-bracketed slot left,
`.apm/agents/<slug>.agent.md` and `.apm/skills/<slug>/SKILL.md`, and everything is saved:
`git status` is clean. For Claude Code, `~/.claude/skills/` holds `init-strategy`, `read`, `query`,
`interview`, `next`, `philosophy`, `brief`, `backup` and the researcher's own skill, and
`~/.claude/agents/` holds `blueprint-critic.md` and the researcher's agent.

---

## Later

**The user's philosophy, and a daily brief.** In a new session in the home: `philosophy`, a second
interview on how they work or how they invest — investing at their level — and `brief setup`, which
schedules the brief on the Claude desktop app and says how to run it elsewhere.

**A strategy.** In a new session in the home: `init-strategy fcf-yield-quality`. It makes the
strategy's folder beside the home, from the KaxaNuk Strategy Template; open that folder in a new
session, and its own `SETUP.md` builds the environment and the keys. `init-example` copies a
finished strategy to read first.

**Updating.** `uvx --from apm-cli==0.33.0 apm update -g` brings every new version to every folder
at once; then `update`, in the home, brings what changed in the home's own files. Always with `-g`:
a bare `apm update` outside an APM project updates APM itself.

**A new machine, or another assistant.** Step 2 with the new target, then install the home, once,
the assistant added under `targets:` in the home's `apm.yml` first, OpenCode aside:
`uvx --from apm-cli==0.33.0 apm install -g "<the home>"`.

---

## Troubleshooting

**What each assistant receives.** Claude Code receives everything: the skills, the commands, the
agents and the three instructions, which land in `~/.claude/rules/` — Bloom Code and PEP 8 for
Python in a KaxaNuk repository, and nowhere else, and filesystem boundaries, in any project, for
every file the assistant reads: outside the folder it works in, only the places the task needs.
Copilot receives the same, its instructions merged into `~/.copilot/copilot-instructions.md`.
Cursor, Gemini, OpenCode and Windsurf get the skills and the commands but not the instructions, and
Gemini and Windsurf take no agent: there the researcher is its skill. OpenCode takes the package
but not the researcher's own agent and skill: it rejects the agent APM writes for it, so the home's
`apm.yml` leaves it out of `targets:`. **Codex gets the skills and the agents, and no commands.**
The skills land in `.agents/skills/` and each agent in
`.codex/agents/<name>.toml`, without its tool list: APM warns that it drops it, so on Codex an agent
has no tool boundary. No instruction lands either: APM asks for `apm compile`, which writes them
into a project's `AGENTS.md`. So the steps a newcomer needs — `init-researcher`, `interview`,
`next`, `read`, `query`, `philosophy`, `brief` — are all skills. A command, such as `objective` or
`blueprint`, is run there by naming its file — *follow
`~/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/prompts/objective.prompt.md`* — and once the
interview has run, the researcher's own skill does this for the user: they name the command, and it
follows the file. Assistants without a question tool, such as Codex and Gemini, ask each question in
chat as a numbered list; the user answers with the numbers.

**Why APM is pinned at 0.33.0.** APM 0.33.0 installs this package cleanly, on Windows too. APM
0.29.1 to 0.31.0 staged every package under long folders, and on Windows the worked example's
longest paths passed the 260-character limit: the install failed with `WinError 3` or
`WinError 206`. APM 0.32.0 shortened them (microsoft/apm#2941). A version is adopted only once the
package's release check passes with it on Windows, so the pin is written into every command that
runs APM. `uv tool upgrade` keeps it.
**Never run `apm self-update`**, nor a bare `apm update` outside an APM project, which forwards to
it: both bring the newest APM back. A machine on any other APM runs the same
`uv tool install apm-cli==0.33.0` over it. If `apm` is *command not found*, run
`uv tool update-shell` and open a new terminal; every command here runs through `uvx` and does not
need it.

**On Windows, if the install fails with *checkout failed*,** git itself went past the
260-character limit. Let git use long paths, once, then install again:

```bash
git config --global core.longpaths true
```

**What installing the home copies.** `uvx --from apm-cli==0.33.0 apm install -g "<the home>"`,
which the interview runs, copies the whole home — `.git/`, `Sources/`, `Extracts/`, `Briefs/` and
`Portfolio/` included — into `~/.apm/apm_modules/_local/<the home's folder name>/`, on the same
machine, and deploys only its `.apm/`: the researcher's agent and skill. Nothing leaves the
machine, and each install refreshes the copy. On Windows a deep path in that copy, such as a long
slug under `Extracts/`, can pass the 260-character limit and fail the install. The fix is a
shorter path for the home, or fewer deep extracts: `Extracts/` is a cache, which `read`'s script
makes again from the source.

**On Windows, `git diff` prints a CRLF warning** for the files the researcher wrote; it is expected
and harmless — `.gitattributes` normalises them on commit.

**One researcher per person.** If a home already exists — a folder with a filled `RESEARCHER.md` —
say where it is and do not make a second.

APM's own reference, for any error it prints: <https://microsoft.github.io/apm/llms.txt>.
