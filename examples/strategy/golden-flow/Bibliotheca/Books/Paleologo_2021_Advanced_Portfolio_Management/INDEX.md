---
source: https://www.wiley.com/en-us/Advanced+Portfolio+Management%3A+A+Quant%27s+Guide+for+Fundamental+Investors-p-9781119789796
citation: "Giuseppe A. Paleologo. John Wiley & Sons, 2021. ISBN 9781119789796. The date the link was last checked is not recorded."
local_copy: none
read: "2026-08-25; what was read: not recorded"
---

# Paleologo (2021) — *Advanced Portfolio Management: A Quant's Guide for Fundamental Investors*

> One section per chapter idea. Every section ends with what it means for **this** repository, as a
> blockquote. Where the book contradicts something we do, that is recorded as a contradiction rather
> than smoothed over.

The book is written for fundamental equity PMs who need the quant apparatus — risk models, sizing,
attribution — without becoming quants.

> Rewritten on 2026-10-07 for this copy, after FINDINGS_1.md reported.
>
> **Why this book matters more than the papers.** Most papers in
> [`BIBLIOGRAPHY.md`](../../BIBLIOGRAPHY.md) argue for or against a *signal*. This book supplies a
> **method for deciding whether the signal is doing anything**: sections 1, 5 and 6 below. It turns
> "the strategy beats its benchmark" into "this part of the return is the idea, and this part is
> beta, size and luck". Experiment 1 used it on claims 1 and 2. Its answer: nine tenths of the
> rule's excess return is factor exposure, and once factors are stripped out the rule's selection is
> +2.70 points over the window, against −0.27 for its control
> ([`FINDINGS_1.md`](../../../Experiments/Experiment_1/FINDINGS_1.md), *What attribution says*).

---

## 1. Momentum is relative; trend-following is absolute

*(section 5.2.3)*

The book draws a distinction that most practitioner writing blurs. **Momentum is relative**: it
ranks a stock against its peers and goes long the winners, short the losers, so a momentum book is
roughly cross-sectional and roughly dollar-neutral. **Trend-following is absolute**: it holds
whatever is going up, sized by how much it is going up, with no reference to anyone else. In the
book's own toy example the same six technology names produce a long-everything trend portfolio and
a long-two / short-two momentum portfolio.

> Rewritten on 2026-10-07 for this copy, after FINDINGS_1.md reported.
>
> **What this implies for Golden Flow: claim 1 is a trend claim.** The golden cross asks whether
> *this* name is above its own average, never whether it out-trends its peers. The factor model's
> momentum factor measures the relative kind, so the blueprint's prediction 8 expected the factor
> model to see little of it. It saw 11.31 points of momentum in the rule's 137.35 points of excess
> return, against 88.10 from the market
> ([`FINDINGS_1.md`](../../../Experiments/Experiment_1/FINDINGS_1.md), the factor model). What the
> cross does show is a cut in beta: 10.39 points for the rule, against 22.15 for the control, the
> same rule without the cross.

## 2. Momentum has a term structure

*(section 5.2.3, citing Novy-Marx 2012)*

Past performance predicts future returns with a sign that flips twice as the lookback lengthens:
the most recent month **reverses** (last month's winners underperform, and more strongly the shorter
the window), one month to one year **continues** (this is the real momentum effect), and beyond a
year **reverses** again.

> Rewritten on 2026-10-07 for this copy, after FINDINGS_1.md reported.
>
> **What this implies for Golden Flow: nothing measured here.** Golden Flow computes no return over
> a fixed lookback as a feature. Its signal is the 50/200 cross, read as a state, which this section
> does not test. It stays as context for claim 1, and as a warning for any later feature built on
> last month's return: the book expects that sign to be negative.

## 3. Momentum's return is partly compensation for a fat left tail

*(section 5.2.3)*

The book z-scores daily momentum factor returns by trailing three-month volatility and shows the
quantiles are materially worse than Gaussian in the left tail. Alongside the behavioural stories
(under-reaction, over-reaction, "frogs in the pan"), it presents the risk-based reading: the premium
is paid for bearing crash risk, and the crash is real.

> Rewritten on 2026-10-07 for this copy, after FINDINGS_1.md reported.
>
> **What this implies for Golden Flow: its tail is close to the market's.** Golden Flow is long
> only, so it holds none of the short leg that owns this tail. Its worst drawdown is −32.47%,
> against −33.75% for the KN US Equity Core and −46.32% for the control, the same rule without the
> cross ([`FINDINGS_1.md`](../../../Experiments/Experiment_1/FINDINGS_1.md)). Mean and variance are
> still not enough to judge it, so the findings report the drawdown and the Sortino beside the
> Sharpe: a Sortino of 1.116 for the rule, against 1.011 for the control.

## 4. Alpha estimates are far noisier than beta estimates

*(section 3.3)*

Regressing a single stock's returns on the market gives a beta with a tight confidence interval and
an alpha whose interval is wider than the estimate itself — the book's worked example has an alpha
point estimate whose 95% band spans both large negative and positive values, while beta lands inside
a narrow range. Alphas also move a lot year to year; betas do not.

> Rewritten on 2026-10-07 for this copy, after FINDINGS_1.md reported.
>
> **What this implies for Golden Flow: its alpha has no error bar.** The engine puts the rule's
> alpha against the index at +7.28%, and the control's at +6.68%, with no interval around either
> ([`FINDINGS_1.md`](../../../Experiments/Experiment_1/FINDINGS_1.md)). What is estimated precisely
> is the exposure: 123.50 of the rule's 137.35 points of excess return are factors. The part claims
> 1 and 2 lean on is thin: once factors are stripped out, the rule's selection is +2.70 points over
> the window, against −0.27 for the control. One window cannot make that a stable property of the
> strategy.

## 5. Decompose P&L into factor and idiosyncratic — then decompose the idiosyncratic part

*(section 8.1–8.2, takeaways section 8.6)*

The recommended order is: split P&L into factor and idiosyncratic; if the factor part is large, your
factor risk is large and should be reduced by hedging, optimisation or tactical trading. Then split
the **idiosyncratic** part three ways:

- **Selection** — being directionally right about which names to hold.
- **Sizing** — being right about *how much*, so the big positions are the good ones.
- **Timing** — carrying risk when your views are better than average.

The mechanism is **counterfactual portfolios rather than a formula.** To measure sizing skill,
rewrite history with every position **equalised within each date**, keeping the side and the total
gross value unchanged, then compare the Sharpe of that book with the real one. The difference is
what sizing contributed. The book also warns to drop economically insignificant positions first, or
the analysis is dominated by residual slivers nobody was really betting on.

> Rewritten on 2026-10-07 for this copy, after FINDINGS_1.md reported.
>
> **What this implies for Golden Flow: Experiment 1 ran two of the three legs.** Sizing is the
> equal-weight arm: the rule's own names on its own dates, equalised. It earns a Sharpe of 0.722
> against the rule's 0.842, and an idiosyncratic return of −30.03 points against +13.84. That is
> claim 2's evidence. Selection is the twenty random books, drawn from the members on the rule's
> dates: every one has a negative idiosyncratic return, −84.50 to −3.77, all below the rule. Timing
> was not priced: the shifted-entry arm was not run
> ([`FINDINGS_1.md`](../../../Experiments/Experiment_1/FINDINGS_1.md)). The book's advice to drop
> slivers first is built into claim 3: the 1% floor holds no name smaller than that.

## 6. Size by risk-adjusted alpha

*(section 6.3–6.5, takeaways section 6.8)*

The book's sizing recipe: form a view of expected **idiosyncratic** return per name, put all views on
one horizon, neutralise them against factor loadings, then convert to position sizes by either a
proportional rule (position proportional to standardised alpha) or a shrunk mean-variance rule. It
notes the simplest proportional rule is often preferable in practice, especially in sector-focused
books.

> Rewritten on 2026-10-07 for this copy, after FINDINGS_1.md reported.
>
> **What this implies for Golden Flow: a contradiction, kept visible.** Golden Flow sizes by traded
> value. That is a capacity and attention argument, not a forecast of idiosyncratic return, so under
> the book's framework it is a constraint used as a weighting scheme. Claim 2 still won as a book: a
> Sharpe of 0.842 against 0.722 for the same names equally weighted. Attribution says how: the
> sizing adds beta and size, and turns an idiosyncratic return of −30.03 points into +13.84
> ([`FINDINGS_1.md`](../../../Experiments/Experiment_1/FINDINGS_1.md)). The book would still ask for
> a forecast behind the weights, and no note in this folder supplies one.

## 7. Volatility targeting is the cheap drawdown lever

*(section 6.6, takeaway section 6.8 #6)*

Scale portfolio gross exposure over time so that **predicted idiosyncratic dollar volatility** hits a
constant target. The book states plainly that volatility targeting improves risk-adjusted
performance.

> Rewritten on 2026-10-07 for this copy, after FINDINGS_1.md reported.
>
> **What this implies for Golden Flow: an untested lever, by design.** The rule has no risk model:
> each screen left out is a lever a later experiment has to earn
> ([`BLUEPRINT_1.md`](../../../Experiments/Experiment_1/BLUEPRINT_1.md), *Rules*). The golden cross
> already lowers volatility a little: 24.13% against 25.86% for the control. A volatility target
> would be tested against this rule in a new experiment, never added to it.

## 8. Stop-losses: the real cost is forgone profit, not commission

*(chapter 9, takeaways section 9.4)*

The book treats stop-loss policies as necessary — as a put against the option-like payoff a PM
holds, and as tail insurance — while being clear about the two costs: transaction costs from
de-grossing and re-grossing, and **performance degradation from profits given up**. Its conclusion
is that the second dominates the first. It also finds the difference between single-threshold and
two-threshold rules to be small, which is a useful licence not to over-engineer the rule.

> Rewritten on 2026-10-07 for this copy, after FINDINGS_1.md reported.
>
> **What this implies for Golden Flow: claim 1 pays this cost, and the findings show where.** The
> golden cross is the rule's exit; it runs no stop-loss besides. Its benefit is the drawdown:
> −32.47% against −46.32% for the control. Its cost is forgone profit: in 2023 to 2026 the names it
> kept out rose faster, and the control won that sub-period by 11.4 points a year
> ([`FINDINGS_1.md`](../../../Experiments/Experiment_1/FINDINGS_1.md), prediction 1). Neither side
> was tuned: the 50/200 pair is the most widely known one, taken as it is.

## 9. Execution: match position building to the alpha's horizon

*(section 8.3, takeaway section 8.6 #8)*

Build positions consistently with how long the alpha is expected to last; VWAP is called out as a
good heuristic; and the book's blunt aside is that most readers' participation rate is higher than it
ought to be.

> Rewritten on 2026-10-07 for this copy, after FINDINGS_1.md reported.
>
> **What this implies for Golden Flow: the first half is done; the second is a bound.** Golden Flow
> fills at each day's dividend-adjusted VWAP and pays commission on the unadjusted price, the
> heuristic the book recommends. Participation is stated, not modelled. At 1% of a name's 63-day
> traded value, the rule's own score, the worst trade allows a $238.6 million portfolio and the
> median $39.5 billion; at 5%, $1.19 billion and $197.5 billion
> ([`FINDINGS_1.md`](../../../Experiments/Experiment_1/FINDINGS_1.md), criterion 4). Golden Flow's
> turnover is 3.09 times its value a year, one way. Market impact is modelled nowhere in this
> repository.

## 10. Diversify as much as you can — but not more than that

*(section 8.2.2, takeaway section 8.6 #9)*

Diversification improves the Sharpe of a book with genuine skill, but the marginal benefit decays,
and past some point extra names dilute the edge without materially reducing risk.

> Rewritten on 2026-10-07 for this copy, after FINDINGS_1.md reported.
>
> **What this implies for Golden Flow: claim 3's bounds answer it, not a count.** No count is
> chosen. The 20% cap and the 1% floor hold a median of 37 names a day, 18 to 61, behaving like 19.0
> effective positions ([`FINDINGS_1.md`](../../../Experiments/Experiment_1/FINDINGS_1.md)). The
> sweep moves the floor: a Sharpe of 0.799 at 0.5%, 0.842 at 1% and 0.920 at 2%, each ahead of its
> own control. A higher floor holds fewer names, and here it did better. The floor stays at the
> owner's 1%: a floor picked from this sweep would be chosen on the metric it is judged by.

---

## Distilled into Golden Flow's language

> Rewritten on 2026-10-07 for this copy, after FINDINGS_1.md reported.
>
> | Book idea | What it implies for claims 1 to 3 |
> | --- | --- |
> | Momentum (relative) is not trend-following (absolute) | Claim 1 is a trend claim: the factor model sees 11.31 points of momentum in the rule's 137.35 points of excess return |
> | Momentum term structure: 1m reverses, 12-1 continues, >12m reverses | No claim: Golden Flow computes no return over a lookback |
> | Momentum's premium is partly tail-risk compensation | Long only, no short leg: a worst drawdown of −32.47% against the control's −46.32% |
> | Alpha estimates are noisy, betas are not | No error bar on the alpha; the residual selection is +2.70 points against the control's −0.27 |
> | **Selection / sizing / timing via counterfactual books** | **Run for claims 1 and 2.** Sizing: 0.842 against 0.722 equally weighted. Selection: above all 20 random books. Timing: not run |
> | Size by risk-adjusted alpha | Claim 2 sizes by traded value instead: a contradiction kept visible |
> | Volatility targeting improves risk-adjusted return | An untested lever, for a later experiment against this rule |
> | Stop-loss cost is forgone profit, not commission | Claim 1's cost: the control won 2023 to 2026 by 11.4 points a year |
> | VWAP execution, watch participation rate | VWAP fills; capacity stated as a participation bound, not modelled |
> | Diversify, but not past the point of dilution | Claim 3's bounds set the count: a median of 37 names a day, 19.0 effective |

## What this book does not settle for us

> Rewritten on 2026-10-07 for this copy, after FINDINGS_1.md reported.
>
> - It assumes a **factor risk model is available** and mostly discusses what to do with one. We
>   have the KN US Equity Factor Model through the attribution stage but not inside portfolio
>   construction, so the hedging and optimisation chapters (7, 11) are currently unreachable
>   machinery.
> - It is written for **long/short, factor-neutral, market-neutral** books. Golden Flow is long-only
>   and deliberately carries beta. Several recommendations — factor neutralisation before sizing
>   above all — would change the strategy into a different one rather than improve it.
> - It says nothing about **universe construction or survivorship**, which is step 2 here. For that,
>   see [`BIBLIOGRAPHY.md`](../../BIBLIOGRAPHY.md) Part 5.
> - It says nothing about **multiple testing or Sharpe deflation**, which is still open here: the
>   deflated Sharpe of the rule against its 107 trials was not computed. For that, see Part 5 as
>   well.
