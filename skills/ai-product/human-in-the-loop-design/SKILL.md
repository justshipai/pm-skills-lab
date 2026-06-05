---
name: human-in-the-loop-design
description: Use when designing the human oversight around an AI feature — when the model should ask, confirm, defer to a person, or let the user undo. Produces a design that maps each action to the right oversight level by risk and confidence, plus the review/escalation/undo UX — so AI assists without removing human control where it matters.
---

# Human-in-the-loop design

The question for any AI feature isn't "automate or not" — it's *where the human sits in the loop*. Too much oversight and the feature is useless friction; too little and a confident mistake ships straight to the customer. This skill designs the oversight: which actions are automatic, which need a glance, which need approval, and how a human reviews, overrides, and undoes.

Complements `agent-capability-spec` (which sets what an agent may do) and `ai-feature-spec` (fallbacks). This skill designs the *human's* role specifically.

## The judgment this skill encodes

- **Match oversight to risk × reversibility, not to a blanket policy.** A reversible, low-stakes action can be automatic; an irreversible or high-stakes one needs a human gate. Map each action, don't pick one global setting.
- **Use the model's confidence as a router.** High-confidence + low-risk → auto; low-confidence or high-risk → ask/confirm/defer. Design the thresholds, and what happens on each side.
- **"Human-on-the-loop" ≠ "human-in-the-loop."** *In* = approves before it happens. *On* = monitors and can intervene after. *Out* = fully automatic with audit. Choose per action class and say which.
- **Make review fast or it won't happen.** Surface what changed, why, and the source — a reviewer rubber-stamps a wall of text. Show the diff, the confidence, the evidence.
- **Always provide undo.** Even automatic actions need a clear, fast reversal. Reversibility is the cheapest safety net.
- **Escalate, don't guess.** When the model is unsure or out of scope, route to a human with context — never improvise a high-stakes action.
- **Design for oversight fatigue.** If humans must approve everything, they stop reading. Reserve approval for what matters; batch or sample the rest.
- **Plan the trust ramp.** Oversight should loosen as evidence accrues (eval + live accuracy), not on day one. State the criteria to move an action from confirm → auto.

## Process

1. **List the AI's actions/outputs** and tag each by risk and reversibility.
2. **Assign an oversight level** to each: auto (out of loop) / confirm (in loop) / review-after (on loop) / defer-to-human.
3. **Define confidence routing:** thresholds and behaviour above/below.
4. **Design the review surface:** what the human sees to decide fast (diff, confidence, evidence, one-click approve/edit/reject).
5. **Design undo & escalation:** how anything is reversed; how uncertainty/out-of-scope routes to a person with context.
6. **Define the trust ramp:** the evidence that loosens oversight over time, and the guardrail that tightens it back.

## Output format

```
# <Feature> — Human-in-the-Loop Design

## Action → oversight map
   | Action / output | Risk | Reversible? | Oversight level (auto / confirm / review-after / defer) | Why |
## Confidence routing               (thresholds; behaviour above/below)
## Review surface                    (what the human sees to decide fast; approve / edit / reject)
## Undo & escalation                 (reversal path; uncertainty/out-of-scope → human with context)
## Trust ramp                        (criteria to loosen oversight; guardrail to tighten)
```

## Anti-patterns to refuse

- One global setting ("everything needs approval" / "it's automatic") → Map per action by risk × reversibility.
- Confirmation prompts with no diff/evidence → Design a review surface a human can act on in seconds.
- Automatic actions with no undo → Add reversal.
- "It'll escalate if unsure" with no defined threshold or hand-off context → Specify both.
- Approve-everything UX → Reserve approval for high-stakes; prevent oversight fatigue.
