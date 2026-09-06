---
name: audit
description: Read-only review of Knowledge/ — broken links, duplicates, stale index, orphans, frontmatter; `deep` adds contradictions and gaps. Reports, never fixes on its own
argument-hint: "[deep]"
---

# /audit

Review the library and report. **Nothing is changed by this command except one entry appended to
`Knowledge/LOG.md`.** Fixes are a plan the owner approves separately.

## Always

- Links that do not resolve, and articles nothing links to.
- Duplicate or overlapping articles — two files on one idea.
- `Knowledge/INDEX.md` entries with no article, and articles with no index entry.
- Articles whose `source` is no longer in `Sources/`.
- Frontmatter with fields other than `source`, `read`, `tags`, `writer`, or missing one.
- Tags outside the policy in `RESEARCHER.md`, when the policy is strict.
- Concepts an article leans on that no article defines.
- `.agents/skills/` out of step with `.claude/skills/` — any skill present in one and not the
  other, or differing between them. Report it as drift and give the copy command; the researcher
  runs on both, and a difference means two different researchers.

## With `deep` — expensive; monthly, not per session

- Contradictory claims between articles.
- A claim superseded by a newer article without a `> [!WARNING]` callout above it.
- Gaps: things the library assumes that no source in `Sources/` supports.

## Report

In chat, grouped by kind, each finding with its path. Then, if the owner wants fixes, present them
as a plan and wait for a go; approved fixes append their own log entry. Append one entry to
`Knowledge/LOG.md`: `## [YYYY-MM-DD] audit | <N> findings` — or `audit deep`.

Never read `Philosophy/Private/`. Never touch `Philosophy/` or `Sources/`. Never fix silently.
