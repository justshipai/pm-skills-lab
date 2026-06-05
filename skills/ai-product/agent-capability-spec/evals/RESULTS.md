# Eval results — `agent-capability-spec`

- **Run:** 2026-06-05 10:30 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ❌ not verified — see per-criterion detail below

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 1.0 | 1.0 | +0.0 | ❌ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `tool-inventory-side-effects` | ✅ pass | Section 2 provides a complete tool inventory with explicit action classes (READ, REVERSIBLE-WRITE, IRREVERSIBLE-EXTERNAL) for every tool, including blast radius reasoning and reversibility classification for all 15+ tools across 5 categories. |
| `autonomy-and-confirmation` | ✅ pass | Section 1 defines a deliberate 'Bounded-autonomous' level with a comparison table. Section 4 specifies per-action-class confirmation rules (READ=auto, REVERSIBLE-WRITE=auto within policy, IRREVERSIBLE-EXTERNAL=confirm by default), a decision tree, and a user-configurable Strict Mode. |
| `never-do-list` | ✅ pass | Section 5 contains 11 absolute prohibited actions (5.1) that cannot be unlocked by any user setting, plus a separate out-of-scope decline list (5.2) covering non-scheduling requests, with rationale for each prohibition. |
| `least-privilege-and-limits` | ✅ pass | Section 3.1 specifies minimal OAuth scopes with explicit withheld scopes per integration. Section 3.2 defines an allow-list for data access. Section 3.3 provides hard numeric limits (email caps, event caps, attendee limits, tool call limits, time limits, scheduling horizon). |
| `containment-recovery` | ✅ pass | Section 6 covers all four elements: append-only audit logging with sync requirement (6.1), multi-level kill switches including auto-halt on limit breach (6.2), rollback/snapshot mechanisms with 15-minute undo (6.3), and explicit escalation triggers with stop-acting requirements (6.4). |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/ai-product/agent-capability-spec`._
