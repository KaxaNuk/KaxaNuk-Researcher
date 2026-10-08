---
name: init-example
description: >
  Copy the KaxaNuk worked example strategy, golden-flow, into a new folder to study or run it — or
  one of its worked files, such as Data/analyzer.ipynb, into a folder of its own to read beside a
  strategy's own — from the copy inside the researcher package, by a script. Only when the owner
  runs it by name. It does NOT start a strategy of the owner's own (use `init-strategy`), does NOT
  bring back a template file a strategy lacks (`init-strategy`'s script with `--only` does), and
  never builds on the example.
metadata:
  version: 0.4.2
---

# Init example — the worked strategy, whole or one piece at a time

The example is one strategy, `golden-flow`, worked through every folder of the KaxaNuk Strategy
Template: the objective and its claims, the notes, the universe, the data, the experiment and its
documents, the findings, the results and the paper-trading gate. Its own lines sit between example
markers — `<!-- example: begin -->` and `<!-- example: end -->` in Markdown,
`# --- example: begin ---` in Python, `# EXAMPLE-ONLY CELL` on a notebook cell — beside the
template's description of what belongs in each file. It is also readable without installing
anything, in `examples/golden-flow/` of `KaxaNuk/KaxaNuk-Researcher`.

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
   `golden-flow` in the folder a caller hands it, else beside the researcher's home — the folder
   holding `RESEARCHER.md` here, or the one the researcher's skill names — else beside the folder
   the session is open in. Never into a strategy: its file of the same name is the template's
   description, for the owner to fill.

2. **The plan.** In chat: what will be copied and where; for one piece, that the folder is made if
   it is not there, that the piece keeps its path inside it, that nothing already there is
   overwritten — the script refuses rather than overwrite — and that the worked strategy's own
   lines come with it. When a newer package is out, checked and dated as item 5 of *Step 4* in the
   `next` skill beside this one says — never with `updatereminder` off or an `updatenext` still
   ahead — one more line: *a newer version of the package is out, X.Y.Z: `update` first brings the
   newest example*. Never a question of its own, and the copy never waits on it. Ask for the go —
   *Go*, *Change something*, *Stop* — and run on *Go* only.

3. **Copy.** The script is in the `init-strategy` skill's folder, beside this one:

   ```bash
   uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" example "<new folder>"
   uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" example "<its folder>" --only <path>
   ```

   The whole example becomes a git repository with its first commit; one piece is only copied, into
   a folder that must exist — make it, empty, when it does not. On Windows without long paths, the
   script refuses a destination so deep that a copied path would pass 259 characters, names that
   path and the longest destination that fits, and writes nothing; choose a shorter place. A fork of
   the package, or a clone in a folder of another name, is not found on its own: pass
   `--package <its install folder>`. A git step that fails leaves the copy in place — the script
   still exits 0 — and prints every command that finishes the repository from that step on. If git
   is missing, install it on the owner's go, then run the printed commands in the new folder. If the
   first commit fails for want of a git identity, ask for *a name and an email to sign the versions
   your researcher saves*, never invented; set them in that folder only,
   `git config user.name "<name>"` and `git config user.email "<email>"`, then run the printed
   commands there.

4. **For one piece, say what it shows.** Everything between the markers in what was copied is
   `golden-flow`'s own work, and so, whole, are its seed and every file only the example has — its
   notes, `Universe/seed.py`, a frozen book's `FREEZE.json` and the files it hashes; around the
   markers is the template's description, which the strategy's copy already holds. Name the path
   it landed at, to read beside the strategy's file; never copy its lines into the strategy.

5. **Hand over**, for the whole example, in three short lines:
   - *Read*, with nothing installed: `OBJECTIVE.md`, `RESULTS.md`, then `BLUEPRINT_1.md` and
     `FINDINGS_1.md` in `Experiments/Experiment_1/`, then `Paper_Trading/BITACORA.md`.
   - *Run*: its README's *Run it*, in a **new** session opened in the folder — an FMP key of their
     own; and, from `lab@kaxanuk.mx`, saying what they are for, the Analytics Factory's KN US Equity
     Core and factor model files and the Backtest Engine and Attribution Analysis licences
     (<https://www.kaxanuk.mx/lab> shows the Lab); the download takes about an hour and a half.
   - *Own*: a strategy of your own is `init-strategy <name>`; nothing is built on the example, and
     its paper book, `Paper_Trading/Paper_Trading_1/`, is a record that does not run.

## References

- `scripts/scaffold.py`, in the `init-strategy` skill's folder — copies
  `examples/golden-flow/` from the KaxaNuk Researcher package, whole or `--only` one path.
