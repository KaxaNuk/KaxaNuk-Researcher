---
name: init-strategy
description: >
  Create a new KaxaNuk strategy repository in a new folder, from the KaxaNuk Strategy Template that
  ships inside the researcher package — copied by a script, byte for byte, its first version
  saved. Only when the owner runs it by name, with the strategy's name. It does NOT set up the
  environment or the keys (the new folder's SETUP.md does), does NOT copy the worked example (use
  `init-example`), does NOT create a researcher (use `init-researcher`), and does NOT create a
  Python library (use `init-python-library`).
metadata:
  version: 0.3.3
---

# Init strategy — a new strategy, one folder, one repository

The owner starts a new strategy. What they said carries the arguments: the strategy's name, which
becomes the folder and the repository — `fcf-yield-quality`, not `Experiment` — where to put it,
and optionally one sentence on the idea. One strategy is one repository: never create a strategy
inside another strategy, inside the researcher's home, or inside this package.

**The copy is the script's, never yours.** A file of the template is never written from memory, so
every strategy made from the same package version starts identical.

## When to Use

- The owner runs `init-strategy` by name — *init-strategy fcf-yield-quality*, *start a new strategy
  called …*.
- Not on its own initiative, and not to repair an existing strategy. A file of the template that
  the strategy lacks — lost, or never there because the strategy was made before template 0.10.0
  shipped the drivers, notebooks and documents — comes back from the template, never from the
  example, whose copy is filled in: run this skill's script from the strategy's root; it never
  overwrites a file.

  ```bash
  uv run --no-project python "<this skill's directory>/scripts/scaffold.py" strategy . --only <path>
  ```

## Steps

1. **The name and the place.** Ask for whatever is missing through the question tool: the name,
   and the parent folder, defaulting to the parent of the folder the session is open in — so a
   strategy lands beside the others, `D:\Research\fcf-yield-quality`. On Windows, keep it short:
   a deep synced path such as `C:\Users\<you>\OneDrive\...` breaks tools later with misleading
   errors such as `WinError 3`. Say the full path you will create.

2. **The plan.** In chat: the path, that it will hold the KaxaNuk Strategy Template at this
   package's version, that it keeps dated versions from the start, the first saved now, and that
   nothing else on the machine changes, the date of the weekly version check in the home's git
   config aside. When a newer package is out, checked and dated as item 5 of *Step 4* in the `next`
   skill beside this one says — never with `updatereminder` off or an `updatenext` still ahead — one
   more line: *a newer version of the package is out, X.Y.Z: `update` first brings the newest
   template*. Never a question of its own, and the copy never waits on it. Ask for the go — *Go*,
   *Change something*, *Stop* — and run on *Go* only.

3. **Copy.** The script is in this skill's folder:

   ```bash
   uv run --no-project python "<this skill's directory>/scripts/scaffold.py" strategy "<full path>"
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
   commands there.

4. **Hand over.** Tell the owner to open the new folder in a **new** session and follow its
   `SETUP.md` from step 2. Repeat their sentence, if any, for them to give the new session at its
   `SETUP.md` step 5, the README's first line; then `OBJECTIVE.md`, before any paper.

## References

- `scripts/scaffold.py`, in this skill's folder — copies `templates/strategy/` from the
  KaxaNuk Researcher package; `--help` has every option. `init-researcher`, `init-example` and
  `init-python-library` run the same script.
