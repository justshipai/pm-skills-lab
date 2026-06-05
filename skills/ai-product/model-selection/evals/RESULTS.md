# Eval results — `model-selection`

- **Run:** 2026-06-05 10:55 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — skill beats the no-skill baseline on every scenario

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.75 | 1.0 | +0.25 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `bar-and-constraints-first` | ✅ pass | Section 1 explicitly defines hard constraints (latency, context window, privacy, availability), a quantified minimum quality bar (≥90% accuracy, ≥80% F1 on tail classes), and volume/cost framing before any model comparison begins. |
| `eval-driven-not-leaderboard` | ✅ pass | Repeatedly and explicitly states that public benchmark numbers are placeholders and that the team's own labeled eval set (500–1000 stratified tickets) is the only number that matters; action item #1 mandates building the eval harness before committing. |
| `quantified-cost-latency` | ✅ pass | Provides $/1M token pricing, per-request cost (e.g. $0.000057 for GPT-4o mini), monthly and annual cost projections at 4M and 40M tickets, and p50 latency estimates per model in the decision matrix. |
| `cheapest-that-clears` | ✅ pass | Explicitly applies the principle: recommends GPT-4o mini over GPT-4o because it clears the quality bar at 17× lower cost, and frames GPT-4o as 'last resort if cheaper models can't hit the bar.' |
| `multiple-candidates` | ✅ pass | Compares five candidates across tiers: frontier (GPT-4o), mid (GPT-4o mini, Claude 3.5 Haiku), budget (Gemini 1.5 Flash), and fine-tuned small model, with a cascade/phase approach. |
| `sensitivity` | ✅ pass | Section 7 provides a detailed sensitivity table covering accuracy thresholds, tail-class F1 floors, volume growth triggers, pricing changes, and provider reliability issues, plus Section 8 re-evaluation triggers. |
| `lock-in-portability` | ✅ pass | Decision matrix includes a lock-in risk column; notes medium lock-in for all cloud providers; recommends fine-tuning as the durable end-state partly because it reduces provider lock-in; flags fallback to Claude 3.5 Haiku if OpenAI has reliability issues. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/ai-product/model-selection`._
