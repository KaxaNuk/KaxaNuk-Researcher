# Changelog

Every notable change to this repository, newest first: `## X.Y.Z (YYYY-MM-DD)` with
`### Added / Changed / Removed`, and [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
This is the researcher *skeleton*; a person's own library is their clone and is not versioned here.

## 0.2.0 (2026-09-09)

**MINOR** — the folders are renamed, and the researcher is no longer tied to one assistant.

**What to do differently:** if you already have a clone, rename three folders — `Library/` to
`Knowledge/`, `Notes/` to `Philosophy/`, `Output/` to `Projects/` — and nothing else moves. The
commands are skills now, so `/compile`, `/query` and the rest still work by the same names, but
they are discoverable only in a **new** session after you pull.

### Changed

* `Library/` is now `Knowledge/`, `Notes/` is now `Philosophy/`, and `Output/` is now `Projects/`.
  The directionality is unchanged: `Sources/ → Knowledge/ → Projects/`, with `Philosophy/` cited
  and never compiled from.
* The eleven commands are eleven **skills**. Skills are the one primitive every assistant supports,
  and on the ones with slash commands a skill still gives you `/name` — so nothing is lost on
  Claude Code and six more assistants are gained. They live in two committed directories, because
  no single one serves everybody: `.claude/skills/`, which is the only place Claude Code reads and
  where you edit them, and `.agents/skills/`, mirrored for Copilot, Cursor, Codex, Gemini, OpenCode
  and Windsurf. A clone needs nothing installed. `/audit` reports it if the two drift apart.
* `/query` and the `library-query` skill were the same procedure reached two ways, and are merged
  into one `query` skill that still answers a direct question and still fires on its own.
* `apm.yml` no longer builds anything. It declares what publishes — `.claude/skills/` and nothing
  else — so the skills can be installed into a project you already have, and so a person's
  `Sources/` and `Philosophy/` are structurally incapable of being packed.
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
* Two more ways to install: `apm install KaxaNuk/KaxaNuk-Researcher` adds the skills to a project
  you already have, and `apm pack` builds a plain plugin bundle for agents that do not use APM.
* `.gitattributes`, so prose checks out with the bytes it was committed with on every platform.

### Removed

* `Philosophy/Private/`, and the rule that it was read only when named. `Philosophy/` is one
  folder, read and cited in full; anything you would not want read does not go in the repository.
* The `KaxaNuk/KaxaNuk-APM/common` dependency. It installed Python style rules — pep8,
  test-writing, bloom-code — into every assistant's context, and there is almost no code in this
  repository. It returns when there is a KaxaNuk package that teaches research rather than linting.
* `requirements-dev.txt`. It pinned `apm-cli`, which nothing here needs: the skills are committed,
  and the APM CLI matters only to install them into another project — the README says where it
  comes from.

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
