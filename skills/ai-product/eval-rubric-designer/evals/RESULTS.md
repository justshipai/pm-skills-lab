# Eval results — `eval-rubric-designer`

- **Run:** 2026-06-05 10:44 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — skill beats the no-skill baseline on every scenario

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.773 | 1.0 | +0.227 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `decomposed-criteria` | ✅ pass | Six distinct, observable criteria are defined: Factual Accuracy, Decision Coverage, Action Item Completeness & Ownership, Next Steps Clarity, Structure & Skimmability, and Tone & Concision — each independently assessable. |
| `anchored-levels` | ✅ pass | Every criterion has concrete observable tests for each level (e.g., PASS for C1 requires every fact traceable to transcript verbatim; FAIL triggers on any unattributed claim). No vague adjectives used as sole descriptors. |
| `discrete-scale` | ✅ pass | Gate criteria use Pass/Fail; substantive criteria use an anchored Pass/Partial/Fail 3-point scale with defined point values. No unanchored 1–10 scale is used. |
| `calibration-examples` | ✅ pass | Every criterion includes concrete calibration examples with labeled PASS, FAIL, and in several cases BORDERLINE→FAIL cases tied to specific quoted transcript excerpts. |
| `gating-and-aggregate` | ✅ pass | C1 is explicitly a gate criterion that fails the entire item. A numeric aggregation formula is provided with point values, thresholds for PASS/PARTIAL/FAIL verdicts, and a rule that any zero score triggers at least PARTIAL. |
| `judge-validation` | ✅ pass | Section 5 specifies ≥90% exact-match agreement target, Cohen's κ ≥0.75, a 30-item calibration set with defined composition, initial validation protocol with two independent raters, re-check triggers, and weekly drift monitoring. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/ai-product/eval-rubric-designer`._
