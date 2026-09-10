---
description: Draft a strategy's OBJECTIVE.md in place — the main idea and its claims — from the strategy's Bibliotheca notes and the library, every claim citing a note; plan first, the owner's go, then write.
argument-hint: "[path to the strategy repository, if not the one the session is in]"
disable-model-invocation: true
---

# /objective

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. If
this session is open elsewhere, invited into a strategy, find the home first and read its
`RESEARCHER.md` and `AGENTS.md` before anything else.

`OBJECTIVE.md` is the first thing a CIO reads and the last thing that changes. Draft it from what
has been read, so every claim in it points back to a source. `$ARGUMENTS` is the strategy's path,
left out when the session is open in it.

## 1. Read the strategy's own material

- `OBJECTIVE.md` as it stands: the slots, and anything the owner already wrote. **The template says
  a person writes this file first.** If nothing in it is theirs yet, ask for the main idea in their
  words before drafting anything; the researcher's part is the claims and their sources.
- Every note in `Bibliotheca/Papers/` and `Bibliotheca/Books/`, and `BIBLIOGRAPHY.md` — which
  sources have notes, and which are only leads.
- `Bibliotheca/Knowledge/`, through its `INDEX.md`, for what the strategy has compiled.
- `AGENTS.md` in that repository, for the bar any new signal must clear.

## 2. Contrast with the researcher's library

Walk `Knowledge/INDEX.md` at home and the links for the domains the strategy touches. Read the
owner's `Philosophy/` on how they invest. Where the home library or a note says something the
strategy's `Bibliotheca/` does not, that is either a lead for `BIBLIOGRAPHY.md` or a warning for the
claim — never a citation, because links stay inside the strategy.

## 3. Draft, in the file's own shape

Fill the template's headings — the main idea in one sentence somebody outside the team could repeat;
the objective as a capability, not a number; the claims table with each claim's status set to
**untested**; what is not claimed. Rules:

- **Every claim cites a note** in the strategy's `Bibliotheca/`, by relative path. A claim that
  rests only on a home article is written with no link **and marked as a lead**: *write the note
  for X before this claim stands.*
- **Name the columns.** Each claim says which `c_*` or `r_*` column will carry it, if the owner
  already knows; otherwise a slot.
- **Include the source that argues against the idea** if the library holds one. An objective that
  cites only agreement is a pitch.
- Replace the italic guidance in the body with the draft, and leave the template's blockquote at
  the top: the owner deletes it when they commit, and its absence is their signature.

## 4. Show, wait, then write

Show the draft in chat and list the leads it depends on — the notes to write first, with `/note` —
and the claims the owner should sharpen. Wait for the go. Then write it into the strategy's
`OBJECTIVE.md`, keeping every line the owner wrote. The owner reviews the diff and commits; that
commit is what makes the objective theirs.

Never write into the researcher's home from here. Never compute or promise a number. The objective
is a capability and a set of claims; the numbers arrive from the Lab's engines later.
