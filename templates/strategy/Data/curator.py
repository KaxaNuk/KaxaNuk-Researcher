"""
Data Curator -- step 3 of 8, block 1 of 3.  The only file in this repository that downloads time
series from a data provider.  `Universe/universe.ipynb` asks the same provider what each security
*is* -- name, type, exchange, currency, inception -- and caches that payload in
`Universe/Provider_Cache/`; nothing else talks to a provider.

In plain words: you describe the data you want -- provider, identifiers, dates and columns -- and
the KaxaNuk Data Curator fetches it, aligns the calendar, handles splits and dividends, and writes
one file per identifier, the same way every run.

Runs first.  Nothing has to exist before it except `Universe/Investable_Universe.csv` and a
provider key in `Config/.env`.  `Universe/universe.ipynb` profiles what this writes.

What is expected here is a short driver, not a framework:

- Read the identifiers from `Universe/Investable_Universe.csv`, column `main_identifier`.  The
  seed is the authority on what exists, so it drives the download.
- Build one Data Curator configuration: the date window, those identifiers, and the output columns
  -- the provider's `m_*` columns plus the `c_*` columns defined in
  `Data/Curator/custom_calculations.py`.  Fix the end date rather than using today, so two people
  running a week apart get comparable files.
- Take a later end date as an argument, `--end-date`, for the one caller that needs today's data:
  `Paper_Trading/daily_update.py`.  A refresh refetches each file whole, because a fresh pull
  rebases every adjusted column from the present, and remembers the date each file was fetched
  through, so a run that stops half way resumes where it stopped.
- Call the public library once -- `kaxanuk-data-curator`, already installed by `uv sync` from
  `pyproject.toml`, imported as `kaxanuk.data_curator`.  It loops over the identifiers, skips one
  that fails and says why, and writes `<identifier>.csv` for each.
- Point its output at `Data/Curator/Time_Series/`.  The library's default folder is `Output/`;
  here every stage has one home, and this is the Curator's.
- A provider's history can stop where its coverage does: a name that left the market years ago may
  be missing from it altogether.  Fetch such names from a second provider that carries them, into
  the same files and columns, and say in the strategy's documents which names came from where and
  how any column the second provider lacks was filled.

Two groups ride along in the same folder although they are not in the seed: a cash proxy, because
a book that goes to cash has to hold a real priced instrument, and the benchmarks the strategy is
reported against.  The backtest engine prices everything from one directory, so a benchmark filed
anywhere else is a benchmark it cannot price.  Neither enters the cross-section, because
`Data/refinery.py` takes membership from the seed.

Three adjustment families arrive from the provider and each does a different job.  Carry all
three: an unused column costs bytes, a missing one costs a refetch of every identifier.

    unadjusted            recovers the split and dividend ratios; commission is charged on it
    split-adjusted        traded value, which is liquidity in today's share terms
    dividend-and-split    the total-return series a signal and the backtest P&L run on

An index's daily holdings and returns, and a factor model's returns, are not sold by any price
provider: they arrive from the desk that builds them, and `Data/hand_supplied.py` reads them -- in
place, from the folder `KN_ANALYTICS_PATH` names, or from the drop zones `Benchmarks/` and
`Factors/` beside the time series.  Without them this script still downloads every price and says
the index was not staged; the notebooks stop where they first read it.

Credentials come from `Config/.env` and are never printed -- not into a log line, a notebook
output or a commit.  An exposed key is rotated, not edited out.

It produces `Data/Curator/Time_Series/<identifier>.csv`, `m_*` plus `c_*`, read by
`Universe/universe.ipynb` and `Data/refinery.py`.

It prevents beautiful results that came from broken inputs -- and a dataset nobody else can
rebuild.
"""
