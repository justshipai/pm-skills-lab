# Eval results — `accessibility-audit`

- **Run:** 2026-06-05 15:09 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ➖ NO MEASURABLE LIFT — the with-skill output passes the rubric, but a strong no-skill baseline already does too on this scenario. This is **not** a failure: a single well-specified scenario can't show a skill's value when the base model already aces that exact prompt. The skill earns its keep through consistency across varied, messy, real-world inputs — which one-shot lift doesn't capture.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 1.0 | 1.0 | +0.0 | ❌ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `covers-key-areas` | ✅ pass | Audit explicitly covers contrast (1.4.3), keyboard operability (2.1.1), visible focus (2.4.7), names/labels (4.1.2, 3.3.2), color-alone (1.4.1), target size (2.5.8), form errors (3.3.1), and more — well beyond a single area. |
| `specific-and-criterion-based` | ✅ pass | Every finding cites specific WCAG criterion numbers (1.4.1, 4.1.2, 3.3.1, 2.4.7, 2.1.1, 1.4.3, 2.5.8, etc.) with precise technical fixes like aria-label values, aria-describedby, aria-live, and input.type toggling. |
| `catches-domain-issues` | ✅ pass | Explicitly catches all three domain-specific issues: color-only password-strength meter (finding #1), icon-only show-password button needing accessible name (finding #2), social login icon buttons needing aria-label (finding #3), and errors conveyed by red text alone (findings #4 and #5). |
| `severity-and-fixes` | ✅ pass | Each finding is rated Blocker/Major/Minor with concrete fixes including specific code examples (aria-label='Show password', aria-pressed, aria-describedby, aria-invalid, role='status', aria-live='polite', outline CSS values). |
| `verify-in-app` | ✅ pass | Dedicated 'Verify In-App' section explicitly acknowledges checks requiring the live UI or screen reader, with specific verification methods for each check and clear disclaimer that they cannot be confirmed from static description. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/design/accessibility-audit`._
