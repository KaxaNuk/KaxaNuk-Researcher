"""
The hand-supplied inputs -- step 3 of 8, beside the Curator.  The index a book is reported against
and the factor model attribution reads are not sold by any price provider: they arrive as files
from the desk that builds them, and this module is the one place that reads them.

In plain words: set `KN_ANALYTICS_PATH` in `Config/.env` to the desk's folder and the files are
read where they are, in the desk's own names and headers -- nobody renames or re-heads a file.
Leave it empty, and the same files, dropped unchanged into `Data/Curator/Benchmarks/` and
`Data/Curator/Factors/`, are read from there.

The desk's layout, its folders read under the Analytics Factory's names first and under the
older ones, `Benchmarks/` and `Factors/`, where those are absent.  The files keep the same names and
headers in both, and the drop-in folders keep the older names:

    Benchmark Portfolios/KN_US_Equity_Benchmark_Holdings.csv
        m_date, ISO dates; one column per listing, its weight in the index that day
    Benchmark Portfolios/KN_US_Equity_Benchmark_Returns.csv
        m_date, day-first dates; kn600, the index's daily return
    Factor Models/<Name>.csv
        dates down in an unnamed first column, ISO; listings across

Four of the factor files are the model's own series rather than factors, and the attribution
library knows them by reserved lower-case names: `Market.csv` is `f_market`, and `Idyo_Returns`,
`Total_Excess_Returns` and `Total_Factor_Returns` become `f_idyo_returns`,
`f_total_excess_returns` and `f_total_factor_returns`.  Every other file is a factor named by its
file name in lower case.

`Data/curator.py` rebuilds the index as a price level from its returns; the universe notebook and
each experiment read the holdings for point-in-time membership; and
`Experiments/attribution_analysis.py` reads all three.  Each loads this file by path, because
`Data/` is a folder rather than a package.

It prevents a renamed copy drifting from the desk's file, and a date read in the wrong order.
"""

# --- example: begin ---

import os
import pathlib

import dotenv
import pandas

__all__ = [
    "ANALYTICS_PATH_KEY",
    "BENCHMARK_HOLDINGS_NAME",
    "BENCHMARK_RETURNS_NAME",
    "LIBRARY_DATE_HEADER",
    "benchmark_directory",
    "factor_directory",
    "read_benchmark_holdings",
    "read_benchmark_returns",
    "read_factor_returns",
    "report_missing",
]

ANALYTICS_PATH_KEY = "KN_ANALYTICS_PATH"
# The desk's folder names, newest first: the Analytics Factory's layout, then the one it replaced.
BENCHMARK_FOLDER_NAMES = (
    "Benchmark Portfolios",
    "Benchmarks",
)
BENCHMARK_HOLDINGS_NAME = "KN_US_Equity_Benchmark_Holdings.csv"
BENCHMARK_RETURNS_NAME = "KN_US_Equity_Benchmark_Returns.csv"
DROP_IN_DIRECTORY = pathlib.Path(__file__).parent / "Curator"
ENVIRONMENT_PATH = pathlib.Path(__file__).parent.parent / "Config" / ".env"
FACTOR_FOLDER_NAMES = (
    "Factor Models",
    "Factors",
)

# The desk writes `m_date` in both benchmark files, ISO in one and day first in the other; the
# attribution library wants every frame's dates under one header of its own.
DESK_DATE_HEADER = "m_date"
FACTOR_DATE_FORMAT = "%Y-%m-%d"
HOLDINGS_DATE_FORMAT = "%Y-%m-%d"
LIBRARY_DATE_HEADER = "date_column"
RETURNS_DATE_FORMAT = "%d/%m/%Y"

# The model's own series, known to the library by these names and dropped from the percentage
# decomposition; a factor file is otherwise named by its file name in lower case.
RESERVED_FACTOR_NAMES = {
    "Idyo_Returns": "f_idyo_returns",
    "Market": "f_market",
    "Total_Excess_Returns": "f_total_excess_returns",
    "Total_Factor_Returns": "f_total_factor_returns",
}


def benchmark_directory() -> "pathlib.Path":
    """
    The folder the index's two files are read from: the desk's, or the drop-in beside the Curator.
    """
    analytics = _analytics_directory()

    if analytics is None:

        return DROP_IN_DIRECTORY / "Benchmarks"

    return _first_existing(
        analytics,
        BENCHMARK_FOLDER_NAMES,
    )


def factor_directory() -> "pathlib.Path":
    """
    The folder the factor model's files are read from: the desk's, or the drop-in.
    """
    analytics = _analytics_directory()

    if analytics is None:

        return DROP_IN_DIRECTORY / "Factors"

    return _first_existing(
        analytics,
        FACTOR_FOLDER_NAMES,
    )


def read_benchmark_holdings() -> "pandas.DataFrame":
    """
    The index's daily holdings: dates down, listings across, each cell a weight.

    A listing absent on a date weighs zero, never null, because both the membership rule and the
    attribution library read a missing weight as a hole rather than as a name that was not held.
    """
    path = benchmark_directory() / BENCHMARK_HOLDINGS_NAME
    holdings = pandas.read_csv(path)
    dates = pandas.to_datetime(
        holdings[DESK_DATE_HEADER],
        format=HOLDINGS_DATE_FORMAT,
    )
    weights = holdings.drop(columns=[DESK_DATE_HEADER])
    weights.index = pandas.DatetimeIndex(
        dates,
        name=LIBRARY_DATE_HEADER,
    )
    ordered = weights.sort_index()

    return ordered.fillna(0.0)


def read_benchmark_returns() -> "pandas.Series":
    """
    The index's daily return, in date order, under the index's own name.

    The file writes its dates day first, so they are parsed with the format stated, never guessed:
    the fourth of January and the first of April are the same string read two ways.
    """
    path = benchmark_directory() / BENCHMARK_RETURNS_NAME
    returns = pandas.read_csv(path)
    dates = pandas.to_datetime(
        returns[DESK_DATE_HEADER],
        format=RETURNS_DATE_FORMAT,
    )
    return_column = returns.columns[1]
    series = pandas.Series(
        returns[return_column].to_numpy(),
        index=pandas.DatetimeIndex(
            dates,
            name=LIBRARY_DATE_HEADER,
        ),
        name=return_column,
    )

    return series.sort_index()


def read_factor_returns() -> dict[str, "pandas.DataFrame"]:
    """
    Every factor file in the folder, each one named for the attribution library.

    Every file is read as a factor, so a stray file is a stray factor.  The date column arrives
    unnamed and as strings; a string date aligns with nothing and the factor attribution comes back
    with zero rows rather than an error, so it is parsed here.
    """
    factors = {}
    directory = factor_directory()

    for path in sorted(directory.glob("*.csv")):
        name = RESERVED_FACTOR_NAMES.get(
            path.stem,
            path.stem.lower(),
        )
        frame = pandas.read_csv(path)
        dates = pandas.to_datetime(
            frame[frame.columns[0]],
            format=FACTOR_DATE_FORMAT,
        )
        values = frame.drop(columns=[frame.columns[0]])
        values.index = pandas.DatetimeIndex(
            dates,
            name=LIBRARY_DATE_HEADER,
        )
        factors[name] = values

    return factors


def report_missing() -> list[str]:
    """
    Say which of the hand-supplied files is absent, in one pass, before anything is loaded.
    """
    missing = []
    holdings_path = benchmark_directory() / BENCHMARK_HOLDINGS_NAME
    returns_path = benchmark_directory() / BENCHMARK_RETURNS_NAME
    directory = factor_directory()
    factor_files = sorted(directory.glob("*.csv"))

    if not holdings_path.is_file():
        missing.append(f"no index holdings at {holdings_path}")

    if not returns_path.is_file():
        missing.append(f"no index returns at {returns_path}")

    if len(factor_files) == 0:
        missing.append(f"no factor files in {directory}")

    return missing


def _analytics_directory() -> "pathlib.Path | None":
    """
    The desk's folder when `KN_ANALYTICS_PATH` names one, taken from the environment first.

    `Config/.env` is loaded without overriding what the environment already holds, so a scheduler
    that sets the variable wins.  A path that does not exist is an error, not a fallback: reading
    the drop-in folder when the desk's was meant is how two sets of numbers start to circulate.
    """
    dotenv.load_dotenv(
        ENVIRONMENT_PATH,
        override=False,
    )
    configured = os.environ.get(ANALYTICS_PATH_KEY, "").strip()

    if configured == "":

        return None

    directory = pathlib.Path(configured)

    if not directory.is_dir():
        message = f"{ANALYTICS_PATH_KEY} names {directory}, which is not a folder"

        raise FileNotFoundError(message)

    return directory


def _first_existing(
    parent: "pathlib.Path",
    names: tuple[str, ...],
) -> "pathlib.Path":
    """
    The first of the names that is a folder under the parent, or the first name when none is.

    The desk renamed its folders once; reading both layouts keeps a strategy running across the
    change, and a missing folder is reported under the newest name.
    """
    for name in names:
        candidate = parent / name

        if candidate.is_dir():

            return candidate

    return parent / names[0]


# --- example: end ---
