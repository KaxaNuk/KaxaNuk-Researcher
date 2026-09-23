---
type: regex
target: last_message
pattern: 'no claims|claims yet|without claims|run .?/?(?:[\w-]+:)?objective|objective.? first'
flags: i
---
The owner is sent to `objective` first, because the objective has no claims; a plan that only
mentions OBJECTIVE.md does not match. The command may be named bare or namespaced, as a run names
it: "run `/kaxanuk-researcher-evals:objective`".
