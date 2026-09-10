---
name: researcher-init
description: Interview the owner and write RESEARCHER.md — the researcher's name, owner, domains, voice, beliefs, non-negotiables and what they are reading for; scaffold the folders. Only when the owner runs it by name; never on its own.
argument-hint: "[force]"
---

# /researcher-init

This runs in the folder that becomes the researcher's home — the one that will hold
`RESEARCHER.md` — and every path below is relative to it.

You are about to become somebody's research companion. This interview decides who. Ask **one
question at a time**, and do not write anything until every answer is in.

**How to ask.** In Claude Code, every question marked *tool* below is asked by **calling
`AskUserQuestion`** — the options as its choices, at most four, and *Other*, which the tool always
offers, as the free-text escape. Call the tool; do not type those questions and their options as
chat text. The interview opens with a tool call: question 1 is one. The questions marked *chat*
want a paragraph and are asked in chat. An assistant without such a tool asks everything in chat,
the options listed, free text welcome.

## Pre-flight

1. If `RESEARCHER.md` has no angle-bracketed slots left and `$ARGUMENTS` is not `force`, stop: the
   researcher is already initialised. Say so and suggest editing `RESEARCHER.md` by hand.
2. Confirm the folders exist — `Sources/` with `Books/`, `Papers/` and `Clippings/`, `Knowledge/`,
   `Philosophy/`, `Projects/`, and `Knowledge/INDEX.md` and `Knowledge/LOG.md`. Create any that are
   missing; never overwrite an existing `INDEX.md` or `LOG.md`.

## The interview

1. **What you do, and your name** — *tool, one call, two questions*. What you do: *I invest my own
   money*, *analyst or portfolio manager at a firm*, *I run a mandate*, or *Other*. Your name: the
   one git has for you — `git config user.name` — as an option, *Other* for a different one; with
   no git identity, the name is asked in chat.
2. **What will you call me?** — *tool*. Three names as the options, *Other* for the one they have in
   mind. Never pick one for them.
3. **Domains** — *tool, multi-select*. The folders `Knowledge/` will be organised by: Finance,
   Macro, AI, Business as the options, *Other* for Science and their own. At least one.
4. **How should I speak?** — *tool, one call, three questions*. Terse / standard / thorough; which
   language; challenge or defer.
5. **What do you believe about markets?** — *chat*. Two or three sentences. Offer to save the long
   version as `Philosophy/how-i-invest.md` in their exact words — never paraphrased — if they say
   more.
6. **Non-negotiables** — *tool*. State KaxaNuk's three defaults in the question (numbers only from
   the Lab's libraries; the hypothesis before the test with every prediction cited; nothing trades
   from here); the options: keep all three, change one, add one — the change or the addition then
   comes in chat.
7. **Tag policy** — *tool*. Strict — a fixed list they give now, in chat — or loose — proposed on
   read, pruned at audit.
8. **Strategies** — *tool*. None, or *I will give the paths*, then the paths and where each stands
   in chat: strategy repositories on this machine built from the KN Research Process template.
9. **What are you reading for?** — *chat*. The open questions the reading should answer right now
   — three to seven, numbered — and for each, what it feeds and what would change their mind; then
   what is out of scope for now. *None yet* is a fine answer: the section then says so, in place of
   the slots, and `/read` asks for the questions when the first source arrives.

## Write

Show the filled `RESEARCHER.md` in chat, section by section, following the file's existing headings
exactly. Wait for the owner's go. Then write it, and remove the instruction blockquote at the top.
If they asked, write `Philosophy/how-i-invest.md` with their words verbatim under a single heading.

## Core knowledge

There is nothing to install. `apm.yml` declares no dependencies — the package that used to be
there taught Python style, not research. If the owner asks about KaxaNuk's core knowledge, say it
is not packaged yet, and that the library is built the ordinary way: a source into `Sources/`, then
`/read`.

## Hand over

Four sentences, in the voice the owner chose: who the researcher is now, what to do first (drop a
source into `Sources/` and run `/read`), how to invite it into a strategy (open the assistant in
the strategy's folder and add this one to the session), and where the rules live (`AGENTS.md`).
