"""
Attribution analysis -- step 6 of 8, the fourth shared module.  Shapes what the KaxaNuk Attribution
Analysis library needs, and says what is missing before it tries.

In plain words: which part of the return did you actually earn?

Runs inside an experiment notebook, section 5, after the backtest.

What is expected here:

- Say what is present.  The library needs four inputs: an index's daily holdings and its daily
  returns in `Data/Curator/Benchmarks/`, one or more factor-return files in
  `Data/Curator/Factors/`, and the book from step 5.  Check for them first and report the gap in a
  sentence, so a clone with no licence and no index files pays nothing to find out.
- Take the book as a daily series, from `Backtest/`, never from `Portfolio/portfolio_weights.csv`.
  The library rejects a weight file that is not daily once it spans a year, and the rebalance-date
  file the engine read is exactly what it refuses.  The book it attributes is the one the engine
  held each trading day, drift and the cash proxy included; the benchmark's holdings follow the
  same rule.
- Widen the book to the benchmark before handing it over: every benchmark constituent the book
  does not hold, added at zero weight, each with its own price series.  The library prices only
  the securities named in the book, and the first cut computes the benchmark's return from those
  prices alone -- the index's own return series is never one of its inputs.  A book that names only
  what it holds is compared against the fraction of the index it happens to own, and the
  difference is reported as alpha, most of it filed under interaction, where nobody looks.  Drop
  the engine's benchmark column on the way, which it returns at zero, and keep the cash position.
- Shape the hand-supplied files into what the library's loader accepts, which is decided by **one
  cell**: the first header.  `Ticker` means securities down and dates across; `date_column` means
  dates down and securities across.  Anything else -- `date`, `m_date`, the name a provider happened
  to use -- raises before a number is read.  The same rule governs the book, the benchmark's
  holdings and the benchmark's return series, and none of them may carry nulls.  That is why the
  shaping lives here and not in a notebook.
- Say what the factor directory has to look like, because every entry in it is read as a factor
  file: one CSV per factor, its name taken from the file name up to the first dot, a date column
  first -- its header may be empty -- and one column per security after it.  Four names are
  reserved, matched exactly and in lower case, and dropped from the percentage decomposition:
  `f_market`, `f_total_factor_returns`, `f_total_excess_returns` and `f_idyo_returns`.  A file
  capitalised differently is attributed as an ordinary factor, which is a quiet way to double-count
  the market.
- Name the two output files and the date convention once, so switching to a different index is an
  edit here and no notebook names a file.
- Capture the library's figures.  It shows them and returns nothing, so this module has to catch
  them on the way past and write them to `Attribution/`, then leave the plotting state as it found
  it.

Expect two methodologies and a third pass, all reported.  Brinson-Fachler splits active return
into allocation, selection and interaction -- the lever that moved.  The factor model splits
excess return into compensated factor tilts and idiosyncratic alpha -- what was paid for, on
purpose or by accident.  Then Brinson-Fachler again on the residual, which says whether the
Sharpe survives once the factor turns.  Expect the answer to be partial -- an absolute rule is
close to invisible to a factor model built on relative factors -- and treat that as a finding.
The follow-ups are counterfactual books the engine can already price.  `AGENTS.md` has the
reasoning.

It produces `Attribution/` -- the figures and the two decompositions -- for `FINDINGS_N.md`, and
the answer to graduation criterion 2.

It prevents selling factor beta as if it were alpha, and a run that stops at its first file because
a header carries the name a provider gave it rather than the one the loader expects.
"""

# --- example: begin ---

import importlib.util
import pathlib

import pandas
import pyarrow

__all__ = [
    "BENCHMARK_HOLDINGS_PATH",
    "BENCHMARK_RETURNS_PATH",
    "DATE_HEADER",
    "FACTOR_DIRECTORY",
    "LIBRARY_INSTALLED",
    "RESERVED_FACTOR_NAMES",
    "load_asset_returns",
    "load_benchmark_weights",
    "load_factor_returns",
    "report_missing_inputs",
    "to_arrow",
    "widen_to_benchmark",
]

BENCHMARK_HOLDINGS_PATH = (
    pathlib.Path(__file__).parent.parent
    / "Data" / "Curator" / "Benchmarks" / "KN_US_Equity_Benchmark.csv"
)
BENCHMARK_RETURNS_PATH = (
    pathlib.Path(__file__).parent.parent
    / "Data" / "Curator" / "Benchmarks" / "KN_US_Equity_Returns.csv"
)
# The one cell that decides whether a file loads: dates down, securities across.  `date`, `m_date`
# or whatever a provider used raises before a number is read.
DATE_HEADER = "date_column"
FACTOR_DIRECTORY = pathlib.Path(__file__).parent.parent / "Data" / "Curator" / "Factors"
LIBRARY_INSTALLED = importlib.util.find_spec("kaxanuk.attribution_analysis") is not None
# Matched exactly, in lower case, and dropped from the percentage decomposition.  A file
# capitalised differently is attributed as an ordinary factor, which double-counts the market.
RESERVED_FACTOR_NAMES = (
    "f_idyo_returns",
    "f_market",
    "f_total_excess_returns",
    "f_total_factor_returns",
)


def load_asset_returns(
    identifiers: tuple[str, ...],
    dates: "pandas.DatetimeIndex",
) -> "pandas.DataFrame":
    """
    Daily returns for every security either book names, on the book's own dates.

    Read by identifier from the Curator's folder rather than from the refined panel, because both
    books speak in identifiers here: the benchmark's holdings name listings, and so does the weight
    file the engine read.  A security with no file contributes nothing rather than breaking the
    run, and a missing day is a zero return rather than a null, because the library refuses nulls.
    """
    market_data_directory = (
        pathlib.Path(__file__).parent.parent / "Data" / "Curator" / "Time_Series"
    )
    columns = {}

    for identifier in identifiers:
        path = market_data_directory / f"{identifier}.csv"

        if not path.is_file():
            continue

        prices = pandas.read_csv(
            path,
            usecols=["m_date", "m_close_dividend_and_split_adjusted"],
            parse_dates=["m_date"],
            index_col="m_date",
        )["m_close_dividend_and_split_adjusted"]
        on_dates = prices.reindex(dates).ffill()
        columns[identifier] = on_dates.pct_change(fill_method=None)

    returns = pandas.DataFrame(
        columns,
        index=dates,
    )

    return returns.fillna(0.0)


def load_benchmark_weights(
    dates: "pandas.DatetimeIndex",
) -> "pandas.DataFrame":
    """
    Read the index's daily holdings, on the book's own dates, with no nulls left in it.

    The holdings file is the benchmark half of the first cut, and it follows the same header rule
    as the book: a security absent on a date weighs zero, never null.
    """
    holdings = pandas.read_csv(
        BENCHMARK_HOLDINGS_PATH,
        parse_dates=[DATE_HEADER],
        dayfirst=True,
    )
    indexed = holdings.set_index(DATE_HEADER)
    on_dates = indexed.reindex(dates)
    forward_filled = on_dates.ffill()

    return forward_filled.fillna(0.0)


def load_factor_returns() -> dict[str, "pandas.DataFrame"]:
    """
    Read every file in the factor drop zone, each one a factor named by its file name.

    Every entry in the directory is read as a factor, so a stray file is a stray factor.  The four
    reserved names are checked for capitalisation here rather than discovered in a decomposition
    that quietly counted the market twice.
    """
    factors = {}
    miscapitalised = []

    for path in sorted(FACTOR_DIRECTORY.glob("*.csv")):
        name = path.name.split(".")[0]

        if name.lower() in RESERVED_FACTOR_NAMES and name not in RESERVED_FACTOR_NAMES:
            miscapitalised.append(name)

        frame = pandas.read_csv(path)
        # The date column's header is empty in these files, and its values are strings. Every other
        # input to the library carries timestamps, and a string date silently aligns with nothing:
        # the factor attribution comes back with zero rows rather than an error.
        dates = pandas.to_datetime(frame[frame.columns[0]])
        dated = frame.drop(columns=[frame.columns[0]])
        dated.index = dates
        dated.index.name = DATE_HEADER
        factors[name] = dated

    if len(miscapitalised) > 0:
        capitalisation_message = f"reserved factor files must be lower case: {miscapitalised}"

        raise ValueError(capitalisation_message)

    return factors


def report_missing_inputs() -> list[str]:
    """
    Say which of the four inputs is absent, in one pass, before anything is loaded.

    A clone with no licence and no hand-supplied index files should pay one sentence to find that
    out, not a stack trace three cells later.
    """
    missing = []

    if not LIBRARY_INSTALLED:
        missing.append("the KaxaNuk Attribution Analysis library is not installed")

    if not BENCHMARK_HOLDINGS_PATH.is_file():
        missing.append(f"no index holdings at {BENCHMARK_HOLDINGS_PATH}")

    if not BENCHMARK_RETURNS_PATH.is_file():
        missing.append(f"no index returns at {BENCHMARK_RETURNS_PATH}")

    factor_files = sorted(FACTOR_DIRECTORY.glob("*.csv"))

    if len(factor_files) == 0:
        missing.append(f"no factor files in {FACTOR_DIRECTORY}")

    return missing


def to_arrow(
    frame: "pandas.DataFrame",
) -> "pyarrow.Table":
    """
    Hand the library a table whose first column is the date header its loader accepts.

    The conversion lives here so no notebook has to remember which of the two layouts a given input
    takes, or that the header is what decides it.
    """
    dated = frame.reset_index()
    renamed = dated.rename(columns={dated.columns[0]: DATE_HEADER})

    return pyarrow.Table.from_pandas(
        renamed,
        preserve_index=False,
    )


def widen_to_benchmark(
    daily_weights: "pandas.DataFrame",
    benchmark_weights: "pandas.DataFrame",
    benchmark_column: str,
) -> "pandas.DataFrame":
    """
    Add every benchmark constituent the book does not hold, at zero weight.

    The library prices only the securities the book names, and the first cut computes the
    benchmark's return from those prices alone -- the index's own return series is never one of its
    inputs.  A book naming only what it holds is therefore compared against the fraction of the
    index it happens to own, and the difference comes back as alpha, most of it filed under
    interaction where nobody looks.  The engine's own benchmark column, which it returns at zero,
    is dropped on the way; the cash position stays.
    """
    without_benchmark = daily_weights.drop(
        columns=[benchmark_column],
        errors="ignore",
    )
    missing_constituents = [
        column
        for column in benchmark_weights.columns
        if column not in without_benchmark.columns
    ]
    widened = without_benchmark.reindex(
        columns=[*without_benchmark.columns, *missing_constituents],
    )

    return widened.fillna(0.0)


# --- example: end ---
