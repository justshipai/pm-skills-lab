# Example: cohort-analysis

## Input

> Read our weekly retention by signup cohort (% still active):
> Week 0: 100%. By cohort, week-4 / week-8 / week-12 retention:
> Jan cohort: 28% / 22% / 21%. Feb: 30% / 24% / 23%. Mar: 33% / 28% / 27%.
> Signups are growing fast. Active-user total is flat, though. What's going on?

## Output

# Retention — Cohort Analysis

## Curve shape & what it means
Within each cohort, retention drops fast then **flattens** (Mar: 33%→28%→27%, basically stable from week 8). That flattening at ~25–27% is a **product-market-fit signal**: roughly a quarter of each cohort finds durable value and sticks. That's a real, retained core — not a decay-to-zero product. (The ~70% who churn in the first month are mostly the normal early drop-off.)

## Cohort-over-cohort trend
Newer cohorts retain **better**: week-12 floor rose 21% (Jan) → 23% (Feb) → 27% (Mar). Whatever you've changed since January is working — the retention floor is climbing cohort-over-cohort. Keep doing it and find out what it was.

## Acquisition vs. retention
Here's the puzzle: signups are growing but **total active users is flat**. With a ~25% retention floor, you're acquiring users about as fast as the ~75% churn drains them — a **leaky bucket**. The binding constraint is **retention, not acquisition**: pouring more signups into a 25%-floor bucket won't grow the active base much; raising the floor will. (You're already raising it — accelerate that.)

## Segment view
Find the segment behind that 25–27% floor — split retention by acquisition channel, plan, and first-week behavior. Hypothesis: users who do [core action] in week 1 retain far above 27%. Identify them; that's the activation target.

## Recommendation
**Prioritize retention/activation over acquisition spend.** (1) Double down on whatever lifted Feb→Mar cohorts. (2) Find the high-retention segment and what they do differently in week 1, then drive more new users to that behavior. (3) Re-evaluate paid acquisition until the floor is higher — you're currently filling a leaky bucket.

## Definition note
"Active" needs a definition — opened-the-app vs. did-the-core-action retain very differently. Confirm which this is; if it's just "opened," the real value-retention floor may be lower.
