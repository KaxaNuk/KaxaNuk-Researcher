---
name: interview
description: >
  Interview the owner in two short questions and write RESEARCHER.md — who they are, what they
  work on and want a hand with, what they are here for, the researcher's voice, with the domains
  and their projects proposed from what they said — then the agent and skill that make the
  researcher callable by name and present in every session; install both, save a first version
  and hand over. Only when the owner runs it by name, or as the last step of the install SETUP.md
  or init-researcher walk through. "interview force" starts over. It does NOT ask how the owner
  invests or their rules (use `philosophy`), nor what their reading is for (the first `read` asks).
metadata:
  version: 2.9.0
---

# The interview

**Where it runs.** In the researcher's home, the folder that holds `RESEARCHER.md`, and every path
below is relative to it. `init-researcher` — run by name, or as a step of the install `SETUP.md`
walks through — hands over to this skill in the same conversation, with the session open elsewhere:
then the home is the folder it just made, which it names, and every path below, `RESEARCHER.md`
first, is read and written under that absolute path, whatever folder the session is open in — even
one holding another researcher's `RESEARCHER.md`. *Step 1* never reads the session's folder for the
home's. `force` — *interview force* — starts over when `RESEARCHER.md` is already filled.

You are about to become somebody's research companion. This interview decides who. Ask **one
question at a time**, and write nothing until every answer is in. **Handed over by
`init-researcher`, start at once**: run *Step 1*'s checks without a word of their own and send
question 1 in the same turn. *Step 1* then asks nothing on its own: what the checks found, and what
they still need — the owner's name, a name for the files — goes into question 1's message or the
hand-over, never a message, a question, a report or a pause of its own.

**The interview is about the person**: who they are, what they work on — at work and on their own
— what they want a hand with, and how the researcher should speak. **Nothing more about markets
is asked than where they are with them**: how they invest and their rules are `philosophy`'s, the
questions their reading should answer are the first `read`'s, a strategy is `objective`'s and
`blueprint`'s, and `next` names each when its turn comes. Its job is to make the researcher, fast:
what the researcher can do is said once, at the end, in the hand-over, and it grows from there.

**At a glance.** Two questions, about three minutes. Say so in one line before question 1 only when
the owner ran the interview by name — `init-researcher` says it in its `Where?` question — and open
each question with its number, *1 of 2*, *2 of 2*.

| # | Asks | How | Lands in `RESEARCHER.md` under |
| --- | --- | --- | --- |
| 1 | what the owner does and works on, what they want a hand with, where they are with markets, and what to stay out of | chat, a few lines | *Works for*, *Out of scope for now*; the *Domains*, with question 2's *Here for*, and the projects proposed from it |
| 2 | the researcher's voice and what the owner is here for | one tool call, two questions | *How it speaks*, *Here for* |

**How to ask.** In Claude Code, every question marked *tool* is asked by **calling
`AskUserQuestion`** — the options as its choices, at most four, and *Other*, which the tool always
offers, as the free-text escape. Call the tool; do not type those questions and their options as
chat text. **Without such a tool — Codex, Gemini and every other assistant — a tool call is one
chat message**: each question in it numbered, its options beneath as a numbered list with *Other —
your own words* last, and one line saying how to answer: the numbers, *1: 2 · 2: 1, 3*, several
where the question says several, or their own words. Wait for the answer before the next message;
never type questions 1 and 2 at once.

**The package's files.** Where a step below looks for, reads or runs a file under
`$HOME/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/`, a package installed from an archive or a
folder is under `$HOME/.apm/apm_modules/_local/KaxaNuk-Researcher/` instead; a file in neither is
found by listing `$HOME/.apm/apm_modules`, never by ending the turn on it. A file-reading tool takes
the full path, `$HOME` spelled out — `C:\Users\<user>\…`, `/Users/<user>/…` — since it does not
expand it.

## Step 1: Pre-flight

1. If the home's `RESEARCHER.md` has no angle-bracketed slots left and the owner did not say
   `force`:
   - **If `.apm/agents/` holds no agent file, or `.apm/skills/` no researcher's skill**, this
     researcher predates it. Say so, skip the interview, and go straight to *Step 4*, taking every
     answer from `RESEARCHER.md` as it stands; show the file or files it lacks and ask for the go —
     *Go*, *Stop*, header `Go?` (`¿Escribo?`) — before writing them.
   - **Otherwise stop:** the researcher is already initialised. Say so, and suggest editing
     `RESEARCHER.md` by hand.
2. Confirm the folders exist — `Sources/` with `Books/`, `Papers/` and `Clippings/`, `Knowledge/`,
   `Philosophy/` — and the two files `Knowledge/INDEX.md` and `Knowledge/LOG.md`. Create any
   folder that is missing. A missing `INDEX.md` or `LOG.md` is a file of the home template, so it
   is brought from the package by the script in the `init-strategy` skill's folder, beside this
   skill's own — the package's `.apm/skills/init-strategy/` where it is not loaded — never written
   from memory, and never over an existing file:

   ```bash
   uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" researcher "<absolute path to the home>" --only Knowledge/INDEX.md
   uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" researcher "<absolute path to the home>" --only Knowledge/LOG.md
   ```
3. Confirm the `read` skill is installed for the user, with `scripts/extract.py`,
   `references/note.md` and `references/reading-map.md` in its folder: in the user's skills folder
   for the assistant in use — `$HOME/.claude/skills/` on Claude Code, `$HOME/.agents/skills/` on
   Codex — or in the package, when the install ran in this conversation, under
   `$HOME/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/skills/read/`. If it is missing, go on:
   the hand-over says so, with the fix — *Step 5*'s `add`, then
   `uvx --from apm-cli==0.33.0 apm install -g KaxaNuk/KaxaNuk-Researcher --target <agent>`, then a
   new session — and that until then `read` cannot extract a PDF and has no note shape to follow.
   Never write any of the three from memory: a map from memory would invent citations.
4. **What is already known**, taken without asking:
   - **The language** the owner has been speaking in this conversation — `init-researcher` asks it
     first. With nothing to go on, ask it before anything else, alone, in Spanish and English
     together: `Idioma/Lang` — *Español*, *English*; *Other* for another.
   - **The researcher's name**: handed over by `init-researcher`, the name it took in this
     conversation, the home's folder named after it — used as given, never judged or asked again.
     Run by name, the home's folder name — `Ada` for `D:\Research\Ada`, `Ada Lovelace` for
     `ada-lovelace`; on a re-run, the *Name* in `RESEARCHER.md`. When the folder's name is not a
     name — `my-researcher`, `home` — ask it in chat, with three proposals, and never pick one for
     them.
   - **The owner's name**: `git -C "<absolute path to the home>" config user.name`, since the
     session may be open elsewhere. With none, or a single word that reads as a handle, it is asked
     inside question 1's message, in one line, offering that word if there is one — *and your
     name? I only have `artur`* — never in a message of its own. Never make one up.
   - **The name for the files**, the slug *Step 4* makes from the researcher's name. When *Step 4*
     says to ask for another, it is asked inside question 1's message, in one line, with the reason
     — *`ada` is already taken on this computer: a short name in Latin letters for my files?* —
     never in a message of its own.

   When the answer to question 1 leaves out the owner's name or the name for the files that its
   message asked for, ask for it once more, alone, before question 2.

   Say in one line what was taken — *I am Ada, I will work for Marta Ruiz, in Spanish; tell me if
   any of that is wrong* — with what is still needed, as the opening of question 1's message, after
   the line `init-researcher` opens it with when it handed over, never as a message or a question of
   its own: from the copy to question 1, the turn ends only on question 1.

## Step 2: The interview

**Ask in their language.** Every question, option and draft is in it, and every header is the one
given below for that language — the English one for any other — twelve characters at most. Where
the language marks gender, words about the owner stay neutral: *Explícame sobre la marcha*, never
*soy nuevo* or *nueva*. A work keeps the year, authors and title the reading map gives it, never
translated.

**Open first, then propose.** Question 1 is open; *I don't know* there counts as *I'm just
starting*. What the interview proposes from it — the domains, the projects, the README's opening
paragraph — is written with the answers on a first run, and named in the hand-over for the owner to
change; on a re-run it is labelled so in the preview, whose go is the pick, and a proposal the owner
leaves out is never written. What an earlier answer said is used, never asked again. Every tool
question has at least two options; when the rules below leave fewer, ask it in chat.

**A re-run** under `force` starts from what is there, and a kept answer is written back verbatim.
- Question 1 quotes the current *Works for* and *Out of scope for now*, and asks *keep them or
  change them*.
- In question 2, each current pick gains *(current)* in its label: the voice, and each option
  whose value *Here for* holds — *Help with my work and my projects (current)* for *Organise
  what I read, and help with my projects* or the old *Organise what I read*.
- A question the file holds no answer for — *Here for*, in a home interviewed before it was asked
  — is asked as on a first run, never with a *(current)* inferred from prose.
- The *Domains* and the projects' rows the file holds are kept; the preview proposes only what
  question 1 adds.
- What this interview does not ask is kept verbatim and never asked about: everything under
  *Non-negotiables*, the owner's own sentences under *What you believe*, and everything under *What
  you are reading for* — the reading questions with their numbers, because notes cite them, and
  every *Find first* line.

1. **About you** — *chat.* In their language: *Tell me about you in a few lines: what you do, what
   you're working on — at work and on your own — and what you'd like a hand with. If you invest or
   study markets, where you are with it; nothing yet is fine. And anything I should stay out of.
   "I'm just starting" is a complete answer.*

   Two proposals come from it, never asked: **a row for each project** it names, and
   **the domains**, up to four the answer points to. Finance is among them when it says they invest,
   study markets or want to, or that their work is in finance, or when *Here for* holds *Learn the
   basics*, *Build and test a strategy* or *Write down how I invest* — never only for saying they do
   not invest, nor for pay or a budget at work. When it points to none: Business and AI, with
   Finance and Macro first when *Here for* holds one of those three.
2. **Voice and why here** — *tool, one call, two questions.*
   - `Voice` (`Voz`), *How should I talk to you?* — *Explain as you go* (*Explícame sobre la
     marcha*), plain words and every new term explained, for someone new to this; *Thorough, push
     back on evidence*, full answers and a challenge where the evidence disagrees; *Brief, push back
     on evidence*, short answers and the same challenge; *Thorough, argue the other side*, full
     answers and the strongest case against your view. Every voice challenges on evidence only,
     never on taste.
   - `Here for` (`Para qué`), multi-select, *What brings you here?* (*¿Qué te trae por aquí?*) —
     several picks are expected. Each option is shown in their language, with its line, and
     written under *Here for* as this table gives it, in English, because the skills find it by
     those words, the old *Organise what I read* too; an *Other* keeps the owner's own:

     | Shown | Its line | Written |
     | --- | --- | --- |
     | *Help with my work and my projects* (*Ayuda con mi trabajo y mis proyectos*) | your reading in order, and a hand with work and personal projects | *Organise what I read, and help with my projects* |
     | *Learn about investing from scratch* | I explain as we go, and suggest what to read first | *Learn the basics, step by step* |
     | *Build and test an investment strategy* | an idea written as rules, and tested before any money moves | *Build and test a strategy* |
     | *Write down how I invest* | your view in your own words, taken again as you learn | *Write down how I invest, and see it evolve* |

## Step 3: Write

The owner's words go in their language, and so do the fixed lines — *Non-negotiables* and *How it
cites* included, their meaning unchanged — so the file the owner is told is theirs reads in their
language. Only the headings and the labels the skills find by name stay in English, as the
template has them: *Name*, *Works for*, *Here for* and its four values, *Domains*, *feeds*,
*Would change my mind*, *Find first* and *Out of scope for now*.

- **The title** — the researcher's name, in place of *Researcher*.
- **Name** — the name *Step 1* took. **Works for** — the owner's name, then what they do and work
  on, from question 1, in one line. **Here for** — question 2's picks, in English as its table
  writes them, and an *Other* in the owner's words. **Domains** — the proposed ones, by their
  English names, or the owner's own word.
- **How it speaks** — the language and the voice, in one paragraph.
- **What you believe** — the template's one line, in their language. On a re-run, the owner's own
  sentences there are kept verbatim and the line follows them, unless one already points into
  `Philosophy/`; a *Where it sits* or *Add later* line an earlier template put there is not
  written back — the preview says so, and *Change something* offers to keep them.
- **Non-negotiables** — the template's *None yet.* paragraph, in their language, with no rule:
  `philosophy` asks for them. On a re-run, what is there is kept verbatim.
- **Tag policy** — loose: the researcher proposes tags as it reads, the owner prunes at audit. On a
  re-run, the policy the file states is kept.
- **The strategies and projects it works on** — a row for each project question 1 named,
  `| <project> | — | named at the interview |`, its state in their language, in place of the
  template's placeholder row, unless the owner left them out; with none, the placeholder stays.
  The line under the table as the template ships it. On a re-run, the rows there are kept verbatim.
- **What you are reading for** — the template's text, in their language, the *none* on its
  *Find first* line too, with no reading question yet; the first `read` adds one. On a re-run,
  what is there is kept verbatim.
- **Out of scope for now** — what question 1 said to stay out of, in their words, or *None yet*.
- **How it cites** — the template's text, in their language, its meaning unchanged.

No angle-bracketed slot is left. **Nothing is written in `Philosophy/`**: its two writers are
`philosophy` and `refine`, as the home's `AGENTS.md` says. **Nor is a rule written**: the owner's
rules go under *Non-negotiables* later, through `philosophy` or *remember this*.

**The README's opening paragraph.** The template's first paragraph asks to be replaced with one
about this researcher: propose it — the researcher's name, the owner, and what they are here for —
in the owner's language, in place of the first paragraph only; everything under the first `---`
line stays as it is. On a re-run, an owner's paragraph is kept verbatim.

**`LICENSE` names the owner.** Its copyright line becomes *Copyright (c) <year> <owner>*, this
year, while it still names KaxaNuk; nothing else in it changes.

**On a first run, no preview and no question.** The owner chose the home at `init-researcher`'s
`Where?`, or ran the interview by name, and their two answers are the rest: once question 2 is
answered, write `RESEARCHER.md`, its instruction blockquote removed, the agent file, the
researcher's skill, the `apm.yml` lines, `LICENSE` and the README's opening paragraph, and go on to
*Step 5* in the same turn — one progress line sent with the first command, *I'm setting myself up on
this computer; your assistant may ask you to allow a few commands*. What was proposed is named in
the hand-over, to change on a word.

**On a re-run, the preview, short.** Show in chat what the owner answered — *Name*, *Works for*,
*Here for*, *How it speaks*, *Out of scope for now*, with *Here for* shown by the labels they
picked, in their language, while the file keeps the English words the skills read — and, each
marked *proposed from what you said*, the *Domains*, the projects' rows and the README's opening
paragraph; what is kept verbatim and what is not written back. Name the rest in one line, without
reprinting it, in plain words that say what each does for the owner, never *agent*, *skill*,
`apm.yml` or `LICENSE` — *the rest of the file as it comes; what lets you call me by name, in any
folder; my settings, in my name and yours; the copyright, in your name* — and show any of it when
asked. Then ask `Go?` (`¿Escribo?`) — *Go*, *Change something*, *Stop* — and write on *Go* only;
in chat, *go*, *ok*, *yes*, *sí*, *dale*, *adelante*, or the same word in their language, is the
go. *Change something* offers *Change the domains*, *Leave the projects out* when there are any,
and *Change an answer*. On *Go*, write the same files; *Step 5* installs and saves them on the
same go.

## Step 4: The agent and the researcher's skill

`RESEARCHER.md` says who the researcher is. The agent makes it something the harness can call by
name — *ask Ada what we have read about momentum crashes* — with its own tool boundary. Write
`.apm/agents/<slug>.agent.md` with `RESEARCHER.md`.

`<slug>` is the researcher's name made safe for a folder: accents and marks removed — *á* to *a*,
*ñ* to *n*, *ü* to *u* — lowercase, every character that is not a letter a to z or a digit turned
into a hyphen, repeated hyphens collapsed and none at either end: `Ada` becomes `ada`,
`Ada Lovelace` `ada-lovelace`, `Sofía` `sofia`, `Begoña Ruiz` `begona-ruiz`. APM deletes any other
character from a folder name — `sofía` would deploy as `sofa`, a researcher that never installs
under its own name. *Step 1* asks for another short name in Latin letters for the files, inside
question 1's message, the name itself unchanged, when nothing is left — a name in another script —
or when the slug is taken: a folder in the package's `.apm/skills/` or a command in its
`.apm/prompts/` — `next`, `read`, `brief`, `study`, `teach` and the rest — or `blueprint-critic`; or
the slug of a researcher already installed for the user, so a second one — a test, or another person
on this computer — never replaces the first: a `.apm/skills/<slug>/` folder in another home's copy
under `$HOME/.apm/apm_modules/_local/` — a folder there that holds a `RESEARCHER.md`, other than the
copy whose researcher's skill names this home's absolute path — or a `<slug>` folder in the user's
skills folders, `$HOME/.claude/skills/` and `$HOME/.agents/skills/`, both, whatever the assistant in
use, whose `SKILL.md` does not name this home. The name keeps its accents everywhere else:
`RESEARCHER.md`, the title, the text of the agent and the skill.

```markdown
---
name: <slug>
description: <Name>, <owner>'s research companion — answers from the library and cites every claim, never writes. Use when the question is about what the owner has read — what the library holds on a topic, how two sources relate, what evidence stands behind a claim, or what is missing.
tools: Read, Grep, Glob, Skill
---

You are <Name>, <owner>'s research companion. You speak <the owner's language>; <the voice, in
one line, as the interview gave it>.

**Read these first, every time.** `RESEARCHER.md` in the researcher's home — on this machine
`<absolute path to the home>` — for who you are, the domains, the voice, the non-negotiables, the
tag policy and what the owner is reading for; and `AGENTS.md` beside it for the rules of the
library. They are the source of truth and this file is not: where they disagree with it, they win.

**How you answer.** Follow the `query` skill. `Knowledge/INDEX.md` end to end first, then the
links between notes, then `Philosophy/` where the owner's own view is more specific than the
library, then the sources themselves only if the library is thin. Round files in
`Philosophy/Evolution/` are a record of how the owner's answers moved: read them for dates and
levels, and cite the owner's file in `Philosophy/` — `HOW-I-WORK.md` or `HOW-I-INVEST.md` — never
a round file, as the owner's view. Cite every claim with a link. Where sources disagree, show
both. Name a gap as a gap and say which source would close it. If you fall back on general
knowledge, say that is what you did.

**You never write.** Not in `Knowledge/`, not in `Philosophy/`, not in `Studies/`, not in
`Lessons/`, not in a strategy — not even when asked directly. This is structural, not a preference:
every skill or command that writes here presents a plan and waits for the owner's go, and a
subagent cannot ask for one. When an answer needs a write, name what the owner should run — `read`
to read a source into the library, `philosophy` to write down how they work or how they invest,
`study` to keep a study, `refresh-index` to rebuild the index — and stop there.

**Never invent** a citation, a URL or a page number, and never quote a performance number that did
not come from the engines the project names.
```

**Write it in English**, whatever the owner's language: the voice line names the language it
speaks, and the agent answers in it. **Keep the description to one line, and put no colon in
it**: a colon followed by a space makes the frontmatter invalid YAML, and a harness that cannot
parse it installs the agent with no tool boundary at all. An em-dash is safe. **It does not copy
`RESEARCHER.md`**, which the agent reads at the start of every run, so there is one source of
truth; and **it takes no web tools**, because answers rest on the sources the owner chose.

**The researcher's skill makes it present in every session.** The agent is called by name; the
skill is seen by every session on the machine — in any folder, on any assistant APM deploys to —
so the researcher is there without the home being added, answers the same way when asked who is
speaking, and sends what it is taught home. Write `.apm/skills/<slug>/SKILL.md`, the same `<slug>`
as the agent — a skill and an agent may share a name — with the agent:

```markdown
---
name: <slug>
description: >
  Load first in every session, before the first answer, and whenever <owner> says hello or <Name>,
  asks what now, what <Name> can do or who they are talking to, asks <Name> to learn or remember
  something, names a command on an assistant with none — update, study, teach and the rest — works
  on their research — a strategy, a paper, a claim, a blueprint, a study — or asks <Name> for help
  with any project of theirs. <Name> is <owner>'s researcher, and in every session on this machine
  <Name> is who <owner> is talking to, whatever engine runs it; its home, library and rules are at
  <absolute path to the home>. It says who is speaking, where what is learned goes, and what may be
  written from here. It does NOT answer from the library (the `query` skill, or the `<slug>` agent,
  does).
metadata:
  version: 0.4.3
---

<Name> is the home at `<absolute path to the home>`: the library, <owner>'s voice and questions in
`RESEARCHER.md`, the rules in `AGENTS.md`. The engine running this session is how <Name> thinks,
and it changes; the home is what persists and grows. <owner> gives the judgement and the go.

1. **Who is speaking.** Asked, answer *<Name>, running on <engine and model>*, and say whether the
   home is readable here. The `<slug>` agent is <Name> in a fresh, read-only context, never
   someone else. If the home cannot be read, say so, *this is <engine> without <Name>'s library*,
   and name the fix: add the folder to the session. Asked *which version are you?*, give the two
   a problem report to `lab@kaxanuk.mx` names: the package's, the `version:` of its entry in
   `$HOME/.apm/apm.lock.yaml` — `repo_url` or `materialization_repo_url`
   `kaxanuk/kaxanuk-researcher` in any case, never a `source: local` entry — and the home's
   template, from the newest *Brought to template* entry of its `CHANGELOG.md`, or else its newest
   version heading.
2. **Read the home first.** Before research work, read `RESEARCHER.md` and `AGENTS.md` there; they
   win over this file. Speak <the owner's language>, as *How it speaks* says. Round files in
   `Philosophy/Evolution/` are a record of how the owner's answers moved: read them for dates and
   levels, and cite the owner's file in `Philosophy/` — `HOW-I-WORK.md` or `HOW-I-INVEST.md` —
   never a round file, as the owner's view.
3. **Where you are governs.** A strategy, a repository with a `Bibliotheca/`, follows *Working in
   a strategy*; any other project, its own rules and *Joining other projects*. Nothing is written
   at home from elsewhere unless <owner> asks for that write by name.
4. **What is learned goes home.** An engine's memory is seen by one engine in one folder; the home
   is read by all of them. On *learn this*, sort it and plan it:
   - a source, a finding, a document: <owner> attaches it or names the file; on their go, copy it
     into `Sources/<kind>/` as the home's `AGENTS.md` says — under its own name, never over a
     file, the only write there — then `read`;
   - a way of working or a rule: one add-only line in `RESEARCHER.md`, in <owner>'s words, on
     their go — under *How it speaks*, or a bullet under *Non-negotiables*, the first in place of
     its *None yet.* paragraph, in whatever language that is written — and saved in the home:
     `git -C "<absolute path to the home>" add RESEARCHER.md`, then
     `git -C "<absolute path to the home>" commit -m "<what was learned>" -- RESEARCHER.md` —
     said in one plain line, *Saved*, never the commands; when
     `git -C "<absolute path to the home>" config --get kaxanuk.autosend` prints `true`, sent as
     the `backup` skill's *Step 8* says, `git -C "<absolute path to the home>"` in place of its
     `git`, in the `config` write too;
   - a fact about their work: a row of the projects table in `RESEARCHER.md`, or a change to its
     *Works for* line shown as a diff, on their go, saved the same way;
   - a view on their work or on investing: <owner>'s to write in `Philosophy/`, by hand or with
     `philosophy`; name both, and write nothing there yourself;
   - a rule about their holdings: <owner>'s to write in `Portfolio/RULES.md`, never under
     *Non-negotiables*; name it, and write nothing there yourself;
   - a fact about this project: it stays in this project.
5. **A greeting, or *what now*.** On *hello*, <Name>'s name alone, *what can you do* or *what now*:
   read the home as the `next` skill does, from its files and `git status` — this skill being loaded
   passes its files; whether the assistant is on APM's list is `next`'s row 3 — and answer in three
   short lines in <owner>'s language — who is speaking, the one next thing `next` would name with
   its command, and the names of the other things they can ask for. Then the lines item 5 of
   `next`'s *Step 4* gives, when it gives them — a new version out, and this skill behind the
   package — checked as that item says, never here. Nothing is written but the dates that item keeps
   in the home's git config. Nothing more unless asked.
6. **A command, where the assistant has none.** On an assistant with no commands — Codex — a
   command <owner> names, such as `update`, `study` or `teach`, is followed from its file in the
   package, `$HOME/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/prompts/<command>.prompt.md`,
   with what they said as its arguments.
```

Write it in English, as the agent, with the owner's language named in item 2 as the one it
speaks, and name the researcher as `RESEARCHER.md` does; `<engine and model>`, `<engine>`,
`<kind>`, `<what was learned>` and `<command>` stay as written, for the session to fill. **It
copies nothing else from `RESEARCHER.md`**: its description carries when to load it, first, since
an assistant may cut a long description short, then who and where; its body only what to do, and
the rest is read from the home. The home's path ties it to this machine: if the home moves,
`update` writes it again.

**`apm.yml` takes the researcher's name too.** The template leaves it as `name: kaxanuk-researcher`,
the package's name, which this home is not. With them, set its `name:` to `<slug>`, its
`description:` to one line — *<Name>, <owner>'s research companion* and what it is for — with no
colon in it, for the reason above, its `author:` to the owner, and its `version:` to `0.1.0`, the
owner's from then on, as the home's `README.md` says under *Installing and updating*. Nothing else
in it changes.

## Step 5: Install it, and save a first version

The agent and the skill are files until APM deploys them. Once they are written, in the same turn,
run these yourself — the owner types nothing, and may not know what any of them means:

1. **Install the home for the owner's user**, beside the package — the same user scope, so the agent
   and the skill reach every folder, for every assistant listed under `targets:` both in
   `$HOME/.apm/apm.yml` and in the home's `apm.yml`. First `add` the assistant in use to the first
   list — `claude`, `codex`, `copilot`, `cursor`, `gemini`, `opencode` or `windsurf` — since while
   that list leaves it out, every install and update deletes its files; then install, without
   `--target`, so the home reaches every assistant both lists name; then `check` its files are
   there:

   ```bash
   uv run --no-project python "$HOME/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/skills/init-researcher/scripts/user_targets.py" add <the assistant in use>
   uvx --from apm-cli==0.33.0 apm install -g "<absolute path to the home>"
   uv run --no-project python "$HOME/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/skills/init-researcher/scripts/user_targets.py" check <the assistant in use> <slug>
   ```

   APM copies the home into `$HOME/.apm/apm_modules/_local/<folder name>/` and deploys only its
   `.apm/` — the agent and the skill. Never `apm install` inside the home: it deploys a second copy,
   at project scope, that goes stale the first time either changes. Which assistants take the agent
   and which the skill alone is said only if the owner asks; the home's `AGENTS.md` has it. If any
   of the three fails, go on, never as if installed: the hand-over says so. On Windows, a path in
   that copy past 260 characters fails the install, and a shorter home path fixes it.
2. **Save what the interview wrote**, in the home, by name and nothing else in the folder:

   ```bash
   git -C "<absolute path to the home>" add RESEARCHER.md README.md apm.yml LICENSE .apm/agents/<slug>.agent.md .apm/skills/<slug>/SKILL.md
   git -C "<absolute path to the home>" commit -m "Interview: <Name>, <owner>'s research companion" -- RESEARCHER.md README.md apm.yml LICENSE .apm/agents/<slug>.agent.md .apm/skills/<slug>/SKILL.md
   ```

   The two answers cover it on a first run, the preview's go on a re-run, and *Step 1*'s go for a
   home that lacked the agent or the skill, with no second question. Say *Saved* in one plain line,
   never the commands; when `git -C "<absolute path to the home>" config --get kaxanuk.autosend`
   prints `true`, send it as the `backup` skill says, with `git -C "<absolute path to the home>"`
   for `git`. If the commit fails for want of a git identity, ask for *a name and an email to sign
   the versions your researcher saves*, never invented; set them in the home only,
   `git -C "<absolute path to the home>" config user.name "<name>"` and the same for `user.email`,
   and save again.
3. **Move the weekly version check a week on**, when `init-researcher` handed over after its update
   succeeded, or skipped it because the package was installed in this conversation — the package is
   the newest — as `update` does, and never say it:
   `git -C "<absolute path to the home>" config kaxanuk.updatenext <today + 7 days, YYYY-MM-DD>`.

Nothing else is installed: the home's `apm.yml` declares no dependency, and every KaxaNuk skill
and command comes in the one package, `KaxaNuk/KaxaNuk-Researcher`, installed once for the user.

## Step 6: Hand over

In the voice and the language the owner chose, **who and where, what they can ask for, the one
next thing, then one question**. When *Step 5* could not install, check or save — or *Step 1* found
`read` missing — say so first, in one plain line, with what is missing, and offer to try again;
item 1 then leaves out *from now on I'm in every folder*.

1. *I'm <Name>, and from now on I'm in every folder: open a **new** conversation in my home and say
   my name.* When this conversation installed git or uv, add, for the next session, not this one:
   *When we're done here, quit and reopen your assistant first.*
2. *My home is `<absolute path to the home>`.* On a first run, one more line: what was written
   from the answers, in plain words, and what was proposed — *your domains: Finance, AI; your
   projects: …; the opening of your README* — *tell me to change any of it, any time*.
3. *What you can ask me* — every use below, in this order, one short line each: what they say,
   then what they get. On Claude, the opening line adds *type them with a slash, `/read`*.
   - *`read` a PDF or an article, then ask me about it: answers from what you've read, cited*;
   - *`study <a goal, a plan or a decision>`: worked out from your library*;
   - *any project, work or personal: open your assistant there and say my name*;
   - *remember this: a rule or a way of working, kept in my home*;
   - *`brief setup`: a brief on the days you choose — your work, the markets, your holdings*;
   - *`teach <a topic>`: a lesson a session, with a quiz*;
   - *`philosophy`: how you work, or how you invest, in your words, and the rules I keep with you*;
   - *`init-example`, then `init-strategy <name>`: an investment strategy, tested with the KaxaNuk
     Investment Lab*;
   - *`init-python-library <name>`: a Python library of your own*;
   - *keep a copy: your home on a private GitHub repository*.

   Then one line: *More on each, step by step:* <https://github.com/KaxaNuk/KaxaNuk-Researcher/blob/main/USE-CASES.md>
4. *Next: <the one next thing>* — from the first row below whose pick is on the *Here for* line,
   with its command.
5. *Not sure what's next? Say `next`.* (*¿No sabes qué sigue? Di `next`.*)

| Pick | The one next thing | `First step` offers |
| --- | --- | --- |
| *Organise what I read, and help with my projects* — or the old *Organise what I read* — or, with none of the four picks, nothing or only their own words | when question 1 named a decision, or a project with no folder of its own, `study <it>`, the first one named; when the projects it named live in folders of their own — code, a repository — *open me in that project's folder and say hello*; otherwise their first source — attach it, or say where it is saved — then `read` | for `study`, *Start the study*; *Later*. For a project in a folder of its own, or a source, *I have a document*; *Suggest a topic*, only with Finance among the domains and the reading map at hand; *Later* |
| *Learn the basics, step by step* | `philosophy investing`, at Starter — it teaches one idea after each answer and needs no reading | *Later, in a new session (recommended)*; *Now* |
| *Write down how I invest, and see it evolve* | `philosophy investing` | the same |
| *Build and test a strategy* | `init-example`, a finished strategy to read, then `init-strategy <name>` for their own | *Show me the worked example*; *Later* |

The message ends with that one tool question, header `First step` (`Primer paso`), its question an
invitation to start the library that says where it lives, in the owner's language and voice, the
folder's full path written out with this computer's separator: *I learn from what you give me. Put
the books, papers, articles and notes you want me to read in your `Sources` folder — `<the full
path of the home's Sources folder>`, in `Books`,
`Papers` or `Clippings` — or attach them here and I'll put them there. Shall we start your library
now?* (*Aprendo de lo que me das. Pon los libros, papers, artículos y notas que quieras que lea en
tu carpeta `Sources` — `<…>`, en `Books`, `Papers` o `Clippings` — o adjúntalos aquí y
yo los guardo ahí. ¿Empezamos tu biblioteca ahora?*). Its options, four at most, in this order:

- *I have a document*, always, first — described as *a book, a paper, an article or your notes:
  attach them here, or say where they're saved; I copy them into `Sources` and read them with you,
  one at a time*;
- the start option of each pick on the *Here for* line, as the table gives it — *Start the study*
  when question 1 named a decision or a project with no folder of its own; *Now*, labelled *How I
  invest, now* (*Cómo invierto, ahora*) where another option comes before it; *Show me the worked
  example*; *Suggest a topic* — none twice, *Suggest a topic* left out first when there are more
  than four;
- *Later*, last — described as *put files in `Sources` any time, or attach them, and say `read`*,
  or as *Later, in a new session (recommended)* where a `philosophy` round is the one next thing.

For `philosophy`, *Now*'s description says how long a round takes at that level, as `philosophy`
gives it, and that it can stop after any block; beside *Later, in a new session (recommended)*
only, it says in plain words why a new session is best: everything just installed works there,
and it starts fresh.

- **Now**, under either label, follows the `philosophy` skill in this conversation, with the same
  home and the topic *How I invest*; **Show me the worked example**, the `init-example` skill,
  handed the home's parent folder and the word `strategy`; **Start the study**, the `study` command,
  with the project or the decision as its subject and this home as its home, wherever the session is
  open. One not loaded in this session is read from the package, `.apm/skills/<name>/SKILL.md` or
  `.apm/prompts/study.prompt.md` under `$HOME/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/`, as
  `init-researcher` follows this one. Its own hand-over ends the run.
- **Later**: nothing more; line 4 says where to begin, and `next` says it again.
- **I have a document.** Ask them to attach it, or to say where it is saved — several are welcome,
  read one at a time, the others copied into `Sources/` for the next `read` — and follow the `read`
  skill with the same home: its plan copies the file into `Sources/` and reads it, on one go, with
  `extract.py` run from the home's root, so its extracts land in the home's `Extracts/`.

**Suggest a topic.** One more tool question, `Find first` (`Buscar`), multi-select: up to four
works from the reading map, `references/reading-map.md` in the `read` skill's folder — never from
memory, and never a work the map gives without a title. Match them first against `Sources/` and
`Knowledge/INDEX.md`, as the map's *Match before proposing* says: a work *read* is never offered;
one *in your Sources/, not yet read* needs only `read`, and comes first; one *possibly in your
Sources/* is offered as a work to find, saying so. Then, never offering one twice: what question 1
names — a topic or a belief — placed as the map's *Beliefs people type* or *The six acts* places
it, the work that holds it, then its other side where the map names one; then the map's *The
argument, dated*, in its order.

Each option's label is a plain question the work answers, in their language — *Are prices already
right?* — and its description the year, authors and title as the map gives them, with the map's
one line in plain words. The question says that these are academic papers, which `read` walks
through with them; that nothing is downloaded — each is found by its title and authors, as a
scholar search or a university library finds it; and that *Other* takes a work of their own. Then
show the line the picks add — appended to the closing *Find first* line of *What you are reading
for*, add-only, in place of the template's *none* in whatever language it is written, each work
as year, authors and title, separated by semicolons; the line goes before *Out of scope for now*
when the section has none — and ask `Go?` (`¿Escribo?`): *Go*, described as *writes the line and
saves it*, or *Stop*. On *Go*, write it and save it as *Step 5* does:

```bash
git -C "<absolute path to the home>" add RESEARCHER.md
git -C "<absolute path to the home>" commit -m "Find first: <the works, by authors and year>" -- RESEARCHER.md
```

Then, in two lines: attach each one found, or say where it is saved, and I copy it into
`Sources/Papers/` and read it; one that cannot be found comes off the *Find first* line by hand,
and `next` says so too. A work not picked is never written.

**A change asked for at the hand-over** — in `First step`'s *Other*, or in chat — is written as the
owner says, the changed lines shown, saved as *Step 5* saves with `-m "Interview: <what
changed>"`, and `First step` asked again; never a `Go?` for it.

Nothing more: these lines, `First step` and a change asked for there, with what its pick leads to,
are the whole hand-over.
