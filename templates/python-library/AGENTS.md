# Agents — how work is done here

<!-- kaxanuk-starting-point: python-library -->

> **Status: nothing released yet.** Replace this line as the library moves; it is the same line
> in `README.md` and `AGENTS.md`.

This repository is a Python library, laid out like the
[KaxaNuk Data Curator](https://github.com/KaxaNuk/Data-Curator), whose repository shows a full
Python library built this way. `README.md` says what the library is; this file says how work is
done here. The marker under the title tells the KaxaNuk Researcher's `next` what this folder is:
keep it.

## First run — for the agent

**If this folder is not the top of a git repository of its own** — `git rev-parse --show-toplevel`
fails, or names another folder — it is the KaxaNuk Python Library Template itself, inside the
KaxaNuk Researcher package: nothing is set up or named here, and `init-python-library <name>`
copies it into a folder of its own; or a copy whose repository is not finished: run the commands
`scaffold.py` printed, then name it.

**If `src/` still holds `kn_python_library_template/`, the library is not named yet.**
`init-python-library`, run by name in this folder, names it first. Set nothing up before it:
`uv sync` would write the template's name into `uv.lock`.

**If `.venv/` is missing, nothing is set up yet.** Run `uv sync` in this folder, never a level
above it: it fetches Python if needed and installs the library, editable, with every development
tool — pytest, ruff, mypy, Sphinx. It writes `uv.lock`, which is committed. Install no skills
here: the KaxaNuk Researcher's are installed once for the user.

## What is where

```
src/<package>/              the library; __init__.py holds __version__ and the public API, __all__
  exceptions.py             its error, from which every error it raises derives
  example.py                the template's example, replaced by the library's first module
  py.typed                  tells type checkers the library carries type hints
tests/unit/                 one <module>_test.py per module of src/<package>/
docs/source/                the documentation in Markdown: index.md, api.md, changelog.md; conf.py
.github/workflows/main.yml  tests every push and pull request, builds, publishes a tag to PyPI
.readthedocs.yml            how Read the Docs builds docs/
pyproject.toml              the build, the dependencies, and the settings of ruff, pytest and mypy
CHANGELOG.md                one entry per version, newest first, what is not released on top
```

## How work reaches `main`

Work is committed on `main`, in small commits whose messages say what moved and why, each with its
`CHANGELOG.md` entry under `## [Unreleased]`; the commits that name the library and lock its
environment change nothing a caller sees, and take none. A branch named `issues/<number>` and a
pull request are for a change you want reviewed; the branch is deleted once merged. The
`how-we-work` skill has the rest.

**Before any commit:**

- `uv run ruff check .`, `uv run mypy` and `uv run pytest` pass, and so does the Bloom Code check
  below. A new public function arrives with its test.
- The `CHANGELOG.md` entry is part of the change-set.
- No secrets and no binaries: a key lives in the environment, never in a file here.

## Code style: Bloom Code

This repository follows **Bloom Code**, KaxaNuk's Python style: PEP 8 and a stricter layer whose
one aim is reading speed for someone who has never seen the file. Naming it here is what brings
the KaxaNuk Researcher's Bloom Code and PEP 8 rules into this folder. In short: no abbreviations
and no import aliases; no nested functions; type hints everywhere; one item per line once there
are three; the error message in a variable before `raise`; a blank line before `return`, `raise`
and `yield`; docstrings in prose, never repeating the type hints. No look-alike characters in
Python files, such as curly quotes or long dashes: ruff rejects them.

The `bloom-code-lint` skill checks the mechanical part: run it from this folder, where it finds the
package in `src/`, with `--max-line-length 120`, the line length in `pyproject.toml`. Ruff's rules
are the Data Curator's with one more ignored, `RET504`: Bloom Code keeps the variable a function
returns, so a debugger can see it.

## Tests

pytest, in `tests/`: `tests/unit/` mirrors `src/<package>/` module by module, a test file named
`<module>_test.py`, and every folder holds an `__init__.py`. Plain `def test_*` functions, with
`@pytest.mark.parametrize` for cases and `pytest.raises` for errors; a test's data goes in a
`fixtures/` folder beside it, and a test of something outside the library — a web service, a file
format — in `tests/integration/`. Replace a dependency with pytest's `monkeypatch`: ruff refuses
`unittest.mock`.

## Documentation

Sphinx, with MyST for the Markdown pages and the pydata theme, as the Data Curator's. `api.md`
documents what `__all__` exports, from the docstrings, and `changelog.md` includes `CHANGELOG.md`.
It builds here as `README.md`'s *Development* says, a warning failing the build, and on Read the
Docs from `.readthedocs.yml` once the repository is imported there, the owner's step.

## Versions and releases

Semantic Versioning, read for a Python library: MAJOR when a caller has to change code, MINOR for a
new capability, PATCH for a fix; while on 0.x, a change that breaks a caller bumps MINOR. The
version lives in one place, `__version__` in `src/<package>/__init__.py`, which `pyproject.toml`
reads; it starts at 0.1.0, and `CHANGELOG.md` gathers what is not released yet under
`## [Unreleased]`.

To release: set `__version__` — 0.1.0 is already there for the first — and rename
`## [Unreleased]` to `## [X.Y.Z] - YYYY-MM-DD`; commit, then tag `main` and push the tag:
`git tag -a vX.Y.Z -m "X.Y.Z: <the entry's first sentence>"`, then `git push origin vX.Y.Z`. The
workflow tests, builds, checks that the tag names the version it built, and publishes to PyPI by
trusted publishing, so no token is stored anywhere.

**Once, before the first release, the owner's step:** on pypi.org, add a pending publisher for this
repository, workflow `main.yml`, environment `pypi`. The same on test.pypi.org with environment
`testpypi` lets a run started by hand from the Actions tab publish a try there first; TestPyPI
takes each version once, and the workflow skips one it already holds. On GitHub, the repository's
*Settings*, *Environments*, can limit `pypi` to tags `v*`.

## Next

The KaxaNuk Researcher's `next` reads this table: the first row whose *Done when* fails gives the
next thing. Every check only reads. Kept private, the library says *not published* in its status
line, and rows 7 and 8 then pass.

| # | Done when | The next thing |
| --- | --- | --- |
| 1 | the library is named: `src/` holds no `kn_python_library_template/`, and the `name` in `pyproject.toml` is not `kn-python-library-template` | `init-python-library`, run by name in this folder: on the owner's go it names a copy `init-python-library` made, with nothing saved or changed since. In the template itself — not the top of a git repository of its own, as *First run* says — nothing: `init-python-library <name>` copies it elsewhere |
| 2 | the environment is built: on this machine `.venv/` exists, and `git ls-files uv.lock` prints `uv.lock` | `uv sync`, then the lock saved alone: `git add uv.lock`, then `git commit -m "Lock the development environment" -- uv.lock` |
| 3 | the library says what it is: `README.md`, `docs/source/index.md` and the `description` in `pyproject.toml` no longer hold `[One sentence on what the library does.]` | that sentence, in the owner's words, in all three; never invented |
| 4 | the library has a module of its own: `src/<package>/example.py` and `tests/unit/example_test.py` are gone, and a module in `src/<package>/` has its `tests/unit/<module>_test.py` | the first module and its test, in Bloom Code from the first line; then the example's two files deleted, its lines in `__init__.py` and the README's *Usage* replaced, and the new module named in the *Unreleased* entry of `CHANGELOG.md` |
| 5 | it is on GitHub: `git remote get-url origin` names a GitHub repository, and `git grep -l github-owner -- ':!AGENTS.md'` prints nothing | the repository, made by the owner on github.com, or by `gh repo create <account>/<name> --private --source . --push` on their go — `--public` for one to publish, as Read the Docs is free for a public one; then `github-owner` replaced by the account in `README.md` and `pyproject.toml` |
| 6 | the workflow passes on `main`: `gh run list --workflow main.yml --branch main --limit 1 --json conclusion --jq ".[0].conclusion"` prints `success`; without `gh`, the owner reads the Actions tab | the failing step's log, read, and the fix pushed |
| 7 | the documentation is online: the link under *Documentation* in `README.md` answers — or the status line says *not published* | the owner's step, once: the repository imported at readthedocs.org, and the link corrected if Read the Docs named the project otherwise; a build warning fails it there, and `uv run sphinx-build -W -b html docs/source docs/_build/html` shows it here. Then its badge beside *Build Status* in `README.md`, as the Data Curator's README has it |
| 8 | the first release is out: a `vX.Y.Z` tag names the version `__version__` declares, `CHANGELOG.md` has its `## [X.Y.Z]` entry, and `https://pypi.org/pypi/<the name in pyproject.toml>/<that version>/json` answers, its `info.project_urls.Repository` the repository `origin` names — or the status line says *not published* | the trusted publishers, the owner's step, as *Versions and releases* says; a try on TestPyPI; then the release. Then the PyPI version and downloads badges in `README.md`, as the Data Curator's README has them |
