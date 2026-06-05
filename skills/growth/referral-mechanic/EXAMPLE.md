# Example: referral-mechanic

## Input

> Design a referral program for our meal-kit subscription. Someone suggested
> "$20 off for you and your friend." Our CAC is ~$45, a subscriber's first-year
> margin (LTV-ish) is ~$120.

## Output

# Meal-Kit Referral — Mechanic

## Viral math
Realistic for a meal-kit: an active subscriber might invite ~1–2 friends over their lifetime, converting at maybe ~15–25%. So **k ≈ 1.5 × 0.2 ≈ 0.3.** That's well under 1.

## Honest verdict
**This is a CAC-reducer, not a viral engine.** A k of ~0.3 means referrals add ~30% on top of other channels' cohorts — valuable, but it won't self-sustain growth. Design it as cheaper, higher-trust acquisition, and don't pitch leadership a "viral loop."

## Incentive
**Two-sided, paid on the friend's first paid box** (not signup):
- Friend: $20 off first box (lowers their trial risk — drives conversion, the weak half of k).
- Referrer: $20 credit *after the friend's first box ships and isn't refunded.*
- Total ≈ $40/successful referral < $45 CAC ✓, and tiny vs. $120 LTV ✓ — so it's accretive even before counting higher referred-user retention (referred users usually retain better). Headroom to raise the friend-side incentive if conversion lags.

## Share trigger
Ask **after a delightful moment** — e.g. right after they rate a meal 5★ or complete their 2nd box (not at signup, when they have nothing to vouch for). One-tap share with a pre-filled message + a personal link/code. Surface "give $20, get $20" in the post-delivery flow. This is the lever for invites/user (the other half of k).

## Abuse guardrails
Meal-kit referrals get farmed for the discount: gate the referrer payout on the friend's **first box shipped + payment cleared + not refunded**; block self-referral (same payment instrument / address / device); cap referrer rewards per period; watch for clusters of one-box-then-cancel.

## Metrics & kill criterion
Track **k**, **referral CAC** (total incentives ÷ activated referrals), and referred-user retention vs. baseline. **Kill/scale rule:** if referral CAC < paid CAC ($45) *and* referred users retain ≥ as well, scale the trigger surface; if referral CAC creeps above paid channels, cut the incentive or stop.
