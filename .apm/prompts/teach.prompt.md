---
description: A multi-session tutor grounded in Knowledge/ — the library checked for the topic first, then an interview, then one lesson per session with a retrieval quiz; state in Lessons/<topic>/; with no topic, list the topics. Only when the owner runs it by name.
input:
  - topic: "Optional: the topic to teach; with none, the topics in Lessons/"
---

# Teach a topic

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`. This command works at home only.

Teach `${input:topic}` from what the owner has read, one lesson per session. Running this command
names `Lessons/<topic-slug>/`, at the home's root, as the only place it may write — the place, not
the go: every write still waits for a plan and an explicit go, as `AGENTS.md` requires of every
command that writes. The home ships no `Lessons/`: the first topic taught creates it, and each new
topic its own folder in it.

**No topic.** List the topics in `Lessons/`, each with its mission and its last session from
`progress.md`, and offer to continue one or start another; with none, say so in one line and ask
for a topic.

**First, the library.** Before any question on a new topic, walk `Knowledge/INDEX.md` for it, the
concept pages first. With no note bearing on it, say so in one line, write nothing, and offer,
through the question tool: `read` a source for it — a work on a *Find first* line of
`RESEARCHER.md`, or a lead from the reading map in the `read` skill's folder; `philosophy`, when
the topic is about investing and `Philosophy/Evolution/` holds no round; or a plain answer through
`query`, labelled as general knowledge, not the library's. Then stop.

**A new topic** (no `progress.md` yet), with notes that bear on it: interview the owner first —
why this topic, what for, what they already know, how they like to learn. Two to four questions.
When `Philosophy/Evolution/` holds a round of `philosophy`, read the newest one's level —
*Starter*, *Building* or *Researching* — instead of asking what they already know, and say so in
one line for them to correct; the newest is the latest date in the file names, and on that date
the highest suffix, `YYYY-MM-DD-2.md`. Then show the plan in chat — the mission, the preferences,
the folder and the files it creates — and ask for the go through the question tool where the
harness has one: *Go*, described as *write it and save a version*; *Change something*; *Stop*. On
the go, write the mission and the preferences into `progress.md` and save it alone, as item 5
says, with the message `Teach: <topic>, mission`. Never skip the interview; never re-interview an
existing topic unless the owner says the mission has changed.

**An existing topic**: read `progress.md` — mission, track, preferences — and pick the next lesson
just beyond what stuck last time.

**A topic still in `Projects/Teach/<topic-slug>/`** is never started afresh in `Lessons/`. Say so
and point at `update`, which moves it to `Lessons/<topic-slug>/` on the owner's go. With a
`Lessons/<topic-slug>/` as well, the owner merges the two by hand; teach it from `Lessons/` then.

**Every lesson:**

1. Ground it in `Knowledge/` by the same walk as `query`: index first, then links, then notes,
   and the owner's `Philosophy/` where their own view bears on the concept, cited as theirs, never
   a round file in `Philosophy/Evolution/`, a record, as the home's `AGENTS.md` says. Cite every
   claim with a link. If the library is thin on the topic, say so and name the sources to add to
   `Sources/` — never substitute what you happen to know for what the owner has read.
2. One tightly scoped concept, tied to the mission and, where it fits, to a strategy the owner is
   building.
3. Show the lesson's plan first — the one concept, the notes it will cite, the file name — and wait
   for the go, *write it and save a version*. Then write it as `sessions/NNNN-<name>.md`, run it
   interactively in chat, and close with a short retrieval quiz that also touches earlier sessions.
4. Append one row to the track in `progress.md`: date, lesson, what stuck, what did not. That row
   is part of the same run, on the same go, the way a `LOG.md` entry is; it needs no second go.
5. **Then save a version**, on the same go, with no second question: `git add` the session file
   and `progress.md`, by name, never `--all`, and `git commit -m "Teach: <topic>, session <N>"`;
   to the owner, *Saved*, in one plain line, never the commands. When
   `git config --get kaxanuk.autosend` prints `true`, it also goes to their copy on GitHub, as the
   `backup` skill says. If git wants a name and an e-mail, ask for both in one plain line, set them
   in this folder only, never invented, and save again; with no `.git/`, say in one line that the
   home keeps no versions yet. This replaces an older home's *Commit?* question.
6. Close the lesson with one line, offered and never pressed: a round of `philosophy` — round 1
   when `Philosophy/Evolution/` holds none, else the next, naming the last round's date — for
   whenever they want to write down how they invest, in their words, as what they learn moves it.

Never edit a past session file. Never write outside `Lessons/<topic-slug>/` — a round of
`philosophy` is that skill's own run, with its own preview and go, never part of a lesson.
