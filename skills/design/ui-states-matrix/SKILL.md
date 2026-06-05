---
name: ui-states-matrix
description: Use when designing or speccing a screen, component, or flow and you need to cover every state it can be in — not just the happy path. Produces a complete state matrix (empty, loading, partial, error, success, permission, offline, and the data edge cases) with what each state shows and does, so the design and the build handle reality instead of breaking on the first non-ideal input.
---

# UI states matrix

Designs and prototypes look great in the demo and fall apart in production because only the **success state** was designed. The empty state is a blank void, the loading state janks, the error state is a raw stack trace, and a list with 0 or 10,000 items breaks the layout. This skill forces the full **state matrix** for a screen or component: every state it can be in, what it shows, and what the user can do — the unglamorous work that separates a real product from a mockup.

Pairs with `prototype-brief` (which embeds these states) and any spec work.

## The states to cover (don't skip the boring ones)

- **Empty** — first-use / no data yet. (What it says + the CTA to get started — never a blank screen.)
- **Loading** — initial load and subsequent loads (skeleton vs. spinner; partial/streaming).
- **Partial** — some data, more loading (pagination, infinite scroll).
- **Error** — failed to load / failed to act (clear message + a way to recover/retry; never a dead end).
- **Success / populated** — the happy path (and a "just completed an action" confirmation).
- **No-permission / restricted** — the user can't see or do this (graceful, not a crash).
- **Offline / degraded** — no/poor connectivity, if relevant.
- **Data edge cases** — zero items, one item, very many items, very long text/names, missing optional fields, stale data.

## The judgment this skill encodes

- **The forgotten states are empty, loading, and error.** These are where products feel broken. Treat them as first-class, designed states with real copy and a recovery path — not afterthoughts.
- **Empty states are an opportunity, not a void.** Explain what goes here and how to fill it; first impressions happen in the empty state.
- **Errors must offer a way out.** Every error names what happened (plainly) and what to do next. No dead ends, no raw errors.
- **Design for the data extremes.** Zero, one, and ten-thousand items all need to look intentional; long strings must not break layout.
- **Per state: what it shows AND what you can do.** A state isn't just a visual; it's the actions available in it.
- **Only the states that apply.** Don't invent offline handling for a server-rendered report — pick the states relevant to this surface.

## Process

1. **Identify the surface** — the screen/component/flow and what data/actions it involves.
2. **Walk the state list** — keep the applicable states; add domain-specific ones.
3. **For each state:** trigger, what's shown (incl. copy intent), and available actions / recovery.
4. **Enumerate the data edge cases** (0 / 1 / many / long / missing).
5. **Flag the riskiest** — which states are most likely to be skipped or to break, and matter most.

## Output format

```
# <Screen/Component> — UI States Matrix

## Surface              (what it is; the data & actions involved)
## States
   | State | Trigger | What it shows | Actions / recovery |
   (empty / loading / partial / error / success / permission / offline as applicable)
## Data edge cases      (0 items / 1 / many / long text / missing fields / stale)
## Watch out for        (the states most likely to be skipped or to break)
```

## Anti-patterns to refuse

- Designing only the success state → Force empty, loading, and error as designed states.
- An empty state that's a blank screen → Give it copy + a CTA.
- An error with no recovery → Add a retry / next step.
- Ignoring data extremes → Cover 0 / 1 / many / long / missing.
- Listing states with no actions → Say what the user can do in each.
