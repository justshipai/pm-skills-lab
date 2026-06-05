# Eval results — `ab-test-designer`

- **Run:** 2026-06-05 16:04 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ➖ NO MEASURABLE LIFT — the with-skill output passes the rubric, but a strong no-skill baseline already does too on this scenario. This is **not** a failure: a single well-specified scenario can't show a skill's value when the base model already aces that exact prompt. The skill earns its keep through consistency across varied, messy, real-world inputs — which one-shot lift doesn't capture.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 1.0 | 1.0 | +0.0 | ❌ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `hypothesis-and-primary-metric` | ✅ pass | Clear directional hypothesis stated ('3-step flow will increase onboarding completion rate by at least 3 pp') with a single named primary metric (onboarding completion rate defined precisely as % reaching final confirmation screen). |
| `sample-size-and-duration` | ✅ pass | Shows the two-proportion z-test formula with all inputs (p1=0.55, p2=0.58, α=0.05, power=80%), computes ~3,490 per variant / ~6,980 total, then divides by weekly traffic (7,000/week) to arrive at ~1 week, recommending 2 weeks for guardrail observability and seasonality coverage. Sensitivity to different MDEs also shown. |
| `mde-stated` | ✅ pass | MDE explicitly stated as +3 pp absolute (55%→58%), with rationale for why smaller effects would not justify shipping, and sensitivity note for alternative MDEs (+1 pp, +5 pp). |
| `guardrails` | ✅ pass | Three guardrail metrics defined: Day-7 retention, Day-1 activation rate, and account setup completeness. Each has a directional rule ('must not drop') and a quantitative threshold (baseline − MoE at 95% CI). Guardrail breach blocks shipping regardless of primary metric outcome. |
| `decision-and-no-peeking` | ✅ pass | Pre-committed decision table covers all outcome scenarios. Explicitly prohibits early stopping for positive primary results, allows early stopping only for guardrail harm, mentions sequential/alpha-spending methods if continuous monitoring is required, and fixes Day 14 as the sole readout date. |
| `randomization-and-traps` | ✅ pass | Randomization unit specified as User ID (not session/device), persistent server-side assignment noted, cross-device leakage addressed. Traps table covers peeking, multiple comparisons, novelty effect, seasonality, segment cherry-picking, primacy effects, and guardrail lag. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/data/ab-test-designer`._
