# Probe notes: `claude plugin eval` for the KaxaNuk Researcher skills

Date: 2026-09-22. Machine: Windows 11, Git Bash, Claude Code 2.1.268, apm-cli 0.31.0, Max
subscription (no API key).

**Status: BLOCKED on every eval run.** Zero eval runs were made; zero cost was spent. The format
facts below come from the official documentation (downloaded verbatim to
`probe/plugin-evals.md` from https://code.claude.com/docs/en/plugin-evals.md), not from a template
the CLI wrote, and none of them has been exercised by a real run yet. Everything marked
"verified" was observed on this machine; everything marked "documented" was read in the doc;
"assumed" means neither.

## 0. The blocker

```
$ claude plugin eval init --bare probe-case
`plugin eval` is currently in early access          (exit 1, nothing written)
$ claude plugin eval . --no-publish --runs 1 --ablation none --max-cost-usd 1
`plugin eval` is currently in early access          (exit 1)
```

- Verified: `claude plugin eval --help` and `claude plugin eval init --help` print (so the command
  exists in 2.1.268), but every action, including `init --bare`, exits 1 with that message.
- Documented (Requirements, and Troubleshooting "plugin eval is currently in early access"):
  the command needs **Claude Code v2.1.269 or later**; "Your build predates general availability
  of the command. Run `claude update`, then run the command again in a fresh session."
- Verified: the 2.1.268 `--help` lacks options the doc lists (`--trust-plugin`, `-j/--concurrency`,
  `--allow-real-servers`), which fits the doc describing a newer build.
- Not done: I did not run `claude update` (it changes the CLI the calling session runs on; the
  owner's call), and I did not use any other way around the gate.

## 1. Case format (documented; `init --bare` could not run)

Layout. A case is a directory under the plugin's eval dir (`evals/` unless `--eval-dir` or
`plugin.json` `"experimental": {"evals": "<rel/dir>"}`) holding `prompt.md`, `case.yaml`, or
both. Nest non-case directories to group cases. Anything inside a case directory (graders,
fixtures, transcripts) belongs to that case. Results go to `<eval dir>/results/<timestamp>/`
(`aggregate-result.json`, `report.html`). The run cannot read the eval directory, so fixtures are
reachable only through `context.add_dirs` or a scaffold.

`init --bare <name>` (documented) writes `evals/<name>/prompt.md` (placeholder body, frontmatter
`max_turns: 10`, `allowed_tools: [Read, Glob, Grep, Skill]`) and `evals/<name>/graders/criteria.md`
(`type: llm`, placeholder PASS/FAIL body). It writes no `case.yaml`.

### prompt.md frontmatter (an unknown key is an error)

| key | default | note |
| --- | --- | --- |
| `schema_version` | `"1.1"`, set for you | |
| `name` | the directory name | `--case` globs match it. Assumed: a `/` in the name is accepted |
| `description`, `expected_outcome` | | humans only |
| `tags` | `[]` | `--tag` filter, any-match |
| `plugins` | nearest enclosing plugin | dirs relative to the case dir, e.g. `["../.."]` |
| `runs` | `3` | 1..50, `--runs` overrides |
| `model` | child default | `--model` overrides |
| `max_turns` | `10` | up to 200; hitting it is a run error |
| `timeout_seconds` | `300` | up to 3600 |
| `allowed_tools` | `[]` | read-only set granted when listed: Read, Glob, Grep, NotebookRead, Skill, Agent, TodoWrite, Task* |
| `append_system_prompt` | | |
| `env` | `{}` | keys must match `EVAL_[A-Z0-9_]*` |

Body = the prompt, verbatim. `@path` mentions are not expanded.

### Grader files `graders/<name>.md` (name = filename without `.md`)

Common keys: `type` (required), `weight` (default 1), `arm` (`with-only` | `both`). Body is a
one-line purpose for non-llm graders, and **the rubric** for `llm`.

| type | keys | passes when |
| --- | --- | --- |
| `regex` | `pattern`, `flags`, `match`, `target` | JS regex found in target. `match`: `contains` (default) / `not_contains` / `"count:N"` |
| `tool_used` | `tool`, `input_match`, `min` (1), `max` (unbounded) | count of calls to `tool` whose JSON input matches `input_match` is in [min, max]; never called = `min: 0, max: 0` |
| `tool_order` | `before`, `after` (tool name or `{tool, input_match}`) | first `before` precedes first `after` |
| `file_exists` | `path` (glob), `exists` (true) | a file **created** during the run matches |
| `llm` | `criteria` (= body in .md), `focus` | judge votes PASS in 2 of 3 |
| `baseline` | `baseline_file` (.jsonl in case dir), `criteria` | judge finds run at least as good as reference |

`target` / `focus` values: `last_message` (default), `trace` (JSON per line; quotes appear as
`\"`; an llm judge sees first 12 + last 12 messages), `files` (created paths only),
`{source: file, path: <p>}` (file contents), `mock_calls`.

Two-arm rule: under `with-without`, every `tool_used` grader with `tool: Skill`, and every
`arm: with-only` grader, is excluded from the score (`scored: false`) unless all graders in the
case are such; under `--ablation none` nothing is excluded.

### case.yaml

Requires `schema_version: "1.1"` **and `name`**. Top level: `description`, `tags`, `plugins`,
`runs`, `expected_outcome`, `graders` (list, each with `name` + grader keys; llm rubric in
`criteria`). Under `execution:`: `model`, `max_turns`, `timeout_seconds`, `allowed_tools`,
`append_system_prompt`, `env`, `prompt`. Under `context:`: `scaffold_script` (bash in the case
dir, runs only with `--scaffold`), `history_file` (`.jsonl` in the case dir; the prompt becomes the
next user turn), `add_dirs` (**directories inside the case directory**, read-only). When both
files exist, `prompt.md` frontmatter wins on shared fields and its body is the prompt.

### Differences from the plan's assumed syntax

1. regex uses **`target`**, not `source`.
2. Inline `(?i)` is **not supported**; write `flags: i`. The plan's step-4 grader `(?i)objective`
   would have failed or matched literally.
3. `case.yaml` needs **`name`** as well as `schema_version`.
4. `context.add_dirs` paths are **inside the case directory**; a plugin-level
   `fixtures/probe-home` is out of reach. Suite-wide fixtures must be copied (or symlinked,
   assumed) into each case, or created by a scaffold.
5. Grader body is a purpose line only for non-llm types; for `llm` it is the rubric itself.
6. `--judge-model` default is "a small fast model" (help text: haiku).
7. With `--json` (or no terminal) a first run against an untrusted directory is **refused with
   exit 1** unless `--trust-plugin` is passed or the directory was trusted interactively once.
   `--trust-plugin` does not exist in 2.1.268.
8. Every run starts in an **empty workspace with a throwaway home**: no user `CLAUDE.md`, rules,
   memory or other skills; the Artifact tool is off. The package's four instructions
   (`~/.claude/rules/*.md` after install) are not part of a plugin, so they will **not** load in
   eval runs.
9. Granting `Bash`/`PowerShell` on **native Windows refuses every run** (no sandbox backend); such
   suites need WSL2. Write/Edit grants are fine. Contract cases that need a shell (scaffold.py,
   extract.py) cannot run on this machine as-is.

## 2. Install into a throwaway home (verified)

The command as planned **fails**:

```
HOME=$P/home USERPROFILE=$P/home uvx --from apm-cli apm install -g C:/Proyectos/KaxaNuk-Researcher --target claude
  [x] ... Failed to download dependency _local/KaxaNuk-Researcher: [WinError 3] The system cannot
      find the path specified: '...\home\.apm\apm_modules\.apm-resolution-staging\<32 hex>\replacements\<64 hex>'
```

Same with `-v`. Cause (traceback via instrumented run): apm copies a local package file by file
into `<HOME>\.apm\apm_modules\.apm-resolution-staging\<32hex>\replacements\<64hex>\` (about 150
characters after HOME) and `shutil.copy2` hits the 260-character Windows path limit
(`LongPathsEnabled` = 0 on this machine). The repository's longest path is 122 characters
(`examples/liquid-golden-cross/Bibliotheca/Books/...`), so a local install of the whole repo cannot
fit under any HOME without long paths. `.apm/` alone tops out at 75 characters.

What worked: copy only `apm.yml` + `.apm/` (no `__pycache__`) to a temp folder and install with a
**short HOME** (`<home>/kx`, since removed). Result, now copied to `probe/home/.claude/`:

```
.claude/commands/  audit.md blueprint.md brainstorm.md challenge.md objective.md refine.md
                   refresh-index.md researcher-init.md teach.md update.md          (10)
.claude/rules/     filesystem-boundaries.md python-bloom-code.md python-pep8.md
                   python-test-writing.md                                          (4)
.claude/skills/    alpha-decomposition attribution-analysis-runs backtest-engine-runs
                   bloom-code-lint data-curator-custom-calculations experiment-lifecycle
                   how-we-work init-example init-researcher init-strategy
                   portfolio-construction-runs query read universe-point-in-time   (14)
```

Consequences for later tasks: build the eval plugin from a stripped copy at a short path (or from
`.apm/` directly), never by installing the full repo locally on this machine. Assumed, not tested:
the GitHub install (`apm install -g KaxaNuk/KaxaNuk-Researcher`) goes through a different path and
may not hit this, and the stripped install lacks `templates/` and `examples/`, which the `init-*`
skills copy from the package, so those skills' contract cases need the full package.

Installed `blueprint.md`, first 20 lines:

```
---
argument-hint: <strategy> <experiment>
arguments:
- strategy
- experiment
description: Draft BLUEPRINT_N.md in place for a strategy, once its objective has
  claims and its investable universe exists — thesis, rules, predictions — with every
  prediction citing a Bibliotheca note or an analyzer measurement; plan first, the
  owner's go, then write, before the rule. Only when the owner runs it by name, on
  a strategy they name or are working in.
---

# Draft a blueprint

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`. In a strategy — the session is open in a
repository with a `Bibliotheca/`, or the owner named one by path — *Working in a strategy* in
`AGENTS.md` says where each of these paths lands.

The blueprint is the hypothesis, fixed once written, recorded before the notebook's rule cell
```

Rendering: apm turned the prompt's `input:` list into `arguments: [strategy, experiment]` plus
`argument-hint`, and `${input:experiment}` / `${input:strategy}` into `$experiment` / `$strategy`.

**Finding (documented behaviour, not run):** Claude Code binds named arguments by position
("with `arguments: [issue, branch]` the placeholder `$issue` expands to the first argument"; a
named placeholder with no argument expands to an empty string). So **`/blueprint 1` sets
`$strategy` = `1` and `$experiment` = empty**. The same holds for `challenge` and `brainstorm`
(`<strategy> <experiment> [<idea>]`); `objective` takes only `<strategy>`. The optional argument
comes first in these three commands. Contract cases must either type `/blueprint . 1` or expect
the model to recover from the text, and the command order may deserve its own issue.

## 3-7. Probe plugin and cases (built, not run)

`probe/run/` holds the plugin and the five probe cases in the documented format;
`claude plugin validate .` passes there (verified; two warnings: no description, no author).

```
run/.claude-plugin/plugin.json      {"name": "kaxanuk-researcher-evals", "version": "0.0.0"}
run/skills/ run/commands/           copied from probe/home/.claude/
run/evals/triggering/query/fires-1/ prompt.md + graders/fired.md (tool_used Skill, query)
run/evals/contract/blueprint/probe/ prompt.md (/blueprint 1) + graders/mentions-objective.md
                                    (regex, target last_message, pattern objective, flags i)
run/evals/probe/fixture/            case.yaml (name, context.add_dirs: [probe-home]),
                                    probe-home/hello.md, prompt.md, graders/word.md
run/evals/probe/judge/              prompt.md + graders/names-a-file.md (type llm, body = rubric)
```

Not built: the replay case (step 6). It needs a real first-turn transcript from a run's
`--keep-temp` directory or JSON; the doc gives no line schema beyond ".jsonl transcript".

What each step still has to establish once the command works:

| step | question | status |
| --- | --- | --- |
| 3 | plugin-folder target accepted; triggering pass/fail; cost; wall time | not run |
| 4 | `/blueprint 1` resolves in `claude -p` (plugin commands are namespaced `kaxanuk-researcher-evals:blueprint`; whether the bare name resolves is assumed) | not run |
| 5 | add_dirs mount path as seen by the session (cwd stays the empty workspace, per doc) | not run |
| 6 | history_file line format; continuation | not run |
| 7 | judge verdict format; extra cost | not run |

Commands to run once enabled (from `probe/run`, add `--trust-plugin` if the version has it, or
run once in a terminal to answer the trust prompt):

```
claude plugin eval . --case 'triggering/query/*' --model claude-opus-5-5 --ablation none --no-publish --runs 1 --max-cost-usd 1 --json ../trig.json
claude plugin eval . --case 'contract/blueprint/*' ... --json ../contract.json
claude plugin eval . --case 'probe/fixture' ...   --json ../fixture.json
claude plugin eval . --case 'probe/judge' --judge-model claude-fable-5-1 ... --json ../judge.json
```

## 8. Usage summary

**No measured figures exist**: no eval run was possible. The only number in the doc is an
illustrative example (one case, 6 runs, $0.41), which is not a measurement on these skills and
should not be used for planning.

The cost model the doc states, for use once step 3-7 figures exist (`c_*` = measured
`costUsd` per single run):

- per suite: cases x runs agent runs (x2 under `with-without`), plus 3 judge calls per `llm` or
  `baseline` grader per run;
- full suite at 3 runs, `--ablation none`:
  `3 x (42 c_trig + 21 c_contract + 7 (c_quality + c_judge))`, and twice the agent part under
  `with-without`;
- proposed batching (unchanged from the plan, ceilings to fill in as estimate x 1.5, rounded up):
  triggering in two batches of 21 cases, contract one batch per command/skill surface, quality in
  one batch with the judge.

`--max-cost-usd` caps the list-price estimate, not plan usage; on a Max plan the real limit is
the plan's usage window, and a run that hits it scores 0 without the suite being marked partial
(documented), so check `cases[].arms.with[].error` before trusting any score.
