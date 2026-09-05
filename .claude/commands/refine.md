---
description: A voice-preserving editor pass over one of the owner's notes — typos and slips fixed, ambiguities flagged, diff shown before anything is written
argument-hint: "<path under Notes/>"
---

# /refine

`Notes/` is the owner's voice. This is the only command that may touch it, and only as an editor.
`$ARGUMENTS` is one file under `Notes/`.

1. Confirm the path is under `Notes/`. `Notes/Private/` is in scope only when the owner names the
   file explicitly.
2. Read the file. Find **only** typos, doubled words, broken links and obvious slips. Preserve the
   voice, the headings, the order, the analogies, the emphasis and the bullet structure.
3. Where a passage is unclear or ambiguous, do not rewrite it: add a `> [!NOTE]` callout beneath it
   with the question a careful reader would ask.
4. Show the diff in chat and wait for an explicit go.
5. Apply exactly the approved diff. Report what changed.

Never restructure, reorder or paraphrase. Never move a note's content into `Library/` as a side
effect. Never invent content to resolve an ambiguity — flag it.
