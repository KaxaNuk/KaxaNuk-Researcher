---
name: read
description: >
  Load this skill whenever the owner asks to read, file, compile or add a source to the library — a
  PDF, a paper, a clipping — at home from Sources/ into Knowledge/, and in a strategy into a note
  beside the PDF in its Bibliotheca/ with a row in BIBLIOGRAPHY.md. It extracts a PDF by chapter
  with a script, shows the owner the table of contents, asks which chapters serve which of their
  questions or claims, reads only those, and writes one note per chapter read, after a plan and the
  owner's go; contradictions are flagged, never overwritten. It does NOT answer questions from the
  library (use `query`) and does NOT rebuild the index (the `refresh-index` command does).
metadata:
  version: 0.3.2
---

# Read — a source into the library, a chapter at a time

The owner drops a PDF or a clipping into the sources and asks to read it, file it, compile it or add
it to the library; names a source and the question or claim it should serve; or asks for a book's
table of contents before deciding what to read. What they said carries the arguments: the
strategy's path when the session is not open in it, a path under the sources to read only that,
the question or claim by number, and *outline only* to stop after the table of contents. It is not
for answering questions from the library — that is `query` — nor for rebuilding the index, which
is the `refresh-index` command.

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`. In a strategy — the session is open in a
repository with a `Bibliotheca/`, or the owner named one by path — *Working in a strategy* in
`AGENTS.md` says where each of these paths lands.

Turn sources into notes — a paper into one note, a book into one note per chapter that serves one
of the owner's questions, and nothing for a chapter they did not choose — and, at home, into the
wiki: the concept pages those chapters touch, one small page per idea, created and updated as the
sources come in. One convention serves both repositories, so a note has the same shape at home and
in a strategy; it and the concept page are in [`references/note.md`](../../../references/note.md)
at the root of the researcher's home. **You must present a plan in chat and receive an explicit go
before writing any file.**

Three jobs, kept apart. **Extracting** text from a PDF is deterministic and belongs to
`scripts/extract.py` in the researcher's home, never to reading the PDF page by page.
**Choosing** what to read is the owner's, with the table of contents in front of them.
**Reading** the chosen text and writing the note is the researcher's.

## 1. Know what happened recently

Read the last five entries of the library's log, its index end to end, and in `RESEARCHER.md` the
domains, the tag policy and the owner's open questions under *What you are reading for*. In a
strategy the index is `BIBLIOGRAPHY.md` — a row without a note is a lead, not a source — and the
questions are the claims in `OBJECTIVE.md`, by number.

**A strategy whose `Bibliotheca/` is empty** — the KN Research Process template ships `main` as the
shape alone, so a new strategy has `Bibliotheca/.gitkeep` and nothing else — cannot take a note
yet: there is no `BIBLIOGRAPHY.md` to add a row to and no convention in it to follow. Say so, and
give the one command that brings step 1 across from the template's public `example` branch, run in
the strategy's root:

```bash
git fetch https://github.com/KaxaNuk/KaxaNuk-Research-Process example && git checkout FETCH_HEAD -- Bibliotheca
```

Then stop; the owner runs it, and the read continues from there. Never scaffold `BIBLIOGRAPHY.md`
by hand: it is the template's file, with its parts and its prose.

A source already read is not read again unless the owner says so. A book begun in an earlier run is
found by its path in the log and by its `INDEX.md` — the status column says which chapters are
read, skimmed, skipped or to come — and this run continues from there.

## 2. List the sources, and extract

List what is in the sources that has no note yet — at home, every subfolder of `Sources/`; in a
strategy, every PDF under `Bibliotheca/Papers/` and `Books/` with no note beside it, and every
clipping under `Notes/` with no note in `Papers/` — or only what the owner named. The owner may
also point at a file under `Sources/` at home for a strategy: it is read for the strategy, and its
note and its extract are written there, nothing at home.

For every PDF among them, run the script — `scripts/extract.py` at the root of the researcher's
home — from the folder whose library this is, home or the strategy, and read what it prints:

```bash
uv run "<home>/scripts/extract.py" "<pdf>" --outline
```

Without `uv`: `pip install pypdf`, then `python` in place of `uv run`. The script's own `--help`
has every option. Extracts land in `Extracts/<book>/` at home and `Bibliotheca/Extracts/<book>/` in
a strategy — `--out` names the folder — one markdown file per chapter, a marker before every page.
They are a cache: regenerable, gitignored, never cited. If the strategy's `.gitignore` does not
ignore `Bibliotheca/Extracts/`, say so in the plan; the owner adds the line.

- **A PDF with no outline.** The script says so and gives the page count. Read the pages that carry
  the table of contents — the first ten to fifteen, through the assistant's PDF reader — and
  propose a split by page ranges for the owner to confirm when the table of contents is shown;
  then run the script with `--split`. A paper is one chapter: `--all`.
- **A PDF whose depth 1 is parts.** The script says so; run `--outline --depth 2`.
- **A PDF with no text layer.** The script refuses to write and says why. Report the source as
  unreadable, leave it out of the plan, and do not fill it in from memory.
- **A source that is not a PDF** — a markdown clipping, a transcript — is read directly, whole.

## 3. Show the table of contents, and ask

One message per book: the chapters as the script numbered them, with their pages, and beside each
a proposal — **read**, **skim** or **skip** — and the question it would serve, by its number under
*What you are reading for* — in a strategy, the claim's number in `OBJECTIVE.md` — judged from the
titles and the owner's questions. A paper is one line: read whole, and which question. Then ask
through the question tool: *Take the proposal as it stands*; *Change some chapters*, and they say
which in chat — *read 3, 4 and 7 for Q2, skim 5, skip the rest*; *Read everything*; *Outline only*.
Where there is no such tool, ask for the one line in chat. Do not ask about a source whose question
came with the command or was given earlier in the session. Three answers are always open: a
question the list does not have yet, which the plan offers to add to `RESEARCHER.md` in the
owner's words; *the other side of question N*; and *background reading, no question in mind*,
recorded as such.

**If the section is empty at home, propose the questions first.** Three to five candidates drawn
from this source's table of contents, the other sources under `Sources/`, and the role and beliefs
in `RESEARCHER.md`, offered through the question tool as a multi-select with *Other*. The ones the
owner picks are theirs, numbered; the plan offers to write them under *What you are reading for*,
in their words, and that is the one write this skill makes outside the library and the extracts,
at home only, said in the plan. The owner may still read a source as background, no question in
mind, but the proposal comes first. In a strategy whose `OBJECTIVE.md` has no claims yet, the
questions are whatever the owner says they are reading for, recorded in the note; the file is
theirs to fill, and nothing is written at home.

Never write a question or a reason the owner did not pick or confirm. Proposing candidates for
them to choose is how the reading keeps moving; writing one they did not choose is not. If the
owner would rather not say, the note simply has no `## Why it is here`. Stop here if the owner
asked for the outline only.

With the owner's choice in hand, extract what they chose — `--chapters 3,4,5,7`, skims included —
and nothing more.

## 4. Read what was chosen, and decide

Read each chosen extract in full — the extract, not the PDF. Where the assistant can delegate, give
each chapter to one delegate with the extract, the question and `references/note.md`, and collect
the drafts; otherwise read one chapter at a time. A skimmed chapter is read for one line: what it
holds, and why it was passed over. For each note, decide:

- **Where it goes.** At home, the domain folder; in a strategy, `Papers/` or `Books/`. For a
  chapter, the book's folder.
- **What the citation is.** `source` and `citation` come from the source itself — its title page,
  its header, its DOI — or from its row in `BIBLIOGRAPHY.md`; never from memory. A URL nobody has
  checked is not written.
- **Whether the home library has read it already.** In a strategy, when `Knowledge/` at home holds
  a note on the source, the source's part travels — the claim headings and their bullets, in the
  source's terms — and only what is the strategy's is written anew: `## Why it is here` against the
  claim, every implication blockquote, `## What it changes`. Say so in the plan. Nothing links back
  home, and the PDF is not read twice.
- **What it links to.** The existing notes it relates to, by relative path, in the same repository.
- **Which concept pages it touches.** At home only: the ideas the chapter argues in the service of
  one of the owner's questions, or that a page already covers — an existing page to update, a new
  one to create, never a page for a passing mention. Three to eight per chapter is usual. Each
  claim a page takes from the chapter cites the chapter note and its page; a claim that contradicts
  what a page holds is kept beside the old one under a `> [!WARNING]` callout naming both notes.
- **What it contradicts or supersedes.** Any claim in an existing note that the chapter conflicts
  with, quoted.
- **What the owner believes about it.** Any file in `Philosophy/` on the same subject — at home,
  to be cited from the note; in a strategy, named in prose — never compiled into it.

What you remember of a well-known book is not the book: nothing is written from memory, and nothing
from a summary.

## 5. Present the plan

In chat: for each source, the notes it becomes — target paths, each with the question or claim it
serves, by number — and, for a book, what its `INDEX.md` will record for the chapters skimmed and
skipped; in a strategy, the row each note adds to `BIBLIOGRAPHY.md` or the lead it replaces, under
the part it bears on; at home, the concept pages it creates and the ones it updates, one line each;
links; `Philosophy/` files to cite; contradictions found; new domain folders at home, if any;
questions to add to `RESEARCHER.md` at home, if any, in the owner's words; and the log
line. Then ask for the go through the question tool — *Go*, *Change something*, *Stop* — or in
chat where there is none; *go*, *proceed*, *ok* or *yes* is the go. **On *Change something*, ask
again with options, never with an open question**: the changes this plan admits, as concrete
alternatives — fewer notes or pages, different names, only the notes this run, a different domain
— and ask for the go again on the revised plan. **Never write on silence or on a rejection.**

## 6. Write, on approval only

- The notes, in the shape `references/note.md` gives and under its names: frontmatter with `source`,
  `citation`, `local_copy`, `read`, and `tags` where the owner's policy asks; the provenance line;
  `## Why it is here` with the question or claim by number and the owner's reason in their words;
  the chapter's claims as headings with the implication as a blockquote under each; and
  `## What it changes` at the end, measured against the question. For a book, its `INDEX.md` with
  every chapter's status.
- At home, the concept pages, in the shape `references/note.md` gives: `type`, `updated`, `sources`
  and `tags` in the frontmatter; every claim linked to the chapter note and its page; a
  contradiction kept under a `> [!WARNING]` callout naming both notes; the page's `## For the
  owner's questions` and `## Open` brought up to date. In a strategy, none: `OBJECTIVE.md` is its
  synthesis.
- For every contradiction the owner confirmed: keep the original claim in the older note and place
  a `> [!WARNING]` callout above it naming the newer note by link. Never delete the claim.
- At home, when the plan added questions: write them under *What you are reading for* in
  `RESEARCHER.md`, in the owner's words, numbered after the ones already there. Nothing else in
  that file changes.
- The index. At home, `Knowledge/INDEX.md`, under the domain: *Concepts* first — one line per
  concept page, title and one-line definition — then *Sources*: one line per paper; one line per
  book linking its `INDEX.md`, saying which chapters were read of how many, with one indented line
  per chapter read.
  In a strategy, `BIBLIOGRAPHY.md`: the note's row under the part it bears on — replacing the
  *No note yet* of a lead, or added where the source was not listed — and nothing else in that
  file: its parts and its prose are the owner's.
- One entry appended to the library's log — `Knowledge/LOG.md` at home, `Bibliotheca/LOG.md` in a
  strategy — in the format `AGENTS.md` gives: `read`, the notes and concept pages written and
  updated, the flags, and for a book a `read:` line naming the chapters read, skimmed, skipped and
  to come.

## 7. Report

In chat: what was written, updated and flagged; any gap the source exposed — a concept the library
leans on with no source behind it — as a suggestion for the sources; and, at home, the strategy a
note could serve, with the `read <strategy> <source>` that would carry it there.

## What this skill will not let you do

- Read a PDF page by page when the script can extract it. The table-of-contents pages of a PDF with
  no outline are the one exception.
- Write to the sources, `Philosophy/` or `Projects/`. The extracts folder is the one place outside
  the library this skill writes, and only the script writes there.
- Write at home while reading in a strategy — no note, no index line, no log entry, no question in
  `RESEARCHER.md`, no extract. A strategy's source enters the home library only when the owner puts
  it in `Sources/` at home and runs `read` there.
- Write into a strategy's `Bibliotheca/Knowledge/`. Its notes live beside its sources, and
  `BIBLIOGRAPHY.md` is its index.
- Rewrite `BIBLIOGRAPHY.md` beyond the row a note adds or replaces.
- Carry a home note's blockquotes into a strategy. The source's words travel; the implications are
  written for the strategy's claims.
- Write a note for a chapter the owner did not choose, or a question or a reason they did not give.
- Cite an extract. Notes cite the source and its pages; extracts are regenerated.
- Cite a PDF or an extract from a concept page, or build one from memory. A concept page cites
  notes and their pages; notes cite sources.
- Create a concept page for a passing mention, or one in a strategy — `OBJECTIVE.md` is the
  strategy's synthesis.
- Read a source you could not open, or fill one in from memory or from a summary.
- Write a plan or a report as a file. The chat and the log entry are the record.
- Rewrite an existing note in a different voice. Match what is there.

## References

- `scripts/extract.py`, at the root of the researcher's home: the PDF's table of contents, and its
  chapters as text, one file per chapter. `--help` has every option.
- `references/note.md`, at the root of the researcher's home: the shape of every note — paths and
  names, frontmatter, the chapter note, the paper note, the book's `INDEX.md`, what the indexes
  show, how a home note travels into a strategy — and of the concept page and the synthesis page.
