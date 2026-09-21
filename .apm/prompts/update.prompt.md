---
description: Bring a new version of the researcher into this home — the skills and commands with apm update -g, and any change to the home's own files shown as a diff against the template in the package — keeping RESEARCHER.md, Philosophy/, Knowledge/ and the agent as they are; plan first, the owner's go, then update. Home only. Only when the owner runs it by name.
input:
  - mode: "Optional: check, to report what is new without changing anything"
metadata:
  version: 0.4
---

# Update the researcher

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`.

**Home only.** A strategy has nothing to update: it installs no skills, and its files are its own
from the day `init-strategy` made it. In a strategy, say so and stop.

The researcher arrives in two parts, and each updates its own way:

- **The skills and commands** are the packages `KaxaNuk/KaxaNuk-Researcher` and
  `KaxaNuk/KaxaNuk-Agent-Skills/kaxanuk` it brings with it, installed once for the user. `apm update -g` brings their
  next version to every folder at once, and nothing in the home's history changes.
- **The home's own files** — `AGENTS.md`, `CLAUDE.md`, `.gitignore` — were copied from
  `templates/researcher/` in the KaxaNuk Researcher package when the home was made. When the package's
  copy changes, the difference is shown, never merged: the owner's home may have renamed its prose.

The owner's files are never touched: `RESEARCHER.md`, `Philosophy/`, `Knowledge/`, `Sources/`,
`Projects/` and the agent file in `.apm/agents/`. `${input:mode}` set to `check` reports what is new
and stops, changing nothing.

## Step 1: Pre-flight

1. **The working tree must be clean.** `git status --short`. Anything uncommitted — stop, say so,
   and tell the owner to commit or stash first.
2. **A home from before the user-scope install.** Any of these means the home predates it, and this
   update is the migration, which *Step 4* carries out:
   - `.apm/skills/` or `.apm/prompts/` holding `read`, `query` or the researcher's commands;
   - `scripts/extract.py` or `references/note.md` at the root;
   - `apm.yml` naming any KaxaNuk package under `dependencies` — `KaxaNuk/KaxaNuk-Researcher`,
     `KaxaNuk/KaxaNuk-Agent-Skills/researcher` or `.../kaxanuk`.
   Edits the owner made to those skill copies are named in the plan, one line each —
   `git log --oneline -- .apm/skills .apm/prompts scripts references` shows whether there are any —
   because the package's version replaces them.

## Step 2: What is new

- **The packages.** `apm outdated -g` names the installed versions and the newest. Read the
  changelog of each package that moved — `researcher/CHANGELOG.md` and the others in
  `KaxaNuk/KaxaNuk-Researcher`, and those in `KaxaNuk/KaxaNuk-Agent-Skills` for the Lab's
  packages — and take every entry between the two.
- **The home's files.** The home's `CHANGELOG.md` names the template version it was made from;
  `templates/researcher/CHANGELOG.md` in the installed package names the current one. For
  `AGENTS.md`, `CLAUDE.md` and `.gitignore`, compare the home's copy with the package's —
  `~/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/templates/researcher/`, after
  `apm update -g` — section by section, and name what the package's copy says that the home's does
  not. A home that renamed *the researcher* and *the owner* differs everywhere in wording; report
  what changed in substance, not in names.
- **Report in chat, newest first:** the versions crossed, one line each on what changed, and every
  **What to do differently** instruction that applies to this home, in full. Those instructions are
  the point of the update; never summarise them away.
- **All current?** Say so and stop. **`check` mode?** Stop here.

## Step 3: Show the plan, wait for the go

In chat: the package versions before and after; for each home file, the sections to bring across,
quoted, in the home's own names; what a migration removes; and what the owner will have to do by
hand afterwards. Then ask for the go through the question tool — *Go*, *Change something*, *Stop* —
and update on *Go* only; in chat, *go*, *proceed*, *ok* or *yes* is the go.

## Step 4: Update

1. **The packages:**

   ```bash
   apm update -g
   ```

   For a migration, install them instead — the dependencies are new at user scope:

   ```bash
   apm install -g KaxaNuk/KaxaNuk-Researcher --target <the owner's agent>
   ```

2. **The migration, for a home from before the user-scope install.** `git rm -r` the researcher's
   own skill and command copies under `.apm/skills/` and `.apm/prompts/`, and `scripts/` and
   `references/` at the root; empty `dependencies.apm` in `apm.yml` to `[]`; keep `.apm/agents/`,
   and any skill or command the owner wrote themselves, which the package does not carry. Then
   `apm install --target <the owner's agent>` in the home, which deploys the agent and removes the
   copies it deployed before.
3. **The home's files**, the sections the owner approved, edited in place in the home's own names.
   Nothing else in them changes.

## Step 5: Report

In chat and nowhere else:

- the package versions, before and after;
- every **What to do differently** instruction, again, as a list of what is now the owner's to do;
- for a migration, what was removed, and that the skills now live at user scope;
- the sections of the home's files brought across, and those the owner declined;
- that the new skills and commands appear in a **new** session, not this one.

Nothing is appended to `Knowledge/LOG.md`: that log records reads, audits and index refreshes, not
version changes — the changelogs are the record of what changed.
