# Example: retrospective

## Input

> Write up our sprint retro. What happened: we missed the sprint goal again. Two
> tickets were way bigger than estimated. QA found a pile of bugs at the very end
> so we crunched. The new onboarding flow we did ship got great feedback. People
> are frustrated and a bit burned out. Last sprint we said we'd add a mid-sprint
> check-in but didn't.

## Output

# Sprint 24 — Retrospective (Jun 5)

## Last retro's actions
- "Add a mid-sprint check-in" — **not done.** (We need to understand why our own actions don't stick — see root causes.)

## What went well (keep doing)
- The onboarding flow shipped and got strong user feedback — the discovery work up front paid off. Keep front-loading discovery on user-facing work.

## What didn't
- Missed the sprint goal (again).
- Two tickets blew past their estimates.
- QA surfaced a wave of bugs at the very end → end-of-sprint crunch.
- Team is frustrated and showing burnout.

## Root causes (dug past the symptom)
- **Missed goal → estimates blew up → why?** The two big tickets were under-specified going into the sprint; we estimated optimistically without breaking them down. *Cause: no "definition of ready" / breakdown step before committing.*
- **Bugs found late → crunch → why?** QA only engaged at the end. *Cause: testing is a phase at the end, not continuous; no mid-sprint integration.*
- **Our own improvement (mid-sprint check-in) didn't happen → why?** No owner was assigned and it lived only in the retro doc. *Cause: actions without an owner and a trigger don't get done.* (This is the meta-lesson.)

## Improvements we'll make
| Action | Owner | So that… |
|---|---|---|
| Add a "definition of ready": tickets >X points get broken down before they enter the sprint | [Eng lead] | estimates are realistic and goals are hittable |
| QA joins from day 1; test the first slices mid-sprint, not at the end | [QA] | bugs surface early, no end crunch |
| Every retro action gets an owner + is added to the board (not just the doc) | [PM] | our improvements actually happen |

*(Framing note: these are process fixes — the misses were systemic, not anyone's fault.)*
