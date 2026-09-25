"""
Securities panel -- steps 4 to 6 of 8, the first of four modules shared by every experiment.  It
turns the refined files into the matrices a rule is written against.

In plain words: one loader, so every experiment measures the same universe the same way.  A
notebook that reads the panel its own way has broken the comparison before the rule is written.

Runs inside an experiment notebook, after `Data/refinery.py` has written
`Data/Refinery/Time_Series/`.

What is expected here:

- Read every refined file for a security in `Universe/Investable_Universe.csv`, and only those --
  the cash proxy and the benchmarks sit in the Curator folder for the engine, not for the
  cross-section.
- Key positions by security, not by listing.  A point-in-time universe contains renamed securities
  -- two identifiers sharing one ISIN, each carrying part of the history -- and left alone they
  become two positions and a double-counted company at the changeover.  Stitch the legs; where two
  overlap on a date, the one still reporting later is the surviving listing.
- Pivot the long panel into one wide `dates x securities` matrix per column the notebook asks for:
  the signal, the mark price, the fill price, and whatever else the rule reads.  A matrix per input
  is what lets the whole rule be a handful of whole-matrix statements instead of a loop over files.
- Name no strategy column.  The columns to load arrive as arguments from the notebook's setup cell.
  A signal declared here becomes every later experiment's default without anyone deciding it.
- Fail readably: a column the files do not carry is named in the error, not discovered inside a
  read.

It produces the matrices section 1 of every experiment notebook starts from, and nothing on disk.

It prevents two experiments that appear to disagree about a strategy when they only disagree
about how the panel was loaded.
"""

# --- example: begin ---

import csv
import operator
import pathlib

import pandas

__all__ = [
    "expand_to_identifiers",
    "load_matrices",
    "read_investable_identifiers",
    "read_position_keys",
]

DATE_COLUMN = "m_date"
IDENTIFIER_COLUMN = "main_identifier"
REFINERY_DIRECTORY = pathlib.Path(__file__).parent.parent / "Data" / "Refinery" / "Time_Series"
SECURITY_MASTER_PATH = pathlib.Path(__file__).parent.parent / "Universe" / "Security_Master.csv"
SEED_PATH = pathlib.Path(__file__).parent.parent / "Universe" / "Investable_Universe.csv"


def expand_to_identifiers(
    weights: "pandas.DataFrame",
) -> "pandas.DataFrame":
    """
    Rewrite a book keyed by position into one keyed by the listing live on each date.

    The rest of the pipeline thinks in positions, because a company that changed ticker is one bet
    and not two.  The backtest engine thinks in identifiers, because that is what its market-data
    folder is named by.  This is the one place the two meet: a stitched position becomes whichever
    of its listings had a price on the date, so a weight is never written against a ticker that did
    not exist yet or had already gone.
    """
    position_keys = read_position_keys()
    identifiers_by_position = {}

    for identifier, position in position_keys.items():
        listings_so_far = identifiers_by_position.setdefault(position, [])
        listings_so_far.append(identifier)

    positions_in_master = set(position_keys.values())
    positions_in_book = set(weights.columns)
    every_listing = positions_in_master | positions_in_book
    expanded = pandas.DataFrame(
        0.0,
        index=weights.index,
        columns=sorted(every_listing),
    )

    for position in weights.columns:
        listings = identifiers_by_position.get(position, [position])

        if len(listings) == 1:
            expanded[position] = weights[position]

            continue

        spans = []

        for listing in listings:
            path = REFINERY_DIRECTORY / f"{listing}.csv"

            if not path.is_file():
                continue

            dates = pandas.read_csv(
                path,
                usecols=[DATE_COLUMN],
                parse_dates=[DATE_COLUMN],
            )[DATE_COLUMN]
            spans.append((
                dates.max(),
                dates.min(),
                listing,
            ))

        # Ordered by the date each listing stops reporting, so that where two overlap -- the weeks
        # around a ticker change, when both have prices -- the surviving one is written last and
        # wins.  Writing both would put the position in the book twice.
        chosen = pandas.Series(
            None,
            index=weights.index,
            dtype=object,
        )

        for last_date, first_date, listing in sorted(spans):
            live = (weights.index >= first_date) & (weights.index <= last_date)
            chosen[live] = listing

        for last_date, first_date, listing in spans:
            holds = chosen == listing

            if listing not in expanded.columns:
                expanded[listing] = 0.0

            expanded.loc[holds, listing] = weights.loc[holds, position]

    held = expanded.columns[expanded.abs().sum() > 0]

    return expanded[held]


def load_matrices(
    columns: tuple[str, ...],
) -> dict[str, "pandas.DataFrame"]:
    """
    Return one `dates x securities` matrix per column the notebook asks for.

    A matrix per input is what lets a rule be a handful of whole-matrix statements instead of a
    loop over files.  Listings that share an identity are stitched into one position first, so a
    renamed security is one column rather than two half-filled ones, and where two legs overlap the
    one still reporting later wins.
    """
    investable = read_investable_identifiers()
    position_keys = read_position_keys()
    paths = [
        path
        for path in sorted(REFINERY_DIRECTORY.glob("*.csv"))
        if path.stem in investable
    ]

    if len(paths) == 0:
        empty_folder_message = (
            f"no refined files in {REFINERY_DIRECTORY}: run Data/refinery.py first"
        )

        raise FileNotFoundError(empty_folder_message)

    frames = []

    for path in paths:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            header = next(csv.reader(handle), [])

        missing = [
            column
            for column in (DATE_COLUMN, *columns)
            if column not in header
        ]

        if len(missing) > 0:
            missing_columns_message = f"{path.name} does not carry {missing}"

            raise KeyError(missing_columns_message)

        frame = pandas.read_csv(
            path,
            usecols=[DATE_COLUMN, *columns],
            parse_dates=[DATE_COLUMN],
        )
        frame[IDENTIFIER_COLUMN] = position_keys.get(path.stem, path.stem)
        frame["last_reported"] = frame[DATE_COLUMN].max()
        frames.append(frame)

    panel = pandas.concat(
        frames,
        ignore_index=True,
    )
    ordered = panel.sort_values([
        DATE_COLUMN,
        "last_reported",
    ])
    matrices = {}

    for column in columns:
        matrix = ordered.pivot_table(
            index=DATE_COLUMN,
            columns=IDENTIFIER_COLUMN,
            values=column,
            aggfunc="last",
        )
        matrices[column] = matrix.sort_index()

    return matrices


def read_investable_identifiers() -> frozenset[str]:
    """
    Read the seed, which decides membership here as it does everywhere else.

    The cash proxy and the benchmark sit in the Curator's folder because the engine prices from one
    directory; neither belongs in a cross-section, and neither is in the seed.
    """
    with SEED_PATH.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        identifiers = {
            row[IDENTIFIER_COLUMN].strip()
            for row in reader
            if row.get(IDENTIFIER_COLUMN, "").strip()
        }

    return frozenset(identifiers)


def read_position_keys() -> dict[str, str]:
    """
    Map each listing onto the position it belongs to, using the master's identity column.

    Two identifiers sharing an ISIN are one company that changed ticker, and left alone they become
    two positions and a double-counted bet at the changeover.  Where the master has no identity
    column the mapping is empty and every listing stands alone, which is correct: the seed has said
    nothing about identity, so nothing may be assumed.
    """
    if not SECURITY_MASTER_PATH.is_file():

        return {}

    with SECURITY_MASTER_PATH.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)

        if "isin" not in (reader.fieldnames or ()):

            return {}

        rows = [
            row
            for row in reader
            if (row.get("isin") or "").strip()
        ]

    first_identifier_by_isin = {}
    position_keys = {}

    by_identifier = operator.itemgetter(IDENTIFIER_COLUMN)

    for row in sorted(rows, key=by_identifier):
        isin = row["isin"].strip()
        first_identifier_by_isin.setdefault(isin, row[IDENTIFIER_COLUMN])
        position_keys[row[IDENTIFIER_COLUMN]] = first_identifier_by_isin[isin]

    return position_keys


# --- example: end ---
