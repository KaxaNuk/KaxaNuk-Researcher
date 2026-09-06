---
name: query
description: >
  Use this whenever the owner asks what their library says, what they have read about a topic, how
  two sources relate, or what evidence there is for a claim — any factual or comparative question
  that should be answered from Knowledge/, Philosophy/ and Sources/ rather than from general
  knowledge. It walks Knowledge/INDEX.md and the links between articles before reading anything,
  and cites every claim. Do NOT use it for writing code or for questions about files outside the
  library.
argument-hint: "<the question>"
---

# Query — answer from what was read, and say where it came from

The owner built this library so that answers rest on sources they chose. Answering from general
knowledge defeats the point; answering from one article in isolation misses the connections that
are the library's value.

When it is invoked by name, `$ARGUMENTS` is the question.

## Procedure

1. **Index first.** Read `Knowledge/INDEX.md` end to end. Note every article whose one-line
   description bears on the question, in any domain. Never answer from one article in isolation.
2. **Follow the links.** Open those articles and follow the standard markdown links between them
   until the map of what the library holds on this question is complete. Two articles that link to
   each other are one argument; read both. Quote the source's terms where they matter.
3. **Then the owner's voice.** Read the relevant files in `Philosophy/` when the owner's own
   synthesis is more specific than the library, and cite them as the owner's view, distinct from
   the sources'.
4. **Then the raw material,** only if the library is thin: read the source in `Sources/` directly,
   and say the library has no article for it yet.
5. **Answer in chat**, with a standard markdown link to every article and note behind every claim.
   Where sources disagree, say so and show both; a `> [!WARNING]` callout in an article means a
   claim has been superseded — report the newer one. Write to `Projects/` only if the owner asks
   for a file.
6. **Name the gaps.** If the library does not hold what the question needs, say exactly that, and
   suggest the kind of source that would close it. Do not fill a gap from memory without saying you
   did, and never write it into the library during a query.

## Never

- Read `Philosophy/Private/` unless the owner names the file in the question.
- Invent a source, a page or a URL. If it is not in `Knowledge/`, `Philosophy/` or `Sources/`, the
  honest answer is that the library does not know, followed by what the researcher would read to
  find out.
- Modify `Knowledge/`, `Philosophy/` or `Sources/` while answering.
- Quote a performance number that did not come from the Lab's engines.
