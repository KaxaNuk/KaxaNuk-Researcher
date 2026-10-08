<!-- example: begin -->

# Golden Flow

**Own the KN US Equity Core stocks the market is trading most, while their trend is up, in
proportion to what they trade** — none above a fifth of the book, none too small to matter.

> **Status, as copied on 2026-10-07: Experiment 1 ran in sample and passed criteria 1 to 4 of its
> gate; its book was frozen for paper trading on 2026-10-06 and is kept here as a record.**
> Net of costs, 2015-01-02 to 2026-06-01: 20.33% a year at a Sharpe of 0.842, against 19.73% and
> 0.763 without the golden cross and 13.05% and 0.713 for the KN US Equity Core. Nine tenths of the
> excess is factor exposure, and the control won 2023 to 2026.
> Replace this line as the strategy moves, and the banner at the top of `AGENTS.md` with it.

This is the worked example of the KaxaNuk Strategy Template, the one `init-example` copies.
It is for reading and running, never for building on.
A strategy of your own starts from `init-strategy`.

Built on the [KaxaNuk Strategy Template](https://github.com/KaxaNuk/KaxaNuk-Researcher/blob/main/templates/strategy/README.md):
eight steps as a folder structure, whose README says what each folder is for.

## How to read it

| Read | For |
| --- | --- |
| [`OBJECTIVE.md`](OBJECTIVE.md) | the idea and its three claims |
| [`RESULTS.md`](RESULTS.md) | *The project in three sentences*, then *The uncomfortable one* |
| [`Experiments/Experiment_1/BLUEPRINT_1.md`](Experiments/Experiment_1/BLUEPRINT_1.md) | the hypothesis, fixed before the run |
| [`Experiments/Experiment_1/FINDINGS_1.md`](Experiments/Experiment_1/FINDINGS_1.md) | what the run found |
| [`Paper_Trading/BITACORA.md`](Paper_Trading/BITACORA.md) | the gate, and the owner's sign-off |

[`JOURNAL_1.md`](Experiments/Experiment_1/JOURNAL_1.md) is the full story. Start with its entries
of 2026-10-06: the owner's decisions, the critic, and the third and fourth runs. In the other
documents, Golden Flow's own text follows the template guidance it answers.

**A key to older text.** Versions such as 0.13.0 and 0.14.0 named in these files are Golden Flow's
own earlier versions, on another index, and are not in this copy. "The desk" is KaxaNuk's Analytics
Factory. "The worked example" in text dated before 2026-10-07 is the package's earlier one.

## The rule, in one table

| Decision | Rule | Where it is named |
| --- | --- | --- |
| Universe | a member of the KN US Equity Core at the prior close: about 600 US stocks a day, from KaxaNuk's Analytics Factory | the seed, `Universe/Investable_Universe.csv`, read by `Data/hand_supplied.py` |
| Eligibility | the golden cross at the prior close: the 50-day average of the adjusted close above the 200-day | `r_trend_50_200 > 0`, from `Data/refinery.py` |
| Ranking and sizing | by 63-day average traded value, weighted in proportion; no weight above 20%, none below 1% | `r_traded_value_sma_63d`, from `Data/refinery.py` |
| Rebalancing | only on the days the held set changes | `portfolio_construction.rebalance_dates_on_change` |
| Exits | a name whose prices are about to stop is sold the day before, at t−1 | `portfolio_construction.exit_before_price_stops` |
| Cash | when fewer than five names are eligible, what the 20% cap cannot place is held in `BIL` | `backtest_engine.CASH_IDENTIFIER` |
| Benchmarks | the KN US Equity Core first, every alpha measured against it; then `SPY` | `KN_US_Equity_Core`, the engine's identifier for the index |
| Window | from the later of 2015-01-02 and the first day priced members hold 90% of the index's weight, to 2026-06-01 | `Universe/universe.ipynb`, before any rule exists |

Each row is the owner's decision. Most were taken on 2026-10-05, before any stage ran, and are
quoted in `JOURNAL_1.md`; rebalancing and cash are in the plan the owner approved that day, as
`BLUEPRINT_1.md` says; the exit came on 2026-10-06, after the cycle's first run.

## How Golden Flow uses the Lab and the Analytics Factory

| Step | Lab library or Factory file | What Golden Flow does | Skill for your own strategy |
| --- | --- | --- | --- |
| 1. Bibliotheca | — | the idea in the owner's words, three claims, and the notes that argue with them | `read`, `objective` |
| 2. Universe | the KN US Equity Core's daily holdings, from the Analytics Factory | the committed seed lists every member listing, 888 of its 896 with an FMP symbol; `Universe/universe.ipynb` fixes the window's first day | `universe-point-in-time` |
| 3. Data | **Data Curator**, open source; **Data Refinery** and **Data Analyzer**, coming | the Curator downloads FMP prices; until the other two ship, `Data/refinery.py` builds the two features and `Data/analyzer.ipynb` screens them | `data-curator-custom-calculations`, `data-analyzer-runs` |
| 4. Portfolio | **Portfolio Construction**, on request: not installed | the strategy's own `bounded_book` sizes the book; `weigh` shows where the library's call goes | `portfolio-construction-runs` |
| 5. Backtest | **Backtest Engine**, licensed | prices the book, its control and the other books it is compared with, net of costs, against the KN US Equity Core and `SPY` | `backtest-engine-runs` |
| 6. Attribution | **Attribution Analysis**, licensed; the Core's holdings and returns and the KN US Equity Factor Model, from the Analytics Factory | Brinson-Fachler, then the factor model, then Brinson-Fachler on what the factors leave | `attribution-analysis-runs`, `alpha-decomposition` |
| 7. Paper trading | the Data Curator, the Backtest Engine and the Factory's files, when a book runs | the book was frozen on 2026-10-06 and is kept here as a record, not run | `paper-trading-gate` |
| 8. Production | — | nothing here deploys | — |

`experiment-lifecycle` holds the documents around the steps: the blueprint, the journal and the
findings. When a library ships, the example moves to it in a new version.

> A licence for the Backtest Engine or Attribution Analysis, or access to Portfolio Construction,
> is KaxaNuk's to give: write to `lab@kaxanuk.mx`, saying which library and what it is for —
> <https://www.kaxanuk.mx/lab> shows the Lab.

**The Analytics Factory** — KaxaNuk's benchmark portfolios and factor models, which a strategy may
read as its universe, its benchmark and attribution's inputs: <https://www.kaxanuk.mx/analytics>;
ask `lab@kaxanuk.mx` for them. A strategy reads them in place from the folder its
`KN_ANALYTICS_PATH` names, or from copies dropped into `Data/Curator/Benchmarks/` and
`Data/Curator/Factors/`, as its `SETUP.md` says.

## Run it

**Before you run**, as [`SETUP.md`](SETUP.md) sets out:

- **An FMP key.** FMP is this experiment's provider, and its symbols are the seed's main
  identifier. A later experiment may use Sharadar, LSEG or another provider, with the main
  identifier KaxaNuk supplies for it.
- **The Analytics Factory's KN US Equity Core holdings and returns**, without which only the
  download runs, and **its KN US Equity Factor Model**, for step 6.
- **The Backtest Engine and Attribution Analysis licences**, for steps 5 and 6. Without them the
  experiment writes the book's weights and skips the rest.

From the repository root, each command reading what the one before it wrote:

```bash
uv run python Data/curator.py --end-date 2026-10-05
uv run python Data/curator.py --end-date 2026-10-05
uv run jupyter nbconvert --to notebook --execute --output-dir ../golden-flow-runs Universe/universe.ipynb
uv run python Data/refinery.py
uv run jupyter nbconvert --to notebook --execute --output-dir ../golden-flow-runs Data/analyzer.ipynb
uv run jupyter nbconvert --to notebook --execute --output-dir ../golden-flow-runs Experiments/Experiment_1/experiment_1.ipynb
```

- **The curator runs twice.** The second pass asks again for every name still without a file, so a
  name FMP refused for a rate limit or a timeout is not booked as one it does not carry.
- **The notebooks write their executed copies to `../golden-flow-runs`**, so the tracked notebooks
  stay stripped. Each ends in a Verify section that raises.
- **`Universe/seed.py` is not part of the run.** The seed is committed; the script shows how it was
  built, and needs the index's master of listings, which `lab@kaxanuk.mx` can be asked for.
- **`Paper_Trading_1` is a record** of the book frozen on 2026-10-06, not run from this copy.
  `promote.py 1` refuses, and `daily_update.py` stops with `unfrozen-input`, for the reasons
  [`Paper_Trading/BITACORA.md`](Paper_Trading/BITACORA.md) gives.

## What a correct run shows

These are the record run's figures, of 2026-10-06, from a wiped working copy. A fresh download
rebases the adjusted columns, so a run lands near these, not on them.

| Stage | A correct run shows | Recorded in |
| --- | --- | --- |
| The index's holdings | 1,399 listings, 2000-01-03 to 2026-08-14 | `JOURNAL_1.md` |
| `Data/curator.py` | on the record's seed: 892 names asked, 809 downloaded, 83 that FMP does not carry | `JOURNAL_1.md`, `CHANGELOG.md` |
| `Universe/universe.ipynb` | `CY` and `NBL` without a symbol, their FMP prices contradicting their membership | `JOURNAL_1.md`, `CHANGELOG.md` |
| `Universe/universe.ipynb` | the window opening on 2015-01-02, when priced members held 92.97% of the index's weight | `RESULTS.md` |
| `Universe/universe.ipynb` | `MNKKQ`, `NE`, `PCP` and `RAI` excluded by name, as blocking rows of `Universe/Data_Issues.csv` | `JOURNAL_1.md`, `BITACORA.md` |
| `Data/refinery.py` | 803 securities refined | `JOURNAL_1.md`, `RESULTS.md` |
| `experiment_1.ipynb` | a median of 37 names a day, re-struck on 48.1% of trading days | `RESULTS.md`, `FINDINGS_1.md` |
| `git status` | the seed unchanged; new only `uv.lock`, which `uv sync` writes | `SETUP.md` |

The record's seed still held `CY` and `NBL` when the curator ran, and the universe notebook dropped
them. The committed seed keeps them as rows with no FMP symbol, so a copy does not ask for them, and
the notebook rewrites the seed only when it drops a name.

## Words used here

- **Control**: the same rule with one ingredient off, here the golden cross, on the rule's dates.
- **Factor exposure**: return the factor model explains, such as the market, size and momentum.
- **Idiosyncratic**: the return left once factor exposure is taken out.
- **Brinson-Fachler**: splits the excess return into weighting (allocation) and picking (selection).
- **Kill switch**: the result on paper days that retires the book instead of tuning it.
- **In sample**: measured on the history the rule was chosen on; only days after the freeze are not.
- **Criteria 1-5**: the graduation gate, in `BITACORA.md`; the fifth is the owner's signature.
- **Information coefficient**: the rank correlation of a feature with the returns that follow it.
- **t−1**: the trading day before day t; every signal is read at its close.
- **Benchmark book**: the template's name for Experiment 1's book; later experiments must beat it.
- **Benchmark index**: the KN US Equity Core, which every alpha here is measured against.

<!-- example: end -->
