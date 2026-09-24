---
description: Challenge a finished experiment against its own blueprint — which predictions held, which falsifiers fired, what the findings do not say — reported in chat and, on the owner's go, as one appended JOURNAL_N.md entry. Never edits the blueprint, the findings or the results, and never computes a number. Only when the owner runs it by name, on a strategy they name or are working in.
input:
  - experiment: "The experiment number N"
  - strategy: "Optional: path to the strategy repository, if not the one the session is in"
---

# Challenge a finished cycle

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`. In a strategy — the session is open in a
repository with a `Bibliotheca/`, or the owner named one by path — *Working in a strategy* in
`AGENTS.md` says where each of these paths lands. With no home in the session, work from the
strategy alone, with no library contrast, and say so.

This is G and H of *The order of work*: the cycle has run, and the researcher's part is to
challenge it. A blueprint is a set of predictions somebody was willing to be wrong about; this
command asks whether the run treated them that way. `${input:experiment}` is the experiment number
`N`; `${input:strategy}` is the strategy's path, given when the session is not already open in it.

**It is the last command that runs, and the only one whose default output is no file at all.**

## Step 1: Refuse if there is nothing to challenge

- **The folder is the worked example** — its `README.md` is titled *Liquid Golden-Cross*, or
  `README.md` or `AGENTS.md` holds a line reading `<!-- example: begin -->`, the test `next` uses.
  The example is for reading and running, never built on; a strategy of the owner's own is
  `init-strategy <name>`.
- **No `Experiments/Experiment_N/BLUEPRINT_N.md`, or it is not filled** — it lacks the line
  `blueprint` writes under the experiment's heading, `**Written YYYY-MM-DD, before any rule was
  coded.**` — there is no hypothesis to check the run against: `blueprint`, E.
- **No `FINDINGS_N.md`, or it reports nothing yet** — the cycle is still running. Say so and stop;
  challenging a run in progress invites the findings to be written to match.
- **Home** — there is no experiment here. Say so and stop.

## Step 2: Read, in this order

1. `Experiments/Experiment_N/BLUEPRINT_N.md` — every prediction with its falsifier, the declared
   window, universe, rules, costs and success criteria, and the claim it names under *The claim this
   moves* where it has that section. This is the fixed side of the comparison.
2. `FINDINGS_N.md` — the verdicts, the tally, the trial count, the caveats, and the claim it says
   the experiment moved.
3. `JOURNAL_N.md` — what happened during the run, and what was already disclosed.
4. `RESULTS.md`, including *Before any experiment* — where the analyzer's measurements survive once
   notebook outputs are stripped, and where the published numbers live.
5. `OBJECTIVE.md` — the claims this experiment tests, and their statuses.
6. `BIBLIOGRAPHY.md` and every note a prediction cites, in the strategy's `Bibliotheca/`.
7. `AGENTS.md` in that repository — the bar a result has to clear, and who writes each document.
8. `Paper_Trading/BITACORA.md` only when graduation is being claimed.

**Not the engine's workbooks.** `Backtest/` and `Attribution/` are gitignored outputs; reading
numbers out of them is the line the non-negotiables draw. Every number in the report is quoted from
`FINDINGS_N.md` or `RESULTS.md`, with its source named.

## Step 3: The checks

1. **Verdict against falsifier.** Take each prediction's falsifier as written. A falsifier with two
   limbs fires when either limb fires — a verdict of *split* or *mixed* where a limb fired is a
   falsification recorded in a softer word, and that is the single most useful thing to catch.
2. **The tally against the rows.** Count the rows yourself and compare with the sentence that sums
   them up. A row counted twice, or a verdict dropped, is a bookkeeping error, not a finding about
   the strategy.
3. **A verdict that answers a question the prediction did not ask.** *Falsified against the index,
   confirmed against the control* where the prediction named only the index is a falsification plus
   a new observation; say that the second half belongs in a new line, not in the verdict.
4. **The run against the frozen blueprint.** Window, universe, rules, costs and any parameter the
   run added. A deviation with a good reason is fine — an undisclosed one is not: check that it is
   in the caveats or the journal, and name it when it is nowhere.
5. **Success criteria, one by one.** Each is met, unmet or unevaluated, before any claim of
   adoption or graduation. A criterion that passes is worth a line too. When the owner claims
   graduation, the gate is covered here: `Paper_Trading/BITACORA.md`'s five criteria are read
   against `FINDINGS_N.md` and `RESULTS.md`, each evidenced or not met, and nothing is written
   there.
6. **The notes behind the predictions** — the part no backtest reviewer will do. Open each cited
   note: does it say what the prediction says it says, does the relative path resolve inside the
   strategy, and is any source cited that has no note? Where the findings claim a source's failure
   mode reproduced, check that against the note rather than against memory.
7. **The trial count.** `FINDINGS_N.md` owes it, under *The trial count*: how many variants were
   ranked to reach the book, and every run excluded by name with its reason. `RESULTS.md` compiles
   it. A count missing from the findings is a finding whether or not graduation is claimed, and one
   present in `RESULTS.md` but not in `FINDINGS_N.md` is a summary leading its source.
8. **Closure.** Every falsified prediction and every falsified claim reaches `RESULTS.md` under
   *What is closed* or *Known limitations*, and the claim's status in `OBJECTIVE.md` moves. Where
   the blueprint names a claim under *The claim this moves*, that is the claim to follow:
   `FINDINGS_N.md` names the status it reached, and `OBJECTIVE.md` — and the experiment's *Claim
   moved* in `RESULTS.md`, where that column exists — carry the same one. A findings file that names
   a different claim, or two files that give it different statuses, is a finding. Where the
   blueprint names none, read the statuses in `OBJECTIVE.md` of the claims it tests. What stops the
   next person repeating an experiment is written down, or it does not exist.
9. **Arithmetic between published numbers.** A difference published alongside the two numbers it
   comes from either reconciles or it does not. Report a disagreement and ask for a re-run; never
   supply the corrected value.

Two things cannot be checked from the working tree, and the report says so when they matter: the
falsifiers are prose, so pairing *a beta at or above one* with *beta is 1.028* is a judgement made
in words; and the ordering the whole process rests on — the blueprint committed before the rule,
the counterfactuals before the engine — lives in the git log, not in the files. So read the log:
run `git log --oneline -- Experiments/Experiment_N` and quote in the report what it shows — the
commit that brought `BLUEPRINT_N.md` in, and whether it came before the one that put the rule into
`experiment_N.ipynb`. A blueprint that arrived in the same commit as its rule, or after it, cannot
be told from one written afterwards; say so. The log is read, never changed.

## Step 4: Report, and offer the one line it may write

**In chat:** what held, what failed and by which falsifier, what the findings do not say, and the
bookkeeping. Then the leads — what to read for what the run left open, and what `brainstorm` should
consider next. Name every file and every note by path.

**Then offer one appended entry in `JOURNAL_N.md`**, dated, in the template's format, and write it
only on the owner's go. It is the one file this command may touch, because the journal is appended
and never edited, and a look-across is already recorded there.

**What it never does, whatever the argument:**

- **`BLUEPRINT_N.md` — never, once written.** A prediction worded better after its test is not a
  prediction. A wording problem becomes a lead for the next blueprint.
- **`FINDINGS_N.md` and `RESULTS.md`** belong to the experiment's own writer, and a challenger that
  rewrites what it challenges is both hands at once. Report the discrepancy and stop.
- **`OBJECTIVE.md`** — a claim's status is `objective`'s to change, and its wording is the owner's.
- **Compute or restate a performance number**, including a corrected one. The engines produce
  numbers; this command compares the ones already written down.
- **Declare graduation.** The gate's last criterion is a person's signature.
- **Open another experiment's files** unless the request and the reason are already in
  `JOURNAL_N.md`, and **write anything at home.**
