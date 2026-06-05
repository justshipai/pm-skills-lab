# Eval results — `funnel-analysis`

- **Run:** 2026-06-05 16:07 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.7 | 1.0 | +0.3 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `priority-leak-by-opportunity` | ✅ pass | The output explicitly identifies the product page→cart drop as the largest absolute volume loss (425,000 users) and weighs it against the checkout friction leak (40K→22K), comparing both by volume and fixability rather than just worst percentage. It notes the cascade effect and downstream leverage, satisfying the weighted-by-volume-and-fixability requirement. |
| `quantified-opportunity` | ✅ pass | Both scenarios are quantified in purchases and revenue using $60 AOV: Scenario A yields +3,600 purchases/month = +$216K/month; Scenario B yields +4,000 purchases/month = +$240K/month. Combined upside is stated as $400K–$450K/month. Calculations are explicit and realistic. |
| `segment-the-drop` | ✅ pass | A dedicated 'Segment View' section recommends segmenting by device, traffic source, new vs. returning, product category, and cart value band, with specific reasoning for each cut. |
| `hypotheses-and-checks` | ✅ pass | For each priority leak, multiple hypotheses are listed with specific cheap validation methods (exit surveys, scroll/click maps, session replays, form error logs, review-count comparisons), clearly framed as hypotheses to test rather than asserted causes. |
| `recommendation` | ✅ pass | A clear where-to-focus-first recommendation is given (two parallel workstreams: checkout friction audit and product page investigation), with concrete next diagnostic steps (three specific queries to run this week before building anything). |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/data/funnel-analysis`._
