# Example: ui-states-matrix

## Input

> Map the states for a "notifications panel" — the dropdown that shows a user's
> recent notifications when they click the bell icon.

## Output

# Notifications Panel — UI States Matrix

## Surface
The bell-icon dropdown showing recent notifications. Data: a list of notifications (read/unread). Actions: open panel, mark read, click through, mark-all-read, see all.

## States
| State | Trigger | What it shows | Actions / recovery |
|---|---|---|---|
| Empty (first use) | No notifications ever | Friendly "You're all caught up — notifications about X will show here" + illustration | — |
| Empty (all cleared) | Had some, all read/dismissed | "Nothing new" (lighter than first-use) | "See all" to history |
| Loading | Panel opened, fetching | 3–4 skeleton rows (not a spinner — avoids jank) | — |
| Partial | Scrolled, more loading | Loaded rows + skeleton at bottom | Infinite scroll / "load more" |
| Error | Fetch failed | "Couldn't load notifications" inline + Retry | Retry button |
| Success | Notifications present | Unread visually distinct (bold/dot); grouped by time | Click → go to item (marks read); mark-all-read; see all |
| No-permission | (n/a for own notifications) | — | — |

## Data edge cases
- **0 items:** empty state (above), never a blank dropdown.
- **1 item:** panel sizes to content, doesn't look broken.
- **Many (100+):** cap the panel (e.g. last 20) + "See all" to a full page; don't render 100 rows in a dropdown.
- **Long text:** notification text truncates to 2 lines with ellipsis; full text on the destination.
- **Missing fields:** notification with no avatar/icon falls back to a default, not a broken image.
- **Stale:** unread count on the bell and the panel reconcile (don't show "3 unread" with an empty panel).

## Watch out for
- **Loading and error** are the most-skipped here — a bell that does nothing for 2 seconds then pops feels broken; design the skeleton + the retry.
- The **count-vs-contents mismatch** (bell says 3, panel empty) is the classic notifications bug — call it out for the build.
