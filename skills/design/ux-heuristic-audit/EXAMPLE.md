# Example: ux-heuristic-audit

## Input

> Audit the UX of our multi-step checkout: cart → shipping → payment → review →
> confirm. Users are dropping off at payment.

## Output

# Checkout Flow — Heuristic Audit

## Context & user goal
A 4-step checkout; the user's goal is to pay and be done with confidence. Drop-off at payment suggests trust/clarity/error issues — weight those heavily.

## Findings (by heuristic)
| # | Heuristic | Issue (or ✓) | Sev | Fix |
|---|---|---|---|---|
| 1 | Visibility of status | No step indicator; users don't know how many steps remain | 3 | Add a "Step 3 of 4" progress indicator |
| 1 | Visibility of status | No spinner after "Pay" — users click twice | 4 | Disable button + show "Processing…"; prevent double-submit |
| 2 | Match real world | "Tokenization failed" shown to users | 3 | Plain message: "Your card couldn't be processed — check the number or try another card" |
| 3 | User control | No way to edit shipping from the payment step without losing entered card data | 3 | Allow edit-in-place or preserve state on back |
| 4 | Consistency | "Continue" vs "Next" vs "Proceed" used across steps | 2 | One consistent primary-action label |
| 5 | Error prevention | Card field accepts wrong length silently; only fails on submit | 4 | Inline validation + format-as-you-type; detect card type |
| 6 | Recognition | Order total not visible on the payment step | 3 | Persist an order summary on every step |
| 7 | Flexibility | No saved-card / express-pay option for returning users | 2 | Offer saved cards / express checkout |
| 8 | Minimalist | Marketing upsell banner competes with the pay button | 3 | Remove/peel back promos on the payment step |
| 9 | Help with errors | Generic "Error" on payment failure, no next step | 4 | Specific cause + what to do + keep entered data |
| 10 | Help | ✓ adequate (support link present) | 0 | — |

## Top must-fix (severity 3–4)
1. **#1/#9 Payment feedback & errors** (sev 4) — no processing state + unhelpful failures; this is very likely the drop-off cause. Fix first.
2. **#5 Inline card validation** (sev 4) — silent invalid input → failed submit → abandonment.
3. **#6 Persistent order total + #8 remove upsell on pay step** (sev 3) — trust/clarity at the moment of payment.

## Minor / cosmetic (severity 1–2)
Inconsistent button labels (#4), express-pay for returning users (#7).
