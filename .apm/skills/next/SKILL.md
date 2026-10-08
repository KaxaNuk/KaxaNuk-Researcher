---
name: next
description: >
  Say where the owner stands — in the researcher's home or in a strategy — and the one thing to do
  next, with the command or skill that does it, read from the files on disk as a checklist; nothing
  is written but a version the owner asks it to save. Takes an optional path to a strategy, when
  the session is not open in it. Only when the owner runs it by name, or when the researcher's
  skill answers a greeting; never on its own otherwise.
metadata:
  version: 1.4.0
---

# Next — where you stand, and what to do next

This skill is the map of the process and of the researcher's skills and commands: it reads the
folder, says which parts are done, and names **the one thing to do next** with the command or skill
that does it. It writes nothing and never starts the next thing itself — doing it is a different
request, by the name this skill gives — save one: the version row 0 or row E offers, on the
owner's pick. It is a skill, not a command, so every assistant APM deploys to has it, Codex
included.

Every path below is relative to the folder being read: a strategy's path when the owner gives one
— *next ../fcf-yield-quality* — because the session is not open in it; otherwise the folder the
session is open in.

## Step 1: Which folder this is

| It holds | It is | What follows |
| --- | --- | --- |
| `Bibliotheca/`, `Universe/` and `Experiments/`, and a line reading `<!-- example: begin -->` in `README.md` or `AGENTS.md`, which a strategy from the template never has | the worked example, made by `init-example` | say so, and quote its status line, which says how far it went: it is for reading, never built on; a strategy of the owner's own is `init-strategy <name>`. No part of *Step 3* is offered |
| `Bibliotheca/`, `Universe/` and `Experiments/` | a strategy | *Step 3* |
| `RESEARCHER.md` | a researcher's home | *Step 2* |
| `.apm/skills/init-strategy/` and `templates/` | the KaxaNuk Researcher package itself | say so: nothing is worked on here; `AGENTS.md` has its rules |
| none of those, and a home is in the session through `--add-dir`, or readable at the path the researcher's skill names | a project the researcher joined | *Joining other projects* in the home's `AGENTS.md` governs, and the project's own rules apply. Name the home and its one next thing, *Step 2* read at the home's path; here, `query` answers from the library, and what the project teaches goes home as a source, then `read`. No `init-*` command is suggested for this folder |
| none of those | not a KaxaNuk folder | when a subfolder one level down holds `RESEARCHER.md` or a strategy's three folders, name it so the owner can open it, applying the first row's test to it: a subfolder that passes it is named as the worked example, for reading, never as a strategy to work in; otherwise say which of the three skills makes one — `init-researcher <name>` once per person, `init-strategy <name>` once per strategy, `init-example` to read the worked example — and stop |

When both a strategy and a home are in the session — added to it, or named by the researcher's
skill — read the strategy: the home is the library it brought along.

## Step 2: At home

Check in this order and stop at the first that fails; that is the next thing. `<slug>` is the
researcher's name in `RESEARCHER.md` made safe for a folder, as `interview` *Step 4* says: accents
removed, lowercase, anything but a to z or a digit a hyphen, hyphens collapsed and none at either
end — `Begoña Ruiz` becomes `begona-ruiz`. In rows 2 and 3 a file or a folder of another name
counts when its `name:` is the one the home's agent carries, as an older `interview` wrote them, so
a home already installed is not sent to install again.

| # | Done when | If not, the next thing is |
| --- | --- | --- |
| 0 | the folder is a git repository — it holds `.git/` — and its working tree is clean: `git status --short` prints nothing, untracked files under `Sources/` aside, which row 4 reports and which do not block | with no `.git/`, say in one line that this folder keeps no versions yet, and offer to start them; on the owner's word, run what `scaffold.py` prints to finish a repository — `git init --quiet --initial-branch=main`, `git add --all`, `git commit --quiet -m "Start from the KaxaNuk Researcher template"` — and say *Saved*. Otherwise, name the changes made by hand in plain words, file by file — *your note on Fama 1970*, *RESEARCHER.md* — never the commands, and ask `Save?` (`¿Guardo?`): *Save this version*, *Not now*, listed in chat without a question tool. On *Save this version*, `git add` each file by name, never `--all`, and `git commit -m "<what changed>"`; say *Saved* — sent too when `git config --get kaxanuk.autosend` prints `true`, as the `backup` skill says — and go on from row 1; on *Not now*, nothing more. A save refused for want of a name and an e-mail asks for both in one plain line, sets them in this folder only, never invented, and saves again |
| 1 | `RESEARCHER.md` has no angle-bracketed slot left. *What you are reading for* with no numbered question is not a slot: the template ships it so, and the first `read` asks for question 1 | `interview` — the interview |
| 2 | `.apm/agents/` holds an agent file named for the researcher, and `.apm/skills/<slug>/` the researcher's skill, its folder named in a to z, digits and hyphens only, whose description names this folder as the home | `interview` again when either is missing: it writes it from `RESEARCHER.md` without repeating the interview; `update` when the skill names another folder — the home has moved — or its folder's name holds anything but a to z, digits and hyphens, such as an accent, which APM deletes on install |
| 3 | the home is installed for the user: the agent and the skill are in the user's folder of the assistant in use — `~/.claude/agents/<slug>.md` and `~/.claude/skills/<slug>/` for Claude Code — or, where that folder cannot be read, `uvx --from apm-cli==0.33.0 apm deps list -g` names `_local/<this folder's name>`, its accents possibly dropped | `uvx --from apm-cli==0.33.0 apm install -g "<this folder>"`, then a new session; a copy still in this folder's `.claude/agents/`, from before the user-scope install, is `update`'s to remove |
| 4 | every source under `Sources/` — a PDF, a document or a clipping, not a `.gitkeep` — has a note: match by the title's distinctive words and the first author's surname against `Knowledge/INDEX.md`, as the `read` skill's `references/reading-map.md` says under *Match before proposing* | `read <the source>`, naming the question it serves; with no numbered question yet, `read <the source>` alone, which asks the owner which question it serves and adds it as question 1 |
| 5 | every work on a *Find first* line of `RESEARCHER.md` is in `Sources/`, or the owner took it off the line, which is theirs to edit by hand | find it by its title and authors, then attach it or say where it is saved, and the researcher copies it into `Sources/Papers/` or `Sources/Books/` on the go, then `read`; or, when it cannot be found, take it off the *Find first* line in `RESEARCHER.md` |
| 6 | `Knowledge/INDEX.md` lists every note and page on disk | `refresh-index` |

All seven done, the one next thing follows the *Here for* line under *Who* in `RESEARCHER.md`: the
first row below whose pick is on the line and whose thing is not done yet. *Step 1*'s first-row
test tells the worked example from a strategy of the owner's own.

| Pick | The one next thing | Done when |
| --- | --- | --- |
| *Learn the basics, step by step* | `philosophy`, at Starter — it teaches one idea after each answer and needs no reading | a round file exists in `Philosophy/Evolution/` |
| *Write down how I invest, and see it evolve* | `philosophy`; once a round exists, `brief setup`, for a daily brief of the markets and holdings they follow, leads the *also* line until `Briefs/` exists | a round file exists in `Philosophy/Evolution/` |
| *Build and test a strategy* | `init-example`, a finished strategy to read — `OBJECTIVE.md`, `RESULTS.md`, Experiment 1 — that needs nothing installed; running it takes a data key, a download of 1 hour 37 minutes, KaxaNuk's benchmark and factor files and licences, as its `SETUP.md` says. Then `init-strategy <name>` for their own | a folder beside the home holds `Bibliotheca/`, `Universe/` and `Experiments/`: the example alone → `init-strategy <name>`; a strategy of their own → done, and `next <its path>` leads the *also* line |
| *Organise what I read*, none, or their own words | a source into `Sources/` — they attach it or name it, and the researcher copies it into `Sources/Papers/`, `Sources/Books/` or `Sources/Clippings/` on their go — then `read`, which asks which question it serves | `Knowledge/` holds a note |

When every pick's thing is done, the one next thing is, with no note in `Knowledge/` yet, the last
row's; otherwise the first of these whose pick is on the line — *Learn the basics*,
`teach <topic>` on a topic the notes cover; *Write down how I invest*, a new source, and
`philosophy` again once notes came in since the last round; *Build and test a strategy*,
`next <its path>`; the rest, a new source, or `query`. Up to three more on one line as *also*: a
question added under *What you are reading for*, `study <subject>` to work out an idea from the
library — `study` alone lists the studies — `teach <topic>`, `brief setup` for a daily brief,
`init-strategy <name>`, or teaching it a tool: its documentation into `Sources/Clippings/`, then
`read` — *Growing your researcher* in the home's README.
Philosophy is never a row that fails: for the other picks, *Step 4* closes with it in one line.

## Step 3: In a strategy

Two things come before the order of work. **Setup:** `.venv/` exists, `Config/.env` exists — never
open it — and `README.md` is the strategy's own, not the template's, whose first line is
*KaxaNuk Strategy Template*. Any of those missing, the next thing is the strategy's `SETUP.md`,
from the step that failed. **The status line** at the top of `README.md` and `AGENTS.md`, which the
owner keeps current; quote it.

The commands assume the KaxaNuk Strategy Template's paths; a strategy made from another template
keeps or maps them in its own `AGENTS.md`.

Then the order of work — *Starting your own strategy* in the template's README, A to H — read from
the files. Check in order and stop at the first part not done; that is the next thing. Data and
engine outputs are gitignored, so a check on them says *on this machine*: a fresh clone shows them
empty after the work was done.

| | Part | Done when | If not, the next thing is |
| --- | --- | --- | --- |
| A | The objective | `OBJECTIVE.md` has a main idea in the owner's words and at least one claim in its table that is not the template's italic guidance | `objective` — from the owner's words, before any paper |
| B | The reading | every claim's evidence is one of three kinds — a note in `Bibliotheca/` by relative path, with a row in `BIBLIOGRAPHY.md`; `RESULTS.md` or the `FINDINGS_N.md` that measured it; or the claim is **true by construction** — or the owner has recorded the claim's evidence in `OBJECTIVE.md` as a lead carried into the blueprint, where E counts it; a claim that still names only the question that would settle it is a lead | `read <source>` for the first claim without a note, then `objective` again to rewrite its evidence from the notes |
| C | The universe | `Universe/Investable_Universe.csv` has rows under `main_identifier` | fill the seed, delisted names included — the `universe-point-in-time` skill says what belongs in it |
| D | The data | on this machine: `Data/Curator/Time_Series/` has files, `Universe/Security_Master.csv` exists, `Data/Refinery/Time_Series/` has files; and `RESULTS.md` has a measurement under *Before any experiment* with the analyzer section it came from | the first of `Data/curator.py`, `Universe/universe.ipynb`, `Data/refinery.py`, `Data/analyzer.ipynb` whose output is missing, in that order — `data-curator-custom-calculations`, `universe-point-in-time`, `data-analyzer-runs` |
| E | The blueprint | `JOURNAL_1.md` has the entry choosing the benchmark — in a strategy that still keeps `BRAINSTORMING_1.md`, its first entry counts; `Experiments/Experiment_N/BLUEPRINT_N.md` carries the line `blueprint` writes under the experiment's heading, `**Written YYYY-MM-DD, before any rule was coded.**`, and every prediction names a note or an analyzer section, and it is saved as a version of its own before the rule cell of `experiment_N.ipynb` holds code | the benchmark, chosen with the owner in chat and appended to `JOURNAL_1.md` on their go, when that entry is missing; else `blueprint N`; else the blueprint saved alone, before the rule — on `blueprint`'s go, or here on *Save this version*, asked and said as row 0 does: `git add` it, then `git commit -m "Blueprint N, before the rule" -- Experiments/Experiment_N/BLUEPRINT_N.md` |
| F | The broad reading | the leads the blueprint counted are read or recorded as leads in `BIBLIOGRAPHY.md` | `read` for the first lead |
| G | The cycle | section 2 of `experiment_N.ipynb` holds the rule; on this machine `Portfolio/`, `Backtest/` and `Attribution/` hold output; `FINDINGS_N.md` reports, every prediction of the blueprint evaluated | the first of `portfolio-construction-runs`, `backtest-engine-runs`, `attribution-analysis-runs` whose output is missing; `alpha-decomposition` to read it; then `challenge N` once `FINDINGS_N.md` reports. When the engine or the attribution library is not installed, which the notebook's guarded import reports, say the step is skipped for want of a licence and give the access line from the Lab's access facts, `references/investment-lab.md` in this skill's folder: *A licence for the Backtest Engine or Attribution Analysis is KaxaNuk's to give: write to `lab@kaxanuk.mx`, saying which library and what it is for — <https://www.kaxanuk.mx/lab> shows the Lab.* When the library is installed and attribution reports its index or factor files missing instead, give the facts file's Analytics Factory line: *KaxaNuk's Analytics Factory ships the benchmark and the factor model files attribution reads, <https://www.kaxanuk.mx/analytics>; ask `lab@kaxanuk.mx` for them.* Then move on to what can still be done — `FINDINGS_N.md` for the book, and the journal's open threads |
| H | The results | `RESULTS.md` has the experiment's row citing `FINDINGS_N.md`; the claim has moved — where `BLUEPRINT_N.md` names one under *The claim this moves*, `OBJECTIVE.md` gives that claim the status `FINDINGS_N.md` says it reached, and so does the row's *Claim moved* where `RESULTS.md` has that column; where the blueprint names none, the statuses in `OBJECTIVE.md` of the claims it tests have moved; and `CHANGELOG.md` has the entry | the missing one of those three |

A to H done for the newest experiment: the next thing is either the gate — `Paper_Trading/
BITACORA.md`, the `paper-trading-gate` skill — when the owner believes the findings evidence its
first criterion, or Experiment N+1, as section 6 of `experiment-lifecycle` says, starting again at
E; the objective, the universe and the data are the strategy's and stay.

## Step 4: Report

In chat, short:

1. **Which folder this is**, and the status line where there is one.
2. **The checklist**: in a strategy, a table — each part, done or not, with the file that says so;
   at home, one line when rows 0 to 6 pass, *setup: all good*, else the failing row alone.
3. **Next:** one line — the part, the command or skill by name, and what it will ask for; any
   *also*, one line after it.
4. **Your philosophy**, at home only, one closing line, offered and never pressed, and left out
   when *Next* names `philosophy`. With no round file in `Philosophy/Evolution/`: *`philosophy`
   writes down how you invest, in your words, at your level — round 1, whenever you like.* With
   one or more: the last round's date and level — the newest file name, `YYYY-MM-DD-2.md` after
   `YYYY-MM-DD.md` — and how many notes came in since: the notes the `read` entries of
   `Knowledge/LOG.md` dated on or after it — a read the same day counts — list as written, a book's
   `INDEX.md` and concept pages aside. When notes came in, add that `philosophy` takes the round
   again; when none did, the date, the level and *no notes since* are the whole line.

Nothing else. No file is written, no log entry appended, no number computed and no plan drafted:
when the owner says *do it*, that is the named command's or skill's own plan and go, not this one's.
Row 0's and row E's saves are all it runs.
