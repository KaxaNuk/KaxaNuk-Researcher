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

<!-- example: begin -->

## 2026-09-24 — before the rule: the download, the provider check, the exclusions and the start

- **Idea / question:** everything `BLUEPRINT_2.md` asks to be recorded before the rule runs.
- **What we tried / considered:**
    - **The download.** Sharadar answered the one call for the 712 names; 665 came back with a price
      file and 47 with none — `AFS.A`, `ARC1`, `ASDV`, `BFO1`, `CBS1`, `CDP1`, `CG1`, `CHA1`,
      `CLFY`, `CNG`, `COMR`, `CSR1`, `DLJ`, `DNB1`, `ETEK1`, `FJ`, `FPC`, `GIC1`, `GTE1`, `HLI.A`,
      `HRD1`, `JPM1`, `LCOS`, `LGE`, `MIR1`, `NA.A`, `NCE`, `NGH`, `NN1`, `NSOL`, `OCLI`, `PNU1`,
      `PWJ1`, `RLM1`, `RLR`, `SE2`, `SEG1`, `TAP1`, `TMC.A`, `TVGIA`, `UCM`, `UPR`, `USW`, `VO1`,
      `VRI`, `WLA`, `YNR` — each reported by the provider as having no market data. Every one of
      the 712 was asked of Sharadar, including the few FMP also carries, so one provider serves
      every name added. The seed now marks them in its `provider` column, and a refresh never asks
      FMP for them.
    - **The provider check**, the first twenty names of the seed, in its order, that both providers
      carry — `A` to `AES`, `ADS` skipped because Sharadar has no metadata for it — fetched from
      Sharadar into a folder outside the repository and compared with FMP's files, daily returns,
      2002-07-30 to 2026-06-01. The mark, the dividend-and-split-adjusted close, agrees: a median
      daily gap of 0.00 to 2.82 basis points, a correlation of 0.9978 or more, and at most fourteen
      days in twenty-four years apart by more than one percent. The fill does not, as expected: the
      FMP fill is the day's VWAP and Sharadar's is the close, a median daily gap of 45.9 to 80.0
      basis points and a correlation of 0.74 to 0.88. That is the difference the blueprint's check
      with every name filled at the close exists to price.
    - **The exclusions**, by Experiment 1's two tests read from `Universe/Data_Issues.csv` and the
      universe notebook's identity check: the 47 names with no price file, and `CIT`, `FMC`, `LCI`
      and `PARA`, whose adjusted price multiplies by more than six in a day. Fifty-one in all; none
      carries two companies under one identifier. No name is excluded for a fall.
    - **The coverage and the start.** The priced names, excluded names counted as unpriced, hold
      99.59% of the index's weight or more on every date from 2001; the lowest inside the test is
      99.71%, on 2003-09-02, and no date after the start falls below 95%. **The test starts on
      2002-07-30**, the first date the rule allows, and runs to 2016-12-30; sub-period 1 runs from
      2002-07-30 to 2006-12-29.
    - **The Curator for the dead names:** the `issues/31` branch at commit `8b54c2f`, as the
      blueprint requires recorded.
- **Outcome / decision:** the rule runs as the blueprint fixed it, on this start and these
  exclusions.
- **Open threads:** a daily refresh of the names Sharadar serves, should this book reach paper
  trading: the few still trading would otherwise stop at 2026-09-23.

<!-- example: end -->

<!-- example: begin -->

## 2026-09-24 — the first run could not be priced; the reserve revised to 5%

- **Idea / question:** the rule as the blueprint fixed it, run in full from 08:48 to 09:25.
- **What we tried / considered:**
    - **What happened.** The notebook stopped at its Verify section: the rule's runs on the test
      window, its every-fill-at-the-close run, its sub-period 2 run and seven perturbation cells'
      rules, and the book-size-30 cell's control, each valued 42% to 47% of the window's trading
      days. The engine's log names the cause: a cash error of −$4,939.68 on 2009-05-18, a full
      re-equalisation on a rising day that overdrew the 2% reserve, after which the engine valued
      no further day while still returning a summary of the stub. No figure from the run is a
      result, and none is reported; a debugging run of the headline rule printed the stub's own
      summary, which describes 2002-07-30 to 2009-05-15 alone.
    - **Also found while debugging:** the Sharadar files carry no unadjusted volume, `m_volume`,
      and no file from either provider carries the unadjusted VWAP, `m_vwap`; the Curator's `c_*`
      columns, which the rule and the engine read, are populated.
    - **The options put to the owner:** a recorded revision of the reserve; closing Experiment 2
      as not priceable at its costs; or looking first at whether the engine could sell before it
      buys on a rebalance day.
- **Outcome / decision:** the owner chose the recorded revision: the cash reserve is 5%, the only
  change, written into `BLUEPRINT_2.md` and committed before the rule runs again. It counts as one
  more trial; the run at 2% is excluded by name in `FINDINGS_2.md` as a run that could not be
  priced.
- **Open threads:** whether 5% holds through the test window's sharpest days; the engine's order of
  sales and purchases on a rebalance day, which the library's maintainers can say.

<!-- example: end -->

<!-- example: begin -->

## 2026-09-24 — the run at 5%, the desk's move, the attribution, and the verdict

- **Idea / question:** the rule as the revised blueprint fixes it, at a 5% cash reserve and
  nothing else changed, run in full.
- **What we tried / considered:**
    - **The run at 5%**, from 09:38 to 10:15, after the revision's commit. Every engine run valued
      its window, and the notebook reached the end of its Verify section: 21 checks on the books
      and the weight file, 68 on 34 engine runs. Step 6 was skipped: the notebook found no index
      holdings, index returns or factor files where the desk had kept them.
    - **The desk's move.** The desk moved its files that day, into the Analytics Factory's folders,
      `Benchmark Portfolios` and `Factor Models`. `Data/hand_supplied.py` now reads both layouts,
      the new one first.
    - **The attribution re-run.** The whole notebook again, from 12:38 to 13:34, with the desk's
      folder set to the Analytics Factory. Every engine figure equals the run of 09:38; step 6 ran,
      over 2008-01-14 to 2016-12-30, bound by the factor files' first date; Verify raised nothing,
      21 checks on the books and 70 on 34 engine runs. `FINDINGS_2.md` is written from this run.
      Neither run started from a wiped working copy.
    - **A correction to the entry before.** The first run's Verify section named ten engine runs
      that stopped at the cash error: the rule, its every-fill-at-the-close run, its sub-period 2
      run, **six** perturbation cells' rules, not seven as that entry says, and the book-size-30
      cell's control.
- **Outcome / decision:** **claim 1 stays falsified, now on two windows, and nothing graduates.**
  On 2002-07-30 to 2016-12-30 the rule earns 4.23% a year at a Sharpe of 0.234, against its
  control's 5.87% and 0.256 and the index's 8.57% and 0.438. Prediction 1 fails, −0.0216 of Sharpe
  and −1.64 points a year against the control, and the verdict is the same with every fill at the
  close; prediction 2 fails; prediction 3 holds narrowly, a deepest fall of −53.32% against the
  index's −53.97% inside 2007 to 2009. The kill switch trips: the rule is ahead of its control on
  both measures in none of three sub-periods. Criterion 3 fails, one cell of ten. The factor model
  leaves the rule −7.93 idiosyncratic points and the control +30.24, so the cross's share is
  −38.17. On 2017 to 2026, the window the design was found on, the same rule trails its control by
  1.46 points a year. The trial count is forty-three.
- **Open threads:** the notebook's check for names held on their last priced day printed none,
  where the engine's log names six in the rule's run, all Sharadar names; a run from a wiped
  working copy; attribution before 2008; the third pass; the engine's order of sales and purchases
  on a rebalance day. What follows is the owner's decision.

<!-- example: end -->

<!-- example: begin -->

## 2026-09-24 — corrections to the entries above

- **Idea / question:** an independent check of this experiment's documents against the runs' logs
  and outputs found statements in the entries above that no output supports, and a figure in the
  blueprint that Experiment 1's journal had withdrawn.
- **What we tried / considered:** each point read again from the first run's log, the debugging
  run's log and the executed notebooks of the runs of 09:38 and 12:38, with the first run's unvalued
  days set on the test window's calendar. The entries above are left as they were written, and
  `BLUEPRINT_2.md` is not touched.
- **Outcome / decision:**
    - *The first run's truncated engine runs.* The entry on the first run says the cash error of
      2009-05-18 stopped each of the runs it names, and the entry before this one, correcting seven
      cells to six, keeps that cause. The Verify section named ten engine runs that stopped short,
      each with the days it left unvalued at the end, and they stopped on different days. Five were
      last valued on 2009-05-15 and so stopped at 2009-05-18: the rule, the rule with every fill at
      the close, sub-period 2's rule, and the band 10% and band 30% cells' rules. The book-size-30
      cell's control was last valued on 2008-09-16, the averages 40 and 160 cell's rule on
      2009-04-20, book size 10's on 2009-05-05, book size 15's on 2009-05-13 and the 5-days-late
      cell's on 2009-05-22. The cash error of −$4,939.68 is logged only by the debugging run of the
      headline rule; the first run's own log holds the Verify section's message and nothing else, so
      why the other nine stopped is not recorded. `BLUEPRINT_2.md`'s revision says every run that
      crossed that date stopped there; it stays as written, and the log does not show it.
    - *The blueprint's 92%.* `BLUEPRINT_2.md` sets its 95% coverage threshold "above the 92%
      Experiment 1's window opened on". That is the seed's share of the index's weight in 2017 that
      `../Experiment_1/JOURNAL_1.md` withdrew on 2026-09-24, because no run printed it. The
      threshold and its result do not depend on it: the lowest coverage inside the test was 99.71%,
      on 2003-09-02, and the test starts on 2002-07-30 either way.
    - *Coverage "on every date from 2001".* The entry before the rule says so; the run printed each
      year's lowest coverage for 2001 to 2017 only. The 99.59% holds on every date from 2001 to
      2017, and nothing printed says what it is after 2017.
- **Open threads:** none new. `FINDINGS_2.md` carries each correction.

<!-- example: end -->
