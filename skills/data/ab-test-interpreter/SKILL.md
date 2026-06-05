---
name: ab-test-interpreter
description: Use when reading the results of an A/B test and deciding what to do. Produces an interpretation that checks statistical AND practical significance, reads the confidence interval (not just the p-value), screens for the classic traps (peeking, underpowered, multiple comparisons, novelty, Simpson's paradox), and gives a defensible ship / iterate / stop call — not "B is higher, ship it".
---

# A/B test interpreter

"Variant B is higher, ship it" is how teams ship noise. Reading a test means asking whether the difference is real, whether it's big enough to matter, how uncertain it is, and whether anything contaminated the result. This skill turns raw results into a defensible decision.

## The judgment this skill encodes

- **Statistical ≠ practical significance.** A result can be significant but too small to matter (huge n), or a promising lift that's not yet significant (small n). Report both: is it real, *and* is it big enough to act on?
- **Read the confidence interval, not just p.** "+0.4pp, 95% CI [−0.1, +0.9]" tells you far more than "p=0.07" — it shows the plausible range, including whether "no effect" or "a meaningful effect" is still in play. Lead with the interval.
- **Check it was powered.** If the test couldn't have detected the MDE at this n, a null result is inconclusive, not "no effect." Underpowered + non-significant ≠ "they're the same."
- **Screen for the traps:**
  - *Peeking* — was it stopped early when it crossed significance? (inflates false positives)
  - *Multiple comparisons* — many metrics/variants/segments tested? (some "wins" are chance)
  - *Novelty/primacy* — is the early effect fading or ramping?
  - *Simpson's paradox / mix shift* — does the aggregate flip when you segment? Check the splits.
  - *Sample ratio mismatch* — is the split actually 50/50? If not, the randomization is broken; distrust the result.
  - *Guardrails* — did the win come at the cost of a guardrail metric?
- **Make a decision, with the reasoning.** Ship / iterate / stop / run-longer — and why, including the risk of being wrong. Don't just describe the numbers.
- **Beware the segment hunt.** A significant effect found only after slicing into post-hoc segments is a hypothesis, not a finding.

## Process

1. **Restate the test** — primary metric, what each arm got, n, the pre-set MDE if known.
2. **Significance & CI** — is the primary difference significant? What's the confidence interval / plausible range?
3. **Practical significance** — is the effect big enough to matter vs. the MDE / cost?
4. **Powered?** — could this n detect the MDE? If a null, is it conclusive?
5. **Trap screen** — peeking, SRM, multiple comparisons, novelty, Simpson's, guardrail breach.
6. **Decision** — ship / iterate / stop / extend, with the rationale and the risk.

## Output format

```
# <Test> — Results Interpretation

## The test               (primary metric, arms, n, pre-set MDE)
## Result                 (effect size + 95% CI; statistically significant?)
## Practical significance  (big enough to matter? vs MDE)
## Powered?               (could this n detect the MDE — is a null conclusive?)
## Trap screen            (peeking · SRM · multiple comparisons · novelty · Simpson's · guardrails)
## Decision               (ship / iterate / stop / extend — and why; risk of being wrong)
```

## Anti-patterns to refuse

- "B is higher, ship it" → Check significance, CI, practical size, and traps first.
- p-value with no confidence interval → Report the interval and plausible range.
- Treating a non-significant underpowered result as "no difference" → Flag it inconclusive.
- Accepting a post-hoc segment win at face value → Mark it a hypothesis to retest.
- Ignoring a guardrail regression because the primary won → Weigh the guardrail.
