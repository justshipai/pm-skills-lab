---
name: prd-generator
description: Use when writing a product requirements document or feature spec for a (non-AI) feature — turning a problem or idea into a buildable PRD. Produces a PRD that leads with the problem and evidence, defines measurable success, prioritizes requirements, and states explicit non-goals — not a feature wish-list. For AI features use ai-feature-spec instead.
---

# PRD generator

A PRD exists to align a team on **what problem we're solving, for whom, and how we'll know we won.** Most PRDs fail by leading with the solution and burying the why. This skill produces a PRD in the Marty Cagan spirit: problem and evidence first, success defined in metrics, requirements prioritized, and scope bounded by what we're explicitly *not* doing.

## When to use

- Speccing a new feature or capability for engineering and design.
- Turning a validated idea, problem, or opportunity into a buildable doc.
- Forcing clarity on scope and success before build starts.

(For features powered by an LLM/model, use `ai-feature-spec` — it adds eval plans, guardrails, and fallbacks this template doesn't.)

## The judgment this skill encodes

- **Problem before solution.** Open with the user problem and the evidence it's real (data, research, support volume). If you can't evidence the problem, that's the finding.
- **Name the user and the job.** Who specifically, and the job-to-be-done — not "users."
- **Success is measurable.** Define the metric(s) that move if this works, with a target. "Users like it" is not success.
- **Prioritize requirements.** Must / should / could (MoSCoW) or P0/P1/P2 — a flat list with no priority is a fight waiting to happen.
- **State non-goals.** What this explicitly does *not* do is as important as what it does; it's how you stop scope creep.
- **Requirements as user stories with acceptance criteria.** Each story testable; cover the unhappy paths and edge cases, not just the demo flow.
- **Surface risks, dependencies, and open questions** rather than pretending they don't exist.

## Process

1. **Problem & evidence** — the user problem and why it matters now, with proof.
2. **Target user & job-to-be-done.**
3. **Goals & success metrics** — what changes if this works; the metric + target; guardrails.
4. **Solution overview** — the approach in a few sentences (+ key flows).
5. **Requirements** — prioritized user stories, each with acceptance criteria; include edge/error cases.
6. **Scope** — in scope vs. explicit non-goals.
7. **Risks, dependencies, open questions.**
8. **Rollout & milestones.**

## Output format

```
# <Feature> — PRD

## Problem & evidence
## Target user & job-to-be-done
## Goals & success metrics        (metric + target + guardrail)
## Solution overview              (+ key user flows)
## Requirements                    (prioritized user stories with acceptance criteria; incl. edge cases)
## Scope: in / non-goals
## Risks, dependencies & open questions
## Rollout & milestones
```

## Anti-patterns to refuse

- Opening with the solution → Lead with the problem and its evidence.
- "Success = ship it / users love it" → Force a measurable metric and target.
- An unprioritized requirements list → Apply MoSCoW / P0–P2.
- No non-goals → Add them; they prevent scope creep.
- Only the happy path → Require edge and error cases in acceptance criteria.
