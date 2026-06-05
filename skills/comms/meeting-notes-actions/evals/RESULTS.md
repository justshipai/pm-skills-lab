# Eval results — `meeting-notes-actions`

- **Run:** 2026-06-05 13:57 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ➖ NO MEASURABLE LIFT — the with-skill output passes the rubric, but a strong no-skill baseline already does too on this scenario. This is **not** a failure: a single well-specified scenario can't show a skill's value when the base model already aces that exact prompt. The skill earns its keep through consistency across varied, messy, real-world inputs — which one-shot lift doesn't capture.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 1.0 | 1.0 | +0.0 | ❌ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `three-buckets` | ✅ pass | Output is clearly separated into Decisions, Action Items, and Open Questions sections with no prose summary. |
| `decisions-as-outcomes` | ✅ pass | States 'API prioritized over reporting dashboard for Q3. Dashboard moves to Q4.' as a concrete outcome, not as 'we discussed prioritization'. |
| `actions-owner-date` | ✅ pass | Each action item has an owner and due date. Jordan/Next Tuesday, Morgan/TBD, and the export bug row flags 'TBD — needs assignment' and TBD for date, appropriately marking unknowns. |
| `open-questions` | ✅ pass | Both unresolved items (export bug fix date and design resource for API docs) are captured as open questions rather than dropped or treated as decided. |
| `faithful-no-invention` | ✅ pass | No dates or owners are fabricated. The export bug fix date is flagged as missing, TBD is used where information is absent, and no unsupported claims are made. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/comms/meeting-notes-actions`._
