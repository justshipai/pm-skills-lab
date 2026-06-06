---
name: launch-tiering
description: Use when planning a product/feature launch and deciding how much launch effort it deserves. Produces a launch tier (T1/T2/T3) chosen against explicit criteria, with the launch activities and channels right-sized to that tier — so a minor update gets a changelog note and a flagship gets the full motion. Pushes back on treating everything as a big launch (or nothing as one).
---

# Launch tiering

Two failure modes: spraying full-launch effort on every minor feature (the team burns out and audiences tune out), or quietly shipping something important with no launch at all. Launch tiering fixes both — it sizes the launch to the thing being launched. This skill assigns a tier against clear criteria and right-sizes the activities, so effort matches impact.

## The tiers

- **T1 (flagship / major):** big news — new product, major capability, strategic bet. Full motion: positioning, PR, exec/launch event, sales enablement, campaign, lifecycle, coordinated cross-functional plan.
- **T2 (notable):** a meaningful feature worth a real announcement. Blog post, in-app + email, social, sales heads-up, docs — but not the full circus.
- **T3 (minor / continuous):** improvements, fixes, small additions. Changelog/release notes, maybe an in-app note. No campaign.

## The judgment this skill encodes

- **Tier by impact and audience, not by how hard it was to build.** A small change that affects every user or unlocks revenue can be T1; a complex backend feature few notice can be T3. Score on *who cares and how much*, not engineering effort.
- **Criteria for the tier:** strategic importance, size of affected audience, revenue/competitive impact, novelty/newsworthiness, and risk (a risky launch needs more comms + a rollback plan regardless of tier).
- **Right-size the activities to the tier.** The output isn't just a label — it's the *matched* set of launch activities/channels/owners. Don't prescribe a press release for a T3.
- **Push back both ways.** If they're planning a huge launch for a minor feature, say so (tier it down — protect the team and the audience's attention). If they're sneaking out something important, tier it up.
- **Reserve T1.** If everything is T1, nothing is. Most launches are T2/T3; T1 is rare and earns the full motion.
- **Match internal readiness to the tier.** Higher tiers need more enablement (sales, support, docs) and a clearer go/no-go; don't fire the campaign before support is ready.

## Process

1. **Assess the launch** against the criteria (strategic importance, audience size, revenue/competitive impact, newsworthiness, risk).
2. **Assign the tier** (T1/T2/T3) with the reasoning — and push back if the proposed effort mismatches.
3. **Right-size activities** — the channels, assets, and cross-functional steps appropriate to that tier.
4. **Owners & timeline** at the right weight; go/no-go for higher tiers.
5. **Risk overlay** — extra comms / rollback if the launch is risky regardless of tier.

## Output format

```
# <Launch> — Tiering & Plan

## Assessment            (criteria: strategic / audience / revenue / newsworthy / risk)
## Tier                  (T1 / T2 / T3 — and why; note if the proposed effort mismatches)
## Right-sized activities  (channels, assets, cross-functional steps for this tier)
## Owners & timeline       (weight matched to tier; go/no-go if T1/T2)
## Risk overlay            (extra comms / rollback if risky)
```

## Anti-patterns to refuse

- Treating every launch as a big launch → Tier it; right-size effort.
- Tiering by build effort → Tier by impact and audience.
- A tier label with no matched activity set → Specify the activities for the tier.
- Full motion (PR, campaign) on a T3 → Scale down to changelog/in-app.
- Everything is T1 → Reserve T1; most things are T2/T3.
