---
name: note
description: Use whenever a source note is to be written into a strategy's Bibliotheca/ — the owner asks for one, or a compile, objective or blueprint left a lead. Writes it in the KN Research Process convention with its line in BIBLIOGRAPHY.md — plan first, the owner's go, then write.
argument-hint: "[path to the strategy repository, if not the one the session is in] <source: a file under the strategy's Bibliotheca/, a path under Sources/ at home, or a citation>"
---

# /note

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. If
this session is open elsewhere, invited into a strategy, find the home first and read its
`RESEARCHER.md` and `AGENTS.md` before anything else.

A strategy repository cites a source only through a note in its `Bibliotheca/`. This skill writes
that note, in the strategy. `$ARGUMENTS` is the source, preceded by the strategy's path when the
session is not already open in it.

## 1. Read the convention where it lives

Open `<strategy>/Bibliotheca/BIBLIOGRAPHY.md` and follow its note convention exactly — the four
frontmatter fields (`source`, `citation`, `local_copy`, `read`), the paper and book body shapes, and
the four rules: the implication is a blockquote; a heading states the source's claim, never a
verdict; contradictions stay visible; never invent a URL or a page number. Read one existing note in
that folder, if there is one, and match it.

## 2. Read the source, and what the strategy believes

Read the source in full — from the strategy's `Bibliotheca/` if it is there, from `Sources/` at
home if the owner pointed there, otherwise from where they pointed. If the strategy's
`Bibliotheca/Knowledge/` already has an article on it, read that too and reuse its reading; if the
home library has one, read it as the researcher's own reading, and link nothing from it. Read the
strategy's `OBJECTIVE.md`, because the blockquoted implication has to be about *this* strategy's
claims, not about finance in general.

## 3. Draft, and wait

Show the note in chat, and the line it adds to `BIBLIOGRAPHY.md` — under the part it bears on,
replacing the *No note yet* lead if one is there. The implication blockquote says what this source
changes about the strategy's claims, and names the claim by its number in `OBJECTIVE.md`. If the
source argues *against* a claim, say so; that is the most useful note there is. Then wait for the
owner's go.

## 4. Write, on approval only

Write the note to `Bibliotheca/Papers/Author_Year_Title.md` — or `Books/Author_Year_Title/INDEX.md`
for a book — and the line into `BIBLIOGRAPHY.md`, inside the strategy. The owner reviews the diff
and commits. If the file came from `Sources/` at home, say so: the note records where it lives,
and a copy sits beside the note only if the owner puts it there — it is gitignored in the strategy.

Never write into the researcher's home from here — no article, no index line, no log entry. If the
source is not yet compiled in the strategy's `Bibliotheca/Knowledge/`, offer a `/compile` there.
Never write a note for a source you have not read. A note from a summary is a summary.
