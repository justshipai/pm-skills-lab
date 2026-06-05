---
name: prototype-brief
description: Use when turning a feature idea into a build-ready brief or prompt for a prototyping / vibe-coding tool (Bolt, v0, Lovable, Claude artifacts, etc.). Produces a structured brief — screens, component breakdown, EVERY UI state, the data shape, interactions, and acceptance criteria — so the tool builds something complete and usable on the first pass, not just a happy-path mockup.
---

# Prototype brief

A vague prompt to a prototyping tool gets you a pretty happy-path screen that falls apart the moment you click anything. The quality of what these tools build is bounded by the brief you give them. This skill turns a feature idea into a **build-ready brief**: the screens, the components, **every state** (not just the success case), the data the UI binds to, the interactions, and what "done" means — so the first generated prototype is something you could actually demo or hand to an engineer.

Works with any prototyping / vibe-coding tool (Bolt, v0, Lovable, Claude artifacts). The brief is the leverage; the tool is interchangeable.

## The judgment this skill encodes

- **Specify states, not just the screen.** The #1 reason a generated prototype feels fake is it only built the success state. Demand empty, loading, error, and edge states up front (pairs with `ui-states-matrix`).
- **Name the components and the layout.** Break the screen into its parts (header, list, item, form, modal) so the tool builds structure, not a blob — and so it's reusable.
- **Give it the data shape.** Define the entities and fields the UI binds to (even fake/sample data). Tools improvise wildly without a data model; a tiny schema anchors them.
- **Specify interactions and flow.** What happens on click/submit/hover/empty? Where does each action lead? Prototypes are judged on whether things *work*, not how they look.
- **Set acceptance criteria.** A short "the prototype is right when…" list (incl. states and key interactions) so you can tell if the output is good — and re-prompt precisely if not.
- **Constrain the scope and style.** One flow, not the whole app; note the visual tone and any must-use components, and what's explicitly out of scope for this prototype.
- **Write it so it's paste-able.** The output should be usable as a prompt with minimal editing — concrete, ordered, unambiguous.

## Process

1. **Goal & scope** — what this prototype demonstrates; the one flow in scope (and what's not).
2. **Screens & layout** — the screen(s) and their component breakdown.
3. **States** — for each screen/key component: empty, loading, error, success, and the relevant edge cases.
4. **Data shape** — the entities/fields the UI uses, with sample values.
5. **Interactions & flow** — what each action does and where it goes.
6. **Style & constraints** — visual tone, component library if any, out-of-scope.
7. **Acceptance criteria** — how you'll know the build is right.

## Output format

```
# <Feature> — Prototype Brief
*(paste into Bolt / v0 / Lovable / artifacts)*

## Goal & scope            (what it demonstrates; the one flow; out of scope)
## Screens & components    (each screen broken into its parts)
## States                  (per screen: empty / loading / error / success / edge)
## Data shape              (entities + fields + sample data)
## Interactions & flow     (action → result → destination)
## Style & constraints
## Acceptance criteria      (the prototype is right when… — incl. states & interactions)
```

## Anti-patterns to refuse

- A one-line "make a screen that does X" brief → Expand to screens, states, data, interactions.
- Happy-path only → Force empty/loading/error/edge states.
- No data model → Add the entities/fields the UI binds to, with sample data.
- No acceptance criteria → Add them, so the output is checkable and re-promptable.
- Trying to spec the whole app → Scope to one demonstrable flow.
