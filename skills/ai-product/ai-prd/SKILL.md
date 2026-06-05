---
name: ai-prd
description: Use when writing the full product requirements document for an AI capability, model integration, or AI-powered product (not a single feature). Produces a PRD anchored on a model card, data strategy, and evaluation strategy — the things a normal PRD template silently omits and an AI initiative dies without.
---

# AI PRD

A normal PRD assumes the system does what you tell it. An AI PRD can't — the capability is *learned*, the data is the product, and "works" is a distribution, not a state. This skill produces the document that gets an AI capability funded and built: it forces a **model card** (what the thing can and can't do), a **data strategy** (where the capability actually comes from), and an **evaluation strategy** (how you'll know it's good enough) into the centre of the doc, not the appendix.

Use `ai-feature-spec` for a single AI feature. Use **this** for an AI *initiative*: a new model integration, an AI product line, or a capability multiple features will share.

## When to use

- Standing up a net-new AI capability or integrating a model/vendor for the first time.
- Writing the doc a leadership team will fund, or that several squads will build against.
- Any time "where does the data come from?" and "what is this allowed to do?" are unanswered.

## The judgment this skill encodes

- **The model card is the spec.** If you can't state intended use, capabilities, and *explicit* limitations, you don't understand the product yet. This section is mandatory and comes early.
- **Data is a requirement, not an assumption.** Name the data you need, where it comes from, who owns the rights, and the privacy/consent position — before build, not in an incident.
- **Evaluation strategy belongs in the PRD.** Not the full eval set (that's `llm-eval-set-designer`), but the strategy: what "good enough" means and how you'll measure it offline and online.
- **Buy-vs-build is an explicit decision.** API model, fine-tune, or own model — state the choice and why, with cost/latency/control/privacy trade-offs.
- **Name what it must not do.** Out-of-scope and prohibited behaviours are first-class requirements for AI products.

## Process

1. **Problem, users, and the bet.** Why now, who it's for, and the outcome that defines success.
2. **Buy vs. build.** API / fine-tune / own model — the decision and its trade-offs.
3. **Model card.** Intended use, capabilities, explicit limitations, prohibited uses, expected inputs/outputs.
4. **Data strategy.** What data the capability needs, sourcing, rights/licensing, labeling, privacy/consent, retention, and the feedback data you'll capture to improve it.
5. **Evaluation strategy.** Definition of "good enough to ship," offline + online measurement approach, and the quality bar gating launch.
6. **UX & trust principles.** How users understand, verify, correct, and recover from model output.
7. **Risks, safety & compliance.** Failure modes, abuse/misuse, regulatory exposure (e.g. EU AI Act tier), and mitigations.
8. **Rollout & milestones.** Phased plan with gates (pairs with `staged-ai-rollout`), and a RACI.
9. **Success & guardrail metrics.** Quality, cost, latency, adoption, plus what must not regress.

## Output format

```
# <Capability> — AI PRD

## 1. Problem, users & the bet
## 2. Approach: buy vs. build       (decision + trade-offs)
## 3. Model card
   - Intended use
   - Capabilities
   - Limitations (explicit)
   - Prohibited / out-of-scope uses
   - Inputs → outputs
## 4. Data strategy
   - Data required & sourcing
   - Rights / licensing / privacy / consent
   - Labeling & quality
   - Feedback data captured
## 5. Evaluation strategy            ("good enough" + how measured, offline & online)
## 6. UX & trust principles
## 7. Risks, safety & compliance     (incl. regulatory tier)
## 8. Rollout, milestones & RACI
## 9. Success & guardrail metrics
## 10. Open questions
```

## Anti-patterns to refuse

- A PRD with no model card → you're specifying a wish. Add section 3.
- "We'll use the data we have." → Force section 4 to name it, with rights and privacy.
- "Success = users like it." → Force a measurable quality bar in section 5.
- No prohibited-use list → AI products need explicit guardrails on intent; add them to section 3.
