# Eval results — `positioning-statement`

- **Run:** 2026-06-05 14:13 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ➖ NO MEASURABLE LIFT — the with-skill output passes the rubric, but a strong no-skill baseline already does too on this scenario. This is **not** a failure: a single well-specified scenario can't show a skill's value when the base model already aces that exact prompt. The skill earns its keep through consistency across varied, messy, real-world inputs — which one-shot lift doesn't capture.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 1.0 | 1.0 | +0.0 | ❌ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `competitive-alternatives` | ✅ pass | Explicitly tables six named alternatives including status-quo spreadsheets/email, do-nothing/honor system, and ERP-native modules, with clear explanation of who uses each and why the status quo is the primary competitive frame for a small challenger. |
| `attributes-to-value` | ✅ pass | Lists six candidate differentiating attributes and maps each one to a concrete customer benefit ('so what') in a dedicated table, culminating in a unifying value theme. The translation is specific, not generic (e.g., 'stops being a manual copy-paste job,' 'stop chasing people for receipts at month end'). |
| `best-fit-segment` | ✅ pass | Names a specific segment (5–75 employee SMBs with no dedicated finance team, specific accounting stacks, outgrowing spreadsheets) with five tightening criteria and named verticals (construction, home services, agencies). Explicitly warns against 'any small business' over-broadening. |
| `market-category` | ✅ pass | Deliberately selects 'small-business expense management' and articulates exactly why competing in 'corporate spend management' (Ramp/Brex) or 'expense reporting software' (Expensify) frames would disadvantage the product. The reasoning connects category choice to competitive positioning directly. |
| `statement` | ✅ pass | Produces a complete positioning statement in standard for/who/is/that/unlike/because structure, integrating segment, category, value, and competitive alternatives into one crisp block. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/market/positioning-statement`._
