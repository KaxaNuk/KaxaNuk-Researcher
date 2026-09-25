"""
Portfolio construction -- step 4 of 8, the second shared module.  Turns the set of securities a
rule calls eligible into the weights a book holds, calling the KaxaNuk Portfolio Construction
library where it is installed.

In plain words: how much of what, and how often you change your mind.

Runs inside an experiment notebook, from the rule in section 2, on the matrices the securities
panel built.

What is expected here is one function signature and a few things behind it:

- The signature.  Given the securities eligible today and a returns history that has already been
  cut off before today, return one weight per security, summing to at most 1.0.  Every weighting
  scheme -- equal weight, or any sizing method the library registers whose configuration has no
  required field: inverse volatility, risk parity, hierarchical risk parity -- is the same shape,
  so swapping one for another is one line in the rule cell and nothing else in the notebook moves.
  That is what makes two experiments comparable rather than merely adjacent.
- The library inside the signature, never around it.  Build one of its methods per rebalance date,
  on the history already cut: a method that estimates from returns uses whatever history it was
  built with, and the library's own pipeline builds each method once for every date.  Import it
  inside a guard -- it is KaxaNuk's own library, installed by hand -- and stop with an error that
  names a method needing it when it is absent.  Equal weight needs nothing.
- At most one, not exactly one.  A strategy that can go to cash cannot satisfy the stricter form;
  the residual becomes a real, priced cash position when the weight file is written.
- The constraints every scheme respects, as arguments of `build_weights`: a maximum weight and a
  minimum holding count.  Each is a lever a later experiment has to earn by beating the book
  without it.
- The two timing helpers that cannot be forgotten if they live here: lag the eligibility so the
  set used on rebalance date t is the one observed at t-1, and rebalance only on the dates that set
  changes -- a signal that has not moved is not a reason to pay commission.
- Causality by construction.  A weigher never sees a date, only a history already cut off, so it
  cannot reach into the future even by accident.

It produces the `REBALANCE_DATES x securities` target weights the rule cell hands to the
diagnostics and the weight file.

It prevents a good signal in a portfolio nobody could hold -- and a weighting difference that reads
as a signal difference because each notebook invented its own sizing.
"""

# --- example: begin ---

import dataclasses
import importlib.util

import pandas

__all__ = [
    "CASH_KEY",
    "LIBRARY_INSTALLED",
    "SlotSettings",
    "build_slot_book",
    "build_weights",
    "first_trading_days",
    "lag_eligibility",
    "select_rebalance_dates",
    "weigh",
]

# The key the slot book keeps its uninvested weight under; never a security's name.
CASH_KEY = "__cash__"
# KaxaNuk's own library, installed by hand rather than by `uv sync`.  Equal weight needs nothing,
# so the module stays usable without it and says so instead of failing on import.
LIBRARY_INSTALLED = importlib.util.find_spec("kaxanuk.portfolio_construction") is not None



@dataclasses.dataclass(frozen=True)
class SlotSettings:
    """
    The settings of a book that sells on a signal and fills the slot it frees.

    `decision_dates`, when given, are the only dates the book may trade on, which is how a control
    is held to the rule's own dates: it is evaluated on them and drifts in between.
    """

    book_size: int
    buffer_rank: int
    reequalise_dates: "pandas.DatetimeIndex"
    decision_dates: "pandas.DatetimeIndex | None" = None


def build_slot_book(
    eligible: "pandas.DataFrame",
    ranking: "pandas.DataFrame",
    returns: "pandas.DataFrame",
    cash_returns: "pandas.Series",
    settings: "SlotSettings",
) -> "pandas.DataFrame":
    """
    Build a book of fixed slots that sells a name the day it stops being eligible.

    Every input is already lagged, so a book struck on a date uses what was known the day before.
    On each date, in order: a holding that is no longer eligible is sold; on a re-equalisation date
    a holding ranked below the buffer is sold too; the freed slots are filled from the top of the
    ranking with names not held; and on a re-equalisation date every holding is set back to equal
    weight.  Between trades the holdings drift with their prices, so a date that trades nobody
    records no target, and a date that sells one name leaves the other weights where the market
    put them.  An entrant takes an equal slot, or the cash available split among the entrants when
    that is less, and what is left waits in cash for the next re-equalisation.

    Returns the target weights on every date the book traded, positions across, cash left out: the
    engine's weight file puts the residual in the cash proxy.
    """
    held = {
        CASH_KEY: 1.0,
    }
    targets = {}
    decision_dates = (
        set(settings.decision_dates)
        if settings.decision_dates is not None
        else None
    )
    reequalise_dates = set(settings.reequalise_dates)

    for date in eligible.index:
        starting = len(targets) == 0
        deciding = decision_dates is None or date in decision_dates

        if starting or deciding:
            traded = _decide_date(
                held,
                eligible.loc[date],
                ranking.loc[date],
                starting or date in reequalise_dates,
                settings,
            )

            if traded:
                targets[date] = _without_cash(held)

        _drift(
            held,
            returns.loc[date],
            cash_returns.get(date, 0.0),
        )

    frame = pandas.DataFrame.from_dict(
        targets,
        orient="index",
    )
    # The frame's rows come back in the order the names first appear, not in date order: sorted
    # here, because every reader of a book -- turnover, the latest target, a window's opening
    # book -- takes its rows in sequence.
    in_date_order = frame.sort_index()
    aligned = in_date_order.reindex(columns=eligible.columns)

    return aligned.fillna(0.0)


def build_weights(
    eligibility: "pandas.DataFrame",
    returns: "pandas.DataFrame",
    rebalance_dates: "pandas.DatetimeIndex",
    method: str,
    maximum_weight: float | None,
    minimum_holdings: int,
) -> "pandas.DataFrame":
    """
    Build the target book on each rebalance date, one weigher call per date.

    The history handed to the weigher is cut off strictly before the date it is sizing, so a method
    that estimates anything from returns cannot reach into the future even by accident.  A date
    with fewer eligible securities than the minimum holds nothing at all: a book of four names is
    not a small version of a book of thirty, it is a different bet.
    """
    rows = {}

    for date in rebalance_dates:
        eligible = eligibility.loc[date]
        selected = tuple(eligible[eligible].index)

        if len(selected) < minimum_holdings:
            rows[date] = pandas.Series(
                0.0,
                index=eligibility.columns,
            )

            continue

        history = returns.loc[returns.index < date, list(selected)]
        sized = weigh(
            selected,
            history,
            method,
            maximum_weight,
        )
        aligned = sized.reindex(eligibility.columns)
        rows[date] = aligned.fillna(0.0)

    return pandas.DataFrame(rows).transpose()


def first_trading_days(
    dates: "pandas.DatetimeIndex",
    frequency: str,
) -> "pandas.DatetimeIndex":
    """
    The first trading day of each month or quarter in the calendar, or none at all.

    `frequency` is `month`, `quarter` or `never`.  Taken from the dates the panel actually has, so a
    holiday on the first of the month moves the day rather than skipping it.
    """
    if frequency == "never":

        return pandas.DatetimeIndex([])

    period_code = "M" if frequency == "month" else "Q"
    periods = dates.to_period(period_code)
    series = pandas.Series(
        dates,
        index=dates,
    )
    firsts = series.groupby(periods).min()

    return pandas.DatetimeIndex(firsts.to_numpy())


def lag_eligibility(
    eligibility: "pandas.DataFrame",
) -> "pandas.DataFrame":
    """
    Shift the eligible set by one day, so a book struck on date t uses what was known at t-1.

    This is the one causal cut in the whole pipeline, and it lives here because a rule cell that
    has to remember it is a rule cell that will one day forget.
    """

    shifted = eligibility.shift(
        1,
        fill_value=False,
    )

    return shifted.astype(bool)


def select_rebalance_dates(
    eligibility: "pandas.DataFrame",
    band: float,
    held: "pandas.DataFrame | None" = None,
) -> "pandas.DatetimeIndex":
    """
    Keep only the dates on which the target set has moved far enough from the one before it.

    Distance is the share of the book a move would trade: with equal weights, three names out of
    thirty is ten percent.  A signal that has not moved is not a reason to pay commission, which is
    what the band is for; `held` is accepted so a later experiment can measure drift against the
    book actually held rather than against the previous target.
    """
    reference = eligibility if held is None else held
    previous = reference.shift(1)
    changed = (reference != previous).sum(axis=1)
    holdings = reference.sum(axis=1)
    # A date holding nothing has no book to measure a move against, so it always counts as a move:
    # dividing by it would be a zero denominator, and treating it as "nothing changed" would leave
    # the book stuck out of the market.
    measurable = holdings.where(holdings > 0)
    turnover = (changed / measurable).fillna(1.0)
    triggered = turnover >= band
    triggered.iloc[0] = True

    return eligibility.index[triggered]


def weigh(
    selected: tuple[str, ...],
    history: "pandas.DataFrame",
    method: str,
    maximum_weight: float | None,
) -> "pandas.Series":
    """
    Size one date's eligible set, by the named method, on the history already cut.

    Equal weight is computed here because it needs nothing but the set; every other method is the
    library's, built fresh for this date.  A cap is applied by trimming and leaving the excess in
    cash rather than redistributing it, so a cap can never quietly concentrate the book further.
    """
    if method == "equal_weight":
        weights = pandas.Series(
            1.0 / len(selected),
            index=list(selected),
        )
    elif not LIBRARY_INSTALLED:
        missing_library_message = (
            f"{method!r} needs the Portfolio Construction library; only equal_weight runs alone"
        )

        raise ModuleNotFoundError(missing_library_message)
    else:
        import pyarrow

        import kaxanuk.portfolio_construction.entities
        import kaxanuk.portfolio_construction.sizing

        # The library reads a wide table -- a `date` column, then one column per security -- and
        # sizes the snapshot of tickers it is handed.  Every argument is keyword-only.
        dated_history = history.rename_axis("date")
        history_table = pyarrow.Table.from_pandas(
            dated_history.reset_index(),
            preserve_index=False,
        )
        allocator = kaxanuk.portfolio_construction.sizing.build_allocator(
            name=method,
            returns=history_table,
        )
        eligible_table = pyarrow.table(
            {
                "ticker": list(selected),
            }
        )
        snapshot = kaxanuk.portfolio_construction.entities.UniverseSnapshot(
            table=eligible_table,
        )
        allocated = allocator.allocate(
            snapshot=snapshot,
        )
        allocated_weights = kaxanuk.portfolio_construction.entities.Weights.from_allocated(
            allocated=allocated,
        )
        weights = pandas.Series(
            allocated_weights.as_mapping(),
        )

    if maximum_weight is None:

        return weights

    return weights.clip(upper=maximum_weight)


def _decide_date(
    held: dict[str, float],
    eligible_row: "pandas.Series",
    ranking_row: "pandas.Series",
    reequalising: bool,
    settings: "SlotSettings",
) -> bool:
    """
    Apply one date's sales and purchases to the holdings in place, and say whether anything traded.
    """
    eligible_names = eligible_row[eligible_row].index
    ranked = ranking_row.reindex(eligible_names)
    standing = ranked.dropna().sort_values(ascending=False)
    places = {
        name: place
        for place, name in enumerate(standing.index, start=1)
    }
    stocks = [
        name
        for name in held
        if name != CASH_KEY
    ]
    leaving = [
        name
        for name in stocks
        if name not in places or (reequalising and places[name] > settings.buffer_rank)
    ]

    for name in leaving:
        held[CASH_KEY] += held.pop(name)

    open_slots = settings.book_size - (len(held) - 1)
    candidates = [
        name
        for name in standing.index
        if name not in held
    ]
    entering = candidates[:max(open_slots, 0)]

    if reequalising:
        _reequalise(
            held,
            entering,
            settings.book_size,
        )

        return True

    if len(entering) > 0:
        slot = 1.0 / settings.book_size
        share = min(
            slot,
            held[CASH_KEY] / len(entering),
        )

        for name in entering:
            held[name] = share
            held[CASH_KEY] -= share

    return len(leaving) > 0 or len(entering) > 0


def _drift(
    held: dict[str, float],
    returns_row: "pandas.Series",
    cash_return: float,
) -> None:
    """
    Let the holdings move with the day's returns, in place: each weight is the one the market left.
    """
    grown = {}

    for name, weight in held.items():
        daily = cash_return if name == CASH_KEY else returns_row.get(name, 0.0)
        growth = 1.0 if pandas.isna(daily) else 1.0 + daily
        grown[name] = weight * growth

    total = sum(grown.values())

    for name, value in grown.items():
        held[name] = value / total


def _reequalise(
    held: dict[str, float],
    entering: list[str],
    book_size: int,
) -> None:
    """
    Add the entrants and set every holding to one equal slot, the rest in cash, in place.
    """
    for name in entering:
        held[name] = 0.0

    stocks = [
        name
        for name in held
        if name != CASH_KEY
    ]

    for name in stocks:
        held[name] = 1.0 / book_size

    held[CASH_KEY] = 1.0 - len(stocks) / book_size


def _without_cash(
    held: dict[str, float],
) -> dict[str, float]:
    """
    The holdings as a target row: every stock's weight, and no cash key.
    """

    return {
        name: weight
        for name, weight in held.items()
        if name != CASH_KEY
    }


# --- example: end ---
