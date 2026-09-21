---
description: Draft BLUEPRINT_N.md in place for a strategy, once its objective has claims and its investable universe exists — thesis, rules, predictions — with every prediction citing a Bibliotheca note or an analyzer measurement; plan first, the owner's go, then write, before the rule. Only when the owner runs it by name, on a strategy they name or are working in.
input:
  - strategy: "Optional: path to the strategy repository, if not the one the session is in"
  - experiment: "The experiment number N"
metadata:
  version: 0.4
---

# Draft a blueprint

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`. In a strategy — the session is open in a
repository with a `Bibliotheca/`, or the owner named one by path — *Working in a strategy* in
`AGENTS.md` says where each of these paths lands.

The blueprint is the hypothesis, fixed once written, recorded before the notebook's rule cell
exists. This command drafts it so that every prediction can be traced to something read or
measured, and writes it where the template keeps it. `${input:experiment}` is the experiment number
`N`; `${input:strategy}` is the strategy's path, given when the session is not already open in it.

## Step 1: Refuse if the order is wrong

The blueprint is item 5 of *The order of work* in `AGENTS.md`. Stop, and name the item that comes
first, when:

- **`OBJECTIVE.md` has no claims** — the objective comes first, and its claims fine-tuned by reading
  for them: `objective`, then `read`.
- **`Universe/Investable_Universe.csv` has no identifier under its header** — the investable
  universe comes before the hypothesis about it.
- **`Experiments/Experiment_N/experiment_N.ipynb` already holds a rule in its section 2** — a
  hypothesis written after its test is not a hypothesis.
- **`BLUEPRINT_N.md` already has its slots filled** — it does not change once written; a new idea is
  Experiment N+1.

**A strategy made by `init-strategy` has no blueprint to fill.** The template ships
`Experiments/.gitkeep` and nothing else; `BLUEPRINT_N.md` and its siblings are in the worked
example. Never write the headings from memory — they are the template's. Say so, and give the
command that brings the file across, run in the strategy's session, and stop:

> init-example Experiments/Experiment_1/BLUEPRINT_1.md

`init-example` copies it from the example inside the KaxaNuk Researcher package and names what is the
worked strategy's: everything between `<!-- example: begin -->` and `<!-- example: end -->`, which
goes before the draft. For N > 1 the file is renamed into
`Experiments/Experiment_N/BLUEPRINT_N.md`. The owner runs it, and the draft continues from there.

## Step 2: Read, in this order

1. `OBJECTIVE.md` — the claims this experiment tests, by number.
2. The strategy's `Bibliotheca/` notes, through `BIBLIOGRAPHY.md`, and which sources are still
   leads.
3. `RESULTS.md`, section *Before any experiment*, and anything in `Data/Analyzer/` — the
   measurements the analyzer has already made about the signal. The data comes before the blueprint
   in the order of work, so if that section is still the template's prose, say so in the plan and
   write every prediction that needed a measurement as a lead — *run analyzer section Y before
   predicting this*. Probe `RESULTS.md` first, not the folder: `Data/Analyzer/` is ignored by git,
   so a fresh clone has it empty even after item 4 was done.
4. `Experiments/Experiment_N/BLUEPRINT_N.md` as shipped — the headings to fill — and for N > 1,
   `FINDINGS_1.md` (the benchmark is shared context) but **no other experiment's files** unless the
   owner has written the request and reason into `JOURNAL_N.md` first. Say so if they have not.
5. The home library, for the domains the thesis touches, and the owner's `Philosophy/` — as
   contrast and warning, never as a citation.

## Step 3: Draft, in the file's own shape

- **Thesis** — one paragraph, modest on purpose, naming the economic mechanism.
- **Rules** — selection, sizing, cash, timing, lag, screens deliberately absent — each naming the
  column it reads and the shared module that implements it.
- **Predictions** — the table the template gives. **Every row's *where it comes from* is a note in
  `Bibliotheca/` or an analyzer section with its number.** A prediction with neither is written as a
  lead — *read X, or run analyzer section Y, before predicting this* — and counted separately.
  Each row says what would falsify it.
- **Success criteria**, **key risks** and **open questions this experiment does not answer**, in the
  template's terms. For Experiment 1, the benchmark does not need to win.
- Fill the recorded date with today's, and say in the header that it was written before the rule.
  Leave the template's blockquote at the top: the owner deletes it when they commit.

## Step 4: Show, wait, then write

Show the draft in chat and list: the leads (notes to write first), the predictions the owner should
be willing to be wrong about, and the analyzer sections still to run. Wait for the go. Then write
it into `Experiments/Experiment_N/BLUEPRINT_N.md` in the strategy, under the template's headings.
The owner edits and commits it **before writing the rule** — the branch's first commit, so the diff
shows the order. Then say what comes next in the order of work: the broad reading, for what the
blueprint left as leads; `brainstorm`, for what to try next; and the cycle — portfolio
construction, backtest, attribution — until it is finished.

Never write into the researcher's home from here. Never state a performance number as a prediction
unless an analyzer measurement licenses it; the engine has not run, and the blueprint must not
pretend it has.
