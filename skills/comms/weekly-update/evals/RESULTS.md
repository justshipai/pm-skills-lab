# Eval results — `weekly-update`

- **Run:** 2026-06-05 13:54 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.9 | 1.0 | +0.1 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `outcomes-not-tasks` | ✅ pass | Leads with a clear status line stating what's at stake (2-week slip), shipped section frames results and impact (activation lift, signal to move to build), not just activities. |
| `blocker-and-ask` | ✅ pass | Dedicated '⚠ Blockers / Decisions Needed' section is prominent, delay-vs-cut-scope options are explicitly named, and a concrete ask (30-min call by a specific day, with default consequence stated) is clear and unburied. |
| `honest-status` | ✅ pass | Status line is 🟡 at-risk with explicit 'Search launch will slip 2 weeks' — not softened or buried. |
| `scannable` | ✅ pass | Clear section headers, bold lead sentences, blockquote for the ask, and concise bullets make it easy to skim for an exec audience. |
| `forward-look` | ✅ pass | 'Next' section lists concrete upcoming actions tied to both paths, including what to expect on activation metrics and a flag commitment if pipeline slips further. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/comms/weekly-update`._
