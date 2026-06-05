---
name: market-sizing
description: Use when estimating the size of a market or opportunity — TAM/SAM/SOM, or "how big is this?". Produces a market-sizing estimate built BOTH top-down and bottom-up, with every assumption stated and a sanity check between the two — not a single confident number pulled from the air.
---

# Market sizing

A market-sizing number is only as good as the assumptions you can see. The failure mode is one impressive-sounding figure ("it's a $50B market!") with no working shown. This skill produces a defensible estimate: **TAM / SAM / SOM**, computed **two independent ways** (top-down and bottom-up), with assumptions explicit and the two estimates cross-checked — so the reader can poke at the logic, not just trust the total.

## The three numbers

- **TAM** (Total Addressable Market) — total demand if everyone who could buy, did.
- **SAM** (Serviceable Addressable Market) — the slice your product + business model + geography can actually serve.
- **SOM** (Serviceable Obtainable Market) — the realistic share you can win in a given timeframe.

## The judgment this skill encodes

- **Do it both ways.** *Top-down*: start from a big published figure and narrow with %s. *Bottom-up*: # of potential customers × price × frequency. Bottom-up is usually more credible; top-down is a sanity ceiling. If the two disagree wildly, your assumptions are wrong — find out which.
- **Every assumption visible and sourced.** Each number used (population, % who fit, price, attach rate) is stated with where it came from or that it's an estimate. No hidden multipliers.
- **Bottom-up grounds reality.** "X potential customers, Y% have the problem acutely, willing to pay $Z/yr" forces honesty that a top-down "1% of a huge number" hides.
- **SOM is about winnability, not ambition.** Ground it in realistic share given competition, GTM capacity, and time — not "if we get 1%."
- **State what would change it.** The 2-3 assumptions the estimate is most sensitive to (the swing factors).
- **A range beats false precision.** Give a range and name the driver of the spread; a single decimal-pointed number is a tell that the math is fake.

## Process

1. **Define the market** precisely — who, what they buy, where. (Sizing is meaningless without this.)
2. **Top-down** — start from a credible total, narrow with stated %s to SAM.
3. **Bottom-up** — # potential customers × price × frequency → SAM, assumptions explicit.
4. **Reconcile** — compare the two; if they diverge, dig into which assumption is off.
5. **SOM** — realistic obtainable share over a timeframe, justified.
6. **Sensitivity + range** — the swing assumptions and a defensible range.

## Output format

```
# <Market> — Sizing (TAM / SAM / SOM)

## Market definition         (who/what/where — precisely)
## Top-down                  (start figure → %s → SAM; assumptions sourced)
## Bottom-up                 (# customers × price × frequency → SAM; assumptions)
## Reconciliation            (do the two agree? if not, which assumption?)
## TAM / SAM / SOM            (the numbers, as ranges)
## Sensitivity               (the 2-3 assumptions that swing it most)
```

## Anti-patterns to refuse

- One confident number with no method → Show top-down AND bottom-up.
- Hidden assumptions / unsourced multipliers → Surface every input.
- "We'll get 1% of a $Xbn market" as the SOM → Ground SOM in winnable share.
- False precision ($4.7283B) → Give a range and name the swing factor.
- Skipping the market definition → Define who/what/where first.
