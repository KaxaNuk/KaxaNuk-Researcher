"""
The paper-trading record -- step 7 of 8.  Where each run of `daily_update.py` writes what it saw,
and the one place that decides how a record is kept: in files, in a database, or both.

In plain words: a paper book's history is evidence only if nobody can quietly rewrite it.  Every
row is keyed, so a second run of the same day replaces that day's rows instead of adding to them,
and a past value the engine now prices differently is flagged as a restatement, never overwritten.

Six tables, each keyed by the columns named here:

    runs         book, as_of                              the commit, the status, the manifest
    books        book, as_of, series, identifier          the target weights in force that day
    performance  book, window, series, date               the engine's daily value and return
    statistics   book, as_of, window, series, statistic   the engine's summary figures
    diagnostics  book, date, measure                      what the book looked like that day
    flags        book, as_of, kind, detail                everything outside its band, every
                                                          failed check, every restatement

`window` is `whole`, from the experiment's first day, or `since_freeze`, from the day the book was
frozen; `series` is `book`, `control` or `benchmark`.

Two sinks, chosen in `Config/.env` by `PAPER_TRADING_SINKS`: `local` writes the tables as CSV files
under `Paper_Trading/Record/`, and `database` writes them to the DuckDB database that
`PAPER_TRADING_DATABASE` names -- a file, or a PostgreSQL server reached through DuckDB's
`postgres` extension, written `postgres:<connection string>`.  A local record is not regenerable:
the provider restates its history, so a day's inputs cannot be fetched again as they were.  Local
alone is not a backup.

With `PAPER_TRADING_PUBLISH_DATA`, the refreshed price files go into the database too, as the
table `market_data`, so a machine with `PAPER_TRADING_INPUT=database` runs every book from them
without a download or a data key.

Nothing here computes a performance figure: `performance` and `statistics` hold what the engine
returned, and nothing else.
"""
