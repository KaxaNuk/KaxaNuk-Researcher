"""
Data Curator -- step 3 of 8, block 1 of 3.  The only file in this repository that downloads time
series from a data provider.  `Universe/universe.ipynb` asks the same provider what each security
*is* -- name, type, exchange, currency, inception -- and caches that payload in
`Universe/Provider_Cache/`; nothing else talks to a provider.

In plain words: you describe the data you want -- provider, identifiers, dates and columns -- and
the KaxaNuk Data Curator fetches it, aligns the calendar, handles splits and dividends, and writes
one file per identifier, the same way every run.

Runs first.  Nothing has to exist before it except `Universe/Investable_Universe.csv` and a
provider key in `Config/.env`.  `Universe/universe.ipynb` profiles what this writes.

What is expected here is a short driver, not a framework:

- Read the identifiers from `Universe/Investable_Universe.csv`, column `main_identifier`.  The
  seed is the authority on what exists, so it drives the download.
- Build one Data Curator configuration: the date window, those identifiers, and the output columns
  -- the provider's `m_*` columns plus the `c_*` columns defined in
  `Data/Curator/custom_calculations.py`.  Fix the end date rather than using today, so two people
  running a week apart get comparable files.
- Call the public library once -- `kaxanuk-data-curator`, already installed by `uv sync` from
  `pyproject.toml`, imported as `kaxanuk.data_curator`.  It loops over the identifiers, skips one
  that fails and says why, and writes `<identifier>.csv` for each.
- Point its output at `Data/Curator/Time_Series/`.  The library's default folder is `Output/`;
  here every stage has one home, and this is the Curator's.

Two groups ride along in the same folder although they are not in the seed: a cash proxy, because
a book that goes to cash has to hold a real priced instrument, and the benchmarks the strategy is
reported against.  The backtest engine prices everything from one directory, so a benchmark filed
anywhere else is a benchmark it cannot price.  Neither enters the cross-section, because
`Data/refinery.py` takes membership from the seed.

Three adjustment families arrive from the provider and each does a different job.  Carry all
three: an unused column costs bytes, a missing one costs a refetch of every identifier.

    unadjusted            recovers the split and dividend ratios; commission is charged on it
    split-adjusted        traded value, which is liquidity in today's share terms
    dividend-and-split    the total-return series a signal and the backtest P&L run on

Two folders beside the time series are drop zones, not outputs: `Benchmarks/` for an index's daily
holdings and returns, `Factors/` for a factor model's returns.  No price provider sells them;
attribution reads them; steps 1 to 5 run without them.

Credentials come from `Config/.env` and are never printed -- not into a log line, a notebook
output or a commit.  An exposed key is rotated, not edited out.

It produces `Data/Curator/Time_Series/<identifier>.csv`, `m_*` plus `c_*`, read by
`Universe/universe.ipynb` and `Data/refinery.py`.

It prevents beautiful results that came from broken inputs -- and a dataset nobody else can
rebuild.
"""

# --- example: begin ---

import csv
import datetime
import importlib.util
import logging
import os
import pathlib
import sys
import types

import pandas

import kaxanuk.data_curator
import kaxanuk.data_curator.data_blocks.market_daily
import kaxanuk.data_curator.data_providers
import kaxanuk.data_curator.entities
import kaxanuk.data_curator.output_handlers

__all__ = [
    "download_identifier",
    "extend_history",
    "load_custom_calculations",
    "main",
    "read_identifiers",
    "read_provider_key",
    "stage_index_price_series",
]

# The benchmark the book is reported against, and a short-Treasury proxy for the cash it holds when
# fewer than thirty stocks qualify.  They ride in the same folder as the universe because the
# backtest engine prices every identifier from one directory; neither enters the cross-section,
# because the refinery takes membership from the seed and neither is in it.
BENCHMARK_AND_CASH_IDENTIFIERS = (
    "SHY",
    "SPY",
)
CUSTOM_CALCULATIONS_PATH = pathlib.Path(__file__).parent / "Curator" / "custom_calculations.py"
# The provider answers at most this many rows per request, so a longer history arrives in windows.
# The earlier window overlaps the one already on file by enough days for the longest rolling column
# to be warm where the two are joined: a window's own first rows are null by construction, and
# joining them in would put a hole in the middle of the series.
HISTORY_OVERLAP_DAYS = 150
# A file that starts within a fortnight of the window asked for has everything the provider holds:
# the first trading day of a year is never the first of January.
HISTORY_TOLERANCE_DAYS = 14
# Fixed, not `today`, so two people running a week apart get the same files.  It is the last date
# the hand-supplied index holdings cover.
END_DATE = datetime.date(
    2026,
    6,
    1,
)
IDENTIFIER_COLUMN = "main_identifier"
# The index the book is reported against. No price provider sells it, so it arrives by hand as a
# daily return series and is rebuilt here as a level the engine can price like any other file.
INDEX_IDENTIFIER = "KN600"
INDEX_RETURNS_PATH = (
    pathlib.Path(__file__).parent / "Curator" / "Benchmarks" / "KN_US_Equity_Returns.csv"
)
# Prices are the only block this strategy reads, and they also set the calendar every other column
# is aligned to.
MARKET_DATA_BLOCK = kaxanuk.data_curator.data_blocks.market_daily.MarketDailyDataBlock
OUTPUT_DIRECTORY = pathlib.Path(__file__).parent / "Curator" / "Time_Series"
SEED_PATH = pathlib.Path(__file__).parent.parent / "Universe" / "Investable_Universe.csv"
# A year before the backtest starts, so the 200-day average is warm on the first day that counts.
START_DATE = datetime.date(
    2001,
    1,
    1,
)
# All three adjustment families in full.  An unused column costs bytes; a missing one costs a
# refetch of every identifier, because widening this tuple changes every file's header.
OUTPUT_COLUMNS = (
    "m_date",
    "m_open",
    "m_high",
    "m_low",
    "m_close",
    "m_vwap",
    "m_volume",
    "m_open_split_adjusted",
    "m_high_split_adjusted",
    "m_low_split_adjusted",
    "m_close_split_adjusted",
    "m_vwap_split_adjusted",
    "m_volume_split_adjusted",
    "m_open_dividend_and_split_adjusted",
    "m_high_dividend_and_split_adjusted",
    "m_low_dividend_and_split_adjusted",
    "m_close_dividend_and_split_adjusted",
    "m_vwap_dividend_and_split_adjusted",
    "m_volume_dividend_and_split_adjusted",
    "c_split_ratio",
    "c_dividend_and_split_ratio",
    "c_vwap",
    "c_vwap_dividend_and_split_adjusted",
    "c_log_returns_dividend_and_split_adjusted",
    "c_daily_traded_value",
    "c_daily_traded_value_sma_63d",
)


def download_identifier(
    identifier: str,
    custom_calculations: "types.ModuleType",
) -> str:
    """
    Fetch one identifier and say what happened, in one word a caller can count.

    One call per identifier is what makes a long run resumable and keeps one bad ticker from
    costing the whole batch.  A file whose header already matches is left alone; a header that does
    not match is refetched, so the folder can never hold two schemas at once.
    """
    output_path = OUTPUT_DIRECTORY / f"{identifier}.csv"

    if output_path.is_file():
        with output_path.open(encoding="utf-8-sig", newline="") as handle:
            header = next(csv.reader(handle), [])

        if tuple(header) == OUTPUT_COLUMNS:

            return "skipped"

    configuration = kaxanuk.data_curator.entities.Configuration(
        start_date=START_DATE,
        end_date=END_DATE,
        period="quarterly",
        identifiers=(identifier,),
        columns=OUTPUT_COLUMNS,
    )
    provider = kaxanuk.data_curator.data_providers.FinancialModelingPrep(
        api_key=read_provider_key(),
    )
    output_handler = kaxanuk.data_curator.output_handlers.CsvOutput(
        output_base_dir=str(OUTPUT_DIRECTORY),
    )
    kaxanuk.data_curator.main(
        configuration=configuration,
        output_handlers=[output_handler],
        custom_calculation_modules=[custom_calculations],
        data_block_providers={MARKET_DATA_BLOCK: provider},
        master_clock_data_block=MARKET_DATA_BLOCK,
        logger_level=logging.WARNING,
    )

    if output_path.is_file():

        return "downloaded"

    return "missing"


def extend_history(
    identifier: str,
    custom_calculations: "types.ModuleType",
) -> str:
    """
    Fetch the history the row limit cut off, and join it to the file already on disk.

    The earlier window overlaps the existing one, and the overlap is where the two are joined: a
    window's first rows have no history behind them, so its rolling columns are null there, and
    taking the earlier window up to a date it has fully warmed keeps the joined series honest.  A
    security that simply did not exist in 2001 returns nothing, which is an answer rather than a
    failure.
    """
    output_path = OUTPUT_DIRECTORY / f"{identifier}.csv"

    if not output_path.is_file():

        return "missing"

    existing = pandas.read_csv(
        output_path,
        parse_dates=["m_date"],
    )
    earliest = existing["m_date"].min()
    tolerance = datetime.timedelta(days=HISTORY_TOLERANCE_DAYS)

    if earliest.date() <= START_DATE + tolerance:

        return "complete"

    window_end = earliest + datetime.timedelta(days=HISTORY_OVERLAP_DAYS)
    history_directory = OUTPUT_DIRECTORY.parent / "_history"
    history_directory.mkdir(
        parents=True,
        exist_ok=True,
    )
    configuration = kaxanuk.data_curator.entities.Configuration(
        start_date=START_DATE,
        end_date=window_end.date(),
        period="quarterly",
        identifiers=(identifier,),
        columns=OUTPUT_COLUMNS,
    )
    provider = kaxanuk.data_curator.data_providers.FinancialModelingPrep(
        api_key=read_provider_key(),
    )
    output_handler = kaxanuk.data_curator.output_handlers.CsvOutput(
        output_base_dir=str(history_directory),
    )
    kaxanuk.data_curator.main(
        configuration=configuration,
        output_handlers=[output_handler],
        custom_calculation_modules=[custom_calculations],
        data_block_providers={MARKET_DATA_BLOCK: provider},
        master_clock_data_block=MARKET_DATA_BLOCK,
        logger_level=logging.WARNING,
    )
    earlier_path = history_directory / f"{identifier}.csv"

    if not earlier_path.is_file():

        return "no earlier history"

    earlier = pandas.read_csv(
        earlier_path,
        parse_dates=["m_date"],
    )
    earlier_path.unlink()

    if len(earlier) == 0 or earlier["m_date"].min() >= earliest:

        return "no earlier history"

    joined = pandas.concat([
        earlier[earlier["m_date"] <= window_end],
        existing[existing["m_date"] > window_end],
    ])
    ordered = joined.sort_values("m_date")
    ordered.to_csv(
        output_path,
        index=False,
    )

    return "extended"


def load_custom_calculations() -> "types.ModuleType":
    """
    Import the `c_*` functions by path, because `Data/` is a folder rather than a package.

    The curator resolves a column to a function by attribute name on this module, so nothing here
    registers anything: defining `c_foo` and asking for the column `c_foo` is the whole contract.
    """
    specification = importlib.util.spec_from_file_location(
        "curator_custom_calculations",
        CUSTOM_CALCULATIONS_PATH,
    )
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)

    return module


def main() -> int:
    """
    Download every identifier in the seed, then the benchmark and the cash proxy, and report.

    Failures are named rather than counted: an identifier the provider does not carry is a hole in
    the panel, and the universe notebook writes it into `Universe/Data_Issues.csv` from here.
    """
    kaxanuk.data_curator.load_config_env()
    OUTPUT_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )
    custom_calculations = load_custom_calculations()
    identifiers = read_identifiers() + BENCHMARK_AND_CASH_IDENTIFIERS
    outcomes = {
        "downloaded": 0,
        "missing": 0,
        "skipped": 0,
    }
    missing_identifiers = []

    for position, identifier in enumerate(identifiers, start=1):
        outcome = download_identifier(
            identifier,
            custom_calculations,
        )
        outcomes[outcome] += 1

        if outcome == "missing":
            missing_identifiers.append(identifier)

        if position % 25 == 0 or position == len(identifiers):
            print(f"{position}/{len(identifiers)}: {outcomes}", flush=True)

    if len(missing_identifiers) > 0:
        names = ", ".join(missing_identifiers)
        print(f"no data for {len(missing_identifiers)}: {names}")

    # Second pass: the provider's row limit truncates a long history, so whatever it cut off is
    # fetched in an earlier window and joined on.
    extensions = {
        "complete": 0,
        "extended": 0,
        "missing": 0,
        "no earlier history": 0,
    }

    for history_position, history_identifier in enumerate(identifiers, start=1):
        extension = extend_history(
            history_identifier,
            custom_calculations,
        )
        extensions[extension] += 1

        if history_position % 25 == 0 or history_position == len(identifiers):
            print(f"history {history_position}/{len(identifiers)}: {extensions}", flush=True)

    index_path = stage_index_price_series()
    print(f"staged the index as {index_path.name}, rebuilt from its own daily returns")

    return 0


def read_identifiers() -> tuple[str, ...]:
    """
    Read the seed, which is the authority on what exists and therefore on what is downloaded.

    Reading it here rather than reading the security master keeps this runnable before the universe
    notebook has ever run -- and that notebook needs these files to profile.
    """
    with SEED_PATH.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        identifiers = [
            row[IDENTIFIER_COLUMN].strip()
            for row in reader
            if row.get(IDENTIFIER_COLUMN, "").strip()
        ]

    if len(identifiers) == 0:
        message = f"{SEED_PATH} has no rows: nothing to download"

        raise ValueError(message)

    return tuple(dict.fromkeys(identifiers))


def read_provider_key() -> str:
    """
    Take the provider key from the environment `load_config_env` filled, by name only.

    It is never printed, logged or returned anywhere else: an exposed key is rotated, not edited
    out of a commit.
    """
    api_key = os.environ.get("KNDC_API_KEY_FMP", "")

    if api_key == "":
        message = "KNDC_API_KEY_FMP is empty; fill it in Config/.env"

        raise RuntimeError(message)

    return api_key


def stage_index_price_series() -> "pathlib.Path":
    """
    Rebuild the index as a price level from its own daily returns, beside the securities.

    The backtest engine resolves every identifier against one market-data directory, so a benchmark
    filed anywhere else is a benchmark it cannot price.  The level starts at 100 and means nothing
    on its own: only its returns are ever read.  A benchmark is never traded, so the two VWAP
    columns the engine asks for by name are the level itself.
    """
    returns = pandas.read_csv(
        INDEX_RETURNS_PATH,
        parse_dates=["date_column"],
        dayfirst=True,
    )
    return_column = returns.columns[1]
    ordered = returns.sort_values("date_column")
    growth = 1 + ordered[return_column].fillna(0.0)
    level = growth.cumprod() * 100
    staged = pandas.DataFrame({
        "m_date": ordered["date_column"].dt.date,
        "m_close": level,
        "m_close_dividend_and_split_adjusted": level,
        "c_vwap": level,
        "c_vwap_dividend_and_split_adjusted": level,
    })
    path = OUTPUT_DIRECTORY / f"{INDEX_IDENTIFIER}.csv"
    staged.to_csv(
        path,
        index=False,
    )

    return path


if __name__ == "__main__":
    sys.exit(main())

# --- example: end ---
