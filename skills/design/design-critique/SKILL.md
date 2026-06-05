---
name: design-critique
description: Use when giving feedback on a design, mockup, or prototype — a structured design critique. Produces feedback anchored to the design's goal and user, organized across usability/states/accessibility/visual hierarchy/content, with each point rated must-fix vs. polish and made specific and actionable — not vague praise or scattered personal taste.
---

# Design critique

"What do you think of this design?" usually gets "looks great, maybe make the button bigger" — opinion dressed as feedback. A good critique is anchored to **what the design is trying to achieve for the user**, covers the dimensions that matter, separates real problems from nitpicks, and gives specific, actionable direction the designer can act on. This skill produces that — useful for reviewing a teammate's mockup or a prototype you generated.

## The judgment this skill encodes

- **Anchor to the goal and the user, first.** State (or ask for) what this design is for and who uses it. Every critique point is judged against "does this help the user achieve the goal?" — not personal taste.
- **Critique the design, not the designer.** Feedback is about the artifact and the user impact; keep it constructive and specific.
- **Cover the dimensions, don't free-associate:** does it achieve the goal/flow · usability (clarity, effort, errors) · states (empty/loading/error handled?) · visual hierarchy (does the eye go to the right thing?) · content/copy · accessibility (obvious gaps) · consistency.
- **Separate must-fix from polish.** The most useful move: rank. What blocks the user vs. what's a nice-to-have. A flat list of 15 equal comments is noise.
- **Be specific and actionable.** Not "improve the hierarchy" — "the primary action and the cancel link have equal weight; make 'Save' the only filled button and demote 'Cancel' to text." A designer should know exactly what to change.
- **Lead with what works (and why).** Name the strengths to keep — both because it's true and so good decisions survive the next iteration.
- **Ask, don't assume, when intent is unclear.** If you can't tell the goal or constraints, say what you'd need to know rather than guessing and critiquing the wrong thing.

## Process

1. **Goal & user** — what this design is for and who it serves (state it, or flag if unknown).
2. **What works** — strengths worth keeping, with the why.
3. **Critique by dimension** — goal/flow, usability, states, hierarchy, content, accessibility, consistency.
4. **Rate each** must-fix / should-fix / polish.
5. **Make each actionable** — the specific change.
6. **Summarize the top 3** the designer should tackle first.

## Output format

```
# <Design> — Critique

## Goal & user             (what it's for; who; flag if unclear)
## What works (keep)
## Findings
   | Dimension | Observation | Priority (must-fix / should / polish) | Specific change |
## Top 3 to address first
## Open questions          (what intent/constraints you'd need to finalize)
```

## Anti-patterns to refuse

- Vague praise / personal taste ("looks clean, love it") → Anchor to goal + give specific points.
- A flat, unranked list → Separate must-fix from polish.
- "Improve X" with no concrete change → Say exactly what to do.
- Critiquing without knowing the goal → State the assumed goal or ask.
- Only problems, no strengths → Name what to keep.
