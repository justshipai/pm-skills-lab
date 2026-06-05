# Eval results — `opportunity-solution-tree`

- **Run:** 2026-06-05 11:36 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.318 | 1.0 | +0.682 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `single-outcome-root` | ✅ pass | Tree is explicitly anchored on a single measurable outcome — free-to-paid conversion rate — stated as the root with supporting metrics defined. Not a feature or list of goals. |
| `opportunity-layer` | ✅ pass | Four distinct opportunities are inserted between the outcome and solutions, all phrased in first-person user voice ('I don't understand why paying is worth it', 'The features I'd pay for are hard to find', etc.), clearly derived from the provided quotes. |
| `solutions-attach-to-opportunities` | ✅ pass | Every solution (including team ideas like onboarding tutorial, AI background removal, referral program, cheaper tier) is nested under a specific opportunity node, not listed directly against the outcome. |
| `experiments` | ✅ pass | Every solution has an explicit, cheap experiment attached — A/B tests, fake-door tests, prototype tests, manual email cohorts — with metrics and scope specified. |
| `evidence-grounding` | ✅ pass | Each opportunity is tagged with either a direct quote or flagged as an assumption with ⚠ symbol. Opportunity 4 is explicitly called out as having no quote support, demonstrating disciplined evidence hygiene. |
| `recommended-path` | ✅ pass | Clear recommendation to start with Opportunity 1a / Solution 1a-1, with explicit rationale table covering evidence strength, impact, cost, and reversibility. Sequencing guidance for subsequent opportunities is also provided. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/discovery/opportunity-solution-tree`._
