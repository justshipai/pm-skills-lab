# Eval results dashboard

Every skill ships with a scenario eval. The default harness (`scripts/run_evals.py`) runs each scenario twice — once with no skill (baseline), once with the skill — and an LLM judge scores both against the rubric. Alternative controlled runners follow the same comparison and document their method in the per-skill results. Per-skill detail, including per-criterion verdicts, lives in each skill's `evals/RESULTS.md`.

**Status key:** ✅ **verified** = the skill passes every scenario and beats the baseline on aggregate. ➖ **no measurable lift** = the skill passes, but a strong base model already matches it unaided. ❌ **not verified** = the with-skill output fails one or more required scenarios.

**42 verified · 15 no-lift (strong baseline) · 0 not verified · 57/57 run.**

| Skill | Status | Baseline | With skill | Last run |
|---|---|---|---|---|
| `agent-capability-spec` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-05 10:30 UTC |
| `ai-feature-spec` | ✅ verified | 0.893 | 1.0 | 2026-06-05 10:33 UTC |
| `check-what-ai-built` | ✅ verified | 0.9822 artifact avg (4/4 pass) | 1.0000 artifact avg (4/4 pass) | 2026-08-21 16:28 UTC |
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
| `ab-test-designer` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-05 16:04 UTC |
| `ab-test-interpreter` | ✅ verified | 0.8 | 1.0 | 2026-06-05 16:05 UTC |
| `cohort-analysis` | ✅ verified | 0.9 | 1.0 | 2026-06-05 16:08 UTC |
| `funnel-analysis` | ✅ verified | 0.7 | 1.0 | 2026-06-05 16:07 UTC |
| `metric-drop-diagnoser` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-05 16:10 UTC |
| `accessibility-audit` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-05 15:09 UTC |
| `ai-interface-patterns` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-05 15:25 UTC |
| `data-viz-design` | ✅ verified | 0.722 | 1.0 | 2026-06-05 15:26 UTC |
| `design-critique` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-05 15:10 UTC |
| `prototype-brief` | ✅ verified | 0.864 | 1.0 | 2026-06-05 15:04 UTC |
| `ui-states-matrix` | ✅ verified | 0.95 | 1.0 | 2026-06-05 15:06 UTC |
| `ux-heuristic-audit` | ✅ verified | 0.7 | 1.0 | 2026-06-05 15:07 UTC |
| `assumption-mapping` | ✅ verified | 0.667 | 1.0 | 2026-06-05 11:38 UTC |
| `interview-script` | ✅ verified | 0.682 | 1.0 | 2026-06-05 11:32 UTC |
| `interview-synthesizer` | ✅ verified | 0.727 | 1.0 | 2026-06-05 11:34 UTC |
| `opportunity-solution-tree` | ✅ verified | 0.318 | 1.0 | 2026-06-05 11:36 UTC |
| `activation-finder` | ✅ verified | 0.7 | 1.0 | 2026-06-05 16:25 UTC |
| `growth-experiment-backlog` | ✅ verified | 0.727 | 1.0 | 2026-06-05 16:31 UTC |
| `growth-loop` | ✅ verified | 0.85 | 1.0 | 2026-06-05 16:23 UTC |
| `referral-mechanic` | ✅ verified | 0.85 | 1.0 | 2026-06-05 16:27 UTC |
| `retention-lifecycle` | ✅ verified | 0.8 | 1.0 | 2026-06-05 16:29 UTC |
| `beachhead-segment` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-06 11:07 UTC |
| `gtm-strategy` | ➖ no measurable lift (strong baseline) | 1.0 | 1.0 | 2026-06-06 11:12 UTC |
| `launch-tiering` | ✅ verified | 0.95 | 1.0 | 2026-06-06 11:09 UTC |
| `messaging-house` | ✅ verified | 0.75 | 1.0 | 2026-06-06 11:14 UTC |
| `pricing-packaging` | ✅ verified | 0.944 | 1.0 | 2026-06-06 11:05 UTC |
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
