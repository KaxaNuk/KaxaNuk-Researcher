---
name: init-strategy
description: >
  Create a new KaxaNuk strategy repository in a new folder, from the KaxaNuk Strategy Template that
  ships inside the researcher package — copied by a script, byte for byte, then made a git
  repository with its first commit. Only when the owner runs it by name, with the strategy's name.
  It does NOT set up the environment or the keys (the new folder's SETUP.md does), does NOT copy
  the worked example (use `init-example`), and does NOT create a researcher (use
  `init-researcher`).
metadata:
  version: 0.1.2
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
   package's version, that it becomes a git repository on branch `main` with the first commit
   *Start from the KaxaNuk Strategy Template*, and that nothing else on the machine changes. Ask
   for the go — *Go*, *Change something*, *Stop* — and run on *Go* only.

3. **Copy.** The script is in this skill's folder:

   ```bash
   uv run --no-project python "<this skill's directory>/scripts/scaffold.py" strategy "<full path>"
   ```

   It refuses a folder that exists and is not empty, and says why; go back to step 1 rather than
   around it. If it cannot find the package, it prints the install command — give it to the owner.
   If the first commit fails for want of a git identity, ask for the name and email — never invent
   them — set them in that repository only, `git config user.name "<name>"` and
   `git config user.email "<email>"`, and commit with the message the script printed.

4. **Hand over.** Tell the owner to open the new folder in a **new** session and follow its
   `SETUP.md` from step 2 — the environment, the keys, and the strategy's own README, into which
   their one sentence goes. Then `OBJECTIVE.md` comes first, before any paper. Say that the
   repository has no remote yet: publishing it to GitHub is theirs, one repository per strategy.

## References

- `scripts/scaffold.py`, in this skill's folder — copies `templates/strategy/` from the
  KaxaNuk Researcher package; `--help` has every option. `init-researcher` and `init-example` run
  the same script.
