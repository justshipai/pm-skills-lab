# Eval results — `ux-heuristic-audit`

- **Run:** 2026-06-05 15:07 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.7 | 1.0 | +0.3 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `systematic-heuristics` | ✅ pass | Explicitly evaluates all 10 Nielsen heuristics in a structured table, addressing each principle individually rather than ad-hoc opinions. Every heuristic is numbered and labeled with a corresponding issue or confirmation of compliance. |
| `severity-ratings` | ✅ pass | Each issue is assigned a numeric severity (0–4) in the table and reinforced in the Must-Fix and Minor sections. Ratings are used to differentiate P0/P1/P2/P3 priorities and separate catastrophic from cosmetic issues. |
| `concrete-fixes` | ✅ pass | Every issue is paired with specific, actionable fixes: e.g., 'type DELETE confirmation', '30-second undo window or 7-day deactivation grace period', 'success toast within 2s', 'sticky jump-nav sidebar', 'collapse Danger zone by default behind disclosure toggle'. No vague advice like 'make it clearer'. |
| `domain-specific-catches` | ✅ pass | Catches all three key domain-specific issues: delete account needing confirmation/re-auth/grace period (H3+H5), long toggle list needing grouping with category headers and master toggles (H4+H7), and save preferences needing status feedback via toasts and error states (H1+H9). |
| `prioritized` | ✅ pass | Explicitly separates Severity 3–4 Must-Fix from Severity 1–2 Minor/Cosmetic issues, and provides a dedicated prioritized action table ranking items P0 through P3 with the most severe issues surfaced first. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/design/ux-heuristic-audit`._
