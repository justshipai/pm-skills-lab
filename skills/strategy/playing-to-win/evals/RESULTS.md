# Eval results — `playing-to-win`

- **Run:** 2026-06-05 13:37 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.7 | 1.0 | +0.3 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `five-choice-cascade` | ✅ pass | Explicitly structures all five levels of the Playing-to-Win cascade as linked choices with clear headers: winning aspiration, where to play, how to win, capabilities, management systems. Each level is framed as a choice with trade-offs, not just goals or initiatives. |
| `where-not-to-play` | ✅ pass | Makes specific where-to-play choices (independent knowledge workers, English-speaking markets, desktop-first, prosumer pricing) AND explicitly names five categories it will NOT play in: team/enterprise, project management, students/casual users, non-English markets, and API platform play. Names specific competitors ceded to each category. |
| `defensible-how-to-win` | ✅ pass | Articulates a specific position ('high retrieval intelligence, low system overhead') with named reasons it's hard to copy: behavioral data moat that grows with usage, brand positioning competitors can't credibly adopt without betraying existing user bases (Notion can't simplify, Apple can't add intelligence), and workflow coherence vs. feature count. Goes beyond 'best features' or 'better UX'. |
| `coherence` | ✅ pass | Includes an explicit coherence table showing how each choice reinforces others. Demonstrates that WTP/WNP, channel, pricing, capabilities, and metrics all point in the same direction, and explains the reinforcing loops (more usage → better intelligence → more retention → more usage). |
| `what-must-be-true` | ✅ pass | Explicitly lists five numbered assumptions that must be true for the strategy to work, each with a named test or validation method. Also identifies the central strategic bet and the biggest external risk (Notion simplifying). |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/strategy/playing-to-win`._
