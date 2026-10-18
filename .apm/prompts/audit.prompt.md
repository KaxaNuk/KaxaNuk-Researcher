---
description: A review of the library at hand — Knowledge/ at home, a strategy's Bibliotheca/ when invited there — broken links, duplicates, stale index, orphans, frontmatter, unread sources and clippings behind their project, checked by a script; `deep` adds contradictions and gaps. Reports, and appends one line to the log; never fixes on its own. Only when the owner runs it by name, on the library at hand.
input:
  - mode: "Optional: deep, the expensive pass that adds contradictions and gaps"
---

# Audit the library

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`. In a strategy — the session is open in a
repository with a `Bibliotheca/`, or the owner named one by path — *Working in a strategy* in
`AGENTS.md` says where each of these paths lands. With no home in the session, audit the strategy
alone — the checks that read `RESEARCHER.md` or the home's installed copies are skipped — and say
so.

Review the library and report; `${input:mode}` set to `deep` adds the expensive pass at the end.
**Nothing is changed by this command except one entry appended to the library's `LOG.md`** —
`Knowledge/LOG.md` at home, `Bibliotheca/LOG.md` in a strategy, never the other. That line is one
of the three writes made without a go of their own, as *Plan first, then write* in the home's
`AGENTS.md` says: running `audit` by name is the go for it. Fixes are a plan the owner approves
separately.

**In the worked example, nothing is appended.** When the folder is the worked example — its
`README.md` or `AGENTS.md` holds a line reading `<!-- example: begin -->`, the test `next` uses —
report in chat and write nothing. The example is for reading and running, never built on; a
strategy of the owner's own is `init-strategy <name>`.

## Step 1: Always

**First, the library check**: `scripts/check_library.py`, in the `read` skill's folder wherever the
harness installed it, run from the library's root, at home and in a strategy alike. It reads and
edits nothing, and needs only the standard library:

```bash
uv run --no-project python "<the read skill's directory>/scripts/check_library.py"
```

It makes the same checks the same way on every run, each finding with its file and line, grouped
by kind: links that do not resolve or that leave the repository; a note, page or study that cites
an extract, and a page or study that cites a PDF; notes and pages nothing links to; the index
against the notes, `INDEX.md` at home and the rows of `BIBLIOGRAPHY.md` in a strategy, where a book
has one row and a row marked *No note yet* is a lead; each book's `INDEX.md` against the chapter
files beside it; the frontmatter's fields, and a `read` that gives only a date; two notes on one
file; at home, a chapter note no concept page names, a page's claim that links no note, and a study
whose first line gives no state; every source no note's `local_copy` names, whatever its name or
its date; and the notes whose `local_copy` is not on this computer, as one line with their count,
since PDFs are ignored by git and a fresh clone or a copy `init-example` made holds none —
`--verbose` lists them. At home it also finds **a clipping behind its project**: a note on a
project in `RESEARCHER.md`'s projects table, a KaxaNuk library say, that states a version older than
the newest in the `CHANGELOG.md` at the project's path, the only file of the project it opens. A
row whose path is a folder of projects — `~/Lab`, holding a folder per library — is read as one
project per folder inside it with a `CHANGELOG.md`, and the report's last lines name the rows it
could not check: say so, rather than read *none of: stale clipping* as all clear. `--help` has the
rest.

Report its findings as it groups them, and never make again by hand a check it makes. An unread
source's fix is `read <the source>`; one it names beside a note of the same first author and year
may be that note's under another path, and its fix is the note's `local_copy`, on the owner's go. A
stale clipping's fix is the project's new `README.md` and `CHANGELOG.md` copied into
`Sources/Clippings/` on the go, then `read`: the old note stays, under a `> [!WARNING]` callout
naming the new one.

Then what the script leaves to judgement:

- Duplicate or overlapping notes it cannot see: one source read twice under two paths, or one
  chapter read twice under two numbers.
- A `read` field whose words do not say what was read — the whole paper, the abstract, the
  chapters, as the `read` skill's `references/note.md` asks: a note on an abstract that does not say
  so claims more than it read.
- Tags outside the policy in `RESEARCHER.md`, when the policy is strict.
- Concepts a note leans on that no note defines.
- Concept pages, at home: a claim its note does not support; two pages that contradict each other
  with no `> [!WARNING]` callout; and an idea a page names that no page defines.
- Studies, at home: the owner's words in a study are theirs, never a finding.
- An installed copy missing or out of step with its source. The source is the package under
  `~/.apm/apm_modules/` for the skills and commands, and the home's own `.apm/` for the agent and
  for any skill or command of the home's own in `.apm/skills/` or `.apm/prompts/`. The installed
  copies: a skill under `~/.claude/skills/` or the user's folder for another agent, a command under
  `~/.claude/commands/`, and the home's own — the agent, the researcher's skill, and any skill or
  command of its own — under `~/.claude/agents/`, `~/.claude/skills/` and `~/.claude/commands/`,
  or the user's folder another agent takes. A copy of a KaxaNuk skill still deployed inside the
  home, in `.claude/skills/`, or the agent in `.claude/agents/` here, is a home from before the
  user-scope install: the fix is `update`. **Compare what APM does not rewrite**: the body below
  the frontmatter, and in it the section headings and the prose. APM translates a command's input
  placeholders into the form each harness takes, and rewrites the frontmatter keys it knows, so
  those differences are the install working, not a stale copy. Report a stale install
  and give the fix: `uvx --from apm-cli==0.33.0 apm update -g` for a skill or a command of the
  package, `uvx --from apm-cli==0.33.0 apm install -g "<the home>"` for the agent, the
  researcher's skill, or a skill or command of the home's own, then a new session.
- The agent file itself: missing from `.apm/agents/` when `RESEARCHER.md` is filled in, named for
  a researcher `RESEARCHER.md` no longer calls by that name, or carrying a copy of `RESEARCHER.md`
  rather than reading it. The fix for the first is `interview`, which writes it.
- The researcher's skill: missing from `.apm/skills/<slug>/` when the agent is there; naming a
  home other than this folder — the home has moved — or behind the template in `interview`, an
  older `metadata.version` or a folder named with anything but a to z, digits and hyphens; or
  carrying a copy of `RESEARCHER.md` beyond the name, the owner and the path. The fix for the
  first is `interview`, for the second `update`, which writes it again.

## Step 2: In a strategy, also

The library check already holds `BIBLIOGRAPHY.md` against the notes and finds a link out of the
strategy, into the researcher's home included. Beyond it:

- A claim in `OBJECTIVE.md` that has none of the three kinds of evidence a claim may cite — a note,
  `RESULTS.md` or the `FINDINGS_N.md` that measured it, or its being **true by construction** — and
  is not marked as a lead. A prediction in a `BLUEPRINT_N.md` that cites neither a note nor an
  analyzer section by its number and is not marked as a lead.
- A claim's status that does not open with a word of the vocabulary the template's `OBJECTIVE.md`
  lists. A qualifier after it is fine — *true by construction, untested as a source of return* —
  but a status word of the strategy's own means something different in every strategy.
- A performance figure of the strategy's own — a CAGR, a Sharpe, a drawdown, an attribution
  share — in a document the researcher drafts, `OBJECTIVE.md`, a `BLUEPRINT_N.md` or a
  `BRAINSTORMING_N.md`, that appears in neither `FINDINGS_N.md` nor `RESULTS.md`. Every number
  about a book comes from the engines the project names, and a figure that is in neither file came
  from somewhere else. A figure matches at the precision it is quoted: *0.08* matches *+0.080*, and
  *13.8* matches *13.84*. Not a figure any of these documents quotes from a paper through a note it
  cites, and not an analyzer measurement cited by its section: those are sources, not the
  strategy's results.

## Step 3: With `deep` — expensive; monthly, not per session

- Contradictory claims between notes.
- A claim superseded by a newer note without a `> [!WARNING]` callout above it.
- Gaps: things the library assumes that no source supports.
- Figures a note states that its source does not: run `scripts/check_numbers.py`, in the `read`
  skill's folder wherever the harness installed it, over the library's notes — at home
  `uv run "<the read skill's directory>/scripts/check_numbers.py" Knowledge --extracts Extracts`,
  in a strategy `Bibliotheca/Papers Bibliotheca/Books --extracts Bibliotheca/Extracts` — from the
  library's root. It looks each figure written beside a page citation up in the extract, leaving
  out years and the numbers of equations, sections, tables, figures, chapters and pages. Report
  every figure *not found* as a finding, with its note, line and cited pages. A note it reports at
  an **offset** cites printed pages, not the extract's PDF pages: one finding for the note, with the
  offset, since `references/note.md` cites PDF pages and gives a book's offset once in its
  `INDEX.md` — its figures at that offset are found, and not findings each. Report the unchecked
  notes as a count, with the `extract.py` command the script prints to regenerate their extracts.
  A figure not found may be the note's own arithmetic or quoted from another source: say which,
  where the note says so. One in a table, an equation or a figure may be on the page and lost by
  the extract: look at the cited page as an image before reporting it, with `render_pages.py` in
  the same folder — `uv run "<the read skill's directory>/scripts/render_pages.py" "<the PDF>"
  <page> --dpi 200`, `--region` for a part of it — and read the image it prints the path of, which
  it writes outside the library. Say what the image shows. Neither script edits anything, and this
  pass fixes nothing either.
- In a strategy, a part of `BIBLIOGRAPHY.md` whose sources only agree with the claims — above all
  *Part 1 — The core idea*, which the template says holds the sources that argue against them. A
  bibliography with no source against the idea is a pitch.

## Step 4: Report

In chat, grouped by kind, each finding with its path. Then, if the owner wants fixes, present them
as a plan and wait for a go; approved fixes append their own log entry. A fix to concept pages — a
chapter's claims brought to the pages it touches, a source added to a page — goes through
`update_concept_pages.py`, in the `read` skill's folder: its spec on standard input, never a file in
the library; run without `--write` its diff is the plan, and the go runs it with `--write`. Append
one entry to the library's `LOG.md`: `## [YYYY-MM-DD] audit | <N> findings` — or `audit deep` —
except in the worked example, where nothing is written. Its entries come from `read`, `audit` and
`refresh-index`, and from `query` when the owner keeps a synthesis page, whose index line `query`
adds on the same go — so a page whose line `query` added is not a stale-index finding.

**Then save a version**, in the folder whose library this is, at home and in a strategy alike, once
the log line is in and any fix the owner approved is written. No question is asked: the line and
each fix's plan already had their go. Every git command, the `backup` skill's send included, runs
as `git -C "<that folder>"` when the session is open elsewhere: `git add` the library's `LOG.md`
and every file a fix changed, by name, never `--all`, and
`git commit -m "Audit: <the log line's summary>" -- <the same files>`. To the owner, *Saved*, in
one plain line, never the commands. In a strategy it is a version of its own, with no
`CHANGELOG.md` entry, version bump or ruff gate: the next change-set's entry names it. When
`git config --get kaxanuk.autosend` prints `true`, it also goes to the owner's copy on GitHub, as
the `backup` skill says. If git wants a name, ask in one open message, with no options, *What's your
name, or what would you like me to call you?*, never invented, and no e-mail; set it in that folder
only, with `user.email` as `"<>"`, an empty address, and save again; with no `.git/`, say in one
line that the folder keeps no versions yet. This replaces an older home's *Commit?* question, and
the owner's own commit in a strategy.

Never touch `Philosophy/`, `Studies/` or the sources. Never fix silently. In a strategy, never write
at home.
