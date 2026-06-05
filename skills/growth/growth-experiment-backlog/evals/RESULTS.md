# Eval results — `growth-experiment-backlog`

- **Run:** 2026-06-05 16:31 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.727 | 1.0 | +0.273 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `hypotheses-not-tasks` | ✅ pass | Every experiment is explicitly framed as 'If X then metric Y because Z' — the table column header even labels this and each row follows the format consistently. |
| `stage-and-metric` | ✅ pass | Each experiment has a dedicated Stage column (Activation, Retention, Acquisition, Referral) and the specific metric to move is stated in both the hypothesis and the detailed success-metric tables for top experiments. |
| `ice-scored-and-sequenced` | ✅ pass | All seven experiments have explicit Impact/Confidence/Ease scores with calculated ICE product scores, and a clear sprint-based run order with rationale for sequencing decisions is provided. |
| `targets-constraint` | ✅ pass | The output explicitly names Day-1 churn/activation as the constraint in the opening section, places activation/retention experiments #1–3 at the top of the ICE ranking and sprint order, and explicitly defers/deprioritizes the web version (#7, ICE 48) and influencer campaigns (#6, ICE 80) with clear reasoning that they burn budget against a leaky funnel. |
| `learning-value-and-decision` | ✅ pass | A Learning Value column is included for all experiments with qualitative framing, and the top 3 experiments each have explicit win bars (with significance thresholds and sample sizes), 'if win' escalation paths, and 'if lose' diagnostic decisions that define what to do next. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/growth/growth-experiment-backlog`._
