---
description: Rebuild Library/INDEX.md from what is on disk — one line per article under its domain, diff shown before writing
---

# /refresh-index

`Library/INDEX.md` is the one index of the library, and the first thing every query reads. Rebuild
it from the files.

1. Scan every `.md` under `Library/` except `INDEX.md` and `LOG.md`. Group by domain folder.
2. For each article take its title from the first heading and its one-line description from
   `## What it changes`, or from the opening paragraph if the article predates that convention.
3. Render one line per article: a standard markdown link and the description. Domains in
   alphabetical order; articles alphabetical inside a domain. No per-folder indexes, ever.
4. Show the diff against the current `INDEX.md` in chat and wait for a go. **Never write on a
   rejected or unanswered plan.**
5. Write `INDEX.md`, and append to `Library/LOG.md`: `## [YYYY-MM-DD] refresh-index | <N> articles
   indexed`.

Never modify an article during a refresh. Never index anything under `Notes/` or `Sources/`.
