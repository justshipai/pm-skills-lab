# Example: activation-finder

## Input

> Help us find our activation metric. We're a recipe app. Week-1 behaviors and the
> % of each group still active at day 30:
> - Opened the app ≥1×: 31% retained (it's ~everyone)
> - Completed onboarding: 33% retained
> - Saved ≥1 recipe: 38% retained
> - Saved ≥3 recipes in week 1: 64% retained
> - Cooked (marked complete) ≥1 recipe in week 1: 71% retained
> Overall retention is 30%. ~25% of new users cook a recipe in week 1.

## Output

# Recipe App — Activation Metric

## Candidate behaviors
- *Opened / completed onboarding* — vanity; ~everyone does it, barely beats baseline (31–33% vs 30%). Signals nothing.
- *Saved a recipe* — mild signal (38%).
- *Saved ≥3 in week 1* — strong (64%).
- *Cooked ≥1 recipe in week 1* — strongest (71% vs 30% overall). Reflects actually getting the product's value (a cooked meal), not just browsing.

## Best predictor
**Cooked (marked complete) ≥1 recipe in week 1.** It separates retention most sharply — 71% vs 30% overall — and it's the behavior that maps to real value delivered, not activity. (Saving ≥3 is a good secondary/leading signal toward it.)

## Magic number
**"Cook ≥1 recipe within the first 7 days."** That's where the retention curve diverges hardest. Worth checking ≥2 vs ≥1 to see if a higher threshold separates further, but ≥1 cooked already more than doubles retention.

## Correlation vs. causation
**Big caveat:** cooking correlates with retention partly because already-committed users cook — we can't yet say *making* someone cook in week 1 causes them to retain. Before we rebuild onboarding around it, **run an experiment:** for a random subset of new users, actively drive toward cooking one recipe in week 1 (nudges, an easy starter recipe, reminders) and compare day-30 retention to a holdout. If the treated group retains meaningfully better, it's causal and worth scaling.

## Use as activation target
Make **"cooked a recipe in week 1"** the activation target onboarding optimizes for (only ~25% hit it today → big headroom). Onboarding should funnel toward picking and cooking one easy recipe fast. **Guardrail:** don't game it (e.g. auto-marking "cooked") — the metric only matters if a real meal happened; track downstream retention to keep it honest.
