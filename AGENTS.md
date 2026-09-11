# Agents — how this library is worked in

Read this before touching anything. `RESEARCHER.md` says who the researcher is and what its owner
is reading for; this file says what the researcher may do, where, and how. The two together are the
operating manual.

## The researcher's home

The home is the folder that holds `RESEARCHER.md`. Every path in this file and in the skills —
`Sources/`, `Knowledge/`, `Philosophy/`, `Projects/` — is relative to the home, never to wherever
the session happened to open. There are two ways to work:

- **From home.** Open the assistant in the researcher's folder. A strategy is reached by its
  path: `blueprint D:\Research\Golden-Flow 1`.
- **Invited into a strategy.** Open the assistant in the strategy's folder and add the
  researcher's folder to the session — `claude --add-dir D:\Research\Luna`, or `/add-dir` once
  inside. The skills and commands load from there on their own, provided `apm install` has been
  run there once on this machine; `RESEARCHER.md` and this file do not, unless
  `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` is set, which is why every skill begins by
  reading them from home. The strategy's own `AGENTS.md` still governs that repository.

Either way, work on a strategy lands in the strategy — see *Working in a strategy* below — and
nothing lands at home. The researcher is one per person and shared by every strategy; what it
learns in one experiment must not leak into the next through its own library.

## What each folder is, and who may write in it

| Folder | What it holds | The researcher may |
| --- | --- | --- |
| `Sources/` | what the owner reads — PDFs, papers, decks, clippings, transcripts | **read only.** Never move, rename or delete a source |
| `Extracts/` | the text the read skill's script pulls out of the PDFs in `Sources/` — one file per chapter, a marker before every page | **write, through `scripts/extract.py` only.** A cache: regenerable, gitignored, never cited, never edited by hand |
| `scripts/` | the code the skills run — `extract.py`, which pulls a PDF's table of contents and chapters into `Extracts/` | **run.** Edited only when the owner asks |
| `references/` | what the skills read on demand — `note.md`, the shape of every note | **read.** Edited only when the owner asks |
| `Knowledge/` | what the researcher read — one note per paper, one folder per book with a note per chapter read — and its wiki: one concept page per idea, grouped by domain folder | **read and write** — this is the researcher's own work |
| `Knowledge/INDEX.md` | the single index of every note and page | rewrite, only through `read` and `refresh-index` |
| `Knowledge/LOG.md` | append-only record of every read, audit and refresh | **append one entry** at the end of those runs; never edit past entries |
| `Philosophy/` | the owner's voice — how they invest, what they believe, in their own words | **read and cite.** Edit only through `refine`, diff first |
| `Projects/` | what the owner asked for at home: lessons from `teach`, and anything else they ask for in chat. Strategy work is not here; it lives in the strategy | write, only when asked — a skill the owner runs, or a request in chat, counts as asking |

`RESEARCHER.md` is not a folder, but it is the owner's too. `researcher-init` writes it once, from
the interview; `read`, at home, may add a question under *What you are reading for* — in the
owner's words, after their go — and nothing else writes it. The owner edits it by hand whenever they
like.

**Directionality:** `Sources/ → Extracts/ → Knowledge/ → Projects/`. Notes are born from sources,
never from `Philosophy/` alone; `Philosophy/` is cited from notes, never compiled into them. That
wall is what keeps the owner's judgement recognisably theirs. Between repositories the valve is
one-way as well: home → strategy, never back.

**Inside `Sources/`** the owner files by kind — `Sources/Books/`, `Sources/Papers/`,
`Sources/Clippings/` — and may add more. The taxonomy is theirs; a read walks all of it. Note that
`Sources/Clippings/` is raw material the owner collected — articles, transcripts, threads — never
the owner's own writing, which lives in `Philosophy/`, and never a note, which is what the
researcher writes from it.

## Knowledge conventions

- **One note per unit read, inside a domain folder** (`Knowledge/Finance/`, `Knowledge/AI/`, the
  domains `RESEARCHER.md` lists). A paper is one file. A book is a folder — the only kind of
  subfolder a domain has — with an `INDEX.md` for its chapters and one file per chapter read;
  nothing is written for a chapter the owner did not choose, and no other per-folder index exists.
  Beside the notes, the **wiki**: one **concept page** per idea the library holds, small and
  specific, created and updated by `read` as chapters come in — never for a passing mention, never
  from memory — every claim on it citing a note and its page; and **synthesis pages**, a `query`
  answer the owner chose to keep. Pages cite notes; a note never cites a page. A strategy has no
  pages: `OBJECTIVE.md` is its synthesis. The shape of every note and page is in
  `references/note.md`.
- **Frontmatter, the four fields the KN Research Process note carries, and one more:** `source`
  (where the work lives outside the repository — a DOI, a URL, a publisher; never invented),
  `citation` (the reference, with the date the link was last checked), `local_copy` (the file read,
  by path in this repository — under `Sources/` at home — or `none`), `read` (the date, and what was
  read — the whole paper, or the chapters), and `tags` (from the owner's tag policy in
  `RESEARCHER.md`; optional in a strategy). Nothing else. A note is named `Author_Year_Title.md`, a
  book folder `Author_Year_Title/`, a chapter file `NN_Chapter_Title.md`. A concept or synthesis
  page carries `type`, `updated`, `sources` and `tags` instead, and is named by its idea,
  `Position_Sizing_Rules.md`.
- **Links are standard markdown links** between notes — `[the aim portfolio](aim-portfolio.md)` —
  so GitHub renders them and the Investment Lab can index them. Never wikilinks.
- **Dense over decorative.** Bullets, tables, the source's own terms. The first line is the
  provenance — the chapter and pages read. The first section is `## Why it is here` — the question
  in `RESEARCHER.md` the source serves, by number, and the owner's reason in their words, as `read`
  asked it; absent if they gave none, never invented. The body is the source's claims as headings,
  each with the implication for that question as a blockquote — the only part that is the
  researcher's. The last is `## What it changes` — three to seven bullets on what this source
  changes for the owner's investing, measured against that question, and one line on what it does
  not settle.
- **Contradictions are recorded, never smoothed.** When a new source conflicts with or supersedes
  a claim in an existing note, keep the original claim and put a `> [!WARNING]` callout above it
  naming the newer note. Time-bound claims carry their date inline.
- **Never invent a citation, a URL or a page number.** If it is not in `Sources/`, `Knowledge/` or
  `Philosophy/`, say so. A gap is reported as a gap, and the fix is a source in `Sources/`.

## The log

`Knowledge/LOG.md` is the library's memory of what was done. One entry at the end of every completed
`read`, `audit` and `refresh-index`:

```
## [YYYY-MM-DD] read | one line on what came in
- wrote: `Finance/Ilmanen_2011_Expected_Returns/INDEX.md`, `Finance/Ilmanen_2011_Expected_Returns/03_The_Equity_Premium.md`
- updated: `Finance/Ang_2014_Asset_Management.md`
- flagged: `Finance/Ang_2014_Asset_Management.md` superseded by `Finance/Ilmanen_2011_Expected_Returns/03_The_Equity_Premium.md`
- read: `Sources/Books/Ilmanen_2011_Expected_Returns.pdf` — 3, 4 read; 5 skimmed; 1–2, 6–12 skipped (a book only)
```

Name files by path in backticks, never as links. Record file-level actions on `Knowledge/` only —
never query content, never answers. Read the last few entries at the start of a read or an audit to
know what happened recently.

## Working in a strategy

A strategy is a separate repository copied from the KN Research Process template. Its
`Bibliotheca/` is step 1 of that process — the sources, and the notes beside them — and
the researcher's job there is **the hypothesis**: turning the strategy's own reading into notes,
claims and predictions, with the home library as the contrast.

**Where things are, in a strategy.** The skills read their paths through this table whenever the
session is open in a strategy — a repository with a `Bibliotheca/` — or the owner names one by path
from home. Home's `Knowledge/` and `Philosophy/` are context there: read, named in prose, never
linked, never written.

| At home | In the strategy |
| --- | --- |
| `Sources/Books/`, `Sources/Papers/`, `Sources/Clippings/` | `Bibliotheca/Books/`, `Bibliotheca/Papers/`, `Bibliotheca/Notes/` — the template's name for the clippings — the PDFs beside the notes, and the clippings; `BIBLIOGRAPHY.md` indexes them and the leads |
| `Knowledge/`, with `INDEX.md` and `LOG.md` | the notes in `Bibliotheca/Papers/` and `Books/`, beside their PDFs; `BIBLIOGRAPHY.md` is the index and `Bibliotheca/LOG.md` the log. No concept pages: `OBJECTIVE.md` is the strategy's synthesis |
| `Extracts/` | `Bibliotheca/Extracts/` — the same cache, beside the strategy's PDFs; gitignored there once the template carries the line |
| `Philosophy/` | nothing — the owner's voice is read at home, named in prose, never linked |
| `Projects/` | the strategy's own files: `OBJECTIVE.md`, `Experiments/Experiment_N/BLUEPRINT_N.md` and `BRAINSTORMING_N.md`, the notes, `BIBLIOGRAPHY.md` |
| *What you are reading for* in `RESEARCHER.md` — the numbered questions | the numbered claims in `OBJECTIVE.md`; while it has none, whatever the owner says they are reading for, and the file is theirs to fill |

- **Strategy work is written in the strategy**, in the file the template gives it, after the plan
  and the owner's go — a note into `Bibliotheca/Papers/` or `Books/` with its row in
  `BIBLIOGRAPHY.md`, the claims into `OBJECTIVE.md`, the hypothesis into `BLUEPRINT_N.md`,
  an entry appended to `BRAINSTORMING_N.md`. The owner reviews the diff and commits; the commit is
  the human act, and for a blueprint it is the branch's first commit, before the rule.
- **Nothing flows back.** While it works on a strategy the researcher writes nothing at home — no
  note, no index line, no log entry, no extract — unless the owner asks for that write by name in
  chat. A strategy's source enters the home library only when the owner puts it in `Sources/` at
  home and runs `read` there. A skill that writes at home, run while invited, says so in its
  plan: *this writes to the researcher's home, not to this strategy.*
- **Links stay inside the strategy.** A path into the researcher's home means nothing to the next
  person who clones the strategy. Where a home note bears on a claim, say so in prose and offer
  its source as a lead for `BIBLIOGRAPHY.md`; once the owner puts that source in the strategy's
  `Bibliotheca/`, it can be read and cited there.
- **Every claim and every prediction cites its source** — a note in the strategy's `Bibliotheca/`,
  by relative path inside that repository. A prediction with no note is written as a **lead**:
  *read X before predicting this.*
- **A source without a note cannot be cited.** Write the note first (`read`), in the one convention
  both repositories share — its shape is in `references/note.md`: the source's
  claims as headings, in its authors' terms, and what each implies for *this* strategy as a
  blockquote, naming the claim by number.
- **The strategy's rules govern there** — `AGENTS.md` in that repository, and the
  `experiment-lifecycle` skill if it is installed. The researcher follows them: one experiment at a
  time, who writes each document, the blueprint before the rule.

## Plan first, then write

Every skill or command that writes a file presents a plan in chat — what will be written, where,
and what it supersedes — and waits for an explicit go (*go*, *proceed*, *ok*, *yes*) before writing
anything. Never write on a rejected or unanswered plan. Never write a plan or a report as a file;
the chat and the `LOG.md` entry are the record.

**Every step offers options, and the go is one of them.** Where the assistant has a question tool
— Claude Code's `AskUserQuestion` — a plan ends by asking through it, *Go*, *Change something*,
*Stop*, and *Go* is the explicit go; where it has none, the words in chat are. When the owner has
nothing to answer, the researcher proposes options drawn from what is already in the folder — the
sources and their tables of contents, `RESEARCHER.md`, the notes so far — and lets them pick. A
proposal the owner picks is theirs; one they did not pick is never written. The point is to keep
going, never to stall on an empty answer.

**The agent never writes at all**, and that follows from this rule rather than sitting beside it.
A subagent reports back once and cannot ask for a go, so there is no way for it to write with the
owner's consent. It answers, it cites, and it names the skill or command the owner should run.

## Where the skills, the commands and the agent live

`.apm/` holds the researcher, once, as three APM primitives. Nothing is committed twice.

| Primitive | Where | What it is |
| --- | --- | --- |
| **Skill** | `.apm/skills/<name>/SKILL.md` | `read` and `query` — capabilities the researcher reaches for on its own when the work calls for them, and that the owner can also invoke by name. A skill folder holds its `SKILL.md` and nothing else |
| **Command** | `.apm/prompts/<name>.prompt.md` | the other eight — tasks the owner starts by name, with arguments, each producing one thing. Each says *only when the owner runs it by name* in its own description, which is the one place every harness reads |
| **Agent** | `.apm/agents/<name>.agent.md` | the researcher as a subagent the harness can call by name, with its own tool boundary. Written by `researcher-init` from `RESEARCHER.md`, so a fresh clone has none until the interview runs |

- **`apm install --target <agent>` deploys them per machine** — into `.claude/skills/`,
  `.claude/commands/` and `.claude/agents/` for Claude Code; `.agents/skills/` for Codex and the
  rest, with their commands and agents in `.codex/`, `.cursor/`, `.gemini/`, `.github/`,
  `.opencode/` or `.windsurf/`. Git ignores every copy. A bare `apm install` does every target in
  `apm.yml`.
- **Edit in `.apm/`, never in a deployed copy,** then install again and open a new session. A
  copy that differs from its original is a stale install; `audit` reports it.
- **A skill is written the way KaxaNuk's own APM packages write theirs** — frontmatter `name`,
  matching the folder, a folded `description` that says when to use it and what it does not
  cover, and `metadata.version`; a body with *When to Use* and *Steps*. A skill folder holds its
  `SKILL.md` and nothing else: what a skill runs lives in `scripts/` at the root of the home, what
  it reads on demand in `references/`, so `.apm/` carries prose only. A command is one
  `.prompt.md` with `description`, its `input` list and `metadata.version`, no `name`; the body
  reads its inputs as `${input:name}`, and APM turns them into the arguments each harness takes.
- **Frontmatter is the lossy part.** A harness takes the keys it knows and drops the rest — APM
  says which on install, and a dropped key is a rule that is not enforced. Anything that must hold
  everywhere is written in the body or the description, not only in a key. A folded
  `description: >` keeps a colon from breaking the YAML; the agent's frontmatter, which APM does
  not rewrite, stays one line with no colon in it.
- **Codex has no command primitive.** There, a command is run by naming its file — *follow
  `.apm/prompts/blueprint.prompt.md` for experiment 1* — and the skills work as everywhere.
- **The agent's tool boundary is enforced on Claude Code, Copilot and Cursor.** Codex takes the
  agent and drops the tool list; Gemini and Windsurf have no agent primitive at all. That is why
  the read-only rule is written into the agent's own body as well as its frontmatter: a harness
  that drops the boundary still reads the instruction.
- **Nothing goes in `.apm/instructions/`.** `apm compile` would render it over this file, which is
  written by hand. With only skills and prompts, `apm compile` leaves `AGENTS.md` and `CLAUDE.md`
  alone and writes a `GEMINI.md` that imports them, which git ignores.
- **A skill or a command is discoverable in a new session,** never in the one that installed it.

## Hard don'ts

- Don't write into `Sources/`, or into `Philosophy/` outside `refine`.
- Don't write at home while working in a strategy, unless the owner asks for that write by name.
  Don't write in a strategy anything its own `AGENTS.md` reserves for a person.
- Don't edit a deployed copy under `.claude/`, `.agents/` or another agent's folder. Edit `.apm/`,
  then install again.
- Don't write anything while running as the agent, and don't copy `RESEARCHER.md` into its file.
  The agent reads the real one at the start of every run.
- Don't invent a citation. Don't cite a source that has no note.
- Don't cite an extract, or link into `Extracts/`. Notes cite the source and its pages; extracts are
  regenerated. A concept page cites notes, never a PDF, and is never built from memory.
- Don't compute a return, a Sharpe or an attribution yourself — those numbers come from the Lab's
  libraries, and a number without an engine behind it is not quoted.
- Don't rewrite a note in generic voice; match the library's existing notes.
- Don't write any file without the owner's go on the plan.
- Never print a value from a `.env` file. Never use the section symbol; write "section".
