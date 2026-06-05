# Eval results — `interview-synthesizer`

- **Run:** 2026-06-05 11:34 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.727 | 1.0 | +0.273 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `evidenced-themes` | ✅ pass | Each theme is anchored to specific verbatim quotes with source identifiers (O1-O6) and the behavioral observation is noted inline. Themes are organized by pattern, not generic narrative. |
| `evidence-strength` | ✅ pass | Every theme explicitly states source count (e.g., '3 of 5', '1 of 5') and a rated strength (Strong/Moderate/Weak) with reasoning. Weak themes are flagged as hypotheses. |
| `behavior-vs-opinion` | ✅ pass | Consistently distinguishes behaviors (batching, abandonment, outsourcing, fine incurred, photo-taking) from stated opinions ('I'd use anything...'), explicitly labeling the latter as weaker and calling out the hypothetical nature of O3's statement. |
| `job-not-feature` | ✅ pass | Jobs table frames underlying needs ('Stay compliant without thinking about it', 'Close out the week without it ruining it') rather than feature requests. Explicitly notes owners want the input problem solved, not dashboards. |
| `limits-and-bias` | ✅ pass | Dedicated sections on caveats and unknowns address N=5 limitations, unknown recruiting source, possible leading questions, missing demographic context, and unresolved follow-up stories. |
| `next-steps` | ✅ pass | Five specific next steps recommended—shadowing, behavioral validation over intent surveys, follow-up interviews on specific stories—none of which are build plans. Each is a research action or cheap experiment. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/discovery/interview-synthesizer`._
