---
name: library-query
description: >
  Use this skill whenever the owner asks what their library says, what they have read about a
  topic, how two sources relate, or what evidence there is for a claim — any factual or comparative
  question that should be answered from Knowledge/, Philosophy/ and Sources/ rather than from
  general knowledge. It walks Knowledge/INDEX.md and the links between articles before reading
  anything, and cites every claim. Do NOT use it for writing code, for slash commands, or for
  questions about files outside the library.
metadata:
  version: 0.1
---

# Library query — answer from what was read, and say where it came from

The owner built this library so that answers rest on sources they chose. Answering from general
knowledge defeats the point; answering from one article in isolation misses the connections that are
the library's value.

## Procedure

1. **Index first.** Read `Knowledge/INDEX.md` end to end. Note every article whose one-line
   description bears on the question, in any domain.
2. **Follow the links.** Open those articles and follow the standard markdown links between them
   until the map of what the library holds on this question is complete. Two articles that link to
   each other are one argument; read both.
3. **Read the notes.** Check `Philosophy/` for the owner's own view on the subject and cite it as
   theirs, separately from the sources.
4. **Answer in chat.** Every claim carries a link to the article or note behind it. Where sources
   disagree, say so and show both; a `> [!WARNING]` callout in an article means a claim has been
   superseded — report the newer one.
5. **Name the gap.** If the library does not hold what the question needs, say exactly that, and
   suggest what to put in `Sources/`. Do not fill the gap from memory without saying you did, and
   never write it into the library during a query.

## Never

- Read `Philosophy/Private/` unless the owner names the file.
- Invent a source, a page or a URL.
- Modify `Knowledge/`, `Philosophy/` or `Sources/` while answering.
- Quote a performance number that did not come from the Lab's engines.
