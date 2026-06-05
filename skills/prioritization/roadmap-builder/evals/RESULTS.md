# Eval results — `roadmap-builder`

- **Run:** 2026-06-05 11:03 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.55 | 1.0 | +0.45 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `now-next-later` | ✅ pass | Explicitly organized into Now / Next / Later horizons with clear labels and no Gantt chart or fixed dates. |
| `outcome-anchored` | ✅ pass | Every item in all three horizons is framed as an outcome or problem statement with specific metrics called out (D30 retention, WAU, notes per session, sharing events, etc.). |
| `laddered-to-strategy` | ✅ pass | Strategy section explicitly states 'win with students' and all items are justified against student jobs-to-be-done (capture, retain, produce). Non-student items (calendar, templates) are deferred to Later with explicit rationale. |
| `confidence-convention` | ✅ pass | Explicitly labels Now as 'high confidence,' Next as 'medium confidence,' Later as 'low confidence / not a commitment.' The 'How to read this' section reinforces that outcomes are committed but solutions evolve and Later items are directional signals. |
| `now-focused` | ✅ pass | Now contains only two items with explicit rationale for keeping the list short. The bulk of the backlog is distributed across Next and Later. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/prioritization/roadmap-builder`._
