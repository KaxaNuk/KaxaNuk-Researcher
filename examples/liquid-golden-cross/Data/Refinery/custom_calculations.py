"""
The `r_*` columns -- step 3 of 8, computed by the Data Refinery over the whole cross-section.

Two kinds of column live here, and only here:

1.  Anything that compares securities against each other on a date -- a rank, a breadth reading, a
    share of the cross-section.  No per-security calculation can express it.
2.  Anything with a setting an experiment will sweep, even when it is per-security -- a fitted
    model, or a window such as a twelve-month return's.  Widening the Curator's schema costs a
    refetch of every identifier, and a sweep must never cost a download, so the frozen inputs stay
    in the Curator and the column with the setting lives here.

What is expected here is one function per column, named exactly as the column, resolved by
parameter name the same way the Curator resolves its own.  Every parameter is a column of the
panel -- the date, `main_identifier`, any `c_*` or `r_*` column, any `current_*` column -- and a
function may group by any of them.  The column is registered by listing it in this module's output
tuple; nothing else registers it.

One requirement this module exists to enforce: causality.  Every cross-sectional column on date t
uses only the cross-section as of t, and every rolling window looks strictly backward.  A rank
taken over the pooled sample, or a mean over the whole history, would leak the future distribution
into every row and would not raise a single error doing it.

Rank convention: every `*_rank` column is a per-date percentile, ascending, so 1.0 is the highest
raw value in that day's cross-section.  A percentile over n values averages to (n + 1) / 2n, not to
0.5 -- 0.542 on 12 securities, 0.5006 on 800.  A check written against 0.5 fails on every date of
a narrow universe and passes on a wide one, which is the worst possible failure mode; check against
the identity.

The minimum that ships in a filled-in repository: a per-date liquidity rank, the universe size on
each date (the denominator behind every rank), and one worked example of per-date normalisation.
A column that reads a `current_*` column is marked as such, so the refinery can skip it before the
security master exists.

It produces the `r_*` columns in every file under `Data/Refinery/Time_Series/`.

It prevents a signal that knew the future distribution, and a rank that was silently pooled.
"""

# --- example: begin ---

import pandas

__all__ = [
    "CLASSIFICATION_DEPENDENT_COLUMNS",
    "REFINERY_COLUMNS",
    "r_liquidity_rank",
    "r_momentum_12_1",
    "r_trend_50_200",
    "r_universe_size",
]

# Both windows live here rather than in the Curator because a later experiment sweeps them, and a
# sweep must never cost a download.
LONG_WINDOW_DAYS = 200
# The twelve-month return skips the most recent month, which reverses rather than persists; both
# lags are trading days, and a later experiment sweeps them.
MOMENTUM_SKIP_DAYS = 21
MOMENTUM_WINDOW_DAYS = 252
SHORT_WINDOW_DAYS = 50
# The columns this module produces, in the order the driver builds them.  A column may read any
# column built before it.
REFINERY_COLUMNS = (
    "r_universe_size",
    "r_liquidity_rank",
    "r_trend_50_200",
    "r_momentum_12_1",
)
# The subset that needs `Universe/Security_Master.csv`, so the refinery still runs before the
# universe notebook has written one.  This strategy groups by nothing, so the subset is empty.
CLASSIFICATION_DEPENDENT_COLUMNS = ()


def r_liquidity_rank(
    m_date: "pandas.Series",
    c_daily_traded_value_sma_63d: "pandas.Series",
) -> "pandas.Series":
    """
    Rank each security's quarter-long average traded value against that day's cross-section.

    The rank is what "most traded" means once it has to be measured: a percentile inside the day,
    so a dollar figure that grows with the market over twenty years stays comparable with itself.
    Ranking within the date is also what keeps it causal -- a rank taken over the pooled sample
    would know the whole history's distribution and would not raise a single error doing it.
    """
    traded_value_by_date = c_daily_traded_value_sma_63d.groupby(m_date)

    return traded_value_by_date.rank(
        pct=True,
        ascending=True,
    )


def r_momentum_12_1(
    main_identifier: "pandas.Series",
    m_close_dividend_and_split_adjusted: "pandas.Series",
) -> "pandas.Series":
    """
    Measure each security's total return over the twelve months before the most recent one.

    The price a month ago over the price a year ago, less one, on the total-return series: both
    look strictly backward, so the column on date t knows nothing after t - 21.  The most recent
    month is left out because over that horizon returns reverse rather than persist.  The first 252
    rows of every security are null, the warm-up, never a zero return.
    """
    panel = pandas.DataFrame({
        "identifier": main_identifier,
        "price": m_close_dividend_and_split_adjusted,
    })
    prices_by_security = panel.groupby("identifier")["price"]
    month_ago = prices_by_security.shift(MOMENTUM_SKIP_DAYS)
    year_ago = prices_by_security.shift(MOMENTUM_WINDOW_DAYS)

    return month_ago / year_ago - 1


def r_trend_50_200(
    main_identifier: "pandas.Series",
    m_close_dividend_and_split_adjusted: "pandas.Series",
) -> "pandas.Series":
    """
    Measure how far the 50-day average sits above the 200-day one, as a fraction.

    Positive means the filter is on for that security on that date; the rule reads only the sign,
    but the distance is kept because it costs nothing and a later experiment can rank on it. The
    first 199 rows of every security are null, which is the warm-up rather than a downtrend, and
    keeping them null is what stops a young listing being read as one.
    """
    panel = pandas.DataFrame({
        "identifier": main_identifier,
        "price": m_close_dividend_and_split_adjusted,
    })
    prices_by_security = panel.groupby("identifier")["price"]
    short_rolling = prices_by_security.rolling(SHORT_WINDOW_DAYS).mean()
    long_rolling = prices_by_security.rolling(LONG_WINDOW_DAYS).mean()
    short_average = short_rolling.reset_index(
        level=0,
        drop=True,
    )
    long_average = long_rolling.reset_index(
        level=0,
        drop=True,
    )

    return short_average / long_average - 1


def r_universe_size(
    m_date: "pandas.Series",
) -> "pandas.Series":
    """
    Count the securities present on each date, which is the denominator behind every rank.

    A percentile over a narrow cross-section means something different from one over a wide one, so
    the count travels beside the rank instead of being reconstructed later by whoever reads it.
    """
    dates = m_date.groupby(m_date)

    return dates.transform("size")


# --- example: end ---
