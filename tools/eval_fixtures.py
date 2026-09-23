"""
Build the folders the eval cases start from, from this repository's current templates.

Each fixture is a folder a case copies into its session: a researcher's home, a strategy, a folder
that already holds a home.  Homes and strategies are copied by the repository's own `scaffold.py`
from `templates/`, then edited, so a fixture follows the template instead of freezing a copy of it.
The PDF is built here with pypdf, so no binary is committed.

Run by `tools/eval_run.py`; it can also be run alone to look at the fixtures:

    uv run --no-project --with pypdf python tools/eval_fixtures.py <folder>

Console output is ASCII only.
"""
import pathlib
import shutil
import subprocess
import sys

import pypdf

REPOSITORY_ROOT = pathlib.Path(__file__).resolve().parent.parent
# The scaffold script, relative to the package whose starting points the fixtures are built from.
SCAFFOLD_SCRIPT = pathlib.Path('.apm') / 'skills' / 'init-strategy' / 'scripts' / 'scaffold.py'
CHAPTERS = (
    (
        'Trend and its persistence',
        'A trend is a run of returns of one sign. Persistence is measured by the autocorrelation of monthly returns.',
    ),
    (
        'Why trends end',
        'Trends end when the flow that drove them stops. The end is visible in volume before price.',
    ),
    (
        'Costs of following a trend',
        'Turnover rises with the speed of the signal. A fast signal pays more in costs than it earns.',
    ),
)
CLAIMS_MARKER = '<!-- eval: claims -->'
# One markdown clipping at home: a tool's README, invented for the fixture.
CLIPPING_PATH = pathlib.Path('Sources') / 'Clippings' / 'Nullwick_2026_Driftwatch_README.md'
FILLED_BLUEPRINT_MARKER = '<!-- eval: filled blueprint -->'
FIXTURE_NAMES = (
    'home-with-clipping',
    'home-with-notes',
    'researcher-existing',
    'strategy-blueprint-filled',
    'strategy-empty-universe',
    'strategy-no-claims',
    'strategy-no-claims-with-home',
    'strategy-ready',
    'strategy-with-home',
)
# The folder, inside a strategy fixture's working folder, that holds the owner's researcher.
HOME_FOLDER = 'Ada'
QUESTIONS_SECTION = '\n'.join([
    '',
    '## What you are reading for',
    '',
    '1. Do trends in prices persist long enough to trade after costs?',
    '2. What ends a trend, and can it be seen coming?',
    '',
])
ADA_RESEARCHER = '\n'.join([
    '# Ada',
    '',
    '## Who',
    '',
    '**Name:** Ada',
    '',
    '**Works for:** the owner, who invests their own money.',
    '',
    '**Domains:** Markets.',
    '',
    '## How it speaks',
    '',
    'Terse, in English. It challenges a claim that has no source behind it.',
    '',
    '## What you believe',
    '',
    'Trends in prices persist, and most of what a trend rule earns goes to costs. The full account is',
    'in [`Philosophy/HOW-I-INVEST.md`](Philosophy/HOW-I-INVEST.md).',
    '',
    '## Non-negotiables',
    '',
    '- Every number about a book comes from the engines the project names — in a KaxaNuk strategy',
    '  the Lab\'s libraries, the Backtest Engine for performance and Attribution Analysis for where it',
    '  came from — never from the researcher.',
    '- A hypothesis is written before its test, and every prediction in it cites a source.',
    '- Nothing trades. No live execution, no order, no money moves from here.',
    '',
    '## Tag policy',
    '',
    'Loose: the researcher proposes tags and the owner prunes them at audit.',
    '',
    '## The strategies and projects it works on',
    '',
    '| Strategy or project | Path | State |',
    '| --- | --- | --- |',
    '| *none listed* | — | — |',
    '',
    '*I join a strategy when you invite me; a row is added only when you ask.*',
    QUESTIONS_SECTION,
    '## How it cites',
    '',
    'Inside `Knowledge/`, a standard markdown link to the note. Inside a strategy, the relative path',
    'of the note in that repository\'s `Bibliotheca/` — never a path into this folder. A claim with no',
    'source is written as a lead, never as a fact.',
    '',
])
CLAIMS_SECTION = '\n'.join([
    '',
    CLAIMS_MARKER,
    '',
    '## Claims',
    '',
    '1. **Liquid names trend.** The most traded stocks show time-series momentum over 50 to 200 days.',
    '   *Evidence:* Moskowitz, Ooi and Pedersen (2012), note in Bibliotheca/Papers.',
    '2. **The trend survives costs.** A monthly rebalance keeps turnover low enough to keep the edge.',
    '   *Evidence:* the question that would settle it: turnover times cost against the spread.',
    '',
])
CLIPPING_TEXT = '\n'.join([
    '# Driftwatch',
    '',
    'Driftwatch is a command-line tool from Nullwick Research that measures how long a trend in',
    'daily prices lasts and what following it costs. Version 0.4.1, released 2026-08-14.',
    '',
    '## Install',
    '',
    '```bash',
    'uv tool install driftwatch',
    '```',
    '',
    'It needs Python 3.12 and a CSV of daily closes with one column per name.',
    '',
    '## Commands',
    '',
    '- `driftwatch persist <prices.csv>` — for every name, the number of consecutive months the sign',
    '  of the return held, as a distribution, and the autocorrelation of monthly returns at lags one',
    '  to twelve.',
    '- `driftwatch ends <prices.csv> --volume <volume.csv>` — for every trend longer than three',
    '  months, the volume in the last month against the trend\'s average, so a fading flow can be',
    '  seen before the price turns.',
    '- `driftwatch cost <prices.csv> --speed <days>` — the yearly turnover of a rule that follows',
    '  the trend at that speed, and the round-trip cost at a spread given in basis points.',
    '',
    '## Output',
    '',
    'Every command writes one CSV to standard output and a one-line summary to standard error. The',
    'summary line names the version, so a number can be traced to the release that produced it.',
    '',
    '## What it does not do',
    '',
    '- It does not download prices. The CSV is the owner\'s.',
    '- It does not size a book or price one: turnover is a count of trades, not a return.',
    '- It does not know about survivorship: a name that left the file is a name it never saw.',
    '',
    '## Changes in 0.4',
    '',
    '- 0.4.1: `cost` reads the spread from `--spread-bp`; the default of 10 basis points is gone.',
    '- 0.4.0: `ends` added.',
    '',
    '## Licence',
    '',
    'MIT. Nullwick Research, 2026.',
    '',
])
SEED_ROWS = 'main_identifier\nAAPL\nMSFT\nJPM\nXOM\nKO\n'
MOSKOWITZ_NOTE = '\n'.join([
    '---',
    'source: "Time Series Momentum"',
    'citation: "Moskowitz, T., Ooi, Y. H., and Pedersen, L. H. (2012). Journal of Financial Economics 104(2), 228-250."',
    'local_copy: ../../Sources/Papers/Moskowitz_2012_Time_Series_Momentum.pdf',
    'read: 2026-09-01',
    '---',
    '',
    '# Time Series Momentum',
    '',
    'Read from the PDF, whole; pages are the journal\'s.',
    '',
    '## Why it is here',
    '',
    'Question 1: do trends persist long enough to trade after costs.',
    '',
    '## Past twelve-month returns predict the next month in 58 futures markets (p. 229)',
    '',
    '> The persistence is the premise of a trend rule; it is measured, not assumed.',
    '',
    '> [!WARNING]',
    '> [Momentum Crashes](Daniel_2016_Momentum_Crashes.md) is newer on the size of the reversal: it',
    '> measures a crash after market rebounds rather than a slow give-back. The claim below stays as',
    '> this paper states it.',
    '',
    '## The effect partly reverses after a year (p. 240)',
    '',
    '> A holding period longer than a year gives back part of the gain.',
    '',
    '## What it changes',
    '',
    'Question 1 has one measured answer, on futures, not on single stocks.',
    '',
])
CRASH_NOTE = '\n'.join([
    '---',
    'source: "Momentum Crashes"',
    'citation: "Daniel, K., and Moskowitz, T. J. (2016). Journal of Financial Economics 122(2), 221-247."',
    'local_copy: ../../Sources/Papers/Daniel_2016_Momentum_Crashes.pdf',
    'read: 2026-09-10',
    '---',
    '',
    '# Momentum Crashes',
    '',
    'Read from the PDF, whole; pages are the journal\'s.',
    '',
    '## Momentum crashes after market rebounds (p. 222)',
    '',
    '> A trend rule is most exposed right after a bear market ends.',
    '',
    '## What it changes',
    '',
    'Question 2 has a first answer: the rebound after a decline ends a trend abruptly.',
    '',
])
INDEX_TEXT = '\n'.join([
    '# Index',
    '',
    '## Markets',
    '',
    '### Sources',
    '',
    '- [Time Series Momentum](Markets/Moskowitz_2012_Time_Series_Momentum.md) — trends persist in futures, question 1',
    '- [Momentum Crashes](Markets/Daniel_2016_Momentum_Crashes.md) — crashes after rebounds, question 2',
    '',
])


def build_all(
    target: pathlib.Path,
    package_root: pathlib.Path = REPOSITORY_ROOT,
) -> None:
    """
    Build every fixture under `target`, one folder each, replacing any that exist.

    The starting points and the scaffold script come from `package_root`: this repository by
    default, or an export of it.
    """
    builders = {
        'home-with-clipping': _build_home_with_clipping,
        'home-with-notes': _build_home_with_notes,
        'researcher-existing': _build_researcher_existing,
        'strategy-blueprint-filled': _build_strategy_blueprint_filled,
        'strategy-empty-universe': _build_strategy_empty_universe,
        'strategy-no-claims': _build_strategy_no_claims,
        'strategy-no-claims-with-home': _build_strategy_no_claims_with_home,
        'strategy-ready': _build_strategy_ready,
        'strategy-with-home': _build_strategy_with_home,
    }

    for name, builder in builders.items():
        folder = target / name
        shutil.rmtree(
            folder,
            ignore_errors=True,
        )
        builder(
            folder,
            package_root,
        )


def main(
    arguments: list[str] | None = None,
) -> int:
    """
    Build every fixture into the folder given on the command line.
    """
    given = sys.argv[1:] if arguments is None else arguments

    if len(given) != 1:
        print('usage: eval_fixtures.py <folder>')

        return 1

    target = pathlib.Path(given[0]).resolve()
    build_all(target)
    print(f'Built {len(FIXTURE_NAMES)} fixtures in {target}')

    return 0


def _add_home(
    folder: pathlib.Path,
    package_root: pathlib.Path,
) -> None:
    """
    Put Ada's home inside a strategy's working folder: scaffolded from the template, then filled.
    """
    home = folder / HOME_FOLDER
    _scaffold(
        'researcher',
        home,
        package_root,
    )
    (home / 'RESEARCHER.md').write_text(
        ADA_RESEARCHER,
        encoding='utf-8',
    )


def _add_questions(
    home: pathlib.Path,
) -> None:
    """
    Give a home's RESEARCHER.md the two questions the reading cases are read for.
    """
    _append(
        home / 'RESEARCHER.md',
        QUESTIONS_SECTION,
    )


def _append(
    path: pathlib.Path,
    text: str,
) -> None:
    """
    Append text to a file.
    """
    with path.open(
        'a',
        encoding='utf-8',
    ) as handle:
        handle.write(text)


def _build_home_with_clipping(
    folder: pathlib.Path,
    package_root: pathlib.Path,
) -> None:
    """
    A researcher's home with two open questions and one markdown clipping, a tool's README.
    """
    _scaffold(
        'researcher',
        folder,
        package_root,
    )
    _add_questions(folder)
    clipping = folder / CLIPPING_PATH
    clipping.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    clipping.write_text(
        CLIPPING_TEXT,
        encoding='utf-8',
    )


def _build_home_with_notes(
    folder: pathlib.Path,
    package_root: pathlib.Path,
) -> None:
    """
    A researcher's home with two notes, one superseding the other, and an index that links both.
    """
    _scaffold(
        'researcher',
        folder,
        package_root,
    )
    _add_questions(folder)
    markets = folder / 'Knowledge' / 'Markets'
    markets.mkdir(
        parents=True,
        exist_ok=True,
    )
    (markets / 'Moskowitz_2012_Time_Series_Momentum.md').write_text(
        MOSKOWITZ_NOTE,
        encoding='utf-8',
    )
    (markets / 'Daniel_2016_Momentum_Crashes.md').write_text(
        CRASH_NOTE,
        encoding='utf-8',
    )
    (folder / 'Knowledge' / 'INDEX.md').write_text(
        INDEX_TEXT,
        encoding='utf-8',
    )


def _build_researcher_existing(
    folder: pathlib.Path,
    package_root: pathlib.Path,
) -> None:
    """
    A folder that already holds a filled researcher's home, `Ada/`.
    """
    home = folder / 'Ada'
    _scaffold(
        'researcher',
        home,
        package_root,
    )
    researcher = home / 'RESEARCHER.md'
    filled = f'# Ada\n\nAda is the researcher of this home.\n{QUESTIONS_SECTION}'
    researcher.write_text(
        filled,
        encoding='utf-8',
    )


def _build_strategy_blueprint_filled(
    folder: pathlib.Path,
    package_root: pathlib.Path,
) -> None:
    """
    A ready strategy whose Experiment 1 blueprint is already written.
    """
    _build_strategy_ready(
        folder,
        package_root,
    )
    blueprint = folder / 'Experiments' / 'Experiment_1' / 'BLUEPRINT_1.md'
    written = '\n'.join([
        '# Blueprint — Experiment 1',
        '',
        FILLED_BLUEPRINT_MARKER,
        '',
        '**Recorded 2026-09-15, before the rule.**',
        '',
        '## Thesis',
        '',
        'The thirty most traded names that are above their 200-day average outperform the index.',
        '',
    ])
    blueprint.write_text(
        written,
        encoding='utf-8',
    )


def _build_strategy_empty_universe(
    folder: pathlib.Path,
    package_root: pathlib.Path,
) -> None:
    """
    A strategy with claims but a seed that holds only its header.
    """
    _scaffold(
        'strategy',
        folder,
        package_root,
    )
    _append(
        folder / 'OBJECTIVE.md',
        CLAIMS_SECTION,
    )


def _build_strategy_no_claims(
    folder: pathlib.Path,
    package_root: pathlib.Path,
) -> None:
    """
    A strategy exactly as the template ships it, with one paper waiting in Bibliotheca/Papers.
    """
    _scaffold(
        'strategy',
        folder,
        package_root,
    )
    _write_book(folder / 'Bibliotheca' / 'Papers' / 'Moskowitz_2012_Time_Series_Momentum.pdf')


def _build_strategy_no_claims_with_home(
    folder: pathlib.Path,
    package_root: pathlib.Path,
) -> None:
    """
    The strategy-no-claims fixture with Ada's home inside the working folder.
    """
    _build_strategy_no_claims(
        folder,
        package_root,
    )
    _add_home(
        folder,
        package_root,
    )


def _build_strategy_ready(
    folder: pathlib.Path,
    package_root: pathlib.Path,
) -> None:
    """
    A strategy with claims, a seed with rows and a note in Bibliotheca: ready for a blueprint.
    """
    _scaffold(
        'strategy',
        folder,
        package_root,
    )
    _append(
        folder / 'OBJECTIVE.md',
        CLAIMS_SECTION,
    )
    (folder / 'Universe' / 'Investable_Universe.csv').write_text(
        SEED_ROWS,
        encoding='utf-8',
    )
    papers = folder / 'Bibliotheca' / 'Papers'
    papers.mkdir(
        parents=True,
        exist_ok=True,
    )
    (papers / 'Moskowitz_2012_Time_Series_Momentum.md').write_text(
        MOSKOWITZ_NOTE,
        encoding='utf-8',
    )


def _build_strategy_with_home(
    folder: pathlib.Path,
    package_root: pathlib.Path,
) -> None:
    """
    The strategy-ready fixture with Ada's home inside the working folder.
    """
    _build_strategy_ready(
        folder,
        package_root,
    )
    _add_home(
        folder,
        package_root,
    )


def _put_text(
    writer: pypdf.PdfWriter,
    page: pypdf.PageObject,
    body: str,
) -> None:
    """
    Give a blank page one line of real text in Helvetica, which pypdf and extract.py both read.

    pypdf has no public call for this, so the page gets a content stream and a font resource by
    hand; `_add_object` makes the stream an indirect object, as the format requires.
    """
    name = pypdf.generic.NameObject
    font = pypdf.generic.DictionaryObject({
        name('/Type'): name('/Font'),
        name('/Subtype'): name('/Type1'),
        name('/BaseFont'): name('/Helvetica'),
    })
    stream = pypdf.generic.DecodedStreamObject()
    content = f'BT /F1 11 Tf 72 720 Td ({body}) Tj ET'
    stream.set_data(content.encode('latin-1'))
    page[name('/Contents')] = writer._add_object(stream)
    fonts = pypdf.generic.DictionaryObject({
        name('/F1'): font,
    })
    page[name('/Resources')] = pypdf.generic.DictionaryObject({
        name('/Font'): fonts,
    })


def _scaffold(
    kind: str,
    destination: pathlib.Path,
    package_root: pathlib.Path,
) -> None:
    """
    Copy a starting point with the package's own scaffold script, without git.
    """
    subprocess.run(
        [
            sys.executable,
            str(package_root / SCAFFOLD_SCRIPT),
            kind,
            str(destination),
            '--no-git',
            '--package',
            str(package_root),
        ],
        check=True,
        capture_output=True,
    )


def _write_book(
    path: pathlib.Path,
) -> None:
    """
    A small PDF of three chapters with an outline and a text layer.
    """
    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    writer = pypdf.PdfWriter()

    for title, body in CHAPTERS:
        page = writer.add_blank_page(
            width=612,
            height=792,
        )
        _put_text(
            writer,
            page,
            body,
        )

        writer.add_outline_item(
            title,
            len(writer.pages) - 1,
        )

    with path.open('wb') as handle:
        writer.write(handle)


if __name__ == '__main__':
    sys.exit(main())
