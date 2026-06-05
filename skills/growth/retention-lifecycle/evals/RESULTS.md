# Eval results — `retention-lifecycle`

- **Run:** 2026-06-05 16:29 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.8 | 1.0 | +0.2 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `targets-real-dropoff` | ✅ pass | Explicitly identifies the activation gap (bank connected, no budget created, no insight viewed) as the primary drop-off point and secondary target of early-engaged users going silent, directly rejecting the generic newsletter approach. |
| `behavior-triggered-stages` | ✅ pass | All 12 messages are mapped to named lifecycle stages (Onboarding, Activating, Engaged, At-risk, Dormant, Churned, Power User) and triggered on specific behavioral signals or absence thereof (e.g., 'bank connected; no budget created after 24h'), not fixed-time blasts. |
| `one-job-routed-to-value` | ✅ pass | Every message has a single explicit CTA that deep-links to a specific in-product value action (pre-filled budget screen, spending insight, weekly progress view, monthly summary), with a dedicated table explaining what each deep link does. No generic 'log in' or 'we miss you' CTAs. |
| `frequency-guardrails` | ✅ pass | Includes a global 2-message/7-day rolling window cap across all channels, immediate suppression on action completion, channel preference fallback, quiet hours, unsubscribe hygiene, churn suppression after 60 days, and newsletter eligibility gating. |
| `holdout-measurement` | ✅ pass | Explicitly designs an 80/20 treatment/holdout split randomized at user level, locked for 90 days, measuring incremental retention by stage (not open/click rates), with a hard kill rule: any message with <3pp incremental lift after 8 weeks or N≥500 per arm is eliminated regardless of CTR. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/growth/retention-lifecycle`._
