# Contributing to the KaxaNuk Researcher

This file is for someone who installs the package by hand, or changes or forks it: the install in a
terminal and the APM it is pinned to, the path after it, what this repository holds and owns, and
how a change is checked before it lands. The rules for changing the package — where work lands,
versions and changelogs, the template and the worked example kept in step, a fork — are in
[`AGENTS.md`](AGENTS.md): read it before changing anything. Using the researcher needs none of
this; the [`README.md`](README.md) is enough.

## Installing by hand, in a terminal

```bash
uv tool install apm-cli==0.33.0
uvx --from apm-cli==0.33.0 apm install -g KaxaNuk/KaxaNuk-Researcher --target claude
```

`--target codex`, `gemini`, `cursor` or another in place of `claude`; Claude Code receives
everything, and *Troubleshooting* in [`SETUP.md`](SETUP.md) says what the others miss. A second
assistant installed so keeps its files through the next update only once it is on APM's list in
`~/.apm/apm.yml`:

```bash
uv run --no-project python "$HOME/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/skills/init-researcher/scripts/user_targets.py" add codex
```

The skills are then in every folder you open, so **a strategy installs nothing of its own**;
`uvx --from apm-cli==0.33.0 apm update -g` brings every new version. **APM stays at 0.33.0, and
every command that runs it names that version**: APM 0.29.1 to 0.31.0 fail the install on Windows
with `WinError 3` or `WinError 206`, and a newer APM is adopted only once it passes the release
check. Never run `apm self-update`. The skills appear only in a new
session: open one, anywhere, and `init-researcher Ada` makes the home and runs the interview. This
is the path by hand; an assistant asked to install follows [`SETUP.md`](SETUP.md) instead, all in
one conversation. *Removing it*, in the README, undoes either.

## The path after the install

| | In | Run | It makes |
| --- | --- | --- | --- |
| 1 | anywhere | `init-researcher Ada` | the researcher's home, named after it, and then the interview: two short questions about you, about three minutes, that write `RESEARCHER.md`, the agent and the researcher's skill, install them for your user and save a first version. The install in [`SETUP.md`](SETUP.md) runs this for you |
| 2 | the home | `read` | your first note: attach a document, or name it, and it is copied into `Sources/` on your go; the first `read` asks which question it serves, and keeps it as question 1 |
| 3 | the home | `philosophy`, `brief setup` | when you like: how you work or how you invest, in your words, and a daily brief |
| 4 | the home | `init-strategy fcf-yield-quality` | your first strategy, one repository of its own, beside the home; its `SETUP.md` finishes the setup |
| 5 | the strategy | `objective` | the strategy's claims, before any paper — then the order of work, A to H, in the template's README, which the strategy's links to |

The reading map covers investment research; `philosophy` asks how the owner invests or how they
work, in any field, and a researcher for another field grows by reading.

**The researcher is in every folder** once the interview has run: open your assistant in a
strategy's folder, or any other project's, and it is there, by name, on whichever assistant APM
deploys to. Add the home to the session — `claude --add-dir <the home>`, `/add-dir`, or the desktop
app's add-folder button — for it to read the library without asking each time. The home's
`AGENTS.md` says how, and what loads.

## What is in here

```
.apm/skills/          every skill: the researcher's, the Investment Lab's and the house rules'
.apm/prompts/         the commands
.apm/instructions/    the house style: Bloom Code, PEP 8, filesystem boundaries
.apm/agents/          the one agent, blueprint-critic
templates/strategy/   the KaxaNuk Strategy Template — the eight steps as folders; its README is the
                      process, and the order of work a strategy follows
templates/researcher/ the researcher's home, empty
templates/python-library/
                      the KaxaNuk Python Library Template — a Python library laid out like the
                      KaxaNuk Data Curator, named for its owner by init-python-library
examples/golden-flow/ one strategy worked through every folder of the template
SETUP.md              the install, step by step — what an assistant follows when you paste the URL
USE-CASES.md          twelve ways to use the researcher, step by step
apm.yml               the package: what apm install reads; it depends on nothing
pyproject.toml        the ruff settings for the skills' scripts
AGENTS.md, CLAUDE.md  the rules for changing this repository
CONTRIBUTING.md       this file: the install by hand, this layout, and how a change is checked
CHANGELOG.md          one entry per version
LICENSE               MIT
.gitignore            what apm install and Python write per machine
```

**What this repository owns, and what a copy owns.** This repository owns what is written once and
copied or installed everywhere; a copy owns what its owner writes in it. A strategy, or a Python
library, made from a template is its owner's from the first commit and never merges back; the
skills keep updating with `uvx --from apm-cli==0.33.0 apm update -g`.

## Development

```bash
uvx ruff check .
(cd templates/strategy && uvx ruff check .)
(cd examples/golden-flow && uvx ruff check .)
(cd templates/python-library && uvx ruff check .)
uv run --no-project python .apm/skills/bloom-code-lint/scripts/bloom_code_check.py .apm/skills/*/scripts
(cd templates/strategy && uv run --no-project python ../../.apm/skills/bloom-code-lint/scripts/bloom_code_check.py . --max-line-length 100)
(cd examples/golden-flow && uv run --no-project python ../../.apm/skills/bloom-code-lint/scripts/bloom_code_check.py . --max-line-length 100)
(cd templates/python-library && uv run --no-project python ../../.apm/skills/bloom-code-lint/scripts/bloom_code_check.py . --max-line-length 120)
```

Ruff lints the skills' scripts, the strategy and Python library templates and the worked example,
each with its own settings; the Bloom Code check runs on the scripts at its default 120 columns
and, from inside each template and the example — so it finds their own packages — at the line
length each sets: 100 for a strategy, 120 for the Python library template. Each runs through `uv`
alone: no Python of your own is needed. They run on your machine before a commit; there is no CI,
so nothing runs them for you. Nothing else runs inside `templates/`: `uv sync`, `uv build` or
Sphinx there would write a `.venv/`, a `uv.lock` or a `dist/` into the package.

**The template and the example in step.** Nothing else is automated: they are kept in step by
hand, as `AGENTS.md` says. For each file `git ls-files templates/strategy` lists, the example's
copy with its own lines removed — those between `<!-- example: begin -->` and
`<!-- example: end -->` or `# --- example: begin ---` and `# --- example: end ---`, and in a
notebook every cell that starts `# EXAMPLE-ONLY CELL` and every marked block inside a markdown
cell — equals the template's but for blank lines and the exceptions `AGENTS.md` lists. For the
Markdown and Python files:

```bash
for f in $(git ls-files templates/strategy | grep -E '\.(md|py)$'); do
  e="examples/golden-flow/${f#templates/strategy/}"
  [ -f "$e" ] || continue
  awk '/^(<!-- example: begin -->|# --- example: begin ---)$/{s=1;next} /^(<!-- example: end -->|# --- example: end ---)$/{s=0;next} !s' "$e" \
    | diff -B <(awk 1 "$f") - > /dev/null || echo "differs: $f"
done
```

For the notebooks, cell by cell, by cell id:

```bash
for nb in $(git ls-files templates/strategy | grep '\.ipynb$'); do
  uv run --no-project python - "$nb" "examples/golden-flow/${nb#templates/strategy/}" <<'PY' || echo "differs: $nb"
import json, re, sys
marked = re.compile(r'^(<!-- example: begin -->|# --- example: begin ---)$.*?^(<!-- example: end -->|# --- example: end ---)$\n?', re.M | re.S)
def cells(path):
    kept = [c for c in json.load(open(path, encoding='utf-8'))['cells'] if not ''.join(c['source']).startswith('# EXAMPLE-ONLY CELL')]
    return [(c.get('id'), c['cell_type'], [l for l in marked.sub('', ''.join(c['source'])).splitlines() if l.strip()]) for c in kept]
sys.exit(cells(sys.argv[1]) != cells(sys.argv[2]))
PY
done
```

Any file either names that `AGENTS.md` does not list as an exception is a fault.

**To try a change** to a skill, a command, an instruction or the agent, install it at project scope,
from a short scratch folder, with the APM the package is pinned to — never `-g` of the working
tree — **in a shell whose home is a short, empty throwaway folder**. A skill installed for your
user wins over a project skill of the same name, so on a machine where the package is installed the
check would otherwise run the installed copy, and the walk below would change your real setup.
From the repository's root:

```bash
K=C:/k   # an absolute, short path of your own: /tmp/k on macOS or Linux, never ~
mkdir -p "$K/home" "$K/check"
REV=$(git stash create)
git -c core.autocrlf=false archive --format=tar --prefix=KaxaNuk-Researcher/ "${REV:-HEAD}" | tar -x -C "$K"
export HOME="$K/home"
export USERPROFILE="$HOME"
git config --global user.name "Tester"; git config --global user.email "tester@example.invalid"
cd "$K/check"
uvx --from apm-cli==0.33.0 apm install "$K/KaxaNuk-Researcher" --target claude
```

`git stash create` takes your uncommitted changes to tracked files without touching them — a new
file once `git add` has staged it — and with nothing uncommitted the archive is `HEAD`: the files
the commit would hold, with LF endings and none of the ignored folders a working tree has. Open a
new session in the `check` folder, from that shell.

**To try the Python library template** — before a release that changes it, `scaffold.py` or
`init-python-library` — build a copy of it in that throwaway shell, under `$K`: nothing else
catches a broken build. From the repository's root:

```bash
R=$(pwd)
uv run --no-project python .apm/skills/init-strategy/scripts/scaffold.py python-library "$K/lib"
cd "$K/lib"
uv sync
uv run ruff check . && uv run mypy && uv run pytest
uv run --no-project python "$R/.apm/skills/bloom-code-lint/scripts/bloom_code_check.py" . --max-line-length 120
uv run sphinx-build -W -b html docs/source docs/_build/html
uv build
```

Then the same in a second copy, `$K/lib2`, named first with the longest name it accepts — by its
`scripts/name_library.py`, run as the `init-python-library` skill runs it — where every check
passes too, and this prints nothing:

```bash
git -C "$K/lib2" grep -n -e kn_python_library_template -e kn-python-library-template -e KnPythonLibraryTemplate -e "KN Python Library Template" -e "KaxaNuk SC" -- ':!AGENTS.md'
```

**Before a release, make the install above with the commit to be tagged.** It should deploy exactly
22 skills, 9 commands, 3 rules and 1 agent, with no warning. **Then install it for the user twice**,
from the archive — never `-g` of the working tree — each time from a new shell whose `HOME` and
`USERPROFILE` are a new empty folder under `$K`: once Claude, then Codex; once Codex, then Claude.
On the first assistant, install the package as `SETUP.md`'s step 2 does, the archive in place of
`KaxaNuk/KaxaNuk-Researcher`, and run `init-researcher` there, which runs `interview`, to a
researcher whose name has an accent, *Sofía*, its home under `$K` and its files deployed as `sofia`.
The archive installs as `_local/KaxaNuk-Researcher`, so wherever the files name
`$HOME/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/`, tell the assistant to read
`$HOME/.apm/apm_modules/_local/KaxaNuk-Researcher/` instead. On the second, install the package and
the home for it, as `SETUP.md`'s *another assistant* does, then update:

```bash
S="$K/KaxaNuk-Researcher/.apm/skills/init-researcher/scripts/user_targets.py"
uvx --from apm-cli==0.33.0 apm install -g "$K/KaxaNuk-Researcher" --target <the second assistant>
uv run --no-project python "$S" add <the second assistant>
uvx --from apm-cli==0.33.0 apm install -g "<Sofía's home>"
uvx --from apm-cli==0.33.0 apm update -g --yes
uv run --no-project python "$S" check claude sofia
uv run --no-project python "$S" check codex sofia
```

Both checks pass, and on disk `~/.claude/` holds the package's 22 skills and `sofia` in `skills/`,
9 commands, 3 rules and 2 agents, `blueprint-critic.md` and `sofia.md`; `~/.agents/skills/` the same
23 skills; and `~/.codex/agents/` 2 agents, `blueprint-critic.toml` and `sofia.toml`. Then, if the
release changes a skill, a command or a script, walk the rest of the newcomer's path by hand on each
run's first assistant — `next`, `read` on one clipping, a round of `philosophy` at Starter and one
on how you work, `brief setup` and `brief`, and `init-strategy`; `init-python-library`, and `next`
in the folder it makes, when the release changes them — once in Spanish, and once on an assistant
with no question tool, Codex. Delete the scratch folder afterwards: under the throwaway home,
nothing the walk installed or scheduled reached your own. A newer APM is adopted only when these
installs pass with it, on Windows.

`AGENTS.md` has the rules for changing this repository: work lands on `main`, and a release is
tagged `vX.Y.Z` there. `CHANGELOG.md` has one entry per version.
