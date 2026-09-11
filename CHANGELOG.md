# Changelog

Every notable change to this repository, newest first: `## X.Y.Z (YYYY-MM-DD)` with
`### Added / Changed / Removed`, and [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
This is the researcher *skeleton*; a person's own library is their clone and is not versioned here.

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
`Knowledge/`, `Notes/` to `Philosophy/`, `Output/` to `Projects/` — and nothing else moves. The
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
