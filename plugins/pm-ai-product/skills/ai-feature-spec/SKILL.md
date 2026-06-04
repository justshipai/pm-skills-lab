---
name: ai-feature-spec
description: Use when specifying a product feature powered by an LLM or AI model — drafting a spec, PRD, or one-pager for anything that generates, classifies, summarizes, retrieves, or decides using a model. Produces a spec with an evaluation plan, failure-mode guardrails, and a graceful fallback, not just user stories.
---

# AI feature spec

Specs for AI features are not specs for normal features with "(AI)" appended. AI features are **non-deterministic**, **fail silently**, and **degrade in ways traditional QA never catches**. A spec that doesn't say how you'll measure quality, what happens when the model is wrong, and what the user sees when it fails is not a spec — it's a wish.

This skill turns a rough AI feature idea into a buildable spec that an engineer and a designer can act on, with the AI-specific risks made explicit up front.

## When to use

- Writing a spec, PRD, or one-pager for a feature that uses an LLM or ML model.
- Reviewing an existing AI feature idea before committing to build it.
- Any feature where the output is generated/predicted rather than deterministic.

Not for: deterministic features (use a normal feature spec), or pure model/infra work with no user-facing surface.

## The first question to ask

Before writing anything, pressure-test the premise: **does this actually need AI?** If a rule, a lookup, or a simpler heuristic gets you 80% of the value with 100% predictability, say so and recommend it. AI earns its place only when the input space is too large or fuzzy for rules. State the non-AI baseline you're comparing against — it's also your fallback later.

## Process

1. **Frame the job.** User, the job-to-be-done, and the non-AI baseline.
2. **Define the AI capability.** Exactly what the model does: inputs, outputs, and the boundary of what it should and shouldn't attempt.
3. **Write the eval plan _before_ the UX.** Decide what "good enough to ship" means and how you'll measure it (offline golden set + online signals). If you can't define this, you can't ship this.
4. **Enumerate failure modes and guardrails.** For each way the model fails, name detection + mitigation.
5. **Design the fallback.** What the user gets when confidence is low or the model fails. Never a dead end.
6. **Design for uncertainty and reversibility.** Confidence cues, citations/sources, edit affordances, undo, human review/escalation.
7. **Close the loop.** What you log to improve the model, plus consent/privacy.
8. **Constrain it.** Cost, latency budget, and rollout with eval gates and a kill switch.
9. **Set success + guardrail metrics.** Quality, cost, latency, adoption — and the metrics that must not regress.

## Output format

Produce a markdown spec with these sections. Keep each tight; flag unknowns as open questions rather than inventing detail.

```
# <Feature> — AI Feature Spec

## 1. Problem & job-to-be-done
## 2. Why AI (and the non-AI baseline)
## 3. The AI capability
   - Inputs / Outputs
   - Model & approach (and why)
   - In scope / explicitly out of scope
## 4. Quality bar & evaluation plan
   - Definition of "good enough to ship"
   - Offline: golden set + rubric (LLM-as-judge or human)
   - Online: live quality signals (thumbs, edits, acceptance rate)
## 5. Failure modes & guardrails   (table: failure | likelihood | detection | mitigation)
## 6. Fallback behaviour            (what the user sees on low-confidence / failure)
## 7. UX for uncertainty & reversibility
   - Confidence cues, citations, edit/undo, human-in-the-loop
## 8. Data & feedback loop           (what we log, consent, privacy)
## 9. Cost, latency & scale          (unit economics, latency budget, limits)
## 10. Rollout plan                  (shadow → canary → GA, eval gates, kill switch)
## 11. Success & guardrail metrics
## 12. Risks & open questions
```

## Rules of thumb (the judgment this skill encodes)

- **No eval plan, no spec.** Section 4 is mandatory. If quality can't be measured, the feature can't be managed.
- **Every AI feature needs a fallback.** Section 6 is mandatory. The model *will* fail; decide what the user sees now, not in incident review.
- **Specify failure before features.** A confident-but-wrong output is worse than no output. Treat hallucination/incorrectness as a first-class requirement, not an edge case.
- **Make the model's confidence legible.** Users trust AI they can verify and correct. Citations, editability, and undo beat a black box.
- **Cost and latency are product decisions.** A feature that's right but takes 30 seconds or costs more than it earns is not shippable. Put numbers in section 9.
- **Roll out behind gates.** Shadow/canary with an eval threshold and a kill switch, not a flag flip.

## Anti-patterns to refuse

- "We'll figure out quality once it's live." → Insist on section 4.
- A spec where the only failure handling is a generic error toast. → Insist on section 6.
- "Use the best model." → Force a model/cost/latency trade-off in section 3.
- Logging user content to improve the model with no mention of consent. → Flag in section 8.
