---
name: philosophy
description: >
  Interview the owner about how they invest — why, what they believe, then questions at their
  level, one idea taught after each — and add their typed answers, word for word, to
  Philosophy/HOW-I-INVEST.md, with a round file in Philosophy/Evolution/; retaken after reading, it
  shows how their view moved. Plan first, the owner's go, then write, at home only. Only when the
  owner runs it by name, or picks it where another skill offers a round. It does NOT edit what
  HOW-I-INVEST.md holds (`refine` does) or write RESEARCHER.md beyond Find first, and never says
  what to buy, sell or hold.
metadata:
  version: 1.1.0
---

# Philosophy — the owner's view, in their own words, round by round

**When it applies.** The owner runs `philosophy` by name, or picks it where another skill offers a
round — `interview`'s hand-over, `read`'s report, `next`'s closing line, the close of a `teach`
lesson. It asks about the owner and their own money: why they invest, what they believe, how they
decide, what would change their mind. Nothing here is about a strategy: a question on a yardstick,
a stop or how long to hold asks about the owner's own habit, never a strategy's rule, which
`objective` and `blueprint` ask later, in a strategy. It is not a test — no score, no quiz, no
wrong answer — and it never tells the owner what to buy, sell or hold, never names a product or a
ticker, never proposes an allocation or a benchmark, and never computes a return. For what the
library says, use `query`; for a lesson on an idea, `teach`.

**What it writes, and only on the owner's go.** The owner's typed answers, added to
`HOW-I-INVEST.md` word for word and add-only, and one round file in `Philosophy/Evolution/`: this
skill and `refine` are `Philosophy/`'s two writers, as the home's `AGENTS.md` says. Beyond
`Philosophy/`, the works the owner picks at the close of a round go on the closing *Find first*
line of `RESEARCHER.md`, add-only, unless they leave that line alone in the preview. Nothing else,
anywhere. The same go saves a version of what it wrote.

**Only typed words reach `Philosophy/`.** Nothing the owner picks — a hunch, a stance, a level, an
example, a work — is written there: this is stricter than the rule for other proposals, where a
pick the owner makes is theirs. After a pick comes one optional line, *in your own words?*, and
only what they type is written. No line the researcher says — a question, a placement, a teaching
line, a pick's label, a reading list — goes into `Philosophy/`, round files included. A round file
is a record, read for dates and levels; the owner's view is cited from `HOW-I-INVEST.md`, never
from a round file, as the home's `AGENTS.md` says.

**The bank.** [`references/questions.md`](references/questions.md), in this skill's folder: the
explainers, every question by level with its plain line, examples and the one idea it teaches,
where each typed answer lands, how a retake runs, and which works bear on which question. Read it
whole before the first question. It is written in English and said in the owner's language — the
one *How it speaks* names — line by line as written, translated and never improvised. IDs are
stable and never renumbered; a retake compares by ID.

**The reading map.** Every work named comes from `references/reading-map.md` in the `read`
skill's folder, or from the owner's own `Sources/` and `Knowledge/`, with its year, authors, title
and page as the map gives them — never from memory. A work is a lead, never a source: a paper's
finding is said as the map sums it up, as a lead to read.

**How to ask.** Open questions are asked in chat, one per message, because only typed words reach
the file; at Building and Researching the owner may ask for a whole block in one message. A pick
is asked by **calling the question tool** — `AskUserQuestion` in Claude Code — its options at most
four, with *Other*, which the tool always offers, as the free-text escape; call the tool, never
type a pick and its options as chat. **Without one** — Codex, Gemini — a pick is asked in chat, as
the home's `AGENTS.md` says, *Other — your own words* last. Every header is the one the bank gives
for that language, the English one for any other, twelve characters at most. Wait for each answer.

**A round at a glance.** About 10, 20 or 30 minutes by level, and it can stop after any block.

| # | Step | How |
| --- | --- | --- |
| 1 | pre-flight: the home, what the owner has said and read, the level to suggest | nothing asked |
| 2 | welcome, or a retake's opening and its scope | said, then one tool question |
| 3 | why you invest (O1), what you already believe (O2) | chat |
| 4 | how much you know (O3) | one tool question |
| 5 | where the belief sits, and the idea the rest builds on | said, never asked |
| 6–7 | the level's blocks, a checkpoint after each | chat; picks and checkpoints by tool |
| 8 | what would change your mind (C1), what to read next (C2) | chat, then one tool question |
| 9 | on a retake, then and now | chat, never written |
| 10 | the preview, and the go | said, then one tool question |
| 11 | write | on the go only |
| 12 | hand over | said |

## 1. Pre-flight, asking nothing

1. **Find the home**, the folder that holds `RESEARCHER.md`; every path below is relative to it.
   Handed over by `interview` in the same conversation, with the session open elsewhere, it is the
   home's absolute path `interview` names. In a strategy or another project, find it through the
   researcher's skill, whose description names the home by path; the preview will open with *this
   writes to the researcher's home, not to this project*. If the home cannot be read from this
   session, say so, name the fix — add the home's folder to the session, or open the assistant
   there — and stop.
2. **Read `RESEARCHER.md` and `AGENTS.md`.**
   - A `RESEARCHER.md` with an angle-bracketed slot left under *Who* or *How it speaks* has not
     been interviewed: say so, offer `interview`, and stop.
   - An `AGENTS.md` whose `Philosophy/` row does not name `philosophy` among its writers predates
     this skill, and the home's own rules do not let it write: say so, offer `update`, which shows
     the new row as a diff to accept, and stop.
   - Take the language and the voice from *How it speaks* — with none, the language of this
     conversation — and the *Here for:* line under *Who*, whose picks `interview` writes in
     English.
3. **Read what the owner has already said.** `Philosophy/HOW-I-INVEST.md`, whole: its headings —
   the template's, translated ones, or none — and every line. Then `Philosophy/Evolution/`. With
   no round file in it, or no folder, this is round 1. Otherwise it is a retake: the latest round
   is the newest file — the latest date in the file names, and on that date the highest suffix,
   `YYYY-MM-DD-2.md` — and its first line gives its number *N*, so this round is *N* + 1; a file
   deleted or renamed by hand leaves no gap to fill, because *N* is read, never counted. From the
   round files, gather each ID's latest typed answer and its round, and its latest status; and
   the questions the last round's level asks, section 3 of the bank, that no round file has a
   line for — O3 and C2 aside, since neither ever takes a line — which a round stopped early
   never reached: they are open, as a skip is.
   A file there whose first line is not a round line is no round: ignore it, and name it once.
4. **Read what the owner has read.** `Knowledge/INDEX.md` end to end; on a retake, also the `read`
   entries of `Knowledge/LOG.md` dated on or after the last round's date — a read the same day
   counts — and the notes they list as written.
5. **Find the reading map**, `references/reading-map.md` in the `read` skill's folder: under
   `~/.claude/skills/read/` or the user's folder for the agent in use, or in the package under
   `~/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/skills/read/`. Match its works against the
   file names under `Sources/` and the notes in `Knowledge/INDEX.md`, as its *Match before
   proposing* says: a work with a note is *read*, never offered as one to find, and named by a
   link to the note; a file with no note is *in your Sources/, not yet read*; a *possibly in your
   Sources/* match is offered as a work to find, saying so.
   **Without the map**, ask the plain questions only, as section 9 of the bank says: no work is
   named anywhere, and no line is placed. Say why in one line — the map comes with the `read`
   skill, which is not installed here — and give the fix,
   `uvx --from apm-cli==0.33.0 apm install -g KaxaNuk/KaxaNuk-Researcher --target <agent>`, then a
   new session. Never write the map, or a work from it, from memory.
6. **Work out, for later**: the level to suggest (*step 4*); on a retake, the last round's level,
   its reading list and the notes read since; and which *Behind it* works have a note, so a
   question can rise a level (*step 6*). **A round's reading list** is the *Behind it* works of the
   questions it asked, at its level, as the bank gives them: derived from its IDs and level, never
   stored.

## 2. Welcome

**Round 1.** Say section 0 of the bank, then ask `Ready?` (`¿Comenzamos?`) — *Start*, *Not now*.
Handed over by `interview`'s `Philosophy?` *Now*, that pick was the start: say section 0 and go
straight to O1. `Ready?` is asked only when the owner ran `philosophy` by name.
**A retake.** Say the opening of the bank's section 7 instead, then ask its scope question,
`Retake?` (`¿Repetir?`); *not now* or *stop* under *Other* is *Not now*. The scope is applied
after O3, against the questions of the level chosen there: a question that level does not ask is
left out, whatever the bank's section 8 lists — Q5, S2 and S3 are never asked below Researching.

On *Not now*, write nothing, and say in one line how to start later: *say `philosophy` whenever
you like — a new session is best.*

## 3. The opening: why you invest, and what you already believe

The same at every level, in plain words, in chat: **O1**, then **O2**, one per message. When
nothing comes for O2 — *not sure yet*, or *example* — show the `Hunches` pick once, as section 1
of the bank gives it: three hunches and *More hunches*, then the other four; in chat, one
numbered list of all seven. Picking none keeps *not sure yet*, a complete answer. After a pick,
ask *want to say that belief in your own words — and why, if you like? One line, or skip* — only
that line is written, never the hunch; it is the O2 line C1 quotes. The belief is placed in
*step 5*, once the level is known.

## 4. How much you know

**O3**, one tool question, `Experience` (`Experiencia`), as section 1 of the bank gives it. One
option is marked *(suggested)* — never picked for the owner — by the first rule that applies:

- **Round 1.** *How it speaks* names the voice *Explain as you go*, in whatever language it is
  written, or *Here for* holds *Learn the basics*: *Just starting*. Otherwise, three or more of
  the map's *Start here* papers have a note: *I research*. Otherwise no option is marked.
- **A retake.** The last round's level is marked *(current)*. The level one above it is marked
  *(suggested)* when two works from the last round's reading list now have notes — never more
  than one level up, never past Researching; otherwise *(current)* is the suggestion.

*Not sure — help me place myself* opens the calibration, `Which fits?` (`¿Cuál va?`): short labels,
the question in each description, nothing checked. Say the level that results, and let the owner
change it. Then say the round's length — *about 10 minutes, in three blocks* — and that it can
stop after any block.

## 5. The idea the rest builds on

Said once, never asked. First, where the O2 belief sits, at the level, as the bank's *Placement*
under O2 says — nothing for *not sure yet*. Then the level's explainer, section 2 of the bank: the
**personal benchmark**, what the owner's money does if they never choose an investment on purpose,
tied to their goal; and why a **process** — how they find out whether they do better than it.
It is worded so that it settles nothing the owner answers later: whether anyone can do better than
the market is their question, not the explainer's. Its purpose line is the bank's and the only
one: *KaxaNuk built me so that more people can make better investment decisions.* Its caveat
stays beside it: nothing on the reading map shows that a process makes more money; a process is
how you find out whether a result is yours, or luck.

On a retake, the explainer is said again only when the level changed, or when the owner asks.

## 6. The level's blocks

Section 3 of the bank says which questions each level asks, block by block — *Your scoreboard*,
*Your edge*, *You*, *The world moves*, *Your proof*, *Your process* — and the levels are nested:
each asks what the one below asks, in harder words, and more. Open each block with its name and
where it stands — *block 2 of 3 · You · 2 questions* — so the owner knows how much is left.

- **An open question** is its *Ask* at the level, ending with the bank's closing line, one per
  message. At Starter after *None yet* in the calibration, its *Example* comes under it unasked.
- **After every answer** — *not sure yet* and *skip* included — the question's *Teaches* line, as
  written: one idea, never a verdict on the answer. Starter names no work; Building at most one,
  as a lead; Researching the placement and the other side.
- **Presses on**, at Researching and on every retake: quote the owner's own line in
  `HOW-I-INVEST.md` that the question tests, if one clearly does; never guess one.
- **Behind it** is shown at Researching, or when the owner asks *show me the paper*: the map's
  leads, a note linked in place of a work it holds, a gap said out loud.
- **A question rises on its own.** When its *Behind it* work has a note, ask it one level higher
  and link the note, even inside a lower level. Rising changes the wording of a question the level
  asks; it never adds one the level does not ask.
- **The stance picks**, S1–S4, are one tool call, as the bank gives them. Then two or three lines
  placing the picks, from the map's *Where a belief sits* only, and *want to say any of that in
  your own words?* — the typed line is written; the picks never are.
- **The escapes** hold on every question — *Escapes and exits* below.

## 7. Checkpoints

After each block but the last, one tool question. The first is the pitch check, `How was it?`
(`¿Qué tal?`); the others are `Continue?` (`¿Seguimos?`); section 3 of the bank gives their
options. *Simpler* and *harder* switch to that level's set for the blocks left; nothing already
answered is asked again, and the round file takes the level the round ended at. *Save and stop
here* goes straight to the preview, *step 10*.

## 8. The closing

**C1**, at the level, quoting the line the owner typed for O2 — never a hunch they picked; with no
such line, ask about any belief they would like to test, or skip. **C2**, `Read next`
(`Aprender`), as the bank gives it at the level: no work already *read* is offered; a work *in
your Sources/, not yet read* only needs `read`; the others are found by their title and authors,
and nothing is downloaded. `teach` is offered only when `Knowledge/` holds a note on the idea;
otherwise that option reads *Learn one idea with me — after your first reading*. The works picked
go on the closing *Find first* line of `RESEARCHER.md` on the go, unless the owner leaves that
line alone in the preview; nothing from C2 reaches `Philosophy/`.

## 9. A retake: what moved

On a retake only, before the preview: the comparison of section 7 of the bank, in chat, and
never written to a file — a line of counts, a table by ID of then and now, and under each changed
answer the notes read between the two rounds whose work is its *Behind it*, named as reading in
between, never as the cause: *you read X between the two rounds; whether it moved you is yours to
say.* With the scope *Just show me what changed*, this is the whole run — the last two rounds, or
the last round and the reading since — and nothing is asked or written.

## 10. The preview, and the go

Show in chat, before anything is written:

- **From a strategy or another project**, first: *this writes to the researcher's home, not to
  this project.*
- **`Philosophy/HOW-I-INVEST.md`**: under each heading, every line to be added, word for word, as
  it will read — `- <their words> *(round N)*` — and a heading to be added at the end of the
  file. On a retake, under each changed answer, the old line, found under its heading by its
  *(round N)* tag and its words, quoted and marked *stays — I only add*.
- **A standing line a new answer clearly cuts against**, quoted once, in round 1 as on a retake:
  *both will stand; edit it by hand, or run `refine`, if one no longer holds.*
- **The round file**, whole, under its path.
- **`RESEARCHER.md`**: the works to add to the closing *Find first* line, or *left alone*.
- **Privacy**, one line: these lines are saved in your researcher's versions; leave out any you
  would rather not keep.

Then ask `Go?` (`¿Escribo?`) — *Go*, described as *write it and save a version* (*escribirlo y
guardar una versión*), *Change something*, *Stop*; in chat, any of the go words in the home's
`AGENTS.md` is the go. **A round with no typed answer** says *nothing typed, so
`HOW-I-INVEST.md` stays as it is*, and asks instead `Keep it?` (`¿Lo guardo?`) — *Keep this round
as a record*, *Change something*, *Write nothing* — because a kept round counts as round *N* and
makes the next run a retake.

**On *Change something*, ask again with options**, the changes this preview admits: *Leave out a
line*; *Reword in my words* — they type the line again, and only their words are written; *Leave
Find first alone*; and, on a retake with a changed answer, *Leave my old line — I'll fix it with
`refine`*, which writes as shown and puts the `refine` run in the hand-over. Then show the revised
preview and ask for the go again.

**On *Stop*, *Write nothing*, silence or a closed session, nothing is written.** The answers are
not kept, and the next run starts as this one did, as round *N* again.

## 11. Write, on the go only

1. **`Philosophy/HOW-I-INVEST.md`, add-only.**
   - One bullet per typed answer, word for word, in the owner's language, tagged *(round N)* —
     `- <their words> *(round N)*` — under the heading the bank's *Lands under* names, at the end
     of that heading's lines. An answer of several lines keeps them, indented under its bullet.
   - **Headings are matched by name or position**: by the English name; else by a heading in the
     owner's language that says the same; else, in a file holding the template's headings in the
     template's order — the newer five or the older four, without *Why I invest* — by position. A
     heading matched is never added again, so a translated heading is never duplicated.
   - Under a heading that still holds its angle-bracketed prompt, the prompt stays and the line
     goes below it: add-only holds for the template's text too, and the prompt is the owner's to
     delete by hand. A prompt is never the owner's view.
   - A heading the file lacks — `## Why I invest` in a file older than the template's, or every
     heading in a file with none — is added at the end of the file, in the language its other
     headings use, English when it has none. Nothing above it is moved.
   - A line identical to one already under its heading is not added again, and *keep* adds
     nothing. Nothing the owner wrote is edited, moved or deleted, the note at the top included.
   - Never written here: a pick, an example, a placement, a *Teaches* line, *not sure yet*, a
     skip, or any other status.
2. **`Philosophy/Evolution/YYYY-MM-DD.md`**, today's date — `YYYY-MM-DD-2.md` for a second round
   the same day, `-3` for a third — the folder created when it is missing. Written once and never
   edited afterwards, it holds only the round's number, date and level on its first line, then
   the question IDs with the owner's typed answers word for word, or their status, and on a
   retake *kept*, *changed*, *new* or *still open*:

   ```markdown
   # Round <N> · <YYYY-MM-DD> · <level>

   - O1 · <the owner's words, word for word>
   - O2 · not sure yet
   - Q2 · skipped
   - Q6 · explained
   ```

   - **The first line** is the round, the date and the level the round ended at — *Starter*,
     *Building* or *Researching*.
   - **One line per question asked**, in the order asked: `- <ID> · <answer>`, the answer the
     owner's typed words or a status — *not sure yet*, *skipped* or *explained*. A pick is never
     recorded: an S question takes the words typed for it, or *skipped* when none were. O3 is the
     level on the first line; C2 takes no line.
   - **On a retake**, a label follows the ID — `- <ID> · <label> · <answer>`: *kept* — and no
     answer, because the earlier words stand; *changed* — new words, or *not sure yet*, for a
     question answered before; *new* — words where no round had any; *still open* — no words in
     any round, and the status now. A question answered before and skipped or explained now takes
     no label, only its status: its earlier answer stands.
   - **In English**: *Round*, the level, the IDs, the labels and the statuses, because skills parse
     them; the answers are in the owner's language. Nothing the researcher wrote goes in — no
     question, placement, pick, teaching line or reading list.
3. **`RESEARCHER.md`**, only when C2 picked a work and the owner did not leave *Find first* alone:
   each work appended to the closing *Find first* line — year, authors and title as the map gives
   them, separated by semicolons, in place of the template's *none* — skipping one already there
   or already read. A section with no such line takes one as its last line, before *Out of scope
   for now*: `**Find first:** <the works>`. Nothing else in that file changes.

**Then save a version**, in the home, on the go that wrote — it covers the save, and no second
question is asked: `git add` each file this run wrote, by name, never `--all` —
`Philosophy/HOW-I-INVEST.md`, the round file, `RESEARCHER.md` when it changed — and
`git commit -m "Philosophy: round <N>, <level>"`. Say it in one plain line, *Saved*, never the
commands. When `git config --get kaxanuk.autosend` prints `true`, the version is also sent to the
owner's copy on GitHub, as the `backup` skill says. This replaces the
*Commit?* question an older home's `AGENTS.md` describes. A save refused for want of a name and an
e-mail asks for both in one plain line — *a name and an e-mail to sign the versions your researcher
saves; they stay on this computer* — sets them in the home only, never invented, and saves again;
a home with no `.git/` gets one line, that it keeps no versions yet.

## 12. Hand over

Short, in the owner's language and voice, in this order:

1. **What moved.** On a retake, the comparison's line of counts; on round 1, *round 1 written*,
   and how many lines went into `HOW-I-INVEST.md`.
2. **The first thing to `read`.** The first work picked in C2 — in `Sources/` already, `read` it;
   otherwise find it by its title and authors, then attach it or say where it is saved, and I copy
   it into `Sources/` on your go and read it; one that cannot be found comes off the *Find first*
   line by hand, the owner's file. With nothing picked, any source, the same way.
3. **When to come back.** Name two or three works from this round's reading list — the works
   picked in C2 first, then the list's *Start here* works in the map's order; at Starter, in the
   plain words of C2's *Three classic studies* — and say: once two of them have notes,
   `philosophy` again, in a new session; what was left *not sure yet*, skipped or never reached
   waits for them there. Without the reading map, no work is named: *once you have read a source
   or two*.
4. **`refine Philosophy/HOW-I-INVEST.md`**, when *Leave my old line* was picked, with the old lines
   to bring to it, each by its *(round N)*.

## Escapes and exits

The bank's escape table holds on every question. What it leaves to this skill:

- **In the owner's language too.** *explain* — *explica*; *example* — *ejemplo*; *not sure yet* —
  *no sé todavía*; *skip* — *salta*; *simpler* — *más simple*; *harder* — *más difícil*; *stop* —
  *para*; on a retake, *keep* — *igual*, *mantener*; and their usual words in any other language.
  A message that is only an escape, in any wording — *no sé*, *I don't know*, *ni idea* — is that
  escape, and writes nothing; a message with more than that is a typed answer, written as typed.
  When it could be either, ask once: *write that as your answer, or mark it not sure yet?* A
  number, or *that one*, after an example is a pick, not typed words: ask for their own words, or
  a skip.
- **Explain climbs a ladder.** The *Plain* line and the question in its plainest form; then the
  *Example*; then *skip, we'll come back after you read*, recorded as *explained*. *Explain* on
  two different questions in one block offers `Simpler?` (`¿Más simple?`) — *Yes*, *Keep this
  level* — once the current question is answered; at Starter, *Yes* puts the *Plain* line and the
  *Example* under every question left.
- **Not sure yet is a complete answer.** Nothing is written to `HOW-I-INVEST.md`, the round file
  records it, and the question's *Behind it* work becomes a reading suggestion in C2 at Building
  and Researching; at Starter, C2 keeps its four options, and *Three classic studies* covers it
  when the work is one of the three.
- **Skip** is recorded, and asked first in the next round. **Simpler** and **harder** work at any
  time, for the rest of the round: at Starter, *simpler* does what `Simpler?` *Yes* does; at
  Researching, *harder* has no set above it — say so, and offer the rest of the block in one
  message. **Stop** works at any time, and goes straight to the preview with what is already
  answered; a question it leaves unreached is open, and the next round picks it up.

## What this skill will not let you do

- Write a pick, an example, a placement, a *Teaches* line or a status into `HOW-I-INVEST.md`, or
  anything the researcher said into a round file.
- Edit, move or delete a line already in `HOW-I-INVEST.md` — that is `refine`'s, or the owner's
  by hand — or touch a round file once written.
- Write in `RESEARCHER.md` anything but works on the closing *Find first* line. A reading question
  is `read`'s to add.
- Name a work from memory, state a paper's finding as a settled fact, or put an *Edge* line of the
  map to the owner below Researching.
- Cite a round file as the owner's view, or as evidence of anything.
- Propose a product, a ticker, an allocation or a benchmark; compute a return; say buy, sell or
  hold.
- Write, or save a version, on a *Stop*, on silence or on a closed session.
- Write at home from a strategy or another project without saying so first in the preview.
- Write a plan, a comparison or a report as a file. The chat is the record, and the round file is
  the owner's answers only.

## References

- [`references/questions.md`](references/questions.md), in this skill's folder: the bank, as *The
  bank* above says, what holds without the reading map, and the *Bears on* table that `read`'s
  report reads to offer the next round.
- `references/reading-map.md`, in the `read` skill's folder: the one list a work may be proposed
  from besides the owner's library — where a belief sits and its other side, the beliefs people
  type, the ten papers of the two timelines, the hints. A work in it is a lead, never a citation.
