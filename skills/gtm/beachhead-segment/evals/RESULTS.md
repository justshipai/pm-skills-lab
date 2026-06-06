# Eval results — `beachhead-segment`

- **Run:** 2026-06-06 11:07 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ➖ NO MEASURABLE LIFT — the with-skill output passes the rubric, but a strong no-skill baseline already does too on this scenario. This is **not** a failure: a single well-specified scenario can't show a skill's value when the base model already aces that exact prompt. The skill earns its keep through consistency across varied, messy, real-world inputs — which one-shot lift doesn't capture.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 1.0 | 1.0 | +0.0 | ❌ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `rejects-broad` | ✅ pass | Explicitly and forcefully pushes back on the 'everyone' framing with four specific reasons (messaging, CAC, competition, word-of-mouth) and calls it 'a trap.' Scores it lowest in the table and dedicates a full section to rejecting it. |
| `criteria-based-choice` | ✅ pass | Uses a scored matrix with six explicit beachhead criteria (urgent pain, reachable, referenceable, big enough, winnable, leads to adjacent) applied consistently to all candidate segments, with rationale for each score and written justification for the winner on every criterion. |
| `concrete-segment` | ✅ pass | Picks 'Operations managers / BizOps leads at Series A–C SaaS companies (50–300 employees, US) building internal tools' — specific who (BizOps/RevOps lead), specific situation (3+ month engineering backlog of internal tool requests), specific company stage and size. |
| `expansion-path` | ✅ pass | Names two explicit next pins: mid-market ops teams (300–2,000 employees) and franchise/multi-location operators, with explanation of why each follows naturally from the beachhead win. |
| `says-no` | ✅ pass | Explicitly de-prioritizes all four runner-up segments (franchise operators, insurance agencies, enterprise IT, freelance designers) with specific reasons for each, and separately rejects the broad horizontal option with detailed reasoning. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/gtm/beachhead-segment`._
