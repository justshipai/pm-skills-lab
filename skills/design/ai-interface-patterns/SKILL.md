---
name: ai-interface-patterns
description: Use when designing the UX of an AI / LLM-powered feature — the interface and interaction, not the model. Produces a design that applies the established AI-UX patterns (streaming with stop, citations/sources, confidence & uncertainty, regenerate/edit, graceful "no answer", error recovery, first-run, latency feedback) so the feature feels trustworthy and controllable — not "a chat box and a spinner".
---

# AI interface patterns

AI features fail in the *interface* as often as in the model: the output streams with no way to stop it, there's no source for a claim, no signal when the model is unsure, no recovery when it's wrong, and a blank box on first run. Designing AI UX well means applying a known set of patterns that make a probabilistic system feel trustworthy and controllable. This skill designs that interaction — drawing on the AI-UX pattern literature (streaming, citations, tool transparency, etc.).

Complements `ai-feature-spec` (the spec), `human-in-the-loop-design` (oversight), and `hallucination-risk-register` (failure modes). This one is specifically the **interaction design**.

## The patterns to apply (don't stop at "chat box")

- **Streaming & stop.** Stream the response so it feels fast; always let the user *stop* generation. Show thinking/working state, not just a spinner.
- **Citations & provenance.** When the answer draws on sources/data, show them inline and clickable — lets users verify, the antidote to "is this made up?".
- **Confidence & uncertainty.** Signal when the model is unsure; degrade gracefully ("I'm not certain, but…" / ask a clarifying question) instead of confident nonsense.
- **Tool/▶action transparency.** If the AI uses tools or takes steps, show what it's doing ("searching docs…", "drafting…") so it's not a black box.
- **Regenerate, edit & steer.** Let users regenerate, edit the output, or adjust the prompt/inputs — AI output is a starting point, not a verdict.
- **Graceful "no answer".** Design the empty-result case: "I couldn't find this — here's where to look / want me to try X?" Never a fake answer or a dead end.
- **Error & fallback.** Model/timeout/safety failures get a clear message and a path forward (retry, fall back to non-AI, contact a human).
- **First-run / empty state.** Show what to type and what good input looks like; AI inputs are intimidatingly open-ended. Suggest examples/starters.
- **Feedback loop.** A lightweight way to rate/correct output (thumbs, "not helpful") that visibly does something.
- **Set expectations & trust.** Label AI output as AI; be honest about limits; make undo/cheap to recover.

## The judgment this skill encodes

- **Design for wrong, slow, and unsure — not just the happy demo.** The patterns above mostly handle the non-ideal cases that make or break trust.
- **Control beats magic.** Stop, edit, regenerate, undo — users trust AI they can steer.
- **Verifiability beats confidence.** Citations and transparency do more for trust than a slick answer.
- **Match the pattern to the risk.** A low-stakes draft needs less ceremony than an AI that takes an action; pull in `human-in-the-loop-design` for the latter.
- **Latency is a UX problem.** Streaming, skeletons, optimistic states, and "working…" messaging are design, not just engineering.

## Process

1. **Frame** the AI feature: input, what the model produces, stakes, whether it acts.
2. **Walk the patterns** above; design the ones that apply (and skip those that don't, with a reason).
3. **Design the non-ideal states**: low-confidence, no-answer, error, slow, first-run — explicitly.
4. **Specify control**: stop / regenerate / edit / undo / feedback.
5. **Trust layer**: labeling, citations/transparency, expectation-setting.

## Output format

```
# <AI feature> — Interface Design

## Feature frame            (input → output, stakes, does it act?)
## Core interaction          (happy path: input, streaming, result)
## Trust & verifiability      (citations/sources, transparency, AI labeling)
## Uncertainty & no-answer    (low-confidence + empty-result behaviour)
## Control                    (stop / regenerate / edit / undo / feedback)
## Errors & latency           (failure messages, fallback, loading/streaming UX)
## First-run / empty state    (what to type; examples/starters)
## Patterns intentionally skipped (and why)
```

## Anti-patterns to refuse

- "A chat box and a loading spinner" → Apply streaming/stop, citations, confidence, fallback.
- Confident output with no source or uncertainty signal → Add verifiability and an unsure state.
- No-answer = blank or a fabricated guess → Design the graceful no-answer.
- No way to stop/regenerate/edit → Add user control.
- Ignoring first-run (blank open-ended box) → Design starters/examples.
