# Eval results — `porters-five-forces`

- **Run:** 2026-06-05 14:20 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ➖ NO MEASURABLE LIFT — the with-skill output passes the rubric, but a strong no-skill baseline already does too on this scenario. This is **not** a failure: a single well-specified scenario can't show a skill's value when the base model already aces that exact prompt. The skill earns its keep through consistency across varied, messy, real-world inputs — which one-shot lift doesn't capture.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 1.0 | 1.0 | +0.0 | ❌ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `all-five-forces` | ✅ pass | All five forces are explicitly analyzed with dedicated sections: competitive rivalry, threat of new entrants, supplier power, buyer power, and threat of substitutes. Each goes beyond listing competitors to analyze structural dynamics. |
| `rated-with-reasoning` | ✅ pass | Every force receives a clear High/Medium rating with explicit structural drivers. Reasoning is detailed — e.g., buyer power HIGH due to zero switching costs and promo-hopping; rivalry HIGH due to fixed costs + slow growth + high exit barriers. |
| `substitutes-identified` | ✅ pass | A dedicated table identifies real substitutes solving the need differently: traditional grocery, grocery delivery, prepared meal delivery, restaurant delivery, meal planning apps, and frozen/rotisserie options — not just direct meal-kit rivals. |
| `overall-read` | ✅ pass | A clear summary table rates all five forces, identifies the market as structurally unattractive, and pinpoints where margins are destroyed — specifically the buyer power + rivalry combination that forces perpetual discounting and CAC spend. Cites Blue Apron and HelloFresh data. |
| `implications` | ✅ pass | Strong strategic implications section explicitly recommends against standard market entry, identifies three alternative strategic angles (niche verticals, lock-in mechanisms, supply-side partnerships), and provides guardrails if proceeding. Ends with a clear recommended stance. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/market/porters-five-forces`._
