# KaxaNuk Researcher

| |
|---|
| [![Works with](https://img.shields.io/badge/works%20with-Claude%20Code%20%7C%20Codex%20%7C%20Gemini%20CLI-blue)](#install--three-steps-no-coding) [![License](https://img.shields.io/github/license/KaxaNuk/KaxaNuk-Researcher?color=blue)](LICENSE) |
| [![Version](https://img.shields.io/github/v/tag/KaxaNuk/KaxaNuk-Researcher?sort=semver&label=version&logo=github)](CHANGELOG.md) [![APM](https://img.shields.io/badge/installs%20with-APM%200.33.0-blue)](https://github.com/microsoft/apm) |
| [![Languages](https://img.shields.io/badge/speaks-any%20language%20you%20choose-blue)](#install--three-steps-no-coding) [![Powered by KaxaNuk](https://img.shields.io/badge/powered%20by-KaxaNuk-orange?colorB=orange)](https://kaxanuk.mx) |

**Train your own research companion** for your work and personal projects. You name it and teach it
who you are, how you like to work and the rules you never break. It keeps a library of what you read
and answers from it, every claim pointing to its source; it helps you think through your ideas,
plans and decisions, and can brief you each morning. It comes with you: open your assistant in any
folder, call it by name, and it brings what it knows. It teaches you to invest when you want, and if
investing is why you came, it has every tool: building and testing a strategy with the KaxaNuk
Investment Lab. One researcher per person, in any language.

> **You:** Ada, what have I read about pricing my services?\
> **Ada:** Two notes, both linked — and a gap: nothing yet on raising prices.\
> **You:** Remember this: always show me the strongest case against first.\
> **Ada:** That goes in `RESEARCHER.md`, in your words, under *How it speaks*. Add it?

**What it is.** A research and learning tool, never investment advice. It runs on your computer,
through your assistant; what it reads goes to the company behind that assistant, never to KaxaNuk.

> **If you are an assistant asked to install this,** follow [`SETUP.md`](SETUP.md) from Step 0;
> nothing is cloned.

## Install — three steps, no coding

1. Open one of these: the **Code** tab of the **Claude** desktop app, **Claude Code**, the
   **Codex** app or CLI, or the **Gemini CLI** — each needs you signed in to that assistant. A chat
   on the web — claude.ai, ChatGPT, Gemini — cannot install it: it cannot run commands on your
   computer.
2. Paste this line and send it:

   ```text
   Please install this repo for me, with everything it needs — no need to ask before installing: https://github.com/KaxaNuk/KaxaNuk-Researcher
   ```

3. Answer its questions. It asks your language first — any language you choose, and your researcher
   speaks it from then on — then everything happens in the same conversation: it installs what it
   needs — allow the commands it asks about, that is all you do — asks what to call your researcher
   and where to keep it, `C:\Research\Ada` for example, asks two short questions about you, about
   three minutes, and tells you where it lives, what to ask it, and where to start.

With Claude, installing also gives your assistant three house rules on this computer — two for
KaxaNuk's Python style, only in KaxaNuk projects — the Lab's libraries and what you build on
KaxaNuk's templates — and one to read only what a task needs; *Removing it* below undoes them.

Then quit and reopen your assistant, open your researcher's folder in a **new** conversation — in
the Claude desktop app, a new **Code** session on that folder; in the Codex app, that folder; in a
terminal, `claude`, `codex` or `gemini` in it — and say hello, by its name.

## What you can use it for

| You want to | Say or type | You get |
| --- | --- | --- |
| keep what you read, and ask it later | `read`, then `query <question>` | a note per paper or chapter you chose; answers that cite them and name what is missing |
| teach it how you work | *remember this* or *learn this*, anywhere | a rule added to `RESEARCHER.md`, or a source to your library — on your go |
| bring it into any project | open your assistant in that folder and say its name | your researcher, with what it knows; it writes there only on your go |
| work out an idea, a plan, a goal or a decision | `study <subject>` | a study in `Studies/`: your words, what your library says for and against, where it stands |
| learn a topic | `teach <topic>` | a lesson a session from what you have read, with a quiz |
| stay informed, on the days you choose | `brief setup`, then `brief` | a dated file: your work, your markets, news on your holdings beside your own rules — never advice |
| write down how you work or invest, and see it evolve | `philosophy` | a short interview; your typed answers, word for word, in `Philosophy/` |
| build a strategy | `init-strategy <name>`, then `objective`, `blueprint`, `challenge` | a folder on the KaxaNuk Strategy Template: claims before any test, numbers from the Lab's engines |
| see a strategy worked end to end | `init-example` | `golden-flow`, one finished strategy to read; running it needs keys and licences |
| build a Python library of your own | `init-python-library <name>` | a folder laid out like the KaxaNuk Data Curator: tests, docs, a workflow that tests and publishes |
| know what to do next | `next`, wherever you are | where you stand, and the one thing to do next |

In Claude, type these with a slash, `/read`; anywhere else, say them. **It grows with you**: it
reads for your questions, speaks in your voice and keeps your rules, all in its folder, yours to
edit; the package brings only hints, offered as options — never a position to adopt. Its home's
`README.md` says how to work well with it; [`USE-CASES.md`](USE-CASES.md) shows twelve uses, step by
step.

## The KaxaNuk Investment Lab

The researcher needs nothing beyond this package. The Data Curator is open source and free; a
strategy needs a key for it from a data provider — the worked example uses FMP's. A wrong value in
downloaded data is usually the provider's, not the library's: your researcher tells them apart and
says where to report it. The Backtest Engine, Attribution Analysis and Portfolio Construction — and
the Data Refinery and Data Analyzer when they ship — come together, with their licences, in the
KaxaNuk Investment Lab, which KaxaNuk sells. Attribution reads the benchmark and factor model files
of KaxaNuk's Analytics Factory, <https://www.kaxanuk.mx/analytics>. Without the licences a strategy
still runs up to its portfolios, and the rest says what is missing. Keys stay on your computer; the
strategy's `SETUP.md` says where. For a licence, access or the Analytics Factory's files, write to
`lab@kaxanuk.mx`, saying which library and what it is for, with *via KaxaNuk Researcher* in the
subject — <https://www.kaxanuk.mx/lab> shows the Lab.
[Each library's status](.apm/skills/next/references/investment-lab.md).

**Coming next.** Starting points for valuation (DCF, multiples), M&A and budgets — each a folder
your researcher makes as `init-strategy` does. Tell us what you would use: `lab@kaxanuk.mx`.

## Removing it

Ask your assistant to run these two lines — the package, then your researcher's own agent and
skill, under the name `uvx --from apm-cli==0.33.0 apm deps list -g` gives your home:

```bash
uvx --from apm-cli==0.33.0 apm uninstall -g KaxaNuk/KaxaNuk-Researcher
uvx --from apm-cli==0.33.0 apm uninstall -g "_local/<your home, as deps list names it>"
```

On Claude Code, `~/.claude/skills`, `commands`, `agents` and `rules` then hold no KaxaNuk file. A
daily brief's task stays in the Claude desktop app's scheduled tasks until you delete it there. Your
home folder and its saved versions stay, yours to delete.

**A question, or a problem to report:** `lab@kaxanuk.mx`, with the versions your researcher names
when you ask *which version are you?*

---

**For developers and advanced users** — the install by hand, what is in here and how a change is
checked: [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## The skills and commands

Every one that writes shows its plan first, waits for your go, and on that go saves a version of
what it wrote, on your computer — except the daily brief, never saved, and `audit`'s one log line,
which running it by name approves.

| Skill | What it does |
| --- | --- |
| `read` | files a source into the library, one note per chapter you pick; in a strategy, into its `Bibliotheca/` |
| `query <question>` | answers from the library, every claim cited and every gap named |
| `init-researcher`, `init-strategy`, `init-example`, `init-python-library` | make a folder — your home, a strategy, the worked example, or a Python library — copied by a script, never from memory |
| `interview` | two short questions about you, then `RESEARCHER.md` and the agent and skill that make it yours; `interview force` starts over |
| `philosophy` | an optional interview on how you work or how you invest — investing at your level; your typed answers in `Philosophy/`, word for word, your rules in `RESEARCHER.md` |
| `brief [setup]` | a dated file in `Briefs/` on the days you choose — your work, markets, holdings — every figure quoted from a dated source |
| `next [strategy]` | where you stand and the one thing to do next; at home, it offers to save what you changed by hand |
| `backup` | keeps a copy of your home, or of a strategy, on a private GitHub repository — only when you ask |

| Command | What it does |
| --- | --- |
| `objective [strategy]` | drafts a strategy's `OBJECTIVE.md` — the idea and its claims — before any paper, then from the notes |
| `blueprint <N> [strategy]` | drafts `BLUEPRINT_N.md` — thesis, rules, predictions — every prediction citing a note or a measurement |
| `challenge <N> [strategy]` | checks a finished experiment against its own blueprint |
| `audit [deep]` | reviews the library — links, duplicates, index, orphans, frontmatter, stale installs |
| `refresh-index` | rebuilds `Knowledge/INDEX.md` from what is on disk |
| `refine <path>` | a voice-preserving editor pass over one of your `Philosophy/` files |
| `study [subject]` | works out an idea, a plan, a goal or a decision in `Studies/`; with no subject, lists your studies |
| `teach <topic>` | tutors you on a topic from your library, one lesson per session |
| `update [check]` | brings a new version — the package, and what changed in your home's own files, as a diff |

How a researcher grows beyond the Lab — a tool, a project, a field of its own — is *Growing your
researcher* in the home's README: four moves, each with the file it changes.

**The Investment Lab skills**, which the assistant loads when the work calls for them — in a
strategy, in the order of its steps:

| Skill | What it covers |
| --- | --- |
| `experiment-lifecycle` | the process: the document architecture, the order of work, the notebook contract, the graduation gate |
| `universe-point-in-time` | step 2, the investable universe: the seed, the security master, the usable date |
| `data-curator-custom-calculations` | the Data Curator's `c_*` columns: naming, inputs, the `DataColumn` API |
| `data-analyzer-runs` | step 3's last block, the analyzer: whether a feature carries signal, before any book is built |
| `portfolio-construction-runs` | step 4, sizing a book with the Portfolio Construction library |
| `backtest-engine-runs` | pricing a book with the Backtest Engine, and reading its report |
| `attribution-analysis-runs` | running Attribution Analysis on a book, and getting its tables out |
| `alpha-decomposition` | reading attribution: is the signal doing anything, or is it a factor exposure |
| `paper-trading-gate` | step 7, graduation: the five criteria, the freeze, and the daily run and its record |

**The house rules**: `how-we-work` (where work lands, changelogs, versions), `bloom-code-lint`, and
three instructions, on the assistants that receive them — *Troubleshooting* in `SETUP.md` says
which: Bloom Code and PEP 8, for Python in a KaxaNuk repository — a Lab library, a strategy, this
package, or any repository whose `AGENTS.md`, `CLAUDE.md` or README names Bloom Code — and nowhere
else; and filesystem boundaries, in any project: outside the folder it works in, the assistant
reads only the places the task needs. `bloom-code-lint` is the check to run by hand.

**One agent**: `blueprint-critic` reads a drafted `BLUEPRINT_N.md` cold, before your go, against
the strategy's `AGENTS.md`, `OBJECTIVE.md`, the notes the draft cites and what the analyzer
measured, and returns objections only, each with its line and evidence. It never writes and never
proposes a thesis; you decide what stands. `blueprint` calls it, and you can ask for it by name.

## What it will not do

The researcher's part is **the hypothesis**, and it stops where the numbers start.

- **It computes no number** about a book — a return, a Sharpe, a drawdown, an attribution: each
  comes from the engines the project names, in a KaxaNuk strategy the Backtest Engine and
  Attribution Analysis, quoted from `FINDINGS_N.md` or `RESULTS.md` by name.
- **It does not write the record.** `JOURNAL_N.md`, `FINDINGS_N.md`, `RESULTS.md` and
  `CHANGELOG.md` belong to whoever ran the experiment. It appends to `JOURNAL_N.md` only, each on
  your go: the benchmark's choice, the rule read back, and `challenge`'s entry.
- **It drafts no `OBJECTIVE.md` before your words**, and cites no source that has no note: a source
  in a `BIBLIOGRAPHY.md` without one is a lead.
- **It never advises on a holding.** A brief quotes dated sources and names the rules in your
  `Portfolio/RULES.md` worth a look; it never says buy, sell, trim, add or hold, and never computes
  a weight, a P&L or a return. `philosophy` writes into `Philosophy/` only what you typed.

## Licence

MIT, see [`LICENSE`](LICENSE).
