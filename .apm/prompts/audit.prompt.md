---
description: A review of the library at hand — Knowledge/ at home, a strategy's Bibliotheca/ when invited there — broken links, duplicates, stale index, orphans, frontmatter; `deep` adds contradictions and gaps. Reports, and appends one line to the log; never fixes on its own. Only when the owner runs it by name, on the library at hand.
input:
  - mode: "Optional: deep, the expensive pass that adds contradictions and gaps"
---

# Audit the library

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`. In a strategy — the session is open in a
repository with a `Bibliotheca/`, or the owner named one by path — *Working in a strategy* in
`AGENTS.md` says where each of these paths lands.

Review the library and report; `${input:mode}` set to `deep` adds the expensive pass at the end.
**Nothing is changed by this command except one entry appended to the library's `LOG.md`** —
`Knowledge/LOG.md` at home, `Bibliotheca/LOG.md` in a strategy, never the other. Fixes are a plan
the owner approves separately.

## Step 1: Always

- Links that do not resolve, and notes nothing links to — a chapter note is linked from its book's
  `INDEX.md`.
- Duplicate or overlapping notes — two files on one source, or one chapter read twice.
- Index entries with no note, and notes with no index entry — `INDEX.md` at home, the rows of
  `BIBLIOGRAPHY.md` in a strategy; a book's `INDEX.md` whose table disagrees with the chapter files
  beside it.
- Notes whose `local_copy` names a file that is not there.
- A source note's or a book `INDEX.md`'s frontmatter with fields other than `source`, `citation`,
  `local_copy`, `read` and `tags`, or missing one of the first four; a concept or synthesis page is
  checked below.
- Tags outside the policy in `RESEARCHER.md`, when the policy is strict.
- Concepts a note leans on that no note defines.
- A note that cites an extract or links into `Extracts/`. Notes cite the source and its pages.
- Concept pages, at home: a claim with no source note behind it, or one that cites a PDF or an
  extract; a page missing `type`, `updated` or `sources`; two pages that contradict each other with
  no `> [!WARNING]` callout; a chapter note none of whose claims reached any concept page; and an
  idea a page names that no page defines.
- An installed copy missing or out of step with its source — the package under
  `~/.apm/apm_modules/` for the skills and commands, the home's own `.apm/` for the agent and for
  any skill or command of the home's own in `.apm/skills/` or `.apm/prompts/`: a skill under
  `~/.claude/skills/` or the user's folder for another agent, a command under
  `~/.claude/commands/`, the agent under `.claude/agents/` here, and the home's own skills and
  commands under `.claude/skills/` and `.claude/commands/` here, or the folder another agent
  takes. A copy of a KaxaNuk skill still deployed inside the home, in `.claude/skills/`, is a home
  from before the user-scope install: the fix is `update`. **Compare what APM does not rewrite**:
  the body below the frontmatter, and in it the section headings and the prose. APM translates a
  command's input placeholders into the form each harness takes, and rewrites the frontmatter keys
  it knows, so those differences are the install working, not a stale copy. Report a stale install
  and give the fix: `apm update -g` for a skill or a command of the package,
  `apm install --target <the owner's agent>` here for the agent or a skill or command of the home's
  own, then a new session.
- The agent file itself: missing from `.apm/agents/` when `RESEARCHER.md` is filled in, named for
  a researcher `RESEARCHER.md` no longer calls by that name, or carrying a copy of `RESEARCHER.md`
  rather than reading it. The fix for the first is `interview`, which writes it.

## Step 2: In a strategy, also

- Notes under `Bibliotheca/Papers/` or `Books/` that `BIBLIOGRAPHY.md` does not list, and lines in
  it that link to a note that does not exist. A book has one row, linking its `INDEX.md`; its
  chapter notes are listed there, not in `BIBLIOGRAPHY.md`, so a chapter without its own row is
  the convention, not a finding.
- A link from the strategy into the researcher's home. Links stay inside the strategy.
- A claim in `OBJECTIVE.md` that cites no note and is not marked as a lead, and a prediction in a
  `BLUEPRINT_N.md` that cites neither a note nor an analyzer section by its number and is not
  marked as a lead.

## Step 3: With `deep` — expensive; monthly, not per session

- Contradictory claims between notes.
- A claim superseded by a newer note without a `> [!WARNING]` callout above it.
- Gaps: things the library assumes that no source supports.

## Step 4: Report

In chat, grouped by kind, each finding with its path. Then, if the owner wants fixes, present them
as a plan and wait for a go; approved fixes append their own log entry. Append one entry to the
library's `LOG.md`: `## [YYYY-MM-DD] audit | <N> findings` — or `audit deep`. Its entries come
from `read`, `audit` and `refresh-index`, and from `query` when the owner keeps a synthesis page,
whose index line `query` adds on the same go — so a page whose line `query` added is not a
stale-index finding.

Never touch `Philosophy/` or the sources. Never fix silently. In a strategy, never write at home.
