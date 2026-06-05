# Eval results — `prototype-brief`

- **Run:** 2026-06-05 15:04 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.864 | 1.0 | +0.136 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `screens-and-components` | ✅ pass | Explicitly names two screens (Inbox List and Thread View) and breaks each into named components with descriptions in tables. AppShell, InboxHeader, ConversationList, ConversationRow, EmptyState, ThreadHeader, MessageThread, MessageBubble, ReplyComposer are all individually specified. |
| `all-states` | ✅ pass | Covers loading (skeletons), populated, empty, and error states for Inbox List; and loading, loaded, error, composing, sending, success, failed, and empty-thread states for Thread View. All major edge cases including reply failure with text preservation are explicitly called out. |
| `data-shape` | ✅ pass | Provides TypeScript type definitions for both Conversation and Message entities with field names and example values, plus a full JSON seed array of 6 conversations with realistic nested message arrays and all required fields populated. |
| `interactions-flow` | ✅ pass | Interaction table covers every trigger (app load, row click, back arrow, textarea input, send click, failure, mark all read, close conversation) with explicit action and result columns. Flow is unambiguous including state mutations like isUnread toggling and status updates. |
| `acceptance-criteria` | ✅ pass | 11 numbered, specific, testable acceptance criteria covering list rendering, skeletons, thread opening, unread clearing, reply disabled state, reply success flow, reply error state, back navigation, empty state, mark-all-read, and rapid-click stability. |
| `scoped-and-pasteable` | ✅ pass | Opens with an explicit scope section listing what's in and out, includes a paste instruction in the header, and the entire brief is self-contained with seed data, type definitions, style constraints, and acceptance criteria — ready to paste directly into a generative UI tool. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/design/prototype-brief`._
