"""
The frozen book of Experiment 1 -- step 7 of 8.  `Paper_Trading_N` mirrors the `Experiment_N` it
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
  the frozen engine module -- over the whole history, over the days after the experiment's window
  and since the freeze date in `FREEZE.json` -- and returns what the record needs: the engine's
  results, the book in force, the day's diagnostics, the flags and a summary.

**Membership past the last date its source wrote is held at that date.**  An index's holdings,
read by `Data/hand_supplied.py`, are refreshed later than prices, and a membership built only from
the dates they hold -- in the rule, or as a refined column -- has no member past their last date:
right for a backtest, and a book that read it so would sell every name the day those files end.
The book holds the last membership they wrote, and `../daily_update.py` flags the files once they
fall behind the day; inside the experiment's window they cover every day, so the rule it ran is
unchanged.

Every module it imports is the copy `../promote.py` made in this folder, loaded by path under a
name of its own, never the shared one in `Experiments/`: that is what keeps it frozen.  It re-fits
nothing, and it computes no performance figure -- the engine does.

`../daily_update.py` calls into here; it never re-derives the rule itself.  A strategy with no
graduated book keeps this file as it is: the contract, with no logic.

See `../BITACORA.md` for the gate, and `../../RESULTS.md` for the numbers a candidate is judged on.
"""

# --- example: begin ---

# Experiment 1's book, frozen on 2026-10-06 after the owner signed it, as
# `Paper_Trading/BITACORA.md` records: the rule of `BLUEPRINT_1.md` and its control, the
# golden cross removed, on the book's own dates, with the bands registered before day one.
# In this package it is a record, and does not run.

import dataclasses
import datetime
import importlib.util
import json
import pathlib
import subprocess
import sys
import types

import pandas

__all__ = [
    "BANDS",
    "BookRun",
    "run",
]

BOOK_DIRECTORY = pathlib.Path(__file__).parent
FREEZE_PATH = BOOK_DIRECTORY / "FREEZE.json"
REFINERY_SCRIPT = BOOK_DIRECTORY / "Data" / "refinery.py"

# The rule's settings, as `experiment_1.ipynb` ran them; `FREEZE.json` records the commit.
EXCLUDED_IDENTIFIERS = (
    "MNKKQ",
    "NE",
    "PCP",
    "RAI",
)
# The experiment's window: it opened here, and ended on the last day the rule was judged on.
EXPERIMENT_END = pandas.Timestamp("2026-06-01")
MAXIMUM_WEIGHT = 0.20
MINIMUM_WEIGHT = 0.01
WINDOW_START = pandas.Timestamp("2015-01-02")

# The columns the rule reads, as the notebook named them.
FILL_COLUMN = "c_vwap_dividend_and_split_adjusted"
MARK_COLUMN = "m_close_dividend_and_split_adjusted"
MEMBERSHIP_COLUMN = "r_index_weight"
SCORE_COLUMN = "r_traded_value_sma_63d"
TREND_COLUMN = "r_trend_50_200"

# The costs every verdict was read at, the notebook's headline row.
CASH_RESERVE = 0.01
COMMISSION_CENTS = 0.05
INITIAL_CAPITAL = 1_000_000
SLIPPAGE_BASIS_POINTS = 5.0

# The index is priced when its hand-supplied returns reach the day; past their end, the benchmark
# every file already carries, and the run says so.
FALLBACK_BENCHMARK = "SPY"

# For each diagnostic, the range outside which a day is flagged; a flag, not a stop.  Taken from
# `FINDINGS_1.md` and registered in `../BITACORA.md` before the book's first day.  Holdings are
# the measured 18 to 61 a day, the invested share the measured 100% throughout, and a held name
# with the cross at 0 never happened; the largest weight's upper end is the rule's own cap, and
# its lower end is not banded.
BANDS = {
    "holdings": (
        18.0,
        61.0,
    ),
    "invested share": (
        1.0,
        1.0,
    ),
    "largest weight": (
        0.0,
        0.2,
    ),
    "names held with the cross at 0 at the prior close": (
        0.0,
        0.0,
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

    fill: "pandas.DataFrame"
    mark: "pandas.DataFrame"
    membership: "pandas.DataFrame"
    score: "pandas.DataFrame"
    trend: "pandas.DataFrame"


def run(
    as_of: "datetime.date",
) -> "BookRun":
    """
    Run the frozen book for one day: refine, rule, engine, and what the day looked like.
    """
    modules = _load_frozen_modules()
    _run_frozen_refinery()
    day = pandas.Timestamp(as_of)
    panel = _load_panel(
        modules,
        day,
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
    benchmark = _choose_benchmarks(
        modules,
        day,
    )
    windows = {
        "whole": WINDOW_START,
        "after_window": EXPERIMENT_END + pandas.Timedelta(1, unit="D"),
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
                benchmark["identifiers"],
            )

    diagnostics = _diagnostics(
        panel,
        book,
        modules,
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

    return BookRun(
        as_of=as_of,
        books=books,
        diagnostics=diagnostics,
        flags=benchmark["flags"],
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
    use_cross: bool,
    decision_dates: "pandas.DatetimeIndex | None",
) -> "pandas.DataFrame":
    """
    The rule as the notebook ran it, from the experiment's first day to the panel's last.

    Eligible on day t: a member with a 200-day history at the close of t-1 and, for the book, the
    golden cross at 1 then, a traded value then, and a fill price on t and on the next day, so a
    name whose prices are about to stop is sold the day before; the names excluded by name never.
    Sized by the bounded weigher, re-struck when the held set changes.  `use_cross=False` is the
    control, struck only on the book's own dates.
    """
    construction = modules["portfolio_construction"]
    trend_before = panel.trend.shift(1)
    member_before = panel.membership.shift(
        1,
        fill_value=False,
    )
    tradable = construction.exit_before_price_stops(panel.fill.notna())
    allowed = ~panel.fill.columns.isin(EXCLUDED_IDENTIFIERS)
    history = member_before & trend_before.notna() & tradable
    eligible = history & (trend_before > 0) if use_cross else history
    permitted = eligible.loc[:, allowed]
    aligned = permitted.reindex(
        columns=panel.fill.columns,
        fill_value=False,
    )
    in_window = aligned.loc[aligned.index >= WINDOW_START]
    daily = construction.bounded_book(
        in_window.astype(bool),
        panel.score,
        MAXIMUM_WEIGHT,
        MINIMUM_WEIGHT,
    )

    if decision_dates is not None:

        return daily.loc[decision_dates]

    dates = construction.rebalance_dates_on_change(daily > 0)

    return daily.loc[dates]


def _choose_benchmarks(
    modules: dict[str, "types.ModuleType"],
    day: "pandas.Timestamp",
) -> dict[str, object]:
    """
    The index and SPY when the index's returns reach the day, else SPY alone, with a flag saying so.
    """
    engine = modules["backtest_engine"]
    index_path = engine.MARKET_DATA_DIRECTORY / f"{engine.INDEX_IDENTIFIER}.csv"
    index_dates = pandas.read_csv(
        index_path,
        usecols=["m_date"],
        parse_dates=["m_date"],
    )["m_date"]
    index_end = index_dates.max()

    if index_end >= day:

        return {
            "flags": [],
            "identifiers": engine.BENCHMARK_IDENTIFIERS,
        }

    detail = " ".join([
        f"the index's returns end {index_end.date()}:",
        f"priced against {FALLBACK_BENCHMARK} until the Analytics Factory's files reach the day",
    ])

    return {
        "flags": [
            {
                "kind": "benchmark-fallback",
                "detail": detail,
                "severity": "flag",
            },
        ],
        "identifiers": (FALLBACK_BENCHMARK,),
    }


def _diagnostics(
    panel: "Panel",
    book: "pandas.DataFrame",
    modules: dict[str, "types.ModuleType"],
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
    cross_yesterday = (panel.trend > 0).shift(
        1,
        fill_value=False,
    ).loc[day]
    broken = [
        name
        for name in held.index
        if not bool(cross_yesterday.get(name, False))
    ]
    recent_days = panel.mark.index[-63:]
    recent_trades = book.index[book.index >= recent_days[0]]
    held_total = held.sum()
    invested = float(held_total)
    squares = held.pow(2)
    squared = float(squares.sum())
    concentration = squared / invested ** 2 if invested > 0 else 0.0
    effective_names = 1.0 / concentration if concentration > 0 else 0.0
    largest_share = sector_shares.max()
    largest_sector = float(largest_share) / invested if invested > 0 else 0.0
    largest_holding = held.max() if len(held) > 0 else 0.0
    largest_weight = float(largest_holding)
    measures = {
        "holdings": float(len(held)),
        "invested share": invested,
        "largest weight": largest_weight,
        "effective names": effective_names,
        "largest sector share": largest_sector,
        "names held with the cross at 0 at the prior close": float(len(broken)),
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
) -> "Panel":
    """
    The refined panel up to the day, on the price calendar, membership as the refinery joined it.

    The refinery never carries membership past the last date the Analytics Factory wrote, which is
    right for a backtest and would empty a paper book the day the Analytics Factory's files fall
    behind: past that date the last membership the Analytics Factory wrote is held, and
    `daily_update.py` flags every day it is. Inside the experiment's window the Analytics Factory
    covers every day, so the rule it ran is unchanged.
    """
    matrices = modules["securities_panel"].load_matrices((
        TREND_COLUMN,
        SCORE_COLUMN,
        MEMBERSHIP_COLUMN,
        MARK_COLUMN,
        FILL_COLUMN,
    ))
    calendar = matrices[MARK_COLUMN].index
    on_or_before = calendar <= day
    weights = matrices[MEMBERSHIP_COLUMN].loc[on_or_before].fillna(0.0)
    desk_holdings = modules["hand_supplied"].read_benchmark_holdings()
    desk_end = desk_holdings.index.max()
    written = weights.loc[weights.index <= desk_end]
    held = written.reindex(
        weights.index,
        method="ffill",
    )

    return Panel(
        fill=matrices[FILL_COLUMN].loc[on_or_before],
        mark=matrices[MARK_COLUMN].loc[on_or_before],
        membership=held > 0,
        score=matrices[SCORE_COLUMN].loc[on_or_before],
        trend=matrices[TREND_COLUMN].loc[on_or_before],
    )


def _price(
    modules: dict[str, "types.ModuleType"],
    name: str,
    weights: "pandas.DataFrame",
    start: "pandas.Timestamp",
    end: "pandas.Timestamp",
    benchmark_identifiers: tuple[str, ...],
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
        benchmark_identifiers,
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

# --- example: end ---
