---
name: ab-test-designer
description: Use when designing an A/B test or experiment — before launching it. Produces a test design with a clear hypothesis, one primary metric plus guardrails, the baseline rate, a minimum detectable effect, the required sample size and duration (so it's actually powered), the randomization unit, and pre-committed stop/decision rules — not "split traffic and see which wins".
---

# A/B test designer

Most A/B tests are designed to be inconclusive: no stated effect size, no sample-size math, so they run until someone eyeballs a winner (which is how false positives ship). This skill designs a test that can actually produce a trustworthy decision — powered to detect the effect you care about, with the decision rules set *before* you look at the data.

## The judgment this skill encodes

- **One primary metric. Plus guardrails.** Pick the single metric the decision hinges on. Add guardrail metrics that must not regress (revenue, latency, churn, quality). Many primary metrics = no decision.
- **State the hypothesis and the effect you'd act on.** "We believe X will increase [metric] by ≥ Y%." The **minimum detectable effect (MDE)** is a product decision — the smallest lift worth shipping — and it drives the whole design.
- **Do the sample-size math up front.** Required n depends on baseline rate, MDE, significance (α, usually 0.05) and power (usually 80%). Compute it (or give the formula/assumptions) → then **duration = n ÷ traffic**. If you can't reach n in a reasonable time, the test is underpowered — say so and propose a bigger MDE or a different approach.
- **Name the randomization unit** (user, not page-view, usually) and check for assignment leakage / contamination.
- **Pre-commit the decision rules.** Ship if primary significant & positive and no guardrail breach; iterate/stop otherwise. Set the duration in advance and **don't peek-and-stop** (inflates false positives) — or use a sequential test if you must monitor.
- **Mind the classic traps:** peeking, multiple-comparisons (many metrics/variants), novelty/primacy effects, weekly seasonality (run ≥ 1 full week), and segment cherry-picking after the fact.

## Process

1. **Hypothesis** — change → expected effect on the primary metric, and why.
2. **Metrics** — primary (1) + guardrails (must-not-regress).
3. **Baseline & MDE** — current rate; the smallest effect worth shipping.
4. **Power & sample size** — required n per variant (α, power, baseline, MDE) → **duration** at expected traffic.
5. **Setup** — randomization unit, variants/split, targeting, instrumentation.
6. **Decision & stop rules** — pre-committed ship/iterate/stop; fixed duration / sequential; guardrail breach = stop.

## Output format

```
# <Test> — A/B Test Design

## Hypothesis
## Metrics              (primary: 1 · guardrails: must-not-regress)
## Baseline & MDE       (current rate; smallest lift worth shipping)
## Sample size & duration   (n/variant from baseline, MDE, α=0.05, power=80%; → run length at <traffic>)
## Setup                (randomization unit, split, targeting, instrumentation)
## Decision & stop rules    (pre-committed ship/iterate/stop; duration; no-peeking)
## Traps to avoid       (peeking, multiple comparisons, novelty, seasonality)
```

## Anti-patterns to refuse

- "Split traffic and see which converts better" → Add hypothesis, primary metric, MDE, sample size.
- No sample-size / duration math → Compute required n and run length (or flag underpowered).
- Many primary metrics → Pick one; the rest are guardrails or secondary.
- "Stop when it's significant" → Pre-commit duration or use a sequential method; no peeking.
- No guardrails → Add the must-not-regress metrics.
