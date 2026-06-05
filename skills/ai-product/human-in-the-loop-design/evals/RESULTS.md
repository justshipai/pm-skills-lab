# Eval results — `human-in-the-loop-design`

- **Run:** 2026-06-05 10:49 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ❌ not verified — see per-criterion detail below

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 1.0 | 1.0 | +0.0 | ❌ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `action-to-oversight-map` | ✅ pass | Detailed table maps every distinct action (auto-approve, auto-reject, flag, priority-flag, bulk re-evaluation, account suspension, appeal resolution) to a specific oversight level (auto/on-loop, review-after, defer, confirm/in-loop) with explicit risk and reversibility reasoning for each. |
| `confidence-routing` | ✅ pass | Explicit confidence band table with numeric thresholds routing to auto-action, human-review, or confirm queue; severity override that bypasses confidence entirely; fail-closed on timeout/error — all three routing modes clearly specified. |
| `review-surface` | ✅ pass | Provides wireframe-level card designs for standard flag, priority-flag, and auto-reject queues; specifies what evidence is shown (confidence score, matched signals, seller history, listing content); defines specific action buttons (Approve, Reject+reason, Escalate, Overturn); sets a 30-second decision-time target. |
| `undo-and-escalation` | ✅ pass | Undo table covers every action type with mechanism, time window, and who can act; escalation section defines trigger conditions, full hand-off context checklist, SLAs with breach behavior (stays held, manager paged), and named-moderator assignment. |
| `asymmetric-error-handling` | ✅ pass | Explicitly sets stricter auto-reject threshold (0.92) vs auto-approve (0.95); false-approval rate limit (0.5%) is tighter than false-rejection (1.0%); severe-signal listings bypass confidence entirely; 'What this design does not do' section explicitly notes severity always overrides score. |
| `trust-ramp-or-fatigue` | ✅ pass | Detailed trust ramp with four quantitative criteria, two-period confirmation requirement, explicit sign-off process, and automatic tightening triggers; ongoing mandatory sampling (5%/10%) explicitly decoupled from volume to prevent fatigue-driven skip; addresses both loosening over time and preventing rubber-stamping. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/ai-product/human-in-the-loop-design`._
