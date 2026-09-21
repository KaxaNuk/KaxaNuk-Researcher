---
description: A multi-session tutor grounded in Knowledge/ — interview first, then one lesson per session with a retrieval quiz; state in Projects/Teach/<topic>/. Only when the owner runs it by name, on a topic they give.
input:
  - topic: "The topic to teach"
metadata:
  version: 0.2
---

# Teach a topic

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`. This command works at home only.

Teach `` from what the owner has read, one lesson per session. Running this command
names `Projects/Teach/<topic-slug>/` as the only place it may write — the place, not the go: every
write still waits for a plan and an explicit go, as `AGENTS.md` requires of every command that
writes.

**A new topic** (no `progress.md` yet): interview the owner first — why this topic, what for, what
they already know, how they like to learn. Two to four questions. Then show the plan in chat — the
mission, the preferences, the folder and the files it creates — and ask for the go through the
question tool where the harness has one: *Go*, *Change something*, *Stop*. On the go, write the
mission and the preferences into `progress.md`. Never skip the interview; never re-interview an
existing topic unless the owner says the mission has changed.

**An existing topic**: read `progress.md` — mission, track, preferences — and pick the next lesson
just beyond what stuck last time.

**Every lesson:**

1. Ground it in `Knowledge/` by the same walk as `query`: index first, then links, then notes,
   and the owner's `Philosophy/` where their own view bears on the concept, cited as theirs. Cite
   every claim with a link. If the library is thin on the topic, say so and name the sources to
   add to `Sources/` — never substitute what you happen to know for what the owner has read.
2. One tightly scoped concept, tied to the mission and, where it fits, to a strategy the owner is
   building.
3. Show the lesson's plan first — the one concept, the notes it will cite, the file name — and wait
   for the go. Then write it as `sessions/NNNN-<name>.md`, run it interactively in chat, and close
   with a short retrieval quiz that also touches earlier sessions.
4. Append one row to the track in `progress.md`: date, lesson, what stuck, what did not. That row
   is part of the same run, on the same go, the way a `LOG.md` entry is; it needs no second go.

Never edit a past session file. Never write outside `Projects/Teach/<topic-slug>/`.
