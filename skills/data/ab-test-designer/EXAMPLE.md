# Example: ab-test-designer

## Input

> Design an A/B test: we want to test adding social-proof ("12,000 teams use this")
> to our signup page to lift signups. We get ~40,000 signup-page visits/week and
> ~4% sign up.

## Output

# Social Proof on Signup — A/B Test Design

## Hypothesis
Adding social proof to the signup page will increase the visit→signup conversion rate, because trust/validation reduces hesitation for first-time visitors.

## Metrics
- **Primary:** signup conversion rate (signups ÷ signup-page visits).
- **Guardrails (must not regress):** signup→activation rate (we don't want lower-intent signups), page load time, paid-conversion rate downstream.

## Baseline & MDE
- Baseline: **4.0%** conversion.
- **MDE: +0.5pp (4.0% → 4.5%, a ~12.5% relative lift)** — the smallest lift that would justify rolling this out and maintaining it. (Anything smaller isn't worth it here.)

## Sample size & duration
- For baseline 4%, detecting +0.5pp at α=0.05, power=80% (two-sided) needs **~24,000–30,000 visitors per variant** (~50–60k total). *(Standard two-proportion power calc; rule-of-thumb n ≈ 16·p(1−p)/MDE² per arm ≈ 16·0.04·0.96/0.005² ≈ 24.6k.)*
- At ~40k visits/week split 50/50 (~20k/arm/week), reaching ~25k/arm takes **~1.5 weeks → run 2 full weeks** (also covers weekly seasonality). If we needed +0.25pp instead, n quadruples (~100k/arm) → ~5 weeks; flag that as likely too long.

## Setup
- **Randomization unit: visitor** (cookie/device), held consistent across the session. 50/50 split. Target: all signup-page visitors. Instrument the primary + guardrail events before launch; QA assignment.

## Decision & stop rules
- **Run a fixed 2 weeks** (no early stopping on a "significant" peek). Ship if the primary lift is significant (p<0.05) and positive **and** no guardrail regresses (esp. activation). If flat/negative or activation drops → don't ship; iterate the message or placement.

## Traps to avoid
- No peeking-and-stopping (use the fixed window). Run ≥1 full week for seasonality. Only one primary metric (avoid multiple-comparison false positives). Watch novelty effect — a week-1 bump may fade, which is why we run two.
