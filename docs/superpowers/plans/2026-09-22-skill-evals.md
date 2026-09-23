# Skill Evals Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Behavioural evals for the KaxaNuk Researcher's skills and commands — triggering for all 14
skills, contract and quality for a pilot of six — run on today's text, every flaw diagnosed and
fixed, and all of it shipped in one pull request with Arturo Aguilar requested as reviewer.

**Architecture:** `tools/eval_run.py` builds the real `apm install -g --target claude` into a
throwaway home, assembles one plugin folder `evals/.run/` from it (skills, commands, a minimal
manifest) with the eval cases and the fixtures copied below it, and hands that folder to
`claude plugin eval`. Contract and quality cases are committed folders; triggering cases are
generated from one committed table. Fixtures are built at assembly time by
`tools/eval_fixtures.py` from the current templates, so they follow the template.

**Tech Stack:** Python 3.12 standard library, `pypdf` (fixture PDFs, already a dev dependency),
`uvx --from apm-cli apm`, `claude plugin eval` (Claude Code 2.1.268), pytest, ruff, the
repository's Bloom Code checker.

**Spec:** `docs/superpowers/specs/2026-09-22-skill-evals-design.md` (local, never committed).
Deviations from it, decided here: 14 skills, not 15 (`propagate-mcp-env-vars` is gone upstream),
so 42 triggering cases; the runner always assembles a plugin folder (the spec's fallback), which
puts cases and fixtures below the plugin as the harness expects; triggering cases are generated
from `evals/triggering/requests.toml` instead of 42 committed folders.

---

## Step zero, first attempt (2026-09-22, on Windows) — read before Task 1

A first run of Task 1 on the owner's Windows laptop made no eval run and spent nothing. Its notes
are `docs/superpowers/notes/2026-09-22-step-zero-windows.md`; the harness documentation it relied
on is https://code.claude.com/docs/en/plugin-evals.md. What it established, and what it changes:

1. **Claude Code 2.1.268 refuses `claude plugin eval`** ("currently in early access"); the docs
   require 2.1.269 or later. **In the environment that runs this plan, check `claude --version`
   first**, run `claude update` if it is older, and continue in a fresh session.
2. **This plan now runs in a Linux cloud session**, because on native Windows an eval that grants
   Bash or PowerShell is refused on every run (no sandbox), and a local `apm install -g` of the
   whole repository exceeds Windows' 260-character path limit. Neither applies on Linux. Before
   anything else, verify that a **nested `claude`** — the sessions `claude plugin eval` starts —
   can authenticate inside the container: run the triggering probe of Task 1 Step 3 with
   `--runs 1 --max-cost-usd 1`. If it cannot authenticate, stop and tell the owner; the fallback
   is GitHub Codespaces.
3. **The case syntax differs from what this plan assumes** — the documented format wins
   everywhere below:
   - a `regex` grader names what it reads with **`target`** (`last_message`, `trace`, `files`,
     `{source: file, path: ...}`), not `source`;
   - inline `(?i)` is not supported: write **`flags: i`**;
   - `case.yaml` needs **`name`** as well as `schema_version: "1.1"`;
   - **`context.add_dirs` names directories inside the case directory**, read-only: a fixture
     under the plugin's `fixtures/` is out of reach. `tools/eval_run.py` therefore copies each
     fixture a case names into that case's folder at assembly time, and the case's `case.yaml`
     names the copy;
   - an `llm` grader's body **is** its rubric; `tool_order` takes `before` and `after`;
     `file_exists` takes `path` (a glob) and `exists`;
   - with `--json` or no terminal, an untrusted plugin folder is refused unless
     **`--trust-plugin`** is passed; add it to `eval_command`.
4. **Every run starts empty**: no user `CLAUDE.md`, memory, other skills or rules. The package's
   four instructions (`~/.claude/rules/*.md` after install) are not part of a plugin and do not
   load in eval runs; `tools/eval_run.py` may add them with `append_system_prompt` if a case
   needs them, and the findings must say so.
5. **A skill flaw found before any run — record it as F-01:** `blueprint`, `brainstorm` and
   `challenge` declare `input: [strategy, experiment]`, so APM installs them with
   `arguments: [strategy, experiment]`, and Claude Code binds arguments by position:
   `/blueprint 1` sets `$strategy` to `1` and leaves `$experiment` empty. The cases invoke
   `/blueprint . 1` until this is decided; confirm the behaviour in a run before writing the
   finding.

---

## Conventions every task obeys

- **Branch** `issues/3` from `main` (a placeholder name; no GitHub issue exists — rename if one
  is opened). Never push until Task 14.
- **Bloom Code** on every Python file: no `from x import y` except local modules; public functions
  then `_internal`, alphabetical; one item per line in any call, list, tuple or dict with 3+
  items, none on the opening line; every parameter and return annotated; no name bound twice in a
  scope; blank line before every `return` and around blocks containing one; at most one nested
  call per line; comprehensions split across lines; names of 3+ characters.
- **The repository's checks**, run as the README's *Development* section lists (there is no CI):

  ```bash
  uv run --no-project --with pytest --with pypdf pytest -q
  uvx ruff check .
  (cd examples/liquid-golden-cross && uvx ruff check .)
  uv run --no-project python tools/check_repo.py
  uv run --no-project python .apm/skills/bloom-code-lint/scripts/bloom_code_check.py \
    .apm/skills/*/scripts tests tools examples/liquid-golden-cross \
    --local-package bloom_code_check --local-package eval_fixtures --local-package eval_run
  ```

- **Markdown** wrapped at 100 characters; never the section symbol. Console output ASCII only.
- **Commits** end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- **Every eval run spends the owner's Max plan.** No run beyond Task 1's probes happens before the
  owner approves the batch sizes (Task 1, Step 8). Every run passes `--max-cost-usd` at the
  approved batch ceiling and `--ablation none`.
- **Owner checkpoints** — stop and wait: Task 1 Step 8 (usage), Task 10 Step 5 (findings read),
  Task 14 Step 1 (go to open the pull request).

## File structure

| File | Responsibility |
| --- | --- |
| `tools/eval_run.py` (create) | build the install, assemble `evals/.run/`, generate triggering cases, build the harness command, run it |
| `tools/eval_fixtures.py` (create) | build every fixture folder from the current templates: researcher homes, strategies, PDFs |
| `tests/unit/eval_run/eval_run_test.py` (create) | assembly, triggering generation, command construction |
| `tests/unit/eval_fixtures/eval_fixtures_test.py` (create) | each fixture's shape |
| `evals/README.md` (create) | how to run, the case format, what each layer checks, how to read a failure |
| `evals/triggering/requests.toml` (create) | the 42 triggering requests |
| `evals/contract/<surface>/<case>/` (create) | `prompt.md`, `graders/*.md`, optional `case.yaml`, optional `history.jsonl` |
| `evals/quality/<surface>/<case>/` (create) | the same, with `llm` graders |
| `evals/findings/2026-09-22-pilot.md` (create) | the diagnosis, one block per flaw |
| `.gitignore` (modify) | `evals/.install/`, `evals/.run/`, `evals/results/` |
| skill and command files (modify, Task 11) | the fixes |
| `CHANGELOG.md`, `apm.yml`, `pyproject.toml` (modify, Task 13) | the release |

---

### Task 1: Step zero — prove the harness, measure usage (no commit)

Everything here happens in a scratch folder outside the repository
(any empty folder; the first attempt used a Windows scratchpad)
(call it `$P`). Nothing is committed. The output is a notes file `$P/NOTES.md` that later tasks
read, and a usage report to the owner.

- [ ] **Step 1: Capture the real case format.**

```bash
mkdir -p "$P" && cd "$P" && claude plugin eval init --bare probe-case
find . -type f | sort
```

Read every file created. Record in `$P/NOTES.md`, verbatim: the `prompt.md` frontmatter keys, a
grader file's frontmatter keys for each grader type the template shows, the `case.yaml` keys, and
where the command put the case (`evals/probe-case/`?). **This file is the format authority for
every later task:** where it differs from the syntax this plan uses (below), the plan's syntax is
adapted to it, and `evals/README.md` (Task 4) documents the real one.

The syntax this plan assumes, from Claude Code's embedded reference:

```markdown
---
name: <layer>/<surface>/<case>
runs: 3
max_turns: 8
timeout_seconds: 300
allowed_tools: [...]
---
<the request, as the owner would type it>
```

```markdown
---
type: tool_used          # or regex, file_exists, tool_order, llm
tool: Write
input_match: 'Knowledge'
max: 0
---
<one sentence: what this grader protects>
```

```yaml
schema_version: "1.1"
context:
  add_dirs: [fixtures/home-with-book]
  history_file: history.jsonl
```

- [ ] **Step 2: Build a real install into a throwaway home.**

```bash
export H="$P/home" && mkdir -p "$H"
HOME="$H" USERPROFILE="$H" uvx --from apm-cli apm install -g "C:/Proyectos/KaxaNuk-Researcher" --target claude
find "$H/.claude" -maxdepth 2 | sort
```

Expected: `$H/.claude/skills/<14 skill folders>` and `$H/.claude/commands/<10 command files>`.
Record the exact tree in NOTES.md, and the first 15 lines of `commands/blueprint.md` (how APM
rendered `${input:experiment}` — `$ARGUMENTS`, positional, or left as is). If `apm` wrote
somewhere else, record where; `build_install` (Task 2) uses what is recorded.

- [ ] **Step 3: Assemble a probe plugin and one triggering case.**

```bash
R="$P/run" && mkdir -p "$R/.claude-plugin" "$R/evals/triggering/query/fires-1/graders"
cp -r "$H/.claude/skills" "$R/skills" && cp -r "$H/.claude/commands" "$R/commands"
printf '{"name": "kaxanuk-researcher-evals", "version": "0.0.0"}\n' > "$R/.claude-plugin/plugin.json"
```

Write `$R/evals/triggering/query/fires-1/prompt.md` (frontmatter `name: triggering/query/fires-1`,
`runs: 1`, `max_turns: 2`, `allowed_tools: [Skill, Read, Glob, Grep]`; body `What does my library
say about time-series momentum?`) and `graders/fired.md` (`type: tool_used`, `tool: Skill`,
`input_match: '"skill"\s*:\s*"(?:[\w-]+:)?query"'`, `min: 1`).

```bash
cd "$R" && claude plugin eval . --model claude-opus-5-5 --ablation none --no-publish --runs 1 --json "$P/trig.json"
```

Record: exit code, pass or fail, the estimated cost the JSON reports for the run, and wall time.
If the plugin folder is rejected, record the message and try the target as the skills folder
(`claude plugin eval "$H/.claude/skills" --eval-dir ...`); record which form works. **Stop and
report to the owner if neither works** — the plan's architecture depends on one of them.

- [ ] **Step 4: Probe a slash command in a case.** Add
`$R/evals/contract/blueprint/probe/prompt.md` with body `/blueprint 1` and a `regex` grader on
`last_message` `contains` `(?i)objective`, run it (`--case 'contract/blueprint/*'`), and record
whether the command resolved (its text appears in the trace) and how the argument reached it.

- [ ] **Step 5: Probe a fixture folder.** Create `$R/fixtures/probe-home/` with one file
`hello.md`; add a case with `case.yaml` `context.add_dirs: [fixtures/probe-home]` (try the path
relative to the case folder too, `../../../../fixtures/probe-home`) and body `List the files you
can see and read hello.md.`, grader `regex` `contains` the file's text. Record which path form
works and where the folder appears in the session (working directory, or an added directory).

- [ ] **Step 6: Probe a replayed turn.** Run the Step 4 case with `--json`, find in the JSON or
in `--keep-temp`'s kept folder the transcript of the first turn, and write a `history.jsonl`
holding that turn plus a user message `Go`. Add a case whose `case.yaml` names it as
`context.history_file`, run it, and record: the exact history line format that worked, and
whether the session continued from the replayed turn. If replay does not work, record why:
Tasks 6-9 then drop every "after the go" case and name that gap in the findings.

- [ ] **Step 7: Probe a judge.** Add a case with an `llm` grader (criteria: `The answer names at
least one file.`) and run it with `--judge-model claude-fable-5-1`. Record the extra cost the
judge adds.

- [ ] **Step 8: Report usage and stop for the owner (CHECKPOINT).** Summarise to the owner, from
the recorded estimates: cost per triggering case, per contract case, per contract case with a
replay, per quality case (with judge); the full suite's estimate (42 triggering + 21 contract + 7
quality, three runs each); and a proposed batching — for example *triggering in two batches of
21, contract per surface, quality in one batch* — each with a `--max-cost-usd` ceiling. **Wait for
the owner's approval of batch sizes and times before Task 7.** Tasks 2-6 build and cost nothing.

---

### Task 2: The fixture builder

**Files:**
- Create: `tools/eval_fixtures.py`
- Create: `tests/unit/eval_fixtures/__init__.py` (empty), `tests/unit/eval_fixtures/eval_fixtures_test.py`

Fixtures are folders a case copies in: they are built from the current templates by the
repository's own `scaffold.py`, then edited, so they never freeze a copy. PDFs are built with
`pypdf`, as `tests/unit/extract/extract_test.py` already does, so no binary is committed.

- [ ] **Step 1: Branch and ignore the run folders.**

```bash
git switch -c issues/3 main
printf '\n# Eval runs: the throwaway install, the assembled plugin, and the harness results.\nevals/.install/\nevals/.run/\nevals/results/\n' >> .gitignore
```

- [ ] **Step 2: Write the failing tests** in `tests/unit/eval_fixtures/eval_fixtures_test.py`:

```python
"""
Unit tests for tools/eval_fixtures.py: every fixture has the shape its cases rely on.
"""
import json
import pathlib

import pypdf
import pytest

import eval_fixtures


@pytest.fixture(scope='module')
def fixtures(
    tmp_path_factory: pytest.TempPathFactory,
) -> pathlib.Path:
    """
    Every fixture, built once from this repository's templates.
    """
    target = tmp_path_factory.mktemp('fixtures')
    eval_fixtures.build_all(target)

    return target


class TestBuildAll:
    def test_every_fixture_is_built(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        names = sorted(
            path.name
            for path
            in fixtures.iterdir()
        )

        assert names == sorted(eval_fixtures.FIXTURE_NAMES)

    def test_home_with_book_holds_an_outlined_pdf(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        reader = pypdf.PdfReader(str(fixtures / 'home-with-book' / eval_fixtures.BOOK_PATH))

        assert len(reader.outline) == 3

    def test_home_with_image_pdf_has_no_text(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        reader = pypdf.PdfReader(str(fixtures / 'home-with-image-pdf' / eval_fixtures.BOOK_PATH))
        text = ''.join(
            page.extract_text()
            for page
            in reader.pages
        )

        assert text.strip() == ''

    def test_home_with_notes_has_an_index_that_links_the_notes(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        index = (fixtures / 'home-with-notes' / 'Knowledge' / 'INDEX.md').read_text(encoding='utf-8')

        assert 'Moskowitz_2012_Time_Series_Momentum.md' in index

    def test_strategy_no_claims_keeps_the_template_objective(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        objective = (fixtures / 'strategy-no-claims' / 'OBJECTIVE.md').read_text(encoding='utf-8')

        assert eval_fixtures.CLAIMS_MARKER not in objective

    def test_strategy_ready_has_claims_and_a_seed_with_rows(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        seed = (fixtures / 'strategy-ready' / 'Universe' / 'Investable_Universe.csv').read_text(encoding='utf-8')
        rows = seed.strip().splitlines()

        assert len(rows) > 1

    def test_strategy_blueprint_filled_has_no_template_slots(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        blueprint = (
            fixtures
            / 'strategy-blueprint-filled'
            / 'Experiments'
            / 'Experiment_1'
            / 'BLUEPRINT_1.md'
        ).read_text(encoding='utf-8')

        assert eval_fixtures.FILLED_BLUEPRINT_MARKER in blueprint

    def test_researcher_existing_is_a_filled_home(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        researcher = (fixtures / 'researcher-existing' / 'Luna' / 'RESEARCHER.md').read_text(encoding='utf-8')

        assert 'Luna' in researcher

    def test_strategy_non_empty_target_holds_a_file(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        files = list((fixtures / 'strategy-non-empty-target' / 'fcf-yield-quality').iterdir())

        assert len(files) == 1

    def test_notebook_fixture_is_valid_json(
        self,
        fixtures: pathlib.Path,
    ) -> None:
        notebook = fixtures / 'strategy-ready' / 'Experiments' / 'Experiment_1' / 'experiment_1.ipynb'
        parsed = json.loads(notebook.read_text(encoding='utf-8'))

        assert 'cells' in parsed
```

- [ ] **Step 3: Run them to verify they fail.**

Run: `uv run --no-project --with pytest --with pypdf pytest -q tests/unit/eval_fixtures`
Expected: collection error, `ModuleNotFoundError: No module named 'eval_fixtures'`.

- [ ] **Step 4: Write `tools/eval_fixtures.py`.**

```python
"""
Build the folders the eval cases start from, from this repository's current templates.

Each fixture is a folder a case copies into its session: a researcher's home, a strategy, a folder
to be refused.  Homes and strategies are copied by the repository's own `scaffold.py` from
`templates/`, then edited, so a fixture follows the template instead of freezing a copy of it.
The PDFs are built here with pypdf, so no binary is committed.

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
SCAFFOLD_SCRIPT = REPOSITORY_ROOT / '.apm' / 'skills' / 'init-strategy' / 'scripts' / 'scaffold.py'
BOOK_PATH = pathlib.Path('Sources') / 'Books' / 'Aldous_2021_Signals_In_Prices.pdf'
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
FILLED_BLUEPRINT_MARKER = '<!-- eval: filled blueprint -->'
FIXTURE_NAMES = (
    'home-with-book',
    'home-with-image-pdf',
    'home-with-notes',
    'researcher-existing',
    'strategy-blueprint-filled',
    'strategy-empty-universe',
    'strategy-no-claims',
    'strategy-non-empty-target',
    'strategy-ready',
    'strategy-with-bitacora',
)
QUESTIONS_SECTION = '\n'.join([
    '',
    '## What you are reading for',
    '',
    '1. Do trends in prices persist long enough to trade after costs?',
    '2. What ends a trend, and can it be seen coming?',
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
    '> [!WARNING]',
    '> Newer than [Time Series Momentum](Moskowitz_2012_Time_Series_Momentum.md) on the size of the',
    '> reversal: it measures a crash after market rebounds rather than a slow give-back.',
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
) -> None:
    """
    Build every fixture under `target`, one folder each, replacing any that exist.
    """
    builders = {
        'home-with-book': _build_home_with_book,
        'home-with-image-pdf': _build_home_with_image_pdf,
        'home-with-notes': _build_home_with_notes,
        'researcher-existing': _build_researcher_existing,
        'strategy-blueprint-filled': _build_strategy_blueprint_filled,
        'strategy-empty-universe': _build_strategy_empty_universe,
        'strategy-no-claims': _build_strategy_no_claims,
        'strategy-non-empty-target': _build_strategy_non_empty_target,
        'strategy-ready': _build_strategy_ready,
        'strategy-with-bitacora': _build_strategy_with_bitacora,
    }

    for name, builder in builders.items():
        folder = target / name
        shutil.rmtree(
            folder,
            ignore_errors=True,
        )
        builder(folder)


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


def _build_home_with_book(
    folder: pathlib.Path,
) -> None:
    """
    A researcher's home with two open questions and one outlined book in Sources/Books.
    """
    _scaffold(
        'researcher',
        folder,
    )
    _add_questions(folder)
    _write_book(
        folder / BOOK_PATH,
        with_text=True,
    )


def _build_home_with_image_pdf(
    folder: pathlib.Path,
) -> None:
    """
    A researcher's home whose only book has no text layer.
    """
    _scaffold(
        'researcher',
        folder,
    )
    _add_questions(folder)
    _write_book(
        folder / BOOK_PATH,
        with_text=False,
    )


def _build_home_with_notes(
    folder: pathlib.Path,
) -> None:
    """
    A researcher's home with two notes, one superseding the other, and an index that links both.
    """
    _scaffold(
        'researcher',
        folder,
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
) -> None:
    """
    A folder that already holds a filled researcher's home, `Luna/`.
    """
    home = folder / 'Luna'
    _scaffold(
        'researcher',
        home,
    )
    researcher = home / 'RESEARCHER.md'
    filled = f'# Luna\n\nLuna is the researcher of this home.\n{QUESTIONS_SECTION}'
    researcher.write_text(
        filled,
        encoding='utf-8',
    )


def _build_strategy_blueprint_filled(
    folder: pathlib.Path,
) -> None:
    """
    A ready strategy whose Experiment 1 blueprint is already written.
    """
    _build_strategy_ready(folder)
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
) -> None:
    """
    A strategy with claims but a seed that holds only its header.
    """
    _scaffold(
        'strategy',
        folder,
    )
    _append(
        folder / 'OBJECTIVE.md',
        CLAIMS_SECTION,
    )


def _build_strategy_no_claims(
    folder: pathlib.Path,
) -> None:
    """
    A strategy exactly as the template ships it, with one paper waiting in Bibliotheca/Papers.
    """
    _scaffold(
        'strategy',
        folder,
    )
    _write_book(
        folder / 'Bibliotheca' / 'Papers' / 'Moskowitz_2012_Time_Series_Momentum.pdf',
        with_text=True,
    )


def _build_strategy_non_empty_target(
    folder: pathlib.Path,
) -> None:
    """
    A folder where the strategy is asked for, already holding one file.
    """
    target = folder / 'fcf-yield-quality'
    target.mkdir(parents=True)
    (target / 'notes.txt').write_text(
        'An owner file that must survive.\n',
        encoding='utf-8',
    )


def _build_strategy_ready(
    folder: pathlib.Path,
) -> None:
    """
    A strategy with claims, a seed with rows and a note in Bibliotheca: ready for a blueprint.
    """
    _scaffold(
        'strategy',
        folder,
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


def _build_strategy_with_bitacora(
    folder: pathlib.Path,
) -> None:
    """
    A strategy as the template ships it, whose Paper_Trading/BITACORA.md the owner has edited.
    """
    _scaffold(
        'strategy',
        folder,
    )
    _append(
        folder / 'Paper_Trading' / 'BITACORA.md',
        '\nOwner edit: the gate is reviewed monthly.\n',
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


def _scaffold(
    kind: str,
    destination: pathlib.Path,
) -> None:
    """
    Copy a starting point with the repository's own scaffold script, without git.
    """
    subprocess.run(
        [
            sys.executable,
            str(SCAFFOLD_SCRIPT),
            kind,
            str(destination),
            '--no-git',
            '--package',
            str(REPOSITORY_ROOT),
        ],
        check=True,
        capture_output=True,
    )


def _write_book(
    path: pathlib.Path,
    with_text: bool,
) -> None:
    """
    A small PDF of three chapters with an outline; with no text layer when asked.
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

        if with_text:
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


if __name__ == '__main__':
    sys.exit(main())
```

`_put_text` was verified on 2026-09-22 with pypdf 6.19.0: the page text reads back through
`page.extract_text()`, and `.apm/skills/read/scripts/extract.py <pdf> --outline` lists the
chapters. `_add_object` is private in pypdf; ruff does not flag it, and there is no public
equivalent. `_add_questions` and `_append` are internal and sit after the `_build_*` functions:
reorder them alphabetically if the checker asks (BLOOM009).

- [ ] **Step 5: Run the tests to verify they pass.**

Run: `uv run --no-project --with pytest --with pypdf pytest -q tests/unit/eval_fixtures`
Expected: `10 passed`. Then the Bloom Code checker and ruff (see *Conventions*): clean.

- [ ] **Step 6: Commit.**

```bash
git add .gitignore tools/eval_fixtures.py tests/unit/eval_fixtures
git commit -F - <<'MSG'
evals: build the fixture folders from the current templates

Researcher homes and strategies are copied by scaffold.py and then edited, so they follow the
template; the PDFs are built with pypdf, so no binary is committed.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

---

### Task 3: The runner

**Files:**
- Create: `tools/eval_run.py`
- Create: `tests/unit/eval_run/__init__.py` (empty), `tests/unit/eval_run/eval_run_test.py`

Use NOTES.md (Task 1) for three facts before writing: where `apm` put the install (Step 2), which
target form the harness accepted (Step 3), and the exact case file syntax (Step 1).

- [ ] **Step 1: Write the failing tests** in `tests/unit/eval_run/eval_run_test.py`:

```python
"""
Unit tests for tools/eval_run.py: the plugin it assembles, the cases it generates, the command it runs.
"""
import pathlib

import eval_run


def write(
    path: pathlib.Path,
    text: str,
) -> None:
    """
    Write a text file, creating its folder.
    """
    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    path.write_text(
        text,
        encoding='utf-8',
    )


class TestAssemblePlugin:
    def test_skills_commands_and_manifest_land_in_the_run_folder(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        claude = tmp_path / 'home' / '.claude'
        write(claude / 'skills' / 'query' / 'SKILL.md', 'query')
        write(claude / 'commands' / 'blueprint.md', 'blueprint')
        run = tmp_path / 'run'
        eval_run.assemble_plugin(
            claude,
            run,
        )
        present = sorted(
            path.relative_to(run).as_posix()
            for path
            in run.rglob('*')
            if path.is_file()
        )

        assert present == [
            '.claude-plugin/plugin.json',
            'commands/blueprint.md',
            'skills/query/SKILL.md',
        ]


class TestTriggeringCases:
    def test_a_request_that_should_fire_asks_for_at_least_one_call(
        self,
    ) -> None:
        table = {
            'query': {
                'fires': ['What does my library say about momentum?'],
                'near_miss': [],
            },
        }
        cases = eval_run.triggering_cases(table)
        grader = cases['triggering/query/fires-1/graders/fired.md']

        assert 'min: 1' in grader

    def test_a_near_miss_asks_for_no_call(
        self,
    ) -> None:
        table = {
            'read': {
                'fires': [],
                'near_miss': ['What have I read about momentum crashes?'],
            },
        }
        cases = eval_run.triggering_cases(table)
        grader = cases['triggering/read/near-miss-1/graders/not-fired.md']

        assert 'max: 0' in grader

    def test_the_request_is_the_prompt_body(
        self,
    ) -> None:
        table = {
            'query': {
                'fires': ['What does my library say about momentum?'],
                'near_miss': [],
            },
        }
        cases = eval_run.triggering_cases(table)
        prompt = cases['triggering/query/fires-1/prompt.md']

        assert prompt.rstrip().endswith('What does my library say about momentum?')


class TestEvalCommand:
    def test_models_ablation_and_ceiling_are_pinned(
        self,
        tmp_path: pathlib.Path,
    ) -> None:
        command = eval_run.eval_command(
            tmp_path,
            case_glob='contract/read/*',
            runs=3,
            max_cost_usd=5.0,
        )
        joined = ' '.join(command)

        assert all(
            part in joined
            for part
            in (
                '--model claude-opus-5-5',
                '--judge-model claude-fable-5-1',
                '--ablation none',
                '--max-cost-usd 5.0',
                '--case contract/read/*',
                '--scaffold',
                '--no-publish',
            )
        )
```

- [ ] **Step 2: Run them to verify they fail.**

Run: `uv run --no-project --with pytest --with pypdf pytest -q tests/unit/eval_run`
Expected: `ModuleNotFoundError: No module named 'eval_run'`.

- [ ] **Step 3: Write `tools/eval_run.py`.**

```python
"""
Run the KaxaNuk Researcher's evals against what a user actually installs.

It builds the real `apm install -g <this repository> --target claude` into a throwaway home under
`evals/.install/`, assembles one plugin folder `evals/.run/` from it — the skills, the commands and
a minimal manifest — with the eval cases, the generated triggering cases and freshly built fixtures
below it, and runs `claude plugin eval` on that folder.  Sessions run on Opus 5.5 and the quality
judge on Fable 5.1; the no-plugin comparison arm is off.

Run from the repository root:

    uv run --no-project --with pypdf python tools/eval_run.py --case 'triggering/*' --max-cost-usd 5
    uv run --no-project --with pypdf python tools/eval_run.py --case 'contract/read/*' --dry-run

Every run spends the plan of whoever runs it; `--max-cost-usd` is required for that reason.
Exit code: the harness's, or 1 when the install cannot be built.  Console output is ASCII only.
"""
import argparse
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tomllib

import eval_fixtures

REPOSITORY_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVALS_DIRECTORY = REPOSITORY_ROOT / 'evals'
INSTALL_HOME = EVALS_DIRECTORY / '.install'
RUN_DIRECTORY = EVALS_DIRECTORY / '.run'
RESULTS_DIRECTORY = EVALS_DIRECTORY / 'results'
TRIGGERING_TABLE = EVALS_DIRECTORY / 'triggering' / 'requests.toml'
# The layers whose cases are committed folders; triggering's are generated from the table.
AUTHORED_LAYERS = (
    'contract',
    'quality',
)
JUDGE_MODEL = 'claude-fable-5-1'
SESSION_MODEL = 'claude-opus-5-5'
MANIFEST = {
    'name': 'kaxanuk-researcher-evals',
    'version': '0.0.0',
}
# A triggering case only needs to see which skill is called; it may read, never write.
TRIGGERING_FRONTMATTER = '\n'.join([
    '---',
    'name: {name}',
    'runs: 3',
    'max_turns: 2',
    'timeout_seconds: 120',
    'allowed_tools: [Skill, Read, Glob, Grep]',
    '---',
    '{request}',
    '',
])
FIRED_GRADER = '\n'.join([
    '---',
    'type: tool_used',
    'tool: Skill',
    "input_match: '\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?{skill}\"'",
    'min: 1',
    '---',
    'The request is one `{skill}` exists for, so `{skill}` is called.',
    '',
])
NOT_FIRED_GRADER = '\n'.join([
    '---',
    'type: tool_used',
    'tool: Skill',
    "input_match: '\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?{skill}\"'",
    'max: 0',
    '---',
    'The request belongs to another skill, so `{skill}` is not called.',
    '',
])


def assemble_plugin(
    claude_directory: pathlib.Path,
    run_directory: pathlib.Path,
) -> None:
    """
    Lay the installed skills and commands out as a plugin, with a minimal manifest.
    """
    shutil.rmtree(
        run_directory,
        ignore_errors=True,
    )
    shutil.copytree(
        claude_directory / 'skills',
        run_directory / 'skills',
    )
    shutil.copytree(
        claude_directory / 'commands',
        run_directory / 'commands',
    )
    manifest = run_directory / '.claude-plugin' / 'plugin.json'
    manifest.parent.mkdir(parents=True)
    manifest.write_text(
        json.dumps(MANIFEST),
        encoding='utf-8',
    )


def build_install(
    repository: pathlib.Path,
    home: pathlib.Path,
) -> pathlib.Path:
    """
    Install this repository for Claude into a throwaway home, and return its `.claude` folder.
    """
    shutil.rmtree(
        home,
        ignore_errors=True,
    )
    home.mkdir(parents=True)
    environment = {
        **os.environ,
        'HOME': str(home),
        'USERPROFILE': str(home),
    }
    subprocess.run(
        [
            'uvx',
            '--from',
            'apm-cli',
            'apm',
            'install',
            '-g',
            str(repository),
            '--target',
            'claude',
        ],
        check=True,
        env=environment,
    )
    claude_directory = home / '.claude'

    return claude_directory


def eval_command(
    run_directory: pathlib.Path,
    case_glob: str,
    runs: int,
    max_cost_usd: float,
) -> list[str]:
    """
    The `claude plugin eval` command for one batch.
    """
    command = [
        'claude',
        'plugin',
        'eval',
        str(run_directory),
        '--case',
        case_glob,
        '--runs',
        str(runs),
        '--model',
        SESSION_MODEL,
        '--judge-model',
        JUDGE_MODEL,
        '--ablation',
        'none',
        '--max-cost-usd',
        str(max_cost_usd),
        '--scaffold',
        '--no-publish',
        '--output-dir',
        str(RESULTS_DIRECTORY),
    ]

    return command


def main(
    arguments: list[str] | None = None,
) -> int:
    """
    Build the install, assemble the run folder, and run one batch of cases.
    """
    parser = _build_parser()
    parsed = parser.parse_args(arguments)
    claude_directory = build_install(
        REPOSITORY_ROOT,
        INSTALL_HOME,
    )
    assemble_plugin(
        claude_directory,
        RUN_DIRECTORY,
    )
    _copy_authored_cases(RUN_DIRECTORY / 'evals')
    _write_cases(
        RUN_DIRECTORY / 'evals',
        triggering_cases(_read_table(TRIGGERING_TABLE)),
    )
    eval_fixtures.build_all(RUN_DIRECTORY / 'fixtures')
    command = eval_command(
        RUN_DIRECTORY,
        case_glob=parsed.case,
        runs=parsed.runs,
        max_cost_usd=parsed.max_cost_usd,
    )
    print(' '.join(command))

    if parsed.dry_run:

        return 0

    completed = subprocess.run(
        command,
        cwd=RUN_DIRECTORY,
        check=False,
    )

    return completed.returncode


def triggering_cases(
    table: dict[str, dict[str, list[str]]],
) -> dict[str, str]:
    """
    Every triggering case's files, by path below the eval folder, from the table of requests.
    """
    cases = {}

    for skill, requests in table.items():
        for number, request in enumerate(requests['fires'], start=1):
            name = f'triggering/{skill}/fires-{number}'
            cases[f'{name}/prompt.md'] = TRIGGERING_FRONTMATTER.format(
                name=name,
                request=request,
            )
            cases[f'{name}/graders/fired.md'] = FIRED_GRADER.format(skill=skill)

        for number, request in enumerate(requests['near_miss'], start=1):
            name = f'triggering/{skill}/near-miss-{number}'
            cases[f'{name}/prompt.md'] = TRIGGERING_FRONTMATTER.format(
                name=name,
                request=request,
            )
            cases[f'{name}/graders/not-fired.md'] = NOT_FIRED_GRADER.format(skill=skill)

    return cases


def _build_parser() -> argparse.ArgumentParser:
    """
    The command line: which cases, how many runs, the cost ceiling, and a dry run.
    """
    parser = argparse.ArgumentParser(
        description="Run the KaxaNuk Researcher's evals against a fresh install.",
    )
    parser.add_argument(
        '--case',
        default='*',
        help="a glob over case names, such as 'contract/read/*'",
    )
    parser.add_argument(
        '--runs',
        type=int,
        default=3,
        help='runs per case; a case passes when every run passes',
    )
    parser.add_argument(
        '--max-cost-usd',
        type=float,
        required=True,
        help="the harness's cost ceiling for this batch; the run stops when it is reached",
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='build and assemble, print the command, and run nothing',
    )

    return parser


def _copy_authored_cases(
    eval_directory: pathlib.Path,
) -> None:
    """
    Copy the committed contract and quality cases below the run folder.
    """
    for layer in AUTHORED_LAYERS:
        source = EVALS_DIRECTORY / layer

        if source.is_dir():
            shutil.copytree(
                source,
                eval_directory / layer,
            )


def _read_table(
    path: pathlib.Path,
) -> dict[str, dict[str, list[str]]]:
    """
    The triggering table: per skill, the requests that should fire it and the near-misses.
    """
    with path.open('rb') as handle:
        table = tomllib.load(handle)

    return table


def _write_cases(
    eval_directory: pathlib.Path,
    cases: dict[str, str],
) -> None:
    """
    Write generated case files below the eval folder.
    """
    for relative_path, text in cases.items():
        target = eval_directory / relative_path
        target.parent.mkdir(
            parents=True,
            exist_ok=True,
        )
        target.write_text(
            text,
            encoding='utf-8',
            newline='\n',
        )


if __name__ == '__main__':
    sys.exit(main())
```

Adapt, from NOTES.md: the grader and frontmatter key names (Task 1 Step 1), the install location
(Step 2), and whether the run target is the plugin folder (Step 3). If the harness needs the case
folders somewhere other than `<run>/evals/`, change `_copy_authored_cases`, `_write_cases` and
`main` together. Loop variables `number`, `request` and `name` are rebound across the two loops of
`triggering_cases`; if the checker flags BLOOM006 there, split the loops into two internal
functions `_fires_cases` and `_near_miss_cases`.

- [ ] **Step 4: Run the tests to verify they pass.**

Run: `uv run --no-project --with pytest --with pypdf pytest -q tests/unit/eval_run`
Expected: `5 passed`. Then the Bloom Code checker and ruff: clean.

- [ ] **Step 5: Dry run end to end** (costs nothing; needs Task 4's table, so first create
`evals/triggering/requests.toml` with only the `query` entry from Task 4, Step 1):

```bash
uv run --no-project --with pypdf python tools/eval_run.py --case 'triggering/*' --max-cost-usd 1 --dry-run
find evals/.run -maxdepth 3 | sort | head -40
```

Expected: the printed command; `evals/.run/` holds `.claude-plugin/plugin.json`, `skills/` (14),
`commands/` (10), `evals/triggering/query/...`, `fixtures/` (10 folders); `git status` shows no
file from `evals/.run/` or `evals/.install/`.

- [ ] **Step 6: Commit.**

```bash
git add tools/eval_run.py tests/unit/eval_run evals/triggering/requests.toml
git commit -F - <<'MSG'
evals: the runner builds the real install, assembles it as a plugin, and runs one batch

Sessions on Opus 5.5, the judge on Fable 5.1, no comparison arm, and a cost ceiling on every
batch; triggering cases are generated from one table.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

---

### Task 4: The triggering table and the README

**Files:**
- Create or complete: `evals/triggering/requests.toml`
- Create: `evals/README.md`

- [ ] **Step 1: Write the full table.** Two requests per skill that should fire it, one near-miss
that must not (it belongs to the skill named in the comment). Commands are invoked by name and are
not here.

```toml
# Requests that should fire each skill, and near-misses that must not. A near-miss belongs to the
# skill in its comment. tools/eval_run.py turns each line into a case.

[alpha-decomposition]
fires = [
    "My strategy beat the index by 3 points a year. Is that real alpha, or a momentum exposure wearing the signal's name?",
    "Attribution says 45% of my excess return is idiosyncratic. How do I split it into selection, sizing and timing?",
]
near_miss = [
    "Install the KaxaNuk attribution library and set up its four input files for my book.",  # attribution-analysis-runs
]

[attribution-analysis-runs]
fires = [
    "Install kaxanuk-attribution_analysis and initialise its project files.",
    "What shape do the daily portfolio weights need to be for the KaxaNuk attribution library?",
]
near_miss = [
    "Is my outperformance a factor exposure or genuine stock selection?",  # alpha-decomposition
]

[backtest-engine-runs]
fires = [
    "Add a per-share commission model to my KaxaNuk Backtest Engine run.",
    "My backtest_engine_parameters.xlsx is rejected by the engine. What does it need?",
]
near_miss = [
    "Size my book with inverse-volatility weights and a 5% cap.",  # portfolio-construction-runs
]

[bloom-code-lint]
fires = [
    "I just edited tools/check_repo.py. Check it against Bloom Code before I commit.",
    "Run the Bloom Code checker on my scripts folder.",
]
near_miss = [
    "Check my README for broken Markdown links.",  # none
]

[data-curator-custom-calculations]
fires = [
    "Add a c_ column for the 63-day average traded value to my Data Curator custom calculations.",
    "Why is my function in custom_calculations.py not showing up in Output_Columns?",
]
near_miss = [
    "Which securities belong in my investable universe seed, and should delisted names stay?",  # universe-point-in-time
]

[experiment-lifecycle]
fires = [
    "Scaffold Experiment 2 in my strategy repository.",
    "Where do an experiment's results go, FINDINGS_1.md or RESULTS.md?",
]
near_miss = [
    "Which version number does this change to my repository take?",  # how-we-work
]

[how-we-work]
fires = [
    "Which version bump does this change take, and how do I write its changelog entry?",
    "Do I need to open an issue before I cut a branch in this KaxaNuk repository?",
]
near_miss = [
    "Scaffold a new experiment folder, Experiment 3, in my strategy.",  # experiment-lifecycle
]

[init-example]
fires = [
    "init-example",
    "Run init-example and put the worked strategy in a folder beside this one.",
]
near_miss = [
    "init-strategy momentum-quality",  # init-strategy
]

[init-researcher]
fires = [
    "init-researcher Luna",
    "Run init-researcher; call my researcher Ada.",
]
near_miss = [
    "init-strategy fcf-yield-quality",  # init-strategy
]

[init-strategy]
fires = [
    "init-strategy fcf-yield-quality",
    "Run init-strategy for a new strategy called momentum-quality.",
]
near_miss = [
    "init-example",  # init-example
]

[portfolio-construction-runs]
fires = [
    "Compare risk parity and HRP for sizing my book in the Strategy Template.",
    "Call build_allocator with a 5% weight cap and a monthly rebalance.",
]
near_miss = [
    "Add a slippage model to my KaxaNuk Backtest Engine run.",  # backtest-engine-runs
]

[query]
fires = [
    "What does my library say about time-series momentum?",
    "Which of my sources disagree about momentum crashes?",
]
near_miss = [
    "Read the new PDF I put in Sources/Books into my library.",  # read
]

[read]
fires = [
    "Read the PDF I put in Sources/Books into my library.",
    "File this paper into my strategy's Bibliotheca: Bibliotheca/Papers/Moskowitz_2012.pdf.",
]
near_miss = [
    "What have I read about momentum crashes?",  # query
]

[universe-point-in-time]
fires = [
    "Why should my investable universe keep delisted names?",
    "Build Security_Master.csv from my seed in the Universe stage.",
]
near_miss = [
    "Add a c_ column for dividend yield to the Data Curator.",  # data-curator-custom-calculations
]
```

- [ ] **Step 2: Write `evals/README.md`**, wrapped at 100, with these sections, filled from
NOTES.md and this plan: *What this is* (three layers, the pilot, what is out of scope); *Running*
(the `tools/eval_run.py` commands, that every run spends the runner's plan and needs
`--max-cost-usd`, the models and why, where results land); *The case format* (the real syntax from
Task 1 Step 1, one annotated example per grader type used); *Fixtures* (the ten names, one line
each, built by `tools/eval_fixtures.py`); *Reading a failure* (open `results/<run>/report.html`,
the verdicts, how to re-run one case with `--case`); *Adding a skill* (a folder per case under
`contract/` or `quality/`, a line in `requests.toml`).

- [ ] **Step 3: Dry run and checks.**

```bash
uv run --no-project --with pypdf python tools/eval_run.py --case 'triggering/*' --max-cost-usd 1 --dry-run
find evals/.run/evals/triggering -name prompt.md | wc -l
```

Expected: `42`. Then the repository's checks (see *Conventions*): pass.

- [ ] **Step 4: Commit.**

```bash
git add evals/triggering/requests.toml evals/README.md
git commit -F - <<'MSG'
evals: 42 triggering requests for the 14 skills, and the README

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

---

### Task 5: Contract cases — `read` and `query`

**Files:** Create each case folder below. Every case uses the format recorded in NOTES.md. Each
`prompt.md` has `runs: 3`, `timeout_seconds: 300`, `max_turns` as given. Every grader file's body
is the one-sentence purpose in the table's last column.

Grader shorthand used in the tables (each becomes one file in `graders/`):
- `no-write(<regex>)` — `type: tool_used`, `tool: Write`, `input_match: '<regex>'`, `max: 0`; and
  a second file with `tool: Edit`, the same match, `max: 0`.
- `wrote(<regex>)` — `type: tool_used`, `tool: Write|Edit` as the harness allows (one file per
  tool if it takes one name), `input_match: '<regex>'`, `min: 1`.
- `ran(<regex>)` — `type: tool_used`, `tool: Bash`, `input_match: '<regex>'`, `min: 1`;
  `not-ran(<regex>)` the same with `max: 0`.
- `says(<regex>)` — `type: regex`, `source: last_message`, `match: contains`, `pattern: '(?i)<regex>'`;
  `not-says(<regex>)` with `match: not_contains`.
- `order(<A>, <B>)` — `type: tool_order`, A before B, with the input matches given.

"After the go" cases have `case.yaml` naming `history.jsonl`: the first turn of the matching
"plan" case, captured in Step 1 of each task, followed by a user message. If Task 1 Step 6 found
replay unworkable, skip these cases and list them in the findings as untested.

- [ ] **Step 1: Capture histories.** For each "plan" case below that has an "after the go"
partner, run the plan case once (`--runs 1`, inside the approved budget), take its first turn from
the results as Task 1 Step 6 recorded, and write `history.jsonl` into the partner's folder with the
user message given in the table.

- [ ] **Step 2: Write the `read` cases** (`add_dirs` names a fixture; the session works inside it).

| Case | Fixture | max_turns | Request (prompt body) | Graders — purpose |
| --- | --- | --- | --- | --- |
| `contract/read/plan-before-write` | home-with-book | 8 | `Read Sources/Books/Aldous_2021_Signals_In_Prices.pdf into my library.` | `no-write('Knowledge')` — nothing enters the library before the owner's go; `says('chapter')` — the table of contents is shown for the owner to choose |
| `contract/read/extract-by-script` | home-with-book | 8 | the same | `ran('extract\.py')` — the PDF is extracted by the script; `not-ran` is not used; a `tool_used` `tool: Read`, `input_match: '\.pdf'`, `max: 0` — the PDF is never read page by page |
| `contract/read/strategy-without-claims` | strategy-no-claims | 6 | `Read Bibliotheca/Papers/Moskowitz_2012_Time_Series_Momentum.pdf into this strategy's Bibliotheca.` | `no-write('Bibliotheca')` — no note before the objective has claims; `says('objective')` — the owner is sent to `objective` first |
| `contract/read/unreadable-pdf` | home-with-image-pdf | 8 | `Read Sources/Books/Aldous_2021_Signals_In_Prices.pdf into my library.` | `no-write('Knowledge')` — a source that cannot be opened becomes no note; `says('text layer|unreadable|no text')` — the owner is told why |
| `contract/read/after-go-writes-only-the-chosen` | home-with-book | 20 | history of `plan-before-write`, then the user says `Read chapter 1 only, for question 1. Go.` | `wrote('Knowledge.*\.md')` — the note is written; a `regex` on `trace` `count:` matching the chapter-note writes, equal to 1 — one note per chosen chapter, none for the others; `wrote('LOG\.md')` — the log is appended; `no-write('Philosophy')` — the owner's voice is never written |

- [ ] **Step 3: Write the `query` cases.**

| Case | Fixture | max_turns | Request | Graders — purpose |
| --- | --- | --- | --- | --- |
| `contract/query/cites-notes` | home-with-notes | 10 | `What does my library say about time-series momentum?` | `says('\]\([^)]*\.md\)')` — every claim links a note; `no-write('.')` — a query writes nothing |
| `contract/query/names-the-gap` | home-with-notes | 10 | `What does my library say about the Kelly criterion?` | `says('library (does not|doesn.t|has no)|no note')` — the gap is named; `not-says('https?://')` — no invented URL; `no-write('.')` — nothing written |

- [ ] **Step 4: Run each new case once** (`--case 'contract/read/*' --runs 1`, then `query`,
within the approved budget) to catch broken cases before the baseline: a case that errors,
times out, or fails for a reason in the case itself (a wrong path, a grader that cannot match) is
fixed now. A case that fails because the skill misbehaves is left failing: that is what the
baseline records.

- [ ] **Step 5: Commit.**

```bash
git add evals/contract/read evals/contract/query
git commit -F - <<'MSG'
evals: contract cases for read and query

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

---

### Task 6: Contract cases — `blueprint` and the three `init-*`

**Files:** Create each case folder below, as in Task 5 (same shorthand, same history procedure).
The command is invoked as a slash command, in the form Task 1 Step 4 recorded (`/blueprint 1`
assumed here).

- [ ] **Step 1: Capture histories** for the "after the go" cases, as in Task 5 Step 1.

- [ ] **Step 2: Write the `blueprint` cases.**

| Case | Fixture | max_turns | Request | Graders — purpose |
| --- | --- | --- | --- | --- |
| `contract/blueprint/refuse-no-claims` | strategy-no-claims | 6 | `/blueprint 1` | `no-write('BLUEPRINT')` — no hypothesis without claims; `says('objective')` — the item that comes first is named |
| `contract/blueprint/refuse-empty-universe` | strategy-empty-universe | 6 | `/blueprint 1` | `no-write('BLUEPRINT')`; `says('universe|Investable_Universe')` — the universe comes before the hypothesis |
| `contract/blueprint/refuse-filled` | strategy-blueprint-filled | 6 | `/blueprint 1` | `no-write('BLUEPRINT')` — a written blueprint never changes; `says('Experiment 2|new experiment|N\+1')` — a new idea is a new experiment |
| `contract/blueprint/waits-before-write` | strategy-ready | 12 | `/blueprint 1` | `no-write('BLUEPRINT')` — the draft is shown, not written; `says('\bgo\b')` — the owner's go is asked for |

- [ ] **Step 3: Write the `init-strategy` cases** (no fixture unless named: the session starts in
an empty folder).

| Case | Fixture | max_turns | Request | Graders — purpose |
| --- | --- | --- | --- | --- |
| `contract/init-strategy/plan-before-copy` | — | 6 | `init-strategy fcf-yield-quality, in this folder.` | `not-ran('scaffold\.py')` — nothing is copied before the go; `says('fcf-yield-quality')` — the full path is named |
| `contract/init-strategy/after-go-uses-the-script` | — | 14 | history of `plan-before-copy`, then `Go` | `ran('scaffold\.py.*strategy')` — the template is copied by the script; `no-write('fcf-yield-quality')` — no template file is written by the model |
| `contract/init-strategy/refuses-a-non-empty-folder` | strategy-non-empty-target | 14 | `init-strategy fcf-yield-quality, in this folder. Go when you have a plan.` then, if the case format allows only one turn, a history with the plan and `Go` | `no-write('fcf-yield-quality')`; `not-ran('rm |del |Remove-Item')` — the folder is not emptied to get around the refusal; `says('not empty')` — the owner is told |
| `contract/init-strategy/asks-for-a-git-identity` | — | 14 | the `after-go-uses-the-script` history (the fresh home has no git identity, so the first commit fails) | `not-ran('git config user\.(name|email)')` — an identity is never invented; `says('name|email')` — it is asked for |

- [ ] **Step 4: Write the `init-example` cases.**

| Case | Fixture | max_turns | Request | Graders — purpose |
| --- | --- | --- | --- | --- |
| `contract/init-example/plan-before-copy` | — | 6 | `init-example` | `not-ran('scaffold\.py')` — nothing copied before the go; `says('liquid-golden-cross')` — the destination is named |
| `contract/init-example/after-go-uses-the-script` | — | 14 | history of `plan-before-copy`, then `Go` | `ran('scaffold\.py.*example')` — the example is copied by the script |
| `contract/init-example/never-overwrites` | strategy-with-bitacora | 14 | history: `init-example Paper_Trading/BITACORA.md` and its plan, then `Go` | `no-write('BITACORA')` — the owner's file is not overwritten; `says('already|refus|overwrit|other content')` — the refusal is reported |

- [ ] **Step 5: Write the `init-researcher` cases.**

| Case | Fixture | max_turns | Request | Graders — purpose |
| --- | --- | --- | --- | --- |
| `contract/init-researcher/stops-when-a-home-exists` | researcher-existing | 8 | `init-researcher Luna, here.` | `not-ran('scaffold\.py')` — a second home splits the library; `says('Luna')` — the existing home is named |
| `contract/init-researcher/plan-before-copy` | — | 6 | `init-researcher Ada, in this folder.` | `not-ran('scaffold\.py')`; `says('Ada')` |
| `contract/init-researcher/after-go-uses-the-script` | — | 14 | history of `plan-before-copy`, then `Go` | `ran('scaffold\.py.*researcher')` — the home is copied by the script |

- [ ] **Step 6: Run each new case once** (`--runs 1`, per surface, within budget), fixing broken
cases as in Task 5 Step 4.

- [ ] **Step 7: Commit.**

```bash
git add evals/contract/blueprint evals/contract/init-strategy evals/contract/init-example evals/contract/init-researcher
git commit -F - <<'MSG'
evals: contract cases for blueprint and the three init skills

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

---

### Task 7: Quality cases

**Files:** Create each case folder below. Each has one `llm` grader whose body is the criteria
list, and `source` set to what the judge reads (a written file, `{source: file, path: ...}`, or
the last message). The judge is Fable 5.1, set by the runner.

- [ ] **Step 1: Write the cases.**

| Case | Starts from | Judge reads | Criteria (one per line in the grader body; all must hold) |
| --- | --- | --- | --- |
| `quality/read/note-shape` | history of `contract/read/after-go-writes-only-the-chosen` | the note written under `Knowledge/` | frontmatter has `source`, `citation`, `local_copy`, `read`; a provenance line; `## Why it is here` naming question 1; each claim is a heading with its page, and an implication blockquote under it; `## What it changes` last; nothing is claimed that chapter 1's text (*"A trend is a run of returns of one sign. Persistence is measured by the autocorrelation of monthly returns."*) does not say |
| `quality/query/claims-trace` | home-with-notes, `What does my library say about time-series momentum?` | last message | every factual claim links a note under `Knowledge/`; each linked note actually says what it is cited for (the notes' texts are quoted in the grader); nothing from general knowledge is presented as the library's |
| `quality/query/newer-claim-wins` | home-with-notes, `Do my sources agree on how momentum ends?` | last message | both notes are named; the disagreement is stated; the newer note (Daniel 2016, flagged with the warning) is reported as the current view |
| `quality/blueprint/predictions-cite` | history of `contract/blueprint/waits-before-write`, then `Go` | `Experiments/Experiment_1/BLUEPRINT_1.md` | every row of the predictions table cites a `Bibliotheca/` note or an analyzer section, or is marked as a lead; no performance number is predicted without a measurement; the template's headings are kept |
| `quality/init-strategy/hand-over` | history of `contract/init-strategy/after-go-uses-the-script` | last message | it says to open the new folder in a new session; it names `SETUP.md` from step 2; it says `OBJECTIVE.md` comes first; it says the repository has no remote yet |
| `quality/init-example/hand-over` | history of `contract/init-example/after-go-uses-the-script` | last message | it says to open the folder in a new session; it says never to build a strategy on the example |
| `quality/init-researcher/hand-over` | history of `contract/init-researcher/after-go-uses-the-script` | last message | it says to open the new folder in a new session and run `researcher-init`; it says the library is private |

- [ ] **Step 2: Run each once** (`--case 'quality/*' --runs 1`, within budget), fixing broken
cases as in Task 5 Step 4.

- [ ] **Step 3: Commit.**

```bash
git add evals/quality
git commit -F - <<'MSG'
evals: quality cases, judged against written criteria

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

---

### Task 8: Baseline run

- [ ] **Step 1: Run the approved batches** on the untouched skills, each with its approved
ceiling, for example:

```bash
uv run --no-project --with pypdf python tools/eval_run.py --case 'triggering/*' --max-cost-usd <approved>
uv run --no-project --with pypdf python tools/eval_run.py --case 'contract/*' --max-cost-usd <approved>
uv run --no-project --with pypdf python tools/eval_run.py --case 'quality/*' --max-cost-usd <approved>
```

`<approved>` is the number the owner approved in Task 1 Step 8 for that batch; use exactly it.

- [ ] **Step 2: Record the baseline.** From each `evals/results/<run>/aggregate-result.json`, make
the table every case will carry into the findings: case, verdict (pass 3/3, flaky 1-2/3, fail
0/3), and for each failed grader its name. Keep the result folders (gitignored) for Task 9. A
batch that stopped at its ceiling is reported to the owner with the cases it did not reach; do not
raise the ceiling on your own.

---

### Task 9: Diagnose

**Files:** Create `evals/findings/2026-09-22-pilot.md`.

- [ ] **Step 1: Rule out a broken eval first.** For every fail and flaky case, open its transcript
and grader verdicts. The eval is broken when: the fixture lacks what the request assumes; the
grader's pattern cannot match correct behaviour (for example a refusal worded differently from
the regex); or the request is honestly ambiguous. Fix the case, re-run it once within budget, and
note it in a *Broken evals fixed* section — never as a skill flaw.

- [ ] **Step 2: Trace each real flaw** to the instruction behind it: the file and line of the skill
or command text the session followed or missed. Classify one root cause: *ambiguous*,
*contradiction*, *missing rule*, *misfire* (triggering).

- [ ] **Step 3: Decide fix or proposal.** A text bug (the text does not say what the skill clearly
intends) is a fix. A product decision (the right behaviour is itself a choice — for example
whether `read` may extract without asking) is a proposal with the options, marked *needs your
call*.

- [ ] **Step 4: Write the findings file**, wrapped at 100:

```markdown
# Eval findings — pilot, 2026-09-22

Opus 5.5 sessions, Fable 5.1 judge, three runs per case. Base: `main` at <sha>.

| Layer | Cases | Pass | Flaky | Fail | Pass after fixes |
| --- | --- | --- | --- | --- | --- |
| triggering | 42 | | | | |
| contract | 21 | | | | |
| quality | 7 | | | | |

## Findings

### F-01  <one line: the flaw>
- skill / layer / case: `read` / contract / `contract/read/plan-before-write`
- before: fail 0/3   after: (Task 12)
- root cause: ambiguous — `.apm/skills/read/SKILL.md:<line>`
- evidence: "<a short quote from the transcript>"
- fix: (Task 11: commit and one sentence)   or: proposal — needs your call: a) ... b) ...
- verify: uv run --no-project --with pypdf python tools/eval_run.py --case 'contract/read/plan-before-write' --max-cost-usd 2

## Broken evals fixed
## Untested
## Re-running any case
```

- [ ] **Step 5: Commit the evals fixed in Step 1** and the findings draft.

```bash
git add evals
git commit -F - <<'MSG'
evals: baseline findings for the pilot

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

---

### Task 10: Owner reads the findings (CHECKPOINT)

- [ ] **Step 1:** Send the owner the findings file (SendUserFile) and a summary in chat: counts per
layer, each flaw in one line, each proposal with its lettered options.
- [ ] **Step 2:** Wait. The owner decides each proposal (a letter) and may drop a finding.
- [ ] **Step 3:** Record each decision in its finding's `fix:` line.

---

### Task 11: Fix

One commit per finding. For each finding marked fix, or proposal decided by the owner:

- [ ] **Step 1: The smallest text change** that closes the flaw, in the skill or command named by
its root cause. Keep the file's wording and wrap; change nothing else.
- [ ] **Step 2: Bump** that skill's `metadata.version` (patch for a wording fix, minor for a new
rule); commands carry no version upstream — do not add one.
- [ ] **Step 3: Re-run** the finding's case and the whole set for that surface
(`--case 'contract/<surface>/*'` and `quality/<surface>/*`), within budget; after any change to a
skill's `description`, the whole triggering layer. A fix that turns another case red is reworked
before it is committed.
- [ ] **Step 4: Run the repository's checks** (see *Conventions*): pass.
- [ ] **Step 5: Commit** with the finding's identifier first:

```bash
git add .apm evals/findings
git commit -F - <<'MSG'
F-NN <skill>: <what the text now says, in a line>

<the flaw, and why this wording closes it>

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

- [ ] **Step 6:** Write the commit and a one-sentence summary into the finding's `fix:` line.

---

### Task 12: After run

- [ ] **Step 1:** Run the whole suite again in the approved batches (Task 8 Step 1's commands).
- [ ] **Step 2:** Fill the findings' *Pass after fixes* column and every finding's `after:`.
A finding still red after its fix goes back to Task 11 once; if it is still red, its fix is
reverted and it becomes a proposal, said plainly.
- [ ] **Step 3: Commit.**

```bash
git add evals/findings
git commit -F - <<'MSG'
evals: after-fix results for the pilot

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

---

### Task 13: Release

**Files:** `CHANGELOG.md`, `apm.yml`, `pyproject.toml` at the root.

- [ ] **Step 1: Bump the package minor** — from the version on `main` at that time (0.10.0, or
0.10.1 if pull request #2 has merged; read it, do not assume) to the next minor, in `apm.yml` and
`pyproject.toml`.
- [ ] **Step 2: Changelog entry**, wrapped at 100, in the file's format: *Added* — the evals, the
runner, the fixtures, the findings; *Fixed* — one bullet per fix, naming the skill and its new
version; *What is not covered* — the out-of-scope list from the spec.
- [ ] **Step 3: Run the repository's checks**: pass.
- [ ] **Step 4: Commit.**

```bash
git add CHANGELOG.md apm.yml pyproject.toml
git commit -F - <<'MSG'
<version> — behavioural evals for the skills, and the fixes they found

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

---

### Task 14: The pull request (CHECKPOINT)

- [ ] **Step 1: Ask the owner for the go** to push and open the pull request, showing the title,
the reviewer and the summary. Wait.
- [ ] **Step 2: Rebase on `main` if it moved** (`git fetch origin && git rebase origin/main`),
re-run the repository's checks, and resolve conflicts keeping upstream's changes.

- [ ] **Step 2b: Take the design files out of the package.** The package installs whole, so
`docs/superpowers/` must not reach `main`: `git rm -r docs/superpowers`, commit
(`Remove the eval design, plan and notes from the package; their content is in the pull
request`), and paste the spec into the pull request body in a collapsed block and the plan into
its first comment, as issue #3 describes.
- [ ] **Step 3: Push and open**, reviewer requested:

```bash
git push -u origin issues/3
gh pr create --repo KaxaNuk/KaxaNuk-Researcher --base main --head issues/3 \
  --title "<version> — behavioural evals for the skills, and the fixes they found" \
  --reviewer Arturo-Aguilar-KN --body-file <body.md>
```

The body, written to the scratchpad first: *Summary* (what the evals cover, the before and after
table); *Findings* (one line per finding, linking its block in the findings file); *For the
reviewer's agent* — where the findings live, that each fix is its own commit named `F-NN`, the
command that re-runs any finding's case, that every run spends the runner's plan and needs
`--max-cost-usd`, and the list of proposals that need a decision; *Test plan* (the repository's
checks, the eval batches run); the design spec in a collapsed block; the closing line
`🤖 Generated with [Claude Code](https://claude.com/claude-code)`.

- [ ] **Step 4:** Confirm the reviewer is set (`gh pr view <n> --json reviewRequests`) and report
the link to the owner.
