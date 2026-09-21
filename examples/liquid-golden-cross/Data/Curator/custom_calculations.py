"""
The `c_*` columns -- step 3 of 8, computed by the Data Curator while it downloads.

`c_*` means one security's own history and nothing else.  The Curator works one identifier at a
time, so anything that compares securities against each other belongs one stage later, in
`Data/Refinery/custom_calculations.py`, as an `r_*` column.

What is expected here is one function per column, named exactly as the column:

- Each function's parameters are named after the columns it reads -- a provider column such as the
  dividend-and-split adjusted close, or another `c_*` column.  The Curator resolves the dependency
  order from the signatures, so the order of definition here does not matter.
- Each returns a column of the same length.  Prices arrive as fixed-point decimals; anything
  statistical casts to float once, at the boundary.
- A column is registered by listing it among the output columns `Data/curator.py` requests.
  Nothing else registers it.

The minimum a backtest needs -- and the first two pairs are never removed:

- the cumulative split ratio and the dividend-and-split ratio, recovered from the adjusted and
  unadjusted closes;
- the unadjusted VWAP, on which per-share commission is charged, and the dividend-and-split
  adjusted VWAP, the fill price;
- the one-day total return, because nearly every feature is built on it;
- a liquidity measure -- average daily traded value over about a quarter -- because capacity is a
  question every strategy has to answer.

Widening the schema changes every file's header, so the next run refetches every identifier.  That
is intended, because it is what stops the folder holding a mix of schemas, and it makes this the
wrong home for anything you intend to tune.  Put a model's frozen arithmetic inputs here and the
model itself in the Refinery: a sweep must never cost a download.

It produces the `c_*` columns in every file under `Data/Curator/Time_Series/`.

It prevents a feature computed on a price basis it should not use -- a plausible number and no
error.
"""

# --- example: begin ---

import kaxanuk.data_curator

__all__ = [
    "c_dividend_and_split_ratio",
    "c_split_ratio",
    "c_vwap",
    "c_vwap_dividend_and_split_adjusted",
]


def c_dividend_and_split_ratio(
    m_close_dividend_and_split_adjusted: "kaxanuk.data_curator.DataColumn",
    m_close: "kaxanuk.data_curator.DataColumn",
) -> "kaxanuk.data_curator.DataColumn":
    """
    Recover the combined dividend-and-split adjustment from the two close columns.

    The provider sends adjusted and unadjusted prices but never the factor between them, and the
    backtest needs it to move between a total-return series and the price actually quoted that day.
    """

    return m_close_dividend_and_split_adjusted / m_close


def c_split_ratio(
    m_close_split_adjusted: "kaxanuk.data_curator.DataColumn",
    m_close: "kaxanuk.data_curator.DataColumn",
) -> "kaxanuk.data_curator.DataColumn":
    """
    Recover the cumulative split adjustment the same way, splits alone.

    It converts a split-adjusted quantity back into the shares a person would have traded on the
    day, which is what per-share commission is charged on.
    """

    return m_close_split_adjusted / m_close


def c_vwap(
    m_vwap_split_adjusted: "kaxanuk.data_curator.DataColumn",
    c_split_ratio: "kaxanuk.data_curator.DataColumn",
) -> "kaxanuk.data_curator.DataColumn":
    """
    Rebuild the unadjusted volume-weighted average price, which this provider leaves empty.

    Dividing the split-adjusted VWAP by the split ratio puts it back in the day's own share terms,
    so commission is charged on a price that existed.
    """

    return m_vwap_split_adjusted / c_split_ratio


def c_vwap_dividend_and_split_adjusted(
    c_vwap: "kaxanuk.data_curator.DataColumn",
    c_dividend_and_split_ratio: "kaxanuk.data_curator.DataColumn",
) -> "kaxanuk.data_curator.DataColumn":
    """
    Put the rebuilt VWAP on the total-return basis, which is the price a fill is booked at.

    Every return in the experiment runs on that basis, so the fill price has to share it, or the
    book earns a return the prices never showed.
    """

    return c_vwap * c_dividend_and_split_ratio


# --- example: end ---
