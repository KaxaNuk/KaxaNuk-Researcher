---
source: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461
citation: "Journal of Wealth Management, Spring 2007. Link verified 2026-08-20."
local_copy: none
read: "2026-09-02; what was read: not recorded"
---

# Faber (2007, updated 2013) — *A Quantitative Approach to Tactical Asset Allocation*

## What it says

A ten-month simple-moving-average filter — hold while the close is above the average, otherwise sit
in cash — applied across asset classes delivers equity-like returns with bond-like drawdowns. The
point is not return enhancement. It is that a trivially simple trend filter is a drawdown-control
device.

## What it implies for Golden Flow

> Rewritten on 2026-10-07 for this copy, after FINDINGS_1.md reported.
>
> **Claim 1, the signal.** The paper reads a moving-average filter as a drawdown control, and that
> is what Golden Flow's book shows most strongly. Its worst drawdown is −32.47%, against −46.32% for
> the control, the same rule with the golden cross removed
> ([`FINDINGS_1.md`](../../Experiments/Experiment_1/FINDINGS_1.md), prediction 2). The filter also
> added return here, which the paper does not promise: 20.33% a year against 19.73%, and a Sharpe of
> 0.842 against 0.763.
>
> Two things it does not license. Its filter runs on asset-class indices, not on single names. And
> its "else cash" leg has only a partial counterpart: the rule moves to `BIL` only when fewer than
> five names are eligible, which never happened.
