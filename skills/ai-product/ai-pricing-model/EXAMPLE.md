# Example: ai-pricing-model

## Input

> We're adding an AI feature to our design tool: "generate a first-draft design
> from a text prompt." Each generation calls an image model. We're on a $20/mo
> Pro plan today. How should we price the AI feature?

## Output

# AI Design Generation — Pricing Model

## Value unit vs. cost unit
- **Value unit the customer buys:** a usable generated design ("a generation").
- **Cost unit underneath:** model inference per generation (incl. retries/variants).

## Unit economics
- Typical generation: 4 variants × ~$0.04 inference = **~$0.16/generation** (loaded with retries/storage ≈ $0.20).
- Heavy user: 30 generations/day × 22 days = 660/mo → **~$132/mo cost** for one seat.
- Assumption: inference at current provider price; revisit if it drops.

## Target margin & constraints
- Target **≥ 75% gross margin** on the AI feature.
- Constraint: **no seat goes underwater** — a $20 Pro seat must not cost us $132 in inference.

## Pricing structure
**Tiered: included monthly allowance + usage credits for overage.** Rejected:
- *Pure per-seat (bundle into $20):* the whale at $132 cost destroys margin. ✗
- *Raw usage-based (charge per generation):* hurts adoption of a "play with it" creative feature; buyers hate per-action friction. ✗
- *Outcome-based:* no clean billable outcome for design exploration. ✗

## Margin stress test
| Segment | Generations/mo | Incl. in plan | Overage rev | Inference cost | Margin |
|---|---|---|---|---|---|
| Typical | 40 | 50 (free in Pro) | $0 | ~$8 | bundled — fine within Pro ARPU |
| p90 | 150 | 50 | 100 × $0.30 = $30 | ~$30 | ~50% on overage; OK |
| Whale | 660 | 50 | 610 × $0.30 = $183 | ~$132 | ~28% — **positive, not underwater** ✓ |

## Guardrails
- **50 generations/mo included** in Pro (covers the typical user, drives adoption).
- **Overage credits at $0.30/generation** (≈75% margin at typical cost; protects margin as usage scales).
- **Soft rate limit** (e.g. burst cap/min) to stop runaway scripts/abuse.
- Optional **"unlimited-ish" add-on** with a fair-use ceiling for power users who prefer predictability.

## Recommended price points
- Keep generation **in Pro with a 50/mo allowance**; sell overage credits ($0.30 each, discounted in packs).
- **Value/WTP cross-check:** a usable first-draft design saves ~15–30 min; at typical designer rates, $0.30 is trivially worth it — pricing is well below value, leaving room.
- **Competitive cross-check:** comparable tools meter generations similarly; our included allowance is a positioning advantage.

## Sensitivity
- If inference cost **halves**, hold the $0.30 price → margin rises to ~85% (accrue to margin now, pass to customers later as a competitive lever).
- If typical usage doubles, raise the included allowance only if ARPU supports it; otherwise the overage model already protects us.
