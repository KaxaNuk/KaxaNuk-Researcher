# Agents — how work is done here

The
[template's README](https://github.com/KaxaNuk/KaxaNuk-Researcher/blob/main/templates/strategy/README.md)
says what this process **is** and where each kind of logic goes; read it first. This file says
**how work is done**: who writes each document, the restrictions, and the bar a result has to
survive before anyone believes it.

> **Status: the template.** No strategy, no data, no result and no code: beyond
> `Config/.env.template`, the header-only seed in `Universe/` and the `Bibliotheca/` index and log,
> every file in the folders is a description of what belongs in it — a `.py` file its docstring, a
> notebook its markdown cells — to be filled in. Replace this banner with your own status when you
> take the repository over; it is the same line as your `README.md`'s.

## First run — for the agent, before anything else

**If `.venv/` is missing, this repository has not been set up.** Say so, and offer to follow
[`SETUP.md`](SETUP.md): the commands in it, every one of them run in the repository root, never a
level above it. A missing `apm_modules/` is expected: the skills are installed once for the user,
and nothing is installed here. Do not start research work in a folder that has not been set up, and
never create a folder around this one: one folder is the whole project, as `SETUP.md` says.

Three rules from `SETUP.md` apply from the first command:

- **Never open, read back, print or echo `Config/.env`**, and never put a value from it into a
  command that gets recorded. You may say which keys are still empty, **by name only**.
- **Install no skills here.** They are installed once for the user, with `apm install -g`, as
  *step 4* of `SETUP.md` says, and `apm update -g` keeps them current for every strategy.
- **Skills are discoverable in a new session**, not the one in which they were installed. Say so
  rather than claiming they are already active.

## How work reaches `main`

Work is committed on `main`, in small commits whose messages say what moved and why, each with its
`CHANGELOG.md` entry. A branch and a pull request are for a change you want reviewed, or for two
lines of work that must not mix — never a gate — and the branch is deleted once it is merged or
abandoned: `main` is the only branch that stays.

**The template and the worked example, `liquid-golden-cross`, live in the
[KaxaNuk Researcher](https://github.com/KaxaNuk/KaxaNuk-Researcher)** package. The example is for
reading, never for building on: nothing in a strategy is brought across from it. Issues and pull
requests about the process land there, and so does a trap found in a Lab library while running a
strategy: it goes into that library's skill in the package, as an issue there, so the next strategy
does not find it again. A strategy of your own stays in your own repository.
What the template ships, and why, is *What is in here* in its README.

### The blueprint is committed before the rule

For an experiment, `BLUEPRINT_N.md` is committed in a commit of its own before the rule cell of
`experiment_N.ipynb` holds code; for Experiment 1 only the `BRAINSTORMING_1.md` entry choosing the
benchmark comes before it. The commit order is what shows the hypothesis was written before the
answer, so the two never share a commit.

### Before any commit to `main`

- `uvx ruff check .` passes, notebooks included.
- **Notebook outputs are stripped.** The committed notebook is the method; `FINDINGS_N.md` is the
  record.
- The `CHANGELOG.md` entry is part of the change-set, not a follow-up. If you cannot write the
  entry, the change-set is not finished.
- **A result is committed once the pipeline has re-run end to end from a wiped working copy**, and
  every notebook has reached the end of its Verify section.
- **If a published number moved, the commit message says which** — and `FINDINGS_N.md` changed
  before `RESULTS.md`, never the other way round.

## Who writes each document, and when it changes

| Document | Who writes it | Changes when |
| --- | --- | --- |
| `OBJECTIVE.md` | a person, first | the idea and the claims' wording almost never — a change is a *different* strategy; each claim's evidence and status move as notes arrive (B) and as findings report (H) |
| the notes in `Bibliotheca/` | a person, or a researcher made with `init-researcher` from the [KaxaNuk Researcher](https://github.com/KaxaNuk/KaxaNuk-Researcher), with its `read` skill — one per paper, one per chapter of a book somebody chose, after a plan and a go | a source is read. A later note corrects an earlier one with a callout above the claim, never by smoothing it away |
| `Bibliotheca/BIBLIOGRAPHY.md` | a person adds the leads; whoever writes a note adds its row | a source is added, or read |
| `Bibliotheca/LOG.md` | whoever reads a source or audits the folder appends it; the researcher's `read` and `audit` do so themselves | append only. Past entries are never edited |
| `RESULTS.md` | the AI, from the findings files | a `FINDINGS_N.md` changes |
| `CHANGELOG.md` | whoever lands a change-set | any change-set lands |
| `AGENTS.md` | anyone | the process changes |
| `BLUEPRINT_N.md` | a person, or with the AI | **never, once written.** A hypothesis edited after its test is not a hypothesis |
| `BRAINSTORMING_N.md` | a person, or with the AI | thinking happens — **before** the work |
| `JOURNAL_N.md` | the AI, as work proceeds | append only. Earlier entries are corrected by new entries, never edited |
| `FINDINGS_N.md` | the AI, from the journal | a result changes. It is rewritten, so there is exactly one current answer |

**`RESULTS.md` is compiled from the findings files and cites each one.** When a number changes,
change it in `FINDINGS_N.md` first — a summary that leads its sources is how two numbers for the
same book start to circulate. **One deliberate exception:** findings from step 3 go straight into
`RESULTS.md`, because notebook outputs are stripped before committing and a measurement living only
in a cell output does not survive the commit.

Repository-level history — the benchmark once `BRAINSTORMING_1.md` has chosen it, the data step,
the architecture — belongs in `JOURNAL_1.md`. Experiment 1 is the declared benchmark and therefore
the shared context; later journals point there rather than copying it.

---

# Restrictions

## One experiment at a time

**When working on `Experiment_N`, do not open another experiment's files** to decide what this one
should do. Each experiment stands on its own hypothesis. Reading another's answers first is how a
parameter tuned on one book quietly becomes the default of the next, and how three experiments
become one experiment reported three times.

Two standing exceptions, and one that has to be asked for:

- **Experiment 1 is the declared benchmark**, so its rules and published numbers are shared
  context. It is not a null: it is a real strategy with a real return. **Its rules freeze once
  `FINDINGS_1.md` reports** — a change invalidates every comparison in `RESULTS.md`, so
  improvements go into a new experiment.
- **`RESULTS.md` is the shared record.** Comparing *final* results across experiments is the whole
  point of having several. What is forbidden is borrowing another experiment's *choices* before your
  own are made.
- **A researcher may lift this, explicitly.** When one experiment needs to read another — to reuse
  a loader, to check a data fix, to build a control arm that differs in exactly one thing — the
  request and the reason go in that experiment's `JOURNAL_N.md` first. A look-across that is
  written down is a decision; one that is not is contamination.

## The bar any new signal must clear

1. **State the economic reason before running.** A result that arrives before a hypothesis is an
   observation, not evidence.
2. **Read sweeps as curves, not cells.** A parameter degrading monotonically across three settings
   is information; a variant beating its control by 0.001 Sharpe is not.
3. **Count the trials and publish the count.** A reader cannot discount a best-of-N result without
   knowing N.
4. **Accept results net, or not at all.** On a high-turnover book, the difference between a flat
   cost model and real per-share commission can be a third of the winning edge.
5. **Attribute before believing.** A strategy that beats its benchmark has not been understood until
   attribution says which part is factor exposure and which part is selection. This stack can do it,
   so "we could not tell" is not an available answer.
6. **Never choose a parameter on the metric it will be judged by.** Choose it on a property of the
   *signal* — persistence, coverage, turnover — and publish the sweep.
7. **Prefer the feature anyone can explain in a sentence.** Complexity is added one lever at a time,
   and each addition must beat the simpler baseline to earn its place.
8. **Report the rejected result as loudly as the promising one.** A negative result costs real work
   and stops the next person repeating it.
9. **Run a control that differs in exactly one thing.** The same rule with one ingredient removed,
   named in the blueprint's *Rules* before the run, and **trading on the rule's own rebalance
   dates**: a control left to choose its own dates also differs in when it trades, and the gap
   between the two books is then two effects read as one. Beating the index says the book worked;
   only the control says which part did.
10. **Pre-register what would falsify the experiment.** One condition for the whole experiment, in
    `BLUEPRINT_N.md` before the rule, and the changes that may not rescue it — a holding count, a
    trigger, a window. A change on that list made after the result is a new experiment, and a trial
    in the count of item 3.
11. **State the horizon and the overlap.** Forward returns over overlapping windows are not
    independent observations, and neither are the days of two books holding the same names: a
    t statistic or an information ratio counted as if they were overstates the evidence. Say the
    horizon and how many days consecutive windows share, and report the share of dates with the
    expected sign beside any t statistic or ratio.

## Other standing rules

- **Every performance figure comes from the KaxaNuk Backtest Engine.** There is deliberately no
  second, lighter simulator: one that disagrees just lets the reader pick the number they prefer.
- **Do not change a committed result to make it agree with a new run.** If the numbers moved, find
  out why first, and record it.
- **Do not quietly drop a bad run.** A run that cannot be believed is excluded **by name**, with its
  reason, in `RESULTS.md`.
- **Do not commit binaries or notebook outputs.** No charts, no engine workbooks, no PDFs.
- **Do not put logic in a file that cannot be traced to a stage.** If a reader cannot tell which
  step owns a file, it does not belong here, however correct it is.
- **Do not touch Production.** Step 8 is not in this repository and nothing here deploys.
- **Never print a value from `Config/.env`** — not into a commit, a notebook output, a log line, or
  a command that gets recorded. An exposed key is rotated, not edited out.
- **Never use the section symbol** in documents here. Write "section" or name the heading.

---

# Research integrity — the five ways a backtest lies

The part of the process that has nothing to do with Python.

| # | The lie | What the process does | What it still does not do |
| --- | --- | --- | --- |
| 1 | **Survivorship bias.** A universe built from *today's* members has deleted everything that failed, and the backtest discovers that markets go up | the seed is point-in-time and **retains delisted names**; step 2 quantifies how much of the universe is dead | audit the *last day* of a delisted name. The missing delisting returns are disproportionately the bad ones |
| 2 | **Look-ahead.** A signal computed from information that did not exist yet always works | every rule is struck on **shifted** data and fills at the next available price; a fitted signal is used in its causal form, and the smoothed form only where it is labelled as not tradable | remove the one stated leak: a delisting exit needs one day of hindsight, because a position is sold on the last day it still has a fill price |
| 3 | **Overfitting.** Try enough rules and one looks brilliant. The Sharpe of the best of *N* trials is the maximum of *N* draws | economic reason first, sweeps read as curves, parameters never chosen on the metric they are judged by, **the trial count published beside the winner** | compute the deflated figure. Publishing the count is the minimum, not the answer |
| 4 | **Costs and capacity.** A backtest with no costs describes a market that does not exist | commission on the **unadjusted** price, integer share counts, a cash reserve, turnover reported, results accepted **net** | model capacity, anywhere. Borrow cost, short rebate and margin are a headline caveat on any long/short book, not a footnote |
| 5 | **Dirty data presented as a finding.** An unadjusted split, a stale price, a reused identifier — each produces a plausible number and no error | coverage checked before conclusions; a truncated engine run is caught by the experiment's Verify section, which counts the days the engine valued against the window's trading days, and the variant is excluded **by name** | catch what nobody thought to check. The instructive case was a run that stopped valuing a book partway and still summarised cleanly over the stub |

**Every notebook ends in a Verify section, and that is where a strategy's tests live.** A strategy
has no test suite: what it adds is a pipeline, and each stage is checked where it produces its
output. Verify reads back what the notebook wrote and **raises** when it is wrong — a check that
prints *PASS* or *FAIL* is one somebody has to read, and a run nobody watches reads none of them.
**Check against the window, not against a fixed floor.** A floor a full run clears is cleared too by
a run that stopped years early, so count the days the engine valued against the trading days in the
window it was asked for. Where a licensed engine is absent, Verify skips its checks the way the
sections that call it do.

**The one deliberate look-ahead is named in its own column prefix.** A `current_*` column comes from
today's security master, so any period before a reclassification is misattributed. That is why the
prefix exists, why anything bucketed on it is read as indicative, and why no rule selects on one.

**If your signal is fitted, measure what look-ahead costs.** Read the same model causally and
smoothed and report the gap. It is the cheapest audit in the process and routinely the largest
number in it: the two series agree on most days and differ exactly at the turning points, which is
where the money is.

## What attribution must report

Savvy investors do not chase past performance. They follow a **process**, an **investing thesis**
and **data**, and attribution is what gives them all three about a book. Step 6 runs two
methodologies and a third pass, and `FINDINGS_N.md` reports each.

**First cut — Brinson-Fachler.** Active return split into **allocation** (did the book overweight
the right groups) and **selection** (did it pick the right names inside them), plus their
interaction. No more hand-waving about "the process worked": the exact lever that moved the needle
is named, and that is a process you can defend, refine or fix.

**Second layer — the factor model.** Realised return projected onto systematic exposures — beta,
momentum, residual volatility, liquidity — so **idiosyncratic alpha** is separated from
**compensated factor tilts**, taken on purpose or by accident. A book that looks like skilful
stock-picking in the first cut can turn out to be a persistent low-beta or momentum tilt that
happened to pay over the sample.

**Third pass — Brinson-Fachler again, on what is left.** Run the first cut on the residual after
factor exposure is stripped out. The selection story gets sharper, and it answers the question the
first cut alone cannot: **whether the Sharpe survives once that factor turns.**

**What it settles:** whether there is genuine idiosyncratic alpha — criterion 2 of the graduation
gate that `Paper_Trading/BITACORA.md` defines, evaluated, not deferred. For a strategy raising
outside money it is also the plainest signal of sophistication: allocators are not buying returns,
they are buying proof you know where the returns come from, and showing both layers cleanly is how
that proof is given.

**What to expect it not to settle:** an *absolute* rule is close to invisible to a factor model
built on *relative* factors, so a book can beat every benchmark while the model assigns roughly
nothing to the factor its thesis is named after. That is a finding, not a failure. The follow-ups
are counterfactual books the engine can already price: the same holdings with the signal switched
off, positions equalised within each date, a random draw from the eligible pool at the same sizes,
and the same holdings with entry dates shifted. Those four separate the exclusion filter, sizing
skill, selection skill and timing skill.

---

# Code style

PEP 8 plus a stricter house layer, shared across KaxaNuk repositories and installed by APM rather
than committed here. One-line summary: *optimise for the reader who has never seen this file.*

- **No import aliases**, and **no abbreviations** — no variable name under three characters.
- **No nested functions, ever.**
- **One item per line** in any comma-separated construct holding three or more items, or two on
  a line over the length limit.
- **Type hints everywhere**; quoted annotations rather than a `__future__` import.
- **Assign the error message to a named variable (`message`) before raising it**, and leave blank
  lines around `return` / `raise` / `yield`.
- **Docstrings are prose, not sections**, and never repeat what the type hints already say. Say
  *why*.

What is committed is the style check, and the whole repository passes it. Nothing checks the process
itself: its rules rest on review, and each stage's output on its notebook's Verify section.

```bash
uvx ruff check .
```

The house layer above is checked by the `bloom-code-lint` skill, installed with the rest; run it,
with `--max-line-length 100`, on the Python files you touched.
