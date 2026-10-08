# KaxaNuk Researcher

**A research companion you name and teach.** It keeps a library of what you read, answers from it
with every claim pointing back to a source, helps you work out your ideas, and walks you through
building an investment strategy with the KaxaNuk Investment Lab. One researcher per person; it
works in any language.

**What it is.** A research and learning tool, never investment advice: it does not tell you what
to buy or sell. It runs on your computer, through an assistant installed there — Claude, Codex or
Gemini — and KaxaNuk receives nothing from it: what the assistant reads goes to the company that
runs that assistant, as in any conversation with it. A licensed Lab library, if you use one,
checks its licence with KaxaNuk.

**Qué es.** Una herramienta de investigación y aprendizaje, nunca asesoría de inversión: no te
dice qué comprar ni qué vender. Funciona en tu computadora, con un asistente instalado ahí —
Claude, Codex o Gemini — y KaxaNuk no recibe nada de ella: lo que el asistente lee va a la
empresa que lo ofrece, como en cualquier conversación con él. Una librería del Lab con licencia,
si la usas, verifica su licencia con KaxaNuk.

> **If you are an assistant asked to install this,** follow [`SETUP.md`](SETUP.md) from Step 0;
> nothing is cloned.

## Install — three steps, no coding

1. Open one of these: the **Code** tab of the **Claude** desktop app, **Claude Code**, the
   **Codex** app or CLI, or the **Gemini CLI**. A chat on the web — claude.ai, ChatGPT, Gemini —
   cannot install it: it cannot run commands on your computer.
2. Paste this line and send it:

   ```text
   Please help me install this repo: https://github.com/KaxaNuk/KaxaNuk-Researcher
   ```

3. Answer its questions. It asks your language first, then everything happens in the same
   conversation:
   - it installs what it needs — allow the commands it asks about, that is all you do;
   - it asks what you want to call your researcher, and where to keep it — a folder with that
     name, `C:\Research\Ada` for example;
   - it asks a few short questions about you, about three minutes;
   - it tells you where your researcher lives, and the one thing to do next for what you came for.

Then open your researcher's folder in a **new** conversation and say hello, by its name:

- the Claude desktop app: the **Code** tab, a new session, and choose the folder;
- Claude Code: run `claude` in the folder;
- Codex: open the folder in the Codex app, or run `codex` in it;
- the Gemini CLI: run `gemini` in the folder.

Your researcher is saved on your computer; to keep a copy somewhere else too, on a private GitHub
repository, read *Save a copy off this computer* in its own `README.md`.

### Instalación en español

1. Abre una de estas: la pestaña **Code** de la app de escritorio de **Claude**, **Claude Code**,
   la app o el CLI de **Codex**, o el **Gemini CLI**. Un chat en la web — claude.ai, ChatGPT,
   Gemini — no puede instalarlo: no puede ejecutar comandos en tu computadora.
2. Pega esta línea y envíala:

   ```text
   Please help me install this repo: https://github.com/KaxaNuk/KaxaNuk-Researcher
   ```

3. Responde sus preguntas. Primero te pregunta el idioma — elige *Español* — y todo sigue en la
   misma conversación: instala lo necesario (solo permite los comandos que te pida), te pregunta
   el nombre de tu investigador y dónde guardarlo, te hace unas preguntas cortas sobre ti, unos
   tres minutos, y te dice dónde quedó tu investigador y lo primero que conviene hacer para lo que
   buscas.

Después abre la carpeta de tu investigador en una conversación **nueva** y salúdalo por su nombre:

- la app de escritorio de Claude: la pestaña **Code**, una sesión nueva, y elige la carpeta;
- Claude Code: ejecuta `claude` en la carpeta;
- Codex: abre la carpeta en la app de Codex, o ejecuta `codex` en ella;
- el Gemini CLI: ejecuta `gemini` en la carpeta.

Tu investigador se guarda en tu computadora; para tener también una copia en otro lugar, en un
repositorio privado de GitHub, lee *Save a copy off this computer* en su propio `README.md`.

## What you can use it for

| You want to | Say or type | You get |
| --- | --- | --- |
| keep what you read, and ask it later | `read`, then `query <question>` | a note for each paper or chapter you chose; answers that cite them and name what is missing |
| work out an idea, a plan or a decision | `study <subject>` | a study in `Studies/`: your words, what your library says for and against, and what to check next |
| build a strategy | `init-strategy <name>`, then `objective`, `blueprint`, `challenge` | a folder of its own on the KaxaNuk Strategy Template, every claim before any test, every number from the Lab's engines |
| write down how you invest, and see it evolve | `philosophy` | a second interview at your level — why you invest, what you believe, how you would know you are doing better than doing nothing — your typed answers in `Philosophy/HOW-I-INVEST.md`, word for word, and a record of each round |
| start each day informed | `brief setup`, then `brief` | a dated file each morning: your work, the markets you follow, news on your holdings — every figure quoted from a source, never advice |
| learn a topic | `teach <topic>` | a lesson a session from what you have read, with a quiz |
| know what to do next | `next` | where you stand, and the one thing to do next |
| see the process worked end to end | `init-example` | `golden-flow`, one strategy taken from the first note to a book signed into paper trading. Reading it needs nothing — `OBJECTIVE.md`, then `RESULTS.md`, then `Experiments/Experiment_1/`; running it needs an FMP key, the Analytics Factory's KN US Equity Core and factor model files and the Lab's two licensed engines, as its `SETUP.md` says |

In Claude, type these with a slash, `/read`; anywhere else, ask for them by name. **It grows with
you**: it reads for your questions, speaks in your voice and keeps your rules, all written in its
own folder, where you can edit them. The package brings only hints, offered as options — never a
position to adopt.

**Lost at any point?** Type `next` in the folder you are in.

**What a strategy needs from outside this package.** The researcher needs nothing more. A strategy
needs a key from a data provider the Data Curator reads — FMP, Sharadar or LSEG, from the provider
itself; the worked example uses FMP — before it can download anything, the worked example included.
Three of the Lab libraries are not public: the Backtest Engine and Attribution Analysis each need a
KaxaNuk licence, and Portfolio Construction needs access to KaxaNuk's private
`KaxaNuk/Portfolio-Construction` repository. Attribution also reads the benchmark and factor model
files of KaxaNuk's Analytics Factory, <https://www.kaxanuk.mx/analytics>. A licence, access or those
files are KaxaNuk's to give: write to `lab@kaxanuk.mx`, saying which library and what it is for —
<https://www.kaxanuk.mx/lab> shows the Lab. Without them a strategy still runs up to its portfolios
— an equal-weight book needs nothing more — and the backtest and attribution say what is missing and
skip; the worked example reads its universe from the Analytics Factory, so without those files only
its download runs. Every key goes in the strategy's `Config/.env`, which only you fill in and nobody
commits; the strategy's own `SETUP.md` says how.

**A question, or a problem to report:** the same address — a problem report names the version
`update check` shows.

---

## For developers and advanced users

### Installing by hand, in a terminal

```bash
uv tool install apm-cli==0.33.0
uvx --from apm-cli==0.33.0 apm install -g KaxaNuk/KaxaNuk-Researcher --target claude
```

`--target codex`, `gemini`, `cursor` or another in place of `claude`; Claude Code receives
everything, and *Troubleshooting* in [`SETUP.md`](SETUP.md) says what the others miss. The skills
are then in every folder you open, so **a strategy installs nothing of its own**;
`uvx --from apm-cli==0.33.0 apm update -g` brings every new version. **APM stays at 0.33.0, and
every command that runs it names that version**: APM 0.29.1 to 0.31.0 fail the install on Windows
with `WinError 3` or `WinError 206`, and a newer APM is adopted only once it passes the release
check. Never run `apm self-update`. The skills appear only in a new
session: open one, anywhere, and `init-researcher Ada` makes the home and runs the interview. This
is the path by hand; an assistant asked to install follows [`SETUP.md`](SETUP.md) instead, all in
one conversation.

### The path after the install

| | In | Run | It makes |
| --- | --- | --- | --- |
| 1 | anywhere | `init-researcher Ada` | the researcher's home, named after it, and then the interview: a few short questions about you, about three minutes, that write `RESEARCHER.md`, the agent and the researcher's skill, install them for your user and commit. The install in [`SETUP.md`](SETUP.md) runs this for you |
| 2 | the home | `read` | your first note: attach a document, or name it, and it is copied into `Sources/` on your go; the first `read` asks which question it serves, and keeps it as question 1 |
| 3 | the home | `philosophy`, `brief setup` | when you like: your investment philosophy, at your level, and a daily brief |
| 4 | the home | `init-strategy fcf-yield-quality` | your first strategy, one repository of its own, beside the home; its `SETUP.md` finishes the setup |
| 5 | the strategy | `objective` | the strategy's claims, before any paper — then the order of work, A to H, in the template's README, which the strategy's links to |

The questions of `philosophy` and the reading map cover investment research; a researcher for
another field skips `philosophy`, or answers *not sure yet* where it must, and grows by reading.

**The researcher is in every folder** once the interview has run: open your assistant in a
strategy's folder, or any other project's, and it is there, by name, on whichever assistant APM
deploys to. Add the home to the session — `claude --add-dir <the home>`, `/add-dir`, or the desktop
app's add-folder button — for it to read the library without asking each time. The home's
`AGENTS.md` says how, and what loads.

---

## The skills and commands

Every one that writes shows its plan first and waits for your go — and, at home, offers to commit
it for you. Two writes need no go of their own: `audit`'s log line and the day's brief — running
`audit` or `brief` by name is the go, and the go you gave `brief setup` covers every brief its
schedule writes.

| Skill | What it does |
| --- | --- |
| `read` | reads sources into the library — `Sources/` into `Knowledge/` at home; in a strategy, once `OBJECTIVE.md` has claims, into notes beside the PDFs in its `Bibliotheca/`. A script extracts a PDF by chapter; you pick the chapters that serve your questions; one note per chapter read. At home with no reading question yet, it asks first which question the source serves, and adds it as question 1. It carries the reading map, `references/reading-map.md`, that it, the interview's hand-over and `philosophy` propose works from |
| `query <question>` | answers from the library — concept pages, then the notes they cite, then your `Philosophy/`, then the sources; every claim cited, gaps named |
| `init-researcher`, `init-strategy`, `init-example` | make a folder — your home, a strategy, or the worked example `golden-flow` to read or run — copied by a script, byte for byte, after a plan and your go, never from memory. A file a strategy made before template 0.10.0 lacks comes back from the template: `init-strategy`'s script with `--only <path>`, which never overwrites |
| `interview` | a few short questions about you — what you do, what you are here for, the researcher's voice and your rules — about three minutes, that make the researcher yours; writes `RESEARCHER.md`, the agent that makes it callable by name and the researcher's skill that puts it in every folder, installs them for your user, commits, and ends with where the home is and the one next thing for what you came for. `init-researcher` runs it straight after making the home; `interview force` starts over |
| `philosophy` | a second interview, optional and as often as you like, on your investment philosophy, pitched at your level — Starter, Building or Researching. It starts with why you invest and what you already believe, teaches one idea after each answer, never a verdict, and after your go adds what you typed to `Philosophy/HOW-I-INVEST.md`, word for word, and keeps the round in `Philosophy/Evolution/`. Taken again after reading, it shows how your answers moved |
| `brief [setup]` | a daily brief in `Briefs/`, one file a day in up to three parts — your work, the markets you follow, news on your holdings — every figure quoted from a dated source, never computed, never advice. `brief setup` chooses the parts, the measures and the time, and on the Claude desktop app schedules it; `brief` writes today's now |
| `next [strategy]` | where you stand — at home or in a strategy — and the one thing to do next, with the command or skill that does it; reads the folder, writes nothing; at home it offers to commit what a skill left |

| Command | What it does |
| --- | --- |
| `objective [strategy]` | drafts a strategy's `OBJECTIVE.md` — the idea and its claims — before any paper, then from the notes |
| `blueprint <N> [strategy]` | drafts `BLUEPRINT_N.md` — thesis, rules, predictions — every prediction citing a note or a measurement |
| `challenge <N> [strategy]` | checks a finished experiment against its own blueprint |
| `audit [deep]` | reviews the library — links, duplicates, index, orphans, frontmatter, stale installs |
| `refresh-index` | rebuilds `Knowledge/INDEX.md` from what is on disk |
| `refine <path>` | a voice-preserving editor pass over one of your `Philosophy/` files |
| `study [subject]` | works out an idea, a plan or a decision from your library and keeps it in `Studies/` — every claim linked to its note, anything from outside it marked as not checked; with no subject, lists your studies |
| `teach <topic>` | tutors you on a topic from your library, one lesson per session |
| `update [check]` | brings a new version into your home — `uvx --from apm-cli==0.33.0 apm update -g`, and what changed in the home's own files, shown as a diff |

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
| `paper-trading-gate` | step 7, graduation: the five criteria, how each is evidenced, the freeze, and the daily run and its record |

**The house rules**: `how-we-work` (where work lands, changelogs, versions), `bloom-code-lint`,
and four instructions, on the assistants that receive them — *Troubleshooting* in `SETUP.md` says
which: Bloom Code and PEP 8, for every Python file on the machine; test writing, for Python tests;
and filesystem boundaries, in any project, for every file the assistant reads: outside the folder
it works in, only the places the task needs. `bloom-code-lint` is the check to run by hand.

**One agent**, deployed for your user with the skills: `blueprint-critic` reads a drafted
`BLUEPRINT_N.md` cold, before your go, against the strategy's `AGENTS.md`, `OBJECTIVE.md`, the
notes the draft cites and what the analyzer measured, and returns objections only — each with the
line and the evidence. It never writes and never proposes a thesis; you decide what stands.
`blueprint` hands it the draft before asking for your go, and you can ask for it by name.

---

## What it will not do

The researcher's part is **the hypothesis**, and it stops where the numbers start.

- **It computes no number.** Not a return, a Sharpe, a drawdown or an attribution: every number
  about a book comes from the engines the project names — in a strategy, the KaxaNuk Backtest
  Engine and Attribution Analysis. It quotes those numbers from `FINDINGS_N.md` and `RESULTS.md`,
  naming the file.
- **It does not write the record.** `JOURNAL_N.md`, `FINDINGS_N.md`, `RESULTS.md` and
  `CHANGELOG.md` belong to whoever ran the experiment; `challenge` may append one entry to
  `JOURNAL_N.md`, on your go, and nothing more.
- **It does not write `OBJECTIVE.md` before your words.** `objective` drafts the idea and its
  claims from what you tell it, before any paper is read; with nothing from you, there is nothing
  to draft.
- **It cites no source that has no note.** A source in a `BIBLIOGRAPHY.md` without a note is a lead,
  and nothing is claimed on its authority.
- **It never advises on a holding.** A brief quotes figures from dated sources and names the rules
  in your `Portfolio/RULES.md` worth a look; it never says buy, sell, trim, add or hold, and never
  computes a weight, a P&L or a return. `philosophy` writes only what you typed, never a view of
  its own.

---

## What is in here

```
.apm/skills/          every skill: the researcher's, the Investment Lab's and the house rules'
.apm/prompts/         the commands
.apm/instructions/    the house style: Bloom Code, PEP 8, test writing, filesystem boundaries
.apm/agents/          the one agent, blueprint-critic
templates/strategy/   the KaxaNuk Strategy Template — the eight steps as folders; its README is the
                      process, and the order of work a strategy follows
templates/researcher/ the researcher's home, empty
examples/golden-flow/ one strategy worked through every folder of the template
SETUP.md              the install, step by step — what an assistant follows when you paste the URL
apm.yml               the package: what apm install reads; it depends on nothing
pyproject.toml        the ruff settings for the skills' scripts
AGENTS.md, CLAUDE.md  the rules for changing this repository
CHANGELOG.md          one entry per version
LICENSE               MIT
.gitignore            what apm install and Python write per machine
```

**What this repository owns, and what a copy owns.** This repository owns what is written once and
copied or installed everywhere; a copy owns what its owner writes in it. A strategy made from the
template is its owner's from the first commit and never merges back; the skills keep updating with
`uvx --from apm-cli==0.33.0 apm update -g`.

---

## Development

```bash
uvx ruff check .
(cd templates/strategy && uvx ruff check .)
(cd examples/golden-flow && uvx ruff check .)
uv run --no-project python .apm/skills/bloom-code-lint/scripts/bloom_code_check.py .apm/skills/*/scripts
(cd templates/strategy && uv run --no-project python ../../.apm/skills/bloom-code-lint/scripts/bloom_code_check.py . --max-line-length 100)
(cd examples/golden-flow && uv run --no-project python ../../.apm/skills/bloom-code-lint/scripts/bloom_code_check.py . --max-line-length 100)
```

Ruff lints the skills' scripts, the template and the worked example, each with its own settings;
the Bloom Code check runs on the scripts at its default 120 columns and, from inside each strategy
— so it finds the strategy's own packages — at the strategy's 100. Each runs through `uv` alone: no
Python of your own is needed. They run on your machine before a commit; there is no CI, so nothing
runs them for you.

**The template and the example in step.** Nothing else is automated: they are kept in step by
hand, as `AGENTS.md` says. For each file `git ls-files templates/strategy` lists, the example's
copy with its own lines removed — those between `<!-- example: begin -->` and
`<!-- example: end -->` or `# --- example: begin ---` and `# --- example: end ---`, and in a
notebook every cell that starts `# EXAMPLE-ONLY CELL` and every marked block inside a markdown
cell — equals the template's but for blank lines and the exceptions `AGENTS.md` lists. For the
Markdown and Python files:

```bash
for f in $(git ls-files templates/strategy | grep -E '\.(md|py)$'); do
  e="examples/golden-flow/${f#templates/strategy/}"
  [ -f "$e" ] || continue
  awk '/^(<!-- example: begin -->|# --- example: begin ---)$/{s=1;next} /^(<!-- example: end -->|# --- example: end ---)$/{s=0;next} !s' "$e" \
    | diff -B <(awk 1 "$f") - > /dev/null || echo "differs: $f"
done
```

For the notebooks, cell by cell, by cell id:

```bash
for nb in $(git ls-files templates/strategy | grep '\.ipynb$'); do
  uv run --no-project python - "$nb" "examples/golden-flow/${nb#templates/strategy/}" <<'PY' || echo "differs: $nb"
import json, re, sys
marked = re.compile(r'^(<!-- example: begin -->|# --- example: begin ---)$.*?^(<!-- example: end -->|# --- example: end ---)$\n?', re.M | re.S)
def cells(path):
    kept = [c for c in json.load(open(path, encoding='utf-8'))['cells'] if not ''.join(c['source']).startswith('# EXAMPLE-ONLY CELL')]
    return [(c.get('id'), c['cell_type'], [l for l in marked.sub('', ''.join(c['source'])).splitlines() if l.strip()]) for c in kept]
sys.exit(cells(sys.argv[1]) != cells(sys.argv[2]))
PY
done
```

Any file either names that `AGENTS.md` does not list as an exception is a fault.

**To try a change** to a skill, a command, an instruction or the agent, install it at project scope,
from a short scratch folder, with the APM the package is pinned to — never `-g` of the working
tree — **in a shell whose home is a short, empty throwaway folder**. A skill installed for your
user wins over a project skill of the same name, so on a machine where the package is installed the
check would otherwise run the installed copy, and the walk below would change your real setup.
From the repository's root:

```bash
K=C:/k   # an absolute, short path of your own: /tmp/k on macOS or Linux, never ~
mkdir -p "$K/home" "$K/check"
REV=$(git stash create)
git -c core.autocrlf=false archive --format=tar --prefix=KaxaNuk-Researcher/ "${REV:-HEAD}" | tar -x -C "$K"
export HOME="$K/home"
export USERPROFILE="$HOME"
git config --global user.name "Tester"; git config --global user.email "tester@example.invalid"
cd "$K/check"
uvx --from apm-cli==0.33.0 apm install "$K/KaxaNuk-Researcher" --target claude
```

`git stash create` takes your uncommitted changes to tracked files without touching them — a new
file once `git add` has staged it — and with nothing uncommitted the archive is `HEAD`: the files
the commit would hold, with LF endings and none of the ignored folders a working tree has. Open a
new session in the `check` folder, from that shell.

**Before a release, do the same with the commit to be tagged.** It should deploy exactly 20 skills,
9 commands, 4 rules and 1 agent, with no warning. Then, if the release changes a skill, a command
or a script, walk the newcomer's path by hand in that folder — `init-researcher`, which runs
`interview`, then `next`, `read` on one clipping, a round of `philosophy` at Starter, `brief setup`
and `brief`, and `init-strategy` — once in Spanish with a researcher whose name has an accent,
*Sofía*, whose skill must deploy as `~/.claude/skills/sofia/`, and once on an assistant with no
question tool, such as Codex. Delete the scratch folder afterwards: under the throwaway home,
nothing the walk installed or scheduled reached your own. A newer APM is adopted only when this
install passes with it, on Windows.

`AGENTS.md` has the rules for changing this repository: work lands on `main`, and a release is
tagged `vX.Y.Z` there. `CHANGELOG.md` has one entry per version.

---

## Licence

MIT, see [`LICENSE`](LICENSE).
