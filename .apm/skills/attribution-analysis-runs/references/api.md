# Attribution Analysis — the surface a run touches

The API reference is public: `https://kaxanuk-attribution-analysis.readthedocs-hosted.com/en/latest/api_reference/index.html`,
build **0.2.0**, read on 2026-09-17. This file keeps only what a run touches, and the places the
documentation and a run disagree; it is written from the documentation, the changelog and runs,
never from the library's code. Everything lives under `kaxanuk.attribution_analysis`.

## The entry point — `performance_attribution.main`

```python
main(
    configuration: Configuration,
    *,
    launch_dashboard: bool = True,
    dashboard_port: int,
) -> None
```

`dashboard_port` is **required and has no default**. It returns `None`: log lines, matplotlib
figures, and a Dash server when `launch_dashboard=True` *and* the factor model is enabled. As the
API reference orders it, it loads the market prices, the portfolio and benchmark weights, the
benchmark returns and the factor files; aligns every table to the common date range; runs the
enabled methods in turn; then plots or serves.

The API reference names `LicenseError` (before any data is read), `FileNotFoundError` and
`ConfigurationError`; the weight entities raise `DataIntegrityError` and `NullError`, and a run on
0.2.0 raised `MissingPortfolioError` for a weight file with the wrong first header.

## Configuration

- `entities.configuration.Configuration` — a frozen dataclass: six directories, three file names,
  the two market-data column names, the two formats, `start_date` / `end_date` (`datetime.date` or
  `"auto"`) and the two method flags. It raises `ConfigurationError` on an invalid value.
- `config_handlers.excel_configurator.ExcelConfigurator(path)` — `get_configuration()`,
  `get_dashboard_port()`, as *Running from Python* shows.
- `services.env_loader.load_config_env()` and
  `services.configuration_logger.configure_logger(logger_name=..., logger_level=...,
  logger_format=...,
  logger_file=...)` — used as *Running from Python* shows; neither has an API page.
- `services.license_validator.validate_license()` — from 0.3.0's changelog, not checked here: it
  returns the licence client's keyword-only `ValidationResult` (`ok`, `message`, `expires_at`), and
  `reset_validation_state()` makes the next call check again.

## `interfaces.brinston_fachler_arrow_method.BrinstonFachlerArrowAttribution`

```python
BrinstonFachlerArrowAttribution(
    returns_investable_assets: pa.Table,
    complete_portfolio_weights: pa.Table,
    complete_benchmark_weights: pa.Table,
    date_column: str = "date",
)
```

| Call | Sets |
| --- | --- |
| `brinson_fachler_model(date)` | `.detail_table`, `.totals` |
| `time_series_calculation()` | `.df`, `.output_dict` |
| `attribution_plots()` | `.brinston_fach_indexes`, and draws a three-panel figure; called after `time_series_calculation()` |

Effects per asset and date, from the *Brinson-Fachler* methodology page:
`allocation = (w_p − w_b) · r_b` with `r_b = w_b · r`, `selection = alpha · w_p`,
`interaction = alpha − allocation − selection`.

## `interfaces.factor_model_arrow_attribution.KNFMArrowAttribution`

```python
KNFMArrowAttribution(
    daily_portfolio_weights: pa.Table,
    by_factor_factor_returns: dict[str, pa.Table],
    asset_returns: pa.Table,
    portfolio_returns: pa.Table | None = None,
    benchmark_returns: pa.Table | None = None,
    date_column: str = "date",
)
```

The documentation gives this signature under the name `FactorModelArrowAttribution`; the class a run
on 0.2.0 imports is `KNFMArrowAttribution`.

| Call | Sets or returns |
| --- | --- |
| `multifactor_attribution()` | `.portfolio_attribution_ts`; logs the average factor coverage |
| `time_series_calculation()` | `.simulated_rets` |
| `run()` | both |
| `calc_pct_area()` | `.pct_df_returns`, with `f_idio_returns` |
| `cummulative_pct_decomp()` | returns `dict[str, float]`, with `idio_returns` |
| `attribution_plots(title=None)`, `last_day_decomposition(title)` | figures |

`modules.data_wrangling.load_by_factor_returns_arrow(path, available_factors, portfolio_weights,
start_date=None, end_date=None)` returns `dict[str, FactorReturns]` — pass `{name:
factor.table}` to the class. The worked example passes the file names, extension included, as
`available_factors`. The API reference says it keeps the date column and the portfolio's own
tickers.

## Entities that decide whether a run loads

| Entity | Validation, as the API reference states it |
| --- | --- |
| `entities.portfolio_weights_arrow.PortfolioWeights` | a `date` timestamp column, no nulls, and **240–260 rows a year** near the start and the end once the table spans a year |
| `entities.factor_returns.FactorReturns` | a table and a `factor_name`; partial coverage of the portfolio is allowed |

## Metrics — `modules.performance_functions`

`annualize_rets`, `annualize_vol`, `compound`, `cvar_historic`, `drawdown`, `kurtosis`,
`portfolio_return_daily_ts`, `semideviation`, `sharpe_ratio`, `skewness`, `summary_stats`,
`var_gaussian`, `var_historic`. `summary_stats(r, riskfree_rate=0.0, periods_per_year=252)` returns
one row indexed `'Strategy'`. The annualising functions take `periods_per_year` and infer nothing.

## The CLI and the dashboard

`kaxanuk.attribution_analysis init excel [--entry_script NAME]`, `run [PATHS...]`, `autorun`,
`update excel | entry_script`, `--version`. An `AttributionDashboard` serves with
`run_server(*, debug=True, port=8050)`, Dash's development server.

## Where the documentation and a run disagree, at 0.2.0

Each changes what a caller should do.

1. **Results are not written to `Output/`.** The quick start, the Excel workflow and the CLI page
   say they are; a full `main()` run wrote nothing. Build the attribution objects and read their
   attributes.
2. **The *Data Formats* weight example cannot load.** It shows three rebalance dates over four
   years; the weight entities' own daily-density rule rejects anything but a daily series once it
   spans a year.
3. **The `main()` examples omit `dashboard_port`**, which the signature requires.
4. **A vertical weight file's first header is `date_column`, not `Date`/`date`.** *Data Formats*
   asks for a date header; a run raised
   `MissingPortfolioError: First column must be 'Ticker' or 'date_column'` for `date`, and loaded
   `date_column`.
5. **The factor model class is `KNFMArrowAttribution`.** Every API page calls it
   `FactorModelArrowAttribution`; importing that name raises `ImportError` on 0.2.0, and the worked
   example runs `KNFMArrowAttribution` from the same module.

## Checked by running 0.2.0 on 2026-09-17

A full `main()` over a synthetic book, a real 788-ticker benchmark and twenty real factor files:

- a vertical benchmark weight file with `date_column` loads (`Detected vertical format`, 788
  tickers) and passes the daily-density check at about 251 rows a year;
- the benchmark returns file loads through the same handler as one ticker;
- factor files whose **first header is empty** load, each logging
  `Factor '<name>': reading k/n asset columns`, with the factor name taken from the file name;
- the alignment line is `Aligned all tables to common date range: <start> to <end>`, and the
  coverage line prints as a percentage:
  `Average total factor coverage throughout the portfolio :  100.0000%`;
- both methodologies ran, `main()` called `plt.show()` for each (harmless under
  `matplotlib.use("Agg")`, which logs a `FigureCanvasAgg is non-interactive` warning), and **no file
  was written**.

Building the two objects by hand afterwards, as the only way to get numbers out, returned exactly
the attributes above: `BrinstonFachlerArrowAttribution.df` with `date`, `portfolio_returns`,
`benchmark_returns`, `alpha`, `allocation`, `selection`, `interaction`, one row per aligned date,
and the identity `alpha = allocation + selection + interaction` holding to floating-point precision;
`.brinston_fach_indexes` and `.output_dict` populated after `attribution_plots()`;
`KNFMArrowAttribution.portfolio_attribution_ts` with one column per factor file, `.simulated_rets`,
`.pct_df_returns`, and `cummulative_pct_decomp()` returning a share per factor plus `idio_returns`.
The decomposition **included `f_Market`** while excluding `f_idyo_returns`, `f_total_excess_returns`
and `f_total_factor_returns`: the names are matched exactly and in lower case, so a file named
`f_Market.csv` is treated as an ordinary factor.
