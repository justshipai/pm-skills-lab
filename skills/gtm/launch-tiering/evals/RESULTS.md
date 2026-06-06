# Eval results — `launch-tiering`

- **Run:** 2026-06-06 11:09 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.95 | 1.0 | +0.05 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `assigns-tier` | ✅ pass | Explicitly assigns T2 with a dedicated section, justifies why not T1 (no new capability, no UI, no pricing change) and why not T3 (fixes a top complaint, warrants real announcement). |
| `tier-by-impact-not-effort-or-visibility` | ✅ pass | Directly flags the engineering-pride trap ('mismatch flag'), rejects T1 because there's no new user capability not because of effort, and rejects T3 explicitly because it fixes a top complaint at scale — impact-based reasoning throughout. |
| `right-sized-activities` | ✅ pass | Activities are proportionate to T2: in-app banner, short email, blog post, social posts, internal enablement. Explicitly lists what is NOT being done (press release, launch event, paid campaign, feature tour), avoiding both over- and under-launch. |
| `communicates-the-benefit` | ✅ pass | Consistently frames around user outcome ('data now updates in near-real time,' 'was 5 min, now instant,' 'You asked for faster sync. We listened.') and explicitly warns against leading with architecture jargon. |
| `owners-or-risk` | ✅ pass | Provides a detailed owners/timeline table with named roles and days-relative timing, plus a thorough risk overlay covering staged rollout, rollback plan, support pre-brief as blocker, copy honesty, and post-launch retention monitoring. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/gtm/launch-tiering`._
