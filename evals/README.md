# Evals

Behavioural evals for the KaxaNuk Researcher's skills and commands, run by Claude Code's
`claude plugin eval` against what a user actually installs.

## What this is

Three layers:

- **Triggering** (`triggering/requests.toml`): for each of the 16 skills, two requests that should
  fire it and one near-miss that must not. The runner turns each line into a case: 48 in all.
- **Contract** (`contract/<surface>/<case>/`, 10 cases): hard gates, graded by tools, files and
  text, with no judge — a plan before any write, a refusal when a prerequisite is missing, a source
  or a home read before anything is said about it.
- **Quality** (`quality/<surface>/<case>/`, 3 cases): what was produced, judged against written
  criteria.

Contract and quality cover the skills `read` and `query`, the command `blueprint`, and
`init-researcher`'s refusal when a home already exists. No case lists Bash, so no case needs a
shell. A case that lists Bash runs only on a Linux host whose sandbox runs a shell (`bubblewrap`
and `socat`); batch it apart. Everything else is triggering only: `init-strategy`, `init-example`
and the rest of `init-researcher`, whose contract is a copy made by a script, and `read`'s
extraction of a PDF, both of which need a shell (the unit tests cover the scripts); the nine
Investment Lab skills, whose behaviour needs a strategy's data and, for three, KaxaNuk's private
libraries; the two house rules, `how-we-work` and `bloom-code-lint`; and the other ten commands.
Codex and Cursor are out of scope (the harness is Claude only), and so is CI (there is none).

## Running

From the repository root:

```bash
uv run --no-project --with pypdf python tools/eval_run.py --case 'triggering/*' --max-cost-usd 21
uv run --no-project --with pypdf python tools/eval_run.py --case 'contract/blueprint/*' \
  --max-cost-usd 10
```

`tools/eval_run.py` exports the working tree without its ignored files (uncommitted edits count)
into a temporary folder, runs the real `apm install -g <export> --target claude` into a temporary
home, and assembles `evals/.run/` (ignored) from it:

```
evals/.run/plugin/              skills/ and commands/ from the install, a minimal manifest, and
                                the batch's cases in plugin/evals/: those --case matches,
                                committed ones copied, triggering ones generated
evals/.run/templates/           the starting points, beside the plugin, where the init-* skills'
evals/.run/examples/            scaffold.py looks for the package
evals/.run/fixtures/            every fixture, built fresh from the export's templates
```

Then it runs one batch: `claude plugin eval` on the plugin folder, each case run as many times as
its own `runs` says (3 when it says nothing; `--runs` overrides every case), a case passing only
when every run passes. `--dry-run` builds and assembles, prints the grants and the command, and runs
nothing.

- **Every run spends the plan of whoever runs it**, so `--max-cost-usd` is required. The ceiling is
  checked before each run starts; runs already in flight can pass it by a dollar or so. The
  harness's `costUsd` is a list-price estimate: about $0.11 a triggering run, $0.15 to $1.10 a
  contract run, $0.40 to $0.55 a quality run, of which the judge's three votes are $0.12 to $0.22.
- **Models are pinned** so a before and an after compare: sessions on Opus 5.5 (`--model
  claude-opus-5-5`), the quality judge on Fable 5.1 (`--judge-model claude-fable-5-1`). The runner
  passes both, so a case's own `model` is overridden; it passes `--runs` only when you give it.
- **`--ablation none`**: the no-plugin arm is off. It would double the usage, and without the
  plugin no skill can fire. In this mode a `tool_used: Skill` grader counts toward the score.
- **`--case` takes a glob over case names, read as the harness reads it**: `*` matches any run of
  characters, `/` included, `?` one character, and every other character stands for itself, so
  braces and brackets match nothing. Batch by prefix, such as `'triggering/*'` or
  `'contract/read/*'`. Only the matching cases are assembled; none matching stops the run.
  `--case` may be repeated: the batch is the union, and the harness gets `--case '*'` over it.
- **Results** land in `evals/results/<UTC time>-<glob>/` (ignored), for example
  `20260923T000155Z-triggering-all/`, with `report.html` and `aggregate-result.json`;
  `--label triggering-1` names the folder instead of the globs.
- **Traces**: the runner passes `--keep-temp`, so every run's folder stays under
  `/tmp/claude-eval-*`: `out/trace.jsonl` (the session as stream-json) and
  `config/projects/*/*.jsonl` (the session transcript). Copy what you need, then remove it:
  `chmod -R u+rwX <folder> && rm -rf <folder>`.

### What a run is

- **Every run starts empty**: a fresh home and working directory, no `CLAUDE.md`, memory or other
  plugins. The package's rules (its instructions) do not load; a case that needs one says so in
  `append_system_prompt`. Claude Code's built-in skills (`dataviz`, `claude-api`, `code-review`,
  `simplify`, `loop`, `run`, ...) are present in every run, so a near-miss may fire one of them.
- **The run home sets a git identity** (`Plugin Eval <eval@example.invalid>`), and the working
  directory is inside an empty git repository: no run starts without an identity.
- **Grants follow the cases.** A case's `allowed_tools` is the only place its tools are named.
  Read-only tools (`Read`, `Glob`, `Grep`, `Skill`, ...) are granted from there; every other tool
  (`Write`, `Edit`, `Bash`, `WebFetch`, ...) needs the operator's `--allow-tools`, which covers the
  whole batch. The runner passes exactly the gated tools the batch's cases list, and no
  `--allow-tools` at all when they list none, as triggering cases do; it prints each granted tool
  with the cases that list it. A batch that mixes a case needing Write with one that must not have
  it gives Write to both: batch them apart. A tool not granted is absent from the session, so a
  "nothing written" grader passes trivially unless its case lists Write.
- **A malformed case stops the run** before anything is installed, with one line naming it; so does
  a failed export, install or fixture build. The exit code is then 1.
- **Triggering runs end with the error `Reached maximum number of turns (2)`.** It is expected: the
  case stops once a skill is chosen, and the run is still graded.

## The case format

A case is a folder with `prompt.md` and `graders/*.md`, and optionally `case.yaml`.

`prompt.md`: the frontmatter holds the run's fields, the body is the message the owner would type.
An unknown key is an error.

```markdown
---
name: contract/read/clipping-at-home   # what --case matches; the runner requires it
max_turns: 14                          # default 10; reaching it is a run error
timeout_seconds: 300
allowed_tools: [Skill, Read, Glob, Grep, Write, Edit] # the case's grants, and the batch's
---
Read Sources/Clippings/Nullwick_2026_Driftwatch_README.md into my library.
```

Other keys: `runs`, `description`, `tags`, `append_system_prompt`, `env` (`EVAL_*` names only).

The runner reads two keys itself, strictly. `name` is required, in `prompt.md` or `case.yaml`.
`allowed_tools` lives only in `prompt.md`'s frontmatter, as one line of list, a trailing comment
allowed; a block list, a list over several lines, or `execution.allowed_tools` in `case.yaml`
stops the run with the case's name.

`case.yaml` needs `schema_version: "1.1"` and `name`, and holds what points at other files:

```yaml
schema_version: "1.1"
name: quality/blueprint/predictions-cite
context:
  scaffold_script: scaffold.sh    # written by the runner for a case with a FIXTURE
  history_file: history.jsonl     # a replayed first turn; prompt.md's body is the next one
```

**Commands** are namespaced in a run: write `/kaxanuk-researcher-evals:blueprint 1`. A bare
`/blueprint` is sent as text, and reaches the command only if the model chooses to call it. A slash
command expands without a Skill call, so a `tool_used: Skill` grader cannot check it, and its
expanded text is in the session transcript, not in `out/trace.jsonl`. **Skills** are reached by
plain requests, through the Skill tool, as `kaxanuk-researcher-evals:<skill>`.

### Graders

One file per grader; the file name is its name, the frontmatter its type and options, the body a
sentence saying what it protects (for `llm`, the rubric).

`regex`: a JavaScript pattern over a `target`: `last_message` (the default), `trace` (the session
as JSON, quotes escaped), `files` (the paths created in the run) or `{source: file, path: ...}`.

```markdown
---
type: regex
target: last_message
pattern: 'OBJECTIVE\.md'
flags: i                 # inline (?i) is not supported
match: not_contains      # optional: absence; or "count:N" for exactly N matches
---
The refusal names the file that comes first.
```

A `trace` regex matches the command text of a tool call as well as its output, and the model may
print the output a command would have given. To prove a command ran, grade a file only a real run
writes; a `{source: file}` target on a missing file fails.

`tool_used`: the calls to `tool` whose JSON input matches `input_match` number between `min`
(default 1) and `max`. A call that must never happen sets **both** `min: 0` and `max: 0`; `max: 0`
alone fails every run.

```markdown
---
type: tool_used
tool: Write
input_match: 'Knowledge/'
min: 0
max: 0
---
Nothing is written to the library before the owner's go.
```

`llm`: the body is the rubric; `focus` names what the judge reads, with the same values as a regex
`target`. The judge votes three times and passes on two. Each vote is one word, PASS or FAIL, and
no reasoning is kept: check a verdict by reading the evidence against the rubric yourself. So the
quality cases write each rubric as lines that must all hold, quoting the fixture text the judge
compares against. A file `focus` reads one exact path in the workspace, not a glob, and a missing
file fails the grader. A `trace` focus shows the judge only the first and last 12 messages.

```markdown
---
type: llm
focus: {source: file, path: Experiments/Experiment_1/BLUEPRINT_1.md}
---
PASS if every row of the predictions table cites a Bibliotheca/ note or an analyzer section, or is
marked as a lead. FAIL otherwise.
```

## Fixtures

A case that starts from a folder puts a one-line `FIXTURE` file, naming the fixture, in its folder,
and `context.scaffold_script: scaffold.sh` in its `case.yaml`, on a line of its own. The runner
copies the fixture into the case's run copy as `fixture-files/` and writes `scaffold.sh`, which
copies it into the empty working directory before the session starts. Committing either, naming
`scaffold.sh` without a `FIXTURE`, a `FIXTURE` without that line, or an unknown fixture stops the
run. `context.add_dirs` does not do this: it only grants read access at an absolute host path the
session is never told. No symbolic links anywhere under `evals/`: one breaks the loading of other
cases.

The fixtures, built by `tools/eval_fixtures.py` from the templates of the same export that is
installed:

| Name | What it is |
| --- | --- |
| `home-with-clipping` | a home with two open questions and one markdown clipping, a tool's README |
| `home-with-notes` | a home with two notes, one superseding the other, and an index linking both |
| `researcher-existing` | a folder that already holds a filled researcher's home, `Ada/` |
| `strategy-blueprint-filled` | a ready strategy whose Experiment 1 blueprint is already written |
| `strategy-empty-universe` | a strategy with claims, but a seed that holds only its header |
| `strategy-no-claims` | a strategy as the template ships it, one paper in `Bibliotheca/Papers` |
| `strategy-no-claims-with-home` | `strategy-no-claims` with Ada's filled home in `Ada/` inside it |
| `strategy-ready` | claims, a seed with rows and a note in `Bibliotheca`: ready for a blueprint |
| `strategy-with-home` | `strategy-ready` with Ada's filled home in `Ada/` inside it |

The strategy fixtures without a home test the no-home fallback on purpose — a strategy-side
command run with no home in the session works from the strategy alone and says so — and the ones
with a home test the invited case, where the prompt names the home's path, `./Ada`.

## Replayed turns

An "after the go" case replays the first turn and tests only the second. Its `history.jsonl` is a
Claude Code session transcript, captured from one run of its first-turn case:

1. Run the first-turn case once: `--case '<its name>' --runs 1`. The runner keeps the run's folder.
2. Write the history from the batch's results; `tools/eval_history.py` finds the kept folder from
   the case's `tracePath` (`<kept folder>/out/trace.jsonl`) and its session under
   `config/projects/*/*.jsonl`:

   ```bash
   uv run --no-project python tools/eval_history.py \
     evals/results/<batch>/aggregate-result.json --case contract/blueprint/waits-before-write \
     evals/quality/blueprint/predictions-cite/history.jsonl
   ```

   It keeps only the `user` and `assistant` lines, and writes nothing if what is left holds an
   e-mail address. The unfiltered file carries the account e-mail of whoever ran it and a snapshot
   of the system prompt: never commit it. A kept folder or a session `.jsonl` also works as the
   source, without `--case`.
3. Remove the kept folders, as *Traces* above says, and commit the history with its case.

A case whose `case.yaml` names a `history_file` it does not hold stops the run when it is
selected, naming this procedure.

`quality/blueprint/predictions-cite/history.jsonl` is the first turn of
`contract/blueprint/waits-before-write`. A history is never the second turn of a run: the replay's
workspace holds only what the scaffold put there, so the case judges the blueprint its own run
writes.

The replay's workspace is fresh: give the case the same `FIXTURE`, so the scaffold recreates what
the first turn saw. The history keeps the first run's absolute paths, and the model may notice and
check again. Resuming writes a `<session-id>.jsonl` into the case's folder; that is the run copy
inside `evals/.run/`, which is ignored.

## Reading a failure

Open `evals/results/<run>/report.html`. Each case shows its runs, each run its graders with a pass
or fail chip; a failed grader is open with its explanation, and an `llm` grader shows the judge's
votes and the evidence it read. A case is a **pass** when all three runs pass, a **fail** when none
does, and **flaky** otherwise; flaky is a finding of its own. A run's `error` in
`aggregate-result.json` does not mean it scored 0: it was graded on what it produced.

Rule out a broken eval first: a fixture that is not what the case needs, a grader that checks the
wrong thing. Then read the trace in the run's kept folder. Re-run one case alone with its full
name, `--case 'contract/read/clipping-at-home' --runs 1`.

## Adding a skill

- **Triggering**: a table in `triggering/requests.toml`, with two `fires` requests and one
  `near_miss` whose comment names the skill it belongs to (or `none`).
- **Contract and quality**: a folder per case under `contract/<skill>/` or `quality/<skill>/`, with
  `prompt.md` (its `name` the folder's path), `graders/*.md`, and a `FIXTURE`, `case.yaml` and
  `history.jsonl` when it needs them. A new fixture is a builder in `tools/eval_fixtures.py`, in
  `FIXTURE_NAMES`, with its test.
- Check the assembly with `--dry-run`, then run the new cases once with `--runs 1` before a batch.
