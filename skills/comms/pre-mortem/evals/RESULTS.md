# Eval results — `pre-mortem`

- **Run:** 2026-06-05 13:56 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.864 | 1.0 | +0.136 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `imagine-failure-framing` | ✅ pass | Opens explicitly with 'It is Launch + 3 months… results are bad' prospective-hindsight scene-setting before listing any risks, fully embodying the pre-mortem framing. |
| `risk-classification` | ✅ pass | Every risk is explicitly tagged as Tiger (🐯), Elephant (🐘), or Paper Tiger (🐸) with a dedicated section explaining why Paper Tigers are dismissed — a clear three-way classification scheme. |
| `prioritized-likelihood-impact` | ✅ pass | Each risk in the table has explicit Likelihood and Impact ratings; a 'Vital Few' section further prioritizes which to act on first, rather than treating all risks equally. |
| `mitigations-and-owners` | ✅ pass | Every material risk has a concrete mitigation action and a named owner (e.g., 'PM + Exec Sponsor', 'Head of Sales + CEO', 'Eng Lead') plus an 'Action this week' directive. Paper Tigers are explicitly deprioritized with justification. |
| `category-breadth` | ✅ pass | Covers engineering/infra (#3, #12), product/onboarding (#1, #2), GTM/ICP (#4), sales alignment/comp (#7), support load (#10), lifecycle/nurture (#9), legal (#12), and competitive response (#11) — well beyond engineering alone. |
| `elephants-surfaced` | ✅ pass | Three explicit elephants are called out: the team has never built PLG and 'done' means shipping not experience (#6); sales will quietly undermine PLG due to comp threat (#7); and the privately-known truth that 8 weeks isn't enough (#8). |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/comms/pre-mortem`._
