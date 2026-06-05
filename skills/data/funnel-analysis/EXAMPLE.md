# Example: funnel-analysis

## Input

> Analyze our signup→paid funnel (per month):
> Visited pricing 100,000 → Started signup 20,000 → Completed signup 14,000 →
> Activated (used core feature) 7,000 → Started trial-to-paid 3,000 → Paid 1,200.
> ARPU is $30/mo. Where should we focus?

## Output

# Signup→Paid Funnel — Analysis

## The funnel
| Step | Count | Step conv | Cumulative |
|---|---|---|---|
| Visited pricing | 100,000 | — | 100% |
| Started signup | 20,000 | 20% | 20% |
| Completed signup | 14,000 | 70% | 14% |
| Activated | 7,000 | 50% | 7% |
| Started trial→paid | 3,000 | 43% | 3% |
| Paid | 1,200 | 40% | 1.2% |

## Priority leak
Two candidates: **pricing→started signup (20%)** is the worst single drop *and* has the most volume flowing into it (100k). **Activation (completed→activated, 50%)** is the other. The top-of-funnel 20% looks like the priority by *opportunity* (huge volume), but a chunk of that is low-intent browsers. The **activation step (50%) is the priority I'd act on first**: these are people who *signed up* (high intent) and half never reach value — that's friction/onboarding, highly fixable, and it gates everything downstream.

## Opportunity size
Lift **activation from 50% → 65%** → ~9,100 activated (vs 7,000) → at the same downstream rates that flows to ~**+340 paid/mo ≈ +$10.2k MRR (~$122k ARR)**. (Top-of-funnel: lifting pricing→signup from 20%→24% adds ~4k signups but, at current downstream rates, only ~240 extra paid — and likely lower-intent.)

## Segment view
Need to split activation by: device (mobile activation often much lower), acquisition channel (paid vs organic intent differs), and first-session behavior. Hypothesis: mobile and paid-channel users activate worse — check before building.

## Hypotheses & how to check
- **Onboarding friction** (too many steps to first value) → session replays of non-activators + the `ui-states-matrix`/empty-state of the first screen.
- **Aha-moment unclear** (users don't reach the core action) → event funnel within onboarding; where exactly do they stall.
- **Wrong-fit signups** from a channel → segment activation by channel.

## Recommendation
Focus first on **activation (completed signup → used core feature)** — biggest fixable prize from high-intent users and it multiplies everything below it. Next diagnostic: segment activation by device + channel and watch 10 session replays of non-activators before committing to a fix.
