# Eval results — `ai-interface-patterns`

- **Run:** 2026-06-05 15:25 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ➖ NO MEASURABLE LIFT — the with-skill output passes the rubric, but a strong no-skill baseline already does too on this scenario. This is **not** a failure: a single well-specified scenario can't show a skill's value when the base model already aces that exact prompt. The skill earns its keep through consistency across varied, messy, real-world inputs — which one-shot lift doesn't capture.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 1.0 | 1.0 | +0.0 | ❌ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `applies-ai-patterns` | ✅ pass | Explicitly implements streaming with stop, regenerate, tone/length steering controls, edit-in-place, undo stack, thumbs feedback, and discoverability via keyboard shortcut — well beyond a button-and-spinner pattern. |
| `uncertainty-and-no-answer` | ✅ pass | Defines a distinct no-answer state with reason text and exits, uses in-draft placeholders for unanswerable specifics, adds hedged language for ambiguous threads, and lists specific triggers (unsupported language, safety filter, empty thread hidden button). |
| `control-and-editability` | ✅ pass | Draft is immediately editable plain text, AI chip fades on first keystroke, undo includes pre-suggestion state, stop mid-stream leaves partial editable draft, regenerate and discard are present, and Send is always explicitly user-owned. |
| `errors-latency-firstrun` | ✅ pass | Covers slow/timeout (4s and 12s thresholds), API error, safety block, each with human-readable messages and exits; streaming as primary latency treatment is explicitly justified; first-run coach mark sets expectations and handles empty-thread edge case. |
| `trust-and-labeling` | ✅ pass | AI chip labels draft with tooltip explaining source, fades on edit to signal ownership transfer, 'Based on' transparency affordance shows model context, first-run tooltip explicitly states user always controls Send, and uncertainty is surfaced in-draft rather than hidden. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/design/ai-interface-patterns`._
