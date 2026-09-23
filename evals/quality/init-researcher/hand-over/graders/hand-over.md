---
type: llm
focus: last_message
---
The message ends the creation of a researcher's home, `Ada`. PASS only if every line below holds;
FAIL if any one does not.

- It reports the home as created, not failed or still to make.
- It tells the owner to open the new folder in a new session and run `researcher-init` there.
- It says the library is private: nothing in `Sources/` is pushed anywhere public (the PDFs are
  kept out by `.gitignore`, or words to that effect).
