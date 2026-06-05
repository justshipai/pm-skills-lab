# Eval results — `cohort-analysis`

- **Run:** 2026-06-05 16:08 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.9 | 1.0 | +0.1 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `reads-curve-shape` | ✅ pass | Explicitly states the curve decays toward zero with no flattening, uses the ski-slope-to-bottom analogy, and directly connects this to absence of durable value/PMF signal. |
| `cohort-trend` | ✅ pass | Directly compares A/B/C cohorts at M1, M3, and M6, notes retention is flat or slightly declining, and explicitly states no upward trajectory despite 3x signup growth. |
| `acquisition-vs-retention` | ✅ pass | Explicitly diagnoses leaky bucket, connects 3x signups + flat revenue to retention failure, and strongly warns against scaling paid acquisition into a non-retaining product with CAC/LTV logic. |
| `segment-and-action` | ✅ pass | Recommends segmenting by channel, first action, plan, and vertical with specific rationale for each; gives concrete next steps including interviewing M6 survivors and instrumenting M1 drop. |
| `definition-caveat` | ✅ pass | Notes 'active' is undefined, distinguishes login vs. core action definitions, flags N-month vs. survival window measurement differences, and recommends restating with core action definition. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/data/cohort-analysis`._
