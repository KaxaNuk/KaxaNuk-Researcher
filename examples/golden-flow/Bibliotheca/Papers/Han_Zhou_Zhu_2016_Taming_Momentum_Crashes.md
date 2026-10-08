---
source: "link not recorded. Add it the next time this source is opened; a wrong link is worse than none."
citation: "Working paper, SSRN id 2407199. Cited from that reference only; the copy linked on 2026-08-20 was a third-party mirror, not the authors', and is not carried."
local_copy: none
read: "2026-09-02; what was read: not recorded"
---

# Han, Zhou & Zhu (2016) — *Taming Momentum Crashes: A Simple Stop-Loss Strategy*

## What it says

A plain stop-loss overlay on a momentum portfolio raised average monthly return from 1.01% to 1.73%
and cut the left tail dramatically. Most of the benefit comes from truncating the worst losers early
rather than from better selection.

## What it implies for Golden Flow

> Rewritten on 2026-10-07 for this copy, after FINDINGS_1.md reported.
>
> **Claim 1, the signal, and against it.** On this paper's argument the death cross — the 50-day
> average falling back under the 200-day — is the slowest possible stop: it confirms a fall that has
> already happened. The paper overlays a long/short momentum book, whose short leg carries the crash
> risk. Golden Flow is long only, and runs no other stop, by design
> ([`BLUEPRINT_1.md`](../../Experiments/Experiment_1/BLUEPRINT_1.md), *Rules*).
>
> Even so, the slow exit cut the worst drawdown to −32.47%, against −46.32% for the control, the
> same rule without the cross ([`FINDINGS_1.md`](../../Experiments/Experiment_1/FINDINGS_1.md),
> prediction 2). No stop-loss besides the cross was tested. The sweep's faster cross, 20/100, kept
> a Sharpe margin of +0.064 over its own control and lost 0.85 points of CAGR to it
> ([`FINDINGS_1.md`](../../Experiments/Experiment_1/FINDINGS_1.md), the sweep). This paper is the
> case for testing a stop-loss in a later experiment, against this rule.
