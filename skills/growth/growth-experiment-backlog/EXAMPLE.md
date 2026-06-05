# Example: growth-experiment-backlog

## Input

> We have a pile of growth ideas for our SaaS: redesign the pricing page, add a
> referral program, shorten onboarding, start a blog, add Slack integration, try
> TikTok ads. Turn it into a prioritized experiment plan. Activation (signup→
> first value) is our weakest step.

## Output

# Growth Experiment Backlog

## The constraint we're attacking
**Activation (signup → first value) is the weakest step**, so we weight activation experiments up — fixing it multiplies the return on every acquisition idea. Acquisition ideas (blog, TikTok) are de-prioritized until the bucket holds.

## Backlog
| Experiment (if X → metric Y because Z) | Stage | Impact | Conf | Ease | ICE | Learning value |
|---|---|---|---|---|---|---|
| If we cut onboarding 5→3 steps, activation rises ~+8pp, because steps are where users drop | Activation | 8 | 6 | 7 | **336** | Med |
| If we add an in-product checklist to first value, activation +5pp | Activation | 6 | 5 | 8 | **240** | Med |
| If we add a post-activation referral prompt, referred signups → ~5% of new, because it's the delight moment | Referral | 5 | 4 | 6 | **120** | High (tests if referral works at all) |
| If we redesign pricing page, signup→trial +3pp | Acquisition | 5 | 4 | 5 | 100 | Med |
| If we add Slack integration, activation+retention rise for team users | Activation | 7 | 4 | 3 | 84 | Med |
| If we run TikTok ads, cheap signups | Acquisition | 5 | 2 | 4 | 40 | High (does the channel work?) but off-constraint |
| If we start a blog, organic signups in ~6mo | Acquisition | 6 | 3 | 2 | 36 | Low (slow) |

## Run order
1. **Shorten onboarding 5→3** (top ICE, hits the constraint, ~1 week). 2. **First-value checklist** (cheap activation lever, stack with #1). 3. **Referral prompt** (cheap, *high learning* — tells us if referral is worth building before investing). 4. Pricing-page test. Defer Slack (build-heavy), TikTok/blog (off-constraint, slow) until activation holds. *What #3 unlocks: whether to invest in the full `referral-mechanic` at all.*

## Top 3 — success metric & decision
- **Onboarding 3-step:** primary = activation rate; win = +5pp vs control (A/B). Win → ship + try further cuts. Lose → the drop isn't step-count; investigate *which* step via funnel.
- **First-value checklist:** activation rate; win = +3pp. Win → keep; Lose → remove (it's clutter).
- **Referral prompt:** referred-signup share + k; win = k contribution > 0.1 at acceptable CAC. Win → build the full mechanic; Lose → shelve referral, it's not our loop.
