# Eval results — `ai-feature-spec`

- **Run:** 2026-06-05 10:33 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.893 | 1.0 | +0.107 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `evaluation-plan` | ✅ pass | Defines a 100-note stratified golden dataset with dual human annotators and a rubric, specific precision/recall/hallucination thresholds, offline eval before launch, LLM-as-judge calibration procedure, and multiple online signals (edit rate, delete rate, add rate, thumbs) with alert thresholds. |
| `graceful-fallback` | ✅ pass | Enumerates distinct fallback paths: API failure shows toast + retry + inline manual template; empty array shows editable table with participant names; note too long shows word count + section-select affordance; user ignoring feature leaves note unchanged. Manual template always available independent of AI. |
| `failure-modes-guardrails` | ✅ pass | Table lists 8 specific failure modes (hallucination, wrong owner, missed items, invented date, empty response, timeout, too-long note, prompt injection) each paired with likelihood, detection mechanism, and concrete mitigation. |
| `non-ai-baseline` | ✅ pass | Explicitly describes the non-AI baseline (manual Action Items table/template), explains why it has low adoption, articulates why regex/keyword rules fail on free-form prose, and sets a measurable bar the AI must clear versus the template to justify shipping. |
| `uncertainty-and-reversibility` | ✅ pass | Source quote citations with highlight link, warning icon when quote unmatched, null fields shown as editable placeholders, list opens in editable state, inline field editing, undo on save-to-note, panel never writes to note until confirmed, confirmation prompt on edited discard. |
| `cost-latency` | ✅ pass | Explicit p50 < 4s and p95 < 8s latency budgets per stage, unit cost calculated (~$0.001-0.002/extraction), daily cost projection at 10K extractions, rate-limit tiers (20/day free, 100/day paid), auto-alert at $500/day, throttle at $1,000/day, mobile network condition testing required. |
| `success-metrics-multi-dimensional` | ✅ pass | Primary metrics span adoption (% users trying feature), repeat usage, acceptance rate, and satisfaction (thumbs up). Guardrail metrics separately track delete rate, latency, cost, data incidents, and core editor crash rate with explicit breach thresholds. |
| `staged-rollout` | ✅ pass | Four explicit phases: shadow/dogfood (logged, not shown), closed beta (~500 opt-in users), 10% canary, GA — each with duration, numeric gate criteria, and a kill switch triggerable in <5 minutes via feature flag with an automatic trigger on delete-rate spike. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/ai-product/ai-feature-spec`._
