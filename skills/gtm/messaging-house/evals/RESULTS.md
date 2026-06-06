# Eval results — `messaging-house`

- **Run:** 2026-06-06 11:14 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.75 | 1.0 | +0.25 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `single-core-message` | ✅ pass | One clearly articulated core message stated in customer-benefit terms (on time, on budget, single source of truth/shared visibility). Explicitly distinguishes it from a tagline and explains why. No competing 'main' messages. |
| `benefit-pillars-not-features` | ✅ pass | Four pillars are each framed as customer benefits: schedule slippage caught early, field issues resolved not buried, budget surprises stopped, day-one productivity. Features are explicitly placed below the line as proof, not as pillar names. |
| `proof-per-pillar` | ✅ pass | Each pillar has a dedicated proof section listing specific features (Gantt, RFIs, daily logs, change orders, pull-planning, etc.) plus placeholders for customer metrics. The document explicitly labels these as proof and explains the structure. |
| `per-audience` | ✅ pass | Four distinct audience translations provided (Executive/Owner, PM/Superintendent, Field/Foreman/Sub, IT/Procurement) with tailored language, emphasis order, and specific messaging angle for each. |
| `usable-architecture` | ✅ pass | Includes a 'How to Use This Document' section mapping the architecture to website, sales deck, product releases, onboarding/CS, and PR. Pillars are designed as reusable slots; features slot into proof layer. Gaps table adds operational guidance for maintaining the system. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/gtm/messaging-house`._
