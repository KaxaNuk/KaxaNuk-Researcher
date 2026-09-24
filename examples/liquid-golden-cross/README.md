<!-- example: begin -->

# Liquid Golden-Cross

Invest in the most traded US stocks in an uptrend, meaning the 50-day simple moving
average is above the 200-day, hold the top 30, and rebalance only when that top 30 differs from the
current portfolio by 10%, to avoid rebalancing too often.

> **Status: steps 1 to 6 run end to end on Experiment 1's two designs, and step 7's gate evaluated
> against each; claim 1 is falsified.** Experiment 1's second design, the twenty most traded names
> above their cross, sold the day after it breaks, beats the index on Sharpe, 0.806 against 0.770,
> earns 0.86 points a year less than the same names without the cross and **fails its kill switch**;
> reproduced from a wiped working copy on 2026-09-24, it returned every engine figure to the digit.
> Its diagnostic arm, the first design's band at twenty names, earned 1.65 points a year more than
> it. Experiment 2, that arm's design on years before 2017, is open: its blueprint is committed
> before its rule, and none of its results is reported. Every number is in
> [`RESULTS.md`](RESULTS.md). **Nothing has graduated, no book is on paper, and nothing here is out
> of sample.**
> Replace this line as the strategy moves, and the banner at the top of `AGENTS.md` with it.

This is the worked example of the KaxaNuk Strategy Template: one strategy worked through the
process, for reading and running, which `init-example` copies. A strategy of your own starts from
`init-strategy`, never from here.

Built on the [KaxaNuk Strategy Template](https://github.com/KaxaNuk/KaxaNuk-Researcher/blob/main/templates/strategy/README.md):
eight steps as a folder structure. Its README says what each folder is for, where each
kind of logic goes and, under *Starting your own strategy*, the order to work in; this one does not
repeat it. **Start at** [`OBJECTIVE.md`](OBJECTIVE.md), the idea and its claims as they were
written before any paper was read, then [`RESULTS.md`](RESULTS.md) for what the claims survived.

| Read | For |
| --- | --- |
| [`OBJECTIVE.md`](OBJECTIVE.md) | the idea, and the status of each claim inside it |
| [`RESULTS.md`](RESULTS.md) | every number this repository has measured, and what it cost |
| [`AGENTS.md`](AGENTS.md) | how work is done here, and the bar a result has to clear |
| [`SETUP.md`](SETUP.md) | how this repository is set up on a new machine |

## What a correct run shows

For a copy made by `init-example` and run in the template's order, with the hand-supplied index and
factor files in place; without them, `SETUP.md` says where each stage stops. Every figure below is
one this repository recorded, on the seed of 788 identifiers. The data stages' rows are from the
runs of 2026-09-19 to 2026-09-22, on a download that ended 2026-06-01, with the re-run from a wiped
working copy's own figures in brackets where they moved; the universe's and the refinery's rows add
their re-run of 2026-09-23, on the refreshed download the experiment first read, and each row names
what the reproduction of 2026-09-24 printed, on a fresh download through 2026-06-01. The
experiment's rows are from Experiment 1's second design, run on 2026-09-23 and reproduced on
2026-09-24, every engine figure to the digit; the first design's figures are at tag `v0.15.0`.
Experiment 2 is open and has no row. A fresh download rebases the adjusted columns, so a run of your
own lands near these figures rather than on them. Clock times were recorded only on 2026-09-24: the
reproduction's FMP download of 789 files from 07:48 to 10:30 and Experiment 1's notebook from 10:47
to 12:38.

| Stage | A correct run shows | Recorded in |
| --- | --- | --- |
| `Data/curator.py` | 789 files, with `MIC` the one identifier that has no data, both times | `JOURNAL_1.md`, 2026-09-22 and 2026-09-24 |
| `Universe/universe.ipynb` | 788 identifiers in the seed; in the register, `MIC` missing, the four impossible prints `CIT`, `FMC`, `LCI` and `PARA`, 265 late starts and 76 early ends; 787 securities that can ever be signalled, and the book fillable from 2001-10-22; the index's holdings from 2017-01-03. The provider's delisted flag drifts: 82 names (79). Re-run on the refresh of 2026-09-23, with the index's files read from the desk's folder: 266 late starts, 79 flagged delisted, and the index's holdings from 2000-01-03 to 2026-08-14. The reproduction of 2026-09-24: 265 late starts, 79 flagged delisted, the same holdings, and 39.8% of the index's members in the seed on the first date | `JOURNAL_1.md`, `FINDINGS_1.md` |
| `Data/refinery.py` | 787 files, a panel of 4,252,848 rows (ten fewer) from 2001-01-02 to 2026-06-01; re-run on the refresh of 2026-09-23, 788 files and 4,308,857 rows; the reproduction of 2026-09-24, 787 files and 4,252,838 rows | `RESULTS.md`, `JOURNAL_1.md` |
| `Data/analyzer.ipynb` | the same panel, 787 securities; mean pairwise correlation 0.303; the rank identity off by more than 0.001 on 203 of 6,328 dates; in the eligible pool, coefficients of 0.0112, 0.0027 (0.0026) and −0.0060 at 21, 63 and 252 days, and an IR of 0.038 at 21 days; forward 21-day volatility of 28.7% with the 50-day average above the 200-day and 36.7% below, on 208,111 observations, the sum of the two counts the notebook prints. The reproduction of 2026-09-24 printed the same figures, the counts as 137,504 observations above and 70,607 below, with 0.0026 at 63 days, on a panel it read as 6,390 dates by 771 securities | `RESULTS.md`, `JOURNAL_1.md` |
| `experiment_1.ipynb`, sections 0 to 3 | the panel read to 2026-06-01, 6,390 dates by 771 positions (772 on the download refreshed through 2026-09-23), with the index's membership known from 2000-01-03 to 2026-08-14; the rule's 311 trade dates, from 2017-01-04, and the window's 114 first trading days of a month; the control's 114, all of them the rule's; the diagnostic arm's 41 rebalances, holding a broken name a median of 28 days; the nine invariants passing; 290 exits, 310 entries, one round trip within five days, mean holdings 20.0; a weight file of 99 identifiers by 311 trade dates. The run of 2026-09-23 printed 462 exits and 482 entries, read from rows out of date order | `FINDINGS_1.md` |
| sections 4 to 6, with the licensed engines | the rule at 17.87% a year and a Sharpe of 0.8057, the control at 18.73% and 0.7748, the diagnostic arm at 19.52% and 0.8773, the index at 14.63% and 0.7699; the rule ahead of its control in one sub-period of three, so the kill switch trips; 12 of 15 perturbation cells keeping the sign of the Sharpe margin; a Brinson-Fachler alpha of 52.14 points; idiosyncratic points of 36.19 for the rule, 40.99 for the control and 50.02 for the arm, and −11.78 to 35.31 for five random books | `FINDINGS_1.md` |
| section 8, Verify | 14 checks on the book and its weight file, and 92 on the runs: 90 window checks on 45 engine runs and 2 on the attribution | `FINDINGS_1.md` |

**Each notebook ends in a Verify section**, which raises when what its stage wrote is wrong, so a
run that reaches the last cell has passed it. Experiment 1's Verify printed its row on 2026-09-23
and again on 2026-09-24, when the reproduction's universe ran 7 checks and its analyzer 8. What the
other notebooks' Verify sections printed before 2026-09-24 is not recorded here.

<!-- example: end -->
