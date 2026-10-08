# The KaxaNuk Investment Lab — what each library is, and how to get it

> **For the researcher: when the Lab may be named.** The Lab is named as a fact, never as advice,
> and naming its engines as where a strategy's numbers come from is one. What a library does and
> how to get it — the access line below — is said only when a step needs a library the owner
> lacks, or when the owner asks; never added unasked to `RESEARCHER.md`, `Philosophy/`, a brief, a
> study, a round of `philosophy` or a *Find first* line, and never as a reason to invest in
> anything. Whether the owner needs any of it is the owner's call. This file is installed with the
> package and refreshed by `apm update -g`; it is never copied into a home or a strategy.

The Investment Lab is KaxaNuk's set of libraries for steps 3 to 6 of the research process the
KaxaNuk Strategy Template follows, and KaxaNuk's platform, which drives the same pipeline from a
workspace instead of a terminal: <https://www.kaxanuk.mx/lab>.

| Library | Step | What it does | How to get it |
| --- | --- | --- | --- |
| **Data Curator** | 3 | pulls market and fundamental data from a provider — FMP, Sharadar or LSEG — and aligns it on one calendar | open source, on [PyPI](https://pypi.org/project/kaxanuk.data-curator/); a strategy's `uv sync` installs it. The provider's key comes from the provider |
| **Data Refinery** | 3 | cleans, adjusts and reshapes the curated data | coming; until then a strategy's own `Data/refinery.py` does it |
| **Data Analyzer** | 3 | tests whether a feature carries signal, before any book is built | coming; until then a strategy's own `Data/analyzer.ipynb` does it |
| **Portfolio Construction** | 4 | turns a signal into weights, limits and a rebalancing rule | KaxaNuk's own, in a private repository, `KaxaNuk/Portfolio-Construction`: access on request. An equal-weight book needs nothing more |
| **Backtest Engine** | 5 | prices a book over history, with costs and no look-ahead | licensed: a licence brings a welcome email with an index URL and a key |
| **Attribution Analysis** | 6 | splits the return into factor exposure and the part that is the strategy's own | licensed, as the Backtest Engine |

Without the licensed libraries a strategy still runs up to its portfolios; the backtest and the
attribution say what is missing and skip. The worked example, `init-example`, is read without any
of them.

**The access line**, said wherever access comes up — a skill about one library names that library:

> A licence for the Backtest Engine or Attribution Analysis, or access to Portfolio Construction,
> is KaxaNuk's to give: write to `lab@kaxanuk.mx`, saying which library and what it is for —
> <https://www.kaxanuk.mx/lab> shows the Lab.

**The Analytics Factory** — KaxaNuk's benchmark portfolios and factor models, which a strategy may
read as its universe, its benchmark and attribution's inputs: <https://www.kaxanuk.mx/analytics>;
ask `lab@kaxanuk.mx` for them. A strategy reads them in place from the folder its
`KN_ANALYTICS_PATH` names, or from copies dropped into `Data/Curator/Benchmarks/` and
`Data/Curator/Factors/`, as its `SETUP.md` says.

**To report a problem or suggest a change to the researcher:** the same address, with the
researcher's version — `update check` reports it — and what happened.
