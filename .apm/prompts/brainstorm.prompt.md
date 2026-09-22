---
description: Draft a dated entry for a strategy's BRAINSTORMING_N.md — the next thing to try, considered against the library — and append it there on the owner's go. Only when the owner runs it by name, on a strategy they name or are working in.
input:
  - strategy: "Optional: path to the strategy repository, if not the one the session is in"
  - experiment: "The experiment number N"
  - idea: "Optional: the idea to think about, in a phrase"
---

# Draft a brainstorming entry

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`. In a strategy — the session is open in a
repository with a `Bibliotheca/`, or the owner named one by path — *Working in a strategy* in
`AGENTS.md` says where each of these paths lands.

Brainstorming is forward-looking planning, done before the work, and never mistaken for the record
of what happened. `${input:experiment}` is the experiment number `N`, `${input:idea}` the idea to
think about when the owner gave one, and `${input:strategy}` the strategy's path when the session is
not already open in it.

1. **Read the experiment's state.** When `BRAINSTORMING_N.md` is missing, never write it from
   memory. For N > 1 the template never ships it: the blank is the `experiment-lifecycle` skill's
   `references/brainstorming-template.md`, copied to `Experiments/Experiment_N/BRAINSTORMING_N.md`
   with `N` replaced, as that skill's section 6 says; offer the copy, make it on the owner's go,
   and continue. For Experiment 1 — a strategy made by `init-strategy` before template 0.11.0,
   which shipped no experiment documents — give the command that restores the file from the
   template, run in the strategy's root — the script is in the `init-strategy` skill's folder:

   ```bash
   uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" \
     strategy . --only Experiments/Experiment_1/BRAINSTORMING_1.md
   ```

   Say that it copies the template's description, with nothing of the example's to delete, and
   stop.

   Otherwise read `BLUEPRINT_N.md`, `BRAINSTORMING_N.md` (the entries so far), `FINDINGS_N.md` if
   it reports, and `RESULTS.md` — what is closed, what is open, what stands. Do not open another
   experiment's files unless the owner has recorded the request and reason in `JOURNAL_N.md`.
2. **Contrast with the library and the owner's voice.** What has the strategy noted and read in
   its `Bibliotheca/` that bears on the idea, what has the owner read at home, and what does their
   `Philosophy/` say about it? What argues against it? Is there a simpler rival — the cheap version
   of the idea that the complicated one has to beat?
3. **Draft one entry** in the template's format — *Idea / question*, *What we tried / considered*,
   *Outcome / decision*, *Open threads* — dated today. Every source named is a link to a note in
   the strategy's `Bibliotheca/`; a source without a note is a lead, and a home note is named in
   prose, never linked.
4. **Show, wait, then append.** Show the entry in chat and wait for the go. Then append it to the
   strategy's `BRAINSTORMING_N.md`, newest at the bottom, touching nothing above it. The owner
   reviews the diff and commits.

Never write into the researcher's home from here. Remind the owner, once, of the rule the file's own
header states: once the blueprint is written, an idea committed to leaves this file for a new
experiment and is not edited into the current one. Before that — the benchmark choice in
`BRAINSTORMING_1.md` is the usual case — an entry feeds the blueprint that has not been written yet,
which is the file working as intended, not an exception.
