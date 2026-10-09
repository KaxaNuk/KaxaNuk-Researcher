---
name: init-researcher
description: >
  Create a KaxaNuk researcher's home, once per person — ask the language, the researcher's name and
  where to put it, bring the package to its newest version with apm update -g, copy the home
  template inside it by a script, its first version saved — then run the interview in the same
  conversation. Only when the owner runs it by name, or as the step of the install SETUP.md walks
  through; never per strategy. It does NOT create a strategy (use `init-strategy`), nor ask how
  the owner works or invests (`philosophy` does, later).
metadata:
  version: 0.7.0
---

# Init researcher — a home for the library, once

A researcher is one per person, not per strategy: its library — `Sources/`, `Knowledge/`,
`Philosophy/` — grows across every strategy and project, and a second home would split it. So this
runs once. The home is named after the researcher — `Ada`, not `my-researcher`.

**Plain words throughout.** The owner may never have used a terminal. Ask one thing at a time, never
ask them to type a command — you run every one — and say what happens in a sentence, as a progress
note while you work: from step 1 to the interview's hand-over, a turn ends only on a question.
Without a question tool — Codex, Gemini — each question marked *through the question tool* is one
chat message, its options numbered beneath and *Other — your own words* last.

## When to Use

- The owner runs `init-researcher` by name — *init-researcher Ada*, *set up my researcher* — or
  `SETUP.md` reaches its step 3, in the conversation that installed the package.
- **Not when a home already exists.** If the owner already has one — a folder with a filled
  `RESEARCHER.md` — say where and make no second: a second home splits the library. Install it for
  the assistant in use instead, as `SETUP.md`'s *One researcher per person* says — the package with
  `--target`, `user_targets.py add`, the home, `check` — and hand over. A home made before the
  researcher was a package is brought forward by `update`, not replaced.

## Steps

1. **The language.** If the owner has not chosen one in this conversation, ask it first, alone, in
   Spanish and English together, through the question tool: `Idioma/Lang` — *Español*,
   *English*; *Other* for another. Everything after is in that language, the interview included.

2. **The name, with a welcome.** One warm line first, in their language — *Your researcher will be
   your companion for your work and your projects, and you'll call it by its name in any folder.*
   (*Tu investigador será tu compañero para tu trabajo y tus proyectos, y lo llamarás por su nombre
   en cualquier carpeta.*) — then *What would you like to call it?* (*¿Cómo te gustaría llamarlo?*),
   through the question tool: three short names proposed, each with a few words on its feel, and
   *Other* for theirs. A name given with the command is used without asking. Never pick one for
   them.

3. **The place and the go, in one question.** `Where?` (`¿Dónde?`), through the question tool:
   - *Go — make it at <path>*, described as *creates your researcher's home there, then two quick
     questions about you, about three minutes*, *after bringing the package up to date* added when
     step 5 will run;
   - *Another folder*, which asks for the parent folder only, in chat, puts `<Name>` inside it — a
     path already ending in `<Name>` is used as is, never nested — and asks `Where?` again with it;
   - *Stop*, and nothing is made.

   The path proposed is built from the name, short and outside any synced folder:
   `C:\Research\<Name>` on Windows — `D:\Research\<Name>` when a `D:` drive exists —
   `/Users/<you>/Research/<Name>` on macOS and `/home/<you>/Research/<Name>` on Linux, handed to
   the script absolute, the home folder spelled out, never `~`. Never a deep path such as
   `C:\Users\<you>\OneDrive\...`: on Windows a copied path may pass the path limit. The folder
   always takes the researcher's name. *About three minutes* is said here and nowhere else on the
   way in. Run on *Go* only.

4. **On *Go*, one line**, a progress note before anything runs, then the next step at once, in the
   same turn: *Your assistant may ask you to allow a few commands; allowing them is all you need to
   do.*

5. **Bring the package up to date**, on the same go, before anything is copied — the owner types
   nothing. First put the assistant in use — `claude`, `codex`, `copilot`, `cursor`, `gemini`,
   `opencode` or `windsurf` — on APM's list in `$HOME/.apm/apm.yml`, so the update keeps its
   files. The script is in this skill's folder; where the skill is not loaded, run it from the
   package:

   ```bash
   uv run --no-project python "<this skill's directory>/scripts/user_targets.py" add <assistant>
   uv run --no-project python "$HOME/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/skills/init-researcher/scripts/user_targets.py" add <assistant>
   ```

   Then update:

   ```bash
   uvx --from apm-cli==0.33.0 apm update -g --yes
   ```

   The go is the confirmation, so `--yes` answers APM's own prompt, which an agent's shell cannot.
   Skip both when the package was installed in this same conversation: it is already the newest,
   and `SETUP.md`'s step 2 listed the assistant. If `add` exits 1, skip the update too — it could
   delete this assistant's files — and say why in one plain line. Old `KaxaNuk-Agent-Skills`
   packages the update may list as orphaned are harmless; leave them unmentioned. If the update
   fails — no network, GitHub out of reach — say so in one plain line. Either way, go on: the home
   is made from the version installed, and `update` brings it forward later.

6. **Copy.** The script is in the `init-strategy` skill's folder, beside this one; in the
   conversation that installed the package, where the skill is not loaded yet, run it from the
   package itself:

   ```bash
   uv run --no-project python "<the init-strategy skill's directory>/scripts/scaffold.py" researcher "<full path>"
   uv run --no-project python "$HOME/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/skills/init-strategy/scripts/scaffold.py" researcher "<full path>"
   ```

   It creates the parent folder when it is missing, and refuses a folder that exists and is not
   empty. On Windows without long paths, it also refuses a destination so deep that a copied path
   would pass 259 characters, names that path and the longest destination that fits, and writes
   nothing; propose a shorter place. A fork of the package, or a clone in a folder of another name,
   is not found on its own: pass `--package <its install folder>`. A git step that fails leaves the
   copy in place — the script still exits 0 — and prints every command that finishes the
   repository from that step on. If git is missing, install it on the owner's go, then run the
   printed commands in the new folder. If the first commit fails for want of a git identity, ask
   for *a name and an email to sign the versions your researcher saves*, never invented; set them
   in that folder only, `git config user.name "<name>"` and `git config user.email "<email>"`,
   then run the printed commands there.

7. **Run the interview now**, in this conversation, in the language chosen: follow the `interview`
   skill — from `$HOME/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/skills/interview/SKILL.md`
   when it is not loaded in this session — with `<full path>` as the home. No turn ends between the
   copy and question 1: *Your researcher's home is ready at `<full path>`. Now two quick questions
   about you, so it is yours.* opens question 1's message. The interview says the rest; its own
   hand-over ends the run, or goes on into what the owner picks there.

   If the owner would rather stop here, one line: *When you're ready, open `<full path>` in a new
   session and say `interview`.*

## References

- `apm update -g`, with the APM the package is pinned to, 0.33.0 — the update its `SETUP.md` and
  the `update` command run.
- `scripts/user_targets.py`, in this skill's folder — puts an assistant on APM's list in
  `~/.apm/apm.yml`, which an install or update without `--target` keeps, and checks the
  researcher's files for it; `SETUP.md`, `interview`, `next` and `update` run it too.
- `scripts/scaffold.py`, in the `init-strategy` skill's folder — copies `templates/researcher/`
  from the KaxaNuk Researcher package.
- The `interview` skill, beside this one.
