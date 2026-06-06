# Eval results — `gtm-strategy`

- **Run:** 2026-06-06 11:12 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ➖ NO MEASURABLE LIFT — the with-skill output passes the rubric, but a strong no-skill baseline already does too on this scenario. This is **not** a failure: a single well-specified scenario can't show a skill's value when the base model already aces that exact prompt. The skill earns its keep through consistency across varied, messy, real-world inputs — which one-shot lift doesn't capture.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 1.0 | 1.0 | +0.0 | ❌ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `motion-fit` | ✅ pass | Explicitly flags freemium/self-serve/TikTok as a mismatch with detailed reasoning tied to $120k ACV, multi-month implementation, and multi-stakeholder buying group. Recommends enterprise/field sales with structured POC and explains why each product signal demands it. |
| `channels-fit-motion` | ✅ pass | Recommends outbound ABM-style sales, industry events (ACAMS/ABA), compliance-focused content on LinkedIn/email, partnerships with consultants/integrators/law firms, and customer referrals. Explicitly excludes TikTok and viral channels. All channels align with reaching CCOs in enterprise context. |
| `icp-and-buying-group` | ✅ pass | Defines beachhead ICP as U.S. regional banks $5B–$50B AUM with specific firmographic filters. Clearly identifies the 4-stakeholder buying group (CCO as champion, IT/CISO, Legal, Procurement) and distinguishes economic buyer from daily users. Recognizes no single self-serve user can drive a purchase. |
| `economics-check` | ✅ pass | Calculates allowable CAC ($30k–$48k) from LTV:CAC ratio, estimates blended CAC at $14k–$19k for a 2-AE team at 15–20 deals/year, confirms math works. Explicitly shows why PLG/freemium unit economics fail at this price point. |
| `message-and-metric` | ✅ pass | Provides explicit positioning statement anchored on exam readiness and regulatory change management. Defines primary GTM metric as sales-qualified pipeline per month with a milestone table (M1–M6) including first POC by month 3, CAC payback, and supporting conversion metrics. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/gtm/gtm-strategy`._
