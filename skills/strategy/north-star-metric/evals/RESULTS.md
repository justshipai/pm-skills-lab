# Eval results — `north-star-metric`

- **Run:** 2026-06-05 13:32 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.95 | 1.0 | +0.05 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `value-capturing-nsm` | ✅ pass | Proposes 'Weekly Active Readers' defined as users completing ≥3 full article reads per week, with 'completed read' defined by scroll depth/time threshold. This is a value-moment rate (quality-weighted engagement), not a cumulative vanity metric. |
| `rejects-vanity-and-revenue` | ✅ pass | Explicitly explains MAU is too coarse and a user can open once in 30 days and count (vanity), and that ad revenue is a lagging output/consequence the team can't directly move — it's downstream of the NSM. The 'Screen' section also reinforces both rejections. |
| `input-metric-tree` | ✅ pass | Decomposes NSM into four named input metrics (Reach, Activation rate, Reads-per-active-user, Week-over-week retention), shows how they combine mathematically, identifies team ownership for each, and explains diagnostic use. |
| `guardrails` | ✅ pass | Provides four explicit guardrail metrics: ad experience score, source credibility flags, app store rating, and ad revenue per weekly active reader, each with clear rationale for why it must not regress. |
| `gameability-check` | ✅ pass | Directly addresses gameability: scroll+time threshold closes the app-open inflation exploit, source credibility guardrail closes the 'viral junk content' exploit, and the 'Screen' table has a dedicated 'Gameable without helping users?' row with specific analysis. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/strategy/north-star-metric`._
