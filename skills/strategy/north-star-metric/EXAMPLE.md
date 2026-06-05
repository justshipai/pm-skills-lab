# Example: north-star-metric

## Input

> We're a marketplace connecting home cooks with people who want home-made meals.
> What should our North Star Metric be?

## Output

# Home-cooked Marketplace — North Star Metric

## Value delivered & the value moment
The value moment is **a meal successfully delivered and enjoyed** — an eater gets a good home-cooked meal, a cook earns money. Value isn't "an order placed"; it's an order *fulfilled and rated well*.

## Business-model archetype
**Two-sided marketplace** (transaction). NSM should reflect *successful transactions*, balanced across both sides, not raw GMV or signups.

## North Star Metric
**Weekly well-rated meals delivered** (meals delivered per week that the eater rated ≥4★). This captures delivered value on both sides, leads revenue (more good meals → more repeat → more GMV), and resists gaming (you can't inflate it without cooks actually delivering meals people liked).

Why not the obvious alternatives: *GMV* is the result and lags; *orders placed* ignores cancellations/bad experiences; *signups* is pure vanity.

## Input-metric tree
Weekly well-rated meals ≈ **active eaters × orders per eater × fulfillment rate × % rated ≥4★**
- **Active eaters/week** (demand) — growth & retention own this.
- **Orders per active eater** (frequency) — merchandising, reminders.
- **Fulfillment rate** (cook supply & reliability) — supply team owns this.
- **% meals rated ≥4★** (quality) — quality/trust team.

## Guardrails
- Cook earnings per active cook (supply health — must not fall).
- Cancellation/refund rate (must not rise).

## Screen
Vanity? No — it's a rate of value-delivered, not a cumulative total. Lagging? No — it moves weekly, ahead of revenue. Gameable? Hard — inflating it requires real, well-rated deliveries; the quality threshold + guardrails block the obvious hacks.
