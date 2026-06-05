# Eval results — `ai-prd`

- **Run:** 2026-06-05 10:39 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — skill beats the no-skill baseline on every scenario

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.731 | 1.0 | +0.269 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `model-card` | ✅ pass | Section 3 explicitly names intended use (SMB email drafting, starting point for human review), capabilities (7 bullet points), and 7 explicit numbered limitations including real-time facts, factual accuracy, language coverage, regulated content, and scope boundaries. |
| `prohibited-uses` | ✅ pass | Section 3 lists 6 prohibited uses with enforcement mechanisms: deceptive/phishing content, spam, harassment, regulated product promotion without disclosure, manipulation of vulnerable populations, and prompt injection attempts. |
| `data-strategy` | ✅ pass | Section 4 specifies all data types, sources, and status; addresses ToS/DPA for user-generated content with explicit launch-blocker requirement; covers rights for industry corpus with consent requirements; details retention, deletion, residency, and full feedback telemetry captured per generation. |
| `evaluation-strategy` | ✅ pass | Section 5 defines 'good enough to ship' with explicit dual bars (70% send-worthy offline, 60% sent online), an 8-dimension offline eval with numeric thresholds, a 500-brief eval set methodology with inter-rater agreement requirement, regression set, and online monitoring with specific alert thresholds and cadence. |
| `buy-vs-build` | ✅ pass | Section 2 provides an explicit decision table comparing API+RAG vs. fine-tune vs. own model vs. third-party, with clear rationale choosing API-first, named primary/fallback models, and a timeline for revisiting fine-tuning at 12 months. |
| `trust-ux` | ✅ pass | Section 6 details 8 trust principles including persistent AI Draft badge until user edits, no auto-insert, editable rich-text editor, section-level regeneration, brief quality enforcement, collapsible limitations disclosure, lightweight feedback, and graceful failure fallback to manual compose. |
| `risk-compliance` | ✅ pass | Section 7 includes EU AI Act tier assessment, a 9-item risk register with likelihood/impact/mitigation, explicit compliance checklist with launch blockers (DPAs, ToS updates), coverage of prompt injection, cross-account data leakage, regulatory non-compliance, abuse, and copyright. |
| `guardrail-metrics` | ✅ pass | Section 9 includes quality guardrails with explicit thresholds: prohibited content escape rate (0/month), error rate (<1%), latency p95 (≤10s), cost per generation (≤$0.08), and offline eval regression cap (5pp), covering both quality and cost/latency dimensions. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/ai-product/ai-prd`._
