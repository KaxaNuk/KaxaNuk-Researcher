"""
Golden Flow's seed builder, for FMP, Experiment 1's provider.  It wrote
`Universe/Investable_Universe.csv` from the KN US Equity Core's membership, and ships to show how
that seed was built: the seed is committed, and running this script overwrites it.

For each listing that was a member at any time from 2015-01-02, it finds the symbol FMP sells the
listing's prices under and proves it is the same security before it writes it down: by CUSIP
first; by CIK only for a common share that is not a fund; by FMP's search for the security's
CUSIP; and, last, unproved under the index's own ticker.  The universe notebook checks every
symbol against the security's price dates once the Curator has fetched it, because the seed keeps
no record of the proof.  Two listings never share a price file: the stronger proof keeps a
disputed symbol.

A row is a listing whose FMP symbol, verified or not, is the index's own (Sharadar) ticker, departed
or not.  FMP does not carry about 80 of them, and the universe notebook's register names them as
missing files.  A listing with no FMP symbol, or one FMP prices under another ticker, has no row,
and the universe notebook names it as one this repository does not price.  `valid_from` and
`valid_to` are the security's first and last price dates in the index's master of listings; a
listing still trading on the master's last date has no `valid_to`.

It needs that master, `--index-master <path>`, a file of KaxaNuk's Analytics Factory that its
published folders do not hold (ask lab@kaxanuk.mx), and `KNDC_API_KEY_FMP` in `Config/.env`.
FMP profiles are cached in `Universe/Provider_Cache/`.  Another provider means another builder,
with the main identifier KaxaNuk supplies for it.

It produces `Universe/Investable_Universe.csv`, tickers and dates only: `main_identifier`,
`index_identifier`, `valid_from`, `valid_to`.
"""

import argparse
import datetime
import importlib.util
import json
import os
import pathlib
import re
import sys
import time
import types
import urllib.error
import urllib.parse
import urllib.request

import pandas

import kaxanuk.data_curator

__all__ = [
    "main",
]

CACHE_DIRECTORY = pathlib.Path(__file__).parent / "Provider_Cache"
CUSIP_SEARCH_CACHE_PATH = CACHE_DIRECTORY / "cusip_search.json"
HAND_SUPPLIED_PATH = pathlib.Path(__file__).parent.parent / "Data" / "hand_supplied.py"
PROFILE_CACHE_PATH = CACHE_DIRECTORY / "profiles.json"
SEED_PATH = pathlib.Path(__file__).parent / "Investable_Universe.csv"

# The first date whose members the seed must carry: the earliest the window can open.
MEMBERSHIP_FLOOR = datetime.date(
    2015,
    1,
    2,
)

FMP_STABLE_URL = "https://financialmodelingprep.com/stable/"
# Ordered from the strongest proof to the weakest; the order decides who keeps a disputed symbol.
MATCH_STRENGTH = {
    "cusip": 4,
    "cusip search": 3,
    "cik": 2,
    "unverified": 1,
}
# A rate limit is a pause, not an answer: asked again after this many seconds, this many times.
REQUEST_ATTEMPTS = 4
REQUEST_PAUSE_SECONDS = 0.2
THROTTLE_PAUSE_SECONDS = 30
# Preferred shares, units, rights and warrants: never the common share a member is.
NOT_COMMON_PATTERN = re.compile(r"(-P\w*$|\.P\w*$|-W\w*$|\.W\w*$|-U$|\.U$|-R$|\.R$|^\w{4,}[UW]$)")
SEED_COLUMNS = (
    "main_identifier",
    "index_identifier",
    "valid_from",
    "valid_to",
)
SUFFIX_PATTERN = re.compile(r"\d+$")


def main() -> int:
    """
    Build the seed from the index's members since the floor, and say how many keep their ticker.
    """
    parser = argparse.ArgumentParser(description="Build the seed from the index's members.")
    parser.add_argument(
        "--index-master",
        required=True,
        help="the index's master of listings, from KaxaNuk's Analytics Factory, read in place",
    )
    arguments = parser.parse_args()
    kaxanuk.data_curator.load_config_env()
    api_key = os.environ.get("KNDC_API_KEY_FMP", "").strip()

    if api_key == "":
        message = "KNDC_API_KEY_FMP is empty; fill it in Config/.env"

        raise RuntimeError(message)

    hand_supplied = _load_hand_supplied()
    holdings = hand_supplied.read_benchmark_holdings()
    floor = pandas.Timestamp(MEMBERSHIP_FLOOR)
    since_floor = holdings.loc[holdings.index >= floor]
    members = sorted(since_floor.columns[(since_floor > 0).any(axis=0)])
    index_master = pandas.read_csv(
        arguments.index_master,
        dtype=str,
        keep_default_na=False,
    )
    print(f"{len(members)} listings were members on some date from {MEMBERSHIP_FLOOR}", flush=True)
    CACHE_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )
    profiles = _read_json(PROFILE_CACHE_PATH)
    cusip_searches = _read_json(CUSIP_SEARCH_CACHE_PATH)
    claims = []

    for position, listing in enumerate(members, start=1):
        security = _find_security(
            listing,
            index_master,
        )
        claim = _match_listing(
            listing,
            security,
            profiles,
            cusip_searches,
            api_key,
        )
        claims.append(claim)

        if position % 50 == 0 or position == len(members):
            _write_json(
                PROFILE_CACHE_PATH,
                profiles,
            )
            _write_json(
                CUSIP_SEARCH_CACHE_PATH,
                cusip_searches,
            )
            print(f"{position}/{len(members)} listings matched", flush=True)

    seed = _one_to_one(claims)
    opened = _open_live_spans(
        seed,
        index_master,
    )
    ordered = opened.sort_values("index_identifier")
    # A listing with no FMP symbol, or one under another ticker, is left out: the seed is tickers
    # and dates, and its two keys are one ticker.
    same_ticker = ordered[ordered["main_identifier"] == ordered["index_identifier"]]
    same_ticker.to_csv(
        SEED_PATH,
        index=False,
        columns=list(SEED_COLUMNS),
        lineterminator="\n",
    )
    listing_count = len(ordered)
    written_count = len(same_ticker)
    written = f"{written_count} of {listing_count} listings"
    print(f"wrote {SEED_PATH.name}: {written}, whose FMP symbol is the index's own ticker")
    match_counts = same_ticker["match"].value_counts()
    print(match_counts.to_string())

    return 0


def _ask_fmp(
    endpoint: str,
    parameters: dict[str, str],
    api_key: str,
) -> list[dict]:
    """
    One request to FMP's stable API, asked again after a pause when the provider is throttling.

    A refusal that is not a rate limit or a server error is an answer -- the name is unknown -- and
    comes back as an empty list.  The key travels in the request and nowhere else.
    """
    query = urllib.parse.urlencode({
        **parameters,
        "apikey": api_key,
    })
    url = FMP_STABLE_URL + endpoint + "?" + query

    for attempt in range(1, REQUEST_ATTEMPTS + 1):
        time.sleep(REQUEST_PAUSE_SECONDS)

        try:
            with urllib.request.urlopen(url, timeout=60) as response:
                body = response.read()
                payload = json.loads(body.decode("utf-8"))

            return payload if isinstance(payload, list) else []
        except urllib.error.HTTPError as error:
            retryable = error.code == 429 or error.code >= 500

            if error.code == 401:
                message = "FMP rejected the key in Config/.env (HTTP 401); fill a valid one"

                raise RuntimeError(message) from error

            if not retryable:

                return []

            print(f"{endpoint}: HTTP {error.code}, attempt {attempt}; pausing", flush=True)
        except (OSError, ValueError) as error:
            print(f"{endpoint}: {type(error).__name__}, attempt {attempt}; pausing", flush=True)

        time.sleep(THROTTLE_PAUSE_SECONDS)

    exhausted_message = f"FMP did not answer {endpoint} after {REQUEST_ATTEMPTS} attempts"

    raise RuntimeError(exhausted_message)


def _candidate_symbols(
    listing: str,
    security: dict[str, str],
) -> list[str]:
    """
    The FMP symbols a listing may trade under, most likely first, without repeats.
    """
    related = security.get("related_tickers", "").split()
    current = security.get("ticker", "")
    raw_candidates = [
        listing.replace(".", "-"),
        SUFFIX_PATTERN.sub("", listing).replace(".", "-"),
        current.replace(".", "-"),
        *[
            ticker.replace(".", "-")
            for ticker in related
            if not NOT_COMMON_PATTERN.search(ticker)
        ],
    ]
    candidates = [
        candidate
        for candidate in dict.fromkeys(raw_candidates)
        if candidate != ""
    ]

    return candidates


def _claim(
    listing: str,
    security: dict[str, str],
    symbol: str,
    match: str,
) -> dict[str, str]:
    """
    One row of the seed: the listing, the symbol it is matched to, and how, which is reported and
    not written.
    """

    return {
        "index_identifier": listing,
        "last_price_date": security.get("last_price_date", ""),
        "main_identifier": symbol,
        "match": match,
        "valid_from": security.get("first_price_date", ""),
        "valid_to": security.get("last_price_date", ""),
    }


def _cusips(
    security: dict[str, str],
) -> list[str]:
    """
    The security's CUSIPs as the index's master writes them, nine characters each.
    """
    cusips = [
        cusip.strip().upper()
        for cusip in security.get("cusips", "").split()
        if len(cusip.strip()) == 9
    ]

    return cusips


def _find_security(
    listing: str,
    index_master: "pandas.DataFrame",
) -> dict[str, str]:
    """
    The index's master row for a listing: by its ticker, else by the related ticker it once had.

    The holdings keep the ticker a listing had when the file was written; the master keeps today's,
    so a listing renamed since is found among the related tickers.  A listing found nowhere has an
    empty row, and can only be matched as unverified.
    """
    by_ticker = index_master[index_master["ticker"] == listing]

    if len(by_ticker) == 1:

        return by_ticker.iloc[0].to_dict()

    once_had = [
        listing in tickers.split()
        for tickers in index_master["related_tickers"]
    ]
    by_related = index_master[once_had]

    if len(by_related) == 1:

        return by_related.iloc[0].to_dict()

    return {}


def _is_common_share(
    symbol: str,
    profile: dict,
) -> bool:
    """
    Whether an FMP profile describes a common share rather than a fund, a preferred or a unit.
    """
    not_common = bool(NOT_COMMON_PATTERN.search(symbol))
    exchange_traded = bool(profile.get("isEtf"))
    mutual_fund = bool(profile.get("isFund"))

    return not not_common and not exchange_traded and not mutual_fund


def _load_hand_supplied() -> "types.ModuleType":
    """
    Import the reader of the Analytics Factory's files by path, because `Data/` is a folder, not a
    package.
    """
    specification = importlib.util.spec_from_file_location(
        "hand_supplied",
        HAND_SUPPLIED_PATH,
    )
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)

    return module


def _match_listing(
    listing: str,
    security: dict[str, str],
    profiles: dict[str, dict],
    cusip_searches: dict[str, list],
    api_key: str,
) -> dict[str, str]:
    """
    Find the FMP symbol a listing trades under, with the strongest proof available.
    """
    cusips = _cusips(security)
    issuer = security.get("cik", "").lstrip("0")
    candidates = _candidate_symbols(
        listing,
        security,
    )
    current = security.get("ticker", "")
    own_symbols = {
        listing.replace(".", "-"),
        current.replace(".", "-"),
    }
    unprofiled = []

    for symbol in candidates:
        profile = _profile(
            symbol,
            profiles,
            api_key,
        )

        if len(profile) == 0:
            unprofiled.append(symbol)

            continue

        raw_cusip = str(profile.get("cusip") or "")
        profile_cusip = raw_cusip.strip().upper()

        if profile_cusip != "" and profile_cusip in cusips:

            return _claim(
                listing,
                security,
                symbol,
                "cusip",
            )

        raw_issuer = str(profile.get("cik") or "")
        profile_issuer = raw_issuer.lstrip("0")
        same_issuer = issuer != "" and profile_issuer == issuer
        common = _is_common_share(
            symbol,
            profile,
        )

        # The listing's own ticker, or the index's current one, under the same issuer is the
        # security even when the two CUSIP records disagree, as they do after a reorganisation; a
        # related ticker under the same issuer may be a preferred or an older class, so it needs
        # the CUSIP.
        own_or_unrecorded = profile_cusip == "" or symbol in own_symbols

        if same_issuer and common and own_or_unrecorded:

            return _claim(
                listing,
                security,
                symbol,
                "cik",
            )

    for cusip in cusips:
        if cusip not in cusip_searches:
            cusip_searches[cusip] = _ask_fmp(
                "search-cusip",
                {"cusip": cusip},
                api_key,
            )

        symbols = [
            row.get("symbol", "")
            for row in cusip_searches[cusip]
        ]
        found = [
            symbol
            for symbol in symbols
            if symbol != "" and not NOT_COMMON_PATTERN.search(symbol)
        ]

        if len(found) > 0:

            return _claim(
                listing,
                security,
                found[0],
                "cusip search",
            )

    own_symbol = listing.replace(".", "-")

    if own_symbol in unprofiled:

        return _claim(
            listing,
            security,
            own_symbol,
            "unverified",
        )

    return _claim(
        listing,
        security,
        "",
        "no FMP symbol",
    )


def _one_to_one(
    claims: list[dict[str, str]],
) -> "pandas.DataFrame":
    """
    Give each symbol to one listing: the stronger proof, then the security still trading.

    The listing that loses is left with no symbol, and so out of the seed, which the universe
    notebook counts as a member this repository does not price.
    """
    frame = pandas.DataFrame(claims)
    frame["strength"] = frame["match"].map(MATCH_STRENGTH).fillna(0)
    ranked = frame.sort_values(
        [
            "strength",
            "last_price_date",
        ],
        ascending=False,
    )
    claimed = ranked[ranked["main_identifier"] != ""]
    winners = claimed.drop_duplicates("main_identifier")
    losers = claimed.index.difference(winners.index)
    resolved = frame.copy()

    for loser in losers:
        symbol = frame.at[loser, "main_identifier"]
        winner = winners.loc[winners["main_identifier"] == symbol, "index_identifier"].iloc[0]
        resolved.at[loser, "main_identifier"] = ""
        resolved.at[loser, "match"] = f"symbol {symbol} taken by {winner}"

    return resolved.drop(columns=["strength", "last_price_date"])


def _open_live_spans(
    seed: "pandas.DataFrame",
    index_master: "pandas.DataFrame",
) -> "pandas.DataFrame":
    """
    Leave the span open for a listing still trading on the master's last date.

    The master's last price date is the day its builder last wrote it, not a delisting.  A span
    closed there stops every live name's prices on that day: no backtest inside the master's dates
    notices, and a paper book has nothing to price the day it passes.
    """
    price_dates = index_master["last_price_date"]
    master_end = price_dates[price_dates != ""].max()
    live = seed["valid_to"] == master_end
    opened = seed.copy()
    opened.loc[live, "valid_to"] = ""

    return opened


def _profile(
    symbol: str,
    profiles: dict[str, dict],
    api_key: str,
) -> dict:
    """
    FMP's profile of a symbol, from the cache when it was asked for before.

    An empty profile is remembered too: a symbol FMP does not know is not asked about twice.
    """
    if symbol not in profiles:
        payload = _ask_fmp(
            "profile",
            {"symbol": symbol},
            api_key,
        )
        profiles[symbol] = payload[0] if len(payload) > 0 else {}

    return profiles[symbol]


def _read_json(
    path: "pathlib.Path",
) -> dict:
    """
    A cached record, or an empty one before the first run.
    """
    if not path.is_file():

        return {}

    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(
    path: "pathlib.Path",
    content: dict,
) -> None:
    """
    Write a cache as JSON, so an interrupted run resumes where it stopped.
    """
    text = json.dumps(
        content,
        indent=1,
        sort_keys=True,
    )
    path.write_text(
        text,
        encoding="utf-8",
    )


if __name__ == "__main__":
    sys.exit(main())
