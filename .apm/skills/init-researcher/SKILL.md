---
name: init-researcher
description: >
  Create a KaxaNuk researcher's home in a new folder — the library's folders, RESEARCHER.md to be
  filled, AGENTS.md with the library's rules — from the template that ships inside the researcher
  package, copied by a script and made a git repository, then hand over to `interview` for
  the interview. Only when the owner runs it by name; once per person, never per strategy. It does
  NOT run the interview itself and does NOT create a strategy (use `init-strategy`).
metadata:
  version: 0.2.1
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

2. **The plan.** In chat: the path; that it will hold the researcher's home at this package's
   version — `RESEARCHER.md` and `Philosophy/HOW-I-INVEST.md` as blanks for the interview,
   `Sources/` with its empty `Books/`, `Papers/` and `Clippings/`, `Knowledge/` with an empty
   `INDEX.md` and `LOG.md`, `AGENTS.md`, and the template's `README.md`, `CHANGELOG.md`, `LICENSE`,
   `CLAUDE.md`, `apm.yml`, `.gitignore` and `.gitattributes` — every file the script copies, the
   empty folders' `.gitkeep` files aside; that it becomes a git repository with the first commit
   *Start from the KaxaNuk Researcher template*. Ask for the go — *Go*, *Change something*, *Stop*
   — and run on *Go* only.

3. **Copy.** The script is in the `init-strategy` skill's folder, beside this one:

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

4. **Hand over.** Tell the owner to open the new folder in a **new** session and run
   `interview` there: the interview that writes `RESEARCHER.md` and the agent file. Then
   `apm install --target <their agent>` in that folder, once, to deploy the agent; the skills are
   already installed for the user. Say that the library is private: nothing in `Sources/` is
   pushed anywhere public, and the `.gitignore` keeps PDFs out.

## References

- `scripts/scaffold.py`, in the `init-strategy` skill's folder — copies `templates/researcher/`
  from the KaxaNuk Researcher package.
