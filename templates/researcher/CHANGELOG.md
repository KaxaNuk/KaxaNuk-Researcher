# Changelog

Every notable change to this repository, newest first: `## X.Y.Z (YYYY-MM-DD)` with
`### Added / Changed / Removed / Fixed`, and
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).
This is the researcher *skeleton*; a person's own library is their clone and is not versioned here.

## 0.7.1 (2026-09-23)

**PATCH** — `blueprint`, `brainstorm` and `challenge` take the experiment number first.

**What to do differently:** run `blueprint 1`, and `blueprint 1 D:\Research\Golden-Flow` from
home; `brainstorm 2 "an idea"` quotes an idea of more than one word. `apm update -g` brings it.

### Changed

* **`AGENTS.md`** reaches a strategy from home as `blueprint 1 D:\Research\Golden-Flow`: the
  strategy's path is optional, so it comes last.

## 0.7.0 (2026-09-22)

**MINOR** — `RESEARCHER.md` says where your view sits in the evolution of investment research and
which works to find first, from the reading map in the `read` skill.

**What to do differently:** run `apm update -g`, open a new session, and run `update` in your home;
re-run `researcher-init force` to fill the new lines, which keeps what you wrote. Deploy the agent
with `apm install --target <your agent>` (for example `--target claude`), never a bare
`apm install`, which deploys to all seven targets in `apm.yml`.

### Added

* **`RESEARCHER.md` has a *Where it sits* line** under *What you believe*: the act, the work that
  holds your view, who tested it and its other side, from the reading map — a lead, never a
  citation.
* **`RESEARCHER.md` has *Find first***: a line under each reading question with the works to find
  for it, and a closing line for a work that serves no question. A question may say its
  mind-changer is *not yet known*.
* **`AGENTS.md`**: a work to read may be proposed from the reading map, and the primitives table
  lists `reading-map.md`.

### Changed

* **`AGENTS.md` names one package throughout**, says `read` gives the `scaffold.py` command that
  copies `BIBLIOGRAPHY.md` and `LOG.md` from the template inside the package, gives
  `apm install --target <agent>` for the agent, notes that OpenCode rejects the agent's tool list,
  and says a command carries no `metadata`.
* **`RESEARCHER.md`'s strategies table ships a *none listed* row** and the note that the researcher
  joins a strategy when invited, as the interview leaves it, not a slot row it no longer fills.
* **`apm.yml`'s comment** says the package carries every Investment Lab skill itself.

### Fixed

* **`README.md` deploys the agent with `apm install --target claude`**, your assistant in place of
  `claude`, not a bare `apm install`.
* **`LICENSE` names the `read` and `query` skills and the `audit`, `refine`, `refresh-index` and
  `teach` commands**, not a `compile` command that does not exist.
* **`README.md` says `update` adds a *Brought to template* entry to `CHANGELOG.md`**, so the file
  names the template version the home is at, not only the one it was made from.
* **`AGENTS.md` names the worked example's `BRAINSTORMING_1.md`** where it said the template's;
  the strategy template ships none.

## 0.6.1 (2026-09-21)

**PATCH** — the researcher's package carries every Investment Lab skill itself.

**What to do differently:** nothing; `apm update -g` brings it.

### Changed

* **`AGENTS.md` names one package**, `KaxaNuk/KaxaNuk-Researcher`, for the skills and the commands.

## 0.6.0 (2026-09-21)

**MINOR** — the researcher is a package, `KaxaNuk/KaxaNuk-Researcher`, installed once for the user;
this template is its home, which `init-researcher` makes.

**What to do differently:** install once, `apm install -g KaxaNuk/KaxaNuk-Researcher`, which brings
every Investment Lab package from KaxaNuk-Agent-Skills with it; update with `apm update -g`. A home
from 0.5.6 or before runs `update` once.

### Changed

* **The skills and commands are a package.** `read`, `query` and the ten commands were copied into
  every home, so each carried code it could not safely edit and every version arrived by a merge.
  They now live in `KaxaNuk/KaxaNuk-Researcher`, with `extract.py` and `note.md` in the `read`
  skill's folder, and every folder the owner opens has them — the home and every strategy, which
  installs nothing.
* **`apm.yml` names no dependency.** `apm install` here deploys only the home's own agent.
* **`AGENTS.md`**: *Where the skills, the commands and the agent live* says the package is at user
  scope, lists `init-researcher`, `init-strategy` and `init-example`, and names the package's path
  under `~/.apm/` for Codex. A strategy's empty `BIBLIOGRAPHY.md` and `LOG.md` come with the
  template now, and an invited researcher brings the library, not the skills.
* **`README.md`** is a home's README: first run, working at home and in a strategy, what is in
  here. What the researcher is, and how to install it, is the package's README.

### Removed

* **`.apm/skills/`, `.apm/prompts/`, `scripts/`, `references/` and `SETUP.md`.** The package carries
  the first four, and `init-researcher` replaces `SETUP.md`.
* **The repository `KaxaNuk/KaxaNuk-Researcher-Template`** is no longer where the home comes from;
  it is `templates/researcher/` in KaxaNuk-Researcher.

## 0.5.6 (2026-09-21)

**PATCH** — the template every strategy is copied from is called the KaxaNuk Strategy Template
everywhere, and a few leftovers are gone. Nothing to do differently.

### Changed

* **One name for the strategy template.** `AGENTS.md`, `README.md`, `apm.yml`,
  `references/note.md`, `read`, `researcher-init` and `update` said *KN Research Process* where
  they meant the template at `KaxaNuk/KaxaNuk-Strategy-Template`, so there were two names for one
  repository. They now say *KaxaNuk Strategy Template*. Older entries below keep the name they
  were written with.

### Removed

* **A leftover line in `researcher-init`** about a dependency that `apm.yml` no longer declares.
* **`.gitignore` entries for things this repository never produces**: `requirements-dev.txt`,
  which was removed long ago, plus `.grok/`, `.kiro/`, `build/` and `.claude-plugin/`.

## 0.5.5 (2026-09-21)

**PATCH** — the repository is `KaxaNuk/KaxaNuk-Researcher-Template`. GitHub redirects the old
name, so every clone keeps fetching, and the package keeps its name.

**What to do differently:** in a clone whose template remote still names `KaxaNuk-Researcher`,
run the `git remote set-url` line that `update` now gives. Nothing else.

### Changed

* **The repository is KaxaNuk-Researcher-Template**, and `README.md`, `SETUP.md` and the commands
  that name it say so. Both repositories a person starts from are templates, and now both names
  say it: `KaxaNuk-Researcher` read as the researcher itself, when what it holds is the skeleton
  every researcher is cloned from. The package stays `kaxanuk-researcher`, because what
  `apm install` puts in a project is a researcher, not a template.

### Fixed

* **`update` recognises a remote at the old name.** It had one rule — no remote at the template,
  so add `upstream` and stop — and a clone whose `upstream` still named `KaxaNuk-Researcher` would
  have been told to add a remote it already has, which `git remote add` refuses. It now uses that
  remote, which still works, and gives the `git remote set-url` line that renames it.

## 0.5.4 (2026-09-21)

**PATCH** — three template lines fit the 100-column width again. Nothing to do differently.

### Fixed

* **The template's own prose keeps the width every other line here keeps.** The renames of 0.5.2
  and the index of 0.5.3 pushed three lines past 100 columns — one in `researcher-init` reached
  106 — so every home taking the update inherited them, and Luna had once committed a rewrap for
  exactly this. The same words, rewrapped; no command reads differently.

## 0.5.3 (2026-09-21)

**PATCH** — *The order of work* says what it is: an index of the template's list, not a second
copy of it. Nothing to do differently; every command behaves as before.

### Changed

* **The tie-breaker is gone.** *Working in a strategy* said "where the skill and the template's
  README disagree, the README holds" — a clause that only exists because two documents both claimed
  the order. It now says there is one source, *Starting your own strategy* in the template's README,
  and that this repository's table and the `experiment-lifecycle` skill both index it.
* **The table's *Item* column is names, not restatements.** The reasons behind the order — why the
  objective comes before any paper, why the universe comes after the claims — stay in the template's
  README. *Where it lands*, *the researcher's part* and the rule for a command asked for out of order
  are unchanged word for word, and so are the item numbers `blueprint` and `challenge` cite.
* The paragraph on items and steps is three lines instead of six; its examples named lines in a
  strategy's files that change as the strategy does.

## 0.5.2 (2026-09-20)

**PATCH** — the two repositories the researcher points at were renamed. Nothing to do differently.

### Changed

* **`blueprint`, `brainstorm` and `read` fetch from `KaxaNuk/KaxaNuk-Strategy-Template`**, and
  `researcher-init` names `KaxaNuk/KaxaNuk-Agent-Skills` as where the process knowledge lives. The
  template was `KaxaNuk-Research-Process`, which named an abstraction where the artifact is a
  repository you copy — and collided with this repository's own name, the confusion a new reader
  arrives with. The skills package was `KaxaNuk-APM`, which reads as Application Performance
  Monitoring and named the delivery mechanism rather than what the packages hold. GitHub redirects
  both old paths, so a `git fetch` written from an older copy still reaches the right place.
* **The *How it fits with the rest of KaxaNuk* table** uses both new names. The **KN Research
  Process** keeps its name throughout: the process is not the repository.

## 0.5.1 (2026-09-20)

**PATCH** — `update` knows the case it will meet most often. Nothing to do differently.

### Changed

* **`update` handles a clone that renamed the template's prose** (0.2). A home that rewrote the
  text it was given — its researcher's name and its owner's, a narrower target list, its own
  README — conflicts on nearly every template file, and nearly every conflict resolves the same
  way. The command now says so before the merge, resolves by side rather than hunk by hunk, renames
  the taken files in one pass and then reads the result for the pronouns a rename leaves behind,
  sets `apm.yml`'s version by hand because that line was kept, and names the prose the owner had
  deleted that comes back with the template's text.

## 0.5.0 (2026-09-20)

**MINOR** — two commands at the ends of the work that had none: `update`, which takes a new version
of the template into a clone without losing what makes it its owner's, and `challenge`, which
checks a finished experiment against its own blueprint. With them, everything the researcher says
about a strategy checked against a real one, and the rules it breaks in its own files fixed.

**What to do differently:** pull, run `apm install --target <your agent>`, open a new session, and
from then on run `update` instead of merging by hand. A clone whose remote is not named `upstream`
is fine: `update` finds the remote that points at the template. In a strategy, read *The order of
work* again: its rows are the template README's **items**, not the process's eight **steps**, and a
strategy's own files mean the second thing when they say *step 7*.

### Added

* **`update`** (0.1), home only. It checks the working tree is clean and that nothing is hidden by
  `skip-worktree`, finds the template's remote and fetches it, reads the `CHANGELOG` from this
  clone's version to the newest and reports every *What to do differently* in full, names the files
  that are the owner's — `RESEARCHER.md`, `Philosophy/HOW-I-INVEST.md`, `Knowledge/INDEX.md`,
  `LOG.md`, the agent, and the library itself — and what the template wanted to change in them,
  then merges after a plan and a go: template conflicts resolved, the owner's conflicts kept as
  theirs, never `researcher-init force` to pick up a new section. It reinstalls, reports, and
  appends nothing to `Knowledge/LOG.md`, which records reads, audits and refreshes. `update check`
  reports what is new and stops.
* **`challenge`** (0.1), items 7 and 8 of the order of work — the first command that runs *after*
  the work, and the only one whose default output is no file. It checks each verdict against its
  own falsifier, the tally against the rows, a verdict that answers a question the prediction did
  not ask, the run against the frozen window and costs, each success criterion before any claim of
  adoption, the notes behind the predictions, whether every falsification reached *What is closed*,
  and whether a published difference reconciles with the numbers beside it. It reads the engines'
  outputs never, quotes numbers only from `FINDINGS_N.md` and `RESULTS.md`, refuses to touch
  `BLUEPRINT_N.md`, `FINDINGS_N.md`, `RESULTS.md` or `OBJECTIVE.md`, and writes at most one
  appended `JOURNAL_N.md` entry, on the owner's go.
* **`blueprint` and `brainstorm` bootstrap from the `example` branch** (0.3 and 0.2), the way `read`
  already does: a strategy created from the template's `main` has `Experiments/.gitkeep` and no
  `BLUEPRINT_N.md` or `BRAINSTORMING_N.md`, so they give the fetch command, say what between the
  example markers is the worked strategy's, and stop rather than writing the template's headings
  from memory.

### Changed

* **The order of work counts *items*, not steps** (`AGENTS.md`, and the wording in `blueprint`,
  `objective` and `read`). The template's README says its eight are "the order of work, not the
  eight steps above: item 3, the universe, is step 2", and a strategy's own files use *step* in
  that second sense — *step 7* is the paper-trading gate, *step 8* is Production and is not in the
  repository. The table now says so instead of claiming one shared numbering.
* **A prediction may cite an analyzer measurement** (`AGENTS.md`), as `blueprint` has always said
  and the real blueprints do; only a prediction citing neither a note nor a section number is a
  lead. `audit` stops reporting those predictions as defects, and stops asking `BIBLIOGRAPHY.md`
  for a row per book chapter when the convention gives a book one row linking its `INDEX.md`.
* **`objective` takes a claim's status from the template's vocabulary** (0.3) instead of writing
  **untested** over every row — the shipped `OBJECTIVE.md` ships a claim that is *true by
  construction*, and the real first pass kept it.
* **`teach` plans before it writes** (0.2). Running it names `Projects/Teach/<topic-slug>/` as the
  only place it may write — the place, not the go: the new topic's files and each lesson wait for
  a plan and an explicit go, as `AGENTS.md` requires of every command that writes.
* **`query` stays out of the index and the log** (0.3). A kept synthesis page is written under its
  domain and nothing else; `refresh-index` is what puts it under *Concepts* and records the run.
  Its own refusal list no longer forbids the one write it makes.
* **`audit` and `refresh-index` say "only when the owner runs it by name"** in their descriptions,
  as the other eight do and `AGENTS.md` requires (0.2.2 and 0.2.1).
* **Ten commands**, in `README.md`, `AGENTS.md`, `SETUP.md` and the README's file tree.

### Fixed

* **The `example`-branch strip instruction left a dangling link.** The markers bound only Part 1 of
  `BIBLIOGRAPHY.md`; a Part 5 row links a note that does not come across, so a bootstrapped
  strategy shipped a broken relative path and a lead that read as a source already read. `read` and
  `AGENTS.md` now say to put a `[note](...)` link outside the markers back to *No note yet.* rather
  than delete the row, which is the template's.
* **`read`'s extract command wrote to the wrong folder in a strategy.** The script's `--out`
  defaults to `Extracts/` under the folder it runs in, so every run in a strategy now carries
  `--out Bibliotheca/Extracts` (0.4.1).
* **`brainstorm`'s closing reminder contradicted the file it appends to.** An idea leaves the file
  for a new experiment once the blueprint is written; before that — the benchmark choice in
  `BRAINSTORMING_1.md` — an entry feeds the blueprint that does not exist yet.
* **`researcher-init` checks for `scripts/extract.py` and `references/note.md`** (0.3). Installing
  the package into an existing project carries `.apm/` only, so `read` had no extractor and no note
  shape and nothing said so. The README says it too, for that route and for `apm pack`.
* **`SETUP.md` pointed at `git pull upstream main`** as how updates arrive; it names `update`.
* **The README** said "Eight are commands" in the one section that explains them, hard-coded
  `--target claude` in the step that had just told Codex readers what to do, and carried a
  102-character line.
* **`CHANGELOG.md`** stated its own format as *Added / Changed / Removed* while five entries use
  *Fixed*, and 0.2.0's instruction read "The run `apm install`" for "Then run".

## 0.4.2 (2026-09-19)

**PATCH** — the researcher installs the way the KN Research Process template does: paste one line
into Claude or Codex. Nothing to do differently in a researcher that is already installed.

### Added

* **`SETUP.md`**, written for an agent that was given only the URL and readable by a person in two
  minutes: the two tools, git and `uv`; the researcher's name, which is the folder's; one folder as
  the whole researcher, and the wrapper folder to avoid; a short path on Windows; the template kept
  as `upstream` so its updates can still be pulled; APM through `uv tool install apm-cli`, and the
  skills installed without asking, for the assistant doing the install; a check that a PDF can be
  read; the invitation variable, asked for rather than set; and the hand-over to
  `researcher-init` in a new session.
* **`Philosophy/HOW-I-INVEST.md`**, the page where the owner writes how they invest: four headings
  — what I believe about markets, what I have learned, how I decide, what would change my mind —
  each with a one-line prompt, and a blockquote saying the file is theirs and in their own words.
  It replaces `Philosophy/.gitkeep`. `researcher-init` fills it verbatim, heading by heading, where
  it used to create `how-i-invest.md`; `RESEARCHER.md` links it by name; and `AGENTS.md` says a
  prompt still in place is never cited as the owner's view.

### Changed

* **The README opens with the prompt to paste**, and its *Start* no longer carries the clone and
  install commands — `SETUP.md` does, and the README does not repeat it. `researcher-init` can be
  typed or asked for, and on Codex is run by naming its file.

## 0.4.1 (2026-09-17)

**PATCH** — three sentences that were true when written stop contradicting the KN Research Process
template and KaxaNuk-APM. Nothing to do differently.

### Fixed

* **The README's KaxaNuk-APM row** said no KaxaNuk package was installed and that the packages would
  come once they taught research. `investment-lab` carries the process, the Lab libraries each have
  their own package, and a strategy installs them through its own `apm.yml` — as 0.4.0's Fixed entry
  already said.
* **`Bibliotheca/Extracts/` is ignored by the template's `.gitignore`**, and has been since the
  template's 0.7.1; `AGENTS.md` still said it would be once the template carried the line. `read`
  keeps saying so in its plan for a strategy whose `.gitignore` lacks it.
* **`AGENTS.md` no longer names a version of `experiment-lifecycle`** that lists the universe before
  the objective. KaxaNuk-APM's `investment-lab` 0.7.0 follows the template's order of work; the rule
  that stays is general: where the skill and the template's README disagree, the README holds.

## 0.4.0 (2026-09-17)

**MINOR** — the researcher knows the order a strategy is built in, and arrives in a strategy whole:
the objective before any paper, and its own `CLAUDE.md`, `AGENTS.md` and `RESEARCHER.md` loaded
beside its skills when it is invited. Carried back from a researcher in use.

**What to do differently:** set `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` once on each
machine — `setx CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD 1` on Windows — quit and reopen your
assistant, run `apm install --target <your agent>`, and open a new session. In a strategy, run
`objective` before the first `read`: a strategy whose `OBJECTIVE.md` has no claims no longer takes a
note.

### Added

* **The order of work, in `AGENTS.md`.** Eight steps, the template's numbering, each with where it
  lands and the researcher's part: the objective, before any paper; the objective fine-tuned by
  reading for each claim; the investable universe, delisted names included; the data; the
  benchmark, then the blueprint, before the rule; the broad reading and the brainstorming; the
  cycle — portfolio construction, backtest, attribution — until it is finished; and every finished
  cycle into `RESULTS.md`, kept or rejected. Reading comes in two waves: narrow and per claim before
  the blueprint, so its predictions have notes to cite, and broad after it. A command asked for out
  of order names the step that comes first, and stops.
* **Checking an invitation.** `AGENTS.md` and step 5 of the README say what loads from an added
  folder: the skills, the commands and the agent on their own, and `CLAUDE.md` — with its imports,
  `AGENTS.md` and `RESEARCHER.md` — only when the variable is in the environment before launch,
  because an `env` entry in `settings.json` is applied too late for it. They say how to check it
  with `/context`, and give the fallback when the assistant does not honour the variable: a
  gitignored `CLAUDE.local.md` at the strategy's root that imports the researcher's `CLAUDE.md` by
  absolute path.
* **Joining other projects, in `AGENTS.md`.** Outside a strategy the researcher challenges on
  evidence, follows the project's own rules, writes there only after a plan and the go, and brings
  nothing home unless the owner asks — and then as a source in `Sources/` that `read` files.
* **Working lean, in `AGENTS.md`**, a default the owner may change. One short planning round,
  small changes batched into one install, one task per session, search before reading, short
  replies.
* **`.obsidian/` is gitignored**, for owners who open their library as a vault.

### Changed

* **`objective` works before the reading** (0.2). The first pass drafts the claims from the owner's
  words, each claim's evidence the question that would settle it, marked as a lead; fine-tuning
  passes rewrite the evidence from the notes, and a claim the reading sharpened is proposed, never
  changed silently.
* **`read` refuses a strategy with no claims** (0.4.0). The objective comes first; in a strategy a
  question the claims do not cover is a claim to add with `objective`, and every note serves a
  claim.
* **`blueprint` refuses without claims or without an investable universe** (0.2), naming the step
  that comes first, and closes by pointing at the broad reading, `brainstorm` and the cycle. When
  `RESULTS.md` has no analyzer measurement yet, it says so in the plan and writes the predictions
  that needed one as leads, rather than treating the empty section as normal for Experiment 1.
* **Where the `experiment-lifecycle` skill and the template's README disagree on the order, the
  README holds.** Since the KN Research Process 0.7.4 a strategy's own `README.md` links to
  *Starting your own strategy* rather than carrying it; the published skill still lists the
  universe before the objective, and `AGENTS.md` says so.

### Fixed

* **`read` no longer fetches a whole `Bibliotheca/` from the template's `example` branch.** That
  branch is a worked strategy, so the command brought another strategy's notes into a new one. It
  fetches `BIBLIOGRAPHY.md` and `LOG.md` only, says what in them is the example's to delete, and
  checks for the claims before it checks for the folder. The *Working in a strategy* table says the
  same. The fetch is two commands, because `&&` does not parse in Windows PowerShell 5.1.
* **KaxaNuk's `investment-lab` and `data-curator` packages exist**, and `investment-lab` carries
  `experiment-lifecycle`, the process as a skill. `apm.yml` and `researcher-init` said they did not
  exist or were not packaged — 0.2.0's Fixed entry recorded that; it was true when written and is
  not now. A strategy installs them through its own `apm.yml`; a home starts with none, and
  its owner adds whatever stack their own work needs.

## 0.3.0 (2026-09-11)

**MINOR** — the researcher reads a book a chapter at a time, in one note convention shared with the
KN Research Process template, keeps a wiki of concept pages, and lives in `.apm/` as two skills,
eight commands and an agent, in KaxaNuk's own format.

**What to do differently:** pull, run `apm install --target <your agent>` and open a new session,
as 0.2.0 already asks; then run `read` where you ran `compile` or `note`. Reading a PDF needs
[`uv`](https://docs.astral.sh/uv/) on the machine, or `pip install pypdf`. If your `RESEARCHER.md`
is already filled, add the section *What you are reading for* by hand — the shape is in the
template — or leave it out and `read` asks for it the next time a source arrives. A strategy needs
the matching KN Research Process template — the branch `researcher-unified-note` until it is
released — which drops `Bibliotheca/Knowledge/`, adds `Bibliotheca/LOG.md` and ignores
`Bibliotheca/Extracts/`. In an existing clone, rename `Sources/Notes/` to `Sources/Clippings/`.

### Changed

* **Every step offers options, and the go is one of them.** Where the assistant has a question
  tool, the interview's questions with options, the choice of chapters in `read` and every plan
  are asked through it — *Go*, *Change something*, *Stop* closes a plan — and when the owner has
  nothing to answer the researcher proposes, from what is already in the folder: the questions
  they might be reading for, drawn from the sources and their tables of contents; a way of
  investing to start the beliefs from. A proposal the owner picks is theirs; one they did not pick
  is never written. `researcher-init` and `read` are at 0.2 for it.
* **`.apm/` stays the only copy, and `read` is a skill in it.** Two skills in `.apm/skills/` —
  `read` and `query` — and the eight commands in `.apm/prompts/`, as 0.2.0 laid them out; `compile`
  and `note` are gone. Both are written the way KaxaNuk-APM writes its own: a skill with a folded
  description, `metadata.version`, *When to Use* and *Steps*, its folder holding `SKILL.md` and
  nothing else — what `read` runs and reads, `scripts/extract.py` and `references/note.md`, lives
  at the root of the home, so `.apm/` carries prose only; a command with an `input` list that APM
  turns into each harness's arguments, in place of `argument-hint` and `$ARGUMENTS`. The agent that
  `researcher-init` writes names `read` where it named `compile` and `note`, and `audit` checks
  the agent file as well as the installed copies.
* **One note, one convention, both repositories.** A note has the same shape at home and in a
  strategy: the KN Research Process note's frontmatter — `source`, `citation`, `local_copy`, `read`
  — plus `tags` for the owner's tag policy; the name `Author_Year_Title`; the source's claims as
  headings, in its authors' terms, and what each implies for the owner's question — or the
  strategy's claim, by number — as a blockquote; `## Why it is here` first and `## What it changes`
  last. In a strategy `read` writes the note beside the PDF in `Bibliotheca/Papers/` or `Books/`,
  its row in `BIBLIOGRAPHY.md`, and a line in `Bibliotheca/LOG.md`; `Bibliotheca/Knowledge/` is no
  longer written. A note the home library already holds travels into a strategy without re-reading
  the PDF: the source's part is carried, and the implications are written anew for the strategy's
  claims. The `writer` field is gone — git records who wrote — and the word *article* with it: every
  skill says *note*. `refresh-index` is home only, because a strategy's `BIBLIOGRAPHY.md` is
  curated by hand; `read` writes each note's row and `audit` reports the gaps.
* `compile` is `read`, rebuilt around the owner's choice. A script pulls a PDF's table of contents
  and its chapters into text; the researcher shows the table of contents, proposes *read*, *skim* or
  *skip* for each chapter against the owner's questions, reads only what they choose, and writes
  one note per chapter read. A book is a folder, with an `INDEX.md` that records what became of
  every chapter; a paper is one file. "One article per idea" gives way to one note per unit read —
  an idea that spans sources is a synthesis, written on request, linking the notes it rests on.
  The chapter and pages read go in a provenance line under the title.
* `Sources/Notes/` is `Sources/Clippings/` — articles, transcripts and threads the owner collected.
  Now that *note* names what the researcher writes, a folder of raw material could not keep the
  word. The strategy template still says `Bibliotheca/Notes/`; the table in `AGENTS.md` maps one to
  the other.
* Every skill opens with the same lines — find the home, read `RESEARCHER.md` and `AGENTS.md`, and
  in a strategy take the paths from *Working in a strategy* — and that table in `AGENTS.md` is now
  the one place that says where a path lands there, the owner's questions included. The *Which
  library* paragraph that `read`, `query` and `audit` each carried is gone.
* `refine` says what it edits — a file in `Philosophy/`, the owner's own writing — and `audit`
  says what it does: reports, appends one line to the log, never fixes on its own. Neither was
  described that way before.

### Added

* **The wiki: concept pages.** Beside the source notes, `Knowledge/` now holds one small page per
  idea the library knows about, created and updated by `read` as chapters come in — every claim on
  it citing the chapter note and its page, contradictions kept under a callout, an `## Open` list
  of what the library does not yet hold. `query` lands on those pages first and follows them to
  the notes, and offers to keep an answer that spans several notes as a synthesis page, on your
  go. `audit` lints them: a claim with no note behind it, a page that cites a PDF, a chapter whose
  ideas reached no page. `INDEX.md` lists *Concepts* before *Sources* under each domain. A strategy
  has no pages — `OBJECTIVE.md` is its synthesis. This is the LLM-wiki pattern the library was
  built on, kept: the chapter is the unit of choice and provenance, the idea is the unit of
  knowledge. `read` is at 0.3; `query`, `audit` and `refresh-index` at 0.2.
* `RESEARCHER.md` gains *What you are reading for*: the owner's open questions, numbered, each with
  what it feeds and what would change their mind, and what is out of scope for now. It is the one
  section meant to change often, and the owner edits it by hand. `researcher-init` asks for it as
  its last question. `read` reads it before every source and asks which question each one serves,
  by number, instead of a free reason — that is what `## Why it is here` now records and what
  `## What it changes` is measured against. When the section is empty at home, `read` asks for the
  questions first and offers to write them, on the owner's go; in a strategy the numbered claims in
  `OBJECTIVE.md` play that role, and nothing is written at home.
* `scripts/extract.py`, the first code in this repository, because extraction
  is deterministic and the researcher was doing it by hand, twenty pages at a time. It reads the
  PDF's outline, prints the chapters with their pages, and writes one markdown file per chapter
  asked for, a marker before every page — `pdftotext` when it is on the machine, `pypdf` otherwise,
  and it says which. It refuses a PDF with no text layer instead of guessing, takes page ranges by
  hand when a PDF has no outline, and runs with `uv run`, its one dependency declared inline, so it
  needs no install step. Its output lives in `Extracts/` at home and `Bibliotheca/Extracts/` in a
  strategy: a cache, gitignored, regenerable, never cited.
* `references/note.md`, the shape of every note the researcher writes, at home
  and in a strategy — paths and names, frontmatter, the chapter note, the paper note, the book's
  `INDEX.md` and its status vocabulary, what the indexes show, how a home note travels.

### Fixed

* **`read` on a strategy whose `Bibliotheca/` is still a `.gitkeep`.** The KN Research Process
  template released 0.7.0 with `main` as the shape alone, every file below the six folders on its
  public `example` branch, so a new strategy has no `BIBLIOGRAPHY.md` to add a row to. `read` says
  so and hands over the one `git fetch` that brings step 1 across, then stops; it never scaffolds
  that file by hand.
* **`audit` called every command a stale install.** APM translates a command's `${input:name}` into
  each harness's own placeholder on install, so comparing a deployed copy byte for byte against
  `.apm/` always differed. It compares what APM does not rewrite. Found by running `audit deep`.
* **`Knowledge/INDEX.md` ships describing the index it now builds** — Concepts before Sources.

### Removed

* `note`, merged into `read`: the strategy note is what `read` writes there.
* The `writer` frontmatter field.
* The per-skill whitelist in `.gitignore`. Deployed copies under `.claude/`, `.agents/` and the
  other agents' folders are not versioned at all; `.apm/` is. `Extracts/`, `__pycache__/` and
  `.venv/` are ignored too.

## 0.2.0 (2026-09-09)

**MINOR** — the folders are renamed, and the researcher is no longer tied to one assistant.

**What to do differently:** if you already have a clone, rename three folders — `Library/` to
`Knowledge/`, `Notes/` to `Philosophy/`, `Output/` to `Projects/` — and nothing else moves. Then
run `apm install --target <your agent>` in the folder after you pull: `/compile`, `/query` and the
rest keep their names, and they are discoverable only in a **new** session.

### Changed

* `Library/` is now `Knowledge/`, `Notes/` is now `Philosophy/`, and `Output/` is now `Projects/`.
  The directionality is unchanged: `Sources/ → Knowledge/ → Projects/`, with `Philosophy/` cited
  and never compiled from.
* The eleven commands are APM primitives in `.apm/`, the only copy of each: three **skills** in
  `.apm/skills/` — `query`, `compile`, `note`, capabilities the researcher reaches for on its own
  when the work calls for them — and eight **commands** in `.apm/prompts/`, tasks you start by
  name. `apm install --target <agent>` copies them into the folders that agent reads, which git
  ignores, so nothing is committed twice and every assistant runs the same researcher. Codex has
  no command primitive, so there a command is run by naming its prompt file. `/audit` reports an
  installed copy that has gone stale.
* `/query` and the `library-query` skill were the same procedure reached two ways, and are merged
  into one `query` skill that still answers a direct question and still fires on its own.
* `apm.yml` no longer builds anything. It declares what publishes — `.apm/` and nothing else — so
  the researcher can be installed into a project you already have, and so a person's `Sources/`
  and `Philosophy/` are structurally incapable of being packed.
* `Sources/` now has `Books/`, `Papers/` and `Notes/`, and the taxonomy is yours to extend.
  `Sources/Notes/` is raw material you collected; your own writing stays in `Philosophy/`.
* Every skill now works from wherever the session is open. Each begins by finding the researcher's
  home — the folder that holds `RESEARCHER.md` — and reading `RESEARCHER.md` and `AGENTS.md`
  there, so the researcher is itself when invited into a strategy and not only at home.
* Strategy work lives in the strategy. Invited into a repository built from the KN Research
  Process template, the researcher's library is that repository's `Bibliotheca/` — `Papers/`,
  `Books/` and `Notes/` are the sources, `Bibliotheca/Knowledge/` the articles with their own
  index and log — and `/note`, `/objective`, `/blueprint` and `/brainstorm` write into the
  strategy's own files, after the plan and your go, for you to commit. `Projects/` keeps lessons
  and what you ask for in chat at home. **Nothing flows back:** while it works on a strategy the
  researcher writes nothing at home unless you ask for that write by name, so one experiment
  cannot leak into the researcher every strategy shares.
* `/compile` asks, before it reads, why each source is there. The answer opens the article as
  `## Why it is here`, in your words — the reason you added a source decides where it files, what
  it links to, which part of a book matters and what `## What it changes` is measured against —
  and a source read for a strategy ends with the `/note` that would carry it there. It walks every
  subfolder of `Sources/`, compiles a book a part at a time, naming in the log the parts done and
  the parts to come, and reports a source it cannot open rather than filling it in from memory.
  `/brainstorm` and `/teach` now read `Philosophy/`, so how you invest weighs on what to try next
  and on what you are taught.

### Added

* The researcher can be invited into a strategy: open your assistant in the strategy's folder, add
  the researcher's folder to the session, and the skills come along.
* **The researcher is an agent, not only a way of configuring a session.** `/researcher-init` now
  writes `.apm/agents/<your researcher>.agent.md` as well, so the harness can call it by name —
  *ask Luna what we have read about momentum crashes* — with its own tool boundary: read, search
  and the skills, and nothing that writes. Its prompt points at `RESEARCHER.md` and `AGENTS.md`
  instead of copying them, so there is still one source of truth. **It never writes**, structurally
  rather than by preference: every skill that writes waits for your go, and an agent reporting back
  cannot ask for one, so it names the skill for you to run instead. Claude Code, Copilot and Cursor
  enforce the tool list; Codex drops it, which is why the rule is in the prompt too; Gemini and
  Windsurf have no agent primitive. An existing researcher gets one by running `/researcher-init`
  again — it skips the interview when `RESEARCHER.md` is already filled in and only writes the
  agent.
* Two more ways to install: `apm install KaxaNuk/KaxaNuk-Researcher --target claude` adds the
  researcher to a project you already have, and `apm pack` builds a plain plugin bundle for agents
  that do not use APM.
* `.gitattributes`, so prose checks out with the bytes it was committed with on every platform.

### Removed

* `Philosophy/Private/`, and the rule that it was read only when named. `Philosophy/` is one
  folder, read and cited in full; anything you would not want read does not go in the repository.
* The `KaxaNuk/KaxaNuk-APM/common` dependency. It installed Python style rules — pep8,
  test-writing, bloom-code — into every assistant's context, and there is almost no code in this
  repository. It returns when there is a KaxaNuk package that teaches research rather than linting.
* `requirements-dev.txt`. It pinned `apm-cli` for `pip`; the README now says where the APM CLI
  comes from, and `apm install --target <agent>` is the one step a clone needs.

### Fixed

* `apm.yml` declared `KaxaNuk/KaxaNuk-APM/data-curator` and `.../investment-lab`, which do not
  exist in that repository, so every `apm install` failed before it did anything.

## 0.1.0 (2026-09-05)

**MINOR** — the first researcher skeleton.

**What to do differently:** clone it under the name you give your researcher, open the folder in
Claude Code, run `/researcher-init`.

### Added

* The library architecture — `Sources/` read-only, `Library/` compiled with one `INDEX.md` and an
  append-only `LOG.md`, `Notes/` cited never compiled, `Notes/Private/` never read unasked,
  `Output/` written only when asked — adapted from the MIT-licensed obsidian-vault-kit, with
  standard markdown links instead of wikilinks and no dependency on any viewer.
* `RESEARCHER.md`, the personality file the `/researcher-init` interview writes: name, owner,
  domains, voice, beliefs, non-negotiables, tag policy, the strategies it works on.
* `AGENTS.md`, the operating rules, and `CLAUDE.md` pointing at both.
* Eleven commands: `researcher-init`, `compile`, `query`, `teach`, `audit`, `refine`,
  `refresh-index`, and the four that connect the researcher to a strategy built from the KN
  Research Process template — `note`, `objective`, `blueprint`, `brainstorm`.
* The `library-query` skill, which answers questions about what the library says from the index
  and the links, citing every claim.
* `apm.yml` declaring KaxaNuk's core knowledge — the `common`, `data-curator` and `investment-lab`
  packages from `KaxaNuk/KaxaNuk-APM` — so `apm install` teaches the researcher the process and the
  Lab modules.
