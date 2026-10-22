# A key leaked

A key, a token, a password or a licence that was saved as a version, sent, pushed, pasted in a
chat or shown on a screen someone else saw is a leak, even if it was deleted a minute later: a copy
may already be elsewhere, and on GitHub automated scanners find public keys within minutes. The
order matters: make the old key useless first, then look for where it went.

1. **Revoke it, at its provider.** The owner signs in to the provider — the data provider, GitHub,
   the AI provider, the bank — and revokes or deletes the key, then issues a new one. For a KaxaNuk
   licence, write to `lab@kaxanuk.mx` with the licence's name, never its value. Until this is done,
   nothing else helps.
2. **Put the new key where it belongs**, by the owner's hand: in a strategy, `Config/.env`, which
   git never saves; never in a note, a notebook, a commit message or a chat.
3. **Look at where the old one went.** Run the check (`security`'s *Check a folder*) to find every
   file that still holds it; and ask the owner where else it may be: a copy on GitHub, a message, a
   shared document, a screenshot.
4. **Clean the files**, on the owner's go: take the value out, and keep the file of keys out of git
   (`.gitignore`, then `git rm --cached`). Saved versions still hold the old value; since the key
   is revoked, that copy is harmless. Rewriting old versions is the owner's decision and needs care
   with a copy on GitHub, so it is never a step you run on your own.
5. **Watch the provider's account** for a few days — usage, charges, sign-ins — and turn on
   two-factor sign-in there if it is off.

What to say: plain and calm. *A leaked key is common and fixable; what matters is revoking it now.*
