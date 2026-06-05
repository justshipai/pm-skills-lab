---
name: funnel-analysis
description: Use when analyzing a conversion funnel to find where users drop off and what to do about it. Produces an analysis that finds the biggest leak, quantifies the prize (how many users/$ a realistic fix recovers), segments to see who drops, forms hypotheses for the drop, and recommends where to focus — not just restating the funnel percentages.
---

# Funnel analysis

A funnel table tells you the numbers; analysis tells you *where to spend effort and what it's worth*. The failure mode is restating the percentages ("step 2→3 is 40%") with no prioritization. This skill finds the leak that matters most, sizes the opportunity in real terms, and turns it into where-to-focus — so the funnel drives a decision.

## The judgment this skill encodes

- **Find the biggest leak by opportunity, not just the biggest %drop.** The step with the worst conversion isn't always the best target — weight by *volume through it* and *how fixable it looks*. A 50% drop late in a thin funnel may matter less than a 20% drop at the top where everyone is.
- **Quantify the prize.** "If we lift step 2→3 from 40% to 50%, that's +X users/month reaching the end (≈ $Y)." Sizing the opportunity is what makes it prioritizable against everything else.
- **Segment the drop.** A funnel average hides the story — drop-off usually differs by device, channel, new vs. returning, geo, plan. Look for *where* the leak concentrates; the fix is often segment-specific.
- **Separate "didn't proceed" from "couldn't."** A drop can be intent (not interested → maybe fine) or friction/breakage (wanted to, couldn't → fixable and urgent). Diagnose which.
- **Form hypotheses, then say how to check.** For the priority leak, a few plausible causes and the cheapest way to confirm (session replays, an event check, a quick survey, a test) — not a guess presented as fact.
- **Mind funnel-definition traps.** Time windows, whether steps are strictly sequential, counting users vs. sessions, and survivorship — a "funnel" computed wrong tells a false story.

## Process

1. **Lay out the funnel** — steps, counts, step and overall conversion.
2. **Identify the priority leak** — by opportunity (volume × drop × fixability), not just worst %.
3. **Quantify the prize** — what a realistic improvement at that step is worth (users / $).
4. **Segment** — where does the drop concentrate (device/channel/cohort)?
5. **Hypothesize & check** — likely causes for the priority leak + the cheapest way to validate each.
6. **Recommend focus** — where to act first and the next diagnostic step.

## Output format

```
# <Funnel> — Analysis

## The funnel             (steps, counts, step % and overall %)
## Priority leak          (which step, and why it's the priority — volume × drop × fixability)
## Opportunity size       ("lift step X from a% to b% → +N users/mo ≈ $Z")
## Segment view           (where the drop concentrates)
## Hypotheses & how to check   (likely causes + cheapest validation)
## Recommendation         (where to focus first; next diagnostic)
```

## Anti-patterns to refuse

- Restating the percentages with no prioritization → Identify the priority leak by opportunity.
- Targeting the biggest %drop reflexively → Weight by volume and fixability.
- No opportunity sizing → Quantify the prize in users/$.
- Funnel average only → Segment the drop.
- Asserting the cause → Give hypotheses + how to confirm cheaply.
