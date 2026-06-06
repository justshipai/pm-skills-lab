---
name: pricing-packaging
description: Use when setting or revising pricing and packaging for a product or feature. Produces value-based pricing built on a value metric and good-better-best packaging — with fences, anchoring, and a willingness-to-pay check — not cost-plus or a number picked by gut or "what competitors charge".
---

# Pricing & packaging

Pricing is the highest-leverage growth lever and the least-analyzed — most teams set it by adding margin to cost, copying a competitor, or guessing. This skill designs pricing from **value**: what the customer gets, the metric that scales price with that value, the packaging that segments willingness-to-pay, and the psychological structure that makes the right plan obvious. Packaging (what's in which tier) usually matters more than the number.

## The judgment this skill encodes

- **Value-based, not cost-plus.** Anchor price to the value delivered / the alternative's cost, not your COGS. Cost sets a floor, not the price. (For AI features with real marginal cost, pair with `ai-pricing-model`.)
- **Choose a value metric.** The unit you charge by should scale with the value the customer gets (seats, usage, contacts, GMV, outcomes). A good value metric grows the bill as the customer succeeds — and feels fair.
- **Packaging segments willingness-to-pay.** Good-better-best (3 tiers) lets different segments self-select; the middle is usually the target, anchored by a premium tier. Decide *what goes in which tier* (the fences) deliberately — that's where the money is.
- **Design the fences.** Features/limits that separate tiers should map to willingness-to-pay and usage intensity, nudging growing customers to upgrade naturally (expansion).
- **Use anchoring and a decoy if honest.** A high anchor tier reframes the middle as reasonable; a sensible enterprise/"contact us" tier anchors up. Don't manipulate — structure for clarity.
- **Check willingness-to-pay, don't assume it.** Reference WTP research (Van Westendorp, surveys, the value calc, competitor benchmarks) — or flag that it needs validating before committing. (Pairs with a WTP analysis.)
- **Mind the model fit.** Per-seat vs. usage vs. flat vs. outcome — match it to how value accrues and how the buyer wants to budget. Avoid pricing that punishes adoption.

## Process

1. **Value & alternative** — what the customer gains; the cost of their next-best option (sets the ceiling).
2. **Value metric** — the unit to charge by that scales with value and feels fair.
3. **Packaging** — good-better-best (or the right structure); who each tier is for.
4. **Fences** — what separates tiers (features/limits) and drives expansion.
5. **Price points & anchoring** — the numbers, with the anchor logic; how the middle is made obvious.
6. **WTP check** — evidence the prices match willingness-to-pay (or what to validate).

## Output format

```
# <Product> — Pricing & Packaging

## Value & the alternative      (what they gain; next-best-option cost = ceiling)
## Value metric                  (the unit we charge by, and why it's fair/scaling)
## Packaging (good-better-best)   (the tiers + who each is for)
## Fences & expansion            (what separates tiers; what drives upgrades)
## Price points & anchoring       (the numbers + the anchor logic)
## Willingness-to-pay check        (evidence / what to validate before committing)
```

## Anti-patterns to refuse

- Cost-plus or "pick a number" → Anchor to value and the alternative.
- One flat price for everyone → Package good-better-best to segment WTP.
- A value metric that punishes usage/adoption → Pick one that scales with value.
- Copying a competitor's price → Use it as one input; price to your value.
- Assuming WTP → Reference or flag the need for WTP evidence.
