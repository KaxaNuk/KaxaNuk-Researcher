---
description: Bring a new version of the researcher into this home — the skills and commands with apm update -g, and any change to the home's own files shown as a diff against the template in the package — keeping RESEARCHER.md, Philosophy/, Knowledge/ and the agent as they are, but for the agent's name and path, and writing the researcher's skill for a home that lacks it or holds one behind the template; plan first, the owner's go, then update. From a strategy, the package only and a report of the Lab libraries, nothing written there. Only when the owner runs it by name.
input:
  - mode: "Optional: check, to report what is new without changing anything"
---

# Update the researcher

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`, the
one the researcher's skill names when the session is elsewhere — and every git command runs there,
the `backup` skill's send included, as `git -C "<absolute path to the home>"` when the session is
open elsewhere. Find it first and read its `RESEARCHER.md` and `AGENTS.md`.

**From a strategy, the package only.** A strategy installs no skills, and its files are its own
from the day `init-strategy` made it: `update` writes nothing in it. Run there, it brings the
package — *Step 1* item 3, *Step 2*'s first item and *Step 4* item 1, with *Step 3*'s plan and go
between and *Step 5*'s package lines after — and reports the Lab libraries the strategy runs on as
`next`'s *Step 4* item 5 does, whatever its weekly date says; each upgrade is the owner's, between
experiments. The home's own files are updated from the home: say so in one line.

The researcher arrives in two parts, and each updates its own way:

- **The skills and commands** are one package, `KaxaNuk/KaxaNuk-Researcher`, installed once for
  the user. `apm update -g` brings its next version to every folder at once, and nothing in the
  home's history changes.
- **The home's own files** — `AGENTS.md`, `CLAUDE.md`, `README.md`, `LICENSE`, `apm.yml`,
  `.gitignore` and `.gitattributes` — were copied from `templates/researcher/` in the KaxaNuk
  Researcher package when the home was made. When the package's copy changes, the difference is
  shown, never merged: the owner's home may have renamed its prose. `LICENSE` is compared without
  its copyright line, which is the owner's to keep and never proposed back to KaxaNuk. In
  `apm.yml` the comments, `includes` and `dependencies` are compared: its `name`, `version`,
  `description`, `author` and `targets` are the owner's, but for an assistant the template's
  `targets:` lists and the home's does not, proposed as a line to add — the version by a rule of
  its own, which the report in *Step 5* gives in these words: "The home's own version in
  `apm.yml` is yours: `interview` sets it to 0.1.0, you bump it with each entry you add to
  `CHANGELOG.md`, and `update` reads the *Brought to template* line there, never this field."

The owner's files are never touched: `RESEARCHER.md`, `Philosophy/` — its round files in
`Philosophy/Evolution/` included, which nothing edits once `philosophy` has written them —
`Knowledge/`, `Sources/`, `Studies/`, `Lessons/`, `Briefs/`, `Portfolio/`, the agent file in
`.apm/agents/`, and any skill or command of the home's own in `.apm/skills/` or `.apm/prompts/`.
The exceptions are three, each on the owner's go: the `Projects/` a home made before template
0.10.0 still has, which *Step 2* reads and *Step 4* moves or removes; the empty `Studies/` a home
made before template 0.12.0 lacks, whose `.gitkeep` *Step 4* brings from the template; and the
researcher's skill, `.apm/skills/<slug>/SKILL.md`, which *Step 4* writes as `interview` gives it
when the home lacks it or *Step 2* finds it behind the template — and in the agent, its file name
and `name:` when the slug changes and its *on this machine* path when that is not this folder,
nothing else.
`${input:mode}` set to `check` reports what is new and stops, changing nothing.

## Step 1: Pre-flight

1. **Everything must be saved, for the update.** `git status --short`. Anything unsaved — name it
   in plain words, file by file (*your note on Fama 1970*, *RESEARCHER.md*), never the commands,
   and ask `Save?` (`¿Guardo?`): *Save this version*, *Stop*. On *Save this version*, save it as
   `next`'s row 0 does — `git add` each file by name, never `--all`, and `git commit` — and go on;
   on *Stop*, stop. In `check` mode, which changes nothing, unsaved files do not stop the check:
   report them as one line and go on. A home with no `.git/` keeps no versions yet: the update
   stops and the check says so in one line; `next` offers to start them.
2. **A home from before the user-scope install.** Any of these means the home predates it, and this
   update is the migration, which *Step 4* carries out:
   - `.apm/skills/` or `.apm/prompts/` holding `read`, `query` or the researcher's commands;
   - `scripts/extract.py` or `references/note.md` at the root;
   - `apm.yml` naming any KaxaNuk package under `dependencies` — `KaxaNuk/KaxaNuk-Researcher`,
     `KaxaNuk/KaxaNuk-Agent-Skills/researcher` or `.../kaxanuk`.
   Edits the owner made to those skill copies are named in the plan, one line each —
   `git log --oneline -- .apm/skills .apm/prompts scripts references` shows whether there are any —
   because the package's version replaces them.
3. **APM is the version this package is installed with.** APM 0.33.0 installs this package
   cleanly. APM 0.29.1 to 0.31.0 staged each package under about 148 more characters of folders,
   the worked example's longest paths passed Windows' 260-character limit, and the install failed
   with `WinError 3` or `WinError 206`. So every command below that runs APM names
   `apm-cli==0.33.0` itself. `apm --version` should also say `0.33.0`, since a command typed by
   hand runs the `apm` on the path; any other version: say so, and put the pinned install first in
   the plan, ahead of the update —

   ```bash
   uv tool install apm-cli==0.33.0
   ```

   Never `apm self-update`, which brings the newest APM back.

## Step 2: What is new

- **The package.** The installed version is the `version:` of the package's entry in
  `~/.apm/apm.lock.yaml`, read with the file tool — the entry whose `repo_url` or
  `materialization_repo_url` is `kaxanuk/kaxanuk-researcher` in any case, never a `source: local`
  one; `uvx --from apm-cli==0.33.0 apm deps list -g` names the same. The newest is the first tag
  this prints, `v` and the version:

  ```bash
  git -c http.lowSpeedLimit=1000 -c http.lowSpeedTime=10 ls-remote --tags --refs --sort=-v:refname https://github.com/KaxaNuk/KaxaNuk-Researcher
  ```

  The copy under `~/.apm/apm_modules/` stays at the installed version until *Step 4*, so what is
  new is read on GitHub, in the `main` that `apm update -g` brings, by two commands that run the
  same in Git Bash and PowerShell, with `[Console]::OutputEncoding = [Text.Encoding]::UTF8;` before
  them in PowerShell 5.1. The first prints the entries of a changelog there above a version, newest
  first, and nothing when there are none — never the whole root `CHANGELOG.md`, past 140 KB. Run it
  with `CHANGELOG.md` and the installed version, and take every entry it prints. The second prints
  one file of that `main` whole, by its path in the package.

  ```bash
  uv run --no-project python -X utf8 -c "import sys,urllib.request as u;f,v=sys.argv[1:3];t=u.urlopen('https://raw.githubusercontent.com/KaxaNuk/KaxaNuk-Researcher/main/'+f,timeout=10).read().decode().splitlines();h=[i for i,l in enumerate(t) if l[:3]=='## '];e=[i for i in h if t[i].split()[1:2] in ([v],['['+v+']'])];print('\n'.join(t[h[0]:e[0]]) if e else 'No entry for '+v+' in '+f)" CHANGELOG.md <installed version>
  uv run --no-project python -X utf8 -c "import sys,urllib.request as u;sys.stdout.write(u.urlopen('https://raw.githubusercontent.com/KaxaNuk/KaxaNuk-Researcher/main/'+sys.argv[1],timeout=10).read().decode())" templates/researcher/AGENTS.md
  ```

  Offline, or a command that fails: say so in one line and stop, since nothing can be compared.
- **The home's files.** The home's `CHANGELOG.md` names the template version it is at — its newest
  *Brought to template* entry, or else the newest template version in it. The first command, run
  with `templates/researcher/CHANGELOG.md` and that version, prints the template's entries above
  it, and the newest heading it prints is the current template version. For each of the home's own
  files above, compare the home's copy with the package's under `templates/researcher/`, which the
  second command prints, section by section and in both directions: what the package's copy says
  that the home's does not, and what the home's copy carries that the package's dropped or renamed
  — a `.gitignore` line, a section, a product or file name — because a home that has run `update`
  four times can still carry lines the template removed. A rename of a product or a file name is
  substance; the owner's renaming of *the researcher* and *the owner* is not: such a home differs
  everywhere in wording, and its `README.md` opens with a paragraph of its own, so report what
  changed in substance, not in names. In `apm.yml` compare `includes` and `dependencies` as well
  as the comments.
- **A home at or ahead of the template.** When the home's template version is at or above the one
  `templates/researcher/CHANGELOG.md` names on GitHub — the first command prints nothing, or *No
  entry for* that version: a home made from a checkout with `--package`, or from a release not yet
  pushed — the home is current: say so. Nothing it has is proposed for removal, because what the
  GitHub copy lacks may be what a newer template added. A `Projects/` it still holds is listed all
  the same, as the next item says.
- **The owner's files, read and never written.** The template's `RESEARCHER.md` headings — not its
  slots, nor the blockquote the interview deletes — and the blockquotes of `Knowledge/INDEX.md` and
  `Knowledge/LOG.md`, each against the home's. Every difference is a *by hand* line in *Step 3* and
  *Step 5*, never a change `update` makes: those files are the owner's. Template 0.16.0 adds a line
  a home made before it lacks, a *by hand* line, quoted from the template, when the home has no such
  line: *Here for* under *Who* in `RESEARCHER.md` — what the owner is here for, one of the four the
  interview offers or their own words. A *Here for* holding the older *Organise what I read* is no
  *by hand* line: every skill reads it as *Organise what I read, and help with my projects*. The
  same release points *What you believe* to `HOW-I-INVEST.md` and takes *Where it sits* and its *Add
  later* line out of the template: the home's own prose there is the owner's, and stays unless they
  take it out by hand. Template 0.23.0 ships `Philosophy/` holding only a `.gitkeep`, which is never
  brought across: `Philosophy/` is the owner's, and `philosophy` makes what a round needs. The
  home's `HOW-I-INVEST.md` stays as it is, its headings are no longer compared, and a missing one —
  the file, or a heading such as 0.16.0's `## Why I invest` — is no *by hand* line: `philosophy`
  starts the file, or adds the heading, when a round needs it. *Non-negotiables* is the owner's too:
  template 0.23.0 ships it as *None yet.*, the rules asked later by `philosophy`, and the rules a
  home holds there — an older template's three included — stay as they are, with no *by hand* line.
  The agent file is theirs as well: a line `interview` now writes into a new agent's body is a *by
  hand* line too — from 0.16.0, and as 0.23.0 words it, in place of the 0.16.0 sentence that cites
  `HOW-I-INVEST.md` alone, where the agent has it: *Round files in `Philosophy/Evolution/` are a
  record of how the owner's answers moved: read them for dates and levels, and cite the owner's file
  in `Philosophy/` — `HOW-I-WORK.md` or `HOW-I-INVEST.md` — never a round file, as the owner's
  view.* So is a second, in *You never write*: `philosophy` *to write down how they work or how they
  invest*, in place of *to write down how they invest*. The researcher's skill is theirs too, unless
  *Step 4* writes it afresh: the first line goes in its item 2, *Read the home first*, by hand.
  After either edit, `uvx --from apm-cli==0.33.0 apm install -g "<absolute path to the home>"`
  deploys it.
- **`Briefs/` and `Portfolio/`.** From template 0.16.0 the home's `.gitignore` ignores both — the
  daily brief `brief` writes, and the holdings and rules the owner keeps for its *Portfolio* part —
  and `AGENTS.md` gives each a row in its folder table. They are compared like any other lines of
  those two files, and the `.gitignore` lines are said first in the plan, so they are in place
  before a first `brief setup` and no holding is ever saved in a version. When either folder exists
  already and `git ls-files Briefs Portfolio` lists a file, say so: a line in `.gitignore` does not
  take a file out of the versions already saved, and what to do about it is the owner's. `update`
  never writes in either folder, and the template ships neither: `brief setup` creates
  `Portfolio/` when the owner opts into its *Portfolio* part, and the first brief `Briefs/`.
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
  accent, when it moves to `.apm/skills/<slug>/`. The version `interview` gives is read on GitHub,
  in `.apm/skills/interview/SKILL.md`, by the second command, since the installed copy is the old
  one until *Step 4*. Written again, it is shown as a diff against the home's: a line there that
  no template gave is the owner's, kept where it stands and shown as kept. A slug that changes
  moves the agent with it, on the same go: its file to `.apm/agents/<slug>.agent.md` and its
  `name:` to `<slug>`. An agent whose *on this machine* path is not this folder has it set to this
  folder on the same go, shown in the plan: beside `name:`, the only edit to that file. When the
  skill or the agent is written, or the user's folder of the assistant in use lacks the agent or the
  skill, as `next`'s row 3 checks, the home is to be installed for the user. And an agent an install
  inside the home deployed there — `.claude/agents/<slug>.md`, or the agent's file in another
  assistant's folder inside the home — is to be deleted: it is git-ignored, it shadows the user's
  copy in every session at home, and it goes stale the first time the agent changes; so are the
  copies a changed slug leaves in the user's folder, the skill and the agent there whose `name:` is
  the old slug, under the name APM gave them — `~/.claude/skills/sofa/` for `sofía`.
- **`targets:` in `apm.yml`, whatever template version the home is at.** Installing a home reaches
  only the assistants listed under `targets:` both in its `apm.yml` and in `~/.apm/apm.yml`. Each
  one the template's lists — the second command, run with `templates/researcher/apm.yml` — and the
  home's does not is to be added as a line, and the home then installed for the user; the home's
  other lines there are the owner's, and stay.
- **Report in chat:** first the installed package version, as `apm deps list -g` names it, and the
  home's template version — the two a problem report to `lab@kaxanuk.mx` names; then the versions
  crossed, newest first, one line each on what changed, and every **What to do differently**
  instruction that applies to this home, in full. Those instructions are the point of the update;
  never summarise them away.
- **All current?** Say so, with those two versions, and stop — unless the home still has a
  `Projects/`, lacks `Studies/` or a `targets:` line the template lists, or its researcher's skill
  or the install for the user is missing or behind, or the agent names another folder, which go on
  to the plan as the items above list them. **`check` mode?** Stop here.

## Step 3: Show the plan, wait for the go

In chat: the pinned APM install, when *Step 1* asked for it; the package versions before and after;
for each home file, the sections to bring across, quoted, in the home's own names, the `targets:`
lines to add to `apm.yml`, and each file the home lacks, to bring across whole — `Studies/.gitkeep`
among them, when the folder is missing; what a migration removes; each move out of `Projects/` and
its removal, path by path, and what stays there; the researcher's skill, shown whole when new and as
a diff when written again, the agent's move when the slug changes and its path when it names another
folder, the install for the user and each copy to delete; and what the owner will have to do by hand
afterwards, one line for each heading, line or blockquote of their own files that the template
changed. When a strategy the session is in, or one the table *The strategies and projects it works
on* in `RESEARCHER.md` lists, has a `BLUEPRINT_N.md` saved and no `FINDINGS_N.md` that reports yet,
one more line, with the version its *Drafted with* stamp names: *Experiment N was drafted with
X.Y.Z; `challenge` will name both versions — update now, or after its findings.* Then ask for the go
through the question tool — *Go*, described as *update it and save a version*; *Change something*;
*Stop* — and update on *Go* only; in chat, any of the go words in the home's `AGENTS.md` is the go.

## Step 4: Update

1. **The package**, after `uv tool install apm-cli==0.33.0` when *Step 1* found another APM:

   ```bash
   uvx --from apm-cli==0.33.0 apm update -g --yes
   ```

   The owner's go in *Step 3* is the confirmation, so `--yes` skips APM's own `[y/N]` prompt,
   which an agent's shell cannot answer; without it the update stops with an error. Then check
   `uvx --from apm-cli==0.33.0 apm deps list -g`: it lists `KaxaNuk/KaxaNuk-Researcher` at the new
   version; a package it still marks orphaned deploys nothing any more. The old
   `KaxaNuk-Agent-Skills` packages deployed skills under the same names as the package's, so if any
   of the package's skills or commands is missing afterwards, deploy it again with the command
   below.

   For a migration, install it instead — it is new at user scope:

   ```bash
   uvx --from apm-cli==0.33.0 apm install -g KaxaNuk/KaxaNuk-Researcher --target <the owner's agent>
   ```

   Either way, the date `next` keeps for its weekly version line then moves a week on, in the
   home's git config — from a strategy too, at the home the researcher's skill names; it is never
   saved or sent anywhere:

   ```bash
   git -C "<home>" config kaxanuk.updatenext <today + 7 days, YYYY-MM-DD>
   ```

2. **The migration, for a home from before the user-scope install.** `git rm -r` the researcher's
   own skill and command copies under `.apm/skills/` and `.apm/prompts/`, and `scripts/` and
   `references/` at the root; empty `dependencies.apm` in `apm.yml` to `[]`; keep `.apm/agents/`,
   and any skill or command the owner wrote themselves, which the package does not carry. Then
   `uvx --from apm-cli==0.33.0 apm install --target <the owner's agent>` in the home, which removes
   the copies it deployed before; the agent it deploys there is deleted in item 5, once the home is
   installed for the user.
3. **The home's files**, the sections and the `targets:` lines the owner approved. A file the home
   has is edited in place, in the home's own names, and nothing else in it changes. A file the home
   lacks — one a later template added, such as `.gitattributes` or `Studies/.gitkeep` — is brought
   across whole by the script in the `init-strategy` skill's folder, run from the home's root, never
   written from memory. It copies the one path and never overwrites:

   ```bash
   uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" researcher . --only <path>
   ```

4. **`Projects/`**, the moves and the removal the owner approved, by git, so each file keeps its
   history — once `Studies/.gitkeep` has come across in the item above:

   ```bash
   mkdir -p "<home>/Lessons"
   git mv Projects/Teach/<topic> Lessons/<topic>
   rmdir "<home>/Projects/Teach"
   git mv Projects/<name> Studies/<name>
   git rm Projects/.gitkeep
   ```

   `mkdir` and the first `git mv` only when a topic moves: a home with none gets no `Lessons/`,
   which the first `teach` makes. One `git mv` per topic and per other file or folder, never onto a
   destination that exists, which would nest one inside the other. `rmdir` once `Projects/Teach/`
   is empty, and `git rm` only when nothing but `Projects/.gitkeep` is left, which removes the
   folder with it. What the owner chose to keep in `Projects/` stays where it is.
5. **The researcher's skill and the install for the user**, as the owner approved — the install
   alone, below, when only `targets:` gained a line. When the slug changed, `git mv` the old skill
   folder to `.apm/skills/<slug>/` and the agent to `.apm/agents/<slug>.agent.md`, so both keep
   their history, and set the agent's `name:` to `<slug>`. Set the agent's *on this machine* path to
   this folder when it names another. Write `.apm/skills/<slug>/SKILL.md`; install the home beside
   the package, so the agent and the skill reach every folder —

   ```bash
   uvx --from apm-cli==0.33.0 apm install -g "<absolute path to the home>"
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
7. **Then save a version**, on the plan's go, with no second question: `git add` every file
   written above, by name, never `--all` — what `git mv` and `git rm` did is staged already — and
   `git commit -m "Update: brought to template X.Y.Z"`; to the owner, *Saved*, in one plain line,
   never the commands. The copies deleted in item 5 are git-ignored or outside the home, and leave
   nothing to save. When `git config --get kaxanuk.autosend` prints `true`, it also goes to their
   copy on GitHub, as the `backup` skill says. If git wants a name and an e-mail, ask for both in
   one plain line, set them in the home only, never invented, and save again. This replaces an
   older home's *Commit?* question.

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
  name or path when either changed; and that the home is now installed for the user, so the
  researcher is in every folder;
- that the new skills and commands appear in a **new** session, not this one.

Nothing is appended to `Knowledge/LOG.md`: that log records reads, audits, index refreshes and kept
synthesis pages, not version changes — the changelogs are the record of what changed.
