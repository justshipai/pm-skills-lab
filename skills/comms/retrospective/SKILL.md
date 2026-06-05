---
name: retrospective
description: Use when running or writing up a team retrospective — turning what happened in a sprint/project/incident into learning and change. Produces a structured retro that gets past symptoms to root causes and lands a few concrete, owned improvement actions — not a blame-y or feel-good list of what went well and badly.
---

# Retrospective

A retro is worthless if it produces a list of complaints and no change. The job is to turn what happened into a *small number of improvements the team will actually make*. This skill structures a retro that (a) looks honestly at what went well and badly, (b) digs to **root cause** instead of stopping at symptoms, and (c) ends with concrete, owned actions — and keeps it blameless so people tell the truth.

## The judgment this skill encodes

- **Root cause, not symptoms.** "Deploys kept breaking" is a symptom; ask why until you hit the cause (no staging parity, no pre-deploy checks). A retro that fixes symptoms repeats itself. Use 5-whys / "why did that happen?" on the few things that mattered.
- **Blameless framing.** Focus on systems and process, not people ("the review step had no owner," not "Sam dropped it"). Blame kills the honesty that makes retros useful.
- **A few actions, owned, not twenty.** Three changes the team commits to beat a wall of ideas nobody does. Each action gets an owner and is specific enough to be done.
- **Close the loop on last time.** A good retro starts by checking whether last retro's actions actually happened — otherwise it's theatre.
- **Keep and amplify what worked.** Not just problems — name what went well so the team keeps doing it deliberately.
- **Separate observations from actions.** What happened (facts), why (causes), what we'll change (actions). Don't jump from a complaint straight to a pet solution.

## Process

1. **Check prior actions** — did last retro's commitments happen? (if applicable)
2. **What went well / what didn't** — gather observations, factually.
3. **Root-cause the few that matter** — why did the worst things happen? (don't stop at the first answer).
4. **Decide improvements** — a small set of concrete changes; assign an owner to each.
5. **Frame blamelessly** — phrase causes as system/process, not individuals.

## Output format

```
# <Sprint/Project> — Retrospective (<date>)

## Last retro's actions      (done / not done — honest)
## What went well            (keep doing)
## What didn't               (observations, factual)
## Root causes               (the few that mattered — why, dug past the symptom)
## Improvements we'll make    (3-ish, each with an owner)
   | Action | Owner | So that… |
```

## Anti-patterns to refuse

- A "went well / went badly" list with no root cause → Dig to why on the items that mattered.
- Blame aimed at people → Reframe as a system/process issue.
- Twenty action items (i.e. none) → Cut to the vital few, each owned.
- Jumping from complaint to pet solution → Insert the root-cause step.
- Ignoring whether last time's actions happened → Open with that check.
