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
  scheme -- equal weight, or any sizing method the library registers: inverse volatility, risk
  parity, hierarchical risk parity, a minimum-variance optimiser -- is the same shape, so swapping
  one for another is one line in the rule cell and nothing else in the notebook moves.  That is what
  makes two experiments comparable rather than merely adjacent.
- The library inside the signature, never around it.  Build one of its methods per rebalance date,
  on the history already cut: a method that estimates from returns uses whatever history it was
  built with, and the library's own pipeline builds each method once for every date.  Import it
  inside a guard -- it is KaxaNuk's own library, installed by hand -- and report and skip a method
  that needs it when it is absent.  Equal weight needs nothing.
- At most one, not exactly one.  A strategy that can go to cash cannot satisfy the stricter form;
  the residual becomes a real, priced cash position when the weight file is written.
- The constraints every scheme respects, switched off by default: a maximum weight, a minimum
  holding count, a lookback for anything that estimates risk.  Each is a lever a later experiment
  has to earn by beating the book without it.
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

import importlib.util

import pandas

__all__ = [
    "LIBRARY_INSTALLED",
    "build_weights",
    "lag_eligibility",
    "select_rebalance_dates",
    "weigh",
]

# KaxaNuk's own library, installed by hand rather than by `uv sync`.  Equal weight needs nothing,
# so the module stays usable without it and says so instead of failing on import.
LIBRARY_INSTALLED = importlib.util.find_spec("kaxanuk.portfolio_construction") is not None


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
        import kaxanuk.portfolio_construction

        allocator = kaxanuk.portfolio_construction.build_allocator(
            method,
            history,
        )
        weights = pandas.Series(allocator.weights)

    if maximum_weight is None:

        return weights

    return weights.clip(upper=maximum_weight)


# --- example: end ---
