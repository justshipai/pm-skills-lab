---
name: hallucination-risk-register
description: Use when you need to map how an AI feature can fail and what guards each failure — building a risk register for an LLM/agent feature before launch or review. Produces a register of failure modes with trigger, severity, likelihood, detection, mitigation, and residual risk, prioritized by exposure.
---

# Hallucination & failure-mode risk register

AI features fail in ways traditional QA never sees: they're confidently wrong, they fail silently, and the same input can pass today and fail tomorrow. This skill produces the artifact that turns "what could go wrong?" into an owned, prioritized list with a guard against each mode — the AI equivalent of a threat model.

"Hallucination" is the headline, but it's one of many modes. This skill covers the full set and forces a **detection** and a **mitigation** for each, then ranks by severity × likelihood so you fix the worst first.

## When to use

- Before shipping any LLM/agent feature, as part of (or alongside) the spec.
- In an AI feature review, to pressure-test safety.
- After an incident, to add the new mode and re-prioritize.

Pairs with `ai-feature-spec` / `ai-prd` (the register populates their failure-modes section) and feeds `staged-ai-rollout` (severe residual risks become rollout gates).

## The failure-mode checklist (don't stop at hallucination)

Walk every one of these and keep the ones that apply:

- **Fabrication / hallucination** — invents facts, citations, APIs, or values.
- **Factual error on real input** — wrong but plausible answer.
- **Omission** — drops a critical item (often worse than being wrong, because it's invisible).
- **Stale / outdated** — confidently returns superseded information.
- **Overconfidence** — no signal that it's unsure when it should be.
- **Wrong tool / action** (agents) — calls the wrong function, wrong args, or unintended side effect.
- **Prompt injection / jailbreak** — user or retrieved content hijacks behaviour.
- **Data leakage** — exposes another user's data, secrets, or PII.
- **Toxic / unsafe / off-brand output.**
- **Bias / unfair performance** across user segments or languages.
- **Latency / cost blowout** — pathological inputs spike time or spend.
- **Silent degradation** — quality drifts after a model/prompt/data change.

## The judgment this skill encodes

- **Every mode needs both a detection and a mitigation.** A mitigation you can't detect firing is faith, not control. If you can't detect it, that *is* the top risk.
- **Severity × likelihood, then fix the worst.** Don't gold-plate a rare, low-harm mode while a likely, high-harm one ships unguarded.
- **Confident-but-wrong outranks no-answer.** Weight modes that mislead a trusting user above modes that visibly fail.
- **Name the residual risk.** After mitigation, state what's left and who accepts it. "Mitigated" is not "gone."
- **Prefer prevention you can verify** (grounding constraints, allow-lists, schema validation, refusal thresholds) over "we'll prompt it not to."

## Process

1. **Scope** the feature: inputs, outputs, whether it takes actions, who sees the output and how much they trust it.
2. **Walk the checklist;** keep applicable modes, add domain-specific ones.
3. For each: **trigger, severity (1–5), likelihood (1–5), detection, mitigation, residual risk, owner.**
4. **Rank by severity × likelihood;** call out anything you can't currently detect.
5. **Summarize** the top guards to build and the residual risks to accept (and by whom).

## Output format

```
# <Feature> — Failure-Mode Risk Register

## Scope                            (inputs, outputs, takes actions?, audience & trust)
## Register
   | # | Failure mode | Trigger | Sev (1-5) | Likelihood (1-5) | Detection | Mitigation | Residual risk | Owner |
## Top risks & guards to build      (ranked by sev × likelihood)
## Cannot currently detect          (the real watchlist)
## Residual risk accepted by        (name / role)
```

## Anti-patterns to refuse

- A register that only lists "hallucination" → Walk the full checklist.
- A mitigation with no detection → Flag it as an undetected risk.
- "We'll tell the model not to" as the only guard for a high-severity mode → Require a verifiable control.
- Equal treatment of all modes → Force severity × likelihood ranking.
