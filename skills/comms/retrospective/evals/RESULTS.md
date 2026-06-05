# Eval results — `retrospective`

- **Run:** 2026-06-05 13:59 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ➖ NO MEASURABLE LIFT — the with-skill output passes the rubric, but a strong no-skill baseline already does too on this scenario. This is **not** a failure: a single well-specified scenario can't show a skill's value when the base model already aces that exact prompt. The skill earns its keep through consistency across varied, messy, real-world inputs — which one-shot lift doesn't capture.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 1.0 | 1.0 | +0.0 | ❌ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `root-cause` | ✅ pass | Applies iterative 'why' analysis to all three key issues (Sales blindsided, slow incident resolution, late delivery), arriving at specific systemic root causes: no ownership of stakeholder communication, no pre-launch readiness gate, no mid-cycle scope checkpoint. Goes clearly beyond symptom listing. |
| `concrete-owned-actions` | ✅ pass | Three actions, each with a named owner (PM, Engineering Lead, PM), a clear deliverable, and a stated purpose. Small, focused set rather than a wish list. |
| `blameless` | ✅ pass | Explicitly frames all failures as process gaps, not individual fault. Closing note directly states 'not about effort or intent' and attributes problems to three process gaps. |
| `keep-what-worked` | ✅ pass | Calls out standups as genuinely useful with a note to preserve the format, and notes the core feature shipped and works. Both are framed as things to continue. |
| `observations-vs-actions` | ✅ pass | Document is clearly structured: observations → iterative why → root cause → separate improvements table. Causes and actions are in distinct sections with no conflation. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/comms/retrospective`._
