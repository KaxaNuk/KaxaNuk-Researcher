"""
<Module title> -- <one-line description>.

Custom Data Curator calculations.  Every function whose name starts with `c_` becomes an output
column with that same name, and each of its parameters is injected with the data of the column
named after it.

Place this module where the project's caller of `main()` loads it from: the library-standard
location is `Config/custom_calculations.py`, but projects with their own multi-module layout have
their own rules, and a notebook can skip files entirely by attaching these functions to an
in-memory module (see `programmatic-run.md`).  In a KaxaNuk Strategy Template repository the module
is `Data/Curator/custom_calculations.py`, and the column is selected among the output columns
`Data/curator.py` requests.  Either way, remember to also select the column: the `Output_Columns`
sheet of `Config/data_curator_parameters.xlsx` in the standard setup, or the `columns` tuple of the
`Configuration` when calling `main()` directly.

Written in a KaxaNuk strategy's style, Bloom Code at 100 columns: qualified imports, a quoted hint
on every parameter and return, and prose docstrings that keep the formula.  As the documentation
says, each parameter is filled with the column it is named after, so a project with another style
keeps the names and changes the rest.

Delete the examples below once the real calculations are written.
"""

import pyarrow
import pyarrow.compute

import kaxanuk.data_curator
import kaxanuk.data_curator.exceptions
import kaxanuk.data_curator.features.helpers

__all__ = [
    "c_example_annualized_volatility_21d",
    "c_example_momentum_21d_dividend_and_split_adjusted",
    "c_example_sales_to_price",
]


def c_example_annualized_volatility_21d(
    c_log_returns_dividend_and_split_adjusted: "kaxanuk.data_curator.DataColumn",
) -> "kaxanuk.data_curator.DataColumn":
    """
    Calculate the 21-day annualized volatility, composing a calculated column and a helper.

    The parameter is the built-in column of the same name, the log returns of the
    dividend-and-split-adjusted close prices, so nothing is recomputed:

        annualized volatility = standard deviation of the log returns over 21 rows * sqrt(252)

    The first 21 rows are null: the first log return is null, so the window holds 21 returns only
    from the 22nd row on.
    """
    volatility = kaxanuk.data_curator.features.helpers.annualized_volatility(
        column=c_log_returns_dividend_and_split_adjusted,
        days=21,
    )

    return volatility


def c_example_momentum_21d_dividend_and_split_adjusted(
    m_close_dividend_and_split_adjusted: "kaxanuk.data_curator.DataColumn",
) -> "kaxanuk.data_curator.DataColumn":
    """
    Calculate the 21-day momentum of the dividend-and-split-adjusted close prices.

        momentum_t = P_t / P_(t-21) - 1

    The first 21 rows are null, as there is no price 21 rows earlier.  The ratio is taken between
    two slices of the column, which leaves it 21 rows short, so the result is padded back to the
    column's length with nulls on the leading rows.
    """
    shifted_ratio = (
        m_close_dividend_and_split_adjusted[21:]
        / m_close_dividend_and_split_adjusted[:-21]
    )
    ratio_array = shifted_ratio.to_pyarrow()
    momentum = pyarrow.compute.subtract(
        ratio_array,
        1,
    )
    padding = pyarrow.array(
        [None] * 21,
        type=momentum.type,
    )
    output = pyarrow.concat_arrays([
        padding,
        momentum,
    ])
    output_column = kaxanuk.data_curator.DataColumn.load(output)
    result = kaxanuk.data_curator.features.helpers.replace_infinite_with_none(output_column)

    return result


def c_example_sales_to_price(
    c_market_cap: "kaxanuk.data_curator.DataColumn",
    fis_revenues: "kaxanuk.data_curator.DataColumn",
    configuration: "kaxanuk.data_curator.entities.Configuration",
) -> "kaxanuk.data_curator.DataColumn":
    """
    Calculate the sales to price ratio, showing a fundamentals-dependent, period-aware calculation.

        sales to price_t = revenues_t / market cap_t

    The revenues come from the income statement, and the market capitalization from the built-in
    column of the same name.  Fundamental data means the run needs a fundamental data provider, and
    the values depend on the configured period, which the `configuration` parameter carries: a
    period other than annual or quarterly is rejected.  Fundamental values are infilled forward
    from each filing, so consecutive rows repeat.  The ratio is null wherever either input is null,
    and wherever the market capitalization is zero.
    """
    if configuration.period not in ("annual", "quarterly"):
        message = f"c_example_sales_to_price failed, unexpected period type: {configuration.period}"

        raise kaxanuk.data_curator.exceptions.CalculationError(message)

    # DataColumn division already yields null on zero denominators and on null operands.
    sales_to_price = fis_revenues / c_market_cap

    return sales_to_price


def _example_private_helper(
    *,
    column: "kaxanuk.data_curator.DataColumn",
    days: int,
) -> "kaxanuk.data_curator.DataColumn":
    """
    Shape a private helper like this: no `c_` prefix, so it never becomes a column.

    It sums the column over a rolling window of `days` rows, leaving the first `days - 1` rows null.
    """
    series = column.to_pandas()
    window = series.rolling(days)
    rolling_sum = window.sum()
    result = kaxanuk.data_curator.DataColumn.load(rolling_sum)

    return result
