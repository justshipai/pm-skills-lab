# Eval results — `competitor-teardown`

- **Run:** 2026-06-05 14:16 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.95 | 1.0 | +0.05 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `strategy-not-inventory` | ✅ pass | Clearly explains who Intuit targets (passive consumers), how they position (free utility via distribution moat), and exactly how they make money (referral marketplace, not budgeting subscriptions). The business model section is the analytical core, not a feature list. |
| `honest-strengths-and-structural-weaknesses` | ✅ pass | Strengths are real and specific (tax data coverage, annual re-engagement forcing function, training data scale). Weaknesses are structural, not cosmetic — the referral revenue model being adversarially misaligned with user health, enterprise inertia deprioritizing consumer roadmap, and passive architecture not building habits. Explicitly labels these as unfixable without destroying the business model. |
| `where-win-lose` | ✅ pass | Provides clear segmented win/lose conditions with specificity — wins on passive intent, price sensitivity, tax integration; loses on active behavior-change intent, irregular income, post-Mint trust, and household collaboration needs. Conditions are stated, not just asserted. |
| `implications-for-us` | ✅ pass | Uses explicit Avoid/Attack/Copy/Ignore framework with concrete moves: ex-Mint user acquisition campaign, behavior-change category framing, irregular-income segment targeting, subscription model as proof-of-alignment. Ends with a stated strategic bet and pricing rationale. Actionable throughout. |
| `evidence-and-gaps` | ✅ pass | Confidence table explicitly rates each claim with basis and flags inferences. Specific follow-up actions are prescribed (App Store review mining, LinkedIn hiring signals, win/loss analysis, pricing survey). Distinguishes between public-filing-backed claims and inferred ones. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/market/competitor-teardown`._
