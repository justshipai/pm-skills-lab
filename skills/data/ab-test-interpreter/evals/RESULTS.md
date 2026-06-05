# Eval results — `ab-test-interpreter`

- **Run:** 2026-06-05 16:05 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.8 | 1.0 | +0.2 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `significance-and-uncertainty` | ✅ pass | Explicitly computes z-score, p-value, and 95% CI [+0.1pp, +1.7pp], notes the wide range and that the lower bound is nearly negligible, conveying uncertainty well beyond just comparing point estimates. |
| `catches-peeking` | ✅ pass | Dedicates a critical-flag section to peeking, explains how repeated checks inflate false positive rates to 20-30%+, flags the 5-day run as too short, and notes the day-2 spike as a specific red flag for novelty effects. |
| `guardrail-revenue` | ✅ pass | Explicitly flags lower revenue-per-order as a guardrail breach, quantifies the risk (e.g., RPO down 2-3% could offset conversion lift), states net revenue could be flat or negative, and makes it a blocking condition for shipping. |
| `powered-check` | ✅ pass | Calculates that the detectable MDE at 80% power for n=5,000/arm is ~1.0pp, notes the observed +0.9pp is below that threshold, concludes the test was slightly underpowered, and recommends 7,000+ per arm for a cleaner read. |
| `clear-decision` | ✅ pass | Issues an unambiguous 'Do not ship' recommendation with four numbered rationale points, provides a structured next-steps table, and explicitly acknowledges the risk of being wrong (losing 2+ weeks of potential upside) while explaining why the delay is acceptable. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/data/ab-test-interpreter`._
