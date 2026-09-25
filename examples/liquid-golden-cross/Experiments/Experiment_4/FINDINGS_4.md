# Findings — Experiment 4

> **Latest valuable results only.** This file is rewritten when a result changes, not appended to —
> the running history is in [`JOURNAL_4.md`](JOURNAL_4.md), and the hypothesis this tested is in
> [`BLUEPRINT_4.md`](BLUEPRINT_4.md).
>
> **[`../../RESULTS.md`](../../RESULTS.md) is compiled from this file.** When a finding here
> changes, change it here first, then update the summary.

## Status

**Not yet run.** When it has: one line saying whether the rule beat the benchmark and its control
by what the blueprint required, and whether it is a candidate for the gate in
`Paper_Trading/BITACORA.md` — a success is necessary for graduation, not sufficient. Then **the
claim it moved**: the claim of `OBJECTIVE.md` the blueprint named, and the status it reached — or
why it reached none.

<!-- example: begin -->

**Experiment 4 ran end to end on 2026-09-25, from a wiped working copy, and it does not graduate.**
The rule is claim 5's second design: of the hundred most traded members of the index, the twenty
with the highest return over the twelve months before the latest one, re-struck on the first trading
day of each month — except in a month that opens after a negative two-year return of the index, when
the book holds the pool's twenty most traded. On its test window, 2002-07-30 to 2026-06-01, it earns
**11.61% a year at a Sharpe of 0.4779, against its control's 10.53% and 0.4694 and the index's
10.99% and 0.5682**. It leads its control by **1.08 points a year**, where prediction 1 asked for
0.5, and by **0.0084 of Sharpe**, where it asked for 0.03: **the kill switch trips on that one
margin**. Its other limbs are silent — the rule is ahead of its control on both Sharpe and CAGR in
two sub-periods of three, and ahead of the same ranking held in every month on both — and the
perturbation fails, five cells of twelve where the blueprint asked for ten. It is not a candidate
for the gate in `Paper_Trading/BITACORA.md`; the gate's rows are below anyway.

**The claim it moved: claim 5 of `OBJECTIVE.md`, momentum, stays falsified, now for two designs on
this window.** The blueprint fixed that status for a failed prediction 1 or a tripped kill switch.
Beside it, as the blueprint fixed: the rule's margin over its control in each sub-period, below; and
rows 31 to 38 of `RESULTS.md`, read before the blueprint, which found the signal below zero in bear
months and above it outside them on 2002 to 2016. **It is the closest any book here has come.** The
state does what the paper and the analyzer said: the rule beats the ranking held in every month by
1.26 points a year and 0.0364 of Sharpe, and over the 2009 rebound it gains 61.74% where that
ranking gains 27.23%. What it does not do is add enough Sharpe over the most traded twenty, at the
commission the blueprint fixed, to clear the bar every experiment here has been judged by.

**The success criteria `BLUEPRINT_4.md` set, each answered.**

| # | Criterion | State |
| --- | --- | --- |
| 1 | Prediction 1's margins over the control on the test window, net, at the headline cost row | **Not met.** CAGR +1.08 points, where +0.5 was required; Sharpe +0.0084, where +0.03 was required. Both are required |
| 2 | The kill switch is silent | **Not met.** Its first limb fires, the whole-window margins. The sub-period limb is silent, two of three, and so is the limb against the arm |
| 3 | The same verdict with every name filled at the close | **Met.** At the close the margins are +0.0034 and +0.97 points: not met either way |
| 4 | The rule beats the index on Sharpe | **Not met.** 0.4779 against 0.5682 |
| 5 | A run reproduced end to end from a wiped working copy, with the Sharadar names' Curator at its recorded commit | **Met, with the downloads kept.** The record is the run from a wiped working copy; the working copy printed every figure the same but one attribution line, caveat 5 |
| 6 | Trades on fewer days than it does not | **Met.** 288 rebalances in 5,998 trading days, and the invariant passed |
| 7 | Every prediction evaluated in this file | **Met.** Three rows below: two failed, and the third, a limb of the kill switch partly known in advance, was met |

**No rule, check or engine run of this experiment has read the months after 2026-06-01.** The
notebook cuts its panel and every price file the stale-bars check reads there.

### The gate, row by row

Every row is evidenced from this file. **Nothing graduates**, and no book of this experiment is
frozen.

| # | Criterion | Verdict | Evidence |
| --- | --- | --- | --- |
| 1 | Beats the benchmarks **and its own control** | **Fails** | CAGR 11.61% against the index's 10.99% and the control's 10.53%: ahead of both. Sharpe 0.4779 against the index's 0.5682 and the control's 0.4694: behind the index, and ahead of the control by 0.0084, short of the 0.03 the blueprint required. The verdict is the same with every name filled at the close |
| 2 | Idiosyncratic alpha in **both** layers | **Partly** | Over 2008-01-14 to 2026-06-01 the factor model leaves the rule 92.55 idiosyncratic points and its control 83.71: the conditioned ranking's share is +8.84, where Experiment 3's ranking's was −5.59; against the arm, the state's share is +13.49. The rule's momentum line is 52.02 against the control's 15.94. The first cut's alpha against the index is +125.59 points, of which selection +26.49 and interaction +100.32, per asset. The third pass has not been run, no random books were priced, and 2002 to 2007 are not attributed |
| 3 | Survives perturbation; trial count published | **Fails** | The rule is ahead of its control on both Sharpe and CAGR in 5 of 12 cells, where the blueprint asked for ten; every cell priced. The trial count is published: sixty-eight, with this experiment's 40 engine runs listed by role. The deflated figure was not computed |
| 4 | Costs and capacity modelled and stated | **Met, capacity as a participation bound** | Turnover, target to target: 3.06 times the book a year, and 25.3% one-way per rebalance on average, 77.7% on the eleven re-strikes where the state turns. Costs are charged on the unadjusted price at two rows, the blueprint's setting 0.1 and a realistic 0.005, with 5 basis points of slippage and a 10% reserve, and reported net: $882,137.50 of commission and $216,577.57 of slippage at the headline row. Capacity, from the book: at 1%, $6,933,709 for the worst trade, $29,839,031 at the first percentile of trades, $107,323,816 at the median; at 5%, $34,668,547, $149,195,153 and $536,619,080. It bounds participation and does not model market impact, and which trade is the worst was not traced |
| 5 | Explicit sign-off | **Not sought** | Criteria 1 and 3 block it, and the kill switch had already tripped |

**No decision of the owner's on what follows is recorded.** Nothing in this file recommends a
design.

<!-- example: end -->

## The predictions, evaluated

**Every prediction in the blueprint gets a row, including the ones that were wrong.** A falsified
prediction is worth more than a correct one: it says something about the strategy that nobody knew,
and it cost one run to find out.

| # | Prediction | Outcome | What it changed |
| --- | --- | --- | --- |
| 1 | as written in the blueprint | confirmed or falsified, with the number | what is now understood differently |

<!-- example: begin -->

**Every prediction in the blueprint gets a row, including the ones that were wrong.** All three are
read net, at the headline cost row, over the test window, 2002-07-30 to 2026-06-01.

| # | Prediction | Outcome | What it changed |
| --- | --- | --- | --- |
| 1 | The rule beats its control, the pool's twenty most traded members with a momentum value on the rule's own dates, by at least 0.03 of Sharpe and 0.5 points a year of CAGR | **Failed, on the Sharpe margin.** CAGR **+1.08 points**, clearing 0.5; Sharpe **+0.0084**, short of 0.03: 0.4779 and 11.61% against 0.4694 and 10.53%. The verdict is the same with every fill at the close, +0.0034 and +0.97. At the realistic cost row both margins clear, +0.0571 and +2.29 points | The state turned Experiment 3's shortfall of 0.22 points a year into a lead of 1.08, and the ranking's idiosyncratic share from −5.59 points to +8.84. The return it adds comes with more volatility than the control's, 24.29% against 22.43%, so the Sharpe margin stays small; the rule paid $882,137.50 of commission against the control's $320,285.50 |
| 2 | The rule beats the KN US Equity 600 on Sharpe over the test window | **Failed.** 0.4779 against the index's 0.5682; CAGR 11.61% against 10.99% | A lead, not a licensed prediction, as the blueprint wrote. Twenty names chosen on a year's return are more volatile than six hundred, 24.29% against 19.34%, and the index's Sharpe stays out of reach even where the rule's return passes it |
| 3 | The rule beats the diagnostic arm, momentum in every month, on both Sharpe and CAGR — a limb of the kill switch, partly known in advance | **Met.** Sharpe +0.0364 and CAGR +1.26 points, 0.4779 and 11.61% against 0.4414 and 10.34%. Over 2009-03-02 to 2009-12-31, all bear months, the rule gained 61.74% and the arm 27.23% | The state earns its place against its simpler baseline, as the house's bar asks. The 2009 rebound was known before the run; the rest of the window was not, and the state's +13.49 idiosyncratic points against the arm are the measure of what it adds over 2008 to 2026 |

One failed on a margin, one failed outright, and one was met. **The first taught the most.** The
design fixed what Experiment 3's run pointed at: the rule no longer loses the 2009 rebound, it leads
the control on return over the window, and its selection now adds idiosyncratic return. What remains
is that a monthly re-strike of twenty momentum names is a more volatile book than the twenty most
traded, and at the commission every experiment here has been judged at, the extra return does not
buy 0.03 of Sharpe.

### The kill switch

**It trips, on its first limb alone.** The blueprint fixed one condition for the whole experiment:
prediction 1's margins over the test window; the rule ahead of its control on both Sharpe and CAGR
in at least two of three sub-periods, each priced by the engine as a window of its own; and the rule
ahead of the diagnostic arm on both over the window.

| Sub-period | Trading days | Rebalances | Bear month starts | Sharpe, the rule | Sharpe, the control | CAGR, the rule | CAGR, the control | Ahead on both |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1, 2002-07-30 to 2008-12-31 | 1,619 | 78 | 19 | 0.001 | −0.046 | 0.02% | −1.14% | yes |
| 2, 2009-01-02 to 2016-12-30 | 2,014 | 96 | 21 | 0.498 | 0.642 | 10.25% | 12.54% | no |
| 3, 2017-01-03 to 2026-06-01 | 2,365 | 114 | 3 | 0.854 | 0.748 | 21.28% | 17.15% | yes |

**Two of three, and the arm beaten.** Sub-period 3 counted for the rule, as the blueprint expected;
sub-period 1 turned, the rule roughly flat where the control lost 1.14% a year; sub-period 2, which
opens with the 2009 rebound, stayed the control's. Only the whole-window Sharpe margin failed. The
changes that may not rescue it are the blueprint's, from the members and the exclusions to the
state, the stale-bars check, the commission setting 0.1, the 10% reserve, the sub-periods,
prediction 1's margins and the perturbation's twelve cells and its threshold of ten. None was moved
after the result.

<!-- example: end -->

## The book, priced by the engine

Record the date of the last full re-run from a wiped working copy, the engine version, and the
window. Then the book against every benchmark it reports against, and against the control its
blueprint names, on the rule's own rebalance dates: CAGR, volatility, Sharpe, Sortino, maximum
drawdown.

<!-- example: begin -->

**Run 2026-09-25, from 07:41 to 09:26, from a wiped working copy**: a clone of this repository at
the commit that holds the notebook, every output of the pipeline's analyzer and experiments wiped
and rebuilt, on the data stages the same clone rebuilt from the curator on the day before, with the
raw downloads Experiment 3's caveat 5 names kept. The working copy the rule was built in ran the
same notebook from 07:37 to 09:24 and printed every figure the same, but one line of the first cut,
caveat 5. KaxaNuk Backtest Engine 0.66.0 and Attribution Analysis 0.2.0; the FMP names from Data
Curator 0.50.0 and the Sharadar names from its `issues/31` branch at commit `8b54c2f`, built as
0.49.1. The notebook reached the end of its Verify section. The window asked of the engine is
**2002-07-30 to 2026-06-01**, 5,998 trading days, and every run valued at least 99% of its own
window's trading days. Costs are the blueprint's: the commission setting 0.1, 5 basis points of
slippage and a **10% cash reserve**, on $1,000,000. Results are net.

| Book | CAGR | Volatility | Sharpe | Max drawdown | Alpha | Commissions | Slippage | Rebalances |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **The rule** | **11.61%** | 24.29% | **0.4779** | −67.13% | 0.62% | $882,137.50 | $216,577.57 | 288 |
| The control, without the ranking | 10.53% | 22.43% | 0.4694 | −64.42% | −0.46% | $320,285.50 | $81,613.56 | 288 |
| The arm, momentum in every month | 10.34% | 23.43% | 0.4414 | −63.33% | −0.65% | $726,459.20 | $164,697.64 | 288 |
| The rule, realistic costs | 13.52% | 24.23% | 0.5578 | −66.43% | 2.53% | $57,381.68 | $306,749.44 | 288 |
| The control, realistic costs | 11.23% | 22.42% | 0.5007 | −63.58% | 0.23% | $17,699.65 | $92,591.37 | 288 |
| The KN600 index | 10.99% | 19.34% | 0.5682 | −55.37% | — | — | — | — |
| The null, the whole pool | 8.94% | 19.06% | 0.4692 | −59.44% | −2.05% | $268,797.80 | $55,641.53 | 288 |

The rule minus its control: **Sharpe +0.0084, CAGR +1.08 points**; minus the arm: **Sharpe +0.0364,
CAGR +1.26 points**. Beta to the index, from the engine's daily series: **the rule 1.097, the
control 1.115, the arm 1.023**. The notebook prints neither Sortino nor the information ratio; no
figure for either is quoted here. The control, the arm and the null traded on the rule's 288 dates
and on no other, 43 of them in a bear month, on each of which the rule held its control's book and
on each other the arm's, as the invariants check. The index row is the rule run's benchmark. The
null's weight file dropped `WCOEQ`, held with no price anywhere in the window, as in Experiment 3.

### The fill convention, checked

| Book, every fill at the close | CAGR | Volatility | Sharpe | Max drawdown | Commissions | Slippage |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| The rule | 11.57% | 24.30% | 0.4763 | −67.08% | $870,565.60 | $214,110.90 |
| The control | 10.61% | 22.43% | 0.4729 | −63.90% | $323,836.00 | $82,922.00 |

**The same verdict.** At the close the margins are +0.0034 of Sharpe and +0.97 points of CAGR,
against +0.0084 and +1.08 with the two conventions mixed: the Sharpe margin is short of 0.03 either
way.

### The realistic cost row

At the setting 0.005 the rule earns 13.52% at a Sharpe of 0.5578, and its control 11.23% at 0.5007:
**Sharpe +0.0571 and CAGR +2.29 points, both of prediction 1's margins cleared.** The rule's Sharpe
there is still below the index's 0.5682. Every verdict is read at the headline row, as the blueprint
fixed, and the commission setting is on its list of changes that may not rescue it. It is the second
experiment in a row whose verdict on prediction 1 turns on the cost row: Experiment 3's CAGR margin
was −0.22 points at 0.1 and +1.23 at 0.005.

### 2002 to 2016, described

| Book, 2002-07-30 to 2016-12-30 | CAGR | Volatility | Sharpe | Max drawdown | Alpha | Rebalances |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| The rule | 5.70% | 23.87% | 0.2390 | −67.13% | −2.87% | 174 |
| The control | 6.36% | 22.10% | 0.2877 | −64.42% | −2.22% | 174 |

**Description, never evidence.** The rule minus its control on these years: **Sharpe −0.0487, CAGR
−0.65 points**, against Experiment 3's −0.1237 and −2.84 on the same window. The state closes most
of that gap and not all of it.

<!-- example: end -->

## What the benchmark actually is, structurally

Rebalance frequency, turnover, holdings, concentration, invested share, and any structural tilt —
each with a reading of what a bad value would have meant.

<!-- example: begin -->

**The panel, the check and the state, section 1.** The panel read to 2026-06-01 holds 6,390 dates by
1,436 positions in the wiped copy and 1,437 in the working copy; the working copy excludes the
fifty-one names `JOURNAL_4.md` recorded before the rule, the wiped copy those and `MIC`, whose fresh
download it lacks. Coverage is 99.71% at the lowest, on 2003-09-02. The stale-bars check ends the
nine listings `JOURNAL_4.md` names, and no book is struck in one after its end; one file, `KN600`,
lacks the bar columns and is not checked. The state is bear on 43 of the rule's 288 entries: 19 in
sub-period 1, 21 in sub-period 2, 3 in sub-period 3.

**The books, sections 2 and 3.** Every invariant of section 2.1 passed, thirty-three in all: seven
on each of the rule, the control, the null and the arm; one on each of the rule and the control that
every name struck in had a momentum value; that the rule holds its control's book on every bear
rebalance and the arm's on every other; and that no book is struck in a name the stale-bars check
has ended. The rule's weight file holds 354 identifiers by 288 rebalances, every column summing to
one, with `SHY` at 0.000 on every date.

| Property | The rule | The control | The arm | What a bad value would have meant |
| --- | --- | --- | --- | --- |
| Rebalances | 288 in the window, 12.1 a year | the same 288 | the same 288 | A rule trading on most days would be a cost question, not an alpha one. The invariant passed |
| Mean one-way turnover per rebalance | 25.3%; 77.7% on the 11 re-strikes where the state turns, 23.3% on the others | 7.6% | 26.9% | A turn of the state swaps most of the book at once; the monthly re-strike swaps about five names |
| Annual turnover, target to target | 3.06 times the book | 0.91 | 3.25 | The engine's realised turnover was not read. The rule's is what its $882,137.50 of commission is charged on |
| Mean invested share | 100.0%, lowest 100.0% | 100.0% | 100.0% | `SHY` holds any slot no name fills, and none was |
| Mean holdings | 20.0 | 20.0 | 20.0 | Equal by construction |
| Mean weight in Sharadar names | 14.2% | 5.3% | 17.1% | The dead names fill at the close; the fill check prices what that does. The null held 14.5% |

**Capacity, criterion 4 of the gate**, measured as Experiment 1's was: each of the rule's trades set
against the name's 63-day average traded value on the day.

| Share of a day's traded value | Worst trade | 1st percentile of trades | Median trade |
| --- | ---: | ---: | ---: |
| 1% | $6,933,709 | $29,839,031 | $107,323,816 |
| 5% | $34,668,547 | $149,195,153 | $536,619,080 |

### Watched, but not predicted

- **The betas, side by side.** The rule 1.097, the control 1.115, the arm 1.023.
- **The momentum line and what is left.** 52.02 points to the rule, 15.94 to the control and 42.71
  to the arm, over 2008 to 2026; the idiosyncratic points, 92.55, 83.71 and 79.06. *Attribution*
  below.
- **Turnover.** 3.06 times the book a year and 25.3% per re-strike, against the control's 0.91 and
  7.6% and the arm's 3.25 and 26.9%; on the eleven re-strikes where the state turns, 77.7%.
- **The bear month starts in each sub-period:** 19, 21 and 3.
- **The weight in `SHY`.** None, for every book.
- **The share of each book's weight in Sharadar names**, from the engine's daily weights: the rule's
  mean 12.6%, highest 55.2%; the control's 4.8% and 22.9%; the arm's 15.1% and 55.0%.
- **The stale-bars check.** No book held a listing past the last distinct bar the check ends it at,
  which the invariants check; the engine carried `KKR`'s last price across interior gaps, 180 days
  in runs of at most 4, in the rule's and the arm's runs, and found no refusal anywhere.
- **The 2002-to-2016 window's margin**: −0.65 points a year and −0.0487 of Sharpe, above.
- **The null beside all three**: 8.94% at 0.4692, above.
- **Every name held on its last priced day.** The notebook's check printed none for any book: it
  reads the engine's daily weight on a name's last priced day, the day the engine sells it, so the
  weight it reads is already zero — caveat 6. The engine's log is the record: in the rule's run it
  sold twenty-three names at their last price, from `UCL1` on 2005-08-10 to `XLNX` on 2022-02-11; in
  the control's none; in the arm's thirty-one, and it ignored the arm's target of 0.05 in `ROH` on
  its last priced day, 2009-04-01.

<!-- example: end -->

## The trial count

How many variants were ranked to reach the book above, and every run excluded by name with its
reason. `RESULTS.md` compiles this: a reader cannot discount a best-of-N result without knowing N,
and the graduation sign-off says whether the deflated figure was also computed.

<!-- example: begin -->

### The perturbation, criterion 3

Twelve cells, fixed in the blueprint, one setting at a time around the rule, each priced beside its
own control, which takes the cell's pool, book size and delay and never the state, and trades on the
cell's own dates. Net, at the headline cost row, over the test window. **The rule itself** reads
Sharpe 0.478, +0.008 over its control and +1.078 points of CAGR, on 288 rebalances. Every cell
priced.

| Cell | Sharpe | Sharpe over control | CAGR over control, points | Rebalances |
| --- | ---: | ---: | ---: | ---: |
| State over 12 months | 0.477 | +0.008 | +1.271 | 288 |
| State over 36 months | 0.463 | −0.007 | +0.768 | 288 |
| Lookback 6 months, skipping 1 | 0.392 | −0.078 | −1.481 | 288 |
| Lookback 9 months, skipping 1 | 0.406 | −0.064 | −0.839 | 288 |
| 12 months, no skip | 0.521 | +0.052 | +2.026 | 288 |
| Pool 50 | 0.536 | +0.067 | +1.400 | 288 |
| Pool 150 | 0.462 | −0.008 | +1.145 | 288 |
| Pool 200 | 0.469 | −0.000 | +1.523 | 288 |
| Book size 10 | 0.390 | −0.133 | −2.048 | 288 |
| Book size 30 | 0.471 | +0.016 | +0.890 | 288 |
| Quarterly | 0.466 | +0.011 | +1.184 | 96 |
| Acted on 5 days late | 0.454 | −0.040 | +0.026 | 287 |

**Each curve's direction, as the blueprint asked:**

- **The state's window.** Twelve months reads as the rule's twenty-four, +0.008 and +1.271;
  thirty-six gives up the Sharpe margin, −0.007, and keeps a smaller CAGR margin, +0.768.
- **The lookback.** Rising with the lookback, as in Experiment 3: −0.078 and −1.481 at six months,
  −0.064 and −0.839 at nine, +0.008 and +1.078 at the rule's twelve less one, and +0.052 and +2.026
  at twelve with no skip.
- **The pool.** Best at fifty, +0.067 and +1.400; at one hundred and fifty and two hundred, which
  Experiment 3 could not price, the CAGR margin holds, +1.145 and +1.523, and the Sharpe margin
  falls to zero or just below.
- **The book size.** Ten names trail on both, −0.133 and −2.048; thirty lead on both, +0.016 and
  +0.890.
- **The frequency.** Quarterly leads on both, +0.011 and +1.184, on a third of the rebalances.
- **The delay.** Acting 5 days late takes the CAGR margin to zero, +0.026, and the Sharpe margin to
  −0.040.

**Criterion 3 is read as failed, on its own rule**: the rule is ahead of its control on both Sharpe
and CAGR in **5 of 12 cells** — twelve months of state, twelve months with no skip, the pool of
fifty, thirty names, and the quarterly re-strike — and the blueprint asked for ten. In nine of the
twelve the CAGR margin is positive; in five the Sharpe margin is. The best cell is never the answer:
picking one after the result is a new experiment, and one more trial.

### The count

**Sixty-eight trials, the count the blueprint fixed**: the fifty-four `RESULTS.md` published, then
this experiment's rule, the diagnostic arm, and the twelve cells. The owner's earlier test outside
this repository is counted as one, so the count is a lower bound.

**Forty engine runs in this experiment's notebook**, every one priced and valued on at least 99% of
its window's trading days. By role:

| Role | Engine runs | Counted as |
| --- | ---: | --- |
| The rule | 1 | a trial |
| The diagnostic arm, momentum in every month | 1 | a trial |
| The control | 1 | a diagnostic |
| The null, the whole pool | 1 | description, never evidence |
| 2002 to 2016: the rule and its control | 2 | description, never evidence |
| The rule and the control at realistic costs | 2 | diagnostics: the same books at another cost row |
| The rule and the control with every fill at the close | 2 | diagnostics: the fill convention |
| The sub-periods: the rule and its control in each of three | 6 | diagnostics: the kill switch |
| The perturbation: twelve cells and their twelve controls | 24 | twelve trials and twelve diagnostics |
| **All** | **40** | |

**The Verify section, section 8, raised nothing.** 41 checks on the books and the weight file: the
thirty-three invariants of section 2.1, and eight on the file read back from disk and the dates the
control, the arm and the null trade on. 82 on the runs: two window checks on each of the 40 engine
runs, and two on the attribution. **No variant was selected on its result.** Every book above was
fixed in `BLUEPRINT_4.md` or in the notebook before the run, and no earlier run of this notebook is
recorded. The deflated Sharpe was not computed.

<!-- example: end -->

## Attribution — is this the signal, or a factor exposure wearing its name?

Brinson-Fachler: allocation, selection, interaction. The factor model: factor against idiosyncratic.
State the window, which is bound by the supplied files' coverage and is usually shorter than the
backtest.

**What it settles**, and **what it does not** — naming the counterfactual book that would settle
what is left: the same holdings with the signal off, positions equalised, a random draw at the same
sizes, entry dates shifted.

<!-- example: begin -->

**Window: 2008-01-14 to 2026-06-01**, bound by the factor files' first date; the backtest runs from
2002-07-30, so sub-period 1 before 2008, with nineteen of its bear month starts, lies outside it.
The book is read daily as the engine held it, widened to the whole index at zero weight, with the
excluded names dropped from both. 1,350 of the 1,351 identifiers the books and the index name have a
price series here.

**First cut, Brinson-Fachler**, the rule against the index, summed daily over the window, in
percentage points: alpha **+125.59**, of which allocation **−1.21**, selection **+26.49** and
interaction **+100.32**, per asset: read it as "the weighting did it".

**Second layer, the factor model**, on the rule, its control and the arm, in percentage points
summed over the window:

| Source | The rule | The control | The arm |
| --- | ---: | ---: | ---: |
| Market | 89.90 | 90.67 | 89.53 |
| Beta | 9.99 | 14.52 | 16.17 |
| Momentum | 52.02 | 15.94 | 42.71 |
| Residual volatility | 3.89 | 5.46 | 3.14 |
| Size | −8.32 | −0.59 | −4.89 |
| Value | 4.75 | 3.01 | 3.16 |
| The eleven sector factors | 0.00 each | 0.00 each | 0.00 each |
| **All factors** | **152.23** | **129.01** | **149.82** |
| **Idiosyncratic** | **92.55** | **83.71** | **79.06** |
| **Excess return** | **244.78** | **212.73** | **228.88** |

**What it settles.**

- **The conditioned ranking adds idiosyncratic return.** The rule keeps 92.55 points the factor
  model cannot explain, its control 83.71: **the ranking's share is +8.84**, where Experiment 3's
  ranking, held in every month, took 5.59 away.
- **The state is what turned it.** Against the arm, which differs from the rule in the state alone,
  the rule keeps 13.49 more idiosyncratic points and 9.31 more momentum points, 52.02 against 42.71,
  and takes a smaller beta line, 9.99 against 16.17.
- **Most of the rule's edge over its control is still the factor.** Of the 32.05 points of excess
  return the rule earns over its control, 36.08 are the momentum line's; the other lines take back
  12.86, and the idiosyncratic line gives 8.84.

**What it does not settle.** The third pass, Brinson-Fachler on the residual returns, has not been
run. The attribution does not reach 2002 to 2007. The sector lines read 0.00 for every book. No
random books were priced, so there is no baseline for the rule's 92.55 points beyond its control's
and the arm's.

<!-- example: end -->

## What is open, ranked

The single highest-value run outstanding, and what it would settle.

<!-- example: begin -->

**None of these can turn the verdict**: the rule misses prediction 1's Sharpe margin over the window
and fails the perturbation. They bear on how it is read. What follows it is the owner's to decide.

1. **The cost row, measured.** The verdict on prediction 1 turns on it in two experiments in a row:
   here both margins clear at the setting 0.005, and neither setting was measured from an executable
   commission schedule for this book's trades. A later blueprint that fixes its cost row from one,
   before its run, would say which describes the book. Highest value.
2. **Paper trading as the unseen test.** The blueprint names it as the only test this design has not
   seen, and the gate does not open it: whether to track this rule on paper without graduation is
   the owner's to decide, never this file's.
3. **The check for names held on their last priced day.** It reads the weight on the day the engine
   sells, which is zero; it should read the weight on the day before. The engine's log names
   twenty-three in the rule's run.
4. **The market's variance, the paper's second state variable**, and a three-year state, each a
   later experiment with its own blueprint.
5. **The third pass, attribution before 2008, and random books**, as for every experiment.

<!-- example: end -->

## Caveats

| # | Caveat | Effect |
| --- | --- | --- |
| 1 | what a reader must know before quoting a number above | what it does to that number |

<!-- example: begin -->

| # | Caveat | Effect |
| --- | --- | --- |
| 1 | **The design was chosen after its weak spot was seen.** The state was chosen after Experiment 3's book lost the 2009 rebound, in months this state covers, and measured on the years it was tested on; the reserve and the stale-bars check after Experiment 3's four cells could not be priced | The rule's lead over the arm in 2009 was known before the run, and its lead in the rest of the window was not. A pass would have been weaker evidence than its margins; the trial count, sixty-eight, is published |
| 2 | **A rare state.** 43 of 288 entries, 40 of them in 2002–2003 and 2008–2010; 3 after 2010 | On 2017 to 2026 the rule is Experiment 3's almost month for month; what the state is worth rests on two episodes |
| 3 | **The dead names fill at the close**, and two Curator versions serve them. The rule held a mean of 12.6% of its weight in Sharadar names, up to 55.2%, the control 4.8%, up to 22.9% | The fill check prices both books with every name at the close: the margins move from +0.0084 and +1.08 to +0.0034 and +0.97, and the verdict does not change |
| 4 | **The stale-bars check uses hindsight.** It ends a listing on the evidence of rows up to the window's end, years later for `CSC`, and reads only a file's end | Nine listings are ended at their last distinct bar, and the engine refused no run, where in Experiment 3 two cells were refused over `VMW`. A listing with repeated bars inside its life is not caught |
| 5 | **The wiped copy kept its raw downloads**, as Experiment 3's did: the FMP files fresh through 2026-06-01, lacking `MIC`, and the Sharadar names re-curated from cached bulk tables | Every figure the two copies print is the same but the first cut's interaction, +100.32 in the wiped copy and +100.31 in the working copy, which drops `MIC` from the index there and not here |
| 6 | **Delisting exits use one day of hindsight, and the notebook's check reads the day of the sale.** The engine sold twenty-three of the rule's names at their last price; the check printed none | The engine's exit at the last price spares whichever book holds a failing name to the end, here the rule and the arm far more than the control. Whether each left the market by failure or by acquisition was not checked |
| 7 | **Costs are the blueprint's row**, the commission setting 0.1: $882,137.50 on the rule over the window, against the control's $320,285.50, with 5 basis points of slippage and a 10% cash reserve held by every book | Every verdict is read there. At the realistic row, 0.005, both of prediction 1's margins clear, +0.0571 and +2.29 points, and the rule's Sharpe, 0.5578, is still below the index's |
| 8 | **The attribution window starts on 2008-01-14** | 2002 to 2007, with nineteen of sub-period 1's bear month starts, are not attributed |
| 9 | **The desk's eleven sector factor lines read 0.00** | A sector tilt is not separated from the other lines |
| 10 | **Sixty-eight trials across four experiments**, on one universe whose years every experiment has read | The deflated Sharpe has never been computed |

<!-- example: end -->
