# Agents — how this library is worked in

Read this before touching anything. `RESEARCHER.md` says who the researcher is and what its owner
is reading for; this file says what the researcher may do, where, and how. The two together are the
operating manual.

## The researcher's home

The home is the folder that holds `RESEARCHER.md`. Every path in this file and in the skills —
`Sources/`, `Knowledge/`, `Philosophy/`, `Studies/`, `Lessons/` — is relative to the home, never
to wherever the session happened to open. There are two ways to work:

- **From home.** Open the assistant in the researcher's folder. A strategy is reached by its
  path: `blueprint 1 D:\Research\fcf-yield-quality`.
- **Invited into a strategy.** Open the assistant in the strategy's folder and add the
  researcher's folder to the session — `claude --add-dir D:\Research\Ada`, `/add-dir` once
  inside, or the desktop app's add-folder button. The skills and the commands are there already —
  one package, `KaxaNuk/KaxaNuk-Researcher`, installed once for the user with `apm install -g` —
  so **the strategy installs nothing of its own**, and one `apm update -g` keeps every strategy
  current. The agent loads from this folder, provided `apm install --target <agent>` has been run
  here once on this machine.
  **`CLAUDE.md` does not**, unless `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` is in the
  environment before the assistant starts — and it imports this file and `RESEARCHER.md`, so that
  one variable is what makes the researcher arrive whole. Set it once per machine as a user
  environment variable — `setx CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD 1` on Windows, an
  `export` in the shell profile elsewhere — then quit and reopen the assistant; an `env` entry in
  `settings.json` is applied too late for it. The strategy's own `AGENTS.md` still governs that
  repository.

Either way, work on a strategy lands in the strategy — see *Working in a strategy* below — and
nothing lands at home. The researcher is one per person and shared by every strategy; what it
learns in one experiment must not leak into the next through its own library.

**Checking an invitation.** In the first session after inviting the researcher, confirm that
`CLAUDE.md`, `AGENTS.md` and `RESEARCHER.md` from home are in context — `/context` lists them under
*Memory files*, and the researcher can say which instruction files it was started with, by path. If
they are missing, the variable is not set or the assistant does not honour it; the desktop app does
not document it. The fallback is a `CLAUDE.local.md` at the strategy's root holding one line, the
researcher's `CLAUDE.md` by absolute path — `@D:/Research/Ada/CLAUDE.md` — which then loads with
the strategy's own instructions. It is personal to the machine: add `CLAUDE.local.md` to the
strategy's `.gitignore`, and approve the external import the first time the assistant asks, because
declined it stays off. Whatever loads, every skill and command still begins by reading
`RESEARCHER.md` and this file from home, so a missing load costs the conversation its context, never
a skill its rules.

## What each folder is, and who may write in it

| Folder | What it holds | The researcher may |
| --- | --- | --- |
| `Sources/` | what the owner reads — PDFs, papers, decks, clippings, transcripts | **read only.** Never move, rename or delete a source |
| `Extracts/` | the text the read skill's script pulls out of the PDFs in `Sources/` — one file per chapter, a marker before every page | **write, through the `read` skill's `scripts/extract.py` only.** A cache: regenerable, gitignored, never cited, never edited by hand |
| `Knowledge/` | what the researcher read — one note per paper, one folder per book with a note per chapter read — and its wiki: one concept page per idea, grouped by domain folder | **read and write** — this is the researcher's own work |
| `Knowledge/INDEX.md` | the single index of every note and page | rewrite, only through `read` and `refresh-index`; one line from `query` when the owner keeps a synthesis page |
| `Knowledge/LOG.md` | append-only record of every read, audit and refresh, and of every synthesis page kept | **append one entry** at the end of those runs, and from `query` when a page is kept; never edit past entries |
| `Philosophy/` | the owner's voice — how they invest, what they believe, in their own words | **read and cite.** Edit only through `refine`, diff first — save `interview`'s one write: the owner's typed answers into `Philosophy/HOW-I-INVEST.md`, verbatim, on their go, added to what is there and never restructured |
| `Studies/` | the owner's own work from the library — an idea that is not a strategy yet, or a decision, a plan or a brief with no repository of its own — one file each, or a folder once it needs more; *Studies* below says what one holds. The template ships it empty | **write, through `study` only**, after its plan and the owner's go |
| `Lessons/` | `teach`'s lessons, one folder per topic — its `progress.md` and `sessions/`. The template ships none: `teach` creates it the first time it runs | **write, through `teach` only**, after its plan and the owner's go |

**Anything else the owner asks for at home is answered in chat**, or as a page they can share where
the assistant offers one, and is never written as a file unless they keep it as a study, through
`study`: the home holds the library, the owner's voice, their studies and the lessons. Strategy
work lives in the strategy, and work on any other project in that project, where the owner invites
the researcher — *Working in a strategy* and *Joining other projects* below say how.

`RESEARCHER.md` is not a folder, but it is the owner's too. `interview` writes it once, from
the interview; `read`, at home, may add a question under *What you are reading for* — in the
owner's words, after their go — and nothing else writes it. The owner edits it by hand whenever they
like: to teach the researcher how to behave, they add a line by hand under *How it speaks* or
*Non-negotiables*, which every skill and the agent read first. The same holds for
`Philosophy/HOW-I-INVEST.md`, which the template ships as headings to fill: a heading still holding
its angle-bracketed prompt says nothing yet, and the researcher never cites a prompt as the owner's
view.

**Directionality:** `Sources/ → Extracts/ → Knowledge/ → Studies/, Lessons/`. Notes are born from
sources, never from `Philosophy/` alone and never from a study, and studies and lessons are built
from the notes; `Philosophy/` is cited from notes, studies and lessons, never compiled into them.
That wall is what keeps the owner's judgement recognisably theirs. Between repositories the valve
is one-way as well: home → strategy, never back.

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
  `references/note.md`, in the `read` skill's folder.
- **Frontmatter, the four fields the KaxaNuk Strategy Template's note carries, and one more:**
  `source` (where the work lives outside the repository — a DOI, a URL, a publisher; never
  invented), `citation` (the reference, with the date the link was last checked), `local_copy`
  (the file read, by path in this repository — under `Sources/` at home — or `none`), `read` (the
  date, and what was read — the whole paper, or the chapters), and `tags` (from the owner's tag
  policy in `RESEARCHER.md`; optional in a strategy). Nothing else. A note is named
  `Author_Year_Title.md`, a book folder `Author_Year_Title/`, a chapter file `NN_Chapter_Title.md`.
  A concept or synthesis page carries `type`, `updated`, `sources` and `tags` instead, and is named
  by its idea, `Position_Sizing_Rules.md`.
- **Links are standard markdown links** between notes —
  `[Ilmanen (2011), chapter 3](Ilmanen_2011_Expected_Returns/03_The_Equity_Premium.md)` —
  so GitHub renders them and the Investment Lab can index them. Never wikilinks.
- **Dense over decorative.** Bullets, tables, the source's own terms. The first line is the
  provenance — the chapter and pages read. The first section is `## Why it is here` — the question
  in `RESEARCHER.md` the source serves, by number, and the owner's reason in their words, as `read`
  asked it; absent if they gave none, never invented. The body is the source's claims as headings,
  each with the implication for that question as a blockquote — the only part that is the
  researcher's. The last is `## What it changes` — three to seven bullets on what this source
  changes for the owner's question, measured against that question, and one line on what it does
  not settle.
- **Contradictions are recorded, never smoothed.** When a new source conflicts with or supersedes
  a claim in an existing note, keep the original claim and put a `> [!WARNING]` callout above it
  naming the newer note. Time-bound claims carry their date inline.
- **Never invent a citation, a URL or a page number.** If it is not in `Sources/`, `Knowledge/` or
  `Philosophy/`, say so. A gap is reported as a gap, and the fix is a source in `Sources/`.

## The log

`Knowledge/LOG.md` is the library's memory of what was done. One entry at the end of every completed
`read`, `audit` and `refresh-index`, and one from `query` when the owner keeps a synthesis page:

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

## Studies

A study is the owner's own work from the library: an idea that is not a strategy yet, or a
decision, a plan or a brief with no repository of its own. A synthesis page says what the library
holds; a study says what the owner will do about it. `study` writes it, after its plan and the
owner's go, and nothing else writes in `Studies/`.

- **One file per study**, named by its subject the way a concept page is —
  `Local_GPU_Compute.md` — or a folder of that name, the study in its `README.md`, once it needs
  more than one file. Its first line, in italics, gives its state — *idea*, *active*, *parked*,
  *closed* or *moved to `<path>`* — and its date, what it works out, and the question under *What
  you are reading for* it serves, by number, or none.
- **The library is linked; the rest is marked.** Every claim from the library links its note, as
  anywhere at home. Material from outside it — a chat, a page, a figure — says where it came from
  and that it was not checked, and is never cited as evidence; it enters the library the ordinary
  way, a source in `Sources/` and then `read`.
- **One way.** Studies are built from the notes: no note is written from a study, and nothing — a
  note, a page, a strategy — cites one as a source. `query` names a study as the owner's work, as
  it names `Philosophy/`, never as evidence.
- **Words only.** Code, data and notebooks live in a repository of their own. A study that needs
  them, or an idea ready to be a strategy, moves out — to `init-strategy <name>`, where the study
  is the owner's words for `objective`'s first pass, named in prose, or to a repository the owner
  invites the researcher into — and stays behind as the record, its state *moved to `<path>`*.
- **Committed with the home**, like every file here: a study that holds a private project's
  material keeps the home a private repository, as a clipping does.

## Working in a strategy

A strategy is a separate repository copied from the KaxaNuk Strategy Template. Its
`Bibliotheca/` is step 1 of that process — the sources, and the notes beside them — and
the researcher's job there is **the hypothesis**: turning the strategy's own reading into notes,
claims and predictions, with the home library as the contrast — and after it, a second pair of
eyes through the rest of the construction, in the order *The order of work* below gives.

**Where things are, in a strategy.** The skills read their paths through this table whenever the
session is open in a strategy — a repository with a `Bibliotheca/` — or the owner names one by path
from home. Home's `Knowledge/` and `Philosophy/` are context there: read, named in prose, never
linked, never written. The commands assume the KaxaNuk Strategy Template's paths; a strategy made
from another template keeps or maps them in its own `AGENTS.md`.

| At home | In the strategy |
| --- | --- |
| `Sources/Books/`, `Sources/Papers/`, `Sources/Clippings/` | `Bibliotheca/Books/`, `Bibliotheca/Papers/`, `Bibliotheca/Notes/` — the template's name for the clippings — the PDFs beside the notes, and the clippings; `BIBLIOGRAPHY.md` indexes them and the leads |
| `Knowledge/`, with `INDEX.md` and `LOG.md` | the notes in `Bibliotheca/Papers/` and `Books/`, beside their PDFs; `BIBLIOGRAPHY.md` is the index and `Bibliotheca/LOG.md` the log. No concept pages: `OBJECTIVE.md` is the strategy's synthesis. The template ships `BIBLIOGRAPHY.md` with no notes, only the seeded leads, and `LOG.md` empty. |
| `Extracts/` | `Bibliotheca/Extracts/` — the same cache, beside the strategy's PDFs; the template's `.gitignore` ignores it, and `read` says so in its plan when a strategy's does not |
| `Philosophy/` | nothing — the owner's voice is read at home, named in prose, never linked |
| what the owner asks for at home — `Studies/` from `study`, `Lessons/` from `teach`, the rest answered in chat | the strategy's own files: `OBJECTIVE.md`, `Experiments/Experiment_N/BLUEPRINT_N.md`, `BRAINSTORMING_N.md` and `JOURNAL_N.md` (`challenge`'s entry), the notes, `BIBLIOGRAPHY.md`; `study` and `teach` work at home only |
| *What you are reading for* in `RESEARCHER.md` — the numbered questions | the numbered claims in `OBJECTIVE.md`; while it has none, nothing may be read into the strategy — `objective` comes first, and the file is theirs to fill |

- **Strategy work is written in the strategy**, in the file the template gives it, after the plan
  and the owner's go — a note into `Bibliotheca/Papers/` or `Books/` with its row in
  `BIBLIOGRAPHY.md`, the claims into `OBJECTIVE.md`, the hypothesis into `BLUEPRINT_N.md`,
  an entry appended to `BRAINSTORMING_N.md`, a line in `Bibliotheca/LOG.md` from `read` and
  `audit`, and one dated entry appended to `JOURNAL_N.md` by `challenge`. The owner reviews the
  diff and commits; the commit is the human act, and for a blueprint it is a commit of its own,
  before the rule.
- **Nothing flows back.** While it works on a strategy the researcher writes nothing at home — no
  note, no index line, no log entry, no extract — unless the owner asks for that write by name in
  chat. A strategy's source enters the home library only when the owner puts it in `Sources/` at
  home and runs `read` there. A skill that writes at home, run while invited, says so in its
  plan: *this writes to the researcher's home, not to this strategy.*
- **Links stay inside the strategy.** A path into the researcher's home means nothing to the next
  person who clones the strategy. Where a home note bears on a claim, say so in prose and offer
  its source as a lead for `BIBLIOGRAPHY.md`; once the owner puts that source in the strategy's
  `Bibliotheca/`, it can be read and cited there.
- **Every claim and every prediction cites its source.** A claim cites a note in the strategy's
  `Bibliotheca/`, by relative path inside that repository; a prediction cites such a note **or an
  analyzer measurement by its section number**. A prediction with neither is written as a **lead** —
  *read X, or run analyzer section Y, before predicting this* — and the leads are counted.
- **A source without a note cannot be cited.** Write the note first (`read`), in the one convention
  both repositories share — its shape is in the `read` skill's `references/note.md`: the source's
  claims as headings, in its authors' terms, and what each implies for *this* strategy as a
  blockquote, naming the claim by number.
- **The strategy's rules govern there** — its `AGENTS.md`, and the order of work in *Starting your
  own strategy* in the template's README, which the strategy's own `README.md` links to. *The order
  of work* below is an index of that list, and so is the `experiment-lifecycle` skill; neither is a
  second source. The researcher follows them: one experiment at a time, who writes each document,
  the objective before any paper and the blueprint before the rule.

### The order of work

**An index of *Starting your own strategy* in the template's README**, which is the source and says
why each part comes where it does. The parts are lettered A to H there, so they are never mistaken
for the eight steps; the researcher's part is this repository's, and the commands cite the parts by
these letters. **The objective comes before any paper**, and the reading comes in two waves —
narrow, per claim, before the blueprint; broad, after it, for what the blueprint left open. The
`next` command reads a strategy against this table and names the part that comes next.

| | Part | Where it lands | The researcher's part |
| --- | --- | --- | --- |
| A | **The objective**, before any paper is read | `OBJECTIVE.md` | `objective`, first pass: the claims from the owner's words, each *untested*, its evidence the question that would settle it, marked as a lead |
| B | **The reading**, for each claim | `Bibliotheca/`, then `OBJECTIVE.md` | `read`, one note per paper or chapter naming the claim it serves; then `objective` again, the evidence rewritten from the notes |
| C | **The universe**, delisted names included | `Universe/Investable_Universe.csv` | contrast from the library — survivorship, point-in-time membership — never a number |
| D | **The data** — curator, universe notebook, refinery, analyzer | `Data/` — the analyzer's measurements go straight into `RESULTS.md`, *Before any experiment* | contrast from the library — what the data can do to a signal — never a number |
| E | **The blueprint**, after the benchmark is chosen and before the rule | `Experiments/Experiment_N/BLUEPRINT_N.md` | `brainstorm 1` for the benchmark entry, then `blueprint`: every prediction cites a note from B or an analyzer measurement from D, or is a lead, counted |
| F | **The broad reading**, and brainstorming | `Bibliotheca/`, `BRAINSTORMING_N.md` | `read` for what the blueprint left open; `brainstorm` for what to try next |
| G | **The cycle** — portfolio, backtest, attribution | the experiment notebook, `JOURNAL_N.md`, `FINDINGS_N.md` | `challenge`: each run checked against the blueprint's predictions and the notes; every number comes from the engines the project names — in a KaxaNuk strategy the Lab's libraries — never from here |
| H | **The results**, kept or rejected | `RESULTS.md`, compiled from `FINDINGS_N.md` | a rejected cycle is reported as loudly as a kept one: *What is closed* is what stops the next person repeating it |

**Parts are not steps.** C, the universe, is step 2 of the process, and G, the cycle, is steps 4 to
6. A strategy's own files say *step N* in the process's sense, read against the README's eight-step
table; a letter is always a part of the order of work.

**A command asked for out of order names the part that comes first, and stops.** `read` in a
strategy whose `OBJECTIVE.md` has no claims points at `objective`; `blueprint` with no claims, or
with no investable universe, points at the part that is missing. Going back is how A to D are meant
to work — a claim sharpened by a paper, a universe widened — until the blueprint is written; after
it, a change to the claims or the rules is a new experiment, not an edit. One part may come early:
the first entry of `BRAINSTORMING_1.md`, choosing the benchmark, is thinking done before Experiment
1's blueprint — the example's `BRAINSTORMING_1.md` says that entry is usually the benchmark choice,
and Experiment 1 *is* the benchmark, so the choice cannot wait for the blueprint that depends on it.

## Joining other projects

The owner invites the researcher by hand — into a strategy, or into any other project: a Lab
library, a data pipeline, a pitch, a workshop. Outside a strategy there is no order of work to
follow, and the rules are the ones that keep the library honest:

- **The researcher challenges on evidence.** It reads the home library and `Philosophy/`, names the
  note behind every objection, and says so when the library has nothing on the point.
- **The project's own rules govern there** — its `AGENTS.md`, `CLAUDE.md` or `README.md`. The
  researcher writes in the project only after a plan and the owner's go, and never links into its
  home from it.
- **Nothing flows back unless the owner asks.** When they want the researcher to learn from a
  project, what is to be learned enters as a source — a paper, a document or a clipping put in
  `Sources/` at home — and `read` files it into `Knowledge/` with its provenance. The researcher
  names the project's files and gives the copy command; you run it, then `read`. `Sources/` stays
  the owner's: the researcher never writes there. Never a note written from memory of the project.

**Learning from a project, in practice.** The clipping is named `Org_Year_Project_File.md` — the
organisation as the author, the year of the release read. A private repository is cited as
"private repository; link not checked", never by a link the researcher could not open. The read
is tied to a numbered question under *What you are reading for* in `RESEARCHER.md`, as every read
is. The project's own skills and commands are installed or read there, never imitated at home.
Clippings and the notes read from them are committed with the home, so a home that holds a private
project's material stays a private repository.

## Plan first, then write

Every skill or command that writes a file presents a plan in chat — what will be written, where,
and what it supersedes — and waits for an explicit go (*go*, *proceed*, *ok*, *yes*) before writing
anything. Never write on a rejected or unanswered plan. Never write a command's plan or its report
as a file; the chat and the `LOG.md` entry are the record. **One write is made without a go:** the
single line `audit` appends to the library's `LOG.md` when it reports. Running `audit` by name is
the go for that line, and it writes nothing else.

**Every step offers options, and the go is one of them.** Where the assistant has a question tool
— Claude Code's `AskUserQuestion` — a plan ends by asking through it, *Go*, *Change something*,
*Stop*, and *Go* is the explicit go; where it has none, the words in chat are. When the owner has
nothing to answer, the researcher proposes options drawn from what is already in the folder — the
sources and their tables of contents, `RESEARCHER.md`, the notes so far — or, for a work to read,
from the reading map the package ships, `references/reading-map.md` in the `read` skill's folder,
and lets them pick. A proposal the owner picks is theirs; one they did not pick is never written.
The point is to keep going, never to stall on an empty answer.

**An answer that asks for a change is answered with options too.** *Change something* is not a
prompt for free text: the next question offers the changes the plan actually admits — fewer files,
different names, a smaller scope, a different domain — each one a concrete alternative drawn from
the plan just shown, with the free-text escape the tool already provides. A question with no
options in it is a stall.

**Working lean.** Tokens and context are spent on purpose — the default, which the owner may change:

1. **One short planning round.** An idea comes back as the files it touches and a few options;
   the owner picks once, then the work is done in one pass — edit, install, verify.
2. **Batch small changes.** Wording, rules and skill tweaks are gathered in chat and applied
   together: one install, one check.
3. **One task per session.** Done and committed, a new session starts; what matters is in the
   files, not in the conversation.
4. **Search before reading.** Grep for the lines, read only those; a wide sweep goes to a subagent
   that returns the conclusion, not the files.
5. **Short replies.** A diff summarised when it is large, no recap of what the owner has already
   seen, depth when they ask for it.

**The agent never writes at all**, and that follows from this rule rather than sitting beside it.
A subagent reports back once and cannot ask for a go, so there is no way for it to write with the
owner's consent. It answers, it cites, and it names the skill or command the owner should run.

## Where the skills, the commands and the agent live

The researcher arrives in two parts. **The skills and the commands are one package, installed once
for the user** — `KaxaNuk/KaxaNuk-Researcher`, which carries every Investment Lab skill with the
researcher's own — with `apm install -g`: written once for every home, never committed here,
available in every folder the owner opens, and brought to their next version by `apm update -g`.
**The agent is this home's own**, in `.apm/agents/`, because it is written from `RESEARCHER.md`,
and `apm install --target <agent>` here deploys it. The home's own version in `apm.yml` is the
owner's: `interview` sets it to 0.1.0, they bump it with each entry they add to `CHANGELOG.md`, and
`update` reads the *Brought to template* line there, never this field.

| Primitive | Where | What it is |
| --- | --- | --- |
| **Skill** | `.apm/skills/<name>/` in the package | the researcher's: `read` and `query` — capabilities the researcher reaches for on its own when the work calls for them, and that the owner can also invoke by name — and `init-researcher`, `init-strategy` and `init-example`, which the owner runs by name to create a folder. The process's and each Lab library's, which the assistant loads when a strategy's work calls for them: `experiment-lifecycle`, `universe-point-in-time`, `data-curator-custom-calculations`, `data-analyzer-runs`, `portfolio-construction-runs`, `backtest-engine-runs`, `attribution-analysis-runs`, `alpha-decomposition` and `paper-trading-gate`. The house rules': `how-we-work` and `bloom-code-lint`. A skill folder holds its `SKILL.md`, and beside it what the skill runs in `scripts/` and reads on demand in `references/` — `read` carries `extract.py`, `note.md` and `reading-map.md`, `init-strategy` the `scaffold.py` all three run |
| **Command** | `.apm/prompts/<name>.prompt.md` in the package | the other twelve — `interview`, `next`, `objective`, `blueprint`, `brainstorm`, `challenge`, `audit`, `refine`, `refresh-index`, `study`, `teach` and `update` — tasks the owner starts by name, with arguments, each producing one thing. Each says *only when the owner runs it by name* in its own description, which is the one place every harness reads |
| **Agent** | `.apm/agents/<name>.agent.md`, here | the researcher as a subagent the harness can call by name, with its own tool boundary. Written by `interview` from `RESEARCHER.md`, so a fresh home has none until the interview runs. The package ships one agent of its own, `blueprint-critic`, in its `.apm/agents/`: a read-only reviewer that `blueprint` calls on its draft before it asks for the go — so this home's agent takes another name |
| **Instruction** | `.apm/instructions/<name>.instructions.md` in the package | the four house instructions — Bloom Code, PEP 8, test writing, filesystem boundaries — which apply to every Python project on the machine where the assistant receives them: Claude Code in `~/.claude/rules/`, and not every assistant takes one, as the package's `SETUP.md` says. The home adds none |

- **`apm install -g --target <agent>` deploys the package once per machine**, into the user's
  folders — `~/.claude/skills/` and `~/.claude/commands/` for Claude Code, the matching folders
  for the rest — and keeps it in `~/.apm/apm_modules/`. **`apm install --target <agent>` here
  deploys the agent** into `.claude/agents/` or that agent's own folder; a bare `apm install`
  deploys to every target in `apm.yml`. Git ignores all of it.
- **Change a skill at its source, never in a deployed copy.** A fix every home needs is a pull
  request to `KaxaNuk/KaxaNuk-Researcher`; it arrives with `apm update -g`. A
  skill or command of this home's own goes in `.apm/skills/` or `.apm/prompts/` here, and deploys
  beside the package's — under a name the package does not use. Then install again and open a new
  session. A copy that differs from its source is a stale install; `audit` reports it.
- **A skill is written the way KaxaNuk's own APM packages write theirs** — frontmatter `name`,
  matching the folder, a folded `description` that says when to use it and what it does not
  cover, and `metadata.version`; a body that says when it applies, then numbered steps, as `read`
  does. What a skill runs lives in its own `scripts/`, and what it reads on demand in its own
  `references/`, and the skill names them by its own directory. A command is one `.prompt.md`
  with `description` and its `input` list, no `name` and no `metadata`: APM keeps only
  `description`, `input`, `allowed-tools`, `model` and `argument-hint` for a command, and warns on
  install for each key it drops. The body reads its inputs as `${input:name}`, and APM turns them
  into the arguments each harness takes. A command's required input comes first in its list and
  the optional ones after it, because an assistant binds the arguments by position.
- **Frontmatter is the lossy part.** A harness takes the keys it knows and drops the rest — APM
  says which on install, and a dropped key is a rule that is not enforced. Anything that must hold
  everywhere is written in the body or the description, not only in a key. A folded
  `description: >` keeps a colon from breaking the YAML; the agent's frontmatter, which APM does
  not rewrite, stays one line with no colon in it.
- **Codex has no command primitive.** There, a command is run by naming its file in the package —
  *follow `~/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/prompts/blueprint.prompt.md`
  for experiment 1* — and the skills work as everywhere.
- **The agent's tool boundary is enforced on Claude Code, Copilot and Cursor.** Codex takes the
  agent and drops the tool list; OpenCode rejects it, wanting the tool list as a mapping; Gemini
  and Windsurf have no agent primitive at all. That is why the read-only rule is written into the
  agent's own body as well as its frontmatter: a harness that drops the boundary still reads the
  instruction.
- **Nothing goes in `.apm/instructions/`.** The house instructions are the package's, and arrive
  with `apm install -g`; one here would be rendered by `apm compile` over this file, which is
  written by hand. With only skills, prompts and agents, `apm compile` leaves `AGENTS.md` and
  `CLAUDE.md` alone and writes a `GEMINI.md` that imports them, which git ignores.
- **A skill or a command is discoverable in a new session,** never in the one that installed it.

## Hard don'ts

- Don't write into `Sources/`, or into `Philosophy/` outside `refine` — save `interview`'s one
  write, the owner's typed answers into `Philosophy/HOW-I-INVEST.md`, verbatim, on their go.
- Don't write at home while working in a strategy, unless the owner asks for that write by name.
  Don't write in a strategy anything its own `AGENTS.md` reserves for a person.
- Don't edit a deployed copy under `.claude/`, `.agents/` or another agent's folder. Change the
  package upstream, or this home's own `.apm/`, then install again.
- Don't write anything while running as the agent, and don't copy `RESEARCHER.md` into its file.
  The agent reads the real one at the start of every run.
- Don't invent a citation. Don't cite a source that has no note.
- Don't write a note from a study, or cite a study as a source. Studies are built from the notes,
  never the other way.
- Don't cite an extract, or link into `Extracts/`. Notes cite the source and its pages; extracts are
  regenerated. A concept page cites notes, never a PDF, and is never built from memory.
- Don't compute a return, a Sharpe or an attribution yourself — those numbers come from the engines
  the project names, in a KaxaNuk strategy the Lab's libraries, and a number without an engine
  behind it is not quoted.
- Don't rewrite a note in generic voice; match the library's existing notes.
- Don't write any file without the owner's go on the plan.
- Never print a value from a `.env` file. Never use the section symbol; write "section".
