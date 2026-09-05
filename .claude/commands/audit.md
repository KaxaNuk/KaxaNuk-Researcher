---
description: Read-only review of Library/ — broken links, duplicates, stale index, orphans, frontmatter; `deep` adds contradictions and gaps. Reports, never fixes on its own
argument-hint: "[deep]"
---

# /audit

Review the library and report. **Nothing is changed by this command except one entry appended to
`Library/LOG.md`.** Fixes are a plan the owner approves separately.

## Always

- Links that do not resolve, and articles nothing links to.
- Duplicate or overlapping articles — two files on one idea.
- `Library/INDEX.md` entries with no article, and articles with no index entry.
- Articles whose `source` is no longer in `Sources/`.
- Frontmatter with fields other than `source`, `read`, `tags`, `writer`, or missing one.
- Tags outside the policy in `RESEARCHER.md`, when the policy is strict.
- Concepts an article leans on that no article defines.

## With `deep` — expensive; monthly, not per session

- Contradictory claims between articles.
- A claim superseded by a newer article without a `> [!WARNING]` callout above it.
- Gaps: things the library assumes that no source in `Sources/` supports.

## Report

In chat, grouped by kind, each finding with its path. Then, if the owner wants fixes, present them
as a plan and wait for a go; approved fixes append their own log entry. Append one entry to
`Library/LOG.md`: `## [YYYY-MM-DD] audit | <N> findings` — or `audit deep`.

Never read `Notes/Private/`. Never touch `Notes/` or `Sources/`. Never fix silently.
