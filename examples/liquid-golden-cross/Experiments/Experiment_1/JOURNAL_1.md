# Journal — Experiment 1

> **Append-only, dated, oldest first.** Every iteration of this experiment, in the order it
> happened. Maintained by the AI as work proceeds.
>
> **Earlier entries are never edited.** The one exception is correcting an error, and the correction
> is written as a new entry saying what was wrong — not by rewriting the original.
>
> The hypothesis is in [`BLUEPRINT_1.md`](BLUEPRINT_1.md); what to try next is in
> [`BRAINSTORMING_1.md`](BRAINSTORMING_1.md); the results that survive are in
> [`FINDINGS_1.md`](FINDINGS_1.md).

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

## 2026-09-19 — repository instantiated from the template

- **Idea / question:** the first worked strategy, `liquid-momentum`, was judged too much for a
  beginner's first example, and it had stopped at step 1. Start `example` again from `main` with a
  simpler strategy and work it through every step, one commit at a time, so that the history itself
  is the walk-through.
- **What we tried / considered:** the idea, as it was first put: invest in the most traded US stocks
  with positive momentum, read from the 50-day simple moving average against the 200-day; hold the
  top 30; rebalance only when the top 30 differs from the current portfolio by 10%, to avoid
  rebalancing too often. The strategy is `liquid-golden-cross`: a golden cross is the 50-day average
  crossing above the 200-day, and the rule holds a stock while it stays above.
- **Outcome / decision:** `example` was reset to `main` at template 0.7.8. `SETUP.md` step 5 came
  first — the README, the status line in `AGENTS.md`, `uv.lock` — and then every file the steps
  fill, brought across with the previous strategy's lines deleted, so each one holds the template's
  description and nothing else. `apm.yml` keeps the template's name, because on `example` it mirrors
  `main`.
- **Open threads:** `OBJECTIVE.md` is not written, and the sentence above is not yet its claims. It
  leaves five things open for step 1 and the blueprint:
    - *most traded* — measured how, dollar volume or shares, over what window, and cut where;
    - *the top 30* — ranked by what: trading volume, or the strength of the trend;
    - the weights — equal, or something else;
    - *10% different* — 10% of what, names replaced or weight moved, and checked how often;
    - fewer than 30 eligible — hold cash, or hold fewer names.

## 2026-09-19 — step 1: the objective, first pass

- **Idea / question:** turn the idea as it was first put into claims before any paper is read, and
  settle the open questions that change what is claimed.
- **What we tried / considered:** two readings of *the top 30* — the 30 most traded among stocks in
  an uptrend, or the 30 strongest uptrends among the most traded — and whether a slot no stock
  qualifies for stays in cash or is spread over the rest. The researcher's home library was read as
  contrast and is cited nowhere here: it separates trend following, which is absolute, from
  momentum, which is relative; it holds no note on moving-average rules for single stocks; and it
  holds the theory of a no-trade band but no test of one on a rule like this.
- **Outcome / decision:** the 30 are the most traded among stocks in an uptrend, so the trend is a
  yes-or-no filter and trading volume the ranking. Equal weight, a thirtieth each, and a slot with no
  eligible stock stays in cash. *10% different* is the weight a rebalance to the new top 30 would
  trade — three names of thirty at equal weight, price drift included — checked every trading day.
  `OBJECTIVE.md` now has four claims: the signal, the sizing and the band untested, the volume
  ranking true by construction. Each claim's evidence is the question that would settle it, and ten
  sources are named as leads, at least one of them against each claim.
- **Open threads:** the reading for each claim's question, then the fine-tuning pass of
  `OBJECTIVE.md`, then the universe. Left for the data step: the window behind *most traded* —
  proposed, a quarter's average daily traded value — and the price the averages are taken on,
  proposed the adjusted close. Left for the blueprint: in a deep fall the 30 most traded stocks still
  in an uptrend can come from far down the volume ranking, and whether that needs a floor.

## 2026-09-19 — steps 2 and 3: the universe, the data, and what the analyzer found

- **Idea / question:** build the universe the claims need, the columns the rule reads, and measure
  the signal before any book exists.
- **What we tried / considered:**
    - *The universe.* The KN US Equity benchmark's own constituents, taken from the header of its
      daily holdings file: 788 identifiers, delisted names kept. 82 of them (10.4%) no longer trade.
    - *The provider.* Financial Modeling Prep. Yahoo was considered, because a free source would let
      anyone rerun the example — but Yahoo drops delisted companies, so a Yahoo run would quietly
      become a survivor list, which is the thing step 2 exists to prevent. A Yahoo variant on
      survivors alone, measured against this one, would price survivorship bias instead of suffering
      it; that is a later experiment.
    - *The windows.* The index's daily holdings begin 2017-01-03 and its returns in 2000, so
      point-in-time membership exists only from 2017. The long run therefore holds the membership
      list fixed, which is a survivorship caveat rather than a second result.
    - *The provider's row limit.* The first full download came back with every long-lived security
      starting on the same day, 5,000 rows each. That is a per-request cap, not the age of the
      companies: an earlier window returns the rest. The driver now pages and joins with a 150-day
      overlap, because a window's rolling columns are null in its own first rows and joining two
      windows end to end would put a hole in the middle of the series.
- **Outcome / decision:** a panel of 4,252,848 rows across 787 securities, 2001-01-02 to
  2026-06-01. 572 securities reach back to 2001; 265 have no prices when the long window opens in
  2002; 76 series end early and every one belongs to a security the provider also calls inactive,
  so no truncation is a silent gap. `MIC` has no file at all. **Four securities carry adjusted
  prices that multiply by more than six in a day** — `CIT`, `FMC`, `LCI` and `PARA`, the last going
  from 57.20 to 101,500 on 2021-02-12 — which is a bad print rather than a return, and which would
  have inflated a 200-day average for a year. They are a blocking row in the register and are
  excluded by name in the rule; the seed keeps all 788, so the universe still matches the index it
  came from.
- **What the analyzer measured, before any book:** the securities are not one trade — mean pairwise
  correlation 0.303. The trend signal's information coefficient inside the eligible pool is 0.0112
  at a month, 0.0027 at a quarter and −0.0060 at a year: noise beside the 0.02 to 0.03 a working
  signal shows. What it separates instead is volatility — 28.7% against 36.7% over the following
  month, on 208,111 observations, against a return difference of 1.20% versus 1.03%. **That is what
  LeBaron (1999) reported on the Dow, reproduced here on 787 US stocks over 25 years**, and it was
  predicted in that note before any of this was downloaded.
- **Two defects of ours, found and fixed:** `pct_change` was padding across gaps, so the first price
  after a halt became one enormous return and poisoned every statistic built on it; and the mean
  pairwise correlation was averaging over pairs that never traded on the same day. A third
  near-miss was not a defect: the per-date rank identity is off by more than 0.001 on 203 of 6,328
  dates, and on the worst of them exactly one security shares a rank, because a security that has
  not traded for a quarter has a traded value of exactly zero.
- **Open threads:** `BLUEPRINT_1.md` before the rule, with the prediction this measurement
  licenses — a defensive book rather than a high-returning one. The analyzer's table is a screen,
  not evidence. And the Yahoo appendix, which would put a number on survivorship bias.

## 2026-09-20 — steps 4 to 6: the book, the engine, and the decomposition

- **Idea / question:** run the rule the blueprint fixed, price it, and find out where the return
  came from.
- **What we tried / considered:** four variants, all specified before the engine ran — the rule, the
  rule at a realistic commission, the filter-off control, and the long window. The control is the
  one claim 1 is actually about: beating the index only says the book worked.
- **Outcome / decision:** the rule compounds at 17.85% against the index's 14.71% over 2017–2026,
  Sharpe 0.861 against 0.774, drawdown −30.5% against −33.8%. **The control earns more** — 18.62% —
  with a 9.3-point deeper drawdown, so the filter bought drawdown rather than return, exactly as an
  information coefficient of 0.0112 should produce. Over 24.7 years the same rule compounds at
  10.29% with a −60.7% drawdown. Attribution puts 71% of the excess return in factor exposure, more
  than half of the whole in market beta at a beta of 1.028, and leaves 45.5 points idiosyncratic.
- **Five things the run taught that no amount of care would have:**
    - *The engine's commission parameter is documented in cents and behaves like dollars.* At the
      frozen 0.1 it charges about $0.083 a share, twenty times a retail rate. The blueprint is not
      edited; the realistic figure is reported beside it and the defect is one to report upstream.
    - *A book whose weights sum to exactly one cannot pay commission.* Three runs died of it, each
      reporting success while valuing a stub — 2003 at a 0.5% reserve, 2009 at 1%, and day one of
      the point-in-time run. The window check caught all three; 2% is what the worst variant needed.
    - *A blocking row in the register applies to every stage.* `PARA`'s bad print was excluded from
      the rule but not from the benchmark, and it contributed 160 percentage points to the index's
      reconstructed return in a single day, which came back as the book's shortfall.
    - *The factor files' dates were strings where everything else used timestamps.* The factor
      attribution returned zero rows rather than an error.
    - *A renamed security must be written as the listing live on the date.* Writing both legs during
      the overlap put 24 rebalance dates above a weight of one.
- **What the predictions did:** four confirmed, one falsified, one split. The falsified one is the
  most useful: volatility was predicted below the index's from a per-security measurement, and
  thirty names are more volatile than six hundred whatever the filter does. Against the book it is
  actually a variant of, the filter removes 2.2 points of volatility.
- **Open threads:** equalise the two books and re-price them, which separates selection from sizing
  and settles who earned the idiosyncratic 45.5 points. The eleven sector factors read exactly zero
  and no sector claim stands until that is understood. The long window's −60.7% drawdown is
  undecomposed.

## 2026-09-20 — the counterfactuals: where the 45.5 idiosyncratic points actually come from

- **Idea / question:** `FINDINGS_1.md` reported 45.5 points of idiosyncratic return and could only
  infer where they came from. Six more books, each removing exactly one of the rule's choices,
  turn the inference into a measurement.
- **What we tried / considered:** the equalised control — the filter off, rebalanced on the
  filtered book's own 87 dates — because the plain control fires 11 times and therefore differs in
  two things, not one. Then five random thirty-name books drawn from the index's members on the
  same dates, which removes the liquidity ranking and keeps everything else. **Adding
  counterfactual arms does not change the rule**, so this stays inside Experiment 1 rather than
  opening a new one; the benchmark's own numbers are untouched, and `AGENTS.md` names these arms
  under *What attribution must report*.
- **The predictions were committed before the engine ran.** All four possible outcomes were written
  into the notebook cell and committed while the run was still going, so the diff shows the order —
  the same discipline as `BLUEPRINT_1.md` before the rule.
- **Outcome / decision:** the equalised control earns 18.97%, more than the plain control's 18.62%
  and more than the rule's 17.85%, so **the filter costs 1.12 points a year rather than 0.77** once
  the trading confound is removed. Idiosyncratic points: the rule 45.5, the equalised control 40.5,
  the plain control 32.1, and the random books −17.6 to 25.2 with a mean of **12.5**. That splits
  the 45.5 into roughly 12.5 of baseline, 28 of liquidity ranking and 5 of trend filter.
- **The prediction that failed is the one that mattered.** The random books were predicted to land
  near zero. They did not. A concentrated equally weighted book earns residual in this window
  whatever it holds, so the published 45.5 overstates genuine selection by about a quarter and the
  honest figure is nearer 33. Nothing in the factor model says so; only the random arm does. **This
  is the second time in this experiment that a portfolio-level claim was read off a measurement
  that could not support it** — the first was prediction 1's volatility.
- **Two defects found on the way:**
    - *The random draw crashed on day one.* The eligibility matrix is lagged, so the first date has
      an empty pool and a draw of thirty from nothing raises. The rule itself holds cash on that
      date; the random books now do the same, which is also the right economics.
    - *The attribution runs on the invested 98% of the book.* The engine's daily weights carry a
      `CASH_RESERVE` column with no price series, and the library silently prices only what it can
      name. It applies identically to every arm and it reproduces the published 45.52 exactly, so
      nothing moves — but it was never stated, and it is now caveat 7.
- **Everything published reproduced.** The notebook was re-run end to end and returned 17.85%,
  0.8612, −30.54% and 45.52 unchanged. Not from a wiped working copy, which is the stronger test.
- **Open threads:** more random draws, because five seeds leave the baseline uncertain across a
  43-point spread. Then the band as a curve — claim 4 has never been tested, and the equalised
  control is the first evidence bearing on it, since the same book at 87 rebalances beat itself at
  11 net of costs. That is a new experiment; the rule here froze when `FINDINGS_1.md` reported.

## 2026-09-20 — challenged: the run read back against the blueprint's own falsifiers

- **Idea / question:** the researcher's `challenge`, run from outside the experiment, asking one
  thing — did each verdict in `FINDINGS_1.md` follow from the falsifier `BLUEPRINT_1.md` fixed for
  it. Nothing was recomputed; every number below is quoted from the two files.
- **What we tried / considered:** each prediction against its written falsifier, the tally against
  its rows, the run against the frozen blueprint, the four success criteria one by one, the notes
  behind the citations, and whether every falsification reached `RESULTS.md`.
- **Outcome / decision:** predictions 2, 3 and 4 hold as written. Four things do not.
    - **Prediction 5 is falsified by its own falsifier and is recorded as *Split*.** The falsifier
      is "a momentum loading at or below zero, **or** a beta at or above one"; beta came back
      1.028, so a limb fired. The row's own prose already concedes it — "It does not inherit low
      beta" — so only the verdict word is wrong, and the verdict word is what gets counted later.
    - **Prediction 1's verdict answers a comparison the prediction did not make.** Its falsifier
      named the index alone, and 20.73% against 19.01% fires it. "Falsified against the index,
      confirmed against the control" is a falsification plus a new observation; the second half
      belongs on its own line.
    - **The tally counts row 1 twice.** "Four confirmed, one falsified, one split" against rows
      that read three confirmed, one falsified, two split.
    - **The long window moved and nothing records it.** The blueprint freezes 2002-01-02; every
      long-window figure runs from 2002-07-30. Caveat 3 says a smaller cash reserve truncates the
      long run, which is adjacent but does not state the deviation.
    - **Success criterion 1 is unmet while adoption is declared.** "Reproducible from a clean
      clone" against `RESULTS.md`'s "It has **not** been re-run from a wiped working copy".
      Criteria 2, 3 and 4 are met on the evidence; none is evaluated explicitly.
  Nothing here is corrected by this entry: `BLUEPRINT_1.md` does not change after its test, and
  `FINDINGS_1.md` belongs to the experiment. The wording is the experimenter's to fix or to leave.
- **Open threads:** prediction 1's falsification and prediction 5's beta limb are in neither *What
  is closed* nor *Known limitations* in `RESULTS.md`; the beta one is what tells the next reader
  this benchmark is a full-beta position. Prediction 6's second clause — that the cash is where the
  drawdown difference comes from — was never tested, and its 2008–09 evidence comes from the
  survivorship-affected long window while the drawdown it explains is short-window. For the next
  blueprint: prediction 6 cited "the rule itself", which is neither a note nor an analyzer section
  and should have been a counted lead.

## 2026-09-21 — the template's headings back outside the markers, and the run reproduced twice

- **Idea / question:** two things the template needed from this experiment's files, neither a change
  to the experiment. The blueprint and the findings kept ten of the template's headings inside the
  example markers, so the skill's references lost them when regenerated; and success criterion 1,
  reproducibility, had never been checked on the interpreter the template supports.
- **What we tried / considered:** splitting each block at the ten headings and putting the
  template's guidance back beneath each one, as *Key risks* already had it; and running the pipeline
  again on Python 3.13.15, first with the kernel named explicitly, then on the plain `python3`
  kernel the notebooks now declare, both times reusing the curator data already downloaded.
- **Outcome / decision:** the headings are outside the markers and the change only adds lines. The
  strategy's text inside the markers is identical, line for line, and stripping the fixed files
  reproduces the skill's references exactly. `BLUEPRINT_1.md` changed after its test in its template
  text only; the hypothesis is byte for byte what it was. Both runs reproduced every published
  figure exactly: the universe files, the 787 refinery files, the nine analyzer measurements, the
  eleven weight files, and every engine figure from the rule's 17.85% and 0.861 to the random books'
  −17.6 to 25.2.
- **Open threads:** criterion 1 asks for a run *from a clean clone*, and neither run was one: both
  reused the curator download, so the download itself has not been reproduced, and `RESULTS.md` is
  still right that the run has not been repeated from a wiped working copy. The findings' section on
  the counterfactuals has no counterpart in the template, so it stays inside the markers, and a new
  experiment's findings file is not prompted to write one.

## 2026-09-22 — a correction: the long window is 23.8 years

- **Idea / question:** the entry of 2026-09-20 on steps 4 to 6 gave the long window as 24.7 years,
  and `FINDINGS_1.md` with it. The window runs 2002-07-30 to 2026-06-01, which is 23.8 years, as
  `RESULTS.md` already says.
- **What we tried / considered:** nothing was re-run; the length is counted from the window's own
  dates.
- **Outcome / decision:** `FINDINGS_1.md` now says 23.8 years. The entry of 2026-09-20 stays as
  written; this entry is its correction. No figure the engine returned changes.
- **Open threads:** none.

## 2026-09-22 — recorded late: the findings answered the challenge of 2026-09-20

- **Idea / question:** the challenge entry above named what in `FINDINGS_1.md` did not hold and
  left the wording to the experimenter. The findings and `RESULTS.md` were corrected afterwards,
  and no entry said so; a correction is a new entry, so this is it.
- **What we tried / considered:** each point of that entry against the two files as they now read.
- **Outcome / decision:** prediction 5 is recorded as *Falsified*, and the tally reads three
  confirmed, two falsified, one split, with row 1 counted once, as falsified; row 1's verdict now
  names the index alone, and the control comparison moves to *What it changed*. Caveat 9 records
  the long window's start at 2002-07-30. The status names criterion 1 as outstanding, and each of
  the four success criteria has a row. `RESULTS.md` closes predictions 1 and 5 under *What is
  closed*. Every figure the challenge quoted is unchanged.
- **Open threads:** prediction 6's second clause — that the cash is where the drawdown difference
  comes from — is still untested, and its 2008–09 evidence still comes from the long window, which
  is survivorship-affected.

## 2026-09-22 — criterion 1: the pipeline re-run from a wiped working copy, on a fresh download

- **Idea / question:** success criterion 1 of `BLUEPRINT_1.md` — reproducible from a clean clone,
  through the pipeline, with no manual step — had never been tested from a wiped copy: both earlier
  re-runs reused the curator's download. A copy made by `init-example` into an empty folder, with
  nothing but the hand-supplied index and factor files added, is that test.
- **What we tried / considered:** the whole pipeline in the template's order on 2026-09-22 —
  `Data/curator.py` against FMP, `Universe/universe.ipynb`, `Data/refinery.py`,
  `Data/analyzer.ipynb`, `experiment_1.ipynb` — with Backtest Engine 0.66.0, the version the
  published run used, and Attribution Analysis 0.2.0, the notebooks executed headless and their
  outputs written outside the repository. The index and factor files came from the desk's own
  folder under other names and one other header: `KN_US_Equity_Benchmark_Holdings.csv` and
  `_Returns.csv` for the two the code reads as `KN_US_Equity_Benchmark.csv` and
  `KN_US_Equity_Returns.csv`, the returns file headed `m_date` where the curator parses
  `date_column`, and the factor files capitalised where the attribution module wants them lower
  case with the four reserved series prefixed `f_`. Renamed on copying; `SETUP.md` now says so. The
  download stalled twice on a hung request after a DNS failure and was restarted; it skips complete
  files, so nothing was fetched twice.
- **Outcome / decision:** the pipeline runs end to end from a wiped copy with no manual step beyond
  the hand-supplied files, every conclusion holds, and the figures reproduce to the data rather than
  to the digit. The download came back 789 files, `MIC` the one name with no data, as published; the
  universe stage repeated its counts exactly — 265 late starts, 76 early ends, the four impossible
  prints, 787 signallable and the book fillable from 2001-10-22 — with one provider-side drift: the
  profile flag marks 79 names delisted where the blueprint recorded 82. The refined panel is ten rows
  short of the published 4,252,848, and the analyzer's nine measurements came back identical but for
  the 63-day coefficient, 0.0026 against 0.0027. The engine's filter-off control and the index
  reproduced to every published decimal and the long window to within 0.01 of a point; the rule
  itself fired 86 rebalances against 87 and compounded at 17.89% against 17.85%, Sharpe 0.863
  against 0.861, drawdown −30.55% against −30.54%. Against the plain control the filter costs 0.73
  points a year against the published 0.77; against the equalised control, 18.96% this run, 1.07
  against 1.12. The attribution's factor lines moved by hundredths — momentum 12.69 against 12.75,
  idiosyncratic 45.44 against 45.52 — and the eleven sector factors read exactly 0.00 again. The
  random arms moved most, as five draws from a pool that shifted by a few names would: −14.0 to 29.5
  points, mean 11.1, against −17.6 to 25.2, mean 12.5; the rule still sits above the range's top.
  Criterion 1 is recorded as met to the data in `FINDINGS_1.md`, with the re-run's figures beside
  the published ones; **no published figure is changed**, because the numbers moved for a known
  reason — a fresh pull rebases the adjusted columns, known limitation 5 of `RESULTS.md` — and a
  committed result is not edited to agree with a new run.
- **Open threads:** which security's ten rows moved, and which rebalance trigger with them, was not
  traced; a diff of the two downloads would say. The 82-against-79 delisted count is the provider's
  flag, not the price files, and only the caveat table cites it. The random arm's sensitivity to the
  pool is one more reason for the first open lead, far more draws.

## 2026-09-23 — the template's new blueprint sections, left unfilled here

- **Idea / question:** the template's blueprint gained three sections after this one was written —
  the claim an experiment moves, the control named in its rules, and one condition that would
  falsify the whole experiment with the changes that may not rescue it. The findings now name the
  claim they moved; `RESULTS.md` gains a column for it, and one for the share of dates on which a
  coefficient had the expected sign; and every notebook ends in a Verify section.
- **What we tried / considered:** filling the three sections of `BLUEPRINT_1.md` from what the run
  showed, which would be a hypothesis written after its test.
- **Outcome / decision:** each new section carries the template's text and, inside the markers, a
  note that it was not written on 2026-09-19 and where the answer lives instead. The change only
  adds lines: the hypothesis inside the markers is what it was, and only the blockquote at the top,
  which is template text, changed. `FINDINGS_1.md`'s status names claim 1, the signal, moved to
  falsified, as `OBJECTIVE.md` already records. The sign share was not measured on 2026-09-19, and
  `RESULTS.md` says so rather than supplying one. No figure changes.
- **Open threads:** the next run of the analyzer fills the sign column. The next run of the
  experiment is the first to reach its Verify section, and what it prints is recorded then.

<!-- example: end -->

<!-- example: begin -->

## 2026-09-23 — the owner rewrites Experiment 1

- **Idea / question:** the owner decided to rewrite Experiment 1 around his own tested idea — the
  twenty most traded names above the cross, sold the day after it breaks — and to bring it to paper
  trading if it passes the gate. The template freezes a reported Experiment 1; this is the recorded
  exception its `AGENTS.md` now allows.
- **What we tried / considered:** the first design's `BLUEPRINT_1.md` says a rebalance fires when
  the move "would trade at least 10% of the book, with price drift counted". The code it ran,
  `select_rebalance_dates`, compares the day's selected set with the day before's, ignores drift,
  and counts a swapped name twice — out and in — so one swap in thirty is 6.7% and never fires, and
  two are 13.3% and do. The published numbers came from the code, so the code is what the first
  design was; the blueprint was not edited. The gap is the mechanism behind the delay measured in
  `BRAINSTORMING_1.md` on this date.
- **Outcome / decision:** the first design stays at tag `v0.15.0` of the KaxaNuk Researcher and as a
  row of `RESULTS.md`; its runs count in the trials. `BLUEPRINT_1.md` is replaced by the second
  design's, committed on its own before the rule. The index's files are now read in place from the
  desk's folder by `Data/hand_supplied.py`, and the Curator can refresh through a later date for
  paper trading; the experiment's window is unchanged, and everything after 2026-06-01 is held out.
- **Open threads:** the rule, the run, the findings and the gate follow the blueprint's commit.

<!-- example: end -->

<!-- example: begin -->

## 2026-09-24 — the second design, run: it fails its kill switch

- **Idea / question:** run Experiment 1's second design end to end, as `BLUEPRINT_1.md` fixed it on
  2026-09-23, and read it against its predictions, its kill switch and the gate.
- **What we tried / considered:**
    - *The refresh.* The Curator's download was refreshed through 2026-09-23, and the universe and
      the refinery were re-run on it before the experiment. The experiment reads the panel to
      2026-06-01 and no further: 6,390 dates by 772 positions, with the index's membership known
      from 2000-01-03 to 2026-08-14. A refresh rebases every adjusted column, so this design and
      the first sit on two downloads.
    - *The aborted run.* The first attempt stopped at the rule's engine run: the engine refused a
      weight column whose gross exposure was 1.000002, because rounding a fully invested
      twenty-name book to six decimals pushed it past one. `write_weight_file` in
      `Experiments/backtest_engine.py` now rounds every weight down, and the remainder goes to
      cash. The attempt produced no figure; `RESULTS.md` excludes it by name.
    - *The capacity cell.* Added to section 3 after the blueprint's commit and before the run. It
      measures construction, each trade against the name's 63-day average traded value, not a
      figure the blueprint predicted, and it answers criterion 4 of the gate, capacity, which the
      first design never modelled.
    - *The seed's coverage.* By the desk's holdings, the 788 identifiers of the seed cover about 92%
      of the index's weight in 2017 and 97.5% in 2025; the rest of the index was never selectable.
      The desk's eleven sector factor files are empty, so the sector factors read zero, as in the
      first design.
- **Outcome / decision:** the run of 2026-09-23 reached the end of its Verify section: 14 checks on
  the book and its weight file, and 92 checks on 45 engine runs.
    - *Against its control.* The rule compounds at 17.87% with a Sharpe of 0.806, against the
      index's 14.63% and 0.770. Its control, the same names without the cross, earns 18.73% at
      0.7748: the rule is 0.031 ahead on Sharpe and 0.86 points a year behind on CAGR, so
      prediction 1 fails. Its beta is 1.067 against the control's 1.238, which the blueprint reads
      as timing.
    - *The kill switch trips.* The rule is ahead of its control on both measures only in
      2020–2022, one sub-period of three. That holds prediction 3 and fires the kill switch.
    - *The arm.* The diagnostic arm reproduced the first design's delay, a median of 28 days held
      after a break, and earned 19.52% at 0.8773: 1.65 points a year more than the rule. That fails
      prediction 2 the other way, and rules out exit speed as the reason the cross loses.
    - *The perturbation.* 12 of 15 cells keep the sign of the rule's Sharpe margin, so criterion 3
      reads as passed on its own rule. The trial count stays at the blueprint's thirty-one.
    - *Attribution.* Idiosyncratic points: the rule 36.19, the control 40.99, the arm 50.02, and
      five random books −11.78 to 35.31, mean 22.4.
    - *The claims.* Claim 1 stays falsified, with exit speed ruled out as the reason; claim 4 moves
      to measured. `FINDINGS_1.md` is rewritten for the second design, with the first design's
      headline figures kept as the superseded row, and `RESULTS.md`, `OBJECTIVE.md` and
      `Paper_Trading/BITACORA.md` follow it.
    - **The owner's decision, 2026-09-24.** The rule failed its kill switch, and the diagnostic arm
      did better than the fast exit. He chose to confirm the arm's design on years it was not
      found on, 2002 to 2016, as Experiment 2, with the seed widened to every name the index held
      since 2000. It goes to paper trading only if it passes its own gate. Nothing is frozen, and
      `Paper_Trading_1/` stays the contract.
- **Open threads:** Experiment 2's blueprint, before its rule. A run of this design from a wiped
  working copy, which its success criteria ask for, is not recorded. The third attribution pass has
  not been run. Sector factor files with data. Far more random books.

<!-- example: end -->

<!-- example: begin -->

## 2026-09-24 — corrections to the entry above, and the data step since

- **Idea / question:** an independent check of the second design's documents against the executed
  notebooks of 2026-09-23 found figures in the entry above that no run printed or that it misread,
  and a change to the data step that no journal recorded.
- **What we tried / considered:** each point read again from the executed experiment and universe
  notebooks and the refinery's log of that run, and the entry above left as it was written.
- **Outcome / decision:**
    - *The seed's coverage.* The entry above says the seed covers about 92% of the index's weight
      in 2017 and 97.5% in 2025. No run recorded here printed either figure, and both are
      withdrawn. The universe run of 2026-09-23 printed the seed's share of the index's members,
      not of its weight: 39.8% on 2000-01-03, and no date through 2026-08-14 on which it held 99%
      of them.
    - *The universe and the refinery, re-run on 2026-09-23.* The universe notebook found 788
      identifiers in the seed, 79 flagged delisted, 266 late starts and 76 early ends, 787 that can
      ever be signalled, and the index's holdings from 2000-01-03 to 2026-08-14, 571 to 600 members
      a date. The refinery wrote 788 files, a panel of 4,308,857 rows.
    - *Sharpe ratios at one precision.* The entry above quotes the rule and the index to three
      decimals and the control to four. Section 4's table gives the rule 0.8057, the control
      0.7748, the diagnostic arm 0.8773 and the index 0.7699.
    - *The random books.* All five engine summaries were printed: CAGR 6.88%, 8.75%, 8.51%, 8.95%
      and 1.82%, Sharpe 0.344, 0.461, 0.440, 0.455 and 0.091, for seeds 11 to 55. They draw on the
      first trading day of each month from 2017-01-03, which is not one of the rule's trade dates,
      and the lagged pool is empty that day, so each holds only cash until 2017-02-01. Every one
      valued a stale `VMW` price, and four of them a stale `SRCL` one.
    - *`TWTR`.* It was sold at its last price in 17 of the 45 runs, not in the rule's alone, and
      both delay cells targeted it after that price; the engine left those weights in cash.
    - *Claim 4.* *Measured* is the status `BLUEPRINT_1.md` fixed for the arm, reached on an
      engine-priced book at a 15% band, where the claim names 10% and the vocabulary of
      `OBJECTIVE.md` names the analyzer. `OBJECTIVE.md` now says both.
    - *`Paper_Trading_1/`.* The entry above says it stays the contract. `paper_trading_1.py` now
      carries the second design's rule, in the form a frozen book takes. Nothing froze it: no
      `FREEZE.json` exists, its bands are not registered in `Paper_Trading/BITACORA.md`, and it
      has never run.
    - *Experiment 2's window.* The entry above names it 2002 to 2016. Its blueprint fixes the start
      by a coverage rule, so it is the years before 2017 that rule allows, from 2002-07-30 at the
      earliest, to 2016-12-30.
    - *Experiment 2's blueprint.* Written on 2026-09-24. It goes in a commit of its own, with its
      brainstorming, before any rule code, and never in this experiment's results commit: that is
      what the open thread above asks.
    - *Two printed labels, corrected after the run.* Section 2's rule cell printed "114 of them
      first days of a month", a count of the first trading days of a month in the window,
      2017-01-03 among them, on which the rule does not trade. Section 5's first cut printed that
      the active return falls into allocation and interaction, where the run puts 0.11 points into
      allocation, 12.26 into selection and 39.78 into interaction. Both now print what they
      measure, and no figure changes.
    - *The data step.* After this design ran, `Data/curator.py` gained a second provider,
      Sharadar, for the names FMP does not carry, keyed by `KNDC_API_KEY_SHARADAR`, through the
      Data Curator's provider on the library's issues/31 branch until it is released. Sharadar
      publishes no VWAP, so for its names the split-adjusted close stands in for the split-adjusted
      VWAP: the fill price is the day's close and the traded value the close times the volume. No
      figure in `FINDINGS_1.md` comes from it: the run came first, on a seed of 788 identifiers.
      It is for Experiment 2, whose seed is to widen to every name the index held since 2000, as
      `../Experiment_2/BRAINSTORMING_2.md` plans.
- **Open threads:** the seed's share of the index's weight, from a cell that prints it, before any
  document quotes one. A run of this design from a wiped working copy, before its results are
  committed.

<!-- example: end -->

<!-- example: begin -->

## 2026-09-24 — the second design reproduced from a wiped working copy

- **Idea / question:** the second design's success criteria ask that it reproduce from a wiped
  working copy, and `AGENTS.md` commits a result only after such a run. The run of 2026-09-23 was
  made in the working copy the design was written in, on a download refreshed in place: not that
  test.
- **What we tried / considered:**
    - *The copy.* A fresh clone of that working copy, on its 788-name seed. The download ran on the
      commit that holds the design's code, the later stages on a later commit that sorts the slot
      book by date; `Data/curator.py` is the same in both. The environment was the one the run of
      2026-09-23 used: Backtest Engine 0.66.0 and Attribution Analysis 0.2.0.
    - *The download.* `Data/curator.py` against FMP from 07:48 to 10:30 on 2026-09-24: 789 files
      through 2026-06-01, `MIC` the one name with no data, and the pass that pages back for earlier
      history finished on all 789.
    - *The desk's move.* The desk moved its files that day, to the Analytics Factory's
      `Benchmark Portfolios/` and `Factor Models/`. The curator looked for the index in the old
      folder and did not stage it, and the universe stage, run next, stopped. The clone took
      `Data/hand_supplied.py`, and nothing else, from a later commit that reads both layouts; the
      curator ran again, skipped the 789 files it had and staged the index, and the universe, the
      refinery, the analyzer and the experiment ran, the notebooks headless, the experiment from
      10:47 to 12:38.
- **Outcome / decision:** every notebook reached the end of its Verify section: 7 checks in the
  universe, 8 in the analyzer, and in the experiment 14 on the book and 92 on 45 engine runs.
    - *To the digit.* Every engine figure: the rule's 17.87% and 0.8057, the control's 18.73% and
      0.7748, the arm's 19.52% and 0.8773, the rule at realistic costs, the index's 14.63% and
      0.7699, the three sub-periods, the fifteen cells and their controls, and the five random
      books. The Brinson-Fachler cut and every factor line of every arm. The book's 311 trade
      dates, its weight file of 99 identifiers, the nine invariants, the holdings, the broken
      name-days and the sector drift. The engine's warnings too: `TWTR` sold at its last price in
      17 runs, the delay books' weights after it, `IPG`, and the stale `SRCL` and `VMW` prices in
      the random books.
    - *Not to the digit.* The notebook's own sum of unpriced weight read 0.01 more for random
      seeds 11, 22, 33 and 55: 39.53, 39.48, 39.35 and 40.05 against 39.52, 39.47, 39.34 and
      40.04. And the panel holds 771 positions against 772: the provider returned nothing for
      `MIC` through 2026-06-01, and the refinery read 787 securities, 4,252,838 rows, where the
      download refreshed through 2026-09-23 gave it 788 and 4,308,857.
    - *The construction figures, corrected.* Exits 290, where the run of 2026-09-23 printed 462;
      entries 310, not 482; mean one-way turnover per trade date 0.060, not 0.088; annual turnover
      1.99 times the book, not 2.9. Capacity at 1% of a day's traded value: the worst trade
      $91,546,647, the first percentile $146,012,883, the median $16,231,104,636, not $2,018,972,
      $123,231,452 and $14,574,799,654; at 5%, $457,733,236, $730,064,416 and $81,155,523,178, not
      $10,094,858, $616,157,261 and $72,873,998,268.
    - *Why.* `portfolio_construction.build_slot_book` builds its frame with pandas from each trade
      date's targets, and pandas assembled the rows in the order the names first appeared, not in
      date order. Section 3 takes each trade as the change from the row before, so exits, entries,
      turnover and capacity compared dates that were not neighbours. The first daily dry run of the
      paper-trading machinery found it, and the function now sorts the rows by date. The engine
      read each trade date's weights by its date, so no engine figure moved; the figures read from
      the book laid on the window's calendar did not move either.
    - *`FINDINGS_1.md`.* Success criterion 3 is shown. The construction and capacity figures are
      the reproduction's, and so is the random books' unpriced weight; the open lead for a run from
      a wiped working copy is closed. The verdict does not change: the rule fails its kill switch
      and does not graduate.
- **Open threads:** which trade is the worst, for capacity, is still not traced, nor the 0.01 of
  unpriced weight. The paper-trading machinery was tested on this design, frozen as a candidate in
  that working copy and never committed, and those runs priced days after 2026-06-01, which the
  blueprint holds out; no figure from them is in `FINDINGS_1.md`.

<!-- example: end -->

<!-- example: begin -->

## 2026-09-24 — a second check of the second design's documents

- **Idea / question:** a second independent check of `FINDINGS_1.md` and `RESULTS.md` against the
  reproduction's outputs, logs and engine reports found statements that no output supports, a cause
  the evidence rules out, and the reproduction described more simply than it ran.
- **What we tried / considered:** each point read again from the reproduction's executed notebooks
  and logs, the engine's report for the rule, the weight files and the run's environment. The
  entries above are left as they were written.
- **Outcome / decision:**
    - *The reproduction, as it ran.* The entry above describes it rightly, and the findings now do
      too: the download ran with the clone at the working copy's commit `50ebdad`, which holds the
      design's code; the universe stage then stopped, once, on the desk's move; and the later stages
      ran at `45a690f`, which sorts the slot book, with `Data/hand_supplied.py` from `d7d1816`,
      after the curator ran again to stage the index. That is a manual step, which the blueprint's
      success criteria do not allow for, and the findings say so beside *Shown*.
    - *The index's row.* The findings named the refresh of the panel as a possible reason the index
      reads 14.63% and 0.7699 here against 14.71% and 0.774 at `v0.15.0`. It is not one: the curator
      stages the index from the desk's own daily returns, and the reproduction, on a download never
      refreshed, returned the same row. The candidates left, untraced, are a different first valued
      day and a change in the desk's index files, whose holdings began in 2017 at `v0.15.0` and
      begin on 2000-01-03 in both runs of this design.
    - *Sortino.* The findings said the run did not measure it. The engine's report carries it for
      every run; the notebook does not print it, and no Sortino figure is quoted.
    - *Turnover.* The findings called the engine's realised turnover lower than the 1.99 times the
      book, target to target. No output gives a realised turnover, and the claim is withdrawn.
    - *The reserve and the capital.* The 2% cash reserve and the $1,000,000 are the notebook's
      settings, not the blueprint's, which fixes the commission, the slippage and `SHY` for cash.
    - *Unprinted, and now sourced.* The first column of the arm's and the random books' weight
      files, 2017-01-03, holds only `SHY`, the cash proxy, and the random books first hold stocks on
      2017-02-01: the weight files show both, and no cell prints either. The arm's 41 rebalances are
      the 41 dates of its weight file, that first column among them. The library versions, Backtest
      Engine 0.66.0 and Attribution Analysis 0.2.0, are those installed on 2026-09-22 in the
      environment both runs used; no cell prints them.
- **Open threads:** a line in the notebook that prints the library versions and each random book's
  first invested date, so the next run records them.

<!-- example: end -->
