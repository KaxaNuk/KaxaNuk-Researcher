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
