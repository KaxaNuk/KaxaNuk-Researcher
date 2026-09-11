---
description: Rebuild Knowledge/INDEX.md at home from what is on disk — one line per note under its domain, a book's chapters beneath it — diff shown before writing. Home only; a strategy's BIBLIOGRAPHY.md is curated by hand
---

# /refresh-index

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`.

**Home only.** `Knowledge/INDEX.md` is derived from the notes and can be rebuilt. A strategy's index
is `Bibliotheca/BIBLIOGRAPHY.md`, curated by hand — its parts, its leads and its prose are the
owner's — so it is never rebuilt: `/read` writes each note's row when it writes the note, and
`/audit` reports a note without a row or a row without a note. In a strategy, say so and stop.

The library's `INDEX.md` is its one index, and the first thing every query reads. Rebuild it from
the files.

1. Scan every `.md` under `Knowledge/` except its own `INDEX.md` and `LOG.md`. Group by domain
   folder. A book folder is one entry: its `INDEX.md`, and beneath it its chapter files.
2. For each note take its title from the first heading and its one-line description from
   `## What it changes`, or from the opening paragraph if the note predates that convention. For a
   book, the description says which chapters were read of how many, from its `INDEX.md` table.
3. Render one line per paper and one per book, with one indented line per chapter read: a standard
   markdown link and the description. Domains in alphabetical order; notes alphabetical inside a
   domain; chapters in book order. No per-folder indexes beyond a book's own.
4. Show the diff against the current `INDEX.md` in chat and wait for a go. **Never write on a
   rejected or unanswered plan.**
5. Write `INDEX.md`, and append to the library's `LOG.md`: `## [YYYY-MM-DD] refresh-index | <N>
   notes indexed`.

Never modify a note during a refresh. Never index anything under `Philosophy/`, `Sources/` or
`Extracts/`.
