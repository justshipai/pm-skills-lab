# Example: ab-test-interpreter

## Input

> Read our A/B test result: control conversion 4.0% (n=20,000), variant 4.3%
> (n=20,000). The dashboard says p=0.11. We also noticed variant wins big for
> mobile users specifically. Should we ship?

## Output

# Signup Variant — Results Interpretation

## The test
Primary: signup conversion. Control 4.0% (n=20k) vs variant 4.3% (n=20k) — a **+0.3pp absolute (+7.5% relative)** lift. Dashboard p=0.11.

## Result
- Effect: **+0.3pp**, 95% CI roughly **[−0.07pp, +0.67pp]**. p=0.11 → **not statistically significant** at 0.05. The interval still includes ~0, so we can't rule out "no effect."

## Practical significance
+0.3pp (+7.5% rel) *would* be worth shipping if real — so this isn't a "too small to care" case; it's a "not yet proven" case. The point estimate is promising.

## Powered?
At baseline 4% and n=20k/arm, the test is powered (~80%) to detect roughly +0.5pp; a true effect of +0.3pp is **smaller than the MDE**, so it's unsurprising it didn't reach significance. The test was slightly underpowered for the effect we're actually seeing — a null here is **inconclusive, not "no effect."**

## Trap screen
- **The mobile "win" is a post-hoc segment** — found by slicing after the fact, across presumably several segments → high chance of a false positive (multiple comparisons). Treat it as a *hypothesis*, not a result.
- Check **sample ratio**: 20k/20k looks clean (no SRM).
- No sign of peeking stated, but confirm it ran the full pre-set window.
- Check the guardrail (activation) before any ship.

## Decision
**Don't ship yet; extend the test (or re-run) to reach the sample size needed for ~+0.3pp** (roughly 2–3× the current n per arm), and pre-register the mobile hypothesis as the next test rather than shipping on the segment. The trend is encouraging but unproven; shipping now risks shipping noise. If extending isn't feasible, iterate the variant to aim for a larger, detectable effect.
