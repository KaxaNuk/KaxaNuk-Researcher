---
name: brainstorm
description: Draft a dated BRAINSTORMING_N.md entry for a strategy — the next thing to try, considered against the library — to Projects/. Only when the owner runs it by name, on a strategy they name.
argument-hint: "<path to the strategy repository> <N> [the idea, in a phrase]"
---

# /brainstorm

Brainstorming is forward-looking planning, done before the work, and never mistaken for the record
of what happened. `$ARGUMENTS` is the strategy's path, the experiment number `N`, and optionally the
idea to think about.

1. **Read the experiment's state.** `BLUEPRINT_N.md`, `BRAINSTORMING_N.md` (the entries so far),
   `FINDINGS_N.md` if it reports, and `RESULTS.md` — what is closed, what is open, what stands. Do
   not open another experiment's files unless the owner has recorded the request and reason in
   `JOURNAL_N.md`.
2. **Contrast with the library and the notes.** What has the owner read that bears on the idea?
   What argues against it? Is there a simpler rival — the cheap version of the idea that the
   complicated one has to beat?
3. **Draft one entry** in the template's format — *Idea / question*, *What we tried / considered*,
   *Outcome / decision*, *Open threads* — dated today, newest at the bottom. Every source named is a
   link to a `Bibliotheca/` note or a `Knowledge/` article; a source without a note is a lead.
4. **Deliver** to `Projects/<strategy name>/BRAINSTORMING_N.entry.md`, show it in chat, and say
   where it goes: appended to the strategy's `BRAINSTORMING_N.md` by the owner. Never write into
   the strategy repository.

Remind the owner, once, that an idea committed to leaves this file for a new blueprint — a new
experiment — and is not edited into the current one.
