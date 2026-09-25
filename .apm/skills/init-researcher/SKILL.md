---
name: init-researcher
description: >
  Create a KaxaNuk researcher's home in a new folder — the library's folders, RESEARCHER.md to be
  filled, AGENTS.md with the library's rules — after bringing the researcher package to its newest
  version with apm update -g, from the template that ships inside it, copied by a script and made a
  git repository; then hand over to `interview` in two plain steps. Only when the owner runs it by
  name; once per person, never per strategy. It does NOT run the interview itself and does NOT
  create a strategy (use `init-strategy`).
metadata:
  version: 0.3.0
---

# Init researcher — a home for the library, once

A researcher is one per person, not per strategy: its library — `Sources/`, `Knowledge/`,
`Philosophy/` — grows across every strategy, and a second home would split it. So this runs once.
The home is named after the researcher — `Ada`, not `my-researcher` — and the owner opens it
in a session of its own, or adds it to a strategy's session to bring the library in.

## When to Use

- The owner runs `init-researcher` by name — *init-researcher Ada*, *set up my researcher*.
- **Not when a home already exists.** If the owner already has one — a folder with a filled
  `RESEARCHER.md` — say where, and stop: a second home splits the library. A home made before the
  researcher was a package is brought forward by `update`, not replaced.

## Steps

1. **The name and the place.** Ask for whatever is missing through the question tool: the
   researcher's name, which names the folder, and the parent folder — short on Windows,
   `D:\Research\Ada`, never a deep synced path. Say the full path you will create.

2. **The plan.** In chat, in plain words: the path; that it first brings the researcher package to
   its newest version for the user, so the home is made from the newest template and every skill
   and command is current; that it then makes the researcher's home — `RESEARCHER.md` and
   `Philosophy/HOW-I-INVEST.md` as blanks for the interview, `Sources/` with its empty `Books/`,
   `Papers/` and `Clippings/`, `Knowledge/` with an empty `INDEX.md` and `LOG.md`, the empty
   `Studies/`, where `study` keeps the owner's studies, `AGENTS.md`, and the template's
   `README.md`, `CHANGELOG.md`, `LICENSE`, `CLAUDE.md`, `apm.yml`, `.gitignore` and
   `.gitattributes` — every file the script copies, the empty folders' `.gitkeep` files aside; and
   that it becomes a git repository with the first commit *Start from the KaxaNuk Researcher
   template*. Say that the assistant may ask to allow two commands, the update and the copy, and
   that allowing them is all the owner has to do. Ask for the go — *Go*, *Change something*,
   *Stop* — and run on *Go* only.

3. **Bring the package up to date**, on the same go, before anything is copied — the owner types
   nothing:

   ```bash
   uvx --from apm-cli==0.29.0 apm update -g --yes
   ```

   The go is the confirmation, so `--yes` answers APM's own prompt, which an agent's shell cannot.
   Then `uvx --from apm-cli==0.29.0 apm deps list -g` names the version now installed: say it in
   one line. Old `KaxaNuk-Agent-Skills` packages it may list as orphaned are harmless; leave them
   unmentioned. If the update fails — no network, GitHub out of reach — say so in one plain line,
   name the version still installed, and go on: the home is made from that version, and `update`
   brings it forward later. What the update brings is there in the owner's next session, which is
   where the interview runs.

4. **Copy.** The script is in the `init-strategy` skill's folder, beside this one:

   ```bash
   uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" researcher "<full path>"
   ```

   It refuses a folder that exists and is not empty. On Windows without long paths, it also refuses
   a destination so deep that a copied path would pass 259 characters, names that path and the
   longest destination that fits, and writes nothing; choose a shorter place. A fork of the package,
   or a clone in a folder of another name, is not found on its own: pass
   `--package <its install folder>`. A git step that fails leaves the copy in place — the script
   still exits 0 — and prints every command that finishes the repository from that step on. If git
   is missing, install it on the owner's go, then run the printed commands in the new folder. If the
   first commit fails for want of a git identity, ask for the name and email — never invent them —
   set them in that repository only, `git config user.name "<name>"` and
   `git config user.email "<email>"`, then run the printed commands there.

5. **Hand over, as a short numbered list in plain words** — the owner may read nothing else:

   1. Open `<full path>` in a **new** session — in the desktop app, choose that folder for the
      session; in a terminal, `cd` into it and start the assistant, `claude` for Claude Code.
   2. Type `/interview` there — elsewhere, ask for the interview by name — and answer its seven
      questions, about ten minutes. It deploys the agent and commits what it writes: there is
      nothing to install and nothing to type but the answers.

   Then one line: the library is private — nothing in `Sources/` is pushed anywhere public, and
   the `.gitignore` keeps PDFs out.

## References

- `apm update -g`, with the APM the package is pinned to, 0.29.0 — the update its `SETUP.md` and
  the `update` command run.
- `scripts/scaffold.py`, in the `init-strategy` skill's folder — copies `templates/researcher/`
  from the KaxaNuk Researcher package.
