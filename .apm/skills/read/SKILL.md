---
name: read
description: Use whenever the owner asks to read, file or add a source to the library — Sources/ into Knowledge/ at home; in a strategy, into notes beside the PDFs in its Bibliotheca/, each with its row in BIBLIOGRAPHY.md. A script extracts a PDF by chapter; the owner sees the table of contents and picks the chapters that serve their questions or claims; one note per chapter read; plan first, the owner's go, then write; contradictions flagged, never overwritten
argument-hint: "[path to the strategy repository, if not the one the session is in] [a path under the sources to read only that] [the question or claim it serves — its number, or a phrase] [outline only]"
---

# /read

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`. In a strategy — the session is open in a
repository with a `Bibliotheca/`, or the owner named one by path — *Working in a strategy* in
`AGENTS.md` says where each of these paths lands.

Turn sources into notes — a paper into one note, a book into one note per chapter that serves one
of the owner's questions, and nothing for a chapter they did not choose. One convention serves both
repositories, so a note has the same shape at home and in a strategy; it is in
[`references/note.md`](references/note.md). **You must present a plan in chat and receive an
explicit go before writing any file.** `$ARGUMENTS`, when given: the strategy's path, when the
session is not open in it; a path under the sources, to read only that; the question or claim it
serves; *outline only*, to stop after step 3.

Three jobs, kept apart. **Extracting** text from a PDF is deterministic and belongs to
`scripts/extract.py`, never to reading the PDF page by page. **Choosing** what to read is the
owner's, with the table of contents in front of them. **Reading** the chosen text and writing the
note is the researcher's.

## 1. Know what happened recently

Read the last five entries of the library's log, its index end to end, and in `RESEARCHER.md` the
domains, the tag policy and the owner's open questions under *What you are reading for*. In a
strategy the index is `BIBLIOGRAPHY.md` — a row without a note is a lead, not a source — and the
questions are the claims in `OBJECTIVE.md`, by number. A source already read is not read again
unless the owner says so. A book begun in an earlier run is found by its path in the log and by its
`INDEX.md` — the status column says which chapters are read, skimmed, skipped or to come — and this
run continues from there.

## 2. List the sources, and extract

List what is in the sources that has no note yet — at home, every subfolder of `Sources/`; in a
strategy, every PDF under `Bibliotheca/Papers/` and `Books/` with no note beside it, and every
clipping under `Notes/` with no note in `Papers/` — or only what `$ARGUMENTS` names. The owner may
also point at a file under `Sources/` at home for a strategy: it is read for the strategy, and its
note and its extract are written there, nothing at home.

For every PDF among them, run the script that lives beside this skill — `scripts/extract.py` in
the skill's own folder, wherever the harness deployed it — from the folder whose library this is,
home or the strategy, and read what it prints:

```bash
uv run "<this skill's folder>/scripts/extract.py" "<pdf>" --outline
```

Without `uv`: `pip install pypdf`, then `python` in place of `uv run`. The script's own `--help`
has every option. Extracts land in `Extracts/<book>/` at home and `Bibliotheca/Extracts/<book>/` in
a strategy — `--out` names the folder — one markdown file per chapter, a marker before every page.
They are a cache: regenerable, gitignored, never cited. If the strategy's `.gitignore` does not
ignore `Bibliotheca/Extracts/`, say so in the plan; the owner adds the line.

- **A PDF with no outline.** The script says so and gives the page count. Read the pages that carry
  the table of contents — the first ten to fifteen, through the assistant's PDF reader — and
  propose a split by page ranges for the owner to confirm in step 3; then run the script with
  `--split`. A paper is one chapter: `--all`.
- **A PDF whose depth 1 is parts.** The script says so; run `--outline --depth 2`.
- **A PDF with no text layer.** The script refuses to write and says why. Report the source as
  unreadable, leave it out of the plan, and do not fill it in from memory.
- **A source that is not a PDF** — a markdown clipping, a transcript — is read directly, whole.

## 3. Show the table of contents, and ask

One message per book: the chapters as the script numbered them, with their pages, and beside each
a proposal — **read**, **skim** or **skip** — and the question it would serve, by its number under
*What you are reading for* — in a strategy, the claim's number in `OBJECTIVE.md` — judged from the
titles and the owner's questions. A paper is one line: read whole, and which question. Then ask the
owner to correct it in one line — *read 3, 4 and 7 for Q2, skim 5, skip the rest*. Do not ask about
a source whose question came with the command or was given earlier in the session. Three answers
are always open: a question the list does not have yet, which the plan offers to add to
`RESEARCHER.md` in the owner's words; *the other side of question N*; and *background reading, no
question in mind*, recorded as such.

**If the section is empty at home**, ask for the questions first, the way `/researcher-init` does —
what they are building or deciding, the three to seven questions the reading should answer, what
would change their mind about each, what is out of scope for now — and offer to write them under
*What you are reading for* on the owner's go, in their words. That is the one write this skill
makes outside the library and the extracts, it happens only at home, and the plan says so. In a
strategy whose `OBJECTIVE.md` has no claims yet, the questions are whatever the owner says they are
reading for, recorded in the note; the file is theirs to fill, and nothing is written at home.

Never supply a question or a reason yourself: if the owner would rather not say, the note simply
has no `## Why it is here`. Stop here if the owner asked for the outline only.

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
the part it bears on; links; `Philosophy/` files to cite; contradictions found; new domain folders
at home, if any; questions to add to `RESEARCHER.md` at home, if any, in the owner's words; and the
log line. Then wait for *go*, *proceed*, *ok* or *yes*. Revise if asked. **Never write on silence or
on a rejection.**

## 6. Write, on approval only

- The notes, in the shape `references/note.md` gives and under its names: frontmatter with `source`,
  `citation`, `local_copy`, `read`, and `tags` where the owner's policy asks; the provenance line;
  `## Why it is here` with the question or claim by number and the owner's reason in their words;
  the chapter's claims as headings with the implication as a blockquote under each; and
  `## What it changes` at the end, measured against the question. For a book, its `INDEX.md` with
  every chapter's status.
- For every contradiction the owner confirmed: keep the original claim in the older note and place
  a `> [!WARNING]` callout above it naming the newer note by link. Never delete the claim.
- At home, when the plan added questions: write them under *What you are reading for* in
  `RESEARCHER.md`, in the owner's words, numbered after the ones already there. Nothing else in
  that file changes.
- The index. At home, `Knowledge/INDEX.md`: one line per paper; one line per book linking its
  `INDEX.md`, saying which chapters were read of how many, with one indented line per chapter read.
  In a strategy, `BIBLIOGRAPHY.md`: the note's row under the part it bears on — replacing the
  *No note yet* of a lead, or added where the source was not listed — and nothing else in that
  file: its parts and its prose are the owner's.
- One entry appended to the library's log — `Knowledge/LOG.md` at home, `Bibliotheca/LOG.md` in a
  strategy — in the format `AGENTS.md` gives: `read`, the notes written and updated, the flags, and
  for a book a `read:` line naming the chapters read, skimmed, skipped and to come.

## 7. Report

In chat: what was written, updated and flagged; any gap the source exposed — a concept the library
leans on with no source behind it — as a suggestion for the sources; and, at home, the strategy a
note could serve, with the `/read <strategy> <source>` that would carry it there.

## Never

- Read a PDF page by page when the script can extract it. The table-of-contents pages of a PDF with
  no outline are the one exception.
- Write to the sources, `Philosophy/` or `Projects/`. The extracts folder is the one place outside
  the library this skill writes, and only the script writes there.
- Write at home while reading in a strategy — no note, no index line, no log entry, no question in
  `RESEARCHER.md`, no extract. A strategy's source enters the home library only when the owner puts
  it in `Sources/` at home and runs `/read` there.
- Write into a strategy's `Bibliotheca/Knowledge/`. Its notes live beside its sources, and
  `BIBLIOGRAPHY.md` is its index.
- Rewrite `BIBLIOGRAPHY.md` beyond the row a note adds or replaces.
- Carry a home note's blockquotes into a strategy. The source's words travel; the implications are
  written for the strategy's claims.
- Write a note for a chapter the owner did not choose, or a question or a reason they did not give.
- Cite an extract. Notes cite the source and its pages; extracts are regenerated.
- Read a source you could not open, or fill one in from memory or from a summary.
- Write a plan or a report as a file. The chat and the log entry are the record.
- Rewrite an existing note in a different voice. Match what is there.
