# Example: retention-lifecycle

## Input

> Our language-learning app loses most users in the first two weeks. We want a
> lifecycle email/push program to keep them. Design it.

## Output

# Language App — Retention Lifecycle Program

## Where retention breaks
Most churn is **week 1–2 before habit forms** — users who don't get a streak going leave. So the program's center of gravity is *early-habit formation*, not win-back of long-gone users. (Confirm with the curve: the cliff is days 2–10.)

## Lifecycle stages & goals
- **Onboarding (day 0–2):** reach the activation moment — complete first lesson.
- **Habit-forming (day 2–14):** build a daily streak (the retention driver).
- **At-risk (missed 2 days):** resurrect before the streak/ habit dies.
- **Dormant (14+ days inactive):** win back with a low-friction restart.
- **Power user:** ask for a review / refer a friend (hand to `referral-mechanic`).

## Triggered messages
| Stage | Behavior trigger | One job + CTA | Channel |
|---|---|---|---|
| Onboarding | Signed up, no lesson done in 24h | Do your first 2-min lesson → deep-link to it | Push + email |
| Habit | Completed a lesson; remind next day | Keep the streak — today's 2-min lesson | Push (at their usual time) |
| At-risk | Streak active, missed 2 days | "Save your N-day streak" → one quick lesson | Push |
| Dormant | 14 days inactive | "Pick up where you left off" → 1-min refresher, no guilt | Email |
| Power user | 30-day streak | Rate us / invite a friend | In-app |

## Route to value
Every message deep-links straight into a *2-minute lesson* (the value moment), not the home screen. The at-risk message reduces friction explicitly ("just 2 minutes keeps your streak") rather than nagging. We also fix the underlying friction: if users stall on lesson length, shorten the first lessons.

## Frequency guardrails
Max 1 push/day; respect quiet hours and the user's active time-of-day; suppress streak reminders for users already active that day; honor channel opt-outs; back off after repeated ignores (don't push a dormant user daily forever).

## Measurement
Hold out a randomized **10% control that receives no lifecycle messages.** Success = day-14 and day-30 retention lift vs. control (not open/click rates). Measure each message's incremental contribution; **kill any message that doesn't lift retention** vs. control — including pretty ones with high open rates.
