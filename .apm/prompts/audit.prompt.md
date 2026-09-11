---
description: A review of the library at hand — Knowledge/ at home, a strategy's Bibliotheca/ when invited there — broken links, duplicates, stale index, orphans, frontmatter; `deep` adds contradictions and gaps. Reports, and appends one line to the log; never fixes on its own
input:
  - mode: "Optional: deep, the expensive pass that adds contradictions and gaps"
metadata:
  version: 0.1
---

# Audit the library

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`. In a strategy — the session is open in a
repository with a `Bibliotheca/`, or the owner named one by path — *Working in a strategy* in
`AGENTS.md` says where each of these paths lands.

Review the library and report; `${input:mode}` set to `deep` adds the expensive pass at the end.
**Nothing is changed by this command except one entry appended to the library's `LOG.md`** —
`Knowledge/LOG.md` at home, `Bibliotheca/LOG.md` in a strategy, never the other. Fixes are a plan
the owner approves separately.

## Step 1: Always

- Links that do not resolve, and notes nothing links to — a chapter note is linked from its book's
  `INDEX.md`.
- Duplicate or overlapping notes — two files on one source, or one chapter read twice.
- Index entries with no note, and notes with no index entry — `INDEX.md` at home, the rows of
  `BIBLIOGRAPHY.md` in a strategy; a book's `INDEX.md` whose table disagrees with the chapter files
  beside it.
- Notes whose `local_copy` names a file that is not there.
- Frontmatter with fields other than `source`, `citation`, `local_copy`, `read` and `tags`, or
  missing one of the first four.
- Tags outside the policy in `RESEARCHER.md`, when the policy is strict.
- Concepts a note leans on that no note defines.
- A note that cites an extract or links into `Extracts/`. Notes cite the source and its pages.
- An installed copy out of step with `.apm/` at home — a skill under `.claude/skills/` or
  `.agents/skills/`, a command under `.claude/commands/` or another agent's folder, or the agent
  under `.claude/agents/` — that differs from its original in `.apm/`, or is missing. Report it as
  a stale install and give the fix: `apm install --target <agent>`, then a new session.
- The agent file itself: missing from `.apm/agents/` when `RESEARCHER.md` is filled in, named for
  a researcher `RESEARCHER.md` no longer calls by that name, or carrying a copy of `RESEARCHER.md`
  rather than reading it. The fix for the first is `researcher-init`, which writes it.

## Step 2: In a strategy, also

- Notes under `Bibliotheca/Papers/` or `Books/` that `BIBLIOGRAPHY.md` does not list, and lines in
  it that link to a note that does not exist.
- A link from the strategy into the researcher's home. Links stay inside the strategy.
- A claim in `OBJECTIVE.md` or a prediction in a `BLUEPRINT_N.md` that cites no note and is not
  marked as a lead.

## Step 3: With `deep` — expensive; monthly, not per session

- Contradictory claims between notes.
- A claim superseded by a newer note without a `> [!WARNING]` callout above it.
- Gaps: things the library assumes that no source supports.

## Step 4: Report

In chat, grouped by kind, each finding with its path. Then, if the owner wants fixes, present them
as a plan and wait for a go; approved fixes append their own log entry. Append one entry to the
library's `LOG.md`: `## [YYYY-MM-DD] audit | <N> findings` — or `audit deep`.

Never touch `Philosophy/` or the sources. Never fix silently. In a strategy, never write at home.
