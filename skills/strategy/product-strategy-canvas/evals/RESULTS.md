# Eval results — `product-strategy-canvas`

- **Run:** 2026-06-05 13:38 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.818 | 1.0 | +0.182 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `diagnosis-first` | ✅ pass | Opens with a dedicated Diagnosis section that honestly names the structural challenge (cannot out-scale incumbents, burn-rate trap) before any solutions are proposed, and cites the profitable-cities lesson as the core tension. |
| `non-obvious-insight` | ✅ pass | The claim that incumbents have a *structural* blind spot — their economics require high commissions that damage indie restaurants, making the indie-loyal segment permanently unwinnable for them — is a specific, arguable belief, not a generic 'focus on customers' platitude. |
| `focus-with-non-goals` | ✅ pass | Names a precise focused bet (mid-size cities 200k–800k, operator-first, indie restaurants) and lists five explicit, concrete non-goals including no chains, no top-10 metros, no speed race, no discount subscription, and no multi-city expansion before profitability. |
| `defensibility` | ✅ pass | Provides a structured moat table with four distinct layers (operator switching costs, local network effects, brand signal, data flywheel) and explains the persistence mechanism for each, including why incumbents cannot replicate without restructuring their P&L. |
| `coherent-bets` | ✅ pass | Each of the four bets includes an explicit 'Why it follows' note tying it back to the diagnosis or insight, and the sequencing logic (operator health → city playbook → community layer → referral) is internally consistent. |
| `success-and-assumptions` | ✅ pass | Names a primary metric (contribution margin per city at month 12), four supporting KPIs with numeric targets, and a risk/assumption table with five rows each paired with a concrete test or trigger. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/strategy/product-strategy-canvas`._
