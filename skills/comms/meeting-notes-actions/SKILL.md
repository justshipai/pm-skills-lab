---
name: meeting-notes-actions
description: Use when turning a meeting transcript or raw notes into something useful afterward — extracting decisions and action items. Produces a structured output of decisions made, action items (each with an owner and due date), and open questions — separating what was decided and who-does-what from the discussion, rather than a prose recap nobody re-reads.
---

# Meeting notes → actions

A prose summary of a meeting is where accountability goes to die. What people actually need afterward is: **what did we decide, who's doing what by when, and what's still open.** This skill extracts exactly that from a messy transcript or notes — the decisions, the owned-and-dated actions, and the unresolved questions — so the meeting turns into follow-through instead of a document.

## The judgment this skill encodes

- **Decisions ≠ discussion.** Pull out the points where the group actually decided something, stated as the decision (not "we talked about pricing" but "decided: launch at $29/mo"). If it was discussed but not decided, it's an open question, not a decision.
- **Every action has an owner and a due date.** "Someone should follow up" is not an action item. If the owner or date is genuinely unknown, flag it as needing assignment rather than leaving it blank.
- **Separate the three buckets.** Decisions / Action items / Open questions. Mixing them back into prose is the failure mode.
- **Attribute carefully; don't invent.** Assign owners only where the notes support it. Where it's ambiguous, mark "owner TBD" rather than guessing — a wrong owner is worse than a flagged gap.
- **Capture what's unresolved.** Open questions and parked items are as important as decisions; they're what the next meeting starts from.
- **Be faithful, not creative.** This is extraction, not authorship — don't add decisions or actions that weren't there. A short context line is fine; inventing content is not.

## Process

1. **Read for decisions** — moments where a choice was actually made; phrase each as the decision.
2. **Extract action items** — concrete next steps; attach owner + due date (flag TBD where unknown).
3. **Collect open questions / parked items** — things raised but unresolved.
4. **(Optional) one-line context** — what the meeting was, attendees, date.
5. **Check faithfulness** — nothing invented; ambiguous owners marked TBD.

## Output format

```
# <Meeting> — Notes & Actions (<date>)
*Attendees: … (if known)*

## Decisions
- <Decision stated as the outcome>

## Action items
| Action | Owner | Due |
|---|---|---|
| <concrete next step> | <name / TBD> | <date / TBD> |

## Open questions / parked
- <unresolved item>
```

## Anti-patterns to refuse

- A prose recap of the discussion → Restructure into decisions / actions / open questions.
- Action items with no owner or date → Add them, or mark TBD and flag for assignment.
- Listing discussion as if it were decisions → Move undecided items to open questions.
- Inventing owners/decisions not in the notes → Mark ambiguous ones TBD instead.
