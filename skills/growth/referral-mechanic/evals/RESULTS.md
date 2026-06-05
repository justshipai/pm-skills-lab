# Eval results — `referral-mechanic`

- **Run:** 2026-06-05 16:27 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.85 | 1.0 | +0.15 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `k-factor-math` | ✅ pass | Explicitly estimates invites/user (2.5) and conversion rate (12%), computes k=0.30 with clear arithmetic, runs a sensitivity check showing even optimistic scenarios stay sub-1, and derives the acquisition multiplier via geometric series convergence. Rigorous and grounded. |
| `honest-viral-verdict` | ✅ pass | Directly tells leadership this is a CAC-reducer not a viral engine, shows k≥1 is unrealistic for a paid B2C productivity tool, quantifies the blended CAC reduction ($25→$17.50), and explicitly warns against designing or framing it as a viral loop. No echo of the 'go viral' framing. |
| `incentive-vs-unit-economics` | ✅ pass | Sizes the two-sided reward ($8+$8=$16 total cost) against CAC ($25) and LTV ($90), showing referral CAC beats existing CAC by $9. Explicitly flags the CMO's signup-trigger flaw, recommends activation/first-paid-month trigger, explains why credit beats cash, and proposes a power-referrer variant. Comprehensive unit-economics reasoning. |
| `share-trigger` | ✅ pass | Identifies specific delight moments (streak milestone, task completion, weekly summary), explains why signup is wrong, specifies one-tap share with pre-filled copy, prioritizes high-converting peer channels (iMessage/WhatsApp), and describes persistent-but-non-annoying cadence. |
| `fraud-guardrails` | ✅ pass | Covers self-referral (device ID + payment method check), fake account farms (payment required before reward), public link posting (volume monitoring), reward stacking (annual cap, link expiry), chargeback fraud, and includes a clear kill criterion (90 days, 200 cycles, referral CAC vs. next-best channel). |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/growth/referral-mechanic`._
