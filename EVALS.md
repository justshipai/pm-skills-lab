# Eval results dashboard

Every skill ships with a scenario eval. The harness (`scripts/run_evals.py`) runs each scenario twice — once with no skill (baseline), once with the skill — and an LLM judge scores both against the rubric. Per-skill detail (incl. per-criterion verdicts) lives in each skill's `evals/RESULTS.md`.

**Status key:** ✅ **verified** = the skill passes the rubric *and* beats the baseline. ➖ **no measurable lift** = the skill passes, but a strong base model already aces this scenario unaided — not a failure, just a task where one-shot lift can't show the skill's value (consistency across varied inputs). ❌ **not verified** = the with-skill output didn't pass the rubric.

**29 verified · 10 no-lift (strong baseline) · 0 not verified · 39/39 run.**

| Skill | Status | Baseline | With skill | Last run |
|---|---|---|---|---|
| `agent-capability-spec` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-05 10:30 UTC |
| `ai-feature-spec` | ✅ verified | 0.893 | 1.0 | 2026-06-05 10:33 UTC |
| `ai-prd` | ✅ verified | 0.731 | 1.0 | 2026-06-05 10:39 UTC |
| `ai-pricing-model` | ✅ verified | 0.955 | 1.0 | 2026-06-05 10:42 UTC |
| `eval-rubric-designer` | ✅ verified | 0.773 | 1.0 | 2026-06-05 10:44 UTC |
| `hallucination-risk-register` | ✅ verified | 0.955 | 1.0 | 2026-06-05 10:47 UTC |
| `human-in-the-loop-design` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-05 10:49 UTC |
| `llm-eval-set-designer` | ✅ verified | 0.885 | 1.0 | 2026-06-05 10:53 UTC |
| `model-selection` | ✅ verified | 0.75 | 1.0 | 2026-06-05 10:55 UTC |
| `staged-ai-rollout` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-05 10:57 UTC |
| `decision-log` | ✅ verified | 0.95 | 1.0 | 2026-06-05 13:57 UTC |
| `meeting-notes-actions` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-05 13:57 UTC |
| `pre-mortem` | ✅ verified | 0.864 | 1.0 | 2026-06-05 13:56 UTC |
| `retrospective` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-05 13:59 UTC |
| `stakeholder-map` | ✅ verified | 0.9 | 1.0 | 2026-06-05 10:59 UTC |
| `weekly-update` | ✅ verified | 0.9 | 1.0 | 2026-06-05 13:54 UTC |
| `accessibility-audit` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-05 15:09 UTC |
| `design-critique` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-05 15:10 UTC |
| `prototype-brief` | ✅ verified | 0.864 | 1.0 | 2026-06-05 15:04 UTC |
| `ui-states-matrix` | ✅ verified | 0.95 | 1.0 | 2026-06-05 15:06 UTC |
| `ux-heuristic-audit` | ✅ verified | 0.7 | 1.0 | 2026-06-05 15:07 UTC |
| `assumption-mapping` | ✅ verified | 0.667 | 1.0 | 2026-06-05 11:38 UTC |
| `interview-script` | ✅ verified | 0.682 | 1.0 | 2026-06-05 11:32 UTC |
| `interview-synthesizer` | ✅ verified | 0.727 | 1.0 | 2026-06-05 11:34 UTC |
| `opportunity-solution-tree` | ✅ verified | 0.318 | 1.0 | 2026-06-05 11:36 UTC |
| `competitive-battlecard` | ✅ verified | 0.95 | 1.0 | 2026-06-05 14:18 UTC |
| `competitor-teardown` | ✅ verified | 0.95 | 1.0 | 2026-06-05 14:16 UTC |
| `market-sizing` | ✅ verified | 0.9 | 1.0 | 2026-06-05 14:12 UTC |
| `porters-five-forces` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-05 14:20 UTC |
| `positioning-statement` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-05 14:13 UTC |
| `okr-drafting` | ✅ verified | 0.542 | 0.875 | 2026-06-05 11:01 UTC |
| `rice-scorer` | ✅ verified | 0.25 | 1.0 | 2026-06-05 11:02 UTC |
| `roadmap-builder` | ✅ verified | 0.55 | 1.0 | 2026-06-05 11:03 UTC |
| `prd-generator` | ✅ verified | 0.917 | 1.0 | 2026-06-05 11:06 UTC |
| `north-star-metric` | ✅ verified | 0.95 | 1.0 | 2026-06-05 13:32 UTC |
| `playing-to-win` | ✅ verified | 0.7 | 1.0 | 2026-06-05 13:37 UTC |
| `product-strategy-canvas` | ✅ verified | 0.818 | 1.0 | 2026-06-05 13:38 UTC |
| `product-vision` | ✅ verified | 0.75 | 1.0 | 2026-06-05 13:31 UTC |
| `working-backwards` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-05 13:34 UTC |
