# Eval results — `activation-finder`

- **Run:** 2026-06-05 16:25 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.7 | 1.0 | +0.3 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `data-driven-best-predictor` | ✅ pass | Explicitly selects 'invited ≥1 teammate who joined' at 78% vs 35% baseline, presents the full comparison table, and calls it 'not a close call' with a +43pp gap. |
| `rejects-vanity` | ✅ pass | Explicitly dismisses 'created an account' as 'baseline — no signal beyond signup' and notes all other behaviors including uploading/commenting can be solo sessions delivering no collaboration value. |
| `magic-number-threshold` | ✅ pass | Defines a specific threshold: '≥1 teammate invite accepted within 7 days of signup' with a clear time window, and even suggests tightening to 72 hours pending further data analysis. |
| `correlation-causation-experiment` | ✅ pass | Dedicates a full section to the confound (motivated/team-mandated users), then proposes a concrete A/B experiment with treatment/control design, randomization unit, primary metric (day-60 retention), secondary metrics, and interpretation of both positive and null results. |
| `use-as-target` | ✅ pass | Recommends it as the onboarding activation target, notes the ~20% current rate with headroom, provides concrete day-by-day onboarding interventions, and includes a guardrail (teammate must join, not just be invited) with gaming detection signals. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/growth/activation-finder`._
