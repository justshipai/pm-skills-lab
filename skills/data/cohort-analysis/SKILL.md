---
name: cohort-analysis
description: Use when analyzing retention or cohort data to understand whether the product keeps users and whether it's improving. Produces a read of the retention curve (does it flatten — the product-market-fit signal — or decay to zero?), compares cohorts over time, separates an acquisition problem from a retention problem, and recommends action — not a description of the numbers.
---

# Cohort analysis

Retention is the truest measure of whether a product delivers lasting value, and cohorts are how you read it without aggregate metrics lying to you (a growing top-of-funnel can mask terrible retention). This skill reads cohort/retention data the way a good growth PM does: the *shape* of the curve, whether it's getting better cohort-over-cohort, and what that implies for what to fix.

## The judgment this skill encodes

- **The curve's shape is the headline.** A retention curve that **flattens** (stabilizes at some % > 0) means a segment found durable value — the core PMF signal. A curve that **decays toward zero** means no lasting value yet; growth will leak out the bottom no matter how much you pour in. Read which one you have.
- **Where it flattens matters more than where it starts.** Early drop is normal (curious tire-kickers leave). The flattening level (the "retention floor") and how big that retained segment is = the real health signal.
- **Compare cohorts over time.** Are newer cohorts retaining better than older ones? Improving curves = your changes are working; flat-or-declining across cohorts = they aren't (or acquisition quality is dropping).
- **Acquisition problem vs. retention problem.** Low retention with high signups = a leaky bucket (fix retention before spending on growth). Good retention but low signups = an acquisition/awareness problem. Don't prescribe growth spend for a retention hole.
- **Segment the cohorts.** Retention often differs sharply by channel, plan, first-action, or persona — the aggregate curve hides a great segment and a terrible one. Find the segment that retains and ask what's different.
- **Watch the definition.** "Retained" = did what, in what window? (opened app vs. did the core action). N-day vs. rolling/bracket retention tell different stories. State it.

## Process

1. **Read the curve shape** — does it flatten (and at what level) or decay to zero? What does that imply?
2. **Compare cohorts** — are newer cohorts better/worse than older? Is retention trending up?
3. **Acquisition vs. retention** — which is the binding constraint here?
4. **Segment** — where does retention concentrate (channel/plan/first-action)?
5. **Recommend** — fix retention vs. scale acquisition; the segment to learn from; the next cut to look at.

## Output format

```
# <Product> — Cohort / Retention Analysis

## Curve shape & what it means   (flattens at X% = PMF signal / decays to zero = no durable value)
## Cohort-over-cohort trend       (are newer cohorts retaining better?)
## Acquisition vs. retention      (which is the binding constraint)
## Segment view                   (who retains; what's different about them)
## Recommendation                 (fix retention / scale acquisition; what to learn from the best segment)
## Definition note                (what "retained" means here; caveats)
```

## Anti-patterns to refuse

- Describing the numbers without reading the curve's shape → Say whether it flattens or decays, and why that matters.
- Treating early drop-off as the problem → Focus on the flattening level and the retained segment.
- Prescribing more acquisition when retention is the leak → Diagnose which is binding first.
- Aggregate curve only → Segment to find the retaining cohort.
- Ignoring how "retained" is defined → State the definition and its effect.
