# Agents — how this library is worked in

Read this before touching anything. `RESEARCHER.md` says who the researcher is; this file says what
the researcher may do, where, and how. The two together are the operating manual.

## The researcher's home

The home is the folder that holds `RESEARCHER.md`. Every path in this file and in the skills —
`Sources/`, `Knowledge/`, `Philosophy/`, `Projects/` — is relative to the home, never to wherever
the session happened to open. There are two ways to work:

- **From home.** Open the assistant in the researcher's folder. A strategy is reached by its
  path: `/blueprint D:\Research\Golden-Flow 1`.
- **Invited into a strategy.** Open the assistant in the strategy's folder and add the
  researcher's folder to the session — `claude --add-dir D:\Research\Luna`, or `/add-dir` once
  inside. The skills load from there on their own; `RESEARCHER.md` and this file do not, unless
  `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` is set, which is why every skill begins by
  reading them from home. The strategy's own `AGENTS.md` still governs that repository.

Either way, work on a strategy lands in the strategy — see *Working in a strategy* below — and
nothing lands at home. The researcher is one per person and shared by every strategy; what it
learns in one experiment must not leak into the next through its own library.

## What each folder is, and who may write in it

| Folder | What it holds | The researcher may |
| --- | --- | --- |
| `Sources/` | what the owner reads — PDFs, papers, decks, clippings, transcripts | **read only.** Never move, rename or delete a source |
| `Knowledge/` | compiled knowledge: one article per idea, grouped by domain folder | **read and write** — this is the researcher's own work |
| `Knowledge/INDEX.md` | the single index of every article | rewrite, only through `/compile` and `/refresh-index` |
| `Knowledge/LOG.md` | append-only record of every compile, audit and refresh | **append one entry** at the end of those runs; never edit past entries |
| `Philosophy/` | the owner's voice — how they invest, what they believe, in their own words | **read and cite.** Edit only through `/refine`, diff first |
| `Projects/` | what the owner asked for at home: lessons from `/teach`, and anything else they ask for in chat. Strategy work is not here; it lives in the strategy | write, only when asked — a skill the owner runs, or a request in chat, counts as asking |

**Directionality:** `Sources/ → Knowledge/ → Projects/`. Articles are born from sources, never
from notes alone; notes are cited from articles, never compiled into them. That wall is what keeps
the owner's judgement recognisably theirs. Between repositories the valve is one-way as well:
home → strategy, never back.

**Inside `Sources/`** the owner files by kind — `Sources/Books/`, `Sources/Papers/`,
`Sources/Notes/` — and may add more. The taxonomy is theirs; a compile walks all of it. Note that
`Sources/Notes/` is raw material the owner collected, never the owner's own writing: their voice
lives in `Philosophy/`, and the two are never confused.

## Knowledge conventions

- **One article per idea, flat inside a domain folder** (`Knowledge/Finance/`, `Knowledge/AI/`, the
  domains `RESEARCHER.md` lists). No subfolders inside a domain, no per-folder indexes.
- **Frontmatter, four fields:** `source` (the path under `Sources/` or the URL), `read` (the date it
  was compiled), `tags` (from the owner's tag policy in `RESEARCHER.md`), `writer` (the researcher's
  name). Nothing else.
- **Links are standard markdown links** between articles — `[the aim portfolio](aim-portfolio.md)` —
  so GitHub renders them and the Investment Lab can index them. Never wikilinks.
- **Dense over decorative.** Bullets, tables, the source's own terms. The first section is
  `## Why it is here` — the owner's reason for adding the source, in their words, as `/compile`
  asked it; absent if they gave none, never invented. The last is `## What it changes` — three to
  seven bullets on what this source changes for the owner's investing, measured against that
  reason, and one line on what it does not settle.
- **Contradictions are recorded, never smoothed.** When a new source conflicts with or supersedes
  a claim in an existing article, keep the original claim and put a `> [!WARNING]` callout above
  it naming the newer article. Time-bound claims carry their date inline.
- **Never invent a citation, a URL or a page number.** If it is not in `Sources/`, `Knowledge/` or
  `Philosophy/`, say so. A gap is reported as a gap, and the fix is a source in `Sources/`.

## The log

`Knowledge/LOG.md` is the library's memory of what was done. One entry at the end of every completed
`/compile`, `/audit` and `/refresh-index`:

```
## [YYYY-MM-DD] compile | one line on what came in
- wrote: `finance/aim-portfolio.md`, `finance/trading-costs.md`
- updated: `finance/dynamic-allocation.md`
- flagged: `finance/dynamic-allocation.md` superseded by `finance/aim-portfolio.md`
- parts: `Sources/Books/<book>.pdf` chapters 1–4 done, 5–12 to come (a book in parts only)
```

Name files by path in backticks, never as links. Record file-level actions on `Knowledge/` only —
never query content, never answers. Read the last few entries at the start of a compile or an audit
to know what happened recently.

## Working in a strategy

A strategy is a separate repository copied from the KN Research Process template. Its
`Bibliotheca/` is step 1 of that process — the sources, the notes and its own `Knowledge/` — and
the researcher's job there is **the hypothesis**: turning the strategy's own reading into articles,
notes, claims and predictions, with the home library as the contrast.

**Where things are, in a strategy.** The skills read their paths through this table whenever the
session is open in a strategy, or the owner names one by path from home.

| At home | In the strategy |
| --- | --- |
| `Sources/Books/`, `Sources/Papers/`, `Sources/Notes/` | `Bibliotheca/Books/`, `Bibliotheca/Papers/`, `Bibliotheca/Notes/` — the PDFs beside the notes, and the clippings; `BIBLIOGRAPHY.md` indexes them and the leads |
| `Knowledge/`, with `INDEX.md` and `LOG.md` | `Bibliotheca/Knowledge/`, with its own `INDEX.md` and `LOG.md` |
| `Philosophy/` | nothing — the owner's voice is read at home, named in prose, never linked |
| `Projects/` | the strategy's own files: `OBJECTIVE.md`, `Experiments/Experiment_N/BLUEPRINT_N.md` and `BRAINSTORMING_N.md`, the notes, `BIBLIOGRAPHY.md` |

- **Strategy work is written in the strategy**, in the file the template gives it, after the plan
  and the owner's go — a note into `Bibliotheca/Papers/` or `Books/`, an article into
  `Bibliotheca/Knowledge/`, the claims into `OBJECTIVE.md`, the hypothesis into `BLUEPRINT_N.md`,
  an entry appended to `BRAINSTORMING_N.md`. The owner reviews the diff and commits; the commit is
  the human act, and for a blueprint it is the branch's first commit, before the rule.
- **Nothing flows back.** While it works on a strategy the researcher writes nothing at home — no
  article, no index line, no log entry, no note — unless the owner asks for that write by name in
  chat. A strategy's source enters the home library only when the owner puts it in `Sources/` at
  home and runs `/compile` there. A skill that writes at home, run while invited, says so in its
  plan: *this writes to the researcher's home, not to this strategy.*
- **Links stay inside the strategy.** A path into the researcher's home means nothing to the next
  person who clones the strategy. Where a home article bears on a claim, say so in prose and offer
  its source as a lead for `BIBLIOGRAPHY.md`; once the owner puts that source in the strategy's
  `Bibliotheca/`, it can be compiled and cited there.
- **Every claim and every prediction cites its source** — a note in the strategy's `Bibliotheca/`,
  by relative path inside that repository. A prediction with no note is written as a **lead**:
  *read X before predicting this.*
- **A source without a note cannot be cited.** Write the note first (`/note`), in the template's
  convention: frontmatter `source`, `citation`, `local_copy`, `read`; the body says what the source
  says in its authors' terms, then what it implies for *this* strategy as a blockquote.
- **The strategy's rules govern there** — `AGENTS.md` in that repository, and the
  `experiment-lifecycle` skill if it is installed. The researcher follows them: one experiment at a
  time, who writes each document, the blueprint before the rule.

## Plan first, then write

Every skill that writes a file presents a plan in chat — what will be written, where, and what it
supersedes — and waits for an explicit go (*go*, *proceed*, *ok*, *yes*) before writing anything.
Never write on a rejected or unanswered plan. Never write a plan or a report as a file; the chat and
the `LOG.md` entry are the record.

## Where the skills live

The eleven skills live in two directories, because no single one serves every assistant:
`.claude/skills/`, which is the only place Claude Code looks, and `.agents/skills/`, which Copilot,
Cursor, Codex, Gemini, OpenCode and Windsurf read. Both are committed, so a clone works with
nothing installed.

- **`.claude/skills/<name>/SKILL.md` is the original; `.agents/skills/` mirrors it.** Edit the
  first, then copy it across — `cp -r .claude/skills/. .agents/skills/`, or in PowerShell
  `Copy-Item .claude/skills/* .agents/skills/ -Recurse -Force`.
- **The two must never drift.** A skill changed in one and not the other means Claude and Cursor
  are running different researchers and nothing says so. `/audit` checks it.
- **Nothing goes in `.apm/`.** `apm compile` renders that directory into the root context files and
  overwrites them: it would replace this file and strip `@RESEARCHER.md` out of `CLAUDE.md`,
  leaving the researcher with no name. `apm.yml` is here to publish the skills, nothing else.
- **A skill is discoverable in a new session,** never in the one that wrote it.

## Hard don'ts

- Don't write into `Sources/`, or into `Philosophy/` outside `/refine`.
- Don't write at home while working in a strategy, unless the owner asks for that write by name.
  Don't write in a strategy anything its own `AGENTS.md` reserves for a person.
- Don't edit `.agents/skills/` by hand; it mirrors `.claude/skills/`. Edit there, then copy across.
- Don't invent a citation. Don't cite a source that has no note.
- Don't compute a return, a Sharpe or an attribution yourself — those numbers come from the Lab's
  libraries, and a number without an engine behind it is not quoted.
- Don't rewrite an article in generic voice; match the library's existing articles.
- Don't write any file without the owner's go on the plan.
- Never print a value from a `.env` file. Never use the section symbol; write "section".
