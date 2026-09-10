---
name: compile
description: File the sources into the library — Sources/ into Knowledge/ at home, a strategy's Bibliotheca/ into its own Knowledge/ — asks why each source is there, plans, waits for the owner's go, then writes; contradictions flagged, never overwritten
argument-hint: "[a path under the sources to compile only that] [why it is there, in a phrase]"
---

# /compile

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. If
this session is open elsewhere, invited into a strategy, find the home first and read its
`RESEARCHER.md` and `AGENTS.md` before anything else.

**Which library.** At home, the sources are `Sources/` and the library is `Knowledge/`. In a
strategy — the session is open in a repository with a `Bibliotheca/`, or the owner named one by
path — the library is that strategy's: `Bibliotheca/Papers/`, `Books/` and `Notes/` are the
sources, `Bibliotheca/Knowledge/` is the library with its own `INDEX.md` and `LOG.md`, and every
path below reads accordingly. Home's `Knowledge/` and `Philosophy/` are context there: read, named
in prose, never linked, never written.

Turn raw sources into library articles. **You must present a plan in chat and receive an explicit go
before writing any file.** `$ARGUMENTS`, when given, is a path under the sources to compile only
that, optionally followed by why it is there.

## 1. Know what happened recently

Read the last five entries of the library's `LOG.md`, its `INDEX.md` end to end, and the domains
and tag policy in `RESEARCHER.md`. In a strategy, read `Bibliotheca/BIBLIOGRAPHY.md` too — the
sources it lists, and which are still leads. A source already compiled is not compiled again unless
the owner says so. A book begun in an earlier run is found by its path in the log — the last entry
that names it says which parts are done — and this run continues from there, never from the first
page again.

## 2. List the sources, and ask why they are there

List what is in the sources that has no article yet — at home every subfolder of `Sources/`,
`Books/`, `Papers/`, `Notes/` and any the owner has added; in a strategy the PDFs, clippings and
transcripts under `Bibliotheca/Papers/`, `Books/` and `Notes/`, never the notes beside them — or
only under `$ARGUMENTS` when given.

Then, **before reading any of it, ask the owner why each source is there.** One message, one line
per source; the owner may answer for a group at once. They put it there for a reason — a strategy
or a claim it should feed, a belief it should test, a claim they want the other side of, a gap
`/query` or `/audit` named, or plain curiosity — and that reason decides where the article files,
what it links to, which part of a book matters, and what `## What it changes` is measured against.
Do not ask about a source whose reason came with the command or was given earlier in the session.
*Background reading, no strategy in mind* is an answer, and is recorded as such. Never supply a
reason yourself: if the owner would rather not say, the article simply has no `## Why it is here`.

## 3. Read, and decide

Read each source in full — for a book, the parts the reason points at first. For each, decide:

- **Where it goes.** An existing article to update, or a new article and its domain folder. One
  article per idea, so a long paper may become several articles and two thin sources may merge.
- **Whether it is too big for one run.** A book is compiled a part at a time. Propose the split in
  the plan — by chapter, or by the sections that carry distinct ideas, the owner's reason first —
  and compile the parts the owner picks. The log entry names the parts done and the parts still to
  come, so the rest can follow in later runs.
- **What it links to.** The existing articles it relates to, by path, in the same library.
- **What it contradicts or supersedes.** Any claim in a touched article that the new source
  conflicts with, quoted.
- **What the owner believes about it.** Any file in `Philosophy/` on the same subject — at home,
  to be cited from the article; in a strategy, named in prose — never compiled into it.

A source that will not open — a scanned PDF with no text layer, a format the assistant cannot read,
a file that fails to load — is reported as unreadable and left out of the plan. What you remember of
a well-known book is not the book: nothing is compiled from memory.

## 4. Present the plan

In chat: sources → target paths, each with the owner's reason in a phrase; links; `Philosophy/`
files to cite; contradictions found; new domain folders if any; and for a book, the parts this run
takes. Then wait for *go*, *proceed*, *ok* or *yes*. Revise if asked. **Never write on silence or on
a rejection.**

## 5. Write, on approval only

- One article per target path. Frontmatter with exactly four fields — `source`, `read`, `tags`,
  `writer` — `source` being the path under the sources, or the URL; the tags by the policy in
  `RESEARCHER.md`, and under a loose policy a strategy the owner named is one of them. Then the
  title, then `## Why it is here`: the owner's reason in one or two lines, in their words, naming
  the strategy or the claim if they did. Then the body in the source's own terms: dense bullets and
  tables, time-bound claims dated inline, standard markdown links to related articles in the same
  library — never across repositories — and `## What it changes` at the end: three to seven
  bullets on what this changes for the owner's investing, measured against the reason they gave,
  plus one line on what it does not settle.
- For every contradiction the owner confirmed: keep the original claim in the older article and
  place a `> [!WARNING]` callout above it naming the newer article by link. Never delete the claim.
- Update the library's `INDEX.md`: one line per article under its domain — a link and the sentence
  that says what the article settles.
- Append one entry to the library's `LOG.md` in the format `AGENTS.md` gives; for a book in parts,
  a line naming the parts done and the parts still to come.

## 6. Report

In chat: what was written, updated and flagged; any gap the source exposed — a concept the library
leans on with no source behind it — as a suggestion for the sources; and the note the source still
lacks — at home, the `/note` that would carry it into a strategy the owner named; in a strategy,
the `/note` that lets `OBJECTIVE.md` and `BLUEPRINT_N.md` cite it.

## Never

- Write to the sources, `Philosophy/` or `Projects/` during a compile.
- Write at home while compiling in a strategy — no article, no index line, no log entry. A
  strategy's source enters the home library only when the owner puts it in `Sources/` at home and
  runs `/compile` there.
- Generate an article from a `Philosophy/` file or a strategy note alone; articles are born from
  sources.
- Compile a source you could not read, or fill one in from memory.
- Write a reason the owner did not give. `## Why it is here` is their words or it is absent.
- Write a plan or a report as a file. The chat and the log entry are the record.
- Rewrite an existing article in a different voice. Match what is there.
