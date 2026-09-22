---
name: init-example
description: >
  Copy the KaxaNuk worked example strategy, liquid-golden-cross, into a new folder to study or run
  it — or copy one of its files or folders, such as Experiments/Experiment_1, into a folder that
  lacks it — from the copy that ships inside the researcher package, by a script. Only when the
  owner runs it by name. It does NOT start a strategy of the owner's own (use `init-strategy`),
  does NOT restore a file a strategy lacks (the template's copy, through `init-strategy`), and never
  builds on the example: it is a worked strategy to read, not a template to fill.
metadata:
  version: 0.2.0
---

# Init example — the worked strategy, whole or one piece at a time

The example is one strategy, `liquid-golden-cross`, worked through every folder of the KaxaNuk
Strategy Template: the objective and its claims, the notes, the universe, the data, the experiment
and its documents, the findings and the results. Its own lines sit between example markers —
`<!-- example: begin -->` and `<!-- example: end -->` in Markdown, `# --- example: begin ---` in
Python, `# EXAMPLE-ONLY CELL` on a notebook cell — beside the template's description of what
belongs in each file. It is also readable without installing anything, in
`examples/liquid-golden-cross/` of `KaxaNuk/KaxaNuk-Researcher`.

## When to Use

- **The whole example, in a new folder** — *init-example*, *give me the example to look at*. To
  read it, run its notebooks, or see what a finished experiment looks like.
- **One piece into a folder that lacks it** — *init-example Experiments/Experiment_1*, to read that
  piece worked through. It is not how a strategy gets its files: one made from template 0.11.0 on
  already holds every file the process expects, each as a description of what belongs in it, and
  the script refuses to overwrite one. A strategy that lacks a template file — one made before
  0.11.0 — restores it from the template, as the `init-strategy` skill says, never from here.
- Not on its own initiative; the owner runs it by name.

## Steps

1. **Which of the two.** A path of the example — `Experiments/Experiment_1`,
   `Paper_Trading/BITACORA.md` — means one piece into the folder the session is open in, or the
   one the owner names, where that path is missing. If the owner wants the file to fill in for
   their strategy, it is the template's: give the `init-strategy` skill's `--only` command
   instead, and stop. No path means the whole example into a new folder: ask where through the
   question tool, defaulting to `liquid-golden-cross` beside the folder the session is open in.

2. **The plan.** In chat: what will be copied and where; for one piece, that nothing already
   there is overwritten — the script refuses rather than overwrite — and that the worked strategy's
   own lines come with it. Ask for the go — *Go*, *Change something*, *Stop* — and run on *Go* only.

3. **Copy.** The script is in the `init-strategy` skill's folder, beside this one:

   ```bash
   uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" example "<new folder>"
   uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" example "<strategy root>" --only <path>
   ```

   The whole example becomes a git repository with its first commit; one piece is only copied.

4. **For one piece, say what is the example's.** Everything between the markers in what was
   copied is `liquid-golden-cross`'s; the template's description around it is the process's. List
   the marked blocks by file.

5. **Hand over.** For the whole example: open it in a **new** session, and its `SETUP.md` from
   step 2 builds the environment if they want to run it. Never build a strategy on it; a strategy
   of their own is `init-strategy`.

## References

- `scripts/scaffold.py`, in the `init-strategy` skill's folder — copies
  `examples/liquid-golden-cross/` from the KaxaNuk Researcher package, whole or `--only` one path.
