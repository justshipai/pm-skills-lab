---
name: referral-mechanic
description: Use when designing a referral or invite program. Produces a mechanic grounded in the viral math (k-factor, cycle time) with an honest read on whether it can actually be viral or is really a CAC-reducer, a two-sided incentive sized against LTV/CAC, the right share trigger, and fraud/abuse guardrails — not "give everyone $10 for a referral".
---

# Referral mechanic

Most referral programs are designed by copying "$10 for you, $10 for them" and hoping it goes viral. It usually doesn't — and whether it can is a *math* question, not a vibe. This skill designs the mechanic from the viral math out: what k-factor is realistic, whether that means viral growth or just cheaper acquisition, and the incentive/trigger/guardrails that follow.

## The viral math (start here)

- **k-factor (virality coefficient) = (invites sent per user) × (conversion rate per invite).**
- **k ≥ 1 → self-sustaining viral growth.** This is rare; be skeptical of claims of it.
- **k < 1 → not viral, but still valuable:** it amplifies other channels and lowers blended CAC (each cohort brings a fraction more). Most good referral programs live here — *say so honestly* rather than promising virality.
- **Cycle time** (how long an invite→signup→invite loop takes) matters as much as k: a k of 0.6 that cycles weekly beats a k of 0.8 that cycles quarterly.

## The judgment this skill encodes

- **Estimate k before designing the rewards.** Realistic invites/user × realistic conversion. If k is going to be ~0.2, design it as a CAC-reducer with modest spend, not a "viral loop."
- **Size the incentive against unit economics.** Total reward (both sides) per successful referral must be < your CAC (and sensible vs. LTV). "Give $10 each" = $20/referral — fine only if CAC > $20 and LTV supports it. Two-sided (referrer + referee) usually beats one-sided.
- **Reward the value moment, not the signup.** Pay out when the referred user *activates/pays*, not on signup — or you'll farm worthless signups (and fraud).
- **Nail the share trigger.** Ask for the referral at a moment of delight/value (post-success, not at signup), make sharing one tap, pre-fill the message. The trigger drives invites/user (half of k).
- **Design against abuse from day one.** Self-referral, fake accounts, reward farming — gate payout on real activation, cap rewards, detect duplicate devices/payment. Referral programs attract fraud; budget for it.
- **Define the success metric and a kill criterion.** k-factor and referral-driven CAC vs. your other channels; if referral CAC isn't better, stop.

## Process

1. **Estimate k** — plausible invites/user × conversion; state the assumption and what k implies (viral vs. CAC-reducer).
2. **Honest verdict** — is this a growth engine or an acquisition discount? Design to match.
3. **Incentive** — one- vs two-sided, amount, sized against CAC/LTV; paid on activation not signup.
4. **Share trigger** — the moment and the mechanics that maximize invites/user.
5. **Abuse guardrails** — fraud vectors and the controls.
6. **Metrics & kill criterion** — k, referral CAC vs. other channels, when to stop.

## Output format

```
# <Product> — Referral Mechanic

## Viral math               (estimated k = invites/user × conversion; what it implies)
## Honest verdict            (viral engine vs. CAC-reducer — and design accordingly)
## Incentive                 (one/two-sided, amount, vs CAC/LTV; paid on activation)
## Share trigger             (the moment + one-tap mechanics that drive invites/user)
## Abuse guardrails          (fraud vectors + controls)
## Metrics & kill criterion   (k, referral CAC vs other channels; when to stop)
```

## Anti-patterns to refuse

- "$10 for you, $10 for them" with no math → Estimate k and size rewards vs. CAC/LTV.
- Promising virality with no k estimate → State k; if k<1, call it a CAC-reducer honestly.
- Rewarding on signup → Pay on activation/payment to avoid junk + fraud.
- Asking for referral at signup → Trigger at the value/delight moment.
- No fraud guardrails → Add abuse controls; referral programs get gamed.
