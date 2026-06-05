# Eval results — `hallucination-risk-register`

- **Run:** 2026-06-05 10:47 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — skill beats the no-skill baseline on every scenario

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.955 | 1.0 | +0.045 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `beyond-hallucination` | ✅ pass | Identifies 12 distinct failure modes including omission, stale/outdated info, overconfidence, prompt injection, cross-patient PII/data leakage, out-of-scope diagnosis, silent degradation, bias across segments, toxic output, wrong appointment details, latency blowout, and fabrication — well beyond plain hallucination. |
| `detection-and-mitigation` | ✅ pass | Every one of the 12 failure modes has an explicit Detection column and a Mitigation column with concrete, distinct controls. Both sides are substantive (e.g., faithfulness scoring + RAG-only; classifier + hard refusal; TTL expiry + staleness alerts), not just one or the other. |
| `prioritized` | ✅ pass | Uses explicit Severity × Likelihood scoring matrix, produces ranked priority table sorted by score (16 down to 6), and includes a launch-gate recommendation ordering which risks must be resolved first. Not all modes treated as equal. |
| `domain-specific` | ✅ pass | Multiple healthcare-specific failure modes: omission of safety-critical prep instructions (colonoscopy/NPO example), crossing no-diagnosis boundary, stale clinical protocols, wrong EHR appointment details, and health-literacy/language equity concerns — not just generic LLM risks. |
| `residual-risk` | ✅ pass | Dedicated 'Residual Risk' column in the main register, a 'Cannot Currently Detect' section explicitly flagging modes where detection is weak or absent, and a formal 'Residual Risk Accepted By' table with named owners and acceptance conditions. |
| `verifiable-controls` | ✅ pass | Strongly prefers verifiable controls throughout: RAG-only with citation anchoring, structured EHR payload injection (never LLM-generated), per-request PII regex+NER scan, automated regression eval as CI gate, TTL-based KB expiry, output classifiers with measurable thresholds, input token caps, canary deployments — not 'we'll prompt it not to'. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/ai-product/hallucination-risk-register`._
