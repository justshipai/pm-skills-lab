# Example: staged-ai-rollout

## Input

> We're ready to launch our AI feature that auto-suggests a reply for support
> agents (drafts a response they can edit and send). Eval set is passing. Plan
> the rollout — we have ~40 agents and ~3,000 tickets/week.

## Output

# AI Reply Suggestions — Staged Rollout Plan

## Bars & guarded risks
- **Quality:** ≥ 85% of drafts rated "send as-is or minor edit"; **0 confidently-wrong factual claims** (e.g. invented policy).
- **Cost:** < $0.04 / draft.
- **Latency:** < 6s to first useful token.
- **Severe risks guarded (from register):** fabricated policy (grounding + citations), wrong-customer data (tenant isolation), out-of-scope tickets (refuse + route).

## Stages
| Stage | Entry gate | Audience / % | Measure | Promote if… |
|---|---|---|---|---|
| 1. Offline eval | — | none | Eval set pass bars | All bars green, incl. zero-tolerance |
| 2. Shadow | Eval passed | 100% of tickets, output hidden | Compare draft vs. agent's actual sent reply; grounding rate | Draft ≈ sent quality on ≥ 60% of tickets; 0 fabricated facts |
| 3. Dogfood | Shadow clean 1 wk | 3 volunteer agents | Qualitative failure log; thumbs | No new severe failure mode in 1 wk |
| 4. Canary | Dogfood positive | 5 agents (low-risk ticket tags) | Acceptance rate, edit distance, latency, $/draft, CSAT vs. control | Acceptance ≥ 50%, CSAT not down, cost/latency within bars, 0 factual incidents |
| 5. Staged GA | Canary gates held 2 wks | Widen by ticket tag, then all agents | Same dashboard, segment by tag | Each tag holds the canary gates before the next opens |

## Kill switch & fallback
A single toggle disables AI drafting for an agent / tag / globally. Fallback = the **existing macro picker** with no draft and no error noise. Drafting is additive, so kill = clean revert to today's workflow.

## Rollback triggers (pre-committed)
Auto-revert the affected scope if **any** of:
- ≥ 1 confidently-wrong factual claim reaches a customer.
- Draft acceptance rate < 35% over a rolling day.
- CSAT on AI-touched tickets drops > 3 pts vs. control.
- p95 latency > 6s or $/draft > $0.06 sustained for 1 hour.

## Steady-state monitoring & eval cadence
Live dashboard: acceptance rate, edit distance, grounding/citation rate, $/draft, p95 latency, CSAT vs. control. **Drift watch:** weekly trend on acceptance + grounding, not just thresholds. Eval set re-runs on every model/prompt change and weekly in CI; every reported bad draft becomes a new eval case.
