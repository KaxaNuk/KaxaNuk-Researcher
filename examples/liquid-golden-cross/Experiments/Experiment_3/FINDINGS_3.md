# Findings — Experiment 3

> **Latest valuable results only.** This file is rewritten when a result changes, not appended to —
> the running history is in [`JOURNAL_3.md`](JOURNAL_3.md), and the hypothesis this tested is in
> [`BLUEPRINT_3.md`](BLUEPRINT_3.md).
>
> **[`../../RESULTS.md`](../../RESULTS.md) is compiled from this file.** When a finding here
> changes, change it here first, then update the summary.

## Status

**Not yet run.** When it has: one line saying whether the rule beat the benchmark and its control
by what the blueprint required, and whether it is a candidate for the gate in
`Paper_Trading/BITACORA.md` — a success is necessary for graduation, not sufficient. Then **the
claim it moved**: the claim of `OBJECTIVE.md` the blueprint named, and the status it reached — or
why it reached none.

## The predictions, evaluated

**Every prediction in the blueprint gets a row, including the ones that were wrong.** A falsified
prediction is worth more than a correct one: it says something about the strategy that nobody knew,
and it cost one run to find out.

| # | Prediction | Outcome | What it changed |
| --- | --- | --- | --- |
| 1 | as written in the blueprint | confirmed or falsified, with the number | what is now understood differently |

## The book, priced by the engine

Record the date of the last full re-run from a wiped working copy, the engine version, and the
window. Then the book against every benchmark it reports against, and against the control its
blueprint names, on the rule's own rebalance dates: CAGR, volatility, Sharpe, Sortino, maximum
drawdown.

## What the benchmark actually is, structurally

Rebalance frequency, turnover, holdings, concentration, invested share, and any structural tilt —
each with a reading of what a bad value would have meant.

## The trial count

How many variants were ranked to reach the book above, and every run excluded by name with its
reason. `RESULTS.md` compiles this: a reader cannot discount a best-of-N result without knowing N,
and the graduation sign-off says whether the deflated figure was also computed.

## Attribution — is this the signal, or a factor exposure wearing its name?

Brinson-Fachler: allocation, selection, interaction. The factor model: factor against idiosyncratic.
State the window, which is bound by the supplied files' coverage and is usually shorter than the
backtest.

**What it settles**, and **what it does not** — naming the counterfactual book that would settle
what is left: the same holdings with the signal off, positions equalised, a random draw at the same
sizes, entry dates shifted.

## What is open, ranked

The single highest-value run outstanding, and what it would settle.

## Caveats

| # | Caveat | Effect |
| --- | --- | --- |
| 1 | what a reader must know before quoting a number above | what it does to that number |
