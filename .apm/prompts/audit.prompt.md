---
description: Read-only review of the library at hand — Knowledge/ at home, a strategy's Bibliotheca/ when invited there — broken links, duplicates, stale index, orphans, frontmatter; `deep` adds contradictions and gaps. Reports, never fixes on its own
argument-hint: "[deep]"
---

# /audit

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. If
this session is open elsewhere, invited into a strategy, find the home first and read its
`RESEARCHER.md` and `AGENTS.md` before anything else.

**Which library.** At home, the sources are `Sources/` and the library is `Knowledge/`. In a
strategy — the session is open in a repository with a `Bibliotheca/`, or the owner named one by
path — the library is that strategy's: `Bibliotheca/Papers/`, `Books/` and `Notes/` are the
sources, `Bibliotheca/Knowledge/` is the library with its own `INDEX.md` and `LOG.md`, and every
path below reads accordingly. Home's `Knowledge/` and `Philosophy/` are context there: read, named
in prose, never linked, never written.

Review the library and report. **Nothing is changed by this skill except one entry appended to
the library's `LOG.md`** — `Knowledge/LOG.md` at home, `Bibliotheca/Knowledge/LOG.md` in a
strategy, never the other. Fixes are a plan the owner approves separately.

## Always

- Links that do not resolve, and articles nothing links to.
- Duplicate or overlapping articles — two files on one idea.
- `INDEX.md` entries with no article, and articles with no index entry.
- Articles whose `source` is no longer among the sources.
- Frontmatter with fields other than `source`, `read`, `tags`, `writer`, or missing one.
- Tags outside the policy in `RESEARCHER.md`, when the policy is strict.
- Concepts an article leans on that no article defines.
- An installed copy out of step with `.apm/` at home — a skill under `.claude/skills/` or
  `.agents/skills/`, a command under `.claude/commands/` or another agent's folder, or the agent
  under `.claude/agents/` — that differs from its original in `.apm/`, or is missing. Report it as
  a stale install and give the fix: `apm install --target <agent>`, then a new session.
- The agent file itself: missing from `.apm/agents/` when `RESEARCHER.md` is filled in, named for
  a researcher `RESEARCHER.md` no longer calls by that name, or carrying a copy of `RESEARCHER.md`
  rather than reading it. The fix for the first is `/researcher-init`, which writes it.

## In a strategy, also

- Notes under `Bibliotheca/Papers/` or `Books/` that `BIBLIOGRAPHY.md` does not list, and lines in
  it that link to a note that does not exist.
- A link from the strategy into the researcher's home. Links stay inside the strategy.
- A claim in `OBJECTIVE.md` or a prediction in a `BLUEPRINT_N.md` that cites no note and is not
  marked as a lead.

## With `deep` — expensive; monthly, not per session

- Contradictory claims between articles.
- A claim superseded by a newer article without a `> [!WARNING]` callout above it.
- Gaps: things the library assumes that no source supports.

## Report

In chat, grouped by kind, each finding with its path. Then, if the owner wants fixes, present them
as a plan and wait for a go; approved fixes append their own log entry. Append one entry to the
library's `LOG.md`: `## [YYYY-MM-DD] audit | <N> findings` — or `audit deep`.

Never touch `Philosophy/` or the sources. Never fix silently. In a strategy, never write at home.
