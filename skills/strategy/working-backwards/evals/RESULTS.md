# Eval results — `working-backwards`

- **Run:** 2026-06-05 13:34 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ➖ NO MEASURABLE LIFT — the with-skill output passes the rubric, but a strong no-skill baseline already does too on this scenario. This is **not** a failure: a single well-specified scenario can't show a skill's value when the base model already aces that exact prompt. The skill earns its keep through consistency across varied, messy, real-world inputs — which one-shot lift doesn't capture.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 1.0 | 1.0 | +0.0 | ❌ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `press-release-customer-first` | ✅ pass | Press release leads with the customer problem (weekly status update burden), quantifies the pain (an hour or more weekly), and centers the benefit on the customer. The customer quote from Jordan M. is specific, believable, and references concrete details (dependency slipping, ticket stuck four days) rather than generic praise. |
| `plain-language` | ✅ pass | Language is direct and concrete throughout: 'one click,' 'under a minute,' 'five minutes reviewing,' 'garbage in, garbage out.' Minimal jargon; the few technical terms (LLM, API) appear only in internal sections. The press release itself reads like something a real person would find compelling. |
| `hard-faq` | ✅ pass | Internal FAQ explicitly tackles: why customers will care (with honest uncertainty about whether review saves time), why us vs. pasting into ChatGPT, biggest risks (detailed risk table with likelihood/impact/mitigation), what they're NOT doing at launch, how it makes money (retention/upsell + switching costs), and success conditions. These are genuinely hard questions answered with candor. |
| `quantified-benefit` | ✅ pass | Concrete claims: 'an hour or more' saved weekly, 'five minutes reviewing' vs. Sunday evening sessions, '5–10× faster than writing from a blank page,' beta success threshold of ≥60% users reporting time saved. These are specific rather than vague. |
| `honest-verdict` | ✅ pass | Verdict section explicitly labels the idea 'reshape and validate, not a drop,' identifies four specific weaknesses (unproven quality bar, data quality problem, time-limited moat, LLM cost math), and sets measurable go/no-go criteria for the beta (60% satisfaction, ≤30% discard rate). Not boosterish filler. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/strategy/working-backwards`._
