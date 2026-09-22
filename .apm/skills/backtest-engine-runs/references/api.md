# Backtest Engine — the public surface

Taken from the official documentation on 2026-09-06, the `main()` section from a run of **0.66.0**
on 2026-09-17, and the `Configuration` section from the worked example's code, run on 0.66.0 on
2026-09-20. Where a page could not be reached, this file says so rather than guessing: **an
invented signature is worse than a missing one.** The URLs are at the end of `SKILL.md`.

## `main()` — the whole run, verified on 0.66.0

```python
kaxanuk.backtest_engine.main(
    *,
    configuration: Configuration,
    input_handlers: list[InputHandlerInterface],
    portfolio_handlers: list[PortfolioInputHandlerInterface],
    logger_level: int = 20,
    logger_format: str = "[%(levelname)s] %(message)s",
    logger_file: str | bytes | os.PathLike | None,
    launch_dashboard: bool,
    dashboard_port: int,
) -> BacktestResult
```

`logger_file`, `launch_dashboard` and `dashboard_port` are keyword-only with no defaults.
`kaxanuk.backtest_engine.load_config_env(env_path)` reads the licence from a `Config/.env`, which is
how a notebook keeps the key out of its own source. `BacktestResult` carries `success`, `error` and
`data`; the keys of `data`:

| Key | What it holds |
| --- | --- |
| `Register_df` | `Portfolio_Value`, `Total_Portfolio_Value`, `Returns`, indexed by the days the engine **valued** |
| `Daily_Weights` | the drifted book, one row per valued day: the holdings, the benchmark and `CASH_RESERVE` — **what step 6 reads** |
| `Shares_df`, `orders_df`, `portfolio_df` | share counts and orders per rebalance date, and the weight file as it was read |
| `Commission_df`, `Slippage_df`, `Execution_costs_df`, `Total_commissions`, `Total_slippage_costs` | what the trading cost |
| `Financing_df`, `Total_financing_costs`, `Risk_free_rate` | borrow, margin and cash interest |
| `Forced_liquidations_df` | positions the engine had to exit, with the reason |
| `benchmark`, `benchmarks`, `benchmark_stats`, `benchmarks_stats` | the comparison arm |
| `portfolio_stats` | `Start Balance`, `End Balance`, `Net Return`, `PnL`, `Annualized Return (CAGR)`, `Annualized Volatility` and the rest |
| `start_date`, `end_date`, `years`, `initial_portfolio_value`, `final_total_portfolio_value` | **the window actually valued**, and the balances |

`start_date`, `end_date` and `years` describe what was valued, not what was configured. Compare them
with the configured window before quoting a metric: a run that stopped partway still returns
`success=True` with `error=None` (see `SKILL.md`, section 6).

## `entities.Configuration` and the input handlers, as the worked example calls them

Read from the worked example's `Experiments/backtest_engine.py`, run on **0.66.0** on 2026-09-20.
These are the keyword arguments it passes, not the full signature: a field it does not set is not
listed, and nothing here says what its default is.

| Field | The example's value | What it decides |
| --- | --- | --- |
| `initial_capital` | `1_000_000` | the starting cash |
| `start_date`, `end_date` | `datetime.date` | the window asked for; compare with `data["start_date"]` and `data["end_date"]` after the run |
| `cash_reserve_percentage` | `0.02` | cash held back to pay commission; `0` truncates the run (`SKILL.md`, section 6) |
| `commission_cents` | `0.1`; `0.005` in the realistic variant | the commission rate; not cents per share (`SKILL.md`, section 6) |
| `commission_model` | `"per_share"` | how commission is charged |
| `slippage_model`, `slippage_basis_points` | `"basis_points"`, `5.0` | slippage |
| `market_data_input_format`, `portfolio_input_format` | `"csv"` | the format of each input |
| `input_market_data_directory` | `Data/Curator/Time_Series`, as a `str` | one `{TICKER}.csv` per security, the benchmark's included |
| `input_portfolio_directory` | `Experiments/Experiment_N/Portfolio`, as a `str` | where the weight file is |
| `portfolio_name` | `"portfolio_weights"` | the weight file's name, without `.csv` |
| `benchmark_file_name` | `"KN600"` | the benchmark's price file in the market-data directory, without `.csv` |
| `backtest_results_output_directory` | `Experiments/Experiment_N/Backtest`, as a `str` | where the results land |
| `user_column_date` | `"m_date"` | the date column |
| `user_column_commission_price` | `"c_vwap"` | the price commission is charged on: **unadjusted** |
| `user_column_trade_execution_price` | `"c_vwap_dividend_and_split_adjusted"` | the fill price, on the total-return basis |
| `user_column_mark_to_market_price` | `"m_close_dividend_and_split_adjusted"` | the daily valuation, on the total-return basis |
| `rebalance_date_handling` | `"next_trading_day"` | a rebalance date that is not a trading day moves to the next one |
| `delisted_position_handling` | `"sell_at_last_price"` | a position whose prices stop is sold on its last priced day: one day of hindsight |

`commission_model` and `slippage_model` here are strings; the `PyArrowBacktester` arguments of the
same names take model objects. The input handlers each take a directory as a `str`, and `main()`
and `create_from_configuration` take each in a one-item list:

```python
import kaxanuk.backtest_engine.input_handlers

csv_input = kaxanuk.backtest_engine.input_handlers.CsvInput(
    input_dir=market_data_directory,
)
csv_portfolio_input_handler = kaxanuk.backtest_engine.input_handlers.CsvPortfolioInputHandler(
    portfolio_directory,
)
```

## `PyArrowBacktester`

Module: `kaxanuk.backtest_engine.backtest.pyarrow_backtester`. Base: `BaseBacktesterInterface`.

```python
PyArrowBacktester(
    *,
    configuration: Configuration,
    market_data_bundle: MarketDataBundlePyarrow,
    portfolio_dict: dict[Timestamp, dict[str, float]],
    benchmark: Table | None,
    portfolio_df: DataFrame | None = None,
    commission_model: CommissionModelInterface | None = None,
    slippage_model: SlippageModelInterface | None = None,
    benchmarks: dict[str, Table] | None = None,
)
```

Keyword-only. In practice it is built through one of the two class methods rather than directly:

```python
@classmethod
create_from_configuration(
    configuration: Configuration,
    input_handlers: list[InputHandlerInterface],
    portfolio_handlers: list[PortfolioInputHandlerInterface],
    commission_model: CommissionModelInterface | None = None,
    slippage_model: SlippageModelInterface | None = None,
) -> PyArrowBacktester
```

```python
@classmethod
create_from_pipeline_result(
    configuration: Configuration,
    pipeline_result: DataPipelineResult,
    commission_model: CommissionModelInterface | None = None,
    slippage_model: SlippageModelInterface | None = None,
) -> PyArrowBacktester
```

Run it:

| Method | Returns |
| --- | --- |
| `run()` | `BacktestResultDict` |
| `run_with_benchmark()` | `BacktestResultDict`, with the comparison arm |

Properties on the instance: `execution_broker` (`ExecutionBroker`), `portfolio_manager`
(`PortfolioStateManager`), `rebalance_dates` (`list[Timestamp]`), `reporting_engine`
(`ReportingEngine`), `tickers` (`list[str]`).

## The `metrics` module

Public, so a figure quoted in a document can be recomputed from the returned series instead of copied
out of a cell.

**Return and risk**

| Function | Returns |
| --- | --- |
| `annualize_rets(r, periods_per_year=252)` | `float` — `(1 + r).prod() ** (periods_per_year / n_periods) - 1` |
| `annualize_vol(r, periods_per_year=252)` | `float` — `r.std() * sqrt(periods_per_year)` |
| `calculate_annualized_return(initial_value, final_value, years)` | `float` — CAGR |
| `compound(r)` | `float` — `expm1(log1p(r).sum())` |
| `sharpe_ratio(r, riskfree_rate, periods_per_year=252)` | `float` |
| `sortino_ratio(r, riskfree_rate=0.0, target_return=None, periods_per_year=252)` | `float` |
| `sortino_ratio_simple(r, riskfree_rate=0.0, periods_per_year=252, use_log_returns=False)` | `float` |
| `downside_deviation(r, target_return=0.0, periods_per_year=252)` | `float` |
| `var_historic(r, level=5)` | `float` or `pd.Series` |
| `var_gaussian(r, level, modified)` | `float` — Cornish-Fisher when `modified` |
| `cvar_historic(r, level=5)` | `float` or `pd.Series` |
| `tracking_error(portfolio_returns, benchmark_returns, periods_per_year=252, annualized=True)` | `float` |
| `information_ratio(portfolio_returns, benchmark_returns, periods_per_year=252)` | `float` |
| `skewness(r)` / `kurtosis(r)` | `float` — population, kurtosis not excess |
| `drawdown(return_series)` | `pd.DataFrame` — Wealth, Previous Peak, Drawdown |

**Series and tables**

| Function | Returns |
| --- | --- |
| `index_price_construction(daily_portfolio_returns, base=1000)` | `pd.Series` |
| `wealth_index(returns, initial_capital)` | `pd.Series` |
| `analyze_annual_returns(df, portfolio_column, strategy_name, method='simple', min_observations=2)` | `pd.DataFrame` |
| `calculate_yearly_returns(series, strategy_name, method, min_observations, annualize=True, trading_days_per_year=252)` | `list[dict]` |
| `calculate_daily_returns(price_array)` | `pa.Array` |
| `calculate_pct_change(price_array)` | `pa.Array` |
| `calculate_returns_table(price_table, date_column_name)` | `pa.Table` |
| `decimal_cumprod_pyarrow(returns_array)` | `pa.Array` |
| `pct_change_pyarrow(column, output_column_name, table, periods=1)` | `pa.Table` |

**Composite and plots**

`compute_portfolio_statistics(initial_capital, initial_portfolio_value, final_portfolio_value,
returns, total_portfolio_series, years, risk_free_rate=0.0, var_level=5.0, periods_per_year=252,
benchmark_returns=None, additional_metrics=None)` returns `dict[str, float]` — performance, risk and
distribution metrics in one call.

`annual_returns_plot(...)` and `active_returns_plot(...)` return a `matplotlib.figure.Figure`.
**A KaxaNuk Strategy Template repository commits no charts**, so these are for looking at, not for saving
into the tree.

## CLI

```
uv run python -m kaxanuk.backtest_engine [--version] COMMAND [ARGS]...
```

| Subcommand | Arguments and options |
| --- | --- |
| `autorun` | installs missing project files on the first run, then executes the entry script |
| `init CONFIG_FORMAT` | `excel`; `--entry_script <name>` changes the generated entry script (default `__main__.py`) |
| `run [ENTRY_SCRIPT_LOCATIONS]...` | paths to entry scripts or directories |
| `update CONFIG_FORMAT` | `excel` or `entry_script` — refresh a template |

The quick start also documents `kaxanuk.backtest_engine init excel` as the first command after
installing, and `python -m kaxanuk.backtest_engine.services.cli autorun` as the run command. Treat
the module-level form above as current and the services path as the older spelling; confirm against
the installed build's `--version` before writing either into a project.

## Named in the documentation but not verified here

These appear in the API overview, but their signature pages could not be retrieved. **Read the
component pages before calling them; do not infer a signature from the name.**

- `MultiPortfolioBacktester.generate_individual_reports` — under Backtest Components, Orchestrators.
- `arrow_to_pandas_for_analysis()` — the helper that turns returned PyArrow tables into pandas.
- Cost models, execution, interfaces and enums — Backtest Components lists them as Commission,
  slippage and trading-record models; portfolio state, trade broker and reporting engine; abstract
  interfaces for backtesters and cost models; and trading enums for order side, price type and
  rebalance status.
- Portfolio Data Pipeline: portfolio configuration service, transformer, helpers and date utilities.

## Inputs, in one place

| Input | Shape |
| --- | --- |
| Portfolio, horizontal | first column `Ticker`; one column per rebalancing date |
| Portfolio, vertical | first column `date`; one column per ticker |
| Market data | `{TICKER}.csv` or `{TICKER}.parquet`; a date column plus at least three price columns, roles mapped in the configuration |
| Dates | `YYYY-MM-DD` |
| Configuration | `Config/backtest_engine_parameters.xlsx`; in code an `entities.Configuration` (see above), or a dict or YAML |
| Licence | `Config/.env` — `KNBE_API_KEY_KAXANUK`. The published quick start still shows an older `KNPC_API_KEY_KAXANUK`; that spelling is stale |
