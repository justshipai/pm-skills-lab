---
name: activation-finder
description: Use when finding a product's activation metric / "aha moment" — the early behavior that predicts long-term retention. Produces the candidate behavior most correlated with retention, a "magic number" threshold, an explicit correlation-vs-causation warning with the experiment to confirm it, and how to use it as an activation target — not a guessed vanity action.
---

# Activation finder

The activation metric — the early action (and threshold) that best predicts a user becoming a retained user — is the highest-leverage thing in growth: it tells onboarding and the whole top of the funnel what to drive toward. The classic examples (Facebook "7 friends in 10 days", Slack "2,000 messages", Twitter "30 follows") are *measured*, not guessed. This skill finds the candidate from data, sets the threshold, and — critically — keeps you honest about correlation vs. causation.

## The judgment this skill encodes

- **It's the behavior that best predicts retention — found in data, not chosen by intuition.** Compare early actions by how strongly doing them correlates with surviving to your retention horizon. The winner is the activation candidate.
- **Find the "magic number" threshold.** Often it's not "did X" but "did X ≥ N times within T days." Look for the point where the retention curve sharply separates (do-it vs. don't, and how much).
- **Correlation ≠ causation — say it loudly.** Heavy early usage correlates with retention partly because *already-committed users do more*. Adding the behavior to onboarding may not cause retention. The honest output flags this and proposes an **experiment** (drive the behavior for a random group, measure retention lift) before betting the roadmap on it.
- **Prefer a leading, soon, controllable behavior.** Activation should be early (week 1, not month 3), reachable in onboarding, and something the product can nudge. A predictor you can't influence isn't an activation metric.
- **Avoid vanity proxies.** "Signed up", "opened the app", "completed onboarding" usually predict little. Look for the behavior that reflects *getting value* (created/shared/connected something real).
- **One activation metric.** Pick the single best predictor as the target; a basket dilutes focus.

## Process

1. **List candidate early behaviors** (from the data provided or proposed) and what each plausibly signals.
2. **Rank by correlation with retention** — which best separates retained from churned.
3. **Set the magic-number threshold** (action × count × time window) where retention diverges.
4. **Causation check** — explicitly warn correlation≠causation; design the experiment to confirm the behavior *drives* retention.
5. **Make it the activation target** — what onboarding should drive toward, and the guardrail (don't game the metric without delivering value).

## Output format

```
# <Product> — Activation Metric

## Candidate behaviors        (and what each signals)
## Best predictor              (the behavior most correlated with retention — and the evidence)
## Magic number                ("X ≥ N within T days" — where the retention curve separates)
## Correlation vs. causation   (the warning + the experiment to confirm it causes retention)
## Use as activation target    (what onboarding drives toward; guardrail against gaming)
```

## Anti-patterns to refuse

- Guessing an activation metric from intuition → Derive it from correlation with retention.
- A vanity action (signed up / opened app) as activation → Use a value-reflecting behavior.
- Asserting the behavior *causes* retention → Flag correlation≠causation; propose the experiment.
- "Did X" with no threshold → Find the magic number (count + window).
- A basket of activation metrics → Pick the single best predictor.
