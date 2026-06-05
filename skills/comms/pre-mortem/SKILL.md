---
name: pre-mortem
description: Use when de-risking a launch, project, or plan before committing — running a pre-mortem to surface what could make it fail. Produces an "imagine it failed, why?" analysis that classifies risks (Tigers / Paper Tigers / Elephants), rates likelihood × impact, and assigns a mitigation and owner to each one that matters — not a generic risk list.
---

# Pre-mortem

A pre-mortem flips risk assessment: instead of "what might go wrong?", you stand at a point in the future where the project **has already failed** and ask "what killed it?". This prospective hindsight surfaces risks people won't otherwise voice — and the social permission to name the elephant. This skill runs that exercise and turns it into a prioritized, owned mitigation plan.

## The judgment this skill encodes

- **Imagine the failure first.** Frame it as "it's launch + 3 months and this flopped — what happened?". This wording unlocks honesty that "any concerns?" never does.
- **Classify the risks (the useful part):**
  - **Tigers** — real, dangerous threats. Address them.
  - **Paper Tigers** — things that *feel* scary but won't actually hurt you. Name them so the team stops worrying about them.
  - **Elephants** — risks everyone privately knows but no one says out loud (the under-resourced team, the exec's pet feature, the dependency no one owns). Surfacing these is the whole point.
- **Rate likelihood × impact, then focus.** Not every risk earns a mitigation. Spend energy on high-likelihood/high-impact Tigers and the Elephants.
- **Every risk that matters gets a mitigation AND an owner.** A risk with no owner is a risk you've documented, not managed. Include an early-warning signal where you can.
- **Cover the categories people skip.** Not just technical — adoption/value, GTM, dependencies, team/capacity, stakeholder/political, external.
- **Separate "prevent" from "detect."** Some risks you reduce up front; others you can only watch for — say which, and what the trigger is.

## Process

1. **Set the scene** — "it's [date], the launch failed. Why?" State what success was meant to look like.
2. **Surface failure modes** across categories; explicitly prompt for Elephants (what aren't we saying?).
3. **Classify** each as Tiger / Paper Tiger / Elephant.
4. **Rate** likelihood and impact; pick the vital few.
5. **Assign mitigation + owner + early-warning signal** for each Tiger/Elephant that matters; explicitly dismiss Paper Tigers.

## Output format

```
# <Project> — Pre-mortem

## The scene                 (it's <date>, this failed — and what success was meant to be)
## Failure modes
   | Risk (how it killed us) | Type (Tiger/Paper Tiger/Elephant) | Likelihood | Impact | Mitigation | Owner | Early warning |
## Top risks to act on now    (the vital few — Tigers + Elephants)
## Paper Tigers (stop worrying about these)
## Watch list                 (can't prevent, will monitor — trigger)
```

## Anti-patterns to refuse

- A generic risk list with no failure framing → Reframe as "imagine it failed, why?".
- Only technical risks → Force adoption, GTM, team, dependency, and political failure modes.
- No Elephants surfaced → Push: what does everyone privately worry about but isn't saying?
- Risks with no owner → Assign one to each that matters.
- Treating all risks equally → Rate and focus on the vital few; dismiss Paper Tigers.
