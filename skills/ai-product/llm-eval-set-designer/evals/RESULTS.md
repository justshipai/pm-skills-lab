# Eval results — `llm-eval-set-designer`

- **Run:** 2026-06-05 10:53 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.885 | 1.0 | +0.115 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `stratified-cases` | ✅ pass | Cases are explicitly divided into four named buckets (Happy Path, Hard/Edge, Adversarial/Abuse, Should Refuse) with distinct rationale, case counts, and failure modes per bucket. |
| `grader-per-dimension` | ✅ pass | Each quality dimension is assigned a specific grader type: code assertions for SQL execution, schema fidelity, safety, and dialect; LLM-as-judge for semantic accuracy, refusal correctness, explanation accuracy, and time-window; hybrid for PII and SQL correctness. |
| `rubric-for-judge` | ✅ pass | Every LLM-as-judge usage includes an explicit prompt template with specific scoring categories (e.g. CORRECT/PARTIALLY CORRECT/INCORRECT, CORRECT_REFUSE/WRONG_REFUSE/etc.) and one-sentence explanation requirements — not generic 1-10 scales. |
| `pass-bars` | ✅ pass | Explicit per-bucket pass bars are defined (e.g. ≥95% happy path execution, ≥70% hard edge semantic accuracy) plus four clearly stated zero-tolerance hard-fail criteria and an aggregate 82% ship threshold. |
| `grounded-in-real-data` | ✅ pass | Explicitly recommends pulling 30–50 real or pilot outputs before finalizing cases; case table shows real vs. synthetic split per bucket; growth policy caps synthetic ratio at 50% and requires real failures to become regression cases. |
| `judge-validation` | ✅ pass | Section 6 specifies building a 30-case human-labelled calibration set, computing Cohen's kappa with target ≥0.7, pinning judge model version, and ongoing 10% spot-checks with a 15% disagreement threshold triggering re-validation. |
| `living-eval` | ✅ pass | Explicit growth policy: every production failure becomes a regression case within 48 hours; run cadence defined per trigger (PR, pre-release, weekly, post-incident, model swap); quarterly schema-driven review of should-refuse bucket. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/ai-product/llm-eval-set-designer`._
