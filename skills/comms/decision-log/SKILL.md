---
name: decision-log
description: Use when recording a product or business decision so it sticks and can be revisited — writing a decision record or log entry. Produces a structured record capturing the decision, the context, the options considered, the rationale, who decided, and whether it's reversible (one-way vs. two-way door) — so future-you knows not just what was decided but why.
---

# Decision log

Teams re-litigate the same decisions because nobody wrote down *why*. A decision log entry captures the reasoning at the moment of choosing, so six months later you can tell whether the decision still holds or the assumptions changed. This skill writes a record that future-you (or a new teammate) can actually use — the decision, the alternatives you rejected and *why*, and how reversible it was.

## The judgment this skill encodes

- **Capture the why, not just the what.** "We chose Postgres" is a fact; "we chose Postgres over DynamoDB because relational queries dominate our access patterns and we valued familiarity over scale we don't need yet" is a *decision*. The rationale is the whole point.
- **Record the options you rejected.** The roads not taken — and why — are what stop the team re-debating, and what you re-read if circumstances change.
- **State reversibility (one-way vs. two-way door).** Bezos' framing: cheap-to-reverse (two-way) decisions should be made fast and low-ceremony; hard-to-reverse (one-way) decisions deserve more rigor. Naming it sets the right bar and tells future-you how much it'd cost to change course.
- **Name the decision-maker and the date.** Accountability and timestamp; "the team decided" with no owner ages badly.
- **Note the assumptions / what would change this.** The conditions under which you'd revisit — so a stale decision gets caught instead of silently calcifying.
- **Keep it short.** A decision record is a paragraph or a small table, not a memo. If it's long, you're writing a strategy doc, not logging a decision.

## Process

1. **State the decision** in one crisp line.
2. **Context** — the situation/forcing function that required a call.
3. **Options considered** — the realistic alternatives, with the key trade-off of each.
4. **Decision & rationale** — what was chosen and the reasoning.
5. **Reversibility** — one-way or two-way door; how costly to undo.
6. **Owner, date, and revisit trigger** — who decided, when, and what would make us reopen it.

## Output format

```
# Decision: <one-line decision>
- **Date / Decider:** <date> · <owner>
- **Reversibility:** one-way door / two-way door (<how costly to undo>)

## Context
## Options considered      (each with its key trade-off; mark the chosen one)
## Decision & rationale
## Assumptions / revisit if…   (what would make us reopen this)
```

## Anti-patterns to refuse

- Recording only the outcome with no rationale → Add the why; that's the point.
- No alternatives listed → Capture the rejected options and why.
- Missing reversibility → Add one-way/two-way door; it sets the right rigor.
- No owner or date → Add both.
- A page-long memo → Compress to a decision record.
