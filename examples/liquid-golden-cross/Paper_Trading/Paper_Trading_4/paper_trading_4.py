"""
The frozen book of Experiment 4 -- step 7 of 8.  `Paper_Trading_N` mirrors the `Experiment_N` it
was promoted from, so the lineage of a paper-traded book is never in question.

In plain words: the rule that graduated, **copied out of the experiment notebook and then left
alone**.  The notebook is the record of how the rule was *chosen*, including everything tried and
rejected, and it stays free for the next piece of research.  This file is the record of what is
*being traded*, and a change to it is a change to a live book, not a change to an experiment.

What it holds, once its experiment graduates:

- the rule's settings, copied from the experiment notebook, and its costs;
- the rule itself, in the form the notebook ran it, with its control -- the same rule with one
  ingredient removed, which runs beside the book every day;
- `BANDS`: for each diagnostic, the range `FINDINGS_N.md` measured over the backtest, registered
  in this book's section of `../BITACORA.md` before its first day; a day outside one is a flag;
- `run(as_of)`, which `../daily_update.py` calls once a day.  It runs the frozen refinery in this
  folder over the raw files linked into `Data/Curator/Time_Series/`, applies the rule from the
  experiment's first day to `as_of`, writes the weight files, prices the book and its control with
  the frozen engine module twice -- over the whole history and since the freeze date in
  `FREEZE.json` -- and returns what the record needs: the engine's results, the book in force,
  the day's diagnostics, the flags and a summary.

Every module it imports is the copy `../promote.py` made in this folder, loaded by path under a
name of its own, never the shared one in `Experiments/`: that is what keeps it frozen.  It re-fits
nothing, and it computes no performance figure -- the engine does.

`../daily_update.py` calls into here; it never re-derives the rule itself.  A strategy with no
graduated book keeps this file as it is: the contract, with no logic.

See `../BITACORA.md` for the gate, and `../../RESULTS.md` for the numbers a candidate is judged on.
"""

# --- example: begin ---

# In this example Experiment 4 did not graduate: it failed its kill switch on one margin. It is on
# paper by the owner's decision of 2026-09-25, as a candidate, so that the months after its test
# window become the unseen test its blueprint named; `../BITACORA.md` records the exception and
# registers this book's bands, review dates and what its record cannot show, before its first day.

import dataclasses
import datetime
import importlib.util
import json
import os
import pathlib
import shutil
import subprocess
import sys
import types

import numpy
import pandas

__all__ = [
    "BANDS",
    "BookRun",
    "run",
]

BOOK_DIRECTORY = pathlib.Path(__file__).parent
FREEZE_PATH = BOOK_DIRECTORY / "FREEZE.json"
REFINERY_SCRIPT = BOOK_DIRECTORY / "Data" / "refinery.py"
# The engine prices from a staged copy of the raw files, in which each listing the stale-bars check
# ends is written to its last distinct bar; the linked raw files themselves are never written.
STAGED_DIRECTORY = BOOK_DIRECTORY / "Backtest" / "Market_Data"

# The rule's settings, as `experiment_4.ipynb` ran them, from `BLUEPRINT_4.md`.
BOOK_SIZE = 20
POOL_SIZE = 100
STATE_WINDOW_DAYS = 504
REBALANCE_FREQUENCY = "month"
TEST_START = pandas.Timestamp("2002-07-30")
# The experiment's window ended here; every day after it is one the rule never saw.
EXPERIMENT_END = pandas.Timestamp("2026-06-01")
# The fifty-one names `JOURNAL_4.md` recorded before the rule ran: Experiment 1's two tests.
EXCLUDED_IDENTIFIERS = (
    "AFS.A",
    "ARC1",
    "ASDV",
    "BFO1",
    "CBS1",
    "CDP1",
    "CG1",
    "CHA1",
    "CIT",
    "CLFY",
    "CNG",
    "COMR",
    "CSR1",
    "DLJ",
    "DNB1",
    "ETEK1",
    "FJ",
    "FMC",
    "FPC",
    "GIC1",
    "GTE1",
    "HLI.A",
    "HRD1",
    "JPM1",
    "LCI",
    "LCOS",
    "LGE",
    "MIR1",
    "NA.A",
    "NCE",
    "NGH",
    "NN1",
    "NSOL",
    "OCLI",
    "PARA",
    "PNU1",
    "PWJ1",
    "RLM1",
    "RLR",
    "SE2",
    "SEG1",
    "TAP1",
    "TMC.A",
    "TVGIA",
    "UCM",
    "UPR",
    "USW",
    "VO1",
    "VRI",
    "WLA",
    "YNR",
)

# The columns the rule reads, as the notebook named them.
BAR_COLUMNS = (
    "m_open",
    "m_high",
    "m_low",
    "m_close",
)
FILL_COLUMN = "c_vwap_dividend_and_split_adjusted"
MARK_COLUMN = "m_close_dividend_and_split_adjusted"
RANKING_COLUMN = "r_liquidity_rank"
SIGNAL_COLUMN = "r_momentum_12_1"

# The costs every verdict was read at, the notebook's headline row.
CASH_RESERVE = 0.10
COMMISSION_CENTS = 0.1
INITIAL_CAPITAL = 1_000_000
SLIPPAGE_BASIS_POINTS = 5.0

# The index is priced when its hand-supplied returns reach the day; past their end, the benchmark
# every file already carries, and the run says so.
FALLBACK_BENCHMARK = "SPY"

# For each diagnostic, the range outside which a day is flagged; a flag, not a stop.  Registered in
# `../BITACORA.md` before the book's first day: holdings as `FINDINGS_4.md` measured them, 20.0 on
# every day; the invested share's floor of 0.95 is a choice where the findings report 100.0%.
BANDS = {
    "holdings": (
        20.0,
        20.0,
    ),
    "invested share": (
        0.95,
        1.0,
    ),
}


@dataclasses.dataclass(frozen=True)
class BookRun:
    """
    One day's run of the book: what the record keeps, and what the log says.

    `results` maps a window and a series -- `("whole", "book")` -- to the engine's result;
    `books` is the book and the control in force that day, one row per holding.
    """

    as_of: "datetime.date"
    books: "pandas.DataFrame"
    diagnostics: "pandas.DataFrame"
    flags: list[dict[str, str]]
    results: dict[tuple[str, str], object]
    summary: list[str]


@dataclasses.dataclass(frozen=True)
class Panel:
    """
    Everything the rule reads, on one calendar and one set of positions, up to the day.
    """

    bear: "pandas.Series"
    fill: "pandas.DataFrame"
    mark: "pandas.DataFrame"
    membership: "pandas.DataFrame"
    ranking: "pandas.DataFrame"
    returns: "pandas.DataFrame"
    signal: "pandas.DataFrame"
    state_end: "pandas.Timestamp"


def run(
    as_of: "datetime.date",
) -> "BookRun":
    """
    Run the frozen book for one day: refine, check, rule, engine, and what the day looked like.
    """
    modules = _load_frozen_modules()
    _run_frozen_refinery()
    day = pandas.Timestamp(as_of)
    endings = _stale_endings(
        modules,
        day,
    )
    _stage_engine_files(
        modules,
        endings,
    )
    panel = _load_panel(
        modules,
        day,
        endings,
    )
    book = _build_book(
        panel,
        modules,
        True,
        None,
    )
    control = _build_book(
        panel,
        modules,
        False,
        book.index,
    )
    freeze = json.loads(FREEZE_PATH.read_text(encoding="utf-8"))
    freeze_day = pandas.Timestamp(freeze["freeze_date"])
    benchmark = _choose_benchmark(
        modules,
        day,
    )
    windows = {
        "whole": TEST_START,
        "after_window": EXPERIMENT_END + pandas.Timedelta(days=1),
        "since_freeze": freeze_day,
    }
    results = {}

    for window, start in windows.items():
        if start >= day:
            continue

        for series, weights in (("book", book), ("control", control)):
            results[(window, series)] = _price(
                modules,
                f"{window}_{series}",
                _from_start(weights, start),
                start,
                day,
                benchmark["identifier"],
            )

    diagnostics = _diagnostics(
        panel,
        book,
        endings,
        day,
    )
    books = _books_table(
        book,
        control,
        modules,
    )
    summary = _summary(
        results,
        book,
        day,
    )
    flags = benchmark["flags"] + _state_flags(
        panel,
        day,
    )

    return BookRun(
        as_of=as_of,
        books=books,
        diagnostics=diagnostics,
        flags=flags,
        results=results,
        summary=summary,
    )


def _books_table(
    book: "pandas.DataFrame",
    control: "pandas.DataFrame",
    modules: dict[str, "types.ModuleType"],
) -> "pandas.DataFrame":
    """
    The book and the control in force on the day, by listing, one row per holding.
    """
    rows = []

    for series, weights in (("book", book), ("control", control)):
        latest = weights.iloc[[-1]]
        by_identifier = modules["securities_panel"].expand_to_identifiers(latest)
        held = by_identifier.iloc[-1]

        for identifier, weight in held[held > 0].items():
            rows.append({
                "series": series,
                "identifier": identifier,
                "weight": float(weight),
                "since": latest.index[-1].date().isoformat(),
            })

    return pandas.DataFrame(rows)


def _build_book(
    panel: "Panel",
    modules: dict[str, "types.ModuleType"],
    use_ranking: bool,
    rebalance_dates: "pandas.DatetimeIndex | None",
) -> "pandas.DataFrame":
    """
    The rule as the notebook ran it, from the experiment's first day to the panel's last.

    The pool is the hundred members with the highest liquidity rank among those with a price and a
    fill price; the book is its twenty with the highest momentum, except on a date whose state is
    bear, when it is the pool's twenty most traded with a momentum value -- the control's own book.
    Every decision reads the prior close through the one-day lag.  `use_ranking=False` is the
    control, trading only on the book's own dates.
    """
    construction = modules["portfolio_construction"]
    tradable = panel.mark.notna() & panel.fill.notna()
    kept_members = (tradable & panel.membership).drop(
        columns=list(EXCLUDED_IDENTIFIERS),
        errors="ignore",
    )
    candidates = kept_members.reindex(
        columns=panel.mark.columns,
        fill_value=False,
    ).astype(bool)
    alphabetical = sorted(panel.mark.columns)
    liquidity_order = panel.ranking.where(candidates)[alphabetical].rank(
        axis=1,
        ascending=False,
        method="first",
    )
    pool = liquidity_order.reindex(columns=panel.mark.columns) <= POOL_SIZE
    with_momentum = pool & panel.signal.notna()
    traded_order = panel.ranking.where(with_momentum)[alphabetical].rank(
        axis=1,
        ascending=False,
        method="first",
    )
    control_book = traded_order.reindex(columns=panel.mark.columns) <= BOOK_SIZE

    if use_ranking:
        momentum_order = panel.signal.where(pool)[alphabetical].rank(
            axis=1,
            ascending=False,
            method="first",
        )
        momentum_book = momentum_order.reindex(columns=panel.mark.columns) <= BOOK_SIZE
        bear = numpy.broadcast_to(
            panel.bear.to_numpy()[:, None],
            momentum_book.shape,
        )
        chosen = momentum_book.where(~bear, control_book)
    else:
        chosen = control_book

    in_window = panel.mark.index >= TEST_START
    lagged = construction.lag_eligibility(chosen).loc[in_window]

    if rebalance_dates is None:
        rebalance_dates = construction.first_trading_days(
            lagged.index,
            REBALANCE_FREQUENCY,
        )

    return construction.build_weights(
        lagged,
        panel.returns,
        rebalance_dates,
        "equal_weight",
        1.0 / BOOK_SIZE,
        1,
    )


def _choose_benchmark(
    modules: dict[str, "types.ModuleType"],
    day: "pandas.Timestamp",
) -> dict[str, object]:
    """
    The index when its returns reach the day, else the fallback, with a flag saying which and why.
    """
    engine = modules["backtest_engine"]
    index_path = engine.MARKET_DATA_DIRECTORY / f"{engine.BENCHMARK_IDENTIFIER}.csv"
    index_dates = pandas.read_csv(
        index_path,
        usecols=["m_date"],
        parse_dates=["m_date"],
    )["m_date"]
    index_end = index_dates.max()

    if index_end >= day:

        return {
            "flags": [],
            "identifier": engine.BENCHMARK_IDENTIFIER,
        }

    detail = " ".join([
        f"the index's returns end {index_end.date()}:",
        f"priced against {FALLBACK_BENCHMARK} until the desk's files reach the day",
    ])

    return {
        "flags": [
            {
                "kind": "benchmark-fallback",
                "detail": detail,
                "severity": "flag",
            },
        ],
        "identifier": FALLBACK_BENCHMARK,
    }


def _diagnostics(
    panel: "Panel",
    book: "pandas.DataFrame",
    endings: dict[str, "pandas.Timestamp"],
    day: "pandas.Timestamp",
) -> "pandas.DataFrame":
    """
    What the book looked like on the day, from its targets: its shape, not its return.
    """
    latest = book.iloc[-1]
    held = latest[latest > 0]
    master_path = BOOK_DIRECTORY / "Universe" / "Security_Master.csv"
    master = pandas.read_csv(master_path).set_index("main_identifier")
    sectors = master["sector"].reindex(held.index).fillna("unknown")
    sector_shares = held.groupby(sectors).sum()
    recent_days = panel.mark.index[-63:]
    recent_trades = book.index[book.index >= recent_days[0]]
    invested = float(held.sum())
    squares = held.pow(2)
    squared = float(squares.sum())
    concentration = squared / invested ** 2 if invested > 0 else 0.0
    effective_names = 1.0 / concentration if concentration > 0 else 0.0
    largest_share = sector_shares.max() if len(sector_shares) > 0 else 0.0
    largest_sector = float(largest_share) / invested if invested > 0 else 0.0
    state_yesterday = panel.bear.shift(1).loc[day]
    measures = {
        "holdings": float(len(held)),
        "invested share": invested,
        "effective names": effective_names,
        "largest sector share": largest_sector,
        "bear state at the prior close": float(bool(state_yesterday)),
        "listings the stale-bars check ends": float(len(endings)),
        "trade dates in the last 63 days": float(len(recent_trades)),
        "traded today": float(book.index[-1] == day),
    }

    return pandas.DataFrame({
        "date": day.date().isoformat(),
        "measure": list(measures),
        "value": list(measures.values()),
    })


def _from_start(
    weights: "pandas.DataFrame",
    start: "pandas.Timestamp",
) -> "pandas.DataFrame":
    """
    The targets from a window's first day: the book in force then, and every trade after it.

    Only the names the window holds are kept.  The book's history carries a column for every name
    it ever held, and a name that left the market before the window has no price in it, which the
    engine refuses rather than ignores.
    """
    earlier = weights[weights.index <= start]
    later = weights[weights.index > start]

    if len(earlier) == 0:
        window_weights = later
    else:
        opening = earlier.iloc[[-1]].copy()
        opening.index = pandas.DatetimeIndex([start])
        window_weights = pandas.concat([
            opening,
            later,
        ])

    held_in_window = window_weights.gt(0).any(axis=0)

    return window_weights.loc[:, held_in_window]


def _load_frozen_modules() -> dict[str, "types.ModuleType"]:
    """
    The copies `promote.py` froze in this folder, each under a name no other book's copy uses.
    """
    locations = {
        "backtest_engine": BOOK_DIRECTORY / "Experiments" / "backtest_engine.py",
        "hand_supplied": BOOK_DIRECTORY / "Data" / "hand_supplied.py",
        "portfolio_construction": BOOK_DIRECTORY / "Experiments" / "portfolio_construction.py",
        "securities_panel": BOOK_DIRECTORY / "Experiments" / "securities_panel.py",
    }
    modules = {}

    for name, path in locations.items():
        unique_name = f"{BOOK_DIRECTORY.name.lower()}_{name}"
        specification = importlib.util.spec_from_file_location(
            unique_name,
            path,
        )
        module = importlib.util.module_from_spec(specification)
        sys.modules[unique_name] = module
        specification.loader.exec_module(module)
        modules[name] = module

    return modules


def _load_panel(
    modules: dict[str, "types.ModuleType"],
    day: "pandas.Timestamp",
    endings: dict[str, "pandas.Timestamp"],
) -> "Panel":
    """
    The refined panel up to the day, with each listing the check ends read as no price after it.

    Membership is the desk's holdings, and the state the desk's index returns: the index's level
    over its level 504 desk dates earlier, below one, at each close. Past the desk's last date both
    are held there, and the run flags it.
    """
    panel_module = modules["securities_panel"]
    matrices = panel_module.load_matrices((
        SIGNAL_COLUMN,
        RANKING_COLUMN,
        MARK_COLUMN,
        FILL_COLUMN,
    ))
    calendar = matrices[MARK_COLUMN].index
    mark = matrices[MARK_COLUMN].loc[calendar <= day].copy()
    columns = mark.columns
    fill = matrices[FILL_COLUMN].reindex(index=mark.index, columns=columns)
    ranking = matrices[RANKING_COLUMN].reindex(index=mark.index, columns=columns)
    signal = matrices[SIGNAL_COLUMN].reindex(index=mark.index, columns=columns)
    position_keys = panel_module.read_position_keys()

    for listing, ending in endings.items():
        position = position_keys.get(listing, listing)

        if position not in columns:
            continue

        after = mark.index > ending

        for frame in (
            mark,
            fill,
            ranking,
            signal,
        ):
            frame.loc[after, position] = numpy.nan

    holdings = modules["hand_supplied"].read_benchmark_holdings()
    holdings.columns = [
        position_keys.get(column, column)
        for column in holdings.columns
    ]
    in_index = (holdings > 0).T.groupby(level=0).any().T
    membership = in_index.reindex(index=mark.index, columns=columns).ffill()
    known_membership = membership.where(membership.notna(), False)
    index_returns = modules["hand_supplied"].read_benchmark_returns()
    index_level = (1.0 + index_returns).cumprod()
    trailing = index_level / index_level.shift(STATE_WINDOW_DAYS) - 1.0

    return Panel(
        bear=(trailing.reindex(mark.index, method="ffill") < 0),
        fill=fill,
        mark=mark,
        membership=known_membership.astype(bool),
        ranking=ranking,
        returns=mark.pct_change(fill_method=None),
        signal=signal,
        state_end=index_returns.index.max(),
    )


def _price(
    modules: dict[str, "types.ModuleType"],
    name: str,
    weights: "pandas.DataFrame",
    start: "pandas.Timestamp",
    end: "pandas.Timestamp",
    benchmark_identifier: str,
) -> object:
    """
    Write one window's weight file in this folder and run the frozen engine module over it.
    """
    engine = modules["backtest_engine"]
    expanded = modules["securities_panel"].expand_to_identifiers(weights)
    # A position that changed ticker expands to every listing it ever had, and a listing with no
    # price in the window is one the engine refuses: only the listings the window holds are written.
    held_listings = expanded.gt(0).any(axis=0)
    by_identifier = expanded.loc[:, held_listings]
    engine.write_weight_file(
        by_identifier,
        BOOK_DIRECTORY,
        name,
    )
    configuration = engine.build_configuration(
        BOOK_DIRECTORY,
        start.date(),
        end.date(),
        INITIAL_CAPITAL,
        COMMISSION_CENTS,
        SLIPPAGE_BASIS_POINTS,
        CASH_RESERVE,
        name,
        benchmark_identifier,
    )
    result = engine.run_backtest(
        BOOK_DIRECTORY,
        configuration,
    )

    if not result.success:
        refused_message = f"the engine refused {name}: {result.error}"

        raise RuntimeError(refused_message)

    return result


def _run_frozen_refinery() -> None:
    """
    Run the refinery frozen in this folder over the raw files linked into it.
    """
    completed = subprocess.run(
        [
            sys.executable,
            str(REFINERY_SCRIPT),
        ],
        check=False,
        cwd=BOOK_DIRECTORY,
    )

    if completed.returncode != 0:
        message = f"the frozen refinery stopped with exit code {completed.returncode}"

        raise RuntimeError(message)


def _stage_engine_files(
    modules: dict[str, "types.ModuleType"],
    endings: dict[str, "pandas.Timestamp"],
) -> None:
    """
    Link every raw file into a folder of the engine's own, and write each listing the check ends to
    its last distinct bar; then point the frozen engine module there.
    """
    engine = modules["backtest_engine"]
    raw_directory = BOOK_DIRECTORY / "Data" / "Curator" / "Time_Series"
    shutil.rmtree(STAGED_DIRECTORY, ignore_errors=True)
    STAGED_DIRECTORY.mkdir(parents=True)

    for path in raw_directory.glob("*.csv"):
        staged = STAGED_DIRECTORY / path.name

        if path.stem in endings:
            rows = pandas.read_csv(
                path,
                dtype=str,
                keep_default_na=False,
            )
            last_bar = endings[path.stem].strftime("%Y-%m-%d")
            rows[rows["m_date"] <= last_bar].to_csv(staged, index=False)
            continue

        try:
            os.link(path, staged)
        except OSError:
            shutil.copy2(path, staged)

    engine.MARKET_DATA_DIRECTORY = STAGED_DIRECTORY


def _stale_endings(
    modules: dict[str, "types.ModuleType"],
    day: "pandas.Timestamp",
) -> dict[str, "pandas.Timestamp"]:
    """
    Each listing whose file, cut at the day, ends in rows repeating its last distinct bar.

    The check `BLUEPRINT_4.md` fixed: the unadjusted open, high, low and close compared exactly,
    whatever the gaps between the rows' dates, and a run whose last row is the day itself not read
    as an ending, since the listing may trade on.
    """
    raw_directory = BOOK_DIRECTORY / "Data" / "Curator" / "Time_Series"
    endings = {}

    for path in sorted(raw_directory.glob("*.csv")):
        header = pandas.read_csv(path, nrows=0).columns

        if not set(BAR_COLUMNS) <= set(header):
            continue

        every_bar = pandas.read_csv(
            path,
            usecols=["m_date", *BAR_COLUMNS],
            parse_dates=["m_date"],
        )
        to_the_day = every_bar[every_bar["m_date"] <= day]
        complete = to_the_day.dropna(subset=list(BAR_COLUMNS))
        bars = complete.sort_values("m_date")

        if len(bars) < 2 or bars["m_date"].iloc[-1] >= day:
            continue

        values = bars[list(BAR_COLUMNS)].to_numpy()
        repeats = (values[1:] == values[:-1]).all(axis=1)
        run_length = _trailing_true(repeats)

        if run_length > 0:
            endings[path.stem] = bars["m_date"].iloc[-run_length - 1]

    return endings


def _state_flags(
    panel: "Panel",
    day: "pandas.Timestamp",
) -> list[dict[str, str]]:
    """
    A flag when the state is read from index returns that end before the day.
    """
    if panel.state_end >= day:

        return []

    detail = " ".join([
        f"the index's returns end {panel.state_end.date()}:",
        "the bear state is held at its value there until the desk's files reach the day",
    ])

    return [
        {
            "kind": "state-held",
            "detail": detail,
            "severity": "flag",
        },
    ]


def _summary(
    results: dict[tuple[str, str], object],
    book: "pandas.DataFrame",
    day: "pandas.Timestamp",
) -> list[str]:
    """
    The log's lines for the day: each window's engine figures for the book and its control.
    """
    lines = [
        f"traded today: {book.index[-1] == day}; last trade {book.index[-1].date()}",
    ]

    for (window, series), result in results.items():
        statistics = result.data["portfolio_stats"]
        lines.append(" ".join([
            f"{window} {series}:",
            f"CAGR {statistics['Annualized Return (CAGR)']:.4f},",
            f"Sharpe {statistics['Portfolio Sharpe Ratio']:.3f},",
            f"max drawdown {statistics['Max Drawdown']:.4f}",
        ]))

    return lines


def _trailing_true(
    flags: "numpy.ndarray",
) -> int:
    """
    How many of the last entries are true, counted back from the end until the first false.
    """
    reversed_flags = flags[::-1]
    falses = numpy.flatnonzero(~reversed_flags)

    if len(falses) == 0:

        return len(flags)

    return int(falses[0])

# --- example: end ---
