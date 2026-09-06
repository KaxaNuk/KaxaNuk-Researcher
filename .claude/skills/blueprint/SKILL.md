---
name: blueprint
description: Draft BLUEPRINT_N.md for a strategy — thesis, rules, predictions — with every prediction citing a Bibliotheca note or an analyzer measurement; to Projects/, before the rule is written. Only when the owner runs it by name, on a strategy they name.
argument-hint: "<path to the strategy repository> <N>"
---

# /blueprint

The blueprint is the hypothesis, fixed once written, recorded before the notebook's rule cell
exists. This command drafts it so that every prediction can be traced to something read or
measured. `$ARGUMENTS` is the strategy's path and the experiment number `N`.

## 1. Refuse if the order is wrong

If `Experiments/Experiment_N/experiment_N.ipynb` already holds a rule in its section 2, stop and say
so: a hypothesis written after its test is not a hypothesis. If `BLUEPRINT_N.md` already has its
slots filled, stop too — it does not change once written; a new idea is Experiment N+1.

## 2. Read, in this order

1. `OBJECTIVE.md` — the claims this experiment tests, by number.
2. The strategy's `Bibliotheca/` notes, and which sources are still leads.
3. `RESULTS.md`, section *Before any experiment*, and anything in `Data/Analyzer/` — the
   measurements the analyzer has already made about the signal. For Experiment 1 there may be none.
4. `Experiments/Experiment_N/BLUEPRINT_N.md` as shipped — the headings to fill — and for N > 1,
   `FINDINGS_1.md` (the benchmark is shared context) but **no other experiment's files** unless the
   owner has written the request and reason into `JOURNAL_N.md` first. Say so if they have not.
5. The library, for the domains the thesis touches, and the owner's `Philosophy/`.

## 3. Draft, in the file's own shape

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

## 4. Deliver

Write `Projects/<strategy name>/BLUEPRINT_N.draft.md`, show it in chat, and list: the leads (notes
to write first), the predictions the owner should be willing to be wrong about, and the analyzer
sections still to run. The owner copies the draft into the repository, edits it, and commits it
**before writing the rule** — the branch's first commit, so the diff shows the order.

Never write into the strategy repository. Never state a performance number as a prediction unless an
analyzer measurement licenses it; the engine has not run, and the blueprint must not pretend it has.
