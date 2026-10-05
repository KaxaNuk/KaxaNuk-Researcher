---
description: A multi-session tutor grounded in Knowledge/ — interview first, then one lesson per session with a retrieval quiz; state in Lessons/<topic>/. Only when the owner runs it by name, on a topic they give.
input:
  - topic: "The topic to teach"
---

# Teach a topic

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`. This command works at home only.

Teach `${input:topic}` from what the owner has read, one lesson per session. Running this command
names `Lessons/<topic-slug>/`, at the home's root, as the only place it may write — the place, not
the go: every write still waits for a plan and an explicit go, as `AGENTS.md` requires of every
command that writes. The home ships no `Lessons/`: the first topic taught creates it, and each new
topic its own folder in it.

**A new topic** (no `progress.md` yet): interview the owner first — why this topic, what for, what
they already know, how they like to learn. Two to four questions. When `Philosophy/Evolution/`
holds a round of `philosophy`, read the newest one's level — *Starter*, *Building* or
*Researching* — instead of asking what they already know, and say so in one line for them to
correct; the newest is the latest date in the file names, and on that date the highest suffix,
`YYYY-MM-DD-2.md`. Then show the plan in chat — the mission, the preferences, the folder and the
files it creates — and ask for the go through the question tool where the harness has one: *Go*,
*Change something*, *Stop*. On the go, write the mission and the preferences into `progress.md`.
Never skip the interview; never re-interview an existing topic unless the owner says the mission
has changed.

**An existing topic**: read `progress.md` — mission, track, preferences — and pick the next lesson
just beyond what stuck last time.

**A topic still in `Projects/Teach/<topic-slug>/`**, from a home made before template 0.10.0:
never start it afresh in `Lessons/`. Say so and point at `update`, which offers to move it to
`Lessons/<topic-slug>/` on the owner's go, as often as a `Projects/` remains — or at the one line
that does it by hand, `git mv Projects/Teach/<topic-slug> Lessons/<topic-slug>`, after
`mkdir -p Lessons`. When a `Lessons/<topic-slug>/` exists as well, the owner merges the two by
hand; teach the topic from `Lessons/` once it is there.

**Every lesson:**

1. Ground it in `Knowledge/` by the same walk as `query`: index first, then links, then notes,
   and the owner's `Philosophy/` where their own view bears on the concept, cited as theirs. Round
   files in `Philosophy/Evolution/` are a record of how the owner's answers moved: read them for
   dates and levels, and cite `HOW-I-INVEST.md`, never a round file, as the owner's view. Cite
   every claim with a link. If the library is thin on the topic, say so and name the sources to
   add to `Sources/` — never substitute what you happen to know for what the owner has read.
2. One tightly scoped concept, tied to the mission and, where it fits, to a strategy the owner is
   building.
3. Show the lesson's plan first — the one concept, the notes it will cite, the file name — and wait
   for the go. Then write it as `sessions/NNNN-<name>.md`, run it interactively in chat, and close
   with a short retrieval quiz that also touches earlier sessions.
4. Append one row to the track in `progress.md`: date, lesson, what stuck, what did not. That row
   is part of the same run, on the same go, the way a `LOG.md` entry is; it needs no second go.
5. Close the lesson with one line, offered and never pressed: a round of `philosophy` — round 1
   when `Philosophy/Evolution/` holds none, else the next, naming the last round's date — for
   whenever they want to write down how they invest, in their words, as what they learn moves it.

Never edit a past session file. Never write outside `Lessons/<topic-slug>/` — a round of
`philosophy` is that skill's own run, with its own preview and go, never part of a lesson.
