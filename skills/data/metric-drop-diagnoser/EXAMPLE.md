# Example: metric-drop-diagnoser

## Input

> Our daily active users dropped ~15% starting last Tuesday and haven't recovered.
> Leadership is panicking. Why, and what do we check?

## Output

# DAU −15% (from last Tue) — Diagnosis

## Is it real? (do this first)
Before any theory, rule out measurement:
- Did we ship anything to **analytics/tracking** around Tuesday (SDK update, event rename, consent banner change that blocks logging)? A consent/cookie change or a renamed event silently drops counts.
- **Pipeline/definition:** is the DAU job complete for those days, and is "active" defined the same? Check for partial data or a dashboard filter change.
- Quick test: does an independent source (server logs, payments) show the same drop? If servers are flat but the dashboard dropped → it's tracking, not users.

## Shape & timing
**Sudden step-change** on a specific day (Tuesday), no recovery → points to a discrete event (a deploy, a tracking break, an outage), not a gradual trend.

## Localize (segment)
Split the −15% by:
- **App version / platform** — is it all on a new release, or one OS? (A bad Tuesday release or an iOS update is the classic cause.)
- **Geography** — one region? (a localized outage / CDN / regulation).
- **Channel / new-vs-returning** — did a marketing campaign end (fewer new) or did returning users stop?
A drop concentrated in one of these usually *is* the answer.

## Timeline vs. changes
Line Tuesday up against the **change log**: app releases, backend deploys, experiment launches, pricing/marketing changes, third-party/API changes, app-store updates. The cause is very often "what shipped Tuesday."

## Mix shift?
Check composition: did a high-frequency segment shrink (e.g. a big customer churned, or paid traffic that drove repeat visits got cut) without any individual segment "getting worse"?

## Ranked hypotheses
| Hypothesis | Likelihood | How to check |
|---|---|---|
| Tracking/consent change dropped logged events (not real) | High | Compare to server logs/payments; review Tue analytics deploys |
| Bad app release crashing/blocking a platform | High | DAU by app version & OS; crash rate by version |
| Marketing/acquisition cut → fewer new users | Med | New vs. returning split; channel volume |
| External (iOS update, outage at a dependency) | Med | Segment by OS/region; status of dependencies |
| Seasonality/holiday | Low | Compare to same week last year/month |

## Start here
**Confirm it's real first** — compare DAU to server logs/payments and check Tuesday's analytics/consent deploys. If it's real, immediately pull **DAU by app version + OS**; that one cut most often names the cause.
