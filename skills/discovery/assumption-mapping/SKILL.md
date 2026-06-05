---
name: assumption-mapping
description: Use when de-risking a product idea or feature before building — surfacing and prioritizing the assumptions it depends on. Produces the riskiest assumptions mapped across Value, Usability, Feasibility, and Viability (Marty Cagan's four risks), plotted by impact × evidence, with the cheapest test for each of the leap-of-faith ones.
---

# Assumption mapping

Every idea is a stack of assumptions wearing a trench coat. Most fail not because the team built it wrong but because a hidden assumption was false. This skill drags those assumptions into the light, sorts them across the **four product risks** (Cagan: Value, Usability, Feasibility, Viability), and prioritizes by **impact × how much evidence you have** — so you test the cheap, fatal "leap-of-faith" assumptions *before* committing, not after launch.

## The four risks (cover all of them)

- **Value** — will users want it / does it solve a real problem they'll choose us for? (Most ideas die here.)
- **Usability** — can users figure out how to use it?
- **Feasibility** — can we actually build and run it with our tech, data, time, skills?
- **Viability** — does it work for the *business* — pricing, margin, legal, GTM, channel, support, strategy fit?

## The judgment this skill encodes

- **Write assumptions as falsifiable statements.** "We assume X is true." Not vague risks. If it can't be proven false, it's not a testable assumption.
- **Force coverage of all four risks.** Teams over-index on Feasibility ("can we build it?") and skip Value and Viability, which is where things actually die. Make yourself fill every quadrant.
- **Prioritize by impact × evidence (the leap-of-faith zone).** The dangerous assumptions are high-impact (if wrong, the idea fails) and low-evidence (we're guessing). Those get tested first. High-evidence or low-impact ones can wait.
- **Separate assumption from fact.** Be honest about what you actually know vs. believe. "Users will pay" is almost always an assumption, not a fact.
- **Match the cheapest test to each leap-of-faith assumption.** The point is to learn fast and cheap — an interview, a fake-door, a landing page, a concierge test — not to build the thing to find out.

## Process

1. **Restate the idea** in one line, plus the outcome it's meant to drive.
2. **Brainstorm assumptions across all four risks** — write each as "We assume that…". Push hard on Value and Viability.
3. **Rate each** on impact (if false, how badly does the idea break?) and evidence (how much do we actually have?).
4. **Identify the leap-of-faith assumptions** — high impact, low evidence.
5. **Pick the cheapest test** for each leap-of-faith assumption, and the order to run them.

## Output format

```
# <Idea> — Assumption Map

## The idea & outcome
## Assumptions by risk
   - **Value:** We assume that… (impact: H/M/L · evidence: H/M/L)
   - **Usability:** …
   - **Feasibility:** …
   - **Viability:** …
## Leap-of-faith assumptions      (high impact × low evidence — test these first)
   | Assumption | Risk type | Cheapest test | What would change our mind |
## Test sequence                   (what to test first and why)
```

## Anti-patterns to refuse

- Only listing build/feasibility risks → Force Value and Viability assumptions too.
- Vague risks ("market might not like it") → Rewrite as falsifiable "we assume…" statements.
- Treating assumptions as facts → Mark evidence level honestly.
- A flat list with no prioritization → Plot impact × evidence and surface the leap-of-faith set.
- "Test = build the MVP" → Require a cheaper test that learns the same thing.
