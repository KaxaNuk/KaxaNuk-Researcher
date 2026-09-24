---
description: Draft a strategy's OBJECTIVE.md in place — the main idea and its claims — first from the owner's words before any paper is read, then fine-tuned from the strategy's Bibliotheca notes as reading for each claim comes in; every claim cites a note, RESULTS.md or a FINDINGS file once measured, is true by construction, or names the question that would settle it; plan first, the owner's go, then write. Only when the owner runs it by name, on a strategy they name or are working in.
input:
  - strategy: "Optional: path to the strategy repository, if not the one the session is in"
---

# Draft the objective

Every path below is relative to the researcher's home — the folder that holds `RESEARCHER.md`. Find
it first and read its `RESEARCHER.md` and `AGENTS.md`. In a strategy — the session is open in a
repository with a `Bibliotheca/`, or the owner named one by path — *Working in a strategy* in
`AGENTS.md` says where each of these paths lands. With no home in the session, work from the
strategy alone, with no library contrast, and say so.

`OBJECTIVE.md` is the first thing a CIO reads and the last thing that changes, and A, the first
part of *The order of work* in `AGENTS.md`: **the objective comes before any paper**. This command
runs on the same file in two kinds of pass — the first before anything is read, the fine-tuning
ones as the notes for each claim arrive — so every claim ends up pointing back to a source without
having been written to fit one. `${input:strategy}` is the strategy's path, left out when the
session is open in it.

**Never in the worked example.** When the folder is the worked example — its `README.md` is titled
*Liquid Golden-Cross*, or `README.md` or `AGENTS.md` holds a line reading `<!-- example: begin -->`,
the test `next` uses — say so and stop: the example is for reading and running, never built on; a
strategy of the owner's own is `init-strategy <name>`.

## Step 1: Read the strategy's own material, and name the pass

- `OBJECTIVE.md` as it stands: the slots, and anything the owner already wrote. **The template says
  a person writes this file first.** If nothing in it is theirs yet, ask for the main idea in their
  words before drafting anything; the researcher's part is the claims, the questions that would
  settle them and, later, their sources.
- Every note in `Bibliotheca/Papers/` and `Bibliotheca/Books/`, and `BIBLIOGRAPHY.md` — which
  sources have notes, which claim each serves, and which are only leads.
- `AGENTS.md` in that repository, for the bar any new signal must clear.
- `RESULTS.md`, section *Before any experiment*, for what the analyzer has already measured about a
  claim's column, and, once an experiment has reported, the `FINDINGS_N.md` that moved a claim. A
  claim the analyzer has measured is not an untested one.

**The first pass** is the one where the claims table is empty or no note serves a claim yet: the
claims come from the owner's idea, never from a source. **A fine-tuning pass** is any later one: the
evidence under each claim is rewritten from the notes that serve it, or from `RESULTS.md` and the
findings where it has been measured, and a claim the reading sharpened is proposed as a change for
the owner to take or leave — never changed silently. Once a blueprint is written, a change to a
claim's wording is not fine-tuning but a different strategy or a new experiment; say so rather than
draft it.

## Step 2: Contrast with the researcher's library

Walk `Knowledge/INDEX.md` at home and the links for the domains the strategy touches. Read the
owner's `Philosophy/` on how they invest. Where the home library or a note says something the
strategy's `Bibliotheca/` does not, that is either a lead for `BIBLIOGRAPHY.md` or a warning for the
claim — never a citation, because links stay inside the strategy. In the first pass this is where
the questions come from: what the home library already holds on each claim, and what argues against
it, names what the strategy should read for.

## Step 3: Draft, in the file's own shape

Fill the template's headings — the main idea in one sentence somebody outside the team could repeat;
the objective as a capability, not a number; the claims table, each claim's status taken from the
vocabulary the template's own `OBJECTIVE.md` lists — **untested** for a claim this strategy will
test, **true by construction** for one the rules make true and that earns nothing by itself, and
the rest of that list as the reading and the runs move a claim along; what is not claimed. Never
invent a status word, and never write **untested** over a status the template or the owner already
set. Rules:

- **Every claim cites its evidence**, of one of three kinds, as the template's `OBJECTIVE.md` and
  the worked example use them: a note in the strategy's `Bibliotheca/`, by relative path; once
  something is measured, `RESULTS.md` or the `FINDINGS_N.md` that moved the claim, which a later
  pass leaves standing rather than swapping for a note; or nothing, for a claim that is **true by
  construction**.
  **In the first pass there are none, and that is the order working, not a gap:** each claim's
  evidence is the question that would settle it — *does the effect survive inside the screened
  universe?* — marked as a lead, with the sources worth reading for it named as leads for
  `BIBLIOGRAPHY.md`. A claim that rests only on a home note is written with no link **and marked
  as a lead**: *write the note for X before this claim stands.*
- **Name the columns.** Each claim says which `c_*` or `r_*` column will carry it, if the owner
  already knows; otherwise a slot.
- **Offer each claim its anatomy, never require it.** The reading map, `references/reading-map.md`
  in the `read` skill's folder, gives an idea's anatomy (page 59 of the deck): beside the claim, its
  **source of edge** — which of the five, and why that door is still open; **the other side** — who
  sells, and what keeps them selling; **the test** — the measurement that would settle it, chosen
  before looking; and **the kill switch** — the result that would end the idea rather than send it
  back for tuning. In the first pass, ask them in chat, once for all the claims, as questions the
  owner may answer, skip or refuse; the five sources may be offered as options, and a claim may be
  proposed in the anatomy's shape — one sentence, present tense, about something measurable — for
  them to edit or refuse. What they answer goes in the claim's short section, in their words; what
  they skip is left out, never filled in for them, and is not a gap. In a fine-tuning pass, an
  answer the reading bears on is proposed as a change, as a claim is.
- **Include the source that argues against the idea** if the library holds one — in the first pass
  as a lead to read, in a fine-tuning pass as a note. An objective that cites only agreement is a
  pitch.
- Replace the italic guidance in the body with the draft, and leave the template's blockquote at
  the top: the owner deletes it when they commit, and its absence is their signature.

## Step 4: Show, wait, then write

Show the draft in chat and list the leads it depends on — the questions to read for, the notes to
write with `read` — and the claims the owner should sharpen, with any part of a claim's anatomy
they skipped and may still want to answer. After a first pass, say what comes next
in the order of work: `read` for those questions, then this command again, then the investable
universe. Wait for the go. Then write it into the strategy's `OBJECTIVE.md`, keeping every line the
owner wrote. The owner reviews the diff and commits; that commit is what makes the objective theirs.

Never write into the researcher's home from here. Never compute or promise a number. The objective
is a capability and a set of claims; the numbers arrive later, from the engines the project names.
