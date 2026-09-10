---
name: refresh-index
description: Rebuild the library's INDEX.md from what is on disk — Knowledge/ at home, Bibliotheca/Knowledge/ in a strategy — one line per article under its domain, diff shown before writing
---

# /refresh-index

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. If
this session is open elsewhere, invited into a strategy, find the home first and read its
`RESEARCHER.md` and `AGENTS.md` before anything else.

**Which library.** At home, the sources are `Sources/` and the library is `Knowledge/`. In a
strategy — the session is open in a repository with a `Bibliotheca/`, or the owner named one by
path — the library is that strategy's: `Bibliotheca/Papers/`, `Books/` and `Notes/` are the
sources, `Bibliotheca/Knowledge/` is the library with its own `INDEX.md` and `LOG.md`, and every
path below reads accordingly. Home's `Knowledge/` and `Philosophy/` are context there: read, named
in prose, never linked, never written.

The library's `INDEX.md` is its one index, and the first thing every query reads. Rebuild it from
the files.

1. Scan every `.md` under the library — `Knowledge/` at home, `Bibliotheca/Knowledge/` in a
   strategy — except `INDEX.md` and `LOG.md`. Group by domain folder.
2. For each article take its title from the first heading and its one-line description from
   `## What it changes`, or from the opening paragraph if the article predates that convention.
3. Render one line per article: a standard markdown link and the description. Domains in
   alphabetical order; articles alphabetical inside a domain. No per-folder indexes, ever.
4. Show the diff against the current `INDEX.md` in chat and wait for a go. **Never write on a
   rejected or unanswered plan.**
5. Write `INDEX.md`, and append to the library's `LOG.md`: `## [YYYY-MM-DD] refresh-index | <N>
   articles indexed`.

Never modify an article during a refresh. Never index anything under `Philosophy/` or the sources —
in a strategy, `BIBLIOGRAPHY.md` indexes those, and this skill does not touch it. In a strategy,
never write at home.
