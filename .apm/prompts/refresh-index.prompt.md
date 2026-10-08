---
description: Rebuild Knowledge/INDEX.md at home from what is on disk — one line per note under its domain, a book's chapters beneath it — diff shown before writing. Home only; a strategy's BIBLIOGRAPHY.md is curated by hand. Only when the owner runs it by name.
---

# Refresh the index

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`.

**Home only.** `Knowledge/INDEX.md` is derived from the notes and can be rebuilt. A strategy's index
is `Bibliotheca/BIBLIOGRAPHY.md`, curated by hand — its parts, its leads and its prose are the
owner's — so it is never rebuilt: `read` writes each note's row when it writes the note, and
`audit` reports a note without a row or a row without a note. In a strategy, say so and stop.

The library's `INDEX.md` is its one index, and the first thing every query reads. Rebuild it from
the files.

1. Scan every `.md` under `Knowledge/` except its own `INDEX.md` and `LOG.md`. Group by domain
   folder. A book folder is one entry: its `INDEX.md`, and beneath it its chapter files.
2. For each note take its title from the first heading and its one-line description from
   `## What it changes`, or from the opening paragraph if the note predates that convention. For a
   book, the description says which chapters were read of how many, from its `INDEX.md` table. For
   a concept or synthesis page — `type` in the frontmatter says so — the first paragraph is the
   description.
3. Render, under each domain — headed as `RESEARCHER.md` spells it, or, for a folder it does not
   list, by the folder's name with underscores read as spaces — *Concepts* first, one line per
   concept or synthesis page, then *Sources*: one line per paper and one per book, with one indented
   line per chapter read; a standard markdown link and the description on every line. Domains in
   alphabetical order; pages and notes alphabetical inside a domain; chapters in book order. No
   per-folder indexes beyond a book's own.
4. Show the diff against the current `INDEX.md` in chat and wait for a go, *write it and save a
   version*. **Never write on a rejected or unanswered plan.**
5. Write `INDEX.md`, and append to the library's `LOG.md`: `## [YYYY-MM-DD] refresh-index | <N>
   notes indexed`.
6. **Then save a version**, in the home, on the same go, with no second question — every git
   command, the `backup` skill's send included, as `git -C "<absolute path to the home>"` when the
   session is open elsewhere: `git add Knowledge/INDEX.md Knowledge/LOG.md`, never `--all`, and
   `git commit -m "Refresh the index" -- Knowledge/INDEX.md Knowledge/LOG.md`; to the owner,
   *Saved*, in one plain line, never the commands. When `git config --get kaxanuk.autosend` prints
   `true`, it also goes to their copy on GitHub, as the `backup` skill says. If git wants a name and
   an e-mail, ask for both in one plain line, set them in the home only, never invented, and save
   again; with no `.git/`, say in one line that the home keeps no versions yet. This replaces an
   older home's *Commit?* question.

Never modify a note during a refresh. Never index anything under `Philosophy/`, `Sources/` or
`Extracts/`.
