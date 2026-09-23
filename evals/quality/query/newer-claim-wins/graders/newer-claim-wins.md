---
type: llm
focus: last_message
---
The answer is to "Do my sources agree on how momentum ends?", from a library that holds two notes.
Moskowitz 2012 (Time Series Momentum, read 2026-09-01) says "The effect partly reverses after a
year (p. 240)": a slow give-back. Daniel 2016 (Momentum Crashes, read 2026-09-10) says "Momentum
crashes after market rebounds (p. 222)", and carries a warning that it is "Newer than Time Series
Momentum on the size of the reversal: it measures a crash after market rebounds rather than a slow
give-back." PASS only if every line below holds; FAIL if any one does not.

- Both notes are named: Moskowitz 2012 (or Time Series Momentum) and Daniel 2016 (or Momentum
  Crashes).
- The disagreement is stated: the sources do not fully agree, the older describing a slow partial
  reversal after about a year and the newer an abrupt crash after market rebounds. An answer that
  says the sources simply agree fails.
- The newer note, Daniel 2016, is reported as the library's current view on how momentum ends,
  with the warning that flags it as superseding Moskowitz 2012 on this point; an answer that treats
  the two as equal weight, or prefers the older, fails.
