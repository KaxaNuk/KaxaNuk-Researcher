<!-- example: begin -->

# Liquid Golden-Cross

Invest in the most traded US stocks with positive momentum, meaning the 50-day simple moving
average is above the 200-day, hold the top 30, and rebalance only when that top 30 differs from the
current portfolio by 10%, to avoid rebalancing too often.

> **Status: steps 1 to 6 run end to end, and step 7's gate evaluated against the result.** The rule
> beats the index by 3.1 points a year and loses to its own control by 1.1; of its 45.5
> idiosyncratic points, about 5 belong to the signal it is named after. It is **not a defensive
> book** — beta 1.028, and more volatile than the index — and what it buys is a drawdown 9.3 points
> shallower than the same thirty names unfiltered. Every number is in [`RESULTS.md`](RESULTS.md).
> **It does not pass the gate, no paper trading has run, and nothing here is out of sample.**
> Replace this line as the strategy moves, and the banner at the top of `AGENTS.md` with it.

This is the worked example of the KaxaNuk Strategy Template: one strategy worked through the
process, for reading and copying, which `init-example` copies. A strategy of your own starts from
`init-strategy`, never from here.

Built on the [KaxaNuk Strategy Template](https://github.com/KaxaNuk/KaxaNuk-Researcher/blob/main/templates/strategy/README.md):
eight steps as a folder structure. Its README says what each folder is for, where each
kind of logic goes and, under *Starting your own strategy*, the order to work in; this one does not
repeat it. **Start at** [`OBJECTIVE.md`](OBJECTIVE.md), the idea and its claims as they were
written before any paper was read, then [`RESULTS.md`](RESULTS.md) for what the claims survived.

| Read | For |
| --- | --- |
| [`OBJECTIVE.md`](OBJECTIVE.md) | the idea, and the status of each claim inside it |
| [`RESULTS.md`](RESULTS.md) | every number this repository has measured, and what it cost |
| [`AGENTS.md`](AGENTS.md) | how work is done here, and the bar a result has to clear |
| [`SETUP.md`](SETUP.md) | how this repository is set up on a new machine |

<!-- example: end -->
