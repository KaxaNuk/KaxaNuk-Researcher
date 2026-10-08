---
name: init-python-library
description: >
  Create a new Python library — code to install and import, never the researcher's library of
  reading — in a new folder, from the KaxaNuk Python Library Template inside the researcher
  package, laid out like the KaxaNuk Data Curator: copied by a script byte for byte, its first
  version saved, then named by a second script and saved again. Only when the owner runs it by
  name, with the Python library's name, or in a copy not yet named. It does NOT build the
  environment or publish anything (`next`, in the new folder, leads there), does NOT create a
  strategy (use `init-strategy`), and does NOT add a source to the library of reading (`read` does).
metadata:
  version: 0.1.0
---

# Init Python library — a new Python library, one folder, one repository

The owner starts a Python library of their own: code others install with `pip` and import. What
they said carries the arguments: its name — `fcf-screen` — which becomes the folder, the repository
and the name on PyPI; where to put it; and optionally one sentence on what it does. One Python
library is one repository: never inside a strategy, the researcher's home, another project or this
package. Here *library* means code; the researcher's library of reading is `Knowledge/`, which this
skill never touches.

**The copy and the naming are the scripts', never yours.** `scaffold.py` copies the template byte
for byte, so every Python library made from the same package version starts identical;
`name_library.py`, in this skill's folder, only puts the names in — the package folder moved to
the import name, the template's names replaced where it has them, the holder on the licence's first
line — and refuses any folder but a fresh copy. A file of the template is never written from
memory, and the naming adds no text of its own: the status line, the `## [Unreleased]` entry of
`CHANGELOG.md` and the version, 0.1.0, are true before and after it.

## When to Use

- The owner runs `init-python-library` by name — *init-python-library fcf-screen*, *start a Python
  library called …*.
- The session is open in a copy not yet named — its `AGENTS.md` holds
  `<!-- kaxanuk-starting-point: python-library -->` alone at column 0, and `src/` still holds
  `kn_python_library_template/` — and the owner runs it there, as `next` says: step 1 without the
  place, the plan, then step 4 on this folder.
- Not in the template itself: a folder that is not the top of a git repository of its own, such as
  `templates/python-library/` inside the package, is never named — the script refuses it. Copy it
  with step 3 instead.
- Not on its own initiative, and not to repair a Python library. A file the naming never changes
  comes back from the template with the copy script, which never overwrites — `.gitignore`,
  `.gitattributes`, `.readthedocs.yml`, `.github/workflows/main.yml`, `CLAUDE.md`, `AGENTS.md`:

  ```bash
  uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" python-library . --only <path>
  ```

  Never a file the naming changes — under `src/`, `tests/` or `docs/`, the README,
  `pyproject.toml`, `CHANGELOG.md` — into a named one: it would land with the template's names.
  Copy it into an empty folder of its own instead, to read beside the library's.

## Steps

1. **The name, and the names it gives.** Ask through the question tool for what is missing: the
   name — lowercase letters, digits and single hyphens, starting with a letter, at most 40
   characters — and the parent folder, defaulting to the parent of the folder the session is open
   in, so the Python library lands beside the owner's other projects: `D:\Research\fcf-screen`.
   On Windows, keep it short: a deep synced path such as `C:\Users\<you>\OneDrive\...` breaks tools
   later with misleading errors such as `WinError 3`. Say the full path. Then check the name:

   ```bash
   uv run --no-project python "<this skill's directory>/scripts/name_library.py" --check-name <name>
   ```

   It prints the names one name gives — `fcf-screen` on PyPI and in `pip install`, `fcf_screen` to
   import, `FcfScreenError` for its errors, *Fcf Screen* as its title — and asks PyPI whether the
   name is taken, the one thing that goes online. It refuses, saying why, a name Python cannot
   import or that would hide one of its own modules — `class`, `json` — a folder of the template —
   `tests`, `docs` — a tool the template installs — `pytest`, `requests` — a name Windows keeps for
   a device — `con`, `nul` — and a name another project holds on PyPI: ask for another. A name PyPI
   holds, or one it could not be asked about, is the owner's to keep only for a Python library they
   will never publish: ask, and on that answer add `--unpublished` here and in step 4. The title is
   the owner's to change, in plain ASCII — `--title "FCF Screen"`, here and in step 4.

   **The holder** `LICENSE` names, also the author in `pyproject.toml`: the owner's name as
   *Works for* in the home's `RESEARCHER.md` gives it, else `git config --global user.name`; with
   neither, ask — *whose name goes in the licence, yours or your company's?* — never invented.

2. **The plan.** In chat: the full path; the four names and the holder; that it will hold the
   KaxaNuk Python Library Template at this package's version, laid out like the KaxaNuk Data
   Curator; that it keeps dated versions from the start — the template as copied, then the naming,
   each saved; that the naming moves the package folder to the import name and puts the names in
   where the template has its own, and the holder on the licence's first line; and that nothing
   else on the machine changes, the date of the weekly version check in the home's git config
   aside: nothing is installed, and nothing goes online but the check of the name. When a newer
   package is out, checked and dated as item 5 of *Step 4* in the `next` skill beside this one says
   — never with `updatereminder` off or an `updatenext` still ahead — one more line: *a newer
   version of the package is out, X.Y.Z: `update` first brings the newest template*. Never a
   question of its own, and the copy never waits on it. Ask for the go — *Go*, *Change something*,
   *Stop* — and run on *Go* only.

3. **Copy.** The script is in the `init-strategy` skill's folder, beside this one:

   ```bash
   uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" python-library "<full path>"
   ```

   It takes a leading `~` as the home folder, and refuses a folder that exists and is not empty,
   saying why; go back to step 1 rather than around it. On Windows without long paths, it also
   refuses a destination so deep that a copied path would pass 259 characters, names that path and
   the longest destination that fits, and writes nothing; choose a shorter place. A copy the system
   stops partway — a full disk, a file refused — ends in one line naming the file and the reason;
   the partial folder can be deleted. If it cannot find the package, it prints the install command —
   give it to the owner. A fork of the package, or a clone in a folder of another name, is not found
   on its own: pass `--package <its install folder>`. A git step that fails leaves the copy in place
   — the script still exits 0 — and prints every command that finishes the repository from that step
   on. If git is missing, install it on the owner's go, then run the printed commands in the new
   folder. If the first commit fails for want of a git identity, ask for *a name and an email to
   sign the versions your researcher saves*, never invented; set them in that folder only,
   `git config user.name "<name>"` and `git config user.email "<email>"`, then run the printed
   commands there. The naming waits for that first version.

4. **Name it**, on the same go, once the copy's first version is saved:

   ```bash
   uv run --no-project python "<this skill's directory>/scripts/name_library.py" "<full path>" --name <name> --title "<title>" --holder "<holder>" --description "<sentence>"
   ```

   `--description` only with the owner's own sentence, never one of yours; `--unpublished` as step 1
   settled. The script asks PyPI again, then refuses, writing nothing, a folder that is not the top
   of a git repository of its own, one whose history holds more than the copy's first version, and
   one with a change not saved: say why, and stop. It moves the package folder first, then rewrites
   each file that holds a name, and prints each. **Only when it exits 0**, save the naming:

   ```bash
   git -C "<full path>" commit --all -m "Name the library <name>"
   ```

   `--all` takes the move and every rewritten file, and leaves out a `uv.lock` written before the
   naming, which the next `uv sync` rewrites. A commit refused for want of an identity is asked for
   as step 3 says. If the script stops partway — a file a sync client or an antivirus holds — it
   names the file and the reason: `git -C "<full path>" reset --hard` puts the copy back as it was
   copied, and step 4 runs again.

5. **Hand over**, in plain words, three lines: where the Python library is, and that the folder is
   the whole project; to open it in a **new** session — in the Claude desktop app, a new Code
   session in that folder; in a terminal, `claude` or `codex` there — and say `next`, whose first
   thing is building the environment, `uv sync`, which the agent there runs for them; and that
   GitHub, Read the Docs and PyPI are theirs to open, later, each when `next` names it. For one they
   will never publish, its status line says *not published* — the owner's words, written there in
   that session — and `next` leaves Read the Docs and PyPI out.

## References

- `scripts/name_library.py`, in this skill's folder — checks a name and prints the four names it
  gives, and names a fresh copy; `--help` has every option.
- `scripts/scaffold.py`, in the `init-strategy` skill's folder — copies `templates/python-library/`
  from the KaxaNuk Researcher package.
- The KaxaNuk Data Curator, <https://github.com/KaxaNuk/Data-Curator> — the Python library the
  template is laid out like.
