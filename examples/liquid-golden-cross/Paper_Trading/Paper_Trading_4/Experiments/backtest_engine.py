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

# --- example: begin ---

import datetime
import importlib.util
import pathlib

import pandas

__all__ = [
    "BENCHMARK_IDENTIFIER",
    "CASH_IDENTIFIER",
    "ENGINE_INSTALLED",
    "EXECUTION_PRICE_COLUMN",
    "MARKET_DATA_DIRECTORY",
    "align_variants",
    "build_configuration",
    "describe_window",
    "earliest_priceable_date",
    "read_daily_weights",
    "run_backtest",
    "write_weight_file",
]

# The index the book is reported against, staged into the market-data folder as a price series, and
# the bill proxy the uninvested residual is parked in.  Named here and nowhere else, so switching
# either is one edit and no notebook carries a file name.
BENCHMARK_IDENTIFIER = "KN600"
CASH_IDENTIFIER = "SHY"
# The engine installs from a licensed index rather than PyPI, so a clone without it still runs
# every other step and says which one it skipped.
ENGINE_INSTALLED = importlib.util.find_spec("kaxanuk.backtest_engine") is not None
# The fill, on the total-return series every return in the experiment uses: the day's VWAP.
EXECUTION_PRICE_COLUMN = "c_vwap_dividend_and_split_adjusted"
MARKET_DATA_DIRECTORY = pathlib.Path(__file__).parent.parent / "Data" / "Curator" / "Time_Series"
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
    benchmark_identifier: str = BENCHMARK_IDENTIFIER,
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

    The benchmark is an argument for a paper book: the index arrives by hand and can lag the day,
    and a run past its last date has to be priced against a benchmark that reached it.  The fill
    price is one for a check: a book whose names come from two providers, one with a VWAP and one
    without, is priced again with every name filled at the close, to show the verdict does not rest
    on how the fills were made.
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
        benchmark_file_name=benchmark_identifier,
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
    The first date on which both the benchmark and the cash proxy have a price.

    A book cannot start before the instruments it is measured against and parks its cash in: the
    engine fails on a position it cannot price, and it fails in the middle of a data-integrity
    check rather than at the window it was given.  Clipping here means the window is a decision
    rather than a crash — and the reason is a fact about an instrument, not about the strategy.
    """
    first_dates = []

    for identifier in (BENCHMARK_IDENTIFIER, CASH_IDENTIFIER):
        path = MARKET_DATA_DIRECTORY / f"{identifier}.csv"
        dates = pandas.read_csv(
            path,
            usecols=["m_date"],
            parse_dates=["m_date"],
        )["m_date"]
        first_dates.append(dates.min())

    return max(first_dates)


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
    # Each weight is rounded down, never to the nearest: a book fully invested in twenty names at a
    # twentieth each rounds up past one, and the engine refuses a column whose gross exposure is
    # above one by a millionth. Rounding down leaves the remainder in cash, where it belongs.
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


# --- example: end ---
