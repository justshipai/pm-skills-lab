# Eval results — `product-vision`

- **Run:** 2026-06-05 13:31 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.75 | 1.0 | +0.25 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `customer-world` | ✅ pass | The vision is entirely framed around the customer's lived experience — the drawer of abandoned courses, the commute becoming the session, the waiter understanding them, the in-law laughing at their joke. Company revenue or market position never appears. |
| `concrete-not-buzzwords` | ✅ pass | Specific, vivid details throughout: '28, 45, 62', 'ten minutes before sleep are the sessions', 'the in-law laughed at their joke', 'a guilt notification at 9 p.m. and a streak they broke'. No buzzwords like seamless or AI-powered. A competitor could not paste their name in without the specifics feeling wrong. |
| `aspirational-believable` | ✅ pass | The aspiration is real but grounded — not 'everyone speaks every language' but 'one person handles one real conversation.' The mechanism (micro-sessions woven into life) is plausible, not fantastical. |
| `not-feature-list` | ✅ pass | The core vision statement and customer-change sections are clearly future-state narrative, not a roadmap. The tradeoffs table names directional principles, not shipped features, and is explicitly framed as what the vision rules in/out rather than a spec. |
| `guides-tradeoffs` | ✅ pass | The tradeoffs table is explicit and sharp: streaks out, forgiveness-first UX in; structured curriculum out, real-life moment exercises in; XP out, conversational milestones in. Decisions would be easy to make against this. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/strategy/product-vision`._
