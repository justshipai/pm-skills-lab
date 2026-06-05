# Eval results — `data-viz-design`

- **Run:** 2026-06-05 15:26 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.722 | 1.0 | +0.278 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `question-first` | ✅ pass | The output explicitly opens with the question and decision it supports, then identifies the data relationship (multi-series trend + cross-cohort comparison) before recommending a chart type. |
| `encoding-fits-data` | ✅ pass | Recommends a multi-line chart with weeks on X and retention % on Y, one line per cohort. Provides a comparison table rejecting grouped bar, heatmap, stacked area, pie, and small multiples with specific justifications for each rejection. |
| `strip-junk-and-label` | ✅ pass | Explicitly removes background fill, heavy gridlines, chart border, and legend box. Replaces legend with direct end-labels on each line. Addresses the 6-line legibility problem with line weight differentiation and direct labeling, so grayscale printouts remain readable. |
| `integrity-accessibility` | ✅ pass | Addresses 0–100% Y-axis with explicit reasoning against truncation, notes unequal X-axis intervals, recommends sequential single-hue palette safe for color-blind readers, references WCAG AA contrast ratio, and notes direct labels as a non-color fallback. |
| `insight-led-takeaway` | ✅ pass | Provides a concrete insight-led title example ('Retention is improving at Week 1–2, but long-term drop-off remains flat'), explicitly contrasts it with a rejected variable-name title, and specifies what to highlight (most recent cohort, divergence points, critical drop-off week). |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/design/data-viz-design`._
