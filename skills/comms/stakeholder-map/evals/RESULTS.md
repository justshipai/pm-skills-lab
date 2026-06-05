# Eval results — `stakeholder-map`

- **Run:** 2026-06-05 10:59 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.9 | 1.0 | +0.1 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `power-interest-grid` | ✅ pass | Explicitly uses a Power × Interest grid with all four named quadrants (Manage Closely, Keep Satisfied, Keep Informed, Monitor) and places named stakeholders in each. |
| `tailored-engagement` | ✅ pass | Detailed table covers every stakeholder with what they care about, what they need, specific cadence, and channel. Clearly differentiated per stakeholder, not a uniform approach. |
| `champions-blockers` | ✅ pass | Dedicated champions and blockers sections with named individuals, specific reasons for each role, and concrete activation/mitigation plans. Even notes the same person (Head of Customer Success) can be both. |
| `distinct-axes` | ✅ pass | Explicitly differentiates high-power/low-interest (CEO, CFO, VP Engineering) from low-power/high-interest (Support Team, Power Users, Analytics), demonstrating clear conceptual separation of the two axes. |
| `revisit` | ✅ pass | A dedicated 'Revisit' section lists specific stakeholders with named triggers that would cause their position to shift, e.g. CEO moving to Manage Closely if a major customer complains. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/comms/stakeholder-map`._
