---
name: north-star-metric
description: Use when defining a North Star Metric or the metric a team should rally around — and the input metrics beneath it. Produces a North Star that captures delivered customer value (not vanity or pure revenue), plus the 3-5 input metrics that teams can actually move, with the common failure modes (vanity, lagging, gameable) screened out.
---

# North Star Metric

A North Star Metric (NSM) is the single measure that best captures the value your product delivers to customers — the thing that, if it goes up, both customers and the business win. The classic mistakes: picking a vanity metric (total signups), a pure-business metric (revenue) that the team can't directly move, or one that's easily gamed. This skill defines a real NSM and the input-metric tree under it.

## The judgment this skill encodes

- **Measure delivered value, not activity.** The NSM should reflect customers *getting value*, which leads revenue rather than just counting it. Spotify's "time spent listening," not "accounts created." If your metric can rise while customers get nothing, it's wrong.
- **Not revenue, not vanity.** Revenue is the *result* of the NSM, not the NSM (teams can't move it directly and it lags). Totals that only ever go up (cumulative users, pageviews) are vanity — prefer rates and active/value-moments.
- **Leading, not lagging.** A good NSM moves *before* revenue and retention do, so it's an early signal the team can act on.
- **Hard to game without helping customers.** If there's a cheap way to inflate it that doesn't help users, redesign it. Pair it with a guardrail.
- **Build the input-metric tree.** Decompose the NSM into 3-5 inputs that teams own and can directly influence (e.g. breadth × depth × frequency × efficiency). The inputs are where roadmaps attach.
- **Name the business-model archetype.** Attention, transaction, productivity, marketplace — the right NSM shape differs (engagement time vs. successful transactions vs. tasks completed). Pick to fit.

## Process

1. **What value does the product deliver, and when does a customer feel it?** (the "value moment").
2. **Classify the business model** (attention / transaction / marketplace / productivity / SaaS) — to pick the right NSM shape.
3. **Propose the NSM** as a measure of that value moment, at a frequency (e.g. weekly active value-moments).
4. **Screen it:** is it vanity? lagging? gameable? Fix or pair with a guardrail.
5. **Decompose into 3-5 input metrics** the team can move; show the relationship (sum/product).
6. **Add guardrail metric(s)** that must not regress (e.g. quality, churn, cost).

## Output format

```
# <Product> — North Star Metric

## Value delivered & the value moment
## Business-model archetype
## North Star Metric          (the metric + why it captures value, not vanity/revenue)
## Input-metric tree           (3-5 inputs the team can move; how they combine)
## Guardrails                  (must-not-regress metrics)
## Screen                      (vanity? lagging? gameable? — and how this one passes)
```

## Anti-patterns to refuse

- Revenue / ARR as the NSM → It's the result; pick the value metric that drives it.
- Cumulative totals (signups, downloads, pageviews) → Swap for active/value-moment rates.
- A metric that rises without customers getting value → Redesign or add a guardrail.
- An NSM with no input tree → Add the 3-5 movable inputs; that's where work attaches.
