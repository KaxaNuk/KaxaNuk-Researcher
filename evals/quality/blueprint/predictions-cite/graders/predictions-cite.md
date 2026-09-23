---
type: llm
focus: {source: file, path: Experiments/Experiment_1/BLUEPRINT_1.md}
---
The file is a strategy's Experiment 1 blueprint, written after the owner's go. The strategy's only
note is `Bibliotheca/Papers/Moskowitz_2012_Time_Series_Momentum.md`, and no analyzer section has
run: `RESULTS.md` holds no measurement. PASS only if every line below holds; FAIL if any one does
not.

- The file is drafted, not the template as shipped: the thesis is not the template's placeholder
  ("One paragraph: what book this rule produces, and why it is a fair yardstick"), and the
  predictions table has rows of its own, not only the placeholder row "what the book should do".
- Every row of the predictions table, under "What this experiment should show", cites in its
  "Where it comes from" column a note under `Bibliotheca/` or an analyzer section by its number, or
  is marked as a lead (the word "lead", or "read X / run analyzer section Y before predicting
  this"). A row with none of these fails.
- No performance number is predicted without a measurement: no row, and no line of the thesis,
  success criteria or risks, states an expected return, Sharpe ratio, volatility, drawdown,
  turnover, hit rate or cost as a figure. Numbers that define the rule (50 and 200 days, monthly,
  five names, a year), page numbers, and figures quoted as the note's own finding are not
  predictions.
- The template's headings are kept, word for word and in this order: "# Blueprint — Experiment 1",
  "## Experiment 1 — the declared benchmark", "### Thesis", "### Rules", "### What this experiment
  should show", "### Success criteria", "### Key risks", "### Open questions this experiment
  deliberately does not answer"; and the predictions table keeps the columns "#", "Prediction",
  "Where it comes from", "What would falsify it". None is renamed or dropped.
