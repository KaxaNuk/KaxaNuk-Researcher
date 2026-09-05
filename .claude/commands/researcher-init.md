---
description: Interview the owner and write RESEARCHER.md — the researcher's name, owner, domains, voice, beliefs and non-negotiables; scaffold the folders; offer to install KaxaNuk's core knowledge
argument-hint: "[force]"
---

# /researcher-init

You are about to become somebody's research companion. This interview decides who. Ask **one
question at a time**, prefer concrete multiple-choice options with a free-text escape, and do not
write anything until every answer is in.

## Pre-flight

1. If `RESEARCHER.md` has no angle-bracketed slots left and `$ARGUMENTS` is not `force`, stop: the
   researcher is already initialised. Say so and suggest editing `RESEARCHER.md` by hand.
2. Confirm the folders exist — `Sources/`, `Library/`, `Notes/`, `Notes/Private/`, `Output/`,
   `Library/INDEX.md`, `Library/LOG.md`. Create any that are missing; never overwrite an existing
   `INDEX.md` or `LOG.md`.

## The interview

1. **Your name, and what you do.** A role, a firm, a mandate, or "I invest my own money".
2. **What will you call me?** The researcher's name. Suggest three if they hesitate; never pick one
   for them.
3. **Domains.** The folders `Library/` will be organised by. Offer Finance, Macro, AI, Business,
   Science, and ask for their own. At least one.
4. **How should I speak?** Terse / standard / thorough; which language; challenge or defer.
5. **What do you believe about markets?** Two or three sentences. Offer to save the long version
   as `Notes/how-i-invest.md` in their exact words — never paraphrased — if they say more.
6. **Non-negotiables.** Show KaxaNuk's four defaults (numbers only from the Lab's libraries; the
   hypothesis before the test with every prediction cited; nothing trades from here;
   `Notes/Private/` read only when named). Keep, change, add.
7. **Tag policy.** Strict — a fixed list they give now — or loose — proposed on compile, pruned at
   audit.
8. **Strategies.** Paths to any strategy repositories on this machine built from the KN Research
   Process template, and where each stands. None is a fine answer.

## Write

Show the filled `RESEARCHER.md` in chat, section by section, following the file's existing headings
exactly. Wait for the owner's go. Then write it, and remove the instruction blockquote at the top.
If they asked, write `Notes/how-i-invest.md` with their words verbatim under a single heading.

## Core knowledge

Ask whether to install KaxaNuk's core knowledge — the APM packages in `apm.yml` that teach the KN
Research Process, the Data Curator's calculations and the Lab modules. If yes:

```sh
pip install apm-cli
apm config set target claude
apm install
```

Say that installed skills are discoverable in a **new** session. If `apm` is missing after the
install, say how to add it to the path and stop; do not guess.

## Hand over

Three sentences, in the voice the owner chose: who the researcher is now, what to do first (drop a
source into `Sources/` and run `/compile`), and where the rules live (`AGENTS.md`).
