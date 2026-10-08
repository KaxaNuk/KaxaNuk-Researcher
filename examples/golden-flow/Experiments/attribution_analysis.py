"""
Attribution analysis -- step 6 of 8, the fourth shared module.  Shapes what the KaxaNuk Attribution
Analysis library needs, and says what is missing before it tries.

In plain words: which part of the return did you actually earn?

Runs inside an experiment notebook, section 5, after the backtest.

What is expected here:

- Say what is present.  The library needs four inputs: an index's daily holdings and its daily
  returns, one or more factor-return files, and the book from step 5.  The first three come from
  KaxaNuk's Analytics Factory, read in place by `Data/hand_supplied.py` from the folder
  `KN_ANALYTICS_PATH` names, or from the drop zones under `Data/Curator/`.  Check for them first
  and report the gap in a sentence, so a clone with no licence and no index files pays nothing
  to find out.
- Speak the book's language.  The index's holdings and the factor files key a listing by the
  index's own ticker; the book keys it by `main_identifier`, the identifier the experiment's
  provider prices it under.  Map one to the other through the seed's two keys, as
  `Data/hand_supplied.py` reads them, before any pass, so `BRK.B` and `BRK-B` are one security and
  a listing the seed does not price is left out rather than matched by accident.  The map comes
  from the strategy's seed builder, or from the Analytics Factory where it supplies one.
- Compare against the index the strategy can price.  On each date, a member with no price -- one
  the experiment's provider does not carry, or a date outside the span its file speaks for -- is
  dropped from the index's holdings and the rest renormalised, and the share dropped is reported
  per year: a member left in at a zero return hands its return to the book as alpha.
- Take the book as a daily series, from `Backtest/`, never from `Portfolio/portfolio_weights.csv`.
  The library rejects a weight file that is not daily once it spans a year, and the rebalance-date
  file the engine read is exactly what it refuses.  The book it attributes is the one the engine
  held each trading day, drift and the cash proxy included; the benchmark's holdings follow the
  same rule.
- Hold both weight tables overnight.  The engine's daily weights and the index's holdings are
  struck at a day's close, after that day's return has moved them, and the library pairs a weight
  with the return of its own date.  Paired as they arrive, a weight that already holds a day's
  move earns that move again, and every book -- the index's too -- is credited with the
  cross-section's daily variance, several points a year, in every pass.  Move both tables one day
  on, so the close of t-1 earns day t, after the asset returns are read on the engine's own days.
- Reconcile the benchmark before any figure is read.  The first cut's benchmark return, mean daily
  times 252, against the index's own returns file over the same days: more than a point a year
  apart, and the benchmark the book was compared with is not the index -- weights a day out,
  members unpriced, a book not widened -- so the notebook's Verify section raises.  The returns
  file never enters the library, which is what makes it the check.
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
- Say what the factor directory has to look like, because it holds nothing but factor files: one CSV per factor, named by its file name, a date column first -- its
  header may be empty -- and one column per security after it.  Four names are reserved by the
  library, matched exactly and in lower case, and dropped from the percentage decomposition:
  `f_market`, `f_total_factor_returns`, `f_total_excess_returns` and `f_idyo_returns`.  The
  Analytics Factory ships them as `Market`, `Total_Factor_Returns`, `Total_Excess_Returns` and
  `Idyo_Returns`, and a reserved file attributed as an ordinary factor is a quiet way to
  double-count the market.  So `Data/hand_supplied.py` maps each file name to the library's name,
  once, and nothing is renamed on disk.
- Name the index's two files and their date convention once, in `Data/hand_supplied.py`, so
  switching to a different index is an edit there and no notebook names one of them.
- Keep the library's numbers as tables.  It writes no file: the first cut, the factor model and
  the third pass are read from the objects it builds, and the notebook writes each table
  `FINDINGS_N.md` quotes to `Attribution/`.  Its figures go to the screen; say whether they are
  kept -- saved to `Attribution/` beside the tables -- or left unshown under a non-interactive
  backend, so a headless run never waits on a window.

Expect two methodologies and a third pass, all reported.  Brinson-Fachler splits active return
into allocation, selection and interaction -- the lever that moved.  The factor model splits
excess return into compensated factor tilts and idiosyncratic alpha -- what was paid for, on
purpose or by accident.  Then Brinson-Fachler again on the residual, which says whether the
Sharpe survives once the factor turns.  Expect the answer to be partial -- an absolute rule is
close to invisible to a factor model built on relative factors -- and treat that as a finding.
The follow-ups are counterfactual books the engine can already price.  `AGENTS.md` has the
reasoning.

It produces `Attribution/` -- the tables of the two decompositions and the third pass, and the
figures where they are kept -- for `FINDINGS_N.md`, and the answer to graduation criterion 2.

It prevents selling factor beta as if it were alpha, crediting a book with a day's return its
weights already held or with an unpriced member's return, and a run that stops at its first file
because a header carries the name a provider gave it rather than the one the loader expects.
"""

# --- example: begin ---

# Golden Flow attributes against the KN US Equity Core's holdings and the KN US Equity Factor
# Model, read through `Data/hand_supplied.py`.  The notebook calls `attribute_books`, which
# runs each book's passes in parallel: all three on the rule, its control and the
# equal-weight arm, the factor model alone on the twenty random books.  `held_overnight`
# pairs the close of t-1 with day t, and `benchmark_coverage` reports the share of the index
# the run can price.

import concurrent.futures
import hashlib
import importlib.util
import pathlib
import types

import pandas
import pyarrow

__all__ = [
    "DATE_HEADER",
    "LIBRARY_INSTALLED",
    "attribute_book",
    "attribute_books",
    "benchmark_coverage",
    "held_overnight",
    "load_asset_returns",
    "load_benchmark_weights",
    "load_factor_returns",
    "load_prices",
    "report_missing_inputs",
    "to_arrow",
    "widen_to_benchmark",
]

# The one cell that decides whether a file loads: dates down, securities across.  `date`, `m_date`
# or whatever a provider used raises before a number is read.
DATE_HEADER = "date_column"
HAND_SUPPLIED_PATH = pathlib.Path(__file__).parent.parent / "Data" / "hand_supplied.py"
LIBRARY_INSTALLED = importlib.util.find_spec("kaxanuk.attribution_analysis") is not None
PRICE_COLUMN = "m_close_dividend_and_split_adjusted"
# The factor files, read once per process: every book attributed in it reads the same ones.
FACTOR_CACHE = {}
# The Curator's files, for the cash proxy and anything else outside the seed.
CURATOR_DIRECTORY = pathlib.Path(__file__).parent.parent / "Data" / "Curator" / "Time_Series"
# The refined files, because each is cut to the span its symbol speaks for its security.
REFINERY_DIRECTORY = pathlib.Path(__file__).parent.parent / "Data" / "Refinery" / "Time_Series"


def attribute_book(
    task: dict[str, object],
) -> dict[str, object]:
    """
    Run the three passes on one book, in a worker process, and return the summed tables.

    The task carries the book's daily weights already widened to the index, the index's weights,
    the asset returns and the layers to run: `brinson`, `factor` and `residual`.  The factor files
    are read once per worker and kept, because they are a gigabyte and every book reads the same
    ones.  The library computes; this only sums its daily tables over the window, in points.  With
    a `cache_directory`, the answer is kept under the hash of everything the task carries, so a
    notebook re-run attributes only what changed.
    """
    cache_path = _attribution_cache_path(task)

    if cache_path is not None and cache_path.is_file():

        return pandas.read_pickle(cache_path)

    import matplotlib

    matplotlib.use("Agg")

    import kaxanuk.attribution_analysis.performance_attribution

    library = kaxanuk.attribution_analysis.performance_attribution

    book = task["book"]
    benchmark = task["benchmark"]
    asset_returns = task["asset_returns"]
    layers = tuple(task["layers"])
    window = book.index
    answer = {
        "name": task["name"],
    }

    if "brinson" in layers:
        brinson = library.BrinstonFachlerArrowAttribution(
            to_arrow(asset_returns),
            to_arrow(book),
            to_arrow(benchmark),
            date_column=DATE_HEADER,
        )
        brinson.time_series_calculation()
        brinson_frame = brinson.df.to_pandas()
        brinson_daily = brinson_frame.set_index("date")
        answer["brinson_daily"] = brinson_daily
        answer["brinson_totals"] = brinson_daily.select_dtypes("number").sum() * 100

    if "factor" in layers or "residual" in layers:
        factors = _factor_returns()

    if "factor" in layers:
        first_date = window.min()
        last_date = window.max()
        by_factor = {
            name: to_arrow(frame.loc[first_date:last_date])
            for name, frame in factors.items()
        }
        factor_model = library.KNFMArrowAttribution(
            to_arrow(book),
            by_factor,
            to_arrow(asset_returns),
            date_column=DATE_HEADER,
        )
        factor_model.multifactor_attribution()
        factor_daily = factor_model.portfolio_attribution_ts.to_pandas()
        answer["factor_totals"] = factor_daily.select_dtypes("number").sum() * 100

    if "residual" in layers:
        idiosyncratic = factors["f_idyo_returns"].reindex(
            index=window,
            columns=asset_returns.columns,
        )
        covered_columns = idiosyncratic.columns[idiosyncratic.notna().any()]
        residual = library.BrinstonFachlerArrowAttribution(
            to_arrow(idiosyncratic.fillna(0.0)),
            to_arrow(book),
            to_arrow(benchmark),
            date_column=DATE_HEADER,
        )
        residual.time_series_calculation()
        residual_frame = residual.df.to_pandas()
        residual_daily = residual_frame.set_index("date")
        answer["residual_totals"] = residual_daily.select_dtypes("number").sum() * 100
        covered_weight = book[covered_columns].sum(axis=1)
        answer["covered_share"] = float(covered_weight.mean())

    if cache_path is not None:
        pandas.to_pickle(
            answer,
            cache_path,
        )

    return answer


def attribute_books(
    tasks: list[dict[str, object]],
    workers: int,
) -> dict[str, dict[str, object]]:
    """
    Attribute many books at once, one per worker process, keyed by name.

    A book whose attribution raises comes back with its error rather than stopping the others.
    """
    attributed = {}

    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(attribute_book, task): str(task["name"])
            for task in tasks
        }

        for future in concurrent.futures.as_completed(futures):
            name = futures[future]

            try:
                attributed[name] = future.result()
            except Exception as error:  # noqa: BLE001 - one book's failure must not stop the rest
                attributed[name] = {
                    "error": f"{type(error).__name__}: {error}",
                    "name": name,
                }

    return attributed


def benchmark_coverage(
    dates: "pandas.DatetimeIndex",
    prices: "pandas.DataFrame",
) -> "pandas.Series":
    """
    The share of the whole index, on each of the book's dates, that this repository can price.

    The rest -- members FMP does not carry, and members on dates outside their file's span -- is
    what `load_benchmark_weights` drops before it renormalises, and it is reported beside every
    Brinson-Fachler table: it is the survivorship cost of an FMP-only universe, as attribution
    sees it.
    """
    kept = _priced_holdings(
        dates,
        prices,
    )

    return kept.sum(axis=1)


def held_overnight(
    weights: "pandas.DataFrame",
) -> "pandas.DataFrame":
    """
    The weights that earn each day's return: the ones standing at the previous close.

    The engine's daily weights and the index's holdings are both struck at a day's close, after its
    return has moved them, and a weight that already contains a day's move, paired with that day's
    return, credits every book with the cross-section's daily variance -- seven points a year on
    this index.  The library pairs the two tables by date, so the weights are moved one day on:
    the close of t-1 earns day t.  The first day has no previous close and is dropped.
    """
    moved = weights.shift(1)

    return moved.iloc[1:]


def load_asset_returns(
    prices: "pandas.DataFrame",
) -> "pandas.DataFrame":
    """
    Daily returns from a price matrix, a missing day a zero rather than a null.

    The library refuses nulls; a zero on a day a security is not priced is harmless only because
    neither book holds a weight in it that day, which `load_benchmark_weights` guarantees for the
    index and the rule guarantees for the book.
    """
    returns = prices.pct_change(fill_method=None)

    return returns.fillna(0.0)


def load_benchmark_weights(
    dates: "pandas.DatetimeIndex",
    prices: "pandas.DataFrame",
) -> "pandas.DataFrame":
    """
    The index's daily holdings on the book's dates, priced members only, summing to one.

    Keyed by the book's identifiers through the seed.  A member with no price on a date weighs
    zero that date and the rest are scaled up, so the first cut compares the book with the index it
    could have held; `benchmark_coverage` says how much of the real index that was.
    """
    kept = _priced_holdings(
        dates,
        prices,
    )
    totals = kept.sum(axis=1)
    positive_totals = totals.where(totals > 0)
    renormalised = kept.div(
        positive_totals,
        axis=0,
    )

    return renormalised.fillna(0.0)


def load_factor_returns() -> dict[str, "pandas.DataFrame"]:
    """
    Every factor file, named for the library and keyed by the book's identifiers.

    `Data/hand_supplied.py` names each file the way the library reserves; here the listings are
    renamed through the seed's map, and a listing the seed does not price is left out.
    """
    hand_supplied = _load_hand_supplied()
    keys = hand_supplied.read_listing_keys()
    factors = hand_supplied.read_factor_returns()
    renamed = {}

    for name, frame in factors.items():
        mapped = [
            listing
            for listing in frame.columns
            if listing in keys
        ]
        keyed = frame[mapped]
        keyed.columns = [
            keys[listing]
            for listing in mapped
        ]
        renamed[name] = keyed

    return renamed


def load_prices(
    identifiers: tuple[str, ...],
    dates: "pandas.DatetimeIndex",
) -> "pandas.DataFrame":
    """
    The total-return price of every security either book names, on the book's dates.

    Read from the refined files, which keep only the dates each symbol speaks for its security, so
    a reused ticker's other company never enters a return; the cash proxy, which the refinery does
    not carry, from the Curator's file.  A date with no price stays null here: the caller decides,
    and `load_benchmark_weights` drops the member that date.  A price of zero or below is not a
    price -- the return after it is infinite -- and is read as none.
    """
    columns = {}

    for identifier in identifiers:
        refined_path = REFINERY_DIRECTORY / f"{identifier}.csv"
        curated_path = CURATOR_DIRECTORY / f"{identifier}.csv"
        path = refined_path if refined_path.is_file() else curated_path

        if not path.is_file():
            continue

        frame = pandas.read_csv(
            path,
            usecols=[
                "m_date",
                PRICE_COLUMN,
            ],
            parse_dates=["m_date"],
            index_col="m_date",
        )
        positive = frame[PRICE_COLUMN].where(frame[PRICE_COLUMN] > 0)
        columns[identifier] = positive.reindex(dates)

    return pandas.DataFrame(
        columns,
        index=dates,
    )


def report_missing_inputs() -> list[str]:
    """
    Say which of the four inputs is absent, in one pass, before anything is loaded.

    A clone with no licence and no hand-supplied index files should pay one sentence to find that
    out, not a stack trace three cells later.
    """
    missing = []

    if not LIBRARY_INSTALLED:
        missing.append("the KaxaNuk Attribution Analysis library is not installed")

    hand_supplied = _load_hand_supplied()
    missing.extend(hand_supplied.report_missing())

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
    benchmark_columns: tuple[str, ...],
) -> "pandas.DataFrame":
    """
    Add every benchmark constituent the book does not hold, at zero weight.

    The library prices only the securities the book names, and the first cut computes the
    benchmark's return from those prices alone -- the index's own return series is never one of its
    inputs.  A book naming only what it holds is therefore compared against the fraction of the
    index it happens to own, and the difference comes back as alpha, most of it filed under
    interaction where nobody looks.  The engine's own benchmark columns, which it returns at zero,
    are dropped on the way; the cash position stays.
    """
    without_benchmark = daily_weights.drop(
        columns=list(benchmark_columns),
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


def _attribution_cache_path(
    task: dict[str, object],
) -> "pathlib.Path | None":
    """
    Where one book's attribution is kept: named by the hash of its inputs, or nowhere.
    """
    directory = task.get("cache_directory")

    if directory is None:

        return None

    digest = hashlib.sha256()
    framed_keys = (
        "book",
        "benchmark",
        "asset_returns",
    )

    for key in framed_keys:
        frame = task[key]
        hashed = pandas.util.hash_pandas_object(
            frame,
            index=True,
        )
        row_hashes = hashed.to_numpy()
        digest.update(row_hashes.tobytes())
        column_names = str(list(frame.columns))
        digest.update(column_names.encode("utf-8"))

    layers = str(task["layers"])
    digest.update(layers.encode("utf-8"))
    cache_directory = pathlib.Path(str(directory))
    cache_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    return cache_directory / f"{digest.hexdigest()}.pkl"


def _factor_returns() -> dict[str, "pandas.DataFrame"]:
    """
    The factor files keyed by the book's identifiers, read on the first call in a process.
    """
    if "factors" not in FACTOR_CACHE:
        FACTOR_CACHE["factors"] = load_factor_returns()

    return FACTOR_CACHE["factors"]


def _load_hand_supplied() -> "types.ModuleType":
    """
    Import the reader of the Analytics Factory's files by path, because `Data/` is a folder, not a
    package.
    """
    specification = importlib.util.spec_from_file_location(
        "hand_supplied",
        HAND_SUPPLIED_PATH,
    )
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)

    return module


def _priced_holdings(
    dates: "pandas.DatetimeIndex",
    prices: "pandas.DataFrame",
) -> "pandas.DataFrame":
    """
    The index's weights on the book's dates, each member's weight zero where it has no price.
    """
    hand_supplied = _load_hand_supplied()
    holdings = hand_supplied.read_member_holdings()
    on_dates = holdings.reindex(dates)
    forward_filled = on_dates.ffill()
    priced = prices.reindex(
        index=dates,
        columns=forward_filled.columns,
    ).notna()
    kept = forward_filled.where(
        priced,
        0.0,
    )

    return kept.fillna(0.0)

# --- example: end ---
