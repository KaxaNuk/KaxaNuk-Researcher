---
description: Bring a new version of the researcher into this home — the skills and commands with apm update -g, and any change to the home's own files shown as a diff against the template in the package — keeping RESEARCHER.md, Philosophy/, Knowledge/ and the agent as they are; plan first, the owner's go, then update. Home only. Only when the owner runs it by name.
input:
  - mode: "Optional: check, to report what is new without changing anything"
---

# Update the researcher

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`.

**Home only.** A strategy has nothing to update: it installs no skills, and its files are its own
from the day `init-strategy` made it. In a strategy, say so and stop.

The researcher arrives in two parts, and each updates its own way:

- **The skills and commands** are one package, `KaxaNuk/KaxaNuk-Researcher`, installed once for
  the user. `apm update -g` brings its next version to every folder at once, and nothing in the
  home's history changes.

  Only for a home from before 0.7.0: the package then brought the Lab's skills from
  `KaxaNuk/KaxaNuk-Agent-Skills`, and now carries them itself. The next `apm update -g` removes what
  those packages deployed; `apm deps list -g` may still name them as orphaned, because their folders
  stay under `~/.apm/apm_modules/`, and that is harmless.
- **The home's own files** — `AGENTS.md`, `CLAUDE.md`, `README.md`, `LICENSE`, `apm.yml`,
  `.gitignore` and `.gitattributes` — were copied from `templates/researcher/` in the KaxaNuk
  Researcher package when the home was made. When the package's copy changes, the difference is
  shown, never merged: the owner's home may have renamed its prose. In `apm.yml` the comments,
  `includes` and `dependencies` are compared: its `name`, `version`, `description`, `author` and
  `targets` are the owner's — the version by a rule of its own, which the report in *Step 5* gives
  in these words: "The home's own version in `apm.yml` is yours: `interview` sets it to 0.1.0, you
  bump it with each entry you add to `CHANGELOG.md`, and `update` reads the *Brought to template*
  line there, never this field."

The owner's files are never touched: `RESEARCHER.md`, `Philosophy/`, `Knowledge/`, `Sources/`,
`Lessons/`, the agent file in `.apm/agents/`, and any skill or command of the home's own in
`.apm/skills/` or `.apm/prompts/`. The one exception is the `Projects/` a home made before template
0.10.0 still has, which *Step 2* reads and *Step 4* moves or removes on the owner's go.
`${input:mode}` set to `check` reports what is new and stops, changing nothing.

## Step 1: Pre-flight

1. **The working tree must be clean, for the update.** `git status --short`. Anything uncommitted
   — stop, say so, and tell the owner to commit or stash first. In `check` mode, which changes
   nothing, a dirty tree does not stop the check: report it as one line and go on. A home with no
   `.git/` is not a repository yet: the update stops and the check reports it, naming the commands
   `next` gives to finish it.
2. **A home from before the user-scope install.** Any of these means the home predates it, and this
   update is the migration, which *Step 4* carries out:
   - `.apm/skills/` or `.apm/prompts/` holding `read`, `query` or the researcher's commands;
   - `scripts/extract.py` or `references/note.md` at the root;
   - `apm.yml` naming any KaxaNuk package under `dependencies` — `KaxaNuk/KaxaNuk-Researcher`,
     `KaxaNuk/KaxaNuk-Agent-Skills/researcher` or `.../kaxanuk`.
   Edits the owner made to those skill copies are named in the plan, one line each —
   `git log --oneline -- .apm/skills .apm/prompts scripts references` shows whether there are any —
   because the package's version replaces them.
3. **APM is the version this package is installed with.** APM 0.29.0 installs this package
   cleanly. From 0.29.1 on, APM stages each package under about 148 more characters of folders, the
   worked example's longest paths pass Windows' 260-character limit, and the install fails with
   `WinError 3` or `WinError 206`. So every command below that runs APM names
   `apm-cli==0.29.0` itself. `apm --version` should also say `0.29.0`, since the skills name the
   `apm` on the path; any other version: say so, and put the pinned install first in the plan,
   ahead of the update —

   ```bash
   uv tool install apm-cli==0.29.0
   ```

   Never `apm self-update`, which brings the newest APM back.

## Step 2: What is new

- **The package.** `uvx --from apm-cli==0.29.0 apm outdated -g` says whether a newer commit is
  out, and `uvx --from apm-cli==0.29.0 apm deps list -g` names the installed version. The copy
  under `~/.apm/apm_modules/` stays at that version until *Step 4*, so read the newest from GitHub
  instead: the `main` that `apm update -g` brings, under
  `https://raw.githubusercontent.com/KaxaNuk/KaxaNuk-Researcher/main/`, with `curl -fsSL` or the
  agent's web fetch. Read `CHANGELOG.md` there and take every entry above the installed version.
- **The home's files.** The home's `CHANGELOG.md` names the template version it is at — its newest
  *Brought to template* entry, or else the newest template version in it — and
  `templates/researcher/CHANGELOG.md` on GitHub names the current one. For each of the home's own
  files above, compare the home's copy with the one under `templates/researcher/` on GitHub,
  section by section and in both directions: what the package's copy says that the home's does
  not, and what the home's copy carries that the package's dropped or renamed — a `.gitignore`
  line, a section, a product or file name — because a home that has run `update` four times can
  still carry lines the template removed. A rename of a product or a file name is substance; the
  owner's renaming of *the researcher* and *the owner* is not: such a home differs everywhere in
  wording, and its `README.md` opens with a paragraph of its own, so report what changed in
  substance, not in names. In `apm.yml` compare `includes` and `dependencies` as well as the
  comments.
- **A home at or ahead of the template.** When the home's template version is at or above the one
  `templates/researcher/CHANGELOG.md` names on GitHub — a home made from a checkout with
  `--package`, or from a release not yet pushed — the home is current: say so. Nothing it has is
  proposed for removal, because what the GitHub copy lacks may be what a newer template added. A
  `Projects/` it still holds is listed all the same, as the next item says.
- **The owner's files, read and never written.** The template's `RESEARCHER.md` headings — not its
  slots, nor the blockquote the interview deletes — the headings of `Philosophy/HOW-I-INVEST.md`,
  and the blockquotes of `Knowledge/INDEX.md` and `Knowledge/LOG.md`, each against the home's.
  Every difference is a *by hand* line in *Step 3* and *Step 5*, never a change `update` makes:
  those files are the owner's.
- **`Projects/`, whenever the home still has one**, whatever template version it is at, so a
  move the owner declined once is offered again. Until 0.10.0 the template shipped an
  empty `Projects/`; from 0.10.0 a new home has none, `teach` keeps its lessons in
  `Lessons/<topic>/`, and anything else the owner asks for at home is answered in chat. List what
  the home's `Projects/` holds, sorted three ways: each `Projects/Teach/<topic>/` is to move to
  `Lessons/<topic>/` — unless a `Lessons/<topic>/` exists already, which is listed instead and
  nothing moves; anything else is listed, one line per path, and stays where it is, the owner's to
  keep, move or delete by hand; and when nothing is left but `Projects/.gitkeep`, it is to be
  removed, and the folder with it. The list goes in the report. A home with no `Projects/` has
  nothing to do here.
- **Report in chat, newest first:** the versions crossed, one line each on what changed, and every
  **What to do differently** instruction that applies to this home, in full. Those instructions are
  the point of the update; never summarise them away.
- **All current?** Say so and stop — unless the home still has a `Projects/`, which goes on to the
  plan as the item above lists it. **`check` mode?** Stop here.

## Step 3: Show the plan, wait for the go

In chat: the pinned APM install, when *Step 1* asked for it; the package versions before and after;
for each home file, the sections to bring across, quoted, in the home's own names, and each file
the home lacks, to bring across whole; what a migration removes; each move out of `Projects/` and
its removal, path by path, and what stays there; and what the owner will have to do by hand
afterwards, one line for each heading or blockquote of their own files that the template changed.
Then ask for the go through the question tool — *Go*, *Change something*, *Stop* — and update on
*Go* only; in chat, *go*, *proceed*, *ok* or *yes* is the go.

## Step 4: Update

1. **The package**, after `uv tool install apm-cli==0.29.0` when *Step 1* found another APM:

   ```bash
   uvx --from apm-cli==0.29.0 apm update -g --yes
   ```

   The owner's go in *Step 3* is the confirmation, so `--yes` skips APM's own `[y/N]` prompt,
   which an agent's shell cannot answer; without it the update stops with an error. Then check
   `uvx --from apm-cli==0.29.0 apm deps list -g`: it lists `KaxaNuk/KaxaNuk-Researcher` at the new
   version; a package it still marks orphaned deploys nothing any more. The old
   `KaxaNuk-Agent-Skills` packages deployed skills under the same names as the package's, so if any
   of the package's skills or commands is missing afterwards, deploy it again with the command
   below.

   For a migration, install it instead — it is new at user scope:

   ```bash
   uvx --from apm-cli==0.29.0 apm install -g KaxaNuk/KaxaNuk-Researcher --target <the owner's agent>
   ```

2. **The migration, for a home from before the user-scope install.** `git rm -r` the researcher's
   own skill and command copies under `.apm/skills/` and `.apm/prompts/`, and `scripts/` and
   `references/` at the root; empty `dependencies.apm` in `apm.yml` to `[]`; keep `.apm/agents/`,
   and any skill or command the owner wrote themselves, which the package does not carry. Then
   `uvx --from apm-cli==0.29.0 apm install --target <the owner's agent>` in the home, which deploys
   the agent and removes the copies it deployed before.
3. **The home's files**, the sections the owner approved. A file the home has is edited in place,
   in the home's own names, and nothing else in it changes. A file the home lacks — one a later
   template added, such as `.gitattributes` — is brought across whole by the script in the
   `init-strategy` skill's folder, run from the home's root, never written from memory. It copies
   the one path and never overwrites:

   ```bash
   uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" researcher . --only <path>
   ```

4. **`Projects/`**, the moves and the removal the owner approved, by git, so each file keeps its
   history:

   ```bash
   mkdir -p Lessons
   git mv Projects/Teach/<topic> Lessons/<topic>
   rmdir Projects/Teach
   git rm Projects/.gitkeep
   ```

   `mkdir` and `git mv` only when a topic moves: a home with none gets no `Lessons/`, which the
   first `teach` makes. One `git mv` per topic, never onto a `Lessons/<topic>/` that exists, which
   would nest one topic inside the other. `rmdir` once `Projects/Teach/` is empty, and `git rm` only
   when nothing but `Projects/.gitkeep` is left, which removes the folder with it. What else
   `Projects/` holds stays where it is.
5. **The template version.** Add one entry at the top of the home's `CHANGELOG.md` — the date,
   *Brought to template X.Y.Z*, a line for each section brought across or declined, and one for
   what left `Projects/` and what stayed — whatever the owner declined, so the file names the
   version the home is now at and the next `update` reports only the versions after it. Nothing
   else in the file changes: it is the home's history.

## Step 5: Report

In chat and nowhere else:

- the package versions, before and after;
- the home's template version, before and after, and the rule for the home's own version in
  `apm.yml`, in the words above;
- every **What to do differently** instruction, again, as a list of what is now the owner's to do;
- the *by hand* lines: each heading or blockquote of the owner's files that the template changed,
  for the owner to carry across or leave;
- for a migration, what was removed, and that the skills now live at user scope;
- what left `Projects/` — each move and the removal — and each path left there for the owner;
- the sections of the home's files brought across, and those the owner declined;
- that the new skills and commands appear in a **new** session, not this one.

Nothing is appended to `Knowledge/LOG.md`: that log records reads, audits, index refreshes and kept
synthesis pages, not version changes — the changelogs are the record of what changed.
