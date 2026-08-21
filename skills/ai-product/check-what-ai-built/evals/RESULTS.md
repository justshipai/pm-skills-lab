# Eval results — `check-what-ai-built`

- **Run:** 2026-08-21 11:27 UTC
- **Model under test:** Codex session default · **Judge:** Codex session default
- **Verdict:** ✅ VERIFIED — the skill passes every required criterion and beats the no-skill baseline.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---:|---:|---:|---|
| scenario-1 | 0.7647 | 1.0 | +0.2353 | ✅ |

### scenario-1 — with-skill verdicts

| Criterion | Verdict | Why |
|---|---|---|
| `decisive-verdict` | ✅ pass | Leads with Not ready and directly ties the verdict to the observed active-project failure and destructive migration risk. |
| `intent-contract` | ✅ pass | Defines observable contract items for admin success, member denial, active-project and invoice eligibility, confirmation and cancellation, data preservation, tenant boundaries, and restore compatibility. |
| `evidence-ledger` | ✅ pass | Provides a complete Pass, Fail, and Unverified ledger, cites direct preview and test evidence, and does not treat absent tests or green CI as proof. |
| `permission-uncertainty` | ✅ pass | Explicitly distinguishes hiding the member action from server-side authorisation and marks endpoint enforcement unverified. |
| `migration-blast-radius` | ✅ pass | Identifies the migration as high-blast-radius scope drift that could archive all existing projects and highlights the absence of a rollback. |
| `minimal-next-actions` | ✅ pass | Gives a short ordered action list covering eligibility enforcement, migration correction and rollback, endpoint authorisation, non-deletion, cancellation, and restore verification. |
| `pm-readable` | ✅ pass | Presents the product consequences and decision-relevant evidence clearly without narrating files or dumping a generic checklist. |

### Where the lift came from

The baseline made the correct do-not-ship decision and caught the largest risks, but scored **0.7647** and failed required criteria. It did not turn the full intent into an explicit contract, omitted non-deletion as an observable invariant and did not map every claim to Pass, Fail or Unverified.

With the skill, the response scored **1.0**. The Intent-to-Evidence ledger exposed every consequential gap, including cancellation, data preservation and tenant scoping, while keeping the decision and next actions clear for a PM.

_Method: two fresh isolated Codex agent runs received the same raw scenario. The baseline received the scenario only; the treatment was explicitly supplied `SKILL.md`. A third agent judged anonymised outputs against `criteria.json`. This uses Codex forward-testing rather than the repository's Anthropic-specific `run_evals.py` runner._
