# Eval results — `metric-drop-diagnoser`

- **Run:** 2026-06-05 16:10 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ➖ NO MEASURABLE LIFT — the with-skill output passes the rubric, but a strong no-skill baseline already does too on this scenario. This is **not** a failure: a single well-specified scenario can't show a skill's value when the base model already aces that exact prompt. The skill earns its keep through consistency across varied, messy, real-world inputs — which one-shot lift doesn't capture.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 1.0 | 1.0 | +0.0 | ❌ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `confirm-real-first` | ✅ pass | The response leads with a dedicated 'Is it real?' section that explicitly checks tracking pixel firing, dashboard definition changes, pipeline delays, payment processor cross-reference, and A/B misconfiguration before any causal theorizing. It even gives a binary decision rule: if orders in payments system are flat, stop and fix measurement. |
| `localize-by-segment` | ✅ pass | A full 'Localize' section covers app version/release, platform/OS, browser, device type, geography/locale, acquisition channel, new vs. returning users, payment method, and checkout funnel step — each with rationale and what a concentrated drop there would suggest. It also prioritizes which segments to pull first. |
| `timeline-vs-changes` | ✅ pass | A dedicated 'Timeline vs. changes' section systematically reviews code deploys, feature flags, third-party dependencies, pricing/promotions, UX/copy changes, marketing/traffic source, external platform changes, and seasonality — explicitly noting that even 'minor' or unannounced changes should be checked. |
| `mix-shift` | ✅ pass | A dedicated 'Mix shift?' section explains the mechanism clearly (aggregate rate falls with no individual segment worsening), lists common drivers (paid campaigns, email list changes, product category promotions, new user share spike), and provides a concrete method to check it. |
| `ranked-hypotheses-with-checks` | ✅ pass | The 'Ranked hypotheses' table lists 8 hypotheses in explicit priority order with likelihood ratings, specific verification methods, and estimated time to check each. A 'Start here' section further distills the top 3 immediate actions, making the starting point unambiguous. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/data/metric-drop-diagnoser`._
