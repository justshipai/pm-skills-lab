---
name: model-selection
description: Use when choosing which model (or provider/tier) to use for an AI feature — weighing quality, cost, latency, context window, privacy/deployment, and lock-in. Produces an eval-driven decision matrix and a recommendation with sensitivity analysis, not "use the best model."
---

# Model selection

"Use the most capable model" is a non-decision. The right model is the cheapest, fastest one that **clears the quality bar for your specific task** under your real constraints. This skill turns model choice into a defensible decision: define the bar and the constraints first, score candidates against *your* eval, and recommend with the sensitivity made explicit.

## When to use

- Picking a model/provider/tier for a new AI feature.
- Re-evaluating after a price change, a new model release, or rising cost/latency.
- Justifying a model choice to engineering or finance.

Depends on: `llm-eval-set-designer` (you score candidates against a real eval set, not a public leaderboard). Feeds: `ai-pricing-model`, `staged-ai-rollout`.

## The judgment this skill encodes

- **Define the bar before you shop.** Minimum acceptable quality, latency budget, cost ceiling, and hard constraints (privacy/residency, context window, tool/function calling, fine-tuning, on-prem). A model that violates a hard constraint is out regardless of quality.
- **Score on your task, not a leaderboard.** Public benchmarks don't predict performance on your prompts and data. Run candidates against your own eval set.
- **Cheapest-that-clears-the-bar wins.** Once a model meets the quality bar, extra capability you can't use is wasted spend and latency.
- **Cost and latency are computed, not vibed.** Estimate cost/request from real token counts × price, and measure p50/p95 latency — at your expected volume.
- **Plan for portability.** Note lock-in (proprietary features, prompt-format coupling) and keep an exit. Models change monthly; your eval set lets you re-decide quickly.
- **Right-size by sub-task.** It's often correct to route easy cases to a cheap model and hard cases to a strong one. Consider a cascade.

## Process

1. **Constraints & bar.** Hard constraints (privacy, context, capabilities), minimum quality, latency budget, cost ceiling, expected volume.
2. **Candidates.** A shortlist spanning tiers (e.g. a frontier, a mid, a small/cheap, and an open option if relevant).
3. **Score quality on your eval set** (see `llm-eval-set-designer`) — per candidate, per bucket.
4. **Compute cost & latency** per request at expected volume; project monthly spend.
5. **Decision matrix** — quality, $/req, latency, constraint fit, lock-in.
6. **Recommendation + sensitivity** — what you'd pick, and what would change the answer (volume 10×, price change, quality bar moves). Consider a routing/cascade option.

## Output format

```
# <Feature> — Model Selection

## Constraints & quality bar       (hard constraints | min quality | latency budget | cost ceiling | volume)
## Candidates                       (and why each is on the list)
## Decision matrix
   | Model | Quality (vs bar, by bucket) | $/req | p50/p95 latency | Constraint fit | Lock-in |
## Cost projection                  (at expected volume; + at 10× volume)
## Recommendation
## Sensitivity / what would change this
## Re-evaluation trigger            (when to revisit)
```

## Anti-patterns to refuse

- "Use GPT-best / Claude-best." → Force a task-specific bar and the cheapest model that clears it.
- Ranking by public benchmark → Insist on scoring against the team's own eval set.
- Cost/latency as adjectives ("cheap", "fast") → Demand $/request and p50/p95 numbers at real volume.
- Ignoring a hard constraint (e.g. data residency) to chase quality → Constraints gate first.
