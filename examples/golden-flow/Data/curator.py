"""
Data Curator -- step 3 of 8, block 1 of 3.  The only file in this repository that downloads time
series from a data provider.  `Universe/universe.ipynb` asks the same provider what each security
*is* -- name, type, exchange, currency, inception -- and caches that payload in
`Universe/Provider_Cache/`.  A strategy's seed builder, where it has one, may ask it which
identifier each listing is priced under; nothing else talks to a provider.

In plain words: you describe the data you want -- provider, identifiers, dates and columns -- and
the KaxaNuk Data Curator fetches it, aligns the calendar, handles splits and dividends, and writes
one file per identifier, the same way every run.

Runs first.  Nothing has to exist before it except `Universe/Investable_Universe.csv` and a
provider key in `Config/.env`.  `Universe/universe.ipynb` profiles what this writes.

What is expected here is a short driver, not a framework:

- Read the identifiers from `Universe/Investable_Universe.csv`, column `main_identifier`, the
  identifier the experiment's provider prices each security under.  The seed is the authority on
  what exists, so it drives the download.
- Build one Data Curator configuration: the date window, those identifiers, and the output columns
  -- the provider's `m_*` columns plus the `c_*` columns defined in
  `Data/Curator/custom_calculations.py`.  Fix the end date rather than using today, so two people
  running a week apart get comparable files.
- Take a later end date as an argument, `--end-date`, for the one caller that needs today's data:
  `Paper_Trading/daily_update.py`.  A refresh refetches each file whole, because a fresh pull
  rebases every adjusted column from the present, and remembers the date each file was fetched
  through, so a run that stops half way resumes where it stopped.
- Call the public library once per identifier -- `kaxanuk-data-curator`, already installed by
  `uv sync` from `pyproject.toml`, imported as `kaxanuk.data_curator` -- so each name gets its own
  answer and its own `<identifier>.csv`.
- Record the provider's answer for each name.  A name it does not carry is then told from one it
  refused today -- a rate limit, a timeout -- and only the second is asked again.
- Point its output at `Data/Curator/Time_Series/`.  The library's default folder is `Output/`;
  here every stage has one home, and this is the Curator's.
- A provider's history can stop where its coverage does: a name that left the market years ago may
  be missing from it altogether.  Fetch such names from a second provider that carries them, into
  the same files and columns, and say in the strategy's documents which names came from where and
  how any column the second provider lacks was filled.  Or leave them out and publish what that
  costs, the survivorship cost, beside every result.  Either is a decision the journal records.

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

An index's daily holdings and returns, and a factor model's returns, are not sold by any price
provider: they arrive from KaxaNuk's Analytics Factory, and `Data/hand_supplied.py` reads them --
in place, from the folder `KN_ANALYTICS_PATH` names, or from the drop zones `Benchmarks/` and
`Factors/` beside the time series.  Without them this script still downloads every price and says
the index was not staged; the notebooks stop where they first read it.

Credentials come from `Config/.env` and are never printed -- not into a log line, a notebook
output or a commit.  An exposed key is rotated, not edited out.

It produces `Data/Curator/Time_Series/<identifier>.csv`, `m_*` plus `c_*`, read by
`Universe/universe.ipynb` and `Data/refinery.py`, and in `Data/Curator/` the provider's last
answer for each name.

It prevents beautiful results that came from broken inputs -- and a dataset nobody else can
rebuild.
"""

# --- example: begin ---

# Golden Flow downloads from FMP alone, Experiment 1's provider: the seed's members, `BIL` and
# `SPY`, and the KN US Equity Core rebuilt as a price level from the Analytics Factory's
# returns file, staged for the engine as `KN_US_Equity_Core`.  A name FMP does not carry is
# told from one it refused tonight, and `fetch_outcomes.json` keeps the last answer for the
# universe notebook.

import argparse
import csv
import datetime
import importlib.util
import json
import logging
import os
import pathlib
import socket
import sys
import time
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
    "load_hand_supplied",
    "main",
    "read_fetched_through",
    "read_identifiers",
    "read_provider_key",
    "stage_index_price_series",
]

# A Treasury-bill fund for the cash the book holds when its bounds cannot place every dollar, and
# the exchange-traded benchmark the book is reported against beside the index.  They ride in the
# same folder as the universe because the backtest engine prices every identifier from one
# directory; neither enters the cross-section, because the refinery takes membership from the seed
# and neither is in it.
BENCHMARK_AND_CASH_IDENTIFIERS = (
    "BIL",
    "SPY",
)
CUSTOM_CALCULATIONS_PATH = pathlib.Path(__file__).parent / "Curator" / "custom_calculations.py"
# An identifier the provider refused is asked again, twice, after a pause: the stalls seen on this
# machine were a DNS failure followed by a request that never returned, and a rate limit answers
# the same way as a missing name unless it is read.
DOWNLOAD_ATTEMPTS = 3
# Fixed, not `today`, so two people running a week apart get the same files.  It is the last date
# of the experiment's window.  `--end-date` moves it for the one fetch that also serves the paper
# book, and for every paper-trading refresh after it.
END_DATE = datetime.date(
    2026,
    6,
    1,
)
# The date each file was last fetched through, so a refresh knows what it has already done.
FETCHED_THROUGH_PATH = pathlib.Path(__file__).parent / "Curator" / "fetched_through.json"
# The provider's last word on each name: `downloaded`, `not carried`, or what refused it.
FETCH_OUTCOMES_PATH = pathlib.Path(__file__).parent / "Curator" / "fetch_outcomes.json"
HAND_SUPPLIED_PATH = pathlib.Path(__file__).parent / "hand_supplied.py"
# The provider answers at most this many rows per request, so a longer history arrives in windows.
# The earlier window overlaps the one already on file by enough days for the longest rolling column
# to be warm where the two are joined: a window's own first rows are null by construction, and
# joining them in would put a hole in the middle of the series.
HISTORY_OVERLAP_DAYS = 150
# A file that starts within a fortnight of the window asked for has everything the provider holds:
# the first trading day of a year is never the first of January.
HISTORY_TOLERANCE_DAYS = 14
IDENTIFIER_COLUMN = "main_identifier"
# The index the book is reported against, under the name the engine prices it by. No price
# provider sells it, so it arrives by hand as a daily return series and is rebuilt here as a level
# the engine can price like any other file.
INDEX_IDENTIFIER = "KN_US_Equity_Core"
# Prices are the only block this strategy reads, and they also set the calendar every other column
# is aligned to.
MARKET_DATA_BLOCK = kaxanuk.data_curator.data_blocks.market_daily.MarketDailyDataBlock
# The words the library logs when FMP says it has nothing for a name, as opposed to refusing.
NOT_CARRIED_PHRASES = (
    "No data found",
    "returned no data",
)
OUTPUT_DIRECTORY = pathlib.Path(__file__).parent / "Curator" / "Time_Series"
# The outcomes that leave a name without a file.
UNANSWERED_OUTCOMES = (
    "not carried",
    "refused",
    "unusable",
)
# The words the library logs when FMP answered with rows it could not assemble into a series: an
# answer about the data, not the moment, so asking again changes nothing.
UNUSABLE_PHRASES = ("during data assembly",)
# The library opens its connections with no timeout of its own, so one that hangs would hang the
# run; this makes it raise instead, and the attempt is made again.
REQUEST_TIMEOUT_SECONDS = 120
RETRY_PAUSE_SECONDS = 60
SEED_PATH = pathlib.Path(__file__).parent.parent / "Universe" / "Investable_Universe.csv"
# Fourteen years before the window opens, so every average is warm on the first day that counts and
# the analyzer has a long history to screen.
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


class _MessageCollector(logging.Handler):
    """
    Keep what the library logs at error level or above during one call, to read why it failed.
    """

    def __init__(self) -> None:
        """
        Start with no messages, at the error level.
        """
        super().__init__(level=logging.ERROR)
        self.messages = []

    def emit(
        self,
        record: "logging.LogRecord",
    ) -> None:
        """
        Keep the formatted message.
        """
        self.messages.append(record.getMessage())


def download_identifier(
    identifier: str,
    custom_calculations: "types.ModuleType",
    end_date: "datetime.date",
    fetched_through: dict[str, str],
) -> str:
    """
    Fetch one identifier through the end date and say what happened, in words a caller counts.

    One call per identifier is what makes a long run resumable and keeps one bad ticker from
    costing the whole batch.  A file with the right header already fetched through this end date
    is left alone.  A header that does not match is refetched, so the folder can never hold two
    schemas at once.  The answer is `downloaded`, `skipped`, `not carried` when FMP said it has no
    data for the name, `unusable` when it answered with rows the library could not assemble, or
    `refused` when every attempt failed for another reason.
    """
    output_path = OUTPUT_DIRECTORY / f"{identifier}.csv"

    if output_path.is_file():
        with output_path.open(encoding="utf-8-sig", newline="") as handle:
            header = next(csv.reader(handle), [])

        remembered = fetched_through.get(
            identifier,
            "",
        )

        if tuple(header) == OUTPUT_COLUMNS and remembered == end_date.isoformat():

            return "skipped"

    configuration = kaxanuk.data_curator.entities.Configuration(
        start_date=START_DATE,
        end_date=end_date,
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
    before = output_path.stat().st_mtime if output_path.is_file() else None

    for attempt in range(1, DOWNLOAD_ATTEMPTS + 1):
        outcome = _fetch_once(
            configuration,
            output_handler,
            provider,
            custom_calculations,
        )
        written = output_path.is_file() and output_path.stat().st_mtime != before

        if written:
            fetched_through[identifier] = end_date.isoformat()

            return "downloaded"

        if outcome in ("not carried", "unusable"):
            # FMP answered about the name itself: asking again only costs the pause.

            return outcome

        print(f"{identifier}: attempt {attempt} failed ({outcome})", flush=True)

        if attempt < DOWNLOAD_ATTEMPTS:
            time.sleep(RETRY_PAUSE_SECONDS)

    return "refused"


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
    _fetch_once(
        configuration,
        output_handler,
        provider,
        custom_calculations,
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


def load_hand_supplied() -> "types.ModuleType":
    """
    Import the reader of the Analytics Factory's files by path, for the same reason.
    """
    specification = importlib.util.spec_from_file_location(
        "hand_supplied",
        HAND_SUPPLIED_PATH,
    )
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)

    return module


def main() -> int:
    """
    Download every identifier in the seed, then the benchmark and the cash proxy, and report.

    Failures are named rather than counted: an identifier the provider does not carry is a hole in
    the panel, and the universe notebook writes it into `Universe/Data_Issues.csv` from the
    outcomes this writes.  The history pass runs only for what this run fetched, so a resumed
    refresh does not ask again for history it already joined.
    """
    parser = argparse.ArgumentParser(description="Download the seed's time series.")
    parser.add_argument(
        "--end-date",
        default=END_DATE.isoformat(),
        help="the last date to fetch through, ISO; the experiment's end date when omitted",
    )
    parser.add_argument(
        "--identifiers",
        default="",
        help="a comma-separated subset of the seed; the whole seed when omitted",
    )
    arguments = parser.parse_args()
    end_date = datetime.date.fromisoformat(arguments.end_date)
    kaxanuk.data_curator.load_config_env()
    socket.setdefaulttimeout(REQUEST_TIMEOUT_SECONDS)
    OUTPUT_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )
    custom_calculations = load_custom_calculations()
    requested = tuple(
        identifier.strip()
        for identifier in arguments.identifiers.split(",")
        if identifier.strip()
    )
    everything = read_identifiers() + BENCHMARK_AND_CASH_IDENTIFIERS
    identifiers = requested if len(requested) > 0 else everything
    fetched_through = read_fetched_through()
    fetch_outcomes = _read_fetch_outcomes()
    outcomes = {
        "downloaded": 0,
        "not carried": 0,
        "refused": 0,
        "skipped": 0,
        "unusable": 0,
    }
    downloaded_identifiers = []

    for position, identifier in enumerate(identifiers, start=1):
        outcome = download_identifier(
            identifier,
            custom_calculations,
            end_date,
            fetched_through,
        )
        outcomes[outcome] += 1

        if outcome != "skipped":
            fetch_outcomes[identifier] = outcome
            _write_json(
                FETCH_OUTCOMES_PATH,
                fetch_outcomes,
            )

        if outcome == "downloaded":
            downloaded_identifiers.append(identifier)
            _write_json(
                FETCHED_THROUGH_PATH,
                fetched_through,
            )

        if position % 25 == 0 or position == len(identifiers):
            print(f"{position}/{len(identifiers)} through {end_date}: {outcomes}", flush=True)

    unanswered = [
        identifier
        for identifier in identifiers
        if fetch_outcomes.get(identifier) in UNANSWERED_OUTCOMES
    ]

    if len(unanswered) > 0:
        names = ", ".join(
            f"{identifier} ({fetch_outcomes[identifier]})"
            for identifier in unanswered
        )
        print(f"no file for {len(unanswered)}: {names}")

    # Second pass: the provider's row limit truncates a long history, so whatever it cut off is
    # fetched in an earlier window and joined on.
    extensions = {
        "complete": 0,
        "extended": 0,
        "missing": 0,
        "no earlier history": 0,
    }

    for history_position, history_identifier in enumerate(downloaded_identifiers, start=1):
        extension = extend_history(
            history_identifier,
            custom_calculations,
        )
        extensions[extension] += 1

        if history_position % 25 == 0 or history_position == len(downloaded_identifiers):
            print(
                f"history {history_position}/{len(downloaded_identifiers)}: {extensions}",
                flush=True,
            )

    # The index is KaxaNuk's own and arrives by hand, so a copy without it is told what it lacks
    # rather than handed a traceback after every price has downloaded.
    hand_supplied = load_hand_supplied()
    missing_inputs = hand_supplied.report_missing()
    returns_missing = [
        line
        for line in missing_inputs
        if "index returns" in line
    ]

    if len(returns_missing) == 0:
        index_path = stage_index_price_series(hand_supplied)
        print(f"staged the index as {index_path.name}, rebuilt from its own daily returns")
    else:
        print(f"{INDEX_IDENTIFIER} not staged: {returns_missing[0]}")

    return 0


def read_fetched_through() -> dict[str, str]:
    """
    The date each file was last fetched through, empty before the first refresh.
    """
    if not FETCHED_THROUGH_PATH.is_file():

        return {}

    return json.loads(FETCHED_THROUGH_PATH.read_text(encoding="utf-8"))


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


def stage_index_price_series(
    hand_supplied: "types.ModuleType",
) -> "pathlib.Path":
    """
    Rebuild the index as a price level from its own daily returns, beside the securities.

    The backtest engine resolves every identifier against one market-data directory, so a benchmark
    filed anywhere else is a benchmark it cannot price.  The level starts at 100 and means nothing
    on its own: only its returns are ever read.  A benchmark is never traded, so the two VWAP
    columns the engine asks for by name are the level itself.
    """
    returns = hand_supplied.read_benchmark_returns()
    growth = 1 + returns.fillna(0.0)
    level = growth.cumprod() * 100
    staged = pandas.DataFrame({
        "m_date": returns.index.date,
        "m_close": level.to_numpy(),
        "m_close_dividend_and_split_adjusted": level.to_numpy(),
        "c_vwap": level.to_numpy(),
        "c_vwap_dividend_and_split_adjusted": level.to_numpy(),
    })
    path = OUTPUT_DIRECTORY / f"{INDEX_IDENTIFIER}.csv"
    staged.to_csv(
        path,
        index=False,
    )

    return path


def _fetch_once(
    configuration: object,
    output_handler: object,
    provider: object,
    custom_calculations: "types.ModuleType",
) -> str:
    """
    One call to the library: `answered`, `not carried`, `unusable`, or why it was refused.

    The library logs a provider's refusal and returns normally, so the call is read through what it
    logged: FMP's "no data" is an answer about the name, while a rate limit or a server error is an
    answer about the moment, and is worth asking again.
    """
    collector = _MessageCollector()
    library_logger = logging.getLogger("kaxanuk")
    library_logger.addHandler(collector)

    try:
        kaxanuk.data_curator.main(
            configuration=configuration,
            output_handlers=[output_handler],
            custom_calculation_modules=[custom_calculations],
            data_block_providers={MARKET_DATA_BLOCK: provider},
            master_clock_data_block=MARKET_DATA_BLOCK,
            logger_level=logging.WARNING,
        )
    except OSError as error:

        return type(error).__name__
    finally:
        library_logger.removeHandler(collector)

    logged = " ".join(collector.messages)
    not_carried = any(
        phrase in logged
        for phrase in NOT_CARRIED_PHRASES
    )

    unusable = any(
        phrase in logged
        for phrase in UNUSABLE_PHRASES
    )

    if not_carried:

        return "not carried"

    if unusable:

        return "unusable"

    if logged == "":

        return "answered"

    return logged[:160]


def _read_fetch_outcomes() -> dict[str, str]:
    """
    The provider's last word on each name, empty before the first run.
    """
    if not FETCH_OUTCOMES_PATH.is_file():

        return {}

    return json.loads(FETCH_OUTCOMES_PATH.read_text(encoding="utf-8"))


def _write_json(
    path: "pathlib.Path",
    content: dict[str, str],
) -> None:
    """
    Write a small record as sorted JSON, so a rerun's diff reads as what changed.
    """
    text = json.dumps(
        content,
        indent=1,
        sort_keys=True,
    )
    path.write_text(
        text,
        encoding="utf-8",
    )


if __name__ == "__main__":
    sys.exit(main())

# --- example: end ---
