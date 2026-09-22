# Setup

Everything needed to go from nothing to a repository you can work in. It is written so an agent —
Claude, Codex, Cursor — can follow it end to end, from `init-strategy` to the strategy's own
README, and so a person can read it in two minutes.

**If the folder you are in already contains `Bibliotheca/`, `Universe/` and `Experiments/`, you have
the repository:** check the two tools below, then skip to step 2.

## What you need first

Two tools. Python is **not** one of them — `uv` fetches the right version itself in step 2.

| Tool | Windows | macOS and Linux |
| --- | --- | --- |
| [git](https://git-scm.com) | `winget install --id Git.Git -e` — or install GitHub Desktop, which brings it | `xcode-select --install` on macOS; your package manager on Linux |
| [uv](https://docs.astral.sh/uv/) | `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |

Open a **new** terminal after installing either, so it is on the path. `git --version` and
`uv --version` both answering is the whole check.

> **For the agent, before anything else.** Look at the folder you are in, and say what you found:
>
> - it holds `Bibliotheca/`, `Universe/` and `Experiments/` → the repository exists, go to step 2;
> - otherwise the repository does not exist yet → step 1. It needs **the strategy's name** — it
>   becomes the folder and repository name, so `fcf-yield-quality`, not `Experiment` — and **where
>   to put it**; ask for whichever the user has not given. A third is optional: **one sentence on
>   the idea**, if the user has it ready — it seeds the README in step 5, and a placeholder is fine
>   if not.
>
> Every command from step 2 on runs **in the root**, the folder step 1 made. Never a level above it.

---

## The rule: one folder is the whole project

One folder is the repository: open that folder, and run every command in it — nothing installed
a level above it, nothing nested a level below. What setup writes there, `.venv/` and
`Config/.env`, is ignored, as is anything an assistant or APM writes per machine (`.claude/`,
`.agents/`, `.codex/`, `apm_modules/`, `apm.lock.yaml`); `uv.lock`, which `uv sync` writes, is
committed, and `apm.yml` comes committed with the template.

---

## Step 1 — Get the repository

**`init-strategy <strategy-name>` makes it** — a skill of the
[KaxaNuk Researcher](https://github.com/KaxaNuk/KaxaNuk-Researcher),
installed once for your user as step 4 says. It copies the template that ships in the researcher
package into a new folder named after the strategy — by a script, byte for byte, so every strategy
made from the same package version starts identical — makes that folder a git repository, and
commits it once. That folder is the root. The template can be read
[on GitHub](https://github.com/KaxaNuk/KaxaNuk-Researcher/tree/main/templates/strategy)
before anything is made.

**A folder that already holds `Bibliotheca/`, `Universe/` and `Experiments/` is the repository
already:** skip to step 2.

**On Windows, keep the path short.** `D:\Research\...` is fine; a deep synced path such as
`C:\Users\<you>\OneDrive\Documents\Projects\...` is not. Tools that write deep inside the
folder, `uv sync` building `.venv/` among them, can pass Windows' 260-character path limit there
and fail with messages that do not say so, such as `WinError 3: The system cannot find the path
specified`.

The worked example, `liquid-golden-cross`, is not copied, on purpose: every file it fills in is
already here, as a description of what belongs in it. `init-example` copies it whole into a folder
of its own, to read or run. Never build on it.

> **For the agent.** If the first commit refuses for want of an identity, on a machine that has
> never committed, ask the user for the name and email to use — never invent them — and set them
> for this repository only: `git config user.name "<name>"` then `git config user.email "<email>"`.
> Then commit again: `git commit -m "Start from the KaxaNuk Strategy Template"`.

---

## Step 2 — Build the environment

From the root:

```bash
uv sync
```

That creates `.venv/` and installs the pipeline. **If neither Python 3.12 nor 3.13 is on the
machine, `uv` downloads 3.13** — there is nothing to install by hand.

**Why 3.13 and not the newest.** The Backtest Engine is documented for Python 3.12 or 3.13, and every
performance figure in this process comes from that engine, so the ceiling is its, not ours. The Data
Curator allows 3.12 to 3.14, which makes 3.13 the version that satisfies both.

**Once the Backtest Engine, Attribution Analysis or Portfolio Construction is installed by hand,
never run a bare `uv sync` here again:** it is exact, and removes every package `uv.lock` does not
name, which those three deliberately are not. Use `uv sync --inexact` instead, and `uv run` for
everything else; both keep them. The `backtest-engine-runs`, `attribution-analysis-runs` and
`portfolio-construction-runs` skills have the installs.

---

## Step 3 — Put your keys in place

```bash
cp Config/.env.template Config/.env
```

Fill in the key for your data provider; the template has a line for FMP, Sharadar and LSEG.
`KNBE_API_KEY_KAXANUK` and `KNAA_API_KEY_KAXANUK` are the Backtest Engine and Attribution Analysis
licences: the process runs without them up to portfolio construction, and the backtest and
attribution report what is missing and skip.

> **For the agent.** Never open, read back, print or echo `Config/.env`, and never put a value from it
> in a command that gets recorded. You may say **which keys are still empty, by name only** — and you
> cannot fill them: that is the one thing in this file only the user can do.

---

## Step 4 — The agent skills are installed once, for your user

**Nothing to install here.** KaxaNuk's agent skills — how each Lab library is called, how an
experiment is structured, how attribution is read, the house rules — and the
[KaxaNuk Researcher](https://github.com/KaxaNuk/KaxaNuk-Researcher)'s own
are installed once for your user, not per repository, by the same command that gave you step 1:

```bash
apm install -g KaxaNuk/KaxaNuk-Researcher --target claude
```

`--target codex`, `cursor` or another assistant in place of `claude`; the researcher package's
[`SETUP.md`](https://github.com/KaxaNuk/KaxaNuk-Researcher/blob/main/SETUP.md) says what each
receives.

They are then available in every folder, this one included, and `apm update -g` keeps every
strategy current at once. **A strategy installs nothing.** Your researcher's home, made once with
`init-researcher`, can be invited into this folder for its library — `claude --add-dir <the
researcher's folder>`, `/add-dir` once inside, or the desktop app's add-folder button.

**Nothing in the pipeline imports a skill either.** The repository runs, the notebooks run and the
results are the same with or without them.

> **For the agent.** Do not install skills into this repository. If they are missing, give the user
> the command above, with the assistant you are as the target — it installs for their user, not
> here, with `uvx --from apm-cli` in front if `apm` is not on the path — and say that they appear
> in a **new** session.

---

## Step 5 — Make the README the strategy's

The `README.md` that `init-strategy` copied describes the KaxaNuk Strategy Template, not your
strategy. A strategy repository's README describes **the strategy**: what it is, what it claims,
where it stands. Replace the whole file with this, filled in, and leave the process to the link:

```markdown
# <strategy-name>

<one sentence on the idea — or: The objective is not written yet; see OBJECTIVE.md.>

> **Status: set up, nothing measured.** Replace this line as the strategy moves, and the banner at
> the top of `AGENTS.md` with it.

Built on the [KaxaNuk Strategy Template](https://github.com/KaxaNuk/KaxaNuk-Researcher/blob/main/templates/strategy/README.md):
eight steps as a folder structure. Its README says what each folder is for, where each
kind of logic goes and, under *Starting your own strategy*, the order to work in; this one does not
repeat it. **Next:** [`OBJECTIVE.md`](OBJECTIVE.md), the idea and its claims, before any paper is
read.

| Read | For |
| --- | --- |
| [`OBJECTIVE.md`](OBJECTIVE.md) | the idea, and the status of each claim inside it |
| [`RESULTS.md`](RESULTS.md) | every number this repository has measured, and what it cost |
| [`AGENTS.md`](AGENTS.md) | how work is done here, and the bar a result has to clear |
| [`SETUP.md`](SETUP.md) | how this repository is set up on a new machine |
```

Put the same status line in place of the banner at the top of `AGENTS.md`. Rename `name` and
`author` in `apm.yml`, and `name` in `pyproject.toml`, to the strategy's and yours, and set
`version` in both to `0.1.0`. In `CHANGELOG.md`, keep everything above the `---` line and replace
the template's entries below it with the strategy's first, naming the template version `apm.yml`
declared before you reset it:

```markdown
## 0.1.0 (YYYY-MM-DD)

**MINOR** — started from the KaxaNuk Strategy Template <template-version>. Nothing measured yet.
```

Then run `uv lock`, so `uv.lock` records the new name and version, and commit them together with
`uv.lock`, the other file the setup itself produced:

```bash
git add README.md AGENTS.md apm.yml pyproject.toml CHANGELOG.md uv.lock
git commit -m "README: <strategy-name>"
```

> **For the agent.** The name is the one you asked for at the start; the sentence too, if the user
> gave one — **never invent a thesis**, use the placeholder. `author` in `apm.yml` is the user's
> name: ask if you do not have it, never invent it. Everything else in the block is fixed. Do not
> keep the template's README under another name: the process lives upstream, and a copy here is a
> copy that drifts.

---

## What "done" looks like

From the root:

```bash
git status
```

**It should be clean.** Step 5 committed what the setup itself changed: the README, the `AGENTS.md`
banner, `apm.yml`'s name, author and version, `pyproject.toml`'s name and version, the first
`CHANGELOG.md` entry, and `uv.lock` — which pins the versions this strategy's results will come
from, and is why the template ships without one and your repository keeps one. Everything else the
commands produced — `.venv/`, `Config/.env`, and whatever your assistant writes per machine, such as
`.claude/` — is ignored.
**Anything showing up means something was written in the wrong place.**

**The repository exists only on this machine until you publish it.** Nothing is lost and nothing
is wrong — but it is not backed up and nobody else can see it. One strategy is one repository. In
GitHub Desktop, *Add* → *Add existing repository*, then *Publish repository*. From the git command
line, create an empty repository on GitHub, then `git remote add origin <its URL>` and
`git push -u origin HEAD`. Either is the whole of it, and it is the user's to do, not the agent's.

Then open **this folder** — not a parent of it — in your editor, PyCharm or VS Code, and in your
assistant, Claude or Codex.

> **For the agent — the hand-over.** Say the absolute path of the root, that it is the whole project
> and the folder to open, that the README is now the strategy's, which `.env` keys are still empty
> by name, that the skills are installed once for the user and nothing is installed here, whether
> the repository has a remote yet, and that the next step is `OBJECTIVE.md`. Then stop.
> Starting research work is a different request.

---

## Next

The first thing to write is `OBJECTIVE.md`: the idea and its claims, before any paper is read. The
order after it is *Starting your own strategy* in the
[template's README](https://github.com/KaxaNuk/KaxaNuk-Researcher/blob/main/templates/strategy/README.md),
which also says where each kind of logic goes; [`AGENTS.md`](AGENTS.md) says how work is done
here.
