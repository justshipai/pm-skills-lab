# Eval results — `market-sizing`

- **Run:** 2026-06-05 14:12 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.9 | 1.0 | +0.1 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `tam-sam-som` | ✅ pass | Clearly distinguishes TAM (~$10B-$13B broad market), SAM (~$280M-$380M strength-training app subscribers), and SOM ($7M Yr1 / $20-30M Yr3 ARR) with separate definitions and derivations for each. |
| `two-methods` | ✅ pass | Executes a genuine top-down estimate (starting from IHRSA gym membership data × paid-app attach rate × price) and a separate bottom-up estimate (building from US adult population × exercise rate × strength-primary × gym-going × pain-point filter × price), presented as independent cross-checks with a reconciliation section. |
| `explicit-assumptions` | ✅ pass | States all key inputs with sourcing: 64M gym members (IHRSA), 45% strength-primary (CDC BRFSS), 18% paid-app attach (Sensor Tower), 60% strength-specific split, $120/yr price point rationale, 30% regular exercisers (CDC), 35% unstructured (ACE survey), 55% prefer app over PT. Each multiplier is explained. |
| `som-winnable` | ✅ pass | SOM is grounded in competitor benchmarks (Ladder ~100K users after 3 years), specific GTM spend ($3-5M), realistic subscriber ramp (60K Yr1, 200K Yr3), and framed as 2-8% of SAM rather than a generic '1% of TAM' hand-wave. |
| `reconcile-or-sensitivity` | ✅ pass | Explicitly reconciles top-down ($300M-$420M) and bottom-up ($250M-$350M), explains the ~20% gap and why bottom-up is more conservative, and provides a full sensitivity table identifying price point as the dominant swing factor with bear/base/bull scenarios. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/market/market-sizing`._
