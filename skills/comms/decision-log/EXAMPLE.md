# Example: decision-log

## Input

> Log this decision: after debate, we decided to launch our new AI feature as a
> paid add-on rather than bundling it into the existing plans. Main reason was
> protecting margin given inference costs, though some worried it'd slow adoption.

## Output

# Decision: Launch the AI feature as a paid add-on, not bundled into existing plans
- **Date / Decider:** 2026-06-05 · [PM], with [Head of Product] approving
- **Reversibility:** **Two-way door** — we can bundle it later (easy); pulling it back out of bundled plans after launch would be much harder. So launching as an add-on keeps the reversible option open.

## Context
The new AI feature carries real per-use inference cost (unlike the rest of our product). We had to decide how to package/price it before launch.

## Options considered
- **Bundle into all plans (no extra charge)** — best for adoption, but exposes margin to heavy users; hard to reverse once customers expect it free.
- **Paid add-on** *(chosen)* — protects margin, lets us learn real usage and willingness-to-pay, and keeps bundling as a future option.
- **New top tier that includes it** — cleaner packaging but forces a plan migration and a bigger pricing change now.

## Decision & rationale
Launch as a **paid add-on**. The deciding factor was margin protection against unknown inference costs combined with reversibility: an add-on is a two-way door (we can bundle later once we understand usage), whereas free-bundling is effectively one-way. We accept the risk of slower initial adoption in exchange for learning real usage/WTP and keeping options open.

## Assumptions / revisit if…
- We assumed inference cost per user is material and variable. **Revisit if** inference costs drop sharply, OR add-on attach-rate is so low it's clearly suppressing adoption of a strategically important feature — at which point bundling (the open two-way door) is back on the table.
