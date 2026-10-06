---
description: Bring a new version of the researcher into this home — the skills and commands with apm update -g, and any change to the home's own files shown as a diff against the template in the package — keeping RESEARCHER.md, Philosophy/, Knowledge/ and the agent as they are, and writing the researcher's skill for a home that lacks it or holds one behind the template; plan first, the owner's go, then update. Home only. Only when the owner runs it by name.
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
- **The home's own files** — `AGENTS.md`, `CLAUDE.md`, `README.md`, `LICENSE`, `apm.yml`,
  `.gitignore` and `.gitattributes` — were copied from `templates/researcher/` in the KaxaNuk
  Researcher package when the home was made. When the package's copy changes, the difference is
  shown, never merged: the owner's home may have renamed its prose. In `apm.yml` the comments,
  `includes` and `dependencies` are compared: its `name`, `version`, `description`, `author` and
  `targets` are the owner's — the version by a rule of its own, which the report in *Step 5* gives
  in these words: "The home's own version in `apm.yml` is yours: `interview` sets it to 0.1.0, you
  bump it with each entry you add to `CHANGELOG.md`, and `update` reads the *Brought to template*
  line there, never this field."

The owner's files are never touched: `RESEARCHER.md`, `Philosophy/` — its round files in
`Philosophy/Evolution/` included, which nothing edits once `philosophy` has written them —
`Knowledge/`, `Sources/`, `Studies/`, `Lessons/`, `Briefs/`, `Portfolio/`, the agent file in
`.apm/agents/`, and any skill or command of the home's own in `.apm/skills/` or `.apm/prompts/`.
The exceptions are three, each on the owner's go: the `Projects/` a home made before template
0.10.0 still has, which *Step 2* reads and *Step 4* moves or removes; the empty `Studies/` a home
made before template 0.12.0 lacks, whose `.gitkeep` *Step 4* brings from the template; and the
researcher's skill, `.apm/skills/<slug>/SKILL.md`, which *Step 4* writes as `interview` gives it
when the home lacks it or *Step 2* finds it behind the template — and, when its slug changes, the
agent's file name and `name:` with it, nothing else in the agent.
`${input:mode}` set to `check` reports what is new and stops, changing nothing.

## Step 1: Pre-flight

1. **The working tree must be clean, for the update.** `git status --short`. Anything uncommitted
   — name it and offer its commit as `next`'s row 0 does, `Commit?` (`¿Confirmo?`), *Commit it
   for me*, *I'll review it first*; on *Commit it for me*, run it and go on; otherwise stop. In
   `check` mode, which changes nothing, a dirty tree does not stop the check: report it as one
   line and go on. A home with no `.git/` is not a repository yet: the update stops and the check
   reports it, naming the commands `next` gives to finish it.
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
   `apm-cli==0.29.0` itself. `apm --version` should also say `0.29.0`, since a command typed by
   hand runs the `apm` on the path; any other version: say so, and put the pinned install first in
   the plan, ahead of the update —

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
  those files are the owner's. Template 0.16.0 adds two lines a home made before it lacks, each a
  *by hand* line, quoted from the template, when the home has no such line: *Here for* under *Who*
  in `RESEARCHER.md` — what the owner is here for, one of the four the interview offers or their
  own words — and `## Why I invest`, the new first heading of `Philosophy/HOW-I-INVEST.md`, which
  the owner may write in their own language. The same release points *What you believe* to
  `HOW-I-INVEST.md` and takes *Where it sits* and its *Add later* line out of the template: the
  home's own prose there is the owner's, and stays unless they take it out by hand. The agent file
  is theirs as well: a line `interview` now writes into a new agent's body is a *by hand* line too
  — from 0.16.0, *Round files in `Philosophy/Evolution/` are a record of how the owner's answers
  moved: read them for dates and levels, and cite `HOW-I-INVEST.md`, never a round file, as the
  owner's view.* So is the researcher's skill, unless *Step 4* writes it afresh: the same line
  goes in its item 2, *Read the home first*, by hand. After either edit,
  `uvx --from apm-cli==0.29.0 apm install -g "<absolute path to the home>"` deploys it.
- **`Briefs/` and `Portfolio/`.** From template 0.16.0 the home's `.gitignore` ignores both — the
  daily brief `brief` writes, and the holdings and rules the owner keeps for its *Portfolio* part —
  and `AGENTS.md` gives each a row in its folder table. They are compared like any other lines of
  those two files, and the `.gitignore` lines are said first in the plan, so they are in place
  before a first `brief setup` and no holding is ever committed. When either folder exists already
  and `git ls-files Briefs Portfolio` lists a file, say so: a line in `.gitignore` does not take a
  committed file out of the history, and what to do about it is the owner's. `update` never writes
  in either folder, and the template ships neither: `brief setup` creates `Portfolio/` when the
  owner opts into its *Portfolio* part, and the first brief `Briefs/`.
- **`Projects/`, whenever the home still has one**, whatever template version it is at, so a move
  the owner declined once is offered again. Until 0.10.0 the template shipped an empty `Projects/`;
  from 0.10.0 `teach` keeps its lessons in `Lessons/<topic>/`, and from 0.12.0 the owner's own work
  from the library is a study in `Studies/`. List what the home's `Projects/` holds, sorted three
  ways: each `Projects/Teach/<topic>/` is to move to `Lessons/<topic>/`; every other file or folder
  at the top of `Projects/` is to move to `Studies/` under the same name — `Projects/GPU_Compute.md`
  to `Studies/GPU_Compute.md` — at the same depth, so its links into `Knowledge/` still resolve; and
  when nothing is left but `Projects/.gitkeep`, it is to be removed, and the folder with it. A
  destination that exists already is listed instead, and nothing moves onto it. A file that moves is
  a study from then on: say that its first line may want a state, the owner's to add by hand or with
  `study`. The list goes in the report. A home with no `Projects/` has nothing to do here.
- **`Studies/`, when the home lacks it** — a home made before template 0.12.0: its `.gitkeep` is
  to come from the template, so the folder is there to see.
- **The researcher's skill and the install for the user**, whatever template version the home is
  at. `<slug>` is the researcher's name made safe for a folder, by the rule `interview`'s *Step 4*
  gives — `Sofía` becomes `sofia` — and the name keeps its accents in the skill's text. APM deletes
  any other character from a folder name — `sofía` would deploy as `sofa` — so a slug that keeps
  an accent never installs under its own name. The skill is to be written as `interview`'s *Step 4*
  gives it, from `RESEARCHER.md` and this folder's absolute path, when the home has an agent in
  `.apm/agents/` and no skill of the same `name:`, and written again when the home's skill
  names a folder other than this one, is behind the template — its `metadata.version` below the
  one `interview`'s *Step 4* gives, as a skill without the items *A greeting, or what now* and *A
  command, where the assistant has none* is — or has a slug that breaks the rule, such as an
  accent, when it moves to `.apm/skills/<slug>/`. Written again, it is shown as a diff against the
  home's: a line there that no template gave is the owner's, kept where it stands and shown as
  kept. A slug that changes moves the agent with it, on the same go: its file to
  `.apm/agents/<slug>.agent.md` and its `name:` to `<slug>`, the only edit to that file. When the
  skill is written, or the user's folder of the assistant in use lacks the agent or the skill, as
  `next`'s row 3 checks, the home is to be installed for the user. And an agent an install inside
  the home deployed there — `.claude/agents/<slug>.md`, or the agent's file in another assistant's
  folder inside the home — is to be deleted: it is git-ignored, it shadows the user's copy in every
  session at home, and it goes stale the first time the agent changes; so are the copies a changed
  slug leaves in the user's folder, the skill and the agent there whose `name:` is the old slug,
  under the name APM gave them — `~/.claude/skills/sofa/` for `sofía`.
- **Report in chat:** first the installed package version, as `apm deps list -g` names it, and the
  home's template version — the two a problem report to `lab@kaxanuk.mx` names; then the versions
  crossed, newest first, one line each on what changed, and every **What to do differently**
  instruction that applies to this home, in full. Those instructions are the point of the update;
  never summarise them away.
- **All current?** Say so, with those two versions, and stop — unless the home still has a
  `Projects/`, lacks `Studies/`, or its researcher's skill or the install for the user is missing
  or behind, which go on to the plan as the items above list them. **`check` mode?** Stop here.

## Step 3: Show the plan, wait for the go

In chat: the pinned APM install, when *Step 1* asked for it; the package versions before and after;
for each home file, the sections to bring across, quoted, in the home's own names, and each file
the home lacks, to bring across whole — `Studies/.gitkeep` among them, when the folder is
missing; what a migration removes; each move out of `Projects/` and its removal, path by path, and
what stays there; the researcher's skill, shown whole when new and as a diff when written again,
the agent's move when the slug changes, the install for the user and each copy to delete; and what
the owner will have to do by hand afterwards, one line for each heading, line or blockquote of
their own files that the template changed. Then ask for the go through the question tool — *Go*,
*Change something*, *Stop* — and update on *Go* only; in chat, any of the go words in the home's
`AGENTS.md` is the go.

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
   `uvx --from apm-cli==0.29.0 apm install --target <the owner's agent>` in the home, which removes
   the copies it deployed before; the agent it deploys there is deleted in item 5, once the home is
   installed for the user.
3. **The home's files**, the sections the owner approved. A file the home has is edited in place,
   in the home's own names, and nothing else in it changes. A file the home lacks — one a later
   template added, such as `.gitattributes` or `Studies/.gitkeep` — is brought across whole by the
   script in the `init-strategy` skill's folder, run from the home's root, never written from
   memory. It copies the one path and never overwrites:

   ```bash
   uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" researcher . --only <path>
   ```

4. **`Projects/`**, the moves and the removal the owner approved, by git, so each file keeps its
   history — once `Studies/.gitkeep` has come across in the item above:

   ```bash
   mkdir -p Lessons
   git mv Projects/Teach/<topic> Lessons/<topic>
   rmdir Projects/Teach
   git mv Projects/<name> Studies/<name>
   git rm Projects/.gitkeep
   ```

   `mkdir` and the first `git mv` only when a topic moves: a home with none gets no `Lessons/`,
   which the first `teach` makes. One `git mv` per topic and per other file or folder, never onto a
   destination that exists, which would nest one inside the other. `rmdir` once `Projects/Teach/`
   is empty, and `git rm` only when nothing but `Projects/.gitkeep` is left, which removes the
   folder with it. What the owner chose to keep in `Projects/` stays where it is.
5. **The researcher's skill and the install for the user**, as the owner approved. When the slug
   changed, `git mv` the old skill folder to `.apm/skills/<slug>/` and the agent to
   `.apm/agents/<slug>.agent.md`, so both keep their history, and set the agent's `name:` to
   `<slug>`. Write `.apm/skills/<slug>/SKILL.md`; install the home beside the package, so the agent
   and the skill reach every folder —

   ```bash
   uvx --from apm-cli==0.29.0 apm install -g "<absolute path to the home>"
   ```

   — and delete each copy *Step 2* listed: the agent's inside the home, and the skill and the agent
   the old slug left in the user's folder. The install copies the whole home — `.git/`, `Sources/`,
   `Extracts/`, `Briefs/` and `Portfolio/` included — into
   `~/.apm/apm_modules/_local/<folder name>/` on this machine, refreshed by each install, and
   deploys only its `.apm/`; nothing leaves the machine. On Windows a long `Extracts/` path in that
   copy can pass the 260-character limit and fail the install: the fix, the owner's to choose, is a
   shorter home path or fewer deep extracts, a regenerable cache.
6. **The template version.** Add one entry at the top of the home's `CHANGELOG.md` — the date,
   *Brought to template X.Y.Z*, a line for each section brought across or declined, one for what
   left `Projects/` and what stayed, one for `Studies/` when it came, and one for the researcher's
   skill when it was written — whatever the owner declined, so the file names the version the home
   is now at and the next `update` reports only the versions after it. Nothing else in the file
   changes: it is the home's history.
7. **Then offer the commit**, as the home's `AGENTS.md` says. Show `git add` with every file
   written above, by name, never `--all`, since what `git mv` and `git rm` did is staged already,
   and `git commit -m "Update: brought to template X.Y.Z"`, and ask `Commit?` (`¿Confirmo?`):
   *Commit it for me* runs them; after *I'll review it first*, they commit, or say *commit it* and
   you run them. Never commit unasked. The copies deleted in item 5 are git-ignored or outside the
   home, and leave nothing to commit.

## Step 5: Report

In chat and nowhere else:

- the package versions, before and after;
- the home's template version, before and after, and the rule for the home's own version in
  `apm.yml`, in the words above;
- every **What to do differently** instruction, again, as a list of what is now the owner's to do;
- the *by hand* lines: each heading, line or blockquote of the owner's files that the template
  changed, for the owner to carry across or leave;
- for a migration, what was removed, and that the skills now live at user scope;
- what left `Projects/` — each move and the removal — and each path left there for the owner, and
  that a file moved into `Studies/` may want a state on its first line;
- the sections of the home's files brought across, and those the owner declined;
- the researcher's skill, when it was written, with the owner's lines it kept, and the agent's new
  name when the slug changed; and that the home is now installed for the user, so the researcher
  is in every folder;
- that the new skills and commands appear in a **new** session, not this one.

Nothing is appended to `Knowledge/LOG.md`: that log records reads, audits, index refreshes and kept
synthesis pages, not version changes — the changelogs are the record of what changed.
