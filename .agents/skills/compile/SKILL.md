---
name: compile
description: File what is in Sources/ into Knowledge/ — plan first, the owner's go, then write; contradictions flagged, never overwritten
argument-hint: "[a path under Sources/ to compile only that]"
---

# /compile

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. If
this session is open elsewhere, invited into a strategy, find the home first and read its
`RESEARCHER.md` and `AGENTS.md` before anything else.

Turn raw sources into library articles. **You must present a plan in chat and receive an explicit go
before writing any file.**

## 1. Know what happened recently

Read the last five entries of `Knowledge/LOG.md` and `Knowledge/INDEX.md` end to end. A source
already compiled is not compiled again unless the owner says so.

## 2. Survey the sources

List what is in `Sources/` — every subfolder, `Books/`, `Papers/`, `Notes/` and any the owner has
added — or only under `$ARGUMENTS` when given — that has no article yet. For each, read it and
decide:

- **Where it goes.** An existing article to update, or a new article and its domain folder. One
  article per idea, so a long paper may become several articles and two thin sources may merge.
- **Whether it is too big for one run.** A book is compiled a part at a time. Propose the split in
  the plan — by chapter, or by the sections that carry distinct ideas — and compile the parts the
  owner picks. The log entry names the parts done, so the rest can follow in later runs.
- **What it links to.** The existing articles it relates to, by path.
- **What it contradicts or supersedes.** Any claim in a touched article that the new source
  conflicts with, quoted.
- **Which notes it touches.** Any file in `Philosophy/` on the same subject, to be cited from the
  article — never compiled into it.

## 3. Present the plan

In chat: sources → target paths, links, notes to cite, contradictions found, new domain folders if
any. Then wait for *go*, *proceed*, *ok* or *yes*. Revise if asked. **Never write on silence or on a
rejection.**

## 4. Write, on approval only

- One article per target path. Frontmatter with exactly four fields — `source`, `read`, `tags`,
  `writer` — then the body in the source's own terms: dense bullets and tables, standard markdown
  links to related articles, and `## What it changes` at the end: three to seven bullets on what
  this changes for the owner's investing, plus one line on what it does not settle.
- For every contradiction the owner confirmed: keep the original claim in the older article and
  place a `> [!WARNING]` callout above it naming the newer article by link. Never delete the claim.
- Update `Knowledge/INDEX.md`: one line per article under its domain — a link and the sentence
  that says what the article settles.
- Append one entry to `Knowledge/LOG.md` in the format `AGENTS.md` gives.

## 5. Report

In chat: what was written, updated and flagged, and any gap the source exposed — a concept the
library leans on with no source behind it — as a suggestion for `Sources/`.

## Never

- Write to `Sources/`, `Philosophy/` or `Projects/` during a compile.
- Generate an article from a note alone; articles are born from sources.
- Write a plan or a report as a file. The chat and the log entry are the record.
- Rewrite an existing article in a different voice. Match what is there.
