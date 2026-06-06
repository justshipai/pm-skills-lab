---
name: gtm-strategy
description: Use when defining the go-to-market strategy for a product — how it reaches and wins customers. Produces a GTM where the sales motion is matched to the product's economics (price, time-to-value, complexity) — not a generic plan or a motion that contradicts the product. Covers ICP, the motion, channels that fit it, the core message, and the metric — anchored on motion-fit.
---

# GTM strategy

The fatal GTM mistake is a **motion mismatch** — running enterprise sales on a $15/mo self-serve product, or expecting PLG virality from a $100k platform that needs an implementation. The motion has to fit the product's economics. This skill builds a GTM anchored on that fit: pick the motion the product's price/value/complexity demands, then make the ICP, channels, message, and metric all serve it.

## The judgment this skill encodes

- **Motion fit is the keystone.** Match the sales motion to the economics:
  - *Low price, instant value, simple* → **product-led / self-serve** (in-product conversion, virality, low-touch).
  - *Mid ACV, some setup* → **sales-assisted / inside sales** (free trial + a human to close).
  - *High ACV, complex, multi-stakeholder* → **enterprise/field sales** (demos, POCs, RFPs, long cycles).
  A mismatch (e.g. a high-touch motion on a cheap product) burns money; flag it loudly.
- **Channels follow the motion, not the other way round.** PLG → SEO, community, integrations, in-product loops. Sales-led → outbound, partnerships, events, ABM. Don't bolt a channel that the motion can't support (e.g. a long enterprise cycle funded by impulse-buy ads).
- **CAC must fit the price.** You can't spend $5,000 to acquire a $20/mo customer. Sanity-check that the motion's cost of acquisition is recoverable by the price/LTV. This is the math that exposes most bad GTM plans.
- **ICP before channels.** Who exactly buys (and who's the user vs. the buyer), tied to the beachhead. (Pairs with `beachhead-segment`, `icp-definition`.)
- **One core message; let positioning lead.** Anchor on the positioning/value, not a feature tour. (Pairs with `positioning-statement`, `messaging-house`.)
- **Define the GTM metric and the first milestone.** What proves the motion works (e.g. self-serve conversion %, sales-qualified pipeline, payback period) and the near-term goal.

## Process

1. **Product economics** — price/ACV, time-to-value, complexity, who's involved in buying.
2. **Pick the motion** that fits — and call out any mismatch with what's been proposed.
3. **ICP** — the specific buyer/user (tied to beachhead).
4. **Channels** that fit the motion.
5. **Core message** — the positioning/value to lead with.
6. **Economics check + metric** — CAC vs. price/LTV sanity; the GTM metric + first milestone.

## Output format

```
# <Product> — GTM Strategy

## Product economics        (price/ACV, time-to-value, complexity, buying group)
## Motion                    (PLG / sales-assisted / enterprise — and why it fits; flag mismatches)
## ICP                       (buyer & user, tied to the beachhead)
## Channels                  (the ones that fit the motion)
## Core message              (positioning/value to lead with)
## Economics check & metric   (CAC vs price/LTV; the GTM metric + first milestone)
```

## Anti-patterns to refuse

- A generic GTM that ignores the product's economics → Anchor on motion fit.
- A motion that contradicts the price (enterprise sales on a cheap product, or vice versa) → Flag the mismatch and correct it.
- Channels that the motion can't support → Match channels to the motion.
- No CAC-vs-price sanity check → Add the economics math.
- "Market to everyone" → Anchor on the ICP/beachhead.
