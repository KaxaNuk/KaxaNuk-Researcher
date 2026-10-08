"""
Backtest engine -- step 5 of 8, the third shared module.  The one path from a book of weights to a
performance number, through the KaxaNuk Backtest Engine.

In plain words: the simulation, run by the engine, with costs and without peeking ahead.

Runs inside an experiment notebook, section 4, after the book has been written to `Portfolio/`.

What is expected here:

- Write the weight file the engine reads: `Portfolio/portfolio_weights.csv`, wide, keyed by the
  identifier the market-data files are named by, dates across the columns, every column summing to
  exactly 1.0.  The engine has no cash row, so the uninvested residual becomes a weight in the cash
  proxy -- going to cash pays commission and earns the bill yield, as it does in life.  A security
  that changed identifier mid-history occupies two rows, each non-zero only while that listing was
  live.
- Run the licensed engine and read its results back: the daily series it marks, the book's daily
  weights as it held them -- the input step 6 needs -- and its summary statistics.  Import it
  inside a guard -- it installs from a licensed index, not PyPI -- and report and skip when it is
  absent, so a clone without a licence still produces everything except the numbers.
- Name the benchmarks a strategy is reported against, in one place, and clip the window to the
  shortest of them up front rather than discovering it as an error.
- Align every variant of an experiment onto one common window before ranking them.  A variant that
  starts a year later is not comparable on its own dates.

There is deliberately no second, lighter simulator here or anywhere.  One that disagrees with the
engine lets the reader pick the number they prefer, and every figure quoted in `RESULTS.md` comes
through this module.

It produces `Backtest/` -- the engine's workbook and the series drawn from it, the daily weights
among them -- for `FINDINGS_N.md` to record and `attribution_analysis.py` to read.

It prevents paper returns that real trading would have erased, and a difference in cost model or
window showing up as strategy skill.
"""


import concurrent.futures
import datetime
import hashlib
import importlib.util
import json
import os
import pathlib
import tempfile

import pandas

__all__ = [
    "BENCHMARK_IDENTIFIERS",
    "CASH_IDENTIFIER",
    "ENGINE_INSTALLED",
    "EXECUTION_PRICE_COLUMN",
    "INDEX_IDENTIFIER",
    "MARKET_DATA_DIRECTORY",
    "align_variants",
    "build_configuration",
    "describe_window",
    "earliest_priceable_date",
    "price_book",
    "price_books",
    "read_daily_weights",
    "run_backtest",
    "write_weight_file",
]

# The benchmarks the book is reported against -- the KN US Equity Core first, staged into the
# market-data folder as a price series, then SPY -- and the bill proxy the uninvested residual is
# parked in.  Named here and nowhere else, so switching any of them is one edit and no notebook
# carries a file name.  The engine takes several benchmarks as one comma-separated name, and the
# first is the one every alpha and information ratio it reports is measured against; attribution
# compares the book against that index and no other.
BENCHMARK_IDENTIFIERS = (
    "KN_US_Equity_Core",
    "SPY",
)
CASH_IDENTIFIER = "BIL"
# The engine installs from a licensed index rather than PyPI, so a clone without it still runs
# every other step and says which one it skipped.
ENGINE_INSTALLED = importlib.util.find_spec("kaxanuk.backtest_engine") is not None
# The fill, on the total-return series every return in the experiment uses: the day's VWAP.
EXECUTION_PRICE_COLUMN = "c_vwap_dividend_and_split_adjusted"
INDEX_IDENTIFIER = BENCHMARK_IDENTIFIERS[0]
MARKET_DATA_DIRECTORY = pathlib.Path(__file__).parent.parent / "Data" / "Curator" / "Time_Series"
# The licence file, loaded by its own path before a worker leaves the repository's folder.
ENVIRONMENT_PATH = pathlib.Path(__file__).parent.parent / "Config" / ".env"
# The engine parses weights as fixed-scale decimals and refuses a value it cannot hold exactly, so
# a third written as 0.3333333333333333 fails before the first fill.  Six places is a hundredth of
# a basis point, far below anything a book can trade.
WEIGHT_DECIMALS = 6


def align_variants(
    returns_by_variant: dict[str, "pandas.Series"],
) -> dict[str, "pandas.Series"]:
    """
    Clip every variant to the window they all share, before any of them are ranked.

    A variant that starts a year later is not comparable on its own dates, and the difference shows
    up as skill.
    """
    first_dates = [
        series.index.min()
        for series in returns_by_variant.values()
    ]
    last_dates = [
        series.index.max()
        for series in returns_by_variant.values()
    ]
    common_start = max(first_dates)
    common_end = min(last_dates)

    return {
        name: series.loc[common_start:common_end]
        for name, series in returns_by_variant.items()
    }


def build_configuration(
    experiment_directory: "pathlib.Path",
    start_date: "datetime.date",
    end_date: "datetime.date",
    initial_capital: int,
    commission_cents: float,
    slippage_basis_points: float,
    cash_reserve_percentage: float,
    portfolio_name: str = "portfolio_weights",
    benchmark_identifiers: tuple[str, ...] = BENCHMARK_IDENTIFIERS,
    execution_price_column: str = EXECUTION_PRICE_COLUMN,
) -> object:
    """
    Describe the simulation, including which column of the market data plays which role.

    The roles are declared rather than inferred from a column's name, which is what lets commission
    be charged on the unadjusted price while the fill and the mark run on the total-return series.
    Costs are arguments because a result is accepted net or not at all, and a default nobody chose
    is how a cost assumption goes unexamined.

    The cash reserve is an argument for a different reason: weights summing to exactly one leave
    nothing to pay commission with, and the engine fails at the first rebalance rather than
    quietly overdrawing.  A real book holds the same buffer for the same reason.

    The benchmarks are an argument for a paper book: the index arrives by hand and can lag the day,
    and a run past its last date has to be priced against a benchmark that reached it.  The fill
    price is one so the same configuration can price a check filled at the close.
    """
    import kaxanuk.backtest_engine.entities

    return kaxanuk.backtest_engine.entities.Configuration(
        initial_capital=initial_capital,
        start_date=start_date,
        end_date=end_date,
        cash_reserve_percentage=cash_reserve_percentage,
        commission_cents=commission_cents,
        commission_model="per_share",
        market_data_input_format="csv",
        portfolio_name=portfolio_name,
        portfolio_input_format="csv",
        benchmark_file_name=",".join(benchmark_identifiers),
        input_market_data_directory=str(MARKET_DATA_DIRECTORY),
        input_portfolio_directory=str(experiment_directory / "Portfolio"),
        backtest_results_output_directory=str(experiment_directory / "Backtest"),
        user_column_date="m_date",
        # Commission is charged on the price a person would have paid that day.
        user_column_commission_price="c_vwap",
        # Fills and marks run on the total-return series every return in the experiment uses.
        user_column_trade_execution_price=execution_price_column,
        user_column_mark_to_market_price="m_close_dividend_and_split_adjusted",
        # A rebalance date that is not a trading day moves to the next one rather than failing.
        rebalance_date_handling="next_trading_day",
        # The one deliberate look-ahead this process names: a position in a security whose prices
        # stop is sold on its last priced day, which nobody could have known was the last.
        delisted_position_handling="sell_at_last_price",
        slippage_model="basis_points",
        slippage_basis_points=slippage_basis_points,
    )


def describe_window(
    result: object,
    end_date: "datetime.date",
) -> str:
    """
    Compare the window the engine actually valued with the one it was asked for.

    A run that stops valuing the book partway still returns success and still summarises cleanly
    over the stub.  This is the check that catches it, and a variant that fails it is excluded by
    name with its reason rather than quietly dropped.
    """
    valued_end = result.data.get("end_date")
    years = result.data.get("years")

    if valued_end is None:

        return "the engine returned no end date: treat every figure from this run as unverified"

    valued_date = pandas.Timestamp(valued_end).date()

    if valued_date < end_date - datetime.timedelta(days=7):

        return f"TRUNCATED: valued to {valued_date}, asked for {end_date} ({years} years)"

    return f"complete: valued to {valued_date} ({years} years)"


def earliest_priceable_date() -> "pandas.Timestamp":
    """
    The first date on which every benchmark and the cash proxy have a price.

    A book cannot start before the instruments it is measured against and parks its cash in: the
    engine fails on a position it cannot price, and it fails in the middle of a data-integrity
    check rather than at the window it was given.  Clipping here means the window is a decision
    rather than a crash — and the reason is a fact about an instrument, not about the strategy.
    """
    first_dates = []

    for identifier in (*BENCHMARK_IDENTIFIERS, CASH_IDENTIFIER):
        path = MARKET_DATA_DIRECTORY / f"{identifier}.csv"
        dates = pandas.read_csv(
            path,
            usecols=["m_date"],
            parse_dates=["m_date"],
        )["m_date"]
        first_dates.append(dates.min())

    return max(first_dates)


def price_book(
    task: dict[str, object],
) -> dict[str, object]:
    """
    Price one weight file in the engine and hand back its tables as plain pandas objects.

    Written to run in a worker process, so a notebook can price many books at once: everything it
    takes and returns can be pickled.  The answer is cached under the hash of the weight file and
    the settings, so a notebook re-run after a late failure skips the books already priced -- and a
    weight file that changed by one digit is priced again, because its hash changed.
    """
    experiment_directory = pathlib.Path(str(task["experiment_directory"]))
    portfolio_name = str(task["portfolio_name"])
    weight_path = experiment_directory / "Portfolio" / f"{portfolio_name}.csv"
    cache_path = _cache_path(
        experiment_directory,
        weight_path,
        task,
    )

    if cache_path.is_file():

        return pandas.read_pickle(cache_path)

    end_date = datetime.date.fromisoformat(str(task["end"]))
    configuration = build_configuration(
        experiment_directory,
        datetime.date.fromisoformat(str(task["start"])),
        end_date,
        int(task["initial_capital"]),
        float(task["commission_cents"]),
        float(task["slippage_basis_points"]),
        float(task["cash_reserve_percentage"]),
        portfolio_name,
        tuple(task.get("benchmark_identifiers", BENCHMARK_IDENTIFIERS)),
        str(task.get("execution_price_column", EXECUTION_PRICE_COLUMN)),
    )
    # The engine draws its report's charts into a file of one fixed name in the working folder, so
    # two engines in one folder overwrite each other's; each run gets a folder of its own, after the
    # licence is loaded from the repository's.
    import kaxanuk.backtest_engine

    kaxanuk.backtest_engine.load_config_env(ENVIRONMENT_PATH)
    home = pathlib.Path.cwd()

    with tempfile.TemporaryDirectory() as scratch:
        os.chdir(scratch)

        try:
            result = run_backtest(
                experiment_directory,
                configuration,
            )
        finally:
            os.chdir(home)

    if not result.success:
        failed = {
            "error": str(result.error),
            "name": portfolio_name,
            "success": False,
        }

        return failed

    data = result.data
    priced = {
        "benchmark_stats": dict(data.get("benchmark_stats") or {}),
        "benchmarks_stats": _plain_benchmarks(data.get("benchmarks_stats")),
        "daily_weights": _to_pandas(data["Daily_Weights"]),
        "end_date": str(data.get("end_date")),
        "error": None,
        "name": portfolio_name,
        "orders": _to_pandas(data["orders_df"]),
        "portfolio_stats": dict(data["portfolio_stats"]),
        "register": _to_pandas(data["Register_df"]),
        "start_date": str(data.get("start_date")),
        "success": True,
        "window": describe_window(
            result,
            end_date,
        ),
        "years": data.get("years"),
    }
    pandas.to_pickle(
        priced,
        cache_path,
    )

    return priced


def price_books(
    tasks: list[dict[str, object]],
    workers: int,
) -> dict[str, dict[str, object]]:
    """
    Price many weight files at once, one engine run per worker process, keyed by portfolio name.

    The engine prices one book on one core; a notebook pricing forty books one after another
    spends an evening on what a pool of workers does in a fraction of it.  A book whose run raises
    comes back with its error rather than stopping the others, and the caller decides.
    """
    priced = {}

    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(price_book, task): str(task["portfolio_name"])
            for task in tasks
        }

        for future in concurrent.futures.as_completed(futures):
            name = futures[future]

            try:
                priced[name] = future.result()
            except Exception as error:  # noqa: BLE001 - one book's failure must not stop the rest
                priced[name] = {
                    "error": f"{type(error).__name__}: {error}",
                    "name": name,
                    "success": False,
                }

    return priced


def read_daily_weights(
    result: object,
) -> "pandas.DataFrame":
    """
    Read the book as the engine held it each trading day, which is what step 6 attributes.

    The weight file holds the rebalance dates alone; this is the drifted book between them, and the
    attribution library refuses the former once it spans a year.
    """
    daily_weights = result.data["Daily_Weights"]

    if hasattr(daily_weights, "to_pandas"):

        return daily_weights.to_pandas()

    return pandas.DataFrame(daily_weights)


def run_backtest(
    experiment_directory: "pathlib.Path",
    configuration: object,
) -> object:
    """
    Run the licensed engine over the weight file already written, and hand back its result.

    Every performance figure in this repository comes through here: there is deliberately no second
    simulator, because one that disagreed would only let a reader pick the number they preferred.
    """
    if not ENGINE_INSTALLED:
        missing_engine_message = "the KaxaNuk Backtest Engine is not installed: step 5 skipped"

        raise ModuleNotFoundError(missing_engine_message)

    import kaxanuk.backtest_engine
    import kaxanuk.backtest_engine.input_handlers

    kaxanuk.backtest_engine.load_config_env()
    output_directory = experiment_directory / "Backtest"
    output_directory.mkdir(
        parents=True,
        exist_ok=True,
    )
    csv_input = kaxanuk.backtest_engine.input_handlers.CsvInput(
        input_dir=str(MARKET_DATA_DIRECTORY),
    )
    portfolio_input = kaxanuk.backtest_engine.input_handlers.CsvPortfolioInputHandler(
        str(experiment_directory / "Portfolio"),
    )

    return kaxanuk.backtest_engine.main(
        configuration=configuration,
        input_handlers=[csv_input],
        portfolio_handlers=[portfolio_input],
        logger_file=None,
        launch_dashboard=False,
        dashboard_port=8050,
    )


def write_weight_file(
    weights: "pandas.DataFrame",
    experiment_directory: "pathlib.Path",
    name: str = "portfolio_weights",
) -> "pathlib.Path":
    """
    Write the book in the layout the engine detects: identifiers down, rebalance dates across.

    The engine has no cash row, so whatever the rule left uninvested becomes a weight in the cash
    proxy: going to cash buys a real instrument, pays commission and earns a yield, as it does in
    life.  Every column is checked to sum to one before the file is written, because a column that
    does not is a book the engine will price as something else.
    """
    portfolio_directory = experiment_directory / "Portfolio"
    portfolio_directory.mkdir(
        parents=True,
        exist_ok=True,
    )
    # Each weight is rounded down, never to the nearest: forty weights rounded to six places can
    # sum to a few millionths over one, and the engine refuses a column whose gross exposure is
    # above one by a millionth.  Rounding down leaves the remainder in cash, where it belongs.
    scale = 10 ** WEIGHT_DECIMALS
    transposed = weights.transpose()
    scaled = transposed.mul(scale)
    held = scaled.floordiv(1).div(scale)
    invested = held.sum(axis=0).round(WEIGHT_DECIMALS)
    cash = 1.0 - invested
    held.loc[CASH_IDENTIFIER] = cash.round(WEIGHT_DECIMALS).clip(lower=0.0)
    totals = held.sum(axis=0)
    off_by_more_than_a_cent = totals[(totals - 1.0).abs() > 0.0001]

    if len(off_by_more_than_a_cent) > 0:
        unbalanced_message = f"{len(off_by_more_than_a_cent)} rebalance dates do not sum to 1.0"

        raise ValueError(unbalanced_message)

    named = held.copy()
    named.index.name = "Ticker"
    formatted_columns = []

    for column in named.columns:
        timestamp = pandas.Timestamp(column)
        rebalance_date = timestamp.date()
        formatted_columns.append(rebalance_date.isoformat())

    named.columns = formatted_columns
    path = portfolio_directory / f"{name}.csv"
    named.to_csv(
        path,
        float_format=f"%.{WEIGHT_DECIMALS}f",
    )

    return path


def _cache_path(
    experiment_directory: "pathlib.Path",
    weight_path: "pathlib.Path",
    task: dict[str, object],
) -> "pathlib.Path":
    """
    Where one engine run's answer is kept: named by the hash of its weight file and its settings.
    """
    settings = {
        key: str(value)
        for key, value in sorted(task.items())
        if key != "experiment_directory"
    }
    digest = hashlib.sha256()
    digest.update(weight_path.read_bytes())
    settings_text = json.dumps(
        settings,
        sort_keys=True,
    )
    digest.update(settings_text.encode("utf-8"))
    cache_directory = experiment_directory / "Backtest" / "cache"
    cache_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    return cache_directory / f"{digest.hexdigest()}.pkl"


def _plain_benchmarks(
    benchmarks: object,
) -> dict[str, dict]:
    """
    The engine's statistics for every benchmark, as plain dictionaries, empty when it gave none.
    """
    if not isinstance(benchmarks, dict):

        return {}

    return {
        str(identifier): dict(statistics)
        for identifier, statistics in benchmarks.items()
        if isinstance(statistics, dict)
    }


def _to_pandas(
    table: object,
) -> "pandas.DataFrame":
    """
    An engine table as a pandas frame, whichever library the engine built it with.
    """
    if hasattr(table, "to_pandas"):

        return table.to_pandas()

    return pandas.DataFrame(table)
