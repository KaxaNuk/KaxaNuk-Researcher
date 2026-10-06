---
description: A voice-preserving editor pass over a file in Philosophy/ — the owner's own writing — typos and slips fixed, ambiguities flagged, diff shown before anything is written; never a round file in Philosophy/Evolution/. Only when the owner runs it by name, on a path they give.
input:
  - path: "The file under Philosophy/ to edit"
---

# Refine a Philosophy file

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`. This command works at home only.

`Philosophy/` is the owner's voice, and it has exactly two writers. `philosophy` adds the owner's
typed answers to `HOW-I-INVEST.md`, word for word and add-only, after the owner's go, and writes
one round file in `Philosophy/Evolution/`, never edited afterwards; `refine` edits
`HOW-I-INVEST.md` as an editor, diff first, and never touches `Evolution/`. A file the owner keeps
beside it in `Philosophy/`, outside `Evolution/`, is theirs in the same way and takes the same
pass. `${input:path}` is one file under `Philosophy/`.

1. Confirm the path is under `Philosophy/` and not under `Philosophy/Evolution/`. A round file is a
   record of how the owner's answers moved, never edited afterwards: refuse it, say so in one line,
   and stop — whatever the owner wants changed there is a line in `HOW-I-INVEST.md`, or the next
   round of `philosophy`.
2. Read the file. Find **only** typos, doubled words, broken links and obvious slips. Preserve the
   voice, the headings, the order, the analogies, the emphasis and the bullet structure, and every
   *(round N)* tag `philosophy` put on a line, exactly as it stands: a retake finds the owner's
   earlier answers by it.
3. Where a passage is unclear or ambiguous, do not rewrite it: add a `> [!NOTE]` callout beneath it
   with the question a careful reader would ask.
4. **A line a later round changed** — the owner names it, or a round of `philosophy` sent them here
   for it: offer, as options, to leave it; to add a `> [!NOTE]` beneath it naming the later line,
   by its round; or, on the owner's explicit word, to take it out. Never reword it for them: their
   new words are already in the file, under their own tag.
5. Show the diff in chat and wait for an explicit go.
6. Apply exactly the approved diff. Report what changed.
7. **Then offer the commit.** Show the two commands it takes — `git add` with the file, by name,
   never `--all`, and `git commit -m "Refine: <file>"` — and ask `Commit?` (`¿Confirmo?`):
   *Commit it for me*, *I'll review it first*; without a question tool, the two as a numbered list
   in chat. On *Commit it for me*, run them: the owner's pick is the human act, as the go was for
   the write. On *I'll review it first*, nothing more: they commit, or say *commit it* and you run
   the commands then. Never commit unasked.

Never restructure, reorder or paraphrase. Never move a `Philosophy/` file's content into
`Knowledge/` as a side effect. Never invent content to resolve an ambiguity — flag it.
