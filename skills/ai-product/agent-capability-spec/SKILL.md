---
name: agent-capability-spec
description: Use when specifying an AI agent that takes actions — defining its tools, permissions, autonomy level, and scope boundaries. Produces a capability spec covering what the agent may do, what it may never do, what needs confirmation, and how it's contained — not just "an agent that helps with X".
---

# Agent capability spec

A chatbot answers; an agent *acts* — and actions have blast radius. The moment an AI can call tools, send messages, move data, or spend money, the spec must define not just what it can do but what it must never do, where it needs a human, and how you contain it when it goes wrong. This skill produces that contract.

Use for anything that takes actions via tools/functions. For a non-acting generative feature, use `ai-feature-spec`. Pairs with `hallucination-risk-register` (agent failure modes) and `human-in-the-loop-design` (the confirmation/escalation UX).

## The judgment this skill encodes

- **Enumerate the toolbox explicitly.** Every tool/function the agent can call, with its inputs and side effects. An undocumented tool is an undocumented risk.
- **Classify each action by reversibility and blast radius.** Read-only / reversible-write / irreversible-or-external (sends email, charges money, deletes, posts publicly). The class sets the guardrail.
- **Set the autonomy level deliberately.** Suggest-only → act-with-confirmation → act-autonomously-within-limits → fully autonomous. Default to the least autonomy that delivers the value; earn more with evidence.
- **Write the never-do list.** Explicit prohibited actions and out-of-scope requests. For agents this is as important as the capability list.
- **Define limits and a budget.** Max actions per task, spend caps, rate limits, data/scope it can touch (allow-list, not deny-list). Contain the blast radius by construction.
- **Least privilege on credentials.** The agent gets the narrowest scopes/permissions for its job — not a broad token "to be safe."
- **Decide what's logged and reversible.** Every action auditable; irreversible actions gated behind confirmation; a way to stop/rollback mid-task.
- **Specify failure & hand-off.** What the agent does when stuck, uncertain, or blocked — escalate to a human, don't improvise an irreversible action.

## Process

1. **Job & autonomy level.** What the agent accomplishes and how autonomous it is (the four-level scale).
2. **Tool inventory.** Each tool: purpose, inputs, side effects, action class (read / reversible / irreversible-external).
3. **Permissions & scope.** Credentials/scopes (least privilege), the data/resources it may touch (allow-list), and hard limits (max actions, spend cap, rate).
4. **Confirmation & autonomy rules.** Which action classes act freely, which need confirmation, which are forbidden (link `human-in-the-loop-design`).
5. **Never-do list.** Prohibited actions and out-of-scope requests.
6. **Containment & recovery.** Logging/audit, stop/kill, rollback, and the escalation/hand-off behaviour on uncertainty or failure.

## Output format

```
# <Agent> — Capability Spec

## Job & autonomy level            (suggest / confirm / bounded-autonomous / autonomous)
## Tool inventory
   | Tool | Purpose | Inputs | Side effects | Action class |
## Permissions & scope             (credentials & scopes [least privilege] | allowed data/resources | limits: max actions, spend cap, rate)
## Autonomy & confirmation rules   (per action class: auto | confirm | forbidden)
## Never-do list                    (prohibited actions; out-of-scope requests)
## Containment & recovery          (audit log | stop/kill switch | rollback | escalation on uncertainty/failure)
## Open questions
```

## Anti-patterns to refuse

- A tool list with no side-effect / reversibility classification → Add the action class column.
- "It's autonomous" with no limits → Force a spend cap, max-actions, and allow-list.
- Broad credentials "for flexibility" → Demand least-privilege scopes.
- No never-do list → Agents need explicit prohibitions; add them.
- No stop/rollback/escalation path → Require containment and hand-off.
