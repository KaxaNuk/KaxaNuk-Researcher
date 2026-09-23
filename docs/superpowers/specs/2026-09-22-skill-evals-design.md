# Evals for the KaxaNuk Researcher's skills and commands

Date: 2026-09-22. Base: `main` at `ba4b9d6` (package 0.10.0). This document stays out of the
repository: the package installs whole, so its content goes into the pull request description.

## Goal

The package's product is prose: fifteen skills in `.apm/skills/` and ten commands in
`.apm/prompts/`. Its tests cover the scripts only. This work adds behavioural evals, runs them,
diagnoses every flaw they find, fixes the skills, and ships evals, findings, fixes and the before
and after results in one pull request into `main`, with Arturo Aguilar (`Arturo-Aguilar-KN`)
requested as reviewer. The findings are written so that his agent can read, verify and act on
them, not only him.

## Scope

- **Triggering**: all 15 skills. Commands are invoked by name, never chosen by description, so
  they have no triggering layer.
- **Contract and quality**: a pilot of six — the skills `read`, `query`, `init-strategy`,
  `init-example`, `init-researcher`, and the command `blueprint`.
- **Out of scope**, named in the pull request: the seven Investment Lab skills beyond triggering
  (their real behaviour needs licensed engines), the other nine commands, Codex and Cursor (the
  harness is Claude only), and CI, which upstream removed on purpose. Each later skill is one more
  folder of cases, added the same way.

## The harness

`claude plugin eval`, built into Claude Code (2.1.268 on the development machine). A case is a
folder with `prompt.md` (frontmatter: `runs`, `max_turns`, `timeout_seconds`, `model`,
`allowed_tools`, ...; body: the request) and `graders/*.md`, optionally `case.yaml` for
`context.scaffold_script`, `context.history_file` (a replayed first turn) and `context.add_dirs`.
Graders used: `tool_used` (including `Skill` with an `input_match` on the skill name, and
`min`/`max` counts to assert a tool was not called), `tool_order`, `file_exists`, `regex` over the
transcript, and `llm` (a judge with a two-of-three vote). Each run gets a throwaway workspace with
a fresh home.

**Step zero** — before anything is built on it — checks, in throwaway runs: that the harness
accepts an installed skills folder as its target, commands included; that a replayed history
drives a second turn; and what one case of each layer draws, as the harness's estimated cost. If
the installed folder is refused, the fallback is a plugin folder generated from the same install,
with a minimal manifest. Nothing else in this design changes either way.

## The install under test

`tools/build_eval_install.py` runs the real `apm install -g <repository> --target claude` with
the home folder pointed at `evals/.install/` (gitignored), producing exactly the skills and
commands a user receives. It is rebuilt before every eval run, so the evals test the current text.
It has unit tests and passes the Bloom Code check, like the other tools.

## Layout

```
evals/
  triggering/<skill>/<case>/     requests that should fire the skill, and near-misses that must not
  contract/<skill>/<case>/       hard gates, graded without a judge
  quality/<skill>/<case>/        output judged against written criteria
  fixtures/                      small starting folders, and the setup scripts that build them
  findings/<date>-pilot.md       the diagnosis, one block per flaw
  results/                       gitignored: transcripts and reports
  README.md                      how to run, what each layer checks, how to read a failure
```

`evals/` ships inside the package, as `tests/` and `tools/` already do; it is small text only.
**No binaries** (`AGENTS.md`): the `read` cases build their PDF at setup with the builder the
`extract.py` tests already use. **Fixtures follow the template**: the strategy fixtures are made at
setup by `scaffold.py` from the current template, plus small edits (claims added, a seed with
rows), never a frozen copy.

## The cases

**Triggering (about 45).** Per skill, two requests that should fire it and one near-miss that
must not — "what does my library say about momentum?" fires `query`; "summarise this PDF I dropped
in" fires `read`, not `query`. Grader: which skill the session called. `max_turns: 2`.

**Contract (about 30)**, graded by tools, files and text only:

| Surface | Gates |
| --- | --- |
| `read` | plan shown and waited on, nothing written before the go; `extract.py` runs before a table of contents is shown; refuses in a strategy with no claims; a PDF with no text layer is reported unreadable, with no note; after the go, only the chosen chapters are written, the log is appended, and `Philosophy/` is untouched |
| `query` | every answer links notes; a question the library cannot answer is named as a gap, with no invented source or URL; nothing is written |
| `blueprint` | refuses, naming the item that comes first, when `OBJECTIVE.md` has no claims, the universe is empty, or the blueprint is already filled; otherwise drafts and waits, nothing written before the go |
| `init-strategy` | nothing runs before the go; after it, `scaffold.py` copies and no template file is written by the model; a folder that is not empty is refused, not worked around; with no git identity (the fresh home has none) the name and email are asked for, never invented |
| `init-example` | plan, then go; a file already present is never overwritten |
| `init-researcher` | stops and says where when a home already exists; otherwise plan, go, script |

"After the go" cases replay the first turn from a history file, so the second turn is tested
alone.

**Quality (about 8)**, judged:

- `read`: the note follows `references/note.md` and claims nothing absent from the extract.
- `query`: every claim traces to a cited note; a contradiction is reported with the newer claim.
- `blueprint`: every prediction cites a note or an analyzer section, or is marked a lead.
- `init-*`: the hand-over names a new session and the right next step.

**Pass rule.** Three runs per case. A case passes when all three pass; one or two out of three is
**flaky**, a finding of its own, because instructions that are followed inconsistently are a flaw.

## Models

Sessions run on **Opus 5.5** (`claude-opus-5-5`), pinned with `--model`. The quality judge is
**Fable 5.1** (`claude-fable-5-1`), pinned with `--judge-model`. The report records both.

## Plan usage

The development machine runs Claude on a Max subscription, with no API key: the evals draw on the
plan's usage limits, not a bill. Step zero reports each layer's estimated cost; from it, batch
sizes are proposed and approved before running, each batch with `--max-cost-usd` as a brake. The
no-plugin comparison arm is off (`--ablation none`): it halves usage, and without skills nothing
can fire.

## Workflow

1. **Baseline.** Run everything on today's text, in the approved batches: pass, fail or flaky per
   case.
2. **Diagnose, eval first.** For each failure, rule out a broken eval — a bad fixture, a grader
   too strict, an ambiguous request. A broken eval is fixed and re-run, never reported as a flaw.
   A real flaw is traced to the instruction behind it, file and line, with one root cause:
   *ambiguous* (two readings), *contradiction* (two documents disagree), *missing rule* (the case
   is not covered), *misfire* (a description overlaps another skill's).
3. **Fix.** The smallest text change that closes the flaw, one commit per finding, so each can be
   taken or dropped alone. After each, re-run the failing case and the skill's whole set; after
   any description change, the whole triggering layer. Where the right behaviour is a product
   decision rather than a text bug, no fix: a proposal, marked as needing the maintainer's call.
4. **After.** The whole suite again, so every case has a before and an after.
5. **The pull request.** From a branch off `main`, reviewer `Arturo-Aguilar-KN`. Package: minor
   bump (a new capability); each fixed skill bumps its own `metadata.version`; changelog entries
   per `AGENTS.md`. Opened only after the owner has read the findings.

## The findings file

`evals/findings/<date>-pilot.md`, one block per flaw, in the same shape every time:

```
### F-NN  <one-line statement of the flaw>
- skill / layer / case: `read` / contract / `read/no-write-before-go`
- before: fail 0/3   after: pass 3/3
- root cause: ambiguous — `.apm/skills/read/SKILL.md:36`
- evidence: "<short transcript quote>"
- fix: <commit> — <one sentence>        (or: proposal — needs your call, with the options)
- verify: claude plugin eval evals/.install/... --case 'contract/read/no-write-before-go'
```

It opens with the summary table — cases per layer, pass, fail, flaky, before and after — and
ends with the exact commands to rebuild the install and re-run any case. The pull request
description summarises it and adds a section addressed to the reviewer's agent: where the findings
live, how to verify each fix, and which proposals need a decision.

## Definition of done

- Step zero passed, or its fallback adopted and noted.
- Every case in the catalogue exists and runs; the baseline and after results are recorded.
- Every failure is diagnosed as a broken eval (fixed) or a flaw (fixed or proposed).
- The repository's checks pass: tests, ruff (root and example), `check_repo.py`, Bloom Code.
- The pull request is open with the reviewer requested, after the owner has read the findings.
