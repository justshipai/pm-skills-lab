# Eval results — `prd-generator`

- **Run:** 2026-06-05 11:06 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — skill beats the no-skill baseline on every scenario

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.917 | 1.0 | +0.083 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `problem-first-with-evidence` | ✅ pass | Opens with the user problem (eye strain in low-light), immediately backed by quantified evidence: 47 App Store mentions, 23% of 1-2 star reviews, 34% of sessions in evening hours, competitive gap analysis, and platform API context. |
| `target-user-jtbd` | ✅ pass | Explicitly names primary user (evening journalers, students, professionals, on-call workers) and secondary user (aesthetic preference), with a precise JTBD statement in the standard 'when/want/so that' format. |
| `measurable-success` | ✅ pass | Five metrics with explicit numeric targets: ≥40% dark mode adoption in 30 days, +5pp retention improvement, ≥4.4 App Store rating, <2% negative dark-mode reviews, <200ms theme switch. Guardrails also specified. |
| `prioritized-requirements` | ✅ pass | Requirements are tiered P0/P1/P2, each expressed as a user story in 'As a user… I want… so that…' format with explicit, checkboxed acceptance criteria. |
| `non-goals` | ✅ pass | Dedicated Non-goals section with six explicit out-of-scope items: web/desktop clients, per-note overrides, custom theme builder, animated transitions, font/layout changes, cross-device sync. |
| `edge-cases` | ✅ pass | Multiple edge cases covered: OS switching while app is backgrounded or foregrounded, older OS versions without API support, OLED vs LCD rendering, third-party SDK surfaces, mid-session theme switch causing crash or data loss, scheduled switching interaction with manual override. |
| `risks-rollout` | ✅ pass | Risks table with likelihood/impact/mitigation for five risks; dependencies section covering design tokens, OS API gating, QA device matrix, analytics; five open questions with owners and due dates; detailed phased rollout plan with milestones and a 10%→50%→100% staged release. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/specs/prd-generator`._
