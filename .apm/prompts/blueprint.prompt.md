---
description: Draft BLUEPRINT_N.md in place for a strategy, once its objective has claims and its investable universe exists — thesis, rules, predictions — with every prediction citing a Bibliotheca note or an analyzer measurement, and the draft put to a critic; plan first, the owner's go, then write, before the rule. Only when the owner runs it by name, on a strategy they name or are working in.
input:
  - experiment: "The experiment number N"
  - strategy: "Optional: path to the strategy repository, if not the one the session is in"
---

# Draft a blueprint

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`. In a strategy — the session is open in a
repository with a `Bibliotheca/`, or the owner named one by path — *Working in a strategy* in
`AGENTS.md` says where each of these paths lands. With no home in the session, work from the
strategy alone, with no library contrast, and say so.

The blueprint is the hypothesis, fixed once written, recorded before the notebook's rule cell
exists. This command drafts it so that every prediction can be traced to something read or
measured, and writes it where the template keeps it. `${input:experiment}` is the experiment number
`N`; `${input:strategy}` is the strategy's path, given when the session is not already open in it.

## Step 1: Refuse if the order is wrong

The blueprint is E in *The order of work* in `AGENTS.md`. Stop, and name the part that comes
first, when:

- **The folder is the worked example** — its `README.md` is titled *Liquid Golden-Cross*, or
  `README.md` or `AGENTS.md` holds a line reading `<!-- example: begin -->`, the test `next` uses.
  The example is for reading and running, never built on; a strategy of the owner's own is
  `init-strategy <name>`.
- **`OBJECTIVE.md` has no claims** — the objective comes first, and its claims fine-tuned by reading
  for them: `objective`, then `read`.
- **`Universe/Investable_Universe.csv` has no identifier under its header** — the investable
  universe comes before the hypothesis about it.
- **`Experiments/Experiment_N/experiment_N.ipynb` already holds a rule in its section 2** — a
  hypothesis written after its test is not a hypothesis.
- **`BLUEPRINT_N.md` is already filled** — it carries the line this command writes under the
  experiment's heading, `**Written YYYY-MM-DD, before any rule was coded.**` It does not change once
  written; a new idea is Experiment N+1.

**For Experiment 1 the blueprint is already there to fill.** The template ships
`Experiments/Experiment_1/BLUEPRINT_1.md` as the headings and what belongs under each. Never write
the headings from memory — they are the template's. A strategy made from a template before 0.10.0
lacks the file: say so, give the command that brings the template's blank back, run from the
strategy's root, and stop. It never overwrites:

```bash
uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" strategy . --only Experiments/Experiment_1/BLUEPRINT_1.md
```

The owner runs it, and the draft continues from there.

**For N > 1 there is no file yet.** The blank is the `experiment-lifecycle` skill's
`references/blueprint-template.md` — the example's file with its own lines stripped — copied to
`Experiments/Experiment_N/BLUEPRINT_N.md` with `N` replaced, as that skill's section 6 says. Offer
the copy as the plan, make it on the owner's go, and the draft continues from there.

## Step 2: Read, in this order

1. `OBJECTIVE.md` — the claims this experiment tests, by number.
2. `AGENTS.md` in the strategy — *The bar any new signal must clear*. Read it, not a memory of it:
   a strategy may have changed it, and the predictions and the rules answer to it.
3. The strategy's `Bibliotheca/` notes, through `BIBLIOGRAPHY.md`, and which sources are still
   leads.
4. `RESULTS.md`, section *Before any experiment*, and anything in `Data/Analyzer/` — the
   measurements the analyzer has already made about the signal. The data comes before the blueprint
   in the order of work, so if that section is still the template's prose, say so in the plan and
   write every prediction that needed a measurement as a lead — *run analyzer section Y before
   predicting this*. Probe `RESULTS.md` first, not the folder: `Data/Analyzer/` is ignored by git,
   so a fresh clone has it empty even after D, the data, was done.
5. `Experiments/Experiment_N/BLUEPRINT_N.md` as shipped — the headings to fill — and for N > 1,
   `FINDINGS_1.md` (Experiment 1 is shared context) but **no other experiment's files** unless the
   owner has written the request and reason into `JOURNAL_N.md` first. Say so if they have not.
6. The home library, for the domains the thesis touches, and the owner's `Philosophy/` — as
   contrast and warning, never as a citation.
7. The reading map, `references/reading-map.md` in the `read` skill's folder — *Seven questions
   before any backtest* and *An idea's anatomy* — as questions to put to the owner, never as a bar
   the draft is held to.

## Step 3: Draft, in the file's own shape

Under each heading, the draft replaces the template's guidance paragraph: what belongs there gives
way to what does. The example's blueprint keeps the guidance only because its own lines are marked
as the example's.

- **Thesis** — one paragraph, modest on purpose, naming the economic mechanism. Before drafting it,
  put the map's seven questions before any backtest to the owner, once, in chat, as questions they
  may answer or skip: why the edge exists; who is on the other side, and why they keep losing; risk
  premium or mispricing, and which they mean to own; how many independent bets a year; whether it
  survives costs, and how much capital it takes; when it fails, and whether they would hold it
  through that; how many ideas came before this one. The thesis draws on what they answer — the
  deck's test is that the seven answers fit in one paragraph — and a question they skip is left
  out, never answered for them, and named again in *Step 5*. The bar in `AGENTS.md`, not these
  seven, is what the draft must meet.
- **The claim this moves** — one claim of `OBJECTIVE.md`, by number, and the status it reaches if
  the predictions hold and if they fail.
- **Rules** — selection, sizing, cash, timing, lag, the control, screens deliberately absent — each
  naming the column it reads and the shared module that implements it. The control differs from the
  book in exactly one ingredient and trades on the rule's own rebalance dates.
- **Predictions** — the table the template gives. **Every row's *where it comes from* is a note in
  `Bibliotheca/` or an analyzer section with its number.** A prediction with neither is written as a
  lead — *read X, or run analyzer section Y, before predicting this* — and counted separately.
  Each row says what would falsify it.
- **Success criteria**, **what would falsify it** — one condition for the whole experiment, and the
  changes that may not rescue it — **key risks** and **open questions this experiment does not
  answer**, in the template's terms. For Experiment 1, what it has to beat is the benchmark
  `BRAINSTORMING_1.md` names.
  For the falsifying condition, ask the owner for the kill switch — the result that would make them
  drop the idea rather than tune it, the map's *An idea's anatomy* — or propose the one the claim
  already carries in `OBJECTIVE.md`; the condition names it, in their words. With none given, the
  drafted condition stands, labelled as the kill switch for them to confirm, change or refuse.
- Add one line under the experiment's heading, with today's date, as the example's blueprint does:
  `**Written YYYY-MM-DD, before any rule was coded.**` — and after it, on the same line, the
  package the draft was made with: `Drafted with KaxaNuk-Researcher X.Y.Z, commit abc1234.` Read
  both from `~/.apm/apm.lock.yaml`, the entry named `kaxanuk-researcher`: its `version`, and the
  first seven characters of its `resolved_commit`. Installed from a local path, the entry has no
  commit: write `local` in its place. With no such entry, read `version:` in
  `~/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/apm.yml` and write no commit; with neither,
  write `version unknown` and say so in *Step 5*. Never a version from memory: the stamp is how
  `challenge` tells whether the process changed between the blueprint and its run. Leave the
  template's blockquote at the top,
  whole, its last line included: *delete this blockquote* is addressed to the owner, who deletes it
  when they commit — never you, before or after the go.

## Step 4: Put the draft to its critic

The blueprint does not change once written, so its weak spots are found now, not at `challenge`.
Where the assistant can call a subagent and the `blueprint-critic` agent is installed, hand it the
draft, the experiment number and the strategy's path, and bring its objections back to show beside
the draft. The critic reads and objects; it writes nothing, and the owner's go stays the only go.
Where the assistant cannot call a subagent, or the agent is not there, review the draft yourself
against the same checklist, and say in *Step 5* that you did: a second reader would have been
better than the hand that drafted it.

The checklist. The agent's objections cover the same ground, grouped their own way, and add two: a
rule that reads data it could not have had on the date, and a tuned parameter with no reason written
beside it. The agent reads only the strategy, so item 6's source against the idea in the home
library is yours to check:

1. **Every prediction's source.** Each row names a note in `Bibliotheca/` that says what the row
   says, or an analyzer section by its number in `RESULTS.md`; a row with neither is written and
   counted as a lead.
2. **Every prediction's falsifier.** Each row says what would falsify it, in terms `FINDINGS_N.md`
   can report; a falsifier with two limbs fires on either.
3. **A prediction worth being wrong about.** A table of things that will obviously happen is not a
   hypothesis.
4. **No performance number without a licence.** No return, Sharpe or drawdown is predicted unless
   an analyzer measurement licenses it.
5. **The bar in the strategy's `AGENTS.md`**, item by item: the economic reason stated in the
   thesis; a *Control* line in *Rules* that differs from the book in exactly one thing and trades on
   the rule's own rebalance dates (item 9); a trial count, if variants will be ranked (item 3);
   results net of the costs the rules declare; each parameter chosen on a property of the signal,
   never on the metric it will be judged by; one condition under *What would falsify it* and the
   changes that may not rescue it (item 10); for any coefficient or ratio a prediction leans on, its
   horizon and overlap, and the share of dates with the expected sign beside it (item 11).
6. **The source against the idea.** The thesis or the key risks name what argues against it, when
   the strategy's `Bibliotheca/` or the home library holds it.
7. **The claim this moves.** One claim of `OBJECTIVE.md`, by number, and the status it reaches
   either way.

## Step 5: Show, wait, then write

Show the draft in chat, the critic's objections beside it — each with what the draft does about it,
changed or kept and why — or the line saying the command reviewed it itself. Then list: the leads
(notes to write first), the predictions the owner should be willing to be wrong about, the analyzer
sections still to run, the seven questions they left open and whether the kill switch is theirs or
still the draft's, and **anything the bar in `AGENTS.md` asks for that the draft does not have**
— a control differing in exactly one thing on the rule's own dates, a trial count if variants will
be ranked, the one falsification condition — so the owner meets now what graduation will ask, not at
the gate. Wait for the go. Then write it into `Experiments/Experiment_N/BLUEPRINT_N.md` in the
strategy, under the template's headings and its blockquote. The owner edits and commits it **before
writing the rule** — in a commit of its own, so the history shows the order. Then say what comes
next in the order of work: the broad reading, for what the blueprint left as leads; `brainstorm`,
for what to try next; and the cycle — portfolio construction, backtest, attribution — until it is
finished.

Never write into the researcher's home from here. Never state a performance number as a prediction
unless an analyzer measurement licenses it; the engine has not run, and the blueprint must not
pretend it has.
