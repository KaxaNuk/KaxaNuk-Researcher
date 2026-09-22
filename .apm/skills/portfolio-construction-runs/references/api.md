# Portfolio Construction — the public surface

Taken from the library's README and CHANGELOG at 1.28.0, on 2026-09-17, and from 2.0.0's changelog
where marked — never from its code. What neither document states is left out: read them before
calling anything not listed here, and settle a doubt by a run. Where this file and the library
disagree, the library wins; tell `lab@kaxanuk.mx`.

Calls are written here as the README writes them, by keyword.

## Imports

The README imports these names from these modules:

| From | Names |
| --- | --- |
| `kaxanuk.portfolio_construction.entities` | `UniverseSnapshot`, `AllocatedUniverse`, `Weights`, `Signal`, `TimeSignal`, `Classification`, `ThresholdSpec`, `Mandate`, `Bounds`, `ConstraintLayer`, `BenchmarkSpec`, `Scenario` |
| `kaxanuk.portfolio_construction.selection` | `LiquidityFilter`, `BinaryFilter`, `CompositeUniverseFilter`, `MembershipFilter`, `UniverseCreator`, `SelectionInterface` |
| `kaxanuk.portfolio_construction.sizing` | `build_allocator`, `describe`, `SizingInterface`, `KNIndexAllocator`, `RiskParityAllocator`, `RiskParityConfig`, `MaxDiversificationAllocator`, `MaxDiversificationConfig`, `MeanVarianceAllocator`, `MeanVarianceConfig`, `BlackLittermanAllocator`, `BlackLittermanConfig`, `AbsoluteView`, `RelativeView`, `BasketView`, `ConstrainedMeanVarianceAllocator`, `ConstrainedMeanVarianceConfig`, `CVaRAllocator`, `CVaRConfig` |
| `kaxanuk.portfolio_construction.timing` | `CalendarRebalancer`, `FixedDateRebalancer`, `TimeSignalRebalancer` |
| `kaxanuk.portfolio_construction.pipeline` | `run_pipeline` |
| `kaxanuk.portfolio_construction.enums` | `MissingDataPolicy`, `ComparisonOp`, `RebalanceFrequency`, `CovarianceMethod`, `OptimizationObjective`, `TimingMode`, `BenchmarkKind`, `LimitBasis` |
| `kaxanuk.portfolio_construction.helpers` | `PanelHelper`, `CrossSectionalHelper`, `PortfolioDiagnosticsHelper`, `FeasibilityHelper`, `FrontierHelper`, `ResamplingHelper`, `ScenarioHelper`, `ActiveHelper`, `DataQualityHelper` |
| `kaxanuk.portfolio_construction.helpers.rolling_helper` | `RollingHelper` |
| `kaxanuk.portfolio_construction.output_handlers` | `PdfReportOutput`, `PortfolioReport` |
| `kaxanuk.portfolio_construction.output_handlers.excel_output_handler` | `ExcelOutputHandler` |
| `kaxanuk.portfolio_construction.config_handlers.excel_configurator` | `ExcelConfigurator` |
| `kaxanuk.portfolio_construction.input_handlers.parquet_input` | `ParquetInput` |
| `kaxanuk.portfolio_construction.market_data_pipeline_services.market_data_service` | `MarketDataProcessingService` |
| `kaxanuk.portfolio_construction.builders.universe_builder` | `UniverseBuilder` |

*Since 2.0.0* the changelog adds `services.license_validator`: `validate_license()`,
`reset_validation_state()`, `ValidationResult`, the licence errors and `PRODUCT`, a wrapper over
`kaxanuk-license-client`.

Named by the README or the changelog with no import shown — rely on one only once the README, the
changelog or a run shows how it is imported:

- **Entities.** `BinaryMatrix`, which the README counts among the entities; `MarketDataPanel`
  (1.0.0) and `Configuration` (1.21.0), which the changelog calls entities.
- **Selection.** `ColumnMembershipFilter`, which the README uses; `UniverseMembership`, what
  `UniverseCreator.build_membership` returns (1.3.0).
- **Sizing.** The registry, `ALLOCATOR_REQUIREMENTS`, with `requirements_for`, in
  `sizing.requirements` (1.19.0). `EqualWeightAllocator` and `InverseVolatilityAllocator` (1.25.0);
  `HRPAllocator`, which the sizing package exports (1.1.0), with `HRPConfig` (1.23.0);
  `HERCAllocator` and `NCOAllocator` (1.13.0); `CDaRAllocator` (1.18.0) with `CDaRConfig`;
  `FeatureWeightingAllocator`, `FeatureWeightingAllocatorConfig` and `KNIndexAllocatorConfig`. At
  1.21.0 the sizing configs moved into the entities, and the `sizing` package re-exports them.
- **Pipeline.** `PipelineTrace` (0.4.0), what `result.trace` holds.
- **Enums.** `WeightingMethod`, moved to `enums/` (1.21.0); `StandardField`, exported from `enums`
  (1.0.0); `ExposureMeasure`, which the README uses (1.22.0).
- **Helpers.** `ThresholdHelper` (0.2.0) and `CovarianceHelper` (0.8.0).
- **Input and output.** `CsvInput`, beside `ParquetInput` (0.10.0); the Excel and CSV output
  handlers (0.1.0), of which the README imports the Excel one.

The changelog names these errors at 1.28.0: `AllocationError`; `ConfigurationError`, with
`AllocatorConfigurationError`, `MandateError` and `ViewError` under it (1.21.0) and
`BenchmarkError` (1.25.0); `FilterError` (1.4.0); `PipelineError` (0.4.0); `PortfolioEntityError`
(0.9.0). *Since 2.0.0*, `kaxanuk.portfolio_construction.exceptions` holds `LicenseError`, with
`LicenseNotFoundError`, `LicenseValidationError`, `LicenseServerError` and
`LicenseConfigurationError` under it, all under `PortfolioConstructionError`, so
`except PortfolioConstructionError` catches them; each is also the licence client's matching error,
so `kaxanuk.license_client.LicenseError` catches them as well.

## Sizing: the registry

`build_allocator(name=..., returns=...)` builds any of the fourteen methods by its registry name,
checked against the registry before construction: a typo lists every valid name, a returns-based
method built without `returns` names the need, and a snapshot-only method handed a history refuses
it (README). A config of the wrong type names both classes (1.23.0), and since 1.28.0 `prices=` is
refused for every method. `describe(name)` renders a method's card — what it needs, honours and
assumes — and `requirements_for(name)` looks up its registry entry, whose `history_input` says
which history it takes (1.19.0, 1.28.0).

| Name | Config | History | Reads from the snapshot | Extra | Bounds | Shorts |
| --- | --- | --- | --- | --- | --- | --- |
| `equal_weight` | not stated | none: snapshot-only | not stated | none | none | long-only |
| `feature_weighting` | `FeatureWeightingAllocatorConfig`; `allow_shorts`, False by default | not stated | a number per security, the conviction | none | not stated | flag, `allow_shorts` |
| `kn_index` | `KNIndexAllocatorConfig` | not stated | market cap and rolling traded-value windows | none | not stated | not stated |
| `inverse_volatility` | not stated | returns | not stated | none | none | long-only |
| `risk_parity` | `RiskParityConfig(budgets=...)`; equal risk contribution without budgets | returns | not stated | none | not stated | long-only by construction |
| `max_diversification` | `MaxDiversificationConfig` | returns | not stated | none | not stated | not stated |
| `mean_variance` | `MeanVarianceConfig(objective=...)`, `MIN_VARIANCE` or `MAX_SHARPE` | returns | `expected_return_column`, set with `MAX_SHARPE` in the README | none | clip | may short; flag, `long_only` |
| `black_litterman` | `BlackLittermanConfig(market_cap_column=..., views=...)`; with no views, the market book | returns | market cap | none | clip | not stated |
| `hrp` | `HRPConfig` | returns | not stated | `clustering` | not stated | not stated |
| `herc` | not stated | returns | not stated | `clustering` | not stated | long-only by construction |
| `nco` | not stated | returns | not stated | `clustering` | clip | flag, `long_only` |
| `constrained_mean_variance` | `ConstrainedMeanVarianceConfig(objective=..., mandate=...)` | returns | not stated | `solver` | hard | the mandate |
| `cvar` | `CVaRConfig(alpha=..., mandate=...)` | returns | tickers only | `solver` | hard | the mandate |
| `cdar` | `CDaRConfig` | returns | not stated | `solver` | hard | the mandate |

*Bounds*, as the README defines them: **hard**, the mandate is a constraint of the solve; **clip**,
shorts clipped and the book renormalised, a documented heuristic rather than an optimum; **none**,
the method imposes no bounds, and group caps come afterwards with `Weights.cap_groups`.

- **Every limit is annual since 1.28.0.** `periods_per_year`, 252 by default, lives on every config
  that reads a covariance or scenario rows, and a limit is read against an annualised covariance:
  monthly returns need `12`, and `periods_per_year=1` keeps the input's own periodicity.
- `covariance_method`: `SAMPLE`, the default of `CovarianceHelper.estimate`, `LEDOIT_WOLF`, `OAS`,
  `EWMA` and `SEMICOVARIANCE` (1.10.0). Ledoit-Wolf and OAS refuse a nonzero `shrinkage`;
  `ewma_decay` reaches every config that names `covariance_method`, and EWMA needs the `date` column
  (1.28.0).
- Missing data in a returns history: `EXCLUDE` drops incomplete rows, `RAISE` errors, and `INCLUDE`
  is refused (0.8.0).
- Risk parity's budgets must cover the universe exactly, and a zero budget raises (1.11.0).
  Black-Litterman's `delta` defaults to `None`, calibrated from the market book (1.28.0).
  `CVaRConfig` and `CDaRConfig` refuse an `alpha` below 0.5 (1.28.0).
- `SizingInterface.allocate(*, snapshot) -> AllocatedUniverse` is the one method an allocator
  implements; `get_sizing_weights(universe=...)` returns the table with the weight column added,
  validated (README).
- **A returns-based method estimates over whatever table it is handed**: see *Known and open*.

## Entities

| Entity | Construct | What the documents say it proves |
| --- | --- | --- |
| `UniverseSnapshot` | `UniverseSnapshot(table=...)`, with an optional `as_of` | the ticker axis present, unique and non-empty; it cannot be filtered to an empty universe (0.3.0) |
| `AllocatedUniverse` | returned by `allocate` | weights on every row, no nulls, non-negative unless shorts are allowed, the sum equal to the target exposure, 1.0 by default — but see *Known and open* for a NaN book |
| `Weights` | `from_allocated(allocated=...)`, `from_table(table=..., weight_column=...)`; the changelog also names `from_scores` and `equal` | every operation returns validated weights or raises. `as_mapping()`; `cap(maximum=...)` **redistributes the excess** and iterates, or raises when the cap is infeasible; `cap_gross`; `cap_groups(classification=..., dimension=..., limits=...)`; `exclude(tickers=...)`; `blend(other, alpha=...)`; `tilt(factors=...)`. `cap`, `cap_groups` and `tilt` refuse short books |
| `Signal` | `Signal.from_mask(mask=..., tickers=..., name=...)` | True, False or null per ticker; `&`, `\|`, `~` are Kleene; `coverage()`; `passing_mask` and `to_binary` collapse it under a policy |
| `BinaryMatrix` | `selection.evaluate_over(snapshots=...)`, `BinaryMatrix.from_panel_threshold(panel=..., threshold=...)`, `BinaryMatrix.from_hysteresis(entry_matrix=..., exit_matrix=..., initial=...)` | dates by tickers, tri-state inside, an absent ticker null. `to_pandas()` has dates as index and tickers as columns; `active_on(target_date=..., missing=...)`, `turnover()`, `hold_through(dates=...)`, `coverage()`, `breadth()` |
| `Classification` | `Classification(assignments=...)`, `Classification.from_snapshot_column(snapshots=..., column=..., dimension=...)` | a dated entry queried without `as_of` raises; an `as_of` before its first record returns None |
| `Mandate` | `Mandate(classification=..., layers=(...), bounds={...}, default_bounds=Bounds(...))` | `violations(weights=...)` audits a book after the solve; `FeasibilityHelper.analyze(mandate=..., tickers=...)` names an impossible constraint, and its fix, before one |

## Selection and timing

- `LiquidityFilter(thresholds=(ThresholdSpec(column=..., op=..., value=...), ...))` — the README
  uses it for any threshold, a z-score or a price above its moving average as well as liquidity.
  `ThresholdSpec` takes `value` or `value_column`, one of the two (1.1.0); the README's
  `ComparisonOp`s are `GE`, `LE` and `GT`.
- `BinaryFilter(column=...)` for a numeric 0/1 flag; `ColumnMembershipFilter(column=...,
  allowed=frozenset(...))` for a string label, matched exactly; `CompositeUniverseFilter(filters=
  (...))` combines its filters with Kleene AND.
- `UniverseCreator(classification=..., dimension=..., rules_by_group=..., base_filters=(...))`:
  `build_membership(snapshots=...)` returns a `UniverseMembership`, whose `matrix` is a
  `BinaryMatrix`, and `explain(target_date=..., ticker=...)` names the rule that decided.
- `CalendarRebalancer(trading_dates=..., frequency=RebalanceFrequency.MONTH_END)` takes the first or
  last trading date per ISO week, month, quarter or year from your own trading dates (0.6.0);
  `get_timing_dates()` returns them.
- `FixedDateRebalancer(dates=...)`; `TimeSignalRebalancer(signal=..., mode=TimingMode.ON_CHANGE,
  missing=...)`, or `WHILE_TRUE` for every active date.
- The QuantLib-backed rebalancers load lazily: their error surfaces only when one is used (0.4.0).

## Pipeline

`run_pipeline(stages=..., snapshots=...)`. `stages` is a tuple of `(name, stage)`, each a selection
or a sizing stage; `snapshots` maps each date to a table, and each stage receives a
`UniverseSnapshot` with `as_of` (1.1.0). `result.weights` maps each date to the final table;
`result.trace.records(date)`, `result.trace.summary()` and `result.trace.dump(directory=...)` show
and write what each stage consumed and produced, as Parquet per date and stage. A failure inside a
stage raises a `PipelineError` carrying the date and the stage name, chaining the original
exception. *Since 2.0.0* it checks the licence first, once per process, before it reads a stage or
a snapshot, and raises a licence error as itself, never wrapped in a `PipelineError`.

## Loading data

The README's flow: `ExcelConfigurator(file_path=...).get_configuration()` reads the workbook;
`MarketDataProcessingService(configuration=config.to_legacy_configuration(), input_handlers=[...])`
takes an input handler, such as `ParquetInput(input_dir=...)`; `load_and_process_market_data(
tickers=...)` returns one `date | ticker` table per column; and `UniverseBuilder().build_snapshots(
market_data_dict=..., tickers=..., required_fields=..., rebalance_dates=...)` returns one table per
rebalance date, one row per ticker and one column per feature.

- A date column in ISO format is required, and an ambiguous DD/MM/YYYY file is refused (1.1.1).
  Missing values flow through as null.
- `build_snapshots` also takes a `MarketDataPanel`, which requires every feature to share the same
  ascending, unique dates and the same tickers (1.0.0).
- `PanelHelper.simple_returns(table=...)` turns a price panel into returns: the first row dropped,
  and a null or zero previous close null (1.15.0).

## Writing the weight file

The Excel and CSV output handlers write `Ticker`, then one ISO date per column: the horizontal
layout the Backtest Engine's portfolio input handlers detect (README; 1.0.1). The README writes it
with `ExcelOutputHandler(output_dir=..., filename=...).write(portfolio=..., config=...)`. The
portfolio entity stores tickers normalised (0.8.1): check they still match the market-data file
names.

## CLI

| Command | Behaviour, as the README gives it |
| --- | --- |
| `kaxanuk.portfolio_construction init excel` | generates `Config/`, with `portfolio_construction_parameters.xlsx`, and `Output/` |
| `kaxanuk.portfolio_construction run`, `autorun` | execute the entry script `init excel` installs |

*Since 2.0.0* the entry script runs its pipeline through `run_pipeline()`, so every command that
runs it needs `KNPC_API_KEY_KAXANUK`, from the environment or a `.kaxanuk_license` file in the home
or the working folder; it does not read `Config/.env`, although the error for a missing key suggests
that file.

Column names are mapped in the workbook; a text cell in the value column of its `Universe_Filters`
sheet is read as a column name (1.1.0).

## Where the README and the changelog disagree, at 1.28.0

- The README's extras table says `calendars` pulls `exchange-calendars`; the changelog makes
  QuantLib the `calendars` dependency group (0.9.0), and its unreleased notes speak of QuantLib
  rebalancers.
- The README says market data may be CSV, Excel or Parquet; its own status table and the changelog
  name only CSV and Parquet input handlers.
- The README's development notes put the example scripts in `portfolio_construction_code_examples/`;
  the rest of the README, and the changelog (1.8.0), put them in `examples/`.
- The README calls the API stable since 1.0.0, and 1.0.0's entry says a breaking change bumps the
  major version; 1.28.0, a minor release, changed `HRPAllocator` and renamed `FrontierBand`'s
  `low_volatility` and `high_volatility` to `low_observed` and `high_observed`.
- The README says the library never guesses around look-ahead; the changelog's *Known and open*
  says a returns-based method inside `run_pipeline` reads future rows.

## Known and open, from the changelog

Recorded under *Known and open after 1.28.0*:

- **Look-ahead in the returns-based family.** Every returns-based allocator estimates over whatever
  table it is handed, and `run_pipeline` calls one allocator on every rebalance date with the same
  table: 24% future observations in the library's own integration test. Slice the returns yourself
  before each rebalance date.
- **`AllocatedUniverse` cannot detect a NaN book.** Its sum check is false for NaN and the
  negativity check passes too, so a book of NaN is accepted: check the weights are finite yourself.
- **Nothing rails observations against assets.** At two dates and four securities HRP returns a book
  of pure noise, and the only floor left is two complete rows.
- **A missing `clustering` extra fails at different moments.** HRP raises `ImportError` when it is
  built; HERC and NCO raise `AllocationError` when they allocate, and the pipeline runner catches
  only the latter.
