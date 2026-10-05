---
name: init-researcher
description: >
  Create a KaxaNuk researcher's home — asking the language, the researcher's name and where to put
  it, the folder named after the researcher — after bringing the researcher package to its newest
  version with apm update -g, from the template that ships inside it, copied by a script and made a
  git repository; then run the interview straight away, in the same conversation — two short steps
  about the owner, about three minutes. Only when the owner runs it by name, or as the step of the
  install SETUP.md walks through; once per person, never per strategy. It does NOT create a
  strategy (use `init-strategy`), and does NOT ask how the owner invests (`philosophy` does, later).
metadata:
  version: 0.5.0
---

# Init researcher — a home for the library, once

A researcher is one per person, not per strategy: its library — `Sources/`, `Knowledge/`,
`Philosophy/` — grows across every strategy, and a second home would split it. So this runs once.
The home is named after the researcher — `Ada`, not `my-researcher` — and the owner opens it
in a session of its own, or adds it to a strategy's session to bring the library in.

**Plain words throughout.** The owner may never have used a terminal. Ask one thing at a time, say
what happens in a sentence, and never ask them to type a command: you run every one.

## When to Use

- The owner runs `init-researcher` by name — *init-researcher Ada*, *set up my researcher* — or
  `SETUP.md` reaches its step 3, in the conversation that installed the package.
- **Not when a home already exists.** If the owner already has one — a folder with a filled
  `RESEARCHER.md` — say where, and stop: a second home splits the library. A home made before the
  researcher was a package is brought forward by `update`, not replaced.

## Steps

1. **The language.** If the owner has not chosen one in this conversation, ask it first, alone, in
   Spanish and English together, through the question tool: `Idioma/Lang` — *Español*,
   *English*; *Other* for another. Everything after is in that language, the interview included.

2. **The name.** "What will you call your researcher?" — through the question tool, three short
   names proposed and *Other* for theirs; a name given with the command is used without asking.
   Never pick one for them.

3. **The place, in one question.** Propose one folder, built from the name, short and outside any
   synced folder: `C:\Research\<Name>` on Windows — `D:\Research\<Name>` when a `D:` drive exists —
   and `~/Research/<Name>` on macOS and Linux. Options: *Here — <that path>*; *Choose another
   folder*, which asks for the parent folder only, in chat, and puts `<Name>` inside it. Never a
   deep path such as `C:\Users\<you>\OneDrive\...`: on Windows a copied path may pass the path
   limit. The folder always takes the researcher's name.

4. **The go, in two lines.** "I will update the researcher package, create `<full path>` with your
   researcher's library, and then ask you a few short questions about you, about three minutes.
   Your assistant may ask you to allow a few commands; allowing them is all you need to do." Ask
   for the go — *Go*, *Change something*, *Stop* — and run on *Go* only. What the copy contains is
   said in the hand-over, not here.

5. **Bring the package up to date**, on the same go, before anything is copied — the owner types
   nothing:

   ```bash
   uvx --from apm-cli==0.29.0 apm update -g --yes
   ```

   The go is the confirmation, so `--yes` answers APM's own prompt, which an agent's shell cannot.
   Skip it when the package was installed in this same conversation: it is already the newest.
   Old `KaxaNuk-Agent-Skills` packages it may list as orphaned are harmless; leave them
   unmentioned. If the update fails — no network, GitHub out of reach — say so in one plain line
   and go on: the home is made from the version installed, and `update` brings it forward later.

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
   printed commands in the new folder. If the first commit fails for want of a git identity, ask for
   the name and email — never invent them — set them in that repository only,
   `git config user.name "<name>"` and `git config user.email "<email>"`, then run the printed
   commands there.

7. **Run the interview now**, in this conversation, in the language chosen: follow the `interview`
   skill — from `~/.apm/apm_modules/KaxaNuk/KaxaNuk-Researcher/.apm/skills/interview/SKILL.md` when
   it is not loaded in this session — with `<full path>` as the home. Say one line first: *Your
   researcher's home is ready at `<full path>`. Now two short steps about you, about three minutes,
   so it is yours.* It asks who the owner is, what they are here for, and the researcher's domains,
   voice and rules — nothing about markets: how the owner invests is `philosophy`'s, a second
   interview the hand-over offers, and what the reading is for is asked by the first `read`. The
   interview's own hand-over — the map of the folders, a first thing to read, the skills that grow
   the researcher, and `philosophy` now or in a new session — ends the run, or hands on to `read`
   or `philosophy` when the owner picks one there.

   If the owner would rather stop here, the hand-over is two lines: open `<full path>` in a new
   session, and there type `/interview` — elsewhere, ask for the interview by name. The library is
   private: nothing in `Sources/` is pushed anywhere public, and the `.gitignore` keeps PDFs out.

## References

- `apm update -g`, with the APM the package is pinned to, 0.29.0 — the update its `SETUP.md` and
  the `update` command run.
- `scripts/scaffold.py`, in the `init-strategy` skill's folder — copies `templates/researcher/`
  from the KaxaNuk Researcher package.
- The `interview` skill, beside this one.
