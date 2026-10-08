---
source: "not recorded. Add it the next time this source is opened; a wrong link is worse than none."
citation: "Journal of Portfolio Management 40(5), 94-107. Cited from the journal reference only; this entry has not been link-checked."
local_copy: none
read: "2026-09-02; what was read: not recorded"
---

# Bailey & López de Prado (2014) — *The Deflated Sharpe Ratio*

## What it says

Provides a Sharpe ratio corrected for the number of trials attempted, for non-normality, and for
track-record length. The maximum Sharpe across N backtests is a biased estimate of the best
strategy's true Sharpe, and the bias grows with N.

## What it implies for Golden Flow

> Rewritten on 2026-10-07 for this copy, after FINDINGS_1.md reported.
>
> **Claims 1 and 2 rest on one book that came after others, and this paper says what that costs.**
> The rule's parameters were fixed before its run. One exit rule, selling at t−1 before a price
> stops, was added after the first attempt, whose 31 books are counted. In all, 107 books count as
> trials across this strategy's versions.
> The window and the margins were set knowing an earlier version's result
> ([`FINDINGS_1.md`](../../Experiments/Experiment_1/FINDINGS_1.md), *The trial count* and caveat 4).
>
> This paper asks how much of the rule's Sharpe of 0.842, against its control's 0.763, survives that
> search. The deflated Sharpe was not computed, and the owner signed knowing it. Computing it is
> open item 3 of `FINDINGS_1.md`.
