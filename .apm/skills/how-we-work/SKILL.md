---
name: how-we-work
description: >
  Load this skill whenever work in a KaxaNuk repository is about to be committed, branched, merged,
  versioned or released. Use it when the user asks where work lands, how to name a branch, what to
  check before a commit, how to write a changelog entry, which version number a change takes, or
  how to publish a release. It covers where work lands (on `main`; an issue, a branch and a pull
  request only when a review is wanted), the `issues/<number>` convention for a branch, the
  checklist before a commit, the changelog format and Semantic Versioning as KaxaNuk applies it.
  It does NOT cover the research process itself (use `experiment-lifecycle`) or Python style (the
  `python-bloom-code` and `python-pep8` instructions).
metadata:
  version: 0.3.0
---

# How we work — issues, branches, changelogs, versions

The same procedure in every KaxaNuk repository, so nobody has to explain it before sharing a tool.
Fewer meetings, more commits with their reasoning attached: a change that carries its changelog
entry is reviewable at any hour; a change proposed in a call is not.

## 1. Work lands on `main`

Work is committed on `main`: small commits whose messages say what moved and why, each
change-set with its `CHANGELOG.md` entry and its version bump. An issue, a branch and a pull
request are tools for a change you want a second pair of eyes on, or for two lines of work that
must not mix — never a gate. Nobody opens an issue to fix a sentence, and a change that carries
its changelog entry has its reasoning with it.

When you do want them:

1. **Open the issue.** State the question or the problem, not the solution.
2. **Cut the branch** from `main`: `git switch -c issues/<number> main`. Use `issues/27-B` and
   `issues/27-C` when one issue needs a second attempt or splits into parallel lines of work — same
   issue, same discussion, separate history.
3. **Work**, committing against the issue. Small commits with messages that say what moved and why.
4. **Open the pull request into `main`**, and delete the branch once it is merged or abandoned:
   `main` is the only branch that stays.

Long-lived branches other than `main` exist only when a repository says so in its `AGENTS.md`
or `README.md` — a product may keep a `dev` branch that is deployed. Never merge into such a
branch by accident: read the repository's own rule first.

## 2. Before any commit to `main`

- **The linter passes.** For Python, `uvx ruff check .`, notebooks included; the repository's own
  configuration decides the rules.
- **Notebook outputs are stripped.** The committed notebook is the method; the record lives in a
  document.
- **The `CHANGELOG.md` entry is part of the change-set**, not a follow-up. If you cannot write the
  entry, the change-set is not finished.
- **No secrets, no binaries.** Nothing from a `.env` file, no keys in a notebook output or a log
  line, no charts, workbooks or PDFs unless the repository explicitly keeps them.
- **If a published number or a public interface moved, the commit message says which** — the pull
  request too, when there is one — and the documents that cite it changed in the same change-set.

## 3. The changelog

One entry per change-set, newest first, in the KaxaNuk Data Curator convention:

```
## X.Y.Z (YYYY-MM-DD)

**One sentence saying what a reader has to do differently.**

### Added
### Changed
### Deprecated
### Fixed
### Removed
```

A repository whose `CHANGELOG.md` names another format in its header keeps it: the KaxaNuk
Researcher's own root `CHANGELOG.md` uses Keep a Changelog, `## [X.Y.Z] - YYYY-MM-DD`. Every
strategy made from the template, and every researcher's home, uses the one above.

Each item is written for somebody who was not in the room: **say what moved and why, not what file
you touched**. "The regime model lives in the Refinery so a penalty sweep costs no download" is an
entry; "updated custom_calculations.py" is a diff. Name anything that invalidates a number or breaks
a caller, and say which. A removal is a change-set too.

## 4. Version numbers

[Semantic Versioning](https://semver.org/spec/v2.0.0.html), read for what the repository's users
actually depend on:

| Repository kind | MAJOR | MINOR | PATCH |
| --- | --- | --- | --- |
| **A library** (public API) | a caller has to change code | new capability, callers untouched | a fix; nothing observable changes except the bug |
| **A research repository** (results and the pipeline) | published results are invalidated and must be re-derived | a new experiment, signal, stage or document; existing results stand | tooling, documentation, hygiene; no result changes |
| **An APM package** (AI primitives) | a skill's contract or a file name changes so a consumer must re-read | a new skill, prompt or instruction | wording, references, fixes with the same contract |

Three conventions follow: a result or contract that changes is MAJOR even if the diff was one line —
severity is what a reader has to throw away, not the size of the diff; re-running a pipeline on
refreshed data is not a bump; while on `0.x`, a breaking change bumps MINOR, and `1.0.0` is reserved
for the first version somebody outside the team depends on — for a research repository, the first
strategy that reaches paper trading with its results reproduced from a clean clone.

## 5. Releasing

1. Bump the version where the repository keeps it — `pyproject.toml`, `apm.yml`, or both — in the
   same commit as the changelog entry, and run `uv lock` where the repository commits a `uv.lock`,
   so the lock records the new version too.
2. Tag on `main` once the version's commit is there, and push the tag:

   ```bash
   git tag -a vX.Y.Z -m "X.Y.Z"
   git push origin vX.Y.Z
   ```

   One tag per release, `v` and the version the repository declares at its root: a strategy tags
   the version its `apm.yml` and `pyproject.toml` share, and the KaxaNuk Researcher tags its
   package's, while its template, example and home keep their own numbers in their folders.
3. **Tag the commit where the version became the state of `main`** — when a branch was used, the
   merge, not the commit on the branch that wrote the bump. A version bump authored early on a long
   branch names a tree that never existed on `main`, and a tag is the one thing that cannot be
   corrected in place once somebody has pinned to it.
4. For a package published to an index, the release job builds from the tag, never from a working
   copy.

## 6. Two things never to do

- **Never rewrite pushed history on a shared branch.** Fix forward with a new commit; the exception
  is a branch only you have ever pushed.
- **Never print a secret to find out whether it is set.** Check for its presence, report *set* or
  *missing*, and stop there. An exposed key is rotated, not edited out of a file.
