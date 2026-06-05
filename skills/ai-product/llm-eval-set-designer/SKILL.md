---
name: llm-eval-set-designer
description: Use when you need to measure the quality of an LLM/AI feature — designing an eval set, test cases, graders, or a "definition of good" for a model-powered capability. Produces a concrete eval set spec (cases, graders, pass bars) you can actually run, grounded in real and adversarial data, not vibes.
---

# LLM eval-set designer

You cannot manage what you cannot measure, and for AI features "it seems good" is not measurement. This skill turns a fuzzy quality goal into a runnable eval set: a curated set of cases, a grader for each, and pass bars per failure mode. It encodes the core discipline from practitioners like Hamel Husain — **look at your data first, write graders that match how you actually judge, and stratify by the ways the feature fails.**

## When to use

- Defining "good enough to ship" for an AI feature in measurable terms.
- Building the eval that gates a launch, a model swap, or a prompt change.
- After an incident, to add the failure as a permanent regression case.

Pairs with: `ai-feature-spec` / `ai-prd` (which reference an eval strategy), `model-selection` (which runs candidates against an eval set), `staged-ai-rollout` (whose gates use eval scores).

## The judgment this skill encodes

- **Start from real outputs, not imagined ones.** Look at 20–50 actual (or pilot) outputs before writing a single criterion. Your failure taxonomy comes from data, not a brainstorm.
- **Stratify by capability and failure mode.** A single aggregate score hides the failures that matter. Bucket cases: core happy path, known-hard cases, adversarial/abuse, and out-of-scope (should-refuse).
- **Match the grader to the question.** Use the cheapest grader that's trustworthy: code-based assertions for checkable facts (valid JSON, contains citation, within length), LLM-as-judge for fuzzy quality (with a written rubric), human for the highest-stakes or to calibrate the judge.
- **Validate the judge.** An LLM-as-judge you haven't checked against human labels is another unmeasured model. Spot-check agreement before you trust it.
- **Set per-bucket bars, including a zero-tolerance bucket.** Some failures (fabrications, leaking PII, harmful output) are pass/fail, not averaged away.
- **Evals are living.** Every production failure becomes a new case. The set only grows.

## Process

1. **State the capability and what "good" means** in one sentence per dimension (e.g. correct, grounded, safe, on-tone, well-formatted).
2. **Look at real data.** Review actual/pilot outputs; write down the failure modes you observe.
3. **Build the case set,** stratified: happy path, hard cases, adversarial, should-refuse. Note count and source (real / synthetic / hand-written) per bucket. Aim for coverage over volume.
4. **Choose a grader per dimension:** code assertion, LLM-as-judge (+ rubric text), or human.
5. **Set pass bars per bucket,** with explicit zero-tolerance criteria.
6. **Plan judge validation and cadence:** how you'll check the judge, and when the eval runs (per PR / pre-release / monitoring).

## Output format

```
# <Feature> — Eval Set Spec

## Capability & definition of good   (dimensions: correctness, grounding, safety, tone, format…)
## Failure modes observed            (from looking at real data)
## Case set                          (table: bucket | # cases | source | example)
   - Happy path
   - Hard / edge
   - Adversarial / abuse
   - Out-of-scope (should refuse)
## Graders                           (table: dimension | grader type | rubric/assertion)
## Pass bars                         (per bucket; mark zero-tolerance criteria)
## Judge validation & cadence
```

## Anti-patterns to refuse

- "Score it 1–10 with GPT." → Demand a written rubric and judge validation.
- One flat list of cases, one average → Force stratified buckets and per-bucket bars.
- Only happy-path cases → Insist on adversarial and should-refuse buckets.
- Writing cases before looking at real outputs → Reverse the order.
