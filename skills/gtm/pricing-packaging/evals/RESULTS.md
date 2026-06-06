# Eval results — `pricing-packaging`

- **Run:** 2026-06-06 11:05 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.944 | 1.0 | +0.056 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `value-based-not-cost-plus` | ✅ pass | Explicitly anchors pricing to recruiter labor saved ($300–$800/role, $1,500–$12,000/month), calls out the $3 infrastructure cost as the floor not the price, and directly argues against the $20 round-number with a detailed ROI framing and trust/signaling argument. |
| `value-metric` | ✅ pass | Systematically evaluates per-posting, flat, per-applicant, and per-seat options with a clear rationale table, selects per recruiter seat with explicit reasoning: scales with team size, expands naturally, intuitive to buyers. |
| `packaging-tiers` | ✅ pass | Designs three distinct tiers (Starter, Growth, Enterprise) with clearly named target buyers, feature differentiation, and seat-count boundaries for each. Includes who each tier is for and what features separate them. |
| `fences-anchoring` | ✅ pass | Provides a detailed fences table showing specific upgrade triggers (role caps, seat thresholds, integrations, compliance, SLA), explains anchoring via Enterprise-first positioning, and describes the natural expansion mechanic as teams grow. |
| `wtp-check` | ✅ pass | Explicitly recommends Van Westendorp survey with specific questions, flags competitor benchmarks as reference points, prescribes win/loss tracking with a target 20–30% pushback rate, and suggests annual vs. monthly uptake as a pricing signal. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/gtm/pricing-packaging`._
