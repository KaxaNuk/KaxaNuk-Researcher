# Journal — Experiment 2

> **Append-only, dated, oldest first.** Every iteration of this experiment, in the order it
> happened. Maintained by the AI as work proceeds.
>
> **Earlier entries are never edited.** The one exception is correcting an error, and the correction
> is written as a new entry saying what was wrong — not by rewriting the original.
>
> The hypothesis is in [`BLUEPRINT_2.md`](BLUEPRINT_2.md); what to try next is in
> [`BRAINSTORMING_2.md`](BRAINSTORMING_2.md); the results that survive are in
> [`FINDINGS_2.md`](FINDINGS_2.md).

**Paths and figures inside entries are as they were written.** Where a path has since moved the
entry is left alone — it was correct on its date.

**Repository-level history belongs here** — choosing the benchmark, the data step, the architecture.
Experiment 1 is the first rule tested against the benchmark and therefore the shared context; later
experiments' journals point here rather than copying it.

**Entry format:**

```
## YYYY-MM-DD — short topic

- Idea / question:
- What we tried / considered:
- Outcome / decision:
- Open threads:
```

---

The first entry is usually *repository instantiated from the template*: what this repository is for,
which template version it was created from, the strategy name, and everything `OBJECTIVE.md` still
leaves open.

<!-- example: begin -->

## 2026-09-24 — the blueprint, the critic, and the dead names' download

- **Idea / question:** confirm Experiment 1's diagnostic arm on 2002 to 2016, with the seed widened
  to every listing the KN US Equity 600 held since 2000 and the names FMP does not carry fetched
  from Sharadar, as the owner decided on 2026-09-24 (`BRAINSTORMING_2.md`).
- **What we tried / considered:**
    - `BLUEPRINT_2.md` was drafted before any rule was coded and before any price after the
      widening was read, then reviewed cold by the blueprint critic, which returned eighteen
      findings: these years were already seen by the first design's long window; the trigger was
      described wrongly; the cited reversal note does not license the thesis; the coverage rule had
      no floor; the exclusions had no test; the dead names' close fill needed a check of its own;
      the perturbation's 20% band cell trades on the headline's days; and the predictions were not
      marked as leads. Every finding was taken, and the figures it quotes were checked against
      `RESULTS.md`, `FINDINGS_1.md` at tag `v0.15.0` and the notes it cites before they were
      written in.
    - **The widening.** The desk's holdings, 2000-01-03 to 2026-08-14, hold 1,399 listings; the seed
      of 788 matches 687 of them. The other 712 were asked of Sharadar in one call through
      `Data/curator.py --provider sharadar --end-date 2026-09-23`, started at 07:13 on 2026-09-24.
    - **The Curator for the dead names:** the Data Curator's `issues/31` branch at commit
      `8b54c2f`, built as 0.49.1, the only version with the Sharadar provider. That branch still
      has the Curator's 0.49 call, one market provider, where `Data/curator.py` makes 0.50's call;
      a launcher outside the repository translated the one into the other, and the code here keeps
      the call the release carrying Sharadar will have. The Sharadar key was read from
      `Config/.env` and never printed.
- **Outcome / decision:** the blueprint is committed before the rule. What the download returned
  is the next entry.
- **Open threads:** the coverage measurement that fixes the test's start; the exclusions by
  Experiment 1's two tests; the twenty seed names fetched from both providers and compared.

<!-- example: end -->
