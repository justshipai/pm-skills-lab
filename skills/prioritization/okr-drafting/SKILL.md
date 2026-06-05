---
name: okr-drafting
description: Use when writing or reviewing OKRs (Objectives and Key Results) for a team, product, or quarter. Produces an inspirational objective with measurable, outcome-based key results tied to a baseline and target — and catches the most common failure, key results that are really a task list.
---

# OKR drafting

OKRs exist to align a team on an ambitious goal and a measurable definition of progress. They fail in one predictable way: the "key results" turn into a list of features to ship. This skill writes OKRs where the **Objective** is a qualitative, motivating destination and the **Key Results** are *outcomes* — metrics that move because users behaved differently — each with a baseline and a target.

## The framework

- **Objective:** qualitative, ambitious, time-bound. Where are we trying to get to, and why does it matter? No metrics here.
- **Key Results (3–5):** measurable outcomes that prove the objective is being met. Each = a metric + baseline → target. If you can complete it by shipping a thing regardless of whether anything improved, it's a task, not a KR.

## The judgment this skill encodes

- **Outcomes, not output.** "Ship feature X" is not a KR. "Increase activation from 40% → 55%" is. The test: could you "do" the KR and have nothing actually improve? If yes, rewrite it.
- **Baseline before target.** A target with no baseline is unanchored. State where you are, then where you're going.
- **Ambitious but not fantasy.** OKRs should stretch (~70% is a good result), but a target no one believes demotivates. Calibrate against the baseline and trend.
- **Few and focused.** One to three objectives; 3–5 KRs each. A dozen OKRs means none.
- **Align up.** Each objective should ladder to a company goal; name the link.
- **Avoid vanity and sandbagging.** Reject metrics that go up regardless of value (e.g. total pageviews) and targets set low to guarantee a win.
- **Pair with a guardrail / health metric.** Make sure hitting a KR can't quietly break something else (quality, churn, cost).

## Process

1. **Anchor to the company goal** this set ladders to.
2. **Draft the objective(s)** — qualitative, ambitious, time-bound.
3. **Draft 3–5 key results** per objective as metric + baseline → target.
4. **Stress-test each KR:** is it an outcome or a disguised task? Is the metric vanity? Is the target stretch-but-believable?
5. **Add guardrail metric(s)** that must hold.
6. **Note the big initiatives** likely to drive each KR (as context, not as the KR itself).

## Output format

```
# <Team/Product> — OKRs (<period>)

## Ladders up to                 (the company goal)

## Objective 1: <qualitative, ambitious statement>
   - KR1: <metric> from <baseline> to <target>
   - KR2: …
   - KR3: …
   - Guardrail: <metric that must not regress>
   - Likely initiatives: <context>

## Objective 2: …
```

## Anti-patterns to refuse

- KRs that are a feature/ship list → Rewrite as outcome metrics.
- A target with no baseline → Add the baseline.
- Vanity metrics (totals that only go up) → Swap for a rate/outcome.
- 6+ objectives → Cut to the vital few.
- Sandbagged targets → Push for stretch calibrated to the trend.
- No guardrail → Add one so a KR can't be won by breaking something else.
