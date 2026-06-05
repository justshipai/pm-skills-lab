# Eval results — `staged-ai-rollout`

- **Run:** 2026-06-05 10:57 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ❌ not verified — see per-criterion detail below

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 1.0 | 1.0 | +0.0 | ❌ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `distinct-staged-plan` | ✅ pass | Five clearly distinct stages: Offline eval, Shadow mode, Internal dogfood, Canary (autonomous low-risk), and Staged GA with incremental percentage ramps. Each is qualitatively different, not just a percentage change. |
| `entry-gates-per-stage` | ✅ pass | Every stage has explicit, specific entry gates referencing what the prior stage measured (e.g., Shadow requires offline eval passed + PII scrubber approved; Canary requires dogfood override rate <20% + rollback triggers pre-committed; Staged GA requires Canary bars met). Gates are numeric and named. |
| `kill-switch-with-fallback` | ✅ pass | Single feature flag `refund_ai_enabled` with self-serve and automatic toggle described. Fallback is explicitly the pre-existing human-agent queue with defined customer-facing message — no error, SLA clock starts immediately. Fallback must be confirmed working before Shadow begins. |
| `precommitted-rollback-triggers` | ✅ pass | Rollback triggers table pre-commits specific numeric thresholds: $5K/$25K hourly dollar runaway, FP >5% over 200-decision window, p95 latency >45s for 15 minutes, re-escalation >2× baseline over 24h, fraud cluster ≥20 in 1 hour. Explicit automatic vs. manual actions specified. |
| `shadow-mode` | ✅ pass | Stage 1 is explicitly a shadow mode: AI runs on 100% of live traffic, no decision is actioned, no payment issued, output compared to human decisions. Described in detail including minimum sample size of 1,000 decisions for promotion. |
| `multi-dimensional-gates` | ✅ pass | Quality (accuracy, FP/FN), cost (cost/decision ≤$0.08, total weekly cost), and latency (p50/p95/p99) bars are all defined upfront and referenced as gate conditions at each stage. All three dimensions appear in the promote-if criteria. |
| `drift-monitoring` | ✅ pass | Steady-state monitoring section covers continuous automated alerts, weekly sampled accuracy audits (explicitly 'never stops, even at full GA'), weekly decision distribution drift check with >5pp shift triggering investigation, and monthly full offline eval re-run. Triggered re-evaluation list also specified. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/ai-product/staged-ai-rollout`._
