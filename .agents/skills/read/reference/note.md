# The note — what `/read` writes, at home and in a strategy

One convention for both repositories, so a note written at home can travel into a strategy and a
strategy's notes read like the researcher's own. It is the KN Research Process note — the convention
in the template's `Bibliotheca/BIBLIOGRAPHY.md` — with the researcher's habits inside it: the
question or claim named first, the source's claims as headings, the implication for the owner under
each as a blockquote, and what it changes at the end.

One note per unit read. A paper is one file. A book is a folder: an `INDEX.md` that holds its table
of contents and what became of each chapter, and one file per chapter read. Nothing is written for
a chapter the owner did not choose.

## Paths and names

```
at home                                                    in a strategy
Knowledge/<Domain>/Author_Year_Title.md                    Bibliotheca/Papers/Author_Year_Title.md
Knowledge/<Domain>/Author_Year_Title/INDEX.md              Bibliotheca/Books/Author_Year_Title/INDEX.md
Knowledge/<Domain>/Author_Year_Title/NN_Chapter_Title.md   Bibliotheca/Books/Author_Year_Title/NN_Chapter_Title.md
```

`Author_Year_Title` is the template's name: the first author's surname — two or three surnames when
there are that many — the year, and the title's first words, joined by underscores, in the source's
own capitals: `Ilmanen_2011_Expected_Returns`, `DeMiguel_Garlappi_Uppal_2009_Optimal_Versus_Naive`.
`NN` is the chapter's number in the book's outline, two digits, so the folder sorts like the book;
`00` is front matter. A chapter file is named by the chapter's own title, the same way:
`03_The_Equity_Premium.md`.

At home, a book folder is the only kind of subfolder a domain has, and its `INDEX.md` the only
per-folder index. A clipping or a transcript — `Sources/Clippings/` at home, `Bibliotheca/Notes/`
in a strategy — is a paper for these purposes; in a strategy its note goes in `Papers/`. In a
strategy the PDF sits beside its note, gitignored; at home it stays in `Sources/`.

## Frontmatter — the template's four fields, and `tags`

```yaml
---
source: https://doi.org/10.1002/9781118467190
citation: Ilmanen, A. (2011). Expected Returns. Wiley. Link checked 2026-09-09.
local_copy: Sources/Books/Ilmanen_2011_Expected_Returns.pdf
read: 2026-09-09, chapters 3 and 4
tags: [expected-returns, risk-premia]
---
```

- `source` — where the work lives outside the repository: a DOI, a URL, a publisher. From the source
  itself — its title page, its header — or from the row in `BIBLIOGRAPHY.md`; never invented.
- `citation` — the reference, with the date the link was last checked.
- `local_copy` — the file read, by path inside this repository, or `none`. At home, the path under
  `Sources/`; in a strategy, the PDF beside the note, gitignored.
- `read` — the date, and what was read: the whole paper, the abstract, the chapters.
- `tags` — by the owner's tag policy in `RESEARCHER.md`. Optional in a strategy.

A chapter note carries the book's `source`, `citation` and `local_copy`; its `read` names the
chapter. Nothing else goes in the frontmatter: the Investment Lab reads these fields.

## A chapter note

```markdown
# Expected Returns — 3. The equity premium

*Chapter 3, pages 45–71, from the extract.*

## Why it is here

Question 2 — *Does the equity premium vary predictably enough to time exposure?* The owner's reason,
one or two lines, in their words.

## <The chapter's first claim, stated as the source states it>

- Dense bullets and tables, in the source's own terms. Time-bound claims carry their date inline.
- Page references as `(p. 52)` — the page markers in the extract are the page numbers.

> **For question 2:** what this claim changes about the owner's question, in one to three sentences.
> This blockquote is the only part of the note that is the researcher's; everything above it is the
> source's.

## <The second claim>

…

> **For question 2:** …

## What it changes

- Three to seven bullets on what this chapter changes for the owner's investing, measured against
  the question it was read for.
- One line on what it does not settle.
```

In a strategy the question is a claim: `## Why it is here` reads *Claim 2 of `OBJECTIVE.md` — its
text — and the owner's reason*; every blockquote reads **For claim 2:** and is about this strategy,
not about finance in general; `## What it changes` is measured against the claim. A note that does
not say what it changes for the strategy is a summary, and summaries are available elsewhere.

Four rules, the template's:

1. **The implication is a blockquote, always.** It is the only part that is ours, and it has to be
   visually separable from what the source said.
2. **A heading states the source's claim, never our verdict.** The verdict lives in the blockquote,
   where it can change when a result moves; a heading carrying a verdict rots silently.
3. **Contradictions stay visible.** When this chapter says the opposite of what an existing note
   claims, the older claim stays and gets a `> [!WARNING]` callout above it naming this note by
   link; when it says the opposite of what the owner believes, the blockquote says so.
4. **Never invent a URL or a page number.** The extract's page markers are the page numbers; a
   reference the chapter gives without a page is quoted without one.

Links to other notes are standard markdown links, relative, inside the same repository — never
across. In a strategy, a home note is named in prose. Match the voice of the notes already there.

## A paper note

The same shape. The provenance line names the whole paper, or the part read — *abstract and
section 4 only* is honest and allowed. The paper's own sections become the claim headings, and a
long paper may have many; a short one may have two. `## Why it is here` and `## What it changes`
stay.

## A book's `INDEX.md`

```markdown
---
source: https://doi.org/10.1002/9781118467190
citation: Ilmanen, A. (2011). Expected Returns. Wiley. Link checked 2026-09-09.
local_copy: Sources/Books/Ilmanen_2011_Expected_Returns.pdf
read: 2026-09-09, chapters 3 and 4
tags: [expected-returns]
---

# Ilmanen (2011) — Expected Returns

Read for question 2 and question 3 — the owner's reason for the book, in their words.

| # | Chapter | Pages | Status | Question | Note |
| --- | --- | --- | --- | --- | --- |
| 1 | Introduction | 1–24 | skipped | | |
| 2 | Whetting the appetite | 25–44 | skimmed | Q2 | a survey of the book's own claims; nothing chapter 3 does not carry |
| 3 | The equity premium | 45–71 | read | Q2 | [03_The_Equity_Premium.md](03_The_Equity_Premium.md) |
| 4 | … | 72–98 | to come | Q3 | |

## What this book does not settle

One to three lines, written after the chapters read; revised as more are.
```

Status vocabulary, so it means the same in every book: **read** — a note exists; **skimmed** — the
extract was read, no note, one line in the Note column says what the chapter holds and why it was
passed over; **skipped** — not read, by the owner's choice, title and pages only; **to come** —
chosen but left for a later run. In a strategy the Question column holds the claim — *C2*. `read`
in the frontmatter names the latest run that touched the book.

## What the indexes show

At home, `Knowledge/INDEX.md`: one line per paper; one line per book, linking its `INDEX.md` and
saying which chapters were read of how many; beneath it, one indented line per chapter read.

```markdown
## Finance

- [Ilmanen (2011) — Expected Returns](Finance/Ilmanen_2011_Expected_Returns/INDEX.md) — read for
  Q2 and Q3: chapters 3 and 4 of 12
  - [3. The equity premium](Finance/Ilmanen_2011_Expected_Returns/03_The_Equity_Premium.md) — the
    sentence that says what the chapter settles
- [Harvey & Liu (2015) — Backtesting](Finance/Harvey_Liu_2015_Backtesting.md) — the sentence that
  says what the paper settles
```

In a strategy, `Bibliotheca/BIBLIOGRAPHY.md` is curated by hand and is not rebuilt. A note adds one
row under the part the source bears on — or, where the source was already listed as a lead, keeps
its row and loses its *No note yet* — with what it bears on, the claim, and the link:

```markdown
| Ilmanen (2011) — *Expected Returns* | the size and cyclicality of the equity premium, claim 2. Chapters 3 and 4 read: [note](Books/Ilmanen_2011_Expected_Returns/INDEX.md) |
```

## Carrying a home note into a strategy

When the home library already holds a note on a source the strategy needs, the PDF is not read
twice. The source's part travels — the claim headings and their bullets, `source` and `citation`;
`local_copy` becomes the strategy's copy or `none`; `read` keeps the date and what was read, and
says *from the researcher's library*. Everything that is the owner's is written anew, for this
strategy's claims: `## Why it is here`, every blockquote, `## What it changes`. No link points home.

## Syntheses

An idea that spans chapters or sources is not a note; it is a synthesis. At home it is written under
the domain folder only when the owner asks for one — in chat, or through `/query` — and it links
every note it rests on. In a strategy the synthesis is `OBJECTIVE.md` itself, its claims citing the
notes. A synthesis cites notes; notes cite sources.
