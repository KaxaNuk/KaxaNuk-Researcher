---
description: Draft a strategy's OBJECTIVE.md — the main idea and its claims — from the strategy's Bibliotheca notes and the library, every claim citing a note; to Output/
argument-hint: "<path to the strategy repository>"
---

# /objective

`OBJECTIVE.md` is the first thing a CIO reads and the last thing that changes. Draft it from what has
been read, so every claim in it points back to a source. `$ARGUMENTS` is the strategy's path.

## 1. Read the strategy's own material

- `OBJECTIVE.md` as it stands: the slots, and anything the owner already wrote.
- Every note in `Bibliotheca/Papers/` and `Bibliotheca/Books/`, and `BIBLIOGRAPHY.md` — which
  sources have notes, and which are only leads.
- `AGENTS.md` in that repository, for the bar any new signal must clear.

## 2. Contrast with the library

Walk `Library/INDEX.md` and the links for the domains the strategy touches. Read the owner's
`Notes/` on how they invest. Where the library or a note says something the strategy's Bibliotheca does not,
that is either a lead for the strategy or a warning for the claim.

## 3. Draft, in the file's own shape

Fill the template's headings — the main idea in one sentence somebody outside the team could repeat;
the objective as a capability, not a number; the claims table with each claim's status set to
**untested**; what is not claimed. Rules:

- **Every claim cites a note** in the strategy's `Bibliotheca/`, by relative path as it will sit in
  that repository. A claim that rests only on a library article is written with the article as its
  source **and marked as a lead**: *write the note for X before this claim stands.*
- **Name the columns.** Each claim says which `c_*` or `r_*` column will carry it, if the owner
  already knows; otherwise a slot.
- **Include the source that argues against the idea** if the library holds one. An objective that
  cites only agreement is a pitch.
- Keep the template's guidance blockquotes out of the draft; the owner deletes them when the file is
  real.

## 4. Deliver

Write `Output/<strategy name>/OBJECTIVE.draft.md`, show it in chat, and list the leads it depends
on — the notes to write first, with `/note` — and the claims the owner should sharpen. Never write
into the strategy repository; the owner copies the draft in and commits it.

Never compute or promise a number. The objective is a capability and a set of claims; the numbers
arrive from the Lab's engines later.
