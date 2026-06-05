# Example: agent-capability-spec

## Input

> Spec an AI "inbox agent" for our project-management tool. It reads a user's
> notifications and can triage them: snooze, assign to a teammate, comment, or
> close. Goal is to clear notification overload. Spec the agent.

## Output

# Inbox Agent — Capability Spec

## Job & autonomy level
Triage a user's PM notifications to a clean, prioritized inbox. **Autonomy: act-with-confirmation for writes; bounded-autonomous only for snoozing.** It proposes a triage plan the user approves; it never silently closes or reassigns work.

## Tool inventory
| Tool | Purpose | Inputs | Side effects | Action class |
|---|---|---|---|---|
| `list_notifications` | Read the inbox | user, filter | none | Read-only |
| `snooze(id, until)` | Defer a notification | id, time | hides until time | Reversible write |
| `comment(id, text)` | Reply on an item | id, text | posts visible comment | Irreversible (others see it) |
| `assign(id, user)` | Reassign an item | id, assignee | changes owner, notifies them | Reversible write (but notifies) |
| `close(id)` | Resolve an item | id | marks done, notifies watchers | Irreversible-ish (reopen exists, but signals "done") |

## Permissions & scope
- **Credentials (least privilege):** scoped to *this user's* notifications and the items they already have access to — no workspace-admin scope, no other users' inboxes.
- **Allowed resources:** only items already visible to the user (allow-list = the user's own access).
- **Limits:** max 50 actions per triage run; no spend (no billing tools); rate-limited to avoid notification storms.

## Autonomy & confirmation rules
- **Auto (no confirm):** `snooze` — fully reversible, low blast radius.
- **Confirm (show a diff first):** `assign`, `comment`, `close` — anything others see or that changes ownership.
- **Forbidden:** bulk-close all; assigning to users outside the item's project; editing others' comments.

## Never-do list
- Never delete anything (no delete tool exposed).
- Never reassign to someone not already on the project.
- Never act on items the user can't access.
- Out-of-scope: changing due dates, editing task content, anything billing/admin.

## Containment & recovery
- **Audit log:** every action recorded with before/after and "agent-initiated" flag.
- **Stop:** user can cancel a run mid-flight; nothing commits until confirmed (except snooze, which is reversible).
- **Rollback:** one-click "undo this triage run" reverses snoozes/assignments from the session.
- **Escalation:** if an item is ambiguous (e.g. unclear who to assign), the agent leaves it untouched and flags it for the user rather than guessing.

## Open questions
- Should `comment` be confirm-each or batch-confirm? (Lean confirm-each for v1.)
- Do we let power users opt into auto-assign within their own team after trust is established?
