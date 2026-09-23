---
type: llm
focus: last_message
---
The answer is to "What does my library say about time-series momentum?", asked in a researcher's
home whose library holds exactly two notes, quoted in full below as the home holds them. The
home's `RESEARCHER.md` lists two open questions: "1. Do trends in prices persist long enough to
trade after costs?" and "2. What ends a trend, and can it be seen coming?". `Knowledge/INDEX.md`
links both notes. `Philosophy/HOW-I-INVEST.md` is the unfilled template, and `Sources/Papers/`
holds no PDF. PASS only if every line below holds; FAIL if any one does not.

`Knowledge/Markets/Moskowitz_2012_Time_Series_Momentum.md`:

````markdown
---
source: "Time Series Momentum"
citation: "Moskowitz, T., Ooi, Y. H., and Pedersen, L. H. (2012). Journal of Financial Economics 104(2), 228-250."
local_copy: ../../Sources/Papers/Moskowitz_2012_Time_Series_Momentum.pdf
read: 2026-09-01
---

# Time Series Momentum

Read from the PDF, whole; pages are the journal's.

## Why it is here

Question 1: do trends persist long enough to trade after costs.

## Past twelve-month returns predict the next month in 58 futures markets (p. 229)

> The persistence is the premise of a trend rule; it is measured, not assumed.

> [!WARNING]
> [Momentum Crashes](Daniel_2016_Momentum_Crashes.md) is newer on the size of the reversal: it
> measures a crash after market rebounds rather than a slow give-back. The claim below stays as
> this paper states it.

## The effect partly reverses after a year (p. 240)

> A holding period longer than a year gives back part of the gain.

## What it changes

Question 1 has one measured answer, on futures, not on single stocks.
````

`Knowledge/Markets/Daniel_2016_Momentum_Crashes.md`:

````markdown
---
source: "Momentum Crashes"
citation: "Daniel, K., and Moskowitz, T. J. (2016). Journal of Financial Economics 122(2), 221-247."
local_copy: ../../Sources/Papers/Daniel_2016_Momentum_Crashes.pdf
read: 2026-09-10
---

# Momentum Crashes

Read from the PDF, whole; pages are the journal's.

## Momentum crashes after market rebounds (p. 222)

> A trend rule is most exposed right after a bear market ends.

## What it changes

Question 2 has a first answer: the rebound after a decline ends a trend abruptly.
````

- The answer links the notes it draws on, as markdown links to paths ending in
  `Moskowitz_2012_Time_Series_Momentum.md` or `Daniel_2016_Momentum_Crashes.md`; a link at the
  head of a paragraph or a group of lines covers the claims under it.
- Every claim the answer attributes to the library, to a note or to the owner's questions is
  supported by the text quoted above: the front matter, the headings and their page numbers, the
  blockquotes, the *Why it is here* and *What it changes* lines, and the warning. A paraphrase is
  supported when it says what the quoted text says; a page, a number, a market count or a finding
  the quoted text does not hold is not.
- Anything the quoted text does not hold (other papers, other asset classes, lookback lengths,
  Sharpe ratios, mechanisms, what a paper is "really" about) is either absent or plainly marked as
  not coming from the library, such as "a lead from the reading map, not in your library" or "from
  memory, not from your library". Remarks about the home itself (the unfilled `Philosophy/` file,
  the missing PDFs, a section a note lacks) are not claims about momentum and do not fail this line.
