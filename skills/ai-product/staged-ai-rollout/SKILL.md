---
name: staged-ai-rollout
description: Use when planning how to launch an AI feature safely — sequencing offline eval, shadow, dogfood, canary, and GA with quality/cost/latency gates and a kill switch. Produces a staged rollout plan where each stage has an entry gate, what you measure, and a rollback path, instead of a single flag flip.
---

# Staged AI rollout

You cannot fully predict an AI feature's behaviour from a staging environment, because its behaviour depends on real inputs you haven't seen. So you don't launch it — you *reveal* it, stage by stage, measuring at each step and keeping a way back. This skill produces that plan: the stages, the gate to enter each, what you watch, and the kill switch.

## When to use

- Planning the launch of any LLM/agent feature.
- Rolling out a model upgrade, prompt change, or new data source to an existing feature (same discipline — treat it as a change to re-prove).
- Defining the launch gates referenced by an `ai-feature-spec` / `ai-prd`.

Uses outputs of `llm-eval-set-designer` (the eval that gates each stage) and `hallucination-risk-register` (severe residual risks become gate conditions).

## The stages (skip only with a reason)

1. **Offline eval gate** — must clear the eval set's pass bars before any user sees it.
2. **Shadow** — run live, output hidden; compare to the human/baseline decision on real traffic. Catches the gap between staging and reality with zero user risk.
3. **Internal dogfood** — your team uses it on real work; qualitative failure-spotting.
4. **Canary** — small % of real users or a low-risk segment; full quality + cost + latency monitoring.
5. **Staged GA** — widen by segment/risk tier with the gates still live.

## The judgment this skill encodes

- **Every stage has an entry gate.** A measurable condition from the previous stage that must hold to proceed. No gate = no stage.
- **Gate on quality, cost, AND latency.** A feature that's accurate but too slow or too expensive should not widen. All three are launch criteria.
- **Shadow mode is the highest-leverage, most-skipped stage.** It's the only way to see real-world behaviour with no user exposure. Default to including it.
- **A kill switch is mandatory, and it has a defined fallback.** Disabling the AI must instantly revert to a known-good experience (the non-AI baseline), not an error.
- **Pre-commit the rollback triggers.** Decide *before* launch what metric breach reverts the rollout, so you're not debating during an incident.
- **Watch for the slow failure, not just the spike.** AI degrades gradually (drift); monitor trend, not only thresholds.

## Process

1. **Restate the quality/cost/latency bars** and the severe residual risks that must be guarded (from the risk register).
2. **Define each stage:** entry gate, audience/%, duration or sample size, what you measure, who reviews.
3. **Specify the kill switch and its fallback experience.**
4. **Pre-commit rollback triggers** (the metric breaches that auto-revert).
5. **Define steady-state monitoring** after GA (quality, cost, latency, drift) and the eval cadence.

## Output format

```
# <Feature> — Staged Rollout Plan

## Bars & guarded risks            (quality | cost | latency | severe risks from the register)
## Stages
   | Stage | Entry gate | Audience / % | Measure | Promote if… |
   (Offline eval → Shadow → Dogfood → Canary → Staged GA)
## Kill switch & fallback           (what users get when AI is off)
## Rollback triggers (pre-committed)
## Steady-state monitoring & eval cadence
```

## Anti-patterns to refuse

- "Put it behind a flag and ramp." → Insist on entry gates and measures per stage.
- Skipping shadow mode with no reason → Default it in; require a justification to drop it.
- A kill switch that returns an error → Require a defined fallback experience.
- Rollback "we'll know it when we see it" → Force pre-committed numeric triggers.
- Gating on quality only → Add cost and latency gates.
