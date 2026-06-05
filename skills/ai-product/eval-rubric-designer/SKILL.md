---
name: eval-rubric-designer
description: Use when writing the rubric an LLM-as-judge (or human) uses to score AI outputs — turning a fuzzy quality goal into discrete, observable criteria that agree with human judgment. Produces a scoring rubric with concrete pass/fail anchors and calibration examples, not a vague 1–10 scale.
---

# Eval rubric designer

A grader is only as good as its rubric. "Rate this answer 1–10" produces noise: the judge invents its own standard each time and two runs disagree. This skill writes the rubric that makes scoring reproducible — decomposed into observable criteria, each with explicit anchors for what passes and what fails, plus calibration examples so an LLM-as-judge (or a human) scores the way *you* would.

Pairs with `llm-eval-set-designer` (which builds the case set and decides where a judge is the right grader); this skill writes the judge's rubric itself.

## When to use

- You've decided an LLM-as-judge or human grader is needed for a dimension (correctness, helpfulness, tone, grounding…).
- A judge's scores feel arbitrary or disagree run-to-run.
- You need a rubric a reviewer or an automated judge can apply consistently.

## The judgment this skill encodes

- **Decompose before you score.** "Good" is several things (e.g. accurate, complete, grounded, on-tone, safe). Score each separately — one blended number hides which thing failed.
- **Anchor every level.** For each criterion, write what a pass looks like and what a fail looks like, in observable terms. "Clear and helpful" is not an anchor; "answers the exact question asked and includes the one required next step" is.
- **Prefer binary or 3-point scales.** Pass/fail (or pass/partial/fail) is far more reliable than 1–10. Reserve fine scales for dimensions that truly vary continuously, and even then anchor each point.
- **Make it pairwise-able.** For subjective quality, "is A better than B, and why" is often more reliable than absolute scoring. Offer a comparison mode where it fits.
- **Calibrate with examples.** Include 2–3 scored examples per criterion (a clear pass, a clear fail, a borderline) so the judge anchors to your standard.
- **Validate against humans.** State the agreement target (e.g. ≥90% with human labels on a calibration set) and re-check when prompts or models change. An unvalidated judge is just another model.
- **Separate severity.** Some criteria are gates (a safety or factual violation fails the whole item) — mark them, don't average them away.

## Process

1. **Restate the quality goal** and decompose it into 3–6 criteria.
2. For each criterion: **scale** (pass/fail or anchored 3-point), **anchors** (what passes / what fails), and whether it's a **gate**.
3. **Write calibration examples** (pass / fail / borderline) per criterion.
4. **Define the aggregate:** how criteria combine into an item verdict (e.g. all gates pass AND weighted score ≥ threshold).
5. **Specify judge validation:** the human-agreement target and re-check cadence.

## Output format

```
# <Task> — Scoring Rubric

## Quality goal & criteria        (the 3–6 dimensions)
## Per-criterion rubric
   For each: scale | PASS looks like | FAIL looks like | gate? | calibration examples
## Aggregate verdict              (how criteria combine; gates)
## Judge validation               (agreement target, calibration set, re-check cadence)
## (Optional) Pairwise mode        (when to compare A vs B instead of absolute scoring)
```

## Anti-patterns to refuse

- A bare 1–10 scale → Decompose and anchor.
- Criteria like "high quality" with no observable anchor → Rewrite as something a judge can check.
- One number for a multi-dimensional output → Split the dimensions.
- A judge rubric with no calibration examples or validation plan → Add both.
