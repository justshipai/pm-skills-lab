---
name: roadmap-builder
description: Use when building or restructuring a product roadmap — turning a feature list or set of goals into a Now/Next/Later, outcome-based roadmap. Produces a roadmap organized around the problems/outcomes to pursue (with confidence decreasing over the horizons), not a dated Gantt chart of features that becomes a promise you can't keep.
---

# Roadmap builder

A roadmap should communicate *intent and direction*, not a contractual delivery schedule. The classic failure is a timeline of dated features: it over-promises, gets out of date instantly, and frames the team around output instead of outcomes. This skill builds a **Now / Next / Later** roadmap organized around the outcomes you're pursuing, where certainty is high for Now and deliberately loose for Later.

## The framework

- **Now** — actively being worked or starting imminently; high confidence; specific.
- **Next** — the likely next set once Now ships; medium confidence; framed as problems/bets.
- **Later** — directional; low confidence; themes and big bets, explicitly subject to learning.

Each item is anchored to an **outcome** (the user/business problem it addresses and the metric it should move), not just a feature name.

## The judgment this skill encodes

- **Organize by outcome, not feature.** "Reduce time-to-first-value" with candidate solutions beats "build onboarding wizard." Outcomes survive when the solution changes.
- **Horizons, not dates.** Now/Next/Later sets expectations honestly; specific quarters/dates invite them to be read as commitments. Use dates only where a real external deadline exists.
- **Confidence decreases over the horizons — say so.** Later is a hypothesis, not a plan. Make the uncertainty explicit so stakeholders don't treat Later as promised.
- **Tie each item to a goal/metric.** If you can't say which outcome an item serves, question why it's on the roadmap.
- **It's a communication tool — frame it for the audience.** A roadmap is a narrative about where the product is going and why, not a backlog dump.
- **Keep Now small.** A "Now" column with fifteen items isn't a roadmap, it's a wish. Focus.

## Process

1. **Clarify the goal(s)/strategy** the roadmap serves.
2. **Translate inputs into outcomes** — for each feature/idea, name the problem and the metric it should move.
3. **Place items in Now / Next / Later** by confidence and readiness; keep Now focused.
4. **For each item:** the outcome, candidate solution(s), and the goal/metric it ladders to.
5. **State the confidence convention** and that Next/Later will shift with learning.
6. **(Optional) Note key dependencies or external deadlines.**

## Output format

```
# <Product> — Roadmap (Now / Next / Later)

## Strategy this serves
## Now            (high confidence)
   - <Outcome> — candidate: <solution> — moves: <metric>
## Next           (medium confidence)
   - <Outcome / problem to tackle> — moves: <metric>
## Later          (directional, low confidence)
   - <Theme / bet>
## How to read this   (confidence convention; Next/Later evolve with learning)
## Dependencies / external dates (if any)
```

## Anti-patterns to refuse

- A dated Gantt of features → Convert to Now/Next/Later outcomes.
- Items named as features with no outcome/metric → Add the problem and metric each serves.
- A "Now" column stuffed with everything → Force focus.
- Presenting Later as if it's committed → State the decreasing-confidence convention.
