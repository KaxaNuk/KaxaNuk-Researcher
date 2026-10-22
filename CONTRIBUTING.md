# Contributing to the KaxaNuk Researcher

This file is for anyone who installs the package by hand, or changes or forks it: the install in a
terminal, the path after it, what this repository holds, and how a change is checked. The rules for
changing the package (where work lands, versions and changelogs, keeping the template and the
worked example in step, forks) are in [`AGENTS.md`](AGENTS.md); read it before changing anything.
Using the researcher needs only the [`README.md`](README.md); its *What it is, and what it is not*
says what the package is for.

## Installing by hand, in a terminal

```bash
uv tool install apm-cli==0.33.0
uvx --from apm-cli==0.33.0 apm install -g KaxaNuk/KaxaNuk-Researcher --target claude
```

For another assistant, put `codex`, `gemini`, `cursor` or another in place of `claude`. Claude Code
receives everything. *Troubleshooting* in [`SETUP.md`](SETUP.md) says what the others miss, and why
APM stays at 0.33.0, named in every command, and `apm self-update` is never run. A second assistant
installed this way keeps its files through the next update only once it is on APM's list in
`~/.apm/apm.yml`:

```bash
uv run --no-project python "$HOME/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/skills/init-researcher/scripts/user_targets.py" add codex
```

`uvx --from apm-cli==0.33.0 apm update -g` brings every new version. Then open a new session,
anywhere, and follow the path below. An assistant asked to install follows [`SETUP.md`](SETUP.md)
instead, all in one conversation. *Removing it*, in the README, undoes either.

## The path after the install

| | In | Run | It makes |
| --- | --- | --- | --- |
| 1 | anywhere | `init-researcher Arya` | the researcher's home, named after it, then the interview, which writes `RESEARCHER.md`, the agent and the researcher's skill, installs them for your user and saves a first version. The install in [`SETUP.md`](SETUP.md) runs this for you |
| 2 | the home | `read` | your first note: attach or name a document, copied into `Sources/` on your go; the first `read` asks which question it serves and keeps it as question 1 |
| 3 | the home | `philosophy`, `brief setup` | when you like: how you work or how you invest, in your words, and a daily brief |
| 4 | the home | `init-strategy fcf-yield-quality` | your first strategy, a repository of its own beside the home; its `SETUP.md` finishes the setup |
| 5 | the strategy | `objective` | the strategy's claims, before any paper; then the order of work, A to H, in the template's README, which the strategy's links to |

The reading map covers investment research; `philosophy` covers how the owner invests or how they
work, in any field, and a researcher for another field grows by reading.

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
examples/<kind>/<name>/
                      the worked examples, one folder each, by kind as the templates are: today
                      one, a strategy worked through every folder of the template
SETUP.md              the install, step by step — what an assistant follows when you paste the URL
USE-CASES.md          twelve ways to use the researcher, step by step
ONBOARDING.md         the onboarding and first read as approved, step by step — frozen
FROZEN.json           the fingerprints of the frozen files
apm.yml               the package: what apm install reads; it depends on nothing
pyproject.toml        the ruff settings for the skills' scripts
AGENTS.md, CLAUDE.md  the rules for changing this repository
CONTRIBUTING.md       this file: the install by hand, this layout, and how a change is checked
CHANGELOG.md          one entry per version
LICENSE               MIT
.gitignore            what apm install and Python write per machine
```

**What this repository owns, and what a copy owns.** This repository owns what is written once and
copied or installed everywhere; a copy owns what its owner writes in it. A strategy or a Python
library made from a template is its owner's from the first commit and never merges back; the
skills keep updating with `uvx --from apm-cli==0.33.0 apm update -g`.

## Development

```bash
uvx ruff check .
(cd templates/strategy && uvx ruff check .)
for e in examples/strategy/*/; do (cd "$e" && uvx ruff check .); done
(cd templates/python-library && uvx ruff check .)
uv run --no-project python .apm/skills/bloom-code-lint/scripts/bloom_code_check.py .apm/skills/*/scripts
(cd templates/strategy && uv run --no-project python ../../.apm/skills/bloom-code-lint/scripts/bloom_code_check.py . --max-line-length 100)
for e in examples/strategy/*/; do (cd "$e" && uv run --no-project python ../../../.apm/skills/bloom-code-lint/scripts/bloom_code_check.py . --max-line-length 100); done
(cd templates/python-library && uv run --no-project python ../../.apm/skills/bloom-code-lint/scripts/bloom_code_check.py . --max-line-length 120)
```

Ruff lints the skills' scripts, the strategy and Python library templates and every strategy
example, each with its own settings. The Bloom Code check runs on the scripts at its default 120
columns, and from inside each template and example, so it finds their own packages, at the line
length each sets: 100 for a strategy, its template and its examples, 120 for the Python library
template. An example of another kind, three folders down in `examples/<kind>/<name>/`, runs as its
template does, with one more `../`. Everything runs through `uv`: no Python of your own is needed.
Run them on your machine before every commit; there is no CI, so nothing runs them for you.
Nothing else runs inside `templates/`: `uv sync`, `uv build` or Sphinx there would write a
`.venv/`, a `uv.lock` or a `dist/` into the package.

**The frozen files stay unchanged** unless the owner says otherwise, as `AGENTS.md` says under
*Rules*. Before every commit, from the repository's root, this prints each frozen file that no
longer matches its fingerprint in `FROZEN.json`, and fails if there is one:

```bash
uv run --no-project python - <<'PY'
import hashlib, json, pathlib, sys
files = json.loads(pathlib.Path("FROZEN.json").read_text(encoding="utf-8"))["files"]
changed = [p for p, h in files.items() if hashlib.sha256(pathlib.Path(p).read_bytes().replace(b"\r\n", b"\n")).hexdigest() != h]
print("\n".join(f"frozen file changed: {p}" for p in changed) or "frozen files unchanged")
sys.exit(bool(changed))
PY
```

**The template and the example in step.** They are kept in step by hand, by the rules in
`AGENTS.md`; these checks are the only automation. For each file `git ls-files templates/strategy`
lists, each check drops a strategy example's own lines, marked as `AGENTS.md` says (in a notebook,
also every marked block inside a markdown cell), and compares the rest with the template's copy,
blank lines aside. For the Markdown and Python files:

```bash
for x in examples/strategy/*/; do
  for f in $(git ls-files templates/strategy | grep -E '\.(md|py)$'); do
    e="$x${f#templates/strategy/}"
    [ -f "$e" ] || continue
    awk '/^(<!-- example: begin -->|# --- example: begin ---)$/{s=1;next} /^(<!-- example: end -->|# --- example: end ---)$/{s=0;next} !s' "$e" \
      | diff -B <(awk 1 "$f") - > /dev/null || echo "differs: $e"
  done
done
```

For the notebooks, cell by cell, by cell id:

```bash
for x in examples/strategy/*/; do for nb in $(git ls-files templates/strategy | grep '\.ipynb$'); do
  uv run --no-project python - "$nb" "$x${nb#templates/strategy/}" <<'PY' || echo "differs: $x${nb#templates/strategy/}"
import json, re, sys
marked = re.compile(r'^(<!-- example: begin -->|# --- example: begin ---)$.*?^(<!-- example: end -->|# --- example: end ---)$\n?', re.M | re.S)
def cells(path):
    kept = [c for c in json.load(open(path, encoding='utf-8'))['cells'] if not ''.join(c['source']).startswith('# EXAMPLE-ONLY CELL')]
    return [(c.get('id'), c['cell_type'], [l for l in marked.sub('', ''.join(c['source'])).splitlines() if l.strip()]) for c in kept]
sys.exit(cells(sys.argv[1]) != cells(sys.argv[2]))
PY
done; done
```

A file either check names is a fault, unless `AGENTS.md` lists it as an exception.

**To try a change** to a skill, a command, an instruction or the agent, install it at project scope
from a short scratch folder, with APM 0.33.0, **in a shell whose home is a short, empty throwaway
folder**. Never install the working tree with `-g`: on Windows that stages its ignored folders too,
past the path limit. A skill installed for your user wins over a project skill of the same name, so
without the throwaway home the check would run your installed copy, and the walk below would change
your real setup. From the repository's root:

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

`git stash create` takes your uncommitted changes to tracked files, and a new file once `git add`
has staged it, without touching them; with nothing uncommitted, the archive is `HEAD`. Either way
it holds the files the commit would, with LF endings and none of the working tree's ignored
folders. Open a new session in the `check` folder, from that shell.

**To try the Python library template**, before a release that changes it, `scaffold.py` or
`init-python-library`, build a copy of it under `$K`, in that throwaway shell: nothing else
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

Then the same in a second copy, `$K/lib2`, first named with the longest name it accepts by its
`scripts/name_library.py`, run as the `init-python-library` skill runs it. Every check passes there
too, and this prints nothing:

```bash
git -C "$K/lib2" grep -n -e kn_python_library_template -e kn-python-library-template -e KnPythonLibraryTemplate -e "KN Python Library Template" -e "KaxaNuk SC" -- ':!AGENTS.md'
```

**Before a release, make the install above with the commit to be tagged.** It should deploy exactly
26 skills, 9 commands, 3 rules and 1 agent, with no warning.

**Then install it for the user twice**, from the archive, each time from a new shell whose `HOME`
and `USERPROFILE` are a new empty folder under `$K`: once Claude, then Codex; once Codex, then
Claude.

- On the first assistant, install the package as `SETUP.md`'s step 2 does, with the archive in
  place of `KaxaNuk/KaxaNuk-Researcher`. Run `init-researcher` there, which runs `interview`, for a
  researcher whose name has an accent, *Sofía*: its home under `$K`, its files deployed as `sofia`.
  The archive installs as `_local/KaxaNuk-Researcher`, so wherever the files name
  `$HOME/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/`, tell the assistant to read
  `$HOME/.apm/apm_modules/_local/KaxaNuk-Researcher/` instead.
- On the second, install the package and the home for it, as `SETUP.md`'s *another assistant* does,
  then update:

```bash
S="$K/KaxaNuk-Researcher/.apm/skills/init-researcher/scripts/user_targets.py"
uvx --from apm-cli==0.33.0 apm install -g "$K/KaxaNuk-Researcher" --target <the second assistant>
uv run --no-project python "$S" add <the second assistant>
uvx --from apm-cli==0.33.0 apm install -g "<Sofía's home>"
uvx --from apm-cli==0.33.0 apm update -g --yes
uv run --no-project python "$S" check claude sofia
uv run --no-project python "$S" check codex sofia
```

Both checks pass. On disk, `~/.claude/` holds the package's 26 skills and `sofia` in `skills/`,
9 commands, 3 rules and 2 agents, `blueprint-critic.md` and `sofia.md`; `~/.agents/skills/` the same
27 skills; and `~/.codex/agents/` 2 agents, `blueprint-critic.toml` and `sofia.toml`.

**If the release changes a skill, a command or a script**, walk the rest of the newcomer's path by
hand on each run's first assistant, once in Spanish and once on Codex, an assistant with no question
tool: `next`, `read` on one clipping, a round of `philosophy` at Starter and one on how you work,
`brief setup` and `brief`, and `init-strategy`; and `init-python-library`, with `next` in the folder
it makes, `workshop` on one session, *Bootcamp S03*, and `known-answer` on one recipe, beside the
strategy `init-strategy` made, when the release changes them.

**When it changes `init-researcher` or `interview`**, last, say `init-researcher` there again: it
asks `Another?`, and *Make a second one*, named *Sofia*, makes a second home under `$K` whose files
take a name other than `sofia`, with Sofía's untouched. Try a second researcher there and only
there, never beside your own.

Delete the scratch folder afterwards: under the throwaway home, nothing the walk installed or
scheduled reached your own. A newer APM is adopted only when these installs pass with it, on
Windows.
