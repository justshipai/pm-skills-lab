# Eval results — `ui-states-matrix`

- **Run:** 2026-06-05 15:06 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.95 | 1.0 | +0.05 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `covers-core-states` | ✅ pass | Explicitly covers empty, loading/uploading, error/failed, and success states both for the upload zone and per-file in the file list, with clear triggers and visual descriptions for each. |
| `domain-specific-states` | ✅ pass | Covers drag-over (Drag Active), drag-rejected for invalid type/oversized files, per-file progress bars with percentage, upload failure with retry, partial/mixed success in multi-file batch, and unsupported file type rejection — all domain-specific states addressed. |
| `actions-recovery` | ✅ pass | Every state in both tables includes an explicit Actions/Recovery column. Failed uploads get per-file Retry and global retry-all; offline state gets Resume prompt; drag-rejected returns to Idle; deletion has confirmation to prevent accidental loss; session timeout prompts re-auth. |
| `data-edge-cases` | ✅ pass | Dedicated edge cases table covers 0 files, 1 file (singular copy), 50+ files (pagination/virtualisation), very long filenames (mid-truncation with tooltip), duplicate filenames, missing metadata, near-instant uploads, and mixed success/failure batches. |
| `empty-and-error-quality` | ✅ pass | Empty state explicitly called out as 'not a blank void' with copy, context, and CTA. Error states provide plain-English messages naming the cause and always include a Retry or next-step action; 'Watch Out For' section reinforces both points explicitly. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/design/ui-states-matrix`._
