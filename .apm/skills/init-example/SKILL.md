---
name: init-example
description: >
  Copy the KaxaNuk worked example strategy, liquid-golden-cross, into a new folder to study or run
  it — or one of its worked files, such as Data/analyzer.ipynb, into a folder of its own to read
  beside a strategy's own — from the copy that ships inside the researcher package, by a script.
  Only when the owner runs it by name. It does NOT start a strategy of the owner's own (use
  `init-strategy`), does NOT bring back a file of the template a strategy lacks (`init-strategy`'s
  script with `--only` does), and never builds on the example: it is a worked strategy to read,
  not a template to fill.
metadata:
  version: 0.1.4
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
- **One worked file, to read beside your own** — *init-example Data/analyzer.ipynb*, *show me the
  example's blueprint*. A strategy's copy of a file says what belongs in it; the example's shows it
  filled. The piece goes into a folder of its own, never into the strategy, and nothing is built
  on it.
- Not to bring back a file a strategy lacks — lost, or never there because the strategy was made
  before template 0.10.0 shipped the drivers, notebooks and documents. That file comes back from
  the template, never from the example, whose copy is filled in: `init-strategy`'s script, run from
  the strategy's root, `scaffold.py strategy . --only <path>`, which never overwrites.
- Not on its own initiative. A skill that points to the example names this skill and the path, and
  the owner runs it.

## Steps

1. **Which of the two, and where.** A path of the example — `Data/analyzer.ipynb`,
   `Experiments/Experiment_1` — means that one piece; no path means the whole example. Either lands
   in a folder outside any strategy: ask where through the question tool, defaulting to
   `liquid-golden-cross` beside the folder the session is open in. Never into a strategy: its file
   of the same name is the template's description, for the owner to fill.

2. **The plan.** In chat: what will be copied and where; for one piece, that the folder is made if
   it is not there, that the piece keeps its path inside it, that nothing already there is
   overwritten — the script refuses rather than overwrite — and that the worked strategy's own
   lines come with it. Ask for the go — *Go*, *Change something*, *Stop* — and run on *Go* only.

3. **Copy.** The script is in the `init-strategy` skill's folder, beside this one:

   ```bash
   uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" example "<new folder>"
   uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" example "<its folder>" --only <path>
   ```

   The whole example becomes a git repository with its first commit; one piece is only copied, into
   a folder that must exist — make it, empty, when it does not. A fork of the package, or a clone
   in a folder of another name, is not found on its own: pass `--package <its install folder>`.

4. **For one piece, say what it shows.** Everything between the markers in what was copied is
   `liquid-golden-cross`'s own work; around it is the template's description, which the strategy's
   copy already holds. Name the path it landed at, to read beside the strategy's file; never copy
   its lines into the strategy.

5. **Hand over.** For the whole example: open it in a **new** session, and its `SETUP.md` from
   step 2 builds the environment if they want to run it. Never build a strategy on it; a strategy
   of their own is `init-strategy`.

## References

- `scripts/scaffold.py`, in the `init-strategy` skill's folder — copies
  `examples/liquid-golden-cross/` from the KaxaNuk Researcher package, whole or `--only` one path.
