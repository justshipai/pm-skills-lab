# Eval results — `decision-log`

- **Run:** 2026-06-05 13:57 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.95 | 1.0 | +0.05 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `decision-stated` | ✅ pass | First line and decision section state clearly: delay Android two quarters, redirect engineers to web performance. |
| `rationale-captured` | ✅ pass | Four numbered reasoning points explain why: revenue concentration on web, focused execution, mobile gap not yet critical, and bounded delay. Dissenting view also acknowledged. |
| `options-considered` | ✅ pass | Four options in a table with trade-offs: continue Android on schedule, partial split, full redirect (chosen), and hire/contract. Each has a stated reason for rejection. |
| `reversibility` | ✅ pass | Explicitly labeled as 'two-way door' with nuance: moderate cost, no technical lock-in, but mobile roadmap slips further with each quarter delayed. |
| `owner-and-date` | ✅ pass | Date (2025-07-11) and decider (Product/PM) both stated at the top. |
| `revisit-trigger` | ✅ pass | Four specific triggers listed (churn attributable to Android, early web goals met, competitive escalation, team growth) plus an explicit checkpoint date of end of Q3 2025. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/comms/decision-log`._
