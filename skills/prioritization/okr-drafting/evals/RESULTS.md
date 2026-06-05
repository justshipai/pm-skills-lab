# Eval results — `okr-drafting`

- **Run:** 2026-06-05 11:01 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.542 | 0.875 | +0.333 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `objective-qualitative` | ✅ pass | Both objectives are qualitative, aspirational statements about user experience ('daily habit users genuinely look forward to opening', 'trusted, opt-in channel') with Q3 2025 time-bounding. Neither is a metric or a task. |
| `krs-are-outcomes` | ✅ pass | All KRs are behavioural metrics: sessions/user/week, DAU, D7 retention, feed engagement rate, opt-in rate, notification-driven session rate, opt-out rate. No feature shipping tasks are listed as KRs; the note explicitly calls out that shipping is excluded. |
| `baseline-to-target` | 🟡 partial | Most KRs have explicit baselines and targets. However, KR3 in Obj 1 and KR2/KR3 in Obj 2 list baselines as 'Establish baseline in wk 1' — these are unanchored at submission time. The document acknowledges this and provides a mitigation plan, but the criterion requires each KR to have a baseline, which three do not yet satisfy. |
| `laddering` | ✅ pass | A clear 'Ladders up to' section explicitly connects both objectives to the company goal of growing engagement across the product. |
| `guardrail` | ✅ pass | Each objective has explicit guardrails: crash rate ≤0.5% and uninstall rate not increasing for Obj 1; push send volume ≤5/user/week and app store rating floor for Obj 2. These prevent gaming the KRs by degrading other dimensions. |
| `not-vanity-not-sandbagged` | ✅ pass | Raw totals are explicitly avoided (no total sessions, no MAU, no total pushes). DAU is the one absolute number but paired with per-user rates. Targets (~35% session lift, 23% DAU lift, 10pp opt-in) are stretch but contextually justified. The document proactively flags the rationale for each target. |
| `focused` | ✅ pass | Two objectives, four KRs in Obj 1 and three in Obj 2 — within the 1-3 objectives / 3-5 KRs guideline. The set is coherent and thematically tight. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/prioritization/okr-drafting`._
