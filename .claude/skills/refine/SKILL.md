---
name: refine
description: A voice-preserving editor pass over a file in Philosophy/ — the owner's own writing — typos and slips fixed, ambiguities flagged, diff shown before anything is written. Only when the owner runs it by name, on a path they give.
argument-hint: "<path under Philosophy/>"
---

# /refine

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`. This skill works at home only.

`Philosophy/` is the owner's voice. This is the only skill that may touch it, and only as an
editor. `$ARGUMENTS` is one file under `Philosophy/`.

1. Confirm the path is under `Philosophy/`.
2. Read the file. Find **only** typos, doubled words, broken links and obvious slips. Preserve the
   voice, the headings, the order, the analogies, the emphasis and the bullet structure.
3. Where a passage is unclear or ambiguous, do not rewrite it: add a `> [!NOTE]` callout beneath it
   with the question a careful reader would ask.
4. Show the diff in chat and wait for an explicit go.
5. Apply exactly the approved diff. Report what changed.

Never restructure, reorder or paraphrase. Never move a `Philosophy/` file's content into
`Knowledge/` as a side effect. Never invent content to resolve an ambiguity — flag it.
