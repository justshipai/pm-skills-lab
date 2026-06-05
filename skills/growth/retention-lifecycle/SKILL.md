---
name: retention-lifecycle
description: Use when designing lifecycle / CRM messaging (email, push, in-app) to improve retention. Produces a behavior-triggered program mapped to lifecycle stages that targets the actual drop-off point, gives each message one job, guards against over-messaging, and measures incremental lift with a holdout — not a generic time-based drip.
---

# Retention lifecycle

A "welcome series + a few drip emails" rarely moves retention, because it's time-based blasting, not behavior-based intervention at the moment that matters. This skill designs a lifecycle program that targets *where users actually drop off*, triggers on *what they do (or don't do)*, gives each touch one clear job, and proves it works with a holdout — rather than adding to inbox noise.

## The judgment this skill encodes

- **Start from where retention breaks.** Look at the retention curve / funnel and target the specific stage that's leaking (e.g. week-1 non-activators, or active→dormant). Don't spread effort evenly across a generic lifecycle.
- **Trigger on behavior, not the clock.** "User hasn't done [core action] in 7 days" beats "send email on day 7 to everyone." Behavior triggers reach the right user at the right moment; time blasts hit everyone including the happy ones.
- **Map the lifecycle stages and the job at each:** onboarding (→ reach activation), engaged/habit (→ deepen, form habit), at-risk/dormant (→ resurrect before they're gone), churned (→ win-back), plus power-user (→ advocacy). Each stage needs a different message and goal.
- **One message, one job, one CTA.** Each touch drives a single next action that moves the user toward (or back to) value. Multi-purpose emails convert nothing.
- **Lead to the value moment, not to "log in."** Re-engagement that just says "we miss you" fails; it must route the user to the action that delivers value (and ideally remove the friction that stopped them).
- **Respect frequency / fatigue.** Cap volume, honor channel preference and quiet hours, and suppress messages that no longer apply. Over-messaging causes the churn (and unsubscribes) it's trying to prevent.
- **Prove incremental lift with a holdout.** Always keep a randomized control that gets *no* lifecycle message, and measure retention lift vs. it — open/click rates lie; incremental retention is the truth. Kill messages that don't lift.

## Process

1. **Find the drop** — which lifecycle stage leaks most (from retention/funnel data).
2. **Map stages** — onboarding / engaged / at-risk / dormant / churned (+ power user); the goal at each.
3. **Design behavior triggers** — the do/didn't-do signals that fire each message, targeting the drop.
4. **One job per message** — the single action each drives, routed to the value moment.
5. **Frequency guardrails** — caps, channel, suppression, quiet hours.
6. **Measurement** — holdout design; the retention lift to look for; kill rule for non-lifting messages.

## Output format

```
# <Product> — Retention Lifecycle Program

## Where retention breaks      (the stage we're targeting; the evidence)
## Lifecycle stages & goals      (onboarding / engaged / at-risk / dormant / churned — job at each)
## Triggered messages           | stage | behavior trigger | the one job + CTA | channel |
## Route to value               (how messages lead to the value action, not just "log in")
## Frequency guardrails         (caps, suppression, quiet hours)
## Measurement                  (holdout; incremental retention lift; kill rule)
```

## Anti-patterns to refuse

- A generic time-based drip → Trigger on behavior and target the real drop-off.
- Treating all users the same → Map lifecycle stages with stage-specific goals.
- "We miss you" with no path to value → Route to the value action + remove the friction.
- Multi-purpose messages → One job, one CTA each.
- No holdout / measuring opens → Add a control and measure incremental retention.
