---
name: backup
description: >
  Keep a copy of the researcher's home — or of a strategy — off this computer, on a private GitHub
  repository: make it, send each new saved version there, and bring it back on a new computer.
  Only when the owner asks — "keep a copy", "back up", "save it online", "a new computer", "what
  is a commit", or the same in their language — never offered on its own. It never makes a
  repository public, never forces a send, never pulls or merges on its own, and never creates an
  account or signs in for the owner.
metadata:
  version: 0.1.1
---

# Backup — a copy of your researcher off this computer

Every go saves a version of what it wrote, on this computer only, as the home's `AGENTS.md` says
under *Plan first, then write*. This skill keeps a second copy, on a private GitHub repository,
when the owner asks for one, and only then: no skill reminds them of it, and no hand-over mentions
it. It is also where a failed send points — *say* back up *when you want me to look*.

**Plain words.** To the owner a version is never a *commit*, and git is named only when they name
it: *a saved version*, *your copy on GitHub*, *send*. You run every command; show one when asked.

**How to ask.** In Claude Code, the questions below are asked by calling `AskUserQuestion` — the
options as its choices, at most four, and *Other*, which the tool always offers, as the free-text
escape. Without such a tool — Codex, Gemini and every other assistant — they are one chat message:
each question numbered, its options numbered beneath it, *Other — your own words* last, and one
line on how to answer. Every question, option and line is in the owner's language, and every
header is the one given below for that language — the English one for any other — twelve
characters at most.

## Step 1: What to say first

Two lines, in the owner's language, before a first copy: *Every go saves a version on this
computer only. A copy on GitHub keeps it safe if the computer breaks, and follows you to a new
one — private: only you can see it.* Asked *what is a commit?*: *git's word for a saved version —
a dated snapshot of the files, signed with your name.* A question alone ends the run there.

## Step 2: Which folder

The researcher's home, by default — the folder that holds `RESEARCHER.md`. When the session is open
in a strategy — `Bibliotheca/`, `Universe/` and `Experiments/` — that strategy: one strategy, one
repository, never inside the home's copy. The worked example, whose `README.md` or `AGENTS.md`
carries `<!-- example: begin -->`, is for reading and takes no copy. Name the folder, by path. A
folder with no `.git/` keeps no versions yet: say so in one line — `next` offers to start them —
and stop. Changes not saved yet stay out of the copy; `next` offers to save them.

## Step 3: A copy already?

`git remote get-url origin`. When it prints an address, first make sure the copy is private: with
`gh` signed in, `gh repo view <the address> --json visibility -q .visibility` prints `PRIVATE`;
without `gh`, ask the owner to look on GitHub. A public copy, or one nobody confirms private, is
said in one line — *make it private in its settings on GitHub first* — and nothing is sent to it.
Then say where the copy is and how many saved versions it lacks — after a fetch, as *Step 8* runs
a send, `git rev-list --count "@{u}..HEAD"`; those only the copy holds, `"HEAD..@{u}"`, are *Step
8*'s last paragraph — and, when `kaxanuk.autosend` is `paused`, that a send failed, and why. Then
ask `Your copy` (`Tu copia`): *Send the versions not sent yet*, as *Step 8* does — on success
`kaxanuk.autosend` goes back to `true` only when it was `paused`; when it is not set, *Step 6*'s
`E-mail` and *Step 7*'s `Send?` are asked in the same call; *Change automatic sending*, *Step 7*'s
question; *Nothing now*. Then stop: the rest is for a first copy.

## Step 4: Plan and go

In chat, short: the folder; the first way of *Step 5* that applies; the repository's name, and
that it is private; what the copy holds and what stays here (*Step 9*); and what is the owner's to
do — sign in to GitHub, or create an account, in any browser window that opens. A home whose
`AGENTS.md` has no *Versions* paragraph gets one line more: `update` brings it, so every skill that
saves knows how to send. Then ask, in one call:

- `Go?` (`¿Adelante?`) — *Go*, *Change something*, *Stop*; in chat, any of the go words in the
  home's `AGENTS.md`. On *Change something*, ask again with options: another name, another way.
  Never act on silence or on a *Stop*.
- `E-mail` (`Correo`), as *Step 6* says, and `Send?` (`¿Envío?`), as *Step 7* says.

On *Go*: the e-mail first, then the way, then the setting *Send?* chose, once the copy exists.

## Step 5: Three ways, in this order

1. **`gh`, installed and signed in** — `gh auth status` succeeds:
   `gh repo create <name> --private --source . --remote origin --push`, always `--private`.
   `<name>` is `<slug>-researcher` for a home, the researcher's name made safe as `interview`'s
   *Step 4* says — `Sofía` gives `sofia-researcher` — or the strategy's folder name.
2. **github.com** — the owner signs in, or creates a free account: theirs to do. They create an
   **empty private** repository at <https://github.com/new>, by that name, with no README, licence
   or `.gitignore`, and paste its address. Then `git remote add origin <the address>` and
   `git push -u origin main`, with `GIT_TERMINAL_PROMPT=0` set as *Step 8* shows for each shell, so
   git never waits on a prompt in the terminal that no one can answer. The first send may open a
   browser window asking them to sign in to GitHub, once: that is expected, and theirs to do.
3. **GitHub Desktop** — when the second fails for want of a sign-in, or they prefer it: *File → Add
   local repository*, this folder, then *Publish repository* with *Keep this code private* ticked.
   `git remote get-url origin` then names the copy.

**Git must be able to sign in to send on its own.** After the first way, `gh auth setup-git`, so
git uses `gh`'s sign-in. After the third, make one send the way the second makes its first —
`GIT_TERMINAL_PROMPT=0` alone, without `credential.interactive=never` — so a browser sign-in can
open once. When git still cannot sign in, automatic sending is not offered: `kaxanuk.autosend`
is `false`, and the copy is updated from GitHub Desktop's *Push origin*, which say in one line.

An owner who wants the assistant to do all of it gets `gh` on their go —
`winget install GitHub.cli` on Windows, `brew install gh` on macOS — and `gh auth login` is their
sign-in, in the browser it opens. Then the first way.

## Step 6: Their e-mail

Every saved version is signed with `git config user.name` and `user.email`, and on GitHub both
travel with it. Before the first send, offer GitHub's private *noreply* address, shown in GitHub's
e-mail settings, <https://github.com/settings/emails>: *Use GitHub's private address
(recommended)*, *Keep the one I have*. Set for this folder only, `git config user.email <it>`, it
signs new versions only: those already saved keep theirs, and history is never rewritten.

If GitHub refuses a send because it would publish a private e-mail — error `GH007` — say so plainly,
and give the two choices: allow it once in GitHub's e-mail settings, or keep the copy as it is.

## Step 7: Sending each new version

Asked once, `Send?` (`¿Envío?`) — *Send each new version automatically (recommended)*, *Only when I
ask*: `git config kaxanuk.autosend true` or `false`, in this folder only. With *Only when I ask*,
*back up* sends what has piled up, as *Step 3* does.

## Step 8: Sending a version

What every skill that saves does when `git config --get kaxanuk.autosend` prints `true`, and what
this skill does when asked — with no prompt that nobody can answer, and in bash under a timeout of
about a minute:

```bash
GIT_TERMINAL_PROMPT=0 timeout 60 git -c credential.interactive=never push
```

```powershell
$env:GIT_TERMINAL_PROMPT = '0'; git -c credential.interactive=never push
```

The fetch of *Step 3* runs the same way, `fetch` in place of `push`.

Never `--force`; never a pull, a merge or a rebase on its own. On success, one line: *Saved and
sent*. On any failure the version stays saved here; one plain line — *Saved on this computer; your
copy on GitHub could not be updated (<the reason in plain words>). Say* back up *when you want me
to look.* — and `git config kaxanuk.autosend paused`.

When the copy holds versions this computer lacks — saved from another computer — say so, and ask
`Bring?` (`¿Los traigo?`): *Bring them here*, *Not now*. On *Bring them here*, `git pull --ff-only`,
only when nothing here differs: no unsaved change and no saved version the copy lacks; otherwise
stop and explain: two computers saved different versions, and joining them is the owner's choice.

## Step 9: What the copy holds

What the folder's saved versions hold, and nothing its `.gitignore` keeps out. At home: the notes,
the studies, the lessons, `Philosophy/`, `RESEARCHER.md` and the clippings in text; **not** the
PDFs and other files kept out of `Sources/`, nor `Extracts/`, `Briefs/`, `Portfolio/` or any
`.env` — they stay on this computer by design. In a strategy: the code, the documents and the
notes; not the PDFs, the data, the engines' output or `Config/.env`. Suggest keeping the PDFs and
`Portfolio/` somewhere private of their own — a personal cloud folder outside the home, or an
external disk — never in this copy, and never force a kept-out file into it.

## Step 10: A new computer

Install the package as the package's `SETUP.md` says — git and uv in its step 1, the package in
its step 2. Then, in a new session, clone the copy into a short folder —
`git clone <the address> <folder>` — run `update` there, which rewrites the researcher's skill for
the new path and installs the home for the user, and open a new session; a strategy's clone takes
its own `SETUP.md` instead. The name, the e-mail and *Send?* do not travel: set them again, as
*Step 6* and *Step 7* say. The PDFs and `Portfolio/` come from wherever they were kept.

## Never

A public repository, or making one public; `--force`, or rewriting history; creating an account or
signing in for the owner; storing a token or a password — in a file, an address or a setting; a
pull, a merge or a rebase on its own; sending anything when `kaxanuk.autosend` is not `true` and
the owner did not ask; offering a copy, or reminding the owner of one, unasked.

## References

- The home's `AGENTS.md`, *Versions*: what a saved version is, and the send each saving skill makes.
- `next`: starts the versions in a folder with none, and saves changes made by hand.
- `update`: on a new computer, rewrites the researcher's skill for the path and installs the home.
