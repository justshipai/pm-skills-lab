# Eval results dashboard

Every skill ships with a scenario eval. This table shows, for each skill, whether it **measurably beats the no-skill baseline** when run through `scripts/run_evals.py`. A skill is **verified** only when its treatment run passes the rubric and scores higher than the baseline on every scenario. Per-skill detail lives in each skill's `evals/RESULTS.md`.

**Status: 11 verified · 15/15 run · 0 not yet run.**

| Skill | Status | Baseline | With skill | Last run |
|---|---|---|---|---|
| `agent-capability-spec` | ✅ verified | 0.636 | 0.864 | 2026-06-05 08:51 UTC |
| `ai-feature-spec` | ✅ verified | 0.25 | 0.857 | 2026-06-05 08:53 UTC |
| `ai-prd` | ❌ not verified | 0.423 | 0.692 | 2026-06-05 08:55 UTC |
| `ai-pricing-model` | ✅ verified | 0.818 | 0.909 | 2026-06-05 08:56 UTC |
| `eval-rubric-designer` | ✅ verified | 0.773 | 0.909 | 2026-06-05 08:58 UTC |
| `hallucination-risk-register` | ✅ verified | 0.955 | 1.0 | 2026-06-05 09:00 UTC |
| `human-in-the-loop-design` | ✅ verified | 0.909 | 0.955 | 2026-06-05 09:02 UTC |
| `llm-eval-set-designer` | ❌ not verified | 0.962 | 0.808 | 2026-06-05 09:04 UTC |
| `model-selection` | ❌ not verified | 0.917 | 0.875 | 2026-06-05 09:05 UTC |
| `staged-ai-rollout` | ❌ not verified | 1.0 | 1.0 | 2026-06-05 09:07 UTC |
| `stakeholder-map` | ✅ verified | 0.8 | 1.0 | 2026-06-05 09:09 UTC |
| `okr-drafting` | ✅ verified | 0.542 | 0.875 | 2026-06-05 09:10 UTC |
| `rice-scorer` | ✅ verified | 0.2 | 1.0 | 2026-06-05 09:12 UTC |
| `roadmap-builder` | ✅ verified | 0.55 | 1.0 | 2026-06-05 09:13 UTC |
| `prd-generator` | ✅ verified | 0.542 | 0.958 | 2026-06-05 09:15 UTC |
