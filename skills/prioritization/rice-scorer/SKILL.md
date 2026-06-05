---
name: rice-scorer
description: Use when prioritizing a list of features, ideas, or initiatives with the RICE framework (Reach × Impact × Confidence ÷ Effort). Produces a scored, ranked table with each factor estimated in consistent units and a sanity-check pass — not a vibes-based ranking dressed up with numbers.
---

# RICE scorer

RICE forces a prioritization argument into four explicit factors so trade-offs are visible and debatable: **Reach × Impact × Confidence ÷ Effort.** Its value is the discipline, not the decimal — a RICE score is an input to judgment, not a verdict. This skill scores a backlog consistently and then sanity-checks the ranking instead of treating the number as truth.

## The framework (use these definitions consistently)

- **Reach** — how many people/events this affects in a fixed time window (e.g. users per quarter). Use the *same* window for every item, and a real count, not a 1–10 guess.
- **Impact** — how much it moves the goal per person, on a standard scale: **3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal.**
- **Confidence** — how sure you are of the Reach/Impact/Effort estimates: **100% = high, 80% = medium, 50% = low.** Below 50% means "go gather evidence," not "score it anyway."
- **Effort** — total person-time (person-months or person-weeks), all functions included. The only denominator.
- **Score = (Reach × Impact × Confidence) ÷ Effort.**

## The judgment this skill encodes

- **Consistency over precision.** The same time window, the same impact scale, the same effort unit across every item — otherwise scores aren't comparable.
- **Reach is a count, not a rating.** Pull it from data where possible; state the assumption when estimated.
- **Confidence is the bullshit detector.** A huge score riding on 50% confidence is a flag to run a cheap test, not to ship.
- **Effort includes everyone.** Design, eng, QA, GTM — not just dev days.
- **Sanity-check the ranking.** After scoring, eyeball it: does anything strategic-but-low-reach get unfairly buried? Does a tiny quick win top a critical bet? RICE doesn't capture strategy, dependencies, or sequencing — call those out.

## Process

1. **Set the units:** the reach time window, effort unit, and confirm the impact/confidence scales.
2. **Score each item** on Reach, Impact, Confidence, Effort, noting the assumption behind each estimate.
3. **Compute** the RICE score and rank.
4. **Sanity-check:** flag low-confidence/high-score items for validation; note strategic items RICE under-rates; note dependencies/sequencing the raw score ignores.
5. **Recommend** a priority order — score-informed, judgment-final.

## Output format

```
# <Backlog> — RICE Prioritization

## Units & assumptions          (reach window | effort unit | scales)
## Scores
   | Item | Reach | Impact | Confidence | Effort | RICE score | Key assumption |
## Ranked order
## Sanity check                  (low-confidence flags | strategic items RICE under-rates | dependencies)
## Recommendation
```

## Anti-patterns to refuse

- Reach as a 1–10 rating → Use a real count over a fixed window.
- Impact/confidence on ad-hoc scales → Use the standard scales above.
- Effort = dev days only → Include all functions.
- Treating the top score as the decision → Add the sanity-check and name what RICE misses.
- Scoring items at <50% confidence as if solid → Flag them for a cheap test first.
