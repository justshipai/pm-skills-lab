---
name: ux-heuristic-audit
description: Use when reviewing a screen, flow, or prototype for usability problems — a heuristic evaluation. Produces a systematic audit against Nielsen's 10 usability heuristics, with each issue rated for severity and paired with a concrete fix — not a handful of generic, unprioritized opinions.
---

# UX heuristic audit

"What's wrong with this UX?" usually gets a few scattered opinions. A heuristic evaluation (Nielsen) makes it systematic: walk the interface against ten well-established usability principles, find the violations, rate how badly each hurts users, and say exactly how to fix it. This skill turns a vague review into a prioritized, actionable list — useful for auditing a prototype (e.g. one built in Bolt) before it goes further.

## Nielsen's 10 heuristics (check against each)

1. **Visibility of system status** — does the UI keep users informed (loading, progress, confirmation)?
2. **Match to the real world** — language/concepts users know, not system jargon.
3. **User control & freedom** — undo, back-out, exits from unwanted states.
4. **Consistency & standards** — same things look/behave the same; follows platform conventions.
5. **Error prevention** — stops mistakes before they happen (constraints, confirmation, good defaults).
6. **Recognition over recall** — options visible; users don't have to remember things across steps.
7. **Flexibility & efficiency** — shortcuts/accelerators for experts without blocking novices.
8. **Aesthetic & minimalist design** — no irrelevant clutter competing with the essentials.
9. **Help users with errors** — plain-language errors that say what happened and how to fix it.
10. **Help & documentation** — guidance available where needed.

## The judgment this skill encodes

- **Go heuristic by heuristic.** Systematic coverage is the point — don't just list whatever jumps out; check the interface against each principle so you catch the non-obvious gaps.
- **Rate severity.** For each issue: 0 (not a problem) – 4 (usability catastrophe), based on frequency × impact × persistence. Severity is what turns a list into a priority order.
- **Every issue gets a concrete fix.** Not "improve feedback" — "show a skeleton on load and a success toast on save." Actionable, or it's just complaining.
- **Tie issues to the heuristic and the user impact.** Name which principle is violated and what it costs the user, so the fix is justified.
- **Don't invent issues to fill all ten.** If a heuristic is fine, say so. Coverage means *checking* all ten, not finding ten problems.
- **Lead with the worst.** Surface the catastrophes/majors first; minors and cosmetics after.

## Process

1. **Note the context** — what the screen/flow is and the user's goal (severity depends on it).
2. **Walk all 10 heuristics** — for each, note compliance or the specific violation(s).
3. **Rate severity** of each issue (0–4).
4. **Attach a concrete fix** to each.
5. **Prioritize** — order by severity; call out the top must-fixes.

## Output format

```
# <Screen/Flow> — Heuristic Audit

## Context & user goal
## Findings (by heuristic)
   | # | Heuristic | Issue (or ✓ OK) | Severity 0–4 | Fix |
## Top must-fix (severity 3–4)
## Minor / cosmetic (severity 1–2)
```

## Anti-patterns to refuse

- A few generic opinions → Walk all 10 heuristics systematically.
- Issues with no severity → Rate each 0–4.
- Vague fixes ("make it clearer") → Give the concrete change.
- Inventing problems to hit all ten → Mark fine heuristics ✓.
- Unordered list → Prioritize by severity.
