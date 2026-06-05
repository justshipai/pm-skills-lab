# Eval results — `rice-scorer`

- **Run:** 2026-06-05 11:02 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.25 | 1.0 | +0.75 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `four-factors-scored` | ✅ pass | Every item has explicit Reach, Impact, Confidence, and Effort values, and a computed RICE score shown in the table. |
| `reach-as-count` | ✅ pass | Reach is expressed as actual user counts (e.g., 15,000; 20,000; 50,000) over a defined 1-quarter window, anchored to a 50,000 MAU baseline. Impact uses the standard 3/2/1/0.5/0.25 scale and Confidence uses percentage scale. |
| `effort-all-functions` | ✅ pass | Effort is measured in person-weeks explicitly covering design, eng, QA, and GTM, and is used as the denominator in the RICE formula consistently across all items. |
| `ranked-output` | ✅ pass | A clear ranked table from score 8,333 down to 375 is provided, with rank numbers and labels. |
| `sanity-check` | ✅ pass | The output flags low-confidence/high-score items (2FA's math-driven #1 vs. actual purpose, mobile app's strategic vs. score tension), notes sequencing dependencies (referral after retention fixes, Slack before mobile), and highlights items RICE under- or over-rates for strategic reasons. |
| `confidence-as-flag` | ✅ pass | Both 50%-confidence items (referral program and mobile app) are explicitly called out with recommendations to validate first — a no-code referral test and a PWA spike — before committing full build effort. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/prioritization/rice-scorer`._
