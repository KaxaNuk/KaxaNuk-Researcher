---
name: teach
description: A multi-session tutor grounded in Knowledge/ — interview first, then one lesson per session with a retrieval quiz; state in Projects/Teach/<topic>/. Only when the owner runs it by name, on a topic they give.
argument-hint: "<topic>"
---

# /teach

Teach `$ARGUMENTS` from what the owner has read, one lesson per session. Invoking this command is
the owner's explicit ask to write under `Projects/Teach/<topic-slug>/`, and nowhere else.

**A new topic** (no `progress.md` yet): interview the owner first — why this topic, what for, what
they already know, how they like to learn. Two to four questions. Write the mission and the
preferences into `progress.md`. Never skip the interview; never re-interview an existing topic
unless the owner says the mission has changed.

**An existing topic**: read `progress.md` — mission, track, preferences — and pick the next lesson
just beyond what stuck last time.

**Every lesson:**

1. Ground it in `Knowledge/` by the same walk as `/query`: index first, then links, then articles.
   Cite every claim with a link. If the library is thin on the topic, say so and name the sources
   to add to `Sources/` — never substitute what you happen to know for what the owner has read.
2. One tightly scoped concept, tied to the mission and, where it fits, to a strategy the owner is
   building.
3. Write it as `sessions/NNNN-<name>.md`, run it interactively in chat, and close with a short
   retrieval quiz that also touches earlier sessions.
4. Append one row to the track in `progress.md`: date, lesson, what stuck, what did not.

Never edit a past session file. Never read `Philosophy/Private/`. Never write outside
`Projects/Teach/<topic-slug>/`.
