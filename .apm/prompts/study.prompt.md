---
description: Work out an idea, a plan or a decision from the library — an idea that is not a strategy yet, or work with no repository of its own — as one study in Studies/, from the owner's words, every claim from the library linked to its note and anything from outside it marked as not checked; with no subject, list the studies. Plan first, the owner's go, then write. Home only. Only when the owner runs it by name.
input:
  - subject: "Optional: the idea, plan or decision to work out, in a phrase, or the name of a study in Studies/"
---

# Work out a study

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`: *Studies* there is the contract this command
writes to. This command works at home only, in a session open in the home. In a strategy, the next
thing to try is `brainstorm`'s and a claim is `objective`'s; in another project the owner invited
the researcher into, the work lives in that project. Say so and stop.

A study is the owner's own work from the library: an idea that is not a strategy yet, or a
decision, a plan or a brief with no repository of its own. A synthesis page that `query` keeps says
what the library holds; a study says what the owner will do about it. `${input:subject}` is the
subject in the owner's words, or the name of a study already in `Studies/`. Running this command
names `Studies/` as the only place it may write — the place, not the go: every write waits for a
plan and an explicit go, as `AGENTS.md` requires of every command that writes.

## Step 1: Which study

- **No subject.** List `Studies/`, each study by its title and its first line, and offer through
  the question tool the studies still *idea* or *active* and, as new subjects, each question under
  *What you are reading for* in `RESEARCHER.md` that feeds a decision no study works out yet. A
  subject the owner did not pick is never written. With no study and nothing to offer, say in one
  line what a study is for, and stop.
- **A study that exists** — the subject matches a file or a folder in `Studies/`, by its name or
  its title: read it whole. This is a revision.
- **A new subject:** a new study. A home without `Studies/`, made before template 0.12.0, gets the
  folder with its first study, on the same go.
- **Something another command owns:** say which, and stop unless the owner says it is a study. A
  source to read is `read`'s, a question about what the library holds is `query`'s, a belief is the
  owner's to write in `Philosophy/`, a topic to learn is `teach`'s, and work on a strategy or on a
  project with a repository of its own happens there.

## Step 2: The owner's words first

A study is never drafted from nothing. For a new one, ask two to four questions, in one round: what
they want to work out, and why now; what would settle it — the decision it feeds, or what would make
the idea worth a strategy; what they already believe or have decided; and whether anything from
outside the library comes with it — a chat, a page, a quote, a figure — and where it came from.
Where they have nothing to say, offer options drawn from `RESEARCHER.md`, `Philosophy/` and the
library; what they skip stays out, and is not a gap. For a revision, ask only what has changed.

## Step 3: The library, for and against

Walk the library the way `query` does — `Knowledge/INDEX.md` end to end, the concept pages first,
then the links between notes, then the notes — and read the owner's `Philosophy/` where their own
view bears on the subject, to cite as theirs. Gather what supports the subject, what argues against
it, and the simpler rival it has to beat. For a revision, start with the notes written since the
study's date, which `Knowledge/LOG.md` names.

Name each gap — what the study needs and the library does not hold — as a lead, labelled as `query`
labels one: a work from the reading map, a work on a *Find first* line, or a file already in
`Sources/`, not yet read; otherwise only the kind of source. Never fill a gap from memory.

## Step 4: Draft, in the study's shape

One file, named by its subject the way a concept page is — `Studies/Local_GPU_Compute.md` — or,
once it needs more than one file, a folder of that name with the study in its `README.md`. The
shape, which the owner may rename or extend:

- **The first line**, in italics: the state — *idea*, *active*, *parked*, *closed* or *moved to
  `<path>`* — and the date; what the study works out, in a line; and the question under *What you
  are reading for* it serves, by number, or none.
- **The owner's words**: the idea, the plan or the decision, and why now, as they gave them.
- **What the library says**, for and against, and the simpler rival: each point with a standard
  markdown link to its note, relative to the study's own file, and the page where the note gives
  one — `[Ang (2014)](../Knowledge/Finance/Ang_2014_Asset_Management.md)`.
- **From outside the library**, only when the owner brought something: each piece with where it
  came from and the words *not checked*. It is never cited as evidence; to count, it goes into
  `Sources/` and through `read`.
- **Where it stands**: what the owner decided, or would need to see — for an idea, the test that
  would make it a strategy and the result that would end it — and what comes next, each by the
  command that does it: `read` for a lead, `study` again once the reading is in, `init-strategy
  <name>` when the idea is ready.

Rules:

- **Every claim from the library links its note.** A source without a note is a lead, never a
  claim; never a link into `Extracts/`, never a PDF.
- **No number is computed here.** A return, a Sharpe ratio, a drawdown or an attribution is quoted
  only from the file that owns it, named beside it, as *Numbers* in the `query` skill says; a figure
  in a source comes through its note, with its page; one from outside the library is marked *not
  checked*, with where it came from.
- **Words only.** Code, data and notebooks belong in a repository of their own. When the study needs
  them, or the idea is ready to be a strategy, say so: its state becomes *moved to `<path>`*, it
  stays behind as the record, and the next thing is `init-strategy <name>` — where the study is the
  owner's words for `objective`'s first pass, named in prose, never linked — or a repository of the
  owner's own, with the researcher invited in.
- **A revision keeps every line the owner wrote.** What the new reading changes is proposed as a
  change, never made silently; the date moves, and the state moves only when the owner says so.

## Step 5: Show, wait, then write

Show the draft in chat — for a revision, the change — with its path and the leads it depends on.
Ask for the go through the question tool — *Go*, *Change something*, *Stop* — and write on *Go*
only; in chat, *go*, *proceed*, *ok* or *yes* is the go. On *Change something*, offer as options the
changes the draft admits: a narrower subject, a part left out, another name. Then write the study
and nothing else — no note, no line in `Knowledge/INDEX.md`, no entry in `Knowledge/LOG.md`, which
record the library, not the owner's work. The owner reviews the diff and commits.

Never move, rename or delete a study on your own, never write outside `Studies/`, and never cite a
study as a source — in a note, a concept page or a strategy.
