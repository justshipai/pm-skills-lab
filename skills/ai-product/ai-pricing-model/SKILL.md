---
name: ai-pricing-model
description: Use when pricing an AI feature or product where usage drives real marginal cost (tokens, inference, API calls) — choosing the pricing model, protecting margin, and aligning price to value. Produces a pricing recommendation with unit-economics math, margin analysis at the per-unit level, and guardrails against runaway cost — not just "charge a monthly fee".
---

# AI pricing model

Most SaaS has ~zero marginal cost, so pricing is pure value capture. AI is different: every request costs real money, and a heavy user can cost more than they pay. Pricing an AI feature is therefore a **unit-economics** problem first and a packaging problem second. This skill builds the model: the cost per unit of work, the pricing structure that keeps margin positive while still mapping to value, and the guardrails that stop a single user (or a prompt-injection loop) from torching your gross margin.

Uses cost inputs from `model-selection`. Pairs with `ai-success-metrics`.

## The judgment this skill encodes

- **Know your cost per unit of value first.** Compute the fully-loaded cost of one "job done" (tokens in/out × price, retries, retrieval, overhead). You cannot price what you can't cost.
- **Price the value unit, meter the cost unit.** Charge for the outcome the customer values (a resolved ticket, a generated doc, a seat) but track the underlying cost driver (tokens/calls) underneath it. Don't make customers reason about tokens unless they're developers.
- **Pick the structure deliberately:**
  - *Per-seat* — simple, predictable, but breaks when usage per seat varies wildly (power users lose you money).
  - *Usage-based / credits* — aligns price with cost, scales with value, but is less predictable for the buyer.
  - *Tiered with included allowance + overage* — the common sweet spot: predictable base, protected margin via overage.
  - *Outcome-based* — strongest value alignment, hardest to meter fairly.
- **Protect margin explicitly.** Set a target gross margin and check it at the unit level *and* for the worst-case heavy user. Include fair-use caps, rate limits, or overage so a whale can't go underwater.
- **Model the distribution, not the average.** Costs are long-tailed; the average user is profitable while the top 5% bleed you. Price for the tail.
- **Account for falling model costs.** Inference prices drop over time — decide whether that accrues to margin or to the customer, and don't lock into a structure that can't flex.
- **Sanity-check willingness-to-pay and the alternative.** Price against the value delivered and the customer's next-best option (do it manually, a competitor), not just cost-plus.

## Process

1. **Define the value unit** the customer buys and the **cost unit** underneath it.
2. **Compute unit cost** (tokens × price + retries + retrieval + overhead) for a typical and a heavy job.
3. **Set target gross margin** and the worst-case-user constraint.
4. **Choose the structure** (seat / usage / tiered+overage / outcome) and justify it.
5. **Stress-test margin** across the usage distribution (typical, p90, whale) — confirm no underwater segment.
6. **Add guardrails** (included allowance, overage, fair-use cap, rate limit).
7. **Recommend price points** with the value/WTP and competitive cross-check, plus what changes if model cost halves.

## Output format

```
# <Feature> — AI Pricing Model

## Value unit vs. cost unit
## Unit economics            (cost of a typical job and a heavy job; assumptions)
## Target margin & constraints
## Pricing structure          (choice + why; rejected alternatives)
## Margin stress test         (table: typical / p90 / whale → revenue, cost, margin)
## Guardrails                  (allowance, overage, fair-use cap, rate limit)
## Recommended price points    (+ value/WTP & competitive cross-check)
## Sensitivity                 (what changes if model cost or usage shifts)
```

## Anti-patterns to refuse

- A flat monthly price with no unit-cost math → Compute cost per job and stress-test the heavy user.
- Pricing on average usage → Model the distribution; price for the tail.
- Pure cost-plus with no value/WTP check → Cross-check against value and the alternative.
- Usage-based pricing exposed as raw tokens to non-technical buyers → Price the value unit, meter cost underneath.
- No fair-use cap or overage on an all-you-can-eat tier → Add a margin guardrail.
