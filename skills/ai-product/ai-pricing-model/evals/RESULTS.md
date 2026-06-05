# Eval results — `ai-pricing-model`

- **Run:** 2026-06-05 10:42 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — skill beats the no-skill baseline on every scenario

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.955 | 1.0 | +0.045 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `unit-economics` | ✅ pass | Explicitly computes cost per draft for both typical ($0.0057) and heavy ($0.0142) jobs with stated token assumptions, model pricing, retry overhead, retrieval, and infra costs. Usage distribution by segment is also computed with clear assumptions about tickets/day and adoption rate. |
| `structure-choice` | ✅ pass | Chooses tiered seat add-on with included allowance + overage and explicitly justifies it. Rejects flat unlimited, pure usage, outcome-based, and baked-in pricing with specific reasons for each rejection. |
| `margin-distribution` | ✅ pass | Full margin stress test across light, typical, heavy p90, whale, and capped-whale segments for both Starter and Pro tiers. Confirms no segment is underwater; whale is explicitly identified as the risk case and shown to be margin-positive with overage. |
| `cost-guardrails` | ✅ pass | Multiple guardrails specified: included allowance, overage billing, fair-use hard cap with soft-pause at 100%, rate limit (60 drafts/hr), admin kill-switch, and anomaly alert at $15 cost threshold. |
| `value-wtp-crosscheck` | ✅ pass | Quantifies value delivered (25 hours/month saved at $625/agent/month labor value), showing $15–25 is only 2–4% of value. Also benchmarks against Salesforce/Zendesk ($50 add-ons) and DIY API cost ($2–5/agent/month). |
| `cost-trend-sensitivity` | ✅ pass | Sensitivity table explicitly models model cost halving (within 12–18 months), LLM cost spike, and competitor price pressure, with recommended responses for each scenario including how overage/caps act as buffers and when to raise overage rates. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/ai-product/ai-pricing-model`._
