---
name: opportunity-solution-tree
description: Use when connecting a desired outcome to what to build — mapping opportunities and solutions, or when a team is jumping straight to features. Produces a Teresa Torres Opportunity Solution Tree (outcome → opportunities → solutions → experiments) that forces solutions to attach to a real, evidenced user need before anyone commits to building.
---

# Opportunity Solution Tree (OST)

Teams jump to solutions. The OST (Teresa Torres) is the antidote: it makes you map the **opportunities** — the user needs, pains, and desires — *between* your outcome and your solutions, so every idea has to earn its place by addressing a real, evidenced need. This skill builds that tree from an outcome and whatever discovery evidence you have.

## The structure (four levels)

1. **Outcome** (root) — the single measurable business/product outcome you're driving (not a feature, not a metric salad).
2. **Opportunities** — user needs, pains, and desires that, if addressed, would move the outcome. Phrased in the **user's** voice, sourced from discovery. Grouped/nested from broad to specific.
3. **Solutions** — ideas that address a *specific* opportunity (not the outcome directly).
4. **Experiments** — the cheapest tests that would validate whether a solution actually addresses its opportunity.

## The judgment this skill encodes

- **One clear outcome at the root.** If you have three outcomes, you have three trees. Pick the one this work serves.
- **Opportunities are needs, not solutions in disguise.** "Faster onboarding" is a solution; "I can't tell if the product is working for me in week one" is an opportunity. Phrase as the user's experience.
- **Ground opportunities in evidence.** Each should trace to something from discovery (an interview, a behavior, support data). Flag the ones that are assumptions, not evidence.
- **Solutions attach to one opportunity.** If a solution doesn't map to a specific opportunity, either you've found a new opportunity or the solution is a solution in search of a problem.
- **Compare solutions within an opportunity, not across the whole tree.** The tree's power is letting you weigh 3 ways to address *the same* need.
- **Experiments test the riskiest assumption cheaply.** Tie each promising solution to the smallest test that would change your mind.

## Process

1. **State the outcome** at the root (measurable, singular).
2. **Map opportunities** from discovery evidence; phrase in the user's voice; group broad → specific; flag evidence vs. assumption.
3. **Generate solutions** under specific opportunities (a few per opportunity worth exploring).
4. **Attach experiments** to the most promising/riskiest solutions.
5. **Recommend a path** — which opportunity to target first and why (impact on outcome × evidence strength), and what to test next.

## Output format

```
# <Outcome> — Opportunity Solution Tree

## Outcome (root)
## Opportunity space
   - Opportunity A (user-voice need) — evidence: <source> / ⚠ assumption
       - Solution A1 → Experiment: <cheapest test>
       - Solution A2 → Experiment: …
   - Opportunity B …
## Recommended path        (which opportunity first, why; riskiest assumption to test)
```
(A text tree is fine; indentation shows the hierarchy.)

## Anti-patterns to refuse

- Skipping straight from outcome to a feature list → Insert the opportunity layer.
- Opportunities written as solutions ("add a dashboard") → Rephrase as the underlying need.
- Opportunities with no evidence and no flag → Mark them assumptions to validate.
- Multiple outcomes at the root → Split into separate trees.
- Solutions with no experiment → Add the cheapest validating test.
