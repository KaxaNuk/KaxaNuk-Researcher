<!-- example: begin -->

# Liquid Golden-Cross

Invest in the most traded US stocks in an uptrend, meaning the 50-day simple moving
average is above the 200-day, hold the top 30, and rebalance only when that top 30 differs from the
current portfolio by 10%, to avoid rebalancing too often.

> **Status: steps 1 to 6 run end to end, reproduced from a wiped working copy on 2026-09-22, and
> step 7's gate evaluated against the result.** The rule
> beats the index by 3.1 points a year and loses to its own control by 1.1; of its 45.5
> idiosyncratic points, about 5 belong to the signal it is named after. It is **not a defensive
> book** — beta 1.028, and more volatile than the index — and what it buys is a drawdown 9.3 points
> shallower than the same thirty names unfiltered. Every number is in [`RESULTS.md`](RESULTS.md).
> **It does not pass the gate, no paper trading has run, and nothing here is out of sample.**
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
one this repository recorded, from the runs of 2026-09-19 and 2026-09-20 and the re-run from a wiped
working copy on 2026-09-22. A fresh download rebases the adjusted columns, so a run of your own
lands near these figures rather than on them; the re-run's own figures are in brackets where they
moved. How long each stage takes was never recorded, so nothing here says.

| Stage | A correct run shows | Recorded in |
| --- | --- | --- |
| `Data/curator.py` | 789 files, with `MIC` the one identifier that has no data | `JOURNAL_1.md`, 2026-09-22 |
| `Universe/universe.ipynb` | 788 identifiers in the seed; in the register, `MIC` missing, the four impossible prints `CIT`, `FMC`, `LCI` and `PARA`, 265 late starts and 76 early ends; 787 securities that can ever be signalled, and the book fillable from 2001-10-22; the index's holdings from 2017-01-03. The provider's delisted flag drifts: 82 names (79) | `JOURNAL_1.md`, `BLUEPRINT_1.md` |
| `Data/refinery.py` | 787 files, a panel of 4,252,848 rows (ten fewer) from 2001-01-02 to 2026-06-01 | `RESULTS.md`, `JOURNAL_1.md` |
| `Data/analyzer.ipynb` | the same panel, 787 securities; mean pairwise correlation 0.303; the rank identity off by more than 0.001 on 203 of 6,328 dates; in the eligible pool, coefficients of 0.0112, 0.0027 (0.0026) and −0.0060 at 21, 63 and 252 days, and an IR of 0.038 at 21 days; forward 21-day volatility of 28.7% with the 50-day average above the 200-day and 36.7% below, on 208,111 observations | `RESULTS.md`, `JOURNAL_1.md` |
| `experiment_1.ipynb`, sections 0 to 3 | 87 rebalances (86) in the point-in-time window, 9.2 a year, 17.8% one-way turnover each, mean holdings 30.0 | `FINDINGS_1.md` |
| sections 4 to 6, with the licensed engines | the rule at 17.85% (17.89%) a year and a Sharpe of 0.861 (0.863), the index at 14.71% and 0.774; the plain control's 11 rebalances; the filter at −0.77 points a year against the plain control (−0.73) and −1.12 against the equalised one (−1.07); 45.52 idiosyncratic points (45.44); the five random books from −17.63 to 25.17 points (−13.98 to 29.45) | `FINDINGS_1.md` |

**Each notebook ends in a Verify section**, which raises when what its stage wrote is wrong, so a
run that reaches the last cell has passed it. Verify came after these runs, and nothing records
what it printed on them.

<!-- example: end -->
