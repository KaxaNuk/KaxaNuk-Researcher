---
type: regex
target: last_message
pattern: 'no claims|claims yet|without claims|run .?/?(?:[\w-]+:)?objective|objective.? (comes )?first'
flags: i
---
The item that comes first is named: the objective has no claims; a draft that only mentions
OBJECTIVE.md does not match. The command may be named bare or namespaced, as a run names it: "run
`/kaxanuk-researcher-evals:objective`".
