---
description: Say where the owner stands — in the researcher's home or in a strategy — and the one thing to do next, with the command or skill that does it, read from the files on disk as a checklist; nothing is written. Only when the owner runs it by name; never on its own.
input:
  - strategy: "Optional: path to the strategy repository, if not the one the session is in"
---

# Next — where you stand, and what to do next

The process has eight steps, an order of work with eight parts, three commands that make folders
and a dozen that write in them. This command is the map: it reads the folder, says which parts are
done, and names **the one thing to do next** with the command that does it. It writes nothing,
runs nothing, and never starts the next thing itself — doing it is a different request, by the
name this command gives.

Every path below is relative to the folder being read. `${input:strategy}` is a strategy's path,
given when the session is not open in it; otherwise the folder the session is open in.

## Step 1: Which folder this is

| It holds | It is | What follows |
| --- | --- | --- |
| `Bibliotheca/`, `Universe/` and `Experiments/` | a strategy | *Step 3* |
| `RESEARCHER.md` | a researcher's home | *Step 2* |
| `.apm/skills/init-strategy/` and `templates/` | the KaxaNuk Researcher package itself | say so: nothing is worked on here; `AGENTS.md` has its rules |
| none of those | not a KaxaNuk folder | say which of the three commands makes one — `init-researcher <name>` once per person, `init-strategy <name>` once per strategy, `init-example` to read the worked example — and stop |

When both a strategy and a home are in the session, read the strategy: the home is the library it
brought along.

## Step 2: At home

Check in this order and stop at the first that fails; that is the next thing.

| # | Done when | If not, the next thing is |
| --- | --- | --- |
| 1 | `RESEARCHER.md` has no angle-bracketed slot left | `researcher-init` — the interview |
| 2 | `.apm/agents/` holds an agent file named for the researcher | `researcher-init` again: it writes the agent from `RESEARCHER.md` without repeating the interview |
| 3 | the agent is deployed: `.claude/agents/<slug>.md`, or the folder of the assistant in use | `apm install --target <the assistant>` in this folder, then a new session |
| 4 | every file under `Sources/` has a note — match by the title's distinctive words and the first author's surname against `Knowledge/INDEX.md`, as the `read` skill's `references/reading-map.md` says under *Match before proposing* | `read <the source>`, naming the question it serves |
| 5 | every work on a *Find first* line of `RESEARCHER.md` is in `Sources/` | find it by its title and authors, put it in `Sources/Papers/` or `Sources/Books/`, then `read` |
| 6 | `Knowledge/INDEX.md` lists every note and page on disk | `refresh-index` |

All six done: say so, and that the next thing is the owner's — a new source into `Sources/`, a
question added under *What you are reading for*, or `init-strategy <name>` for the first strategy,
with the home invited in by `--add-dir`.

## Step 3: In a strategy

Two things come before the order of work. **Setup:** `.venv/` exists, `Config/.env` exists — never
open it — and `README.md` is the strategy's own, not the template's, whose first line is
*KaxaNuk Strategy Template*. Any of those missing, the next thing is the strategy's `SETUP.md`,
from the step that failed. **The status line** at the top of `README.md` and `AGENTS.md`, which the
owner keeps current; quote it.

Then the order of work — *Starting your own strategy* in the template's README, A to H — read from
the files. Check in order and stop at the first part not done; that is the next thing. Data and
engine outputs are gitignored, so a check on them says *on this machine*: a fresh clone shows them
empty after the work was done.

| | Part | Done when | If not, the next thing is |
| --- | --- | --- | --- |
| A | The objective | `OBJECTIVE.md` has a main idea in the owner's words and at least one claim in its table that is not the template's italic guidance | `objective` — from the owner's words, before any paper |
| B | The reading | every claim's evidence names a note in `Bibliotheca/` by relative path, and `BIBLIOGRAPHY.md` has a row for each; a claim that still names only the question that would settle it is a lead | `read <source>` for the first claim without a note, then `objective` again to rewrite its evidence from the notes |
| C | The universe | `Universe/Investable_Universe.csv` has rows under `main_identifier` | fill the seed, delisted names included — the `universe-point-in-time` skill says what belongs in it |
| D | The data | on this machine: `Data/Curator/Time_Series/` has files, `Universe/Security_Master.csv` exists, `Data/Refinery/Time_Series/` has files; and `RESULTS.md` has a measurement under *Before any experiment* with the analyzer section it came from | the first of `Data/curator.py`, `Universe/universe.ipynb`, `Data/refinery.py`, `Data/analyzer.ipynb` whose output is missing, in that order — `data-curator-custom-calculations`, `universe-point-in-time`, `data-analyzer-runs` |
| E | The blueprint | `BRAINSTORMING_1.md` has its first entry, the benchmark; `Experiments/Experiment_N/BLUEPRINT_N.md` has lost the instruction blockquote at its top and every prediction names a note or an analyzer section, and it is committed before the rule cell of `experiment_N.ipynb` holds code | `brainstorm 1` for the benchmark when that entry is missing; else `blueprint N`; else the owner's commit |
| F | The broad reading | the leads the blueprint counted are read or recorded as leads in `BIBLIOGRAPHY.md`, and `BRAINSTORMING_N.md` has an entry after the blueprint | `read` for the first lead, or `brainstorm N` |
| G | The cycle | section 2 of `experiment_N.ipynb` holds the rule; on this machine `Portfolio/`, `Backtest/` and `Attribution/` hold output; `FINDINGS_N.md` reports, every prediction of the blueprint evaluated | the first of `portfolio-construction-runs`, `backtest-engine-runs`, `attribution-analysis-runs` whose output is missing; `alpha-decomposition` to read it; then `challenge N` once `FINDINGS_N.md` reports |
| H | The results | `RESULTS.md` has the experiment's row citing `FINDINGS_N.md`, the claims' statuses in `OBJECTIVE.md` have moved, and `CHANGELOG.md` has the entry | the missing one of those three |

A to H done for the newest experiment: the next thing is either the gate — `Paper_Trading/
BITACORA.md`, the `paper-trading-gate` skill — when the owner believes the findings evidence its
first criterion, or Experiment N+1, as section 6 of `experiment-lifecycle` says, starting again at
E; the objective, the universe and the data are the strategy's and stay.

## Step 4: Report

In chat, short:

1. **Which folder this is**, and the status line where there is one.
2. **The checklist** as a table: each part, done or not, with the file that says so.
3. **Next:** one line — the part, the command or skill by name, and what it will ask for.

Nothing else. No file is written, no log entry appended, no number computed and no plan drafted:
when the owner says *do it*, that is the named command's own plan and go, not this one's.
