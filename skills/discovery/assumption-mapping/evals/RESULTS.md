# Eval results — `assumption-mapping`

- **Run:** 2026-06-05 11:38 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.667 | 1.0 | +0.333 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `four-risks-covered` | ✅ pass | The output explicitly addresses all four product risks — Value (V1–V5), Usability (U1–U3), Feasibility (F1–F4), and Viability (Vi1–Vi5) — with dedicated sections and multiple assumptions under each. |
| `falsifiable-assumptions` | ✅ pass | Every assumption is written as 'We assume that…' with specific, testable conditions. The leap-of-faith table even includes explicit 'what would change our mind' thresholds (e.g., <15% tap rate, <20% users with 3+ friends, ≥30% negative reactions). |
| `impact-evidence-prioritization` | ✅ pass | Each assumption is tagged with impact (H/M) × evidence (L/M) ratings, and the leap-of-faith table explicitly filters to high-impact × low-evidence assumptions, ranking them and explaining why they are the riskiest. |
| `cheapest-tests` | ✅ pass | Every riskiest assumption is paired with a specific cheap test: cohort data pull + churned user interviews, fake-door CTA A/B test, Figma mockup interviews, analytics query, 2-hour legal review, half-day internal audit, and a financial model. No 'build the MVP' suggestions. |
| `value-viability-emphasis` | ✅ pass | Value assumptions dominate the leap-of-faith list (4 of 7 top assumptions), and Viability gets three dedicated high-impact assumptions including unit economics, legal exposure, and social collapse risk. Feasibility is relatively de-emphasized, correctly so. |
| `test-sequence` | ✅ pass | A detailed weekly test sequence is provided with explicit ordering rationale: 'speed to kill the idea if wrong → cost to run → dependencies between tests,' with kill signals at each stage and clear logic for why V4 and V3 must come first. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/discovery/assumption-mapping`._
