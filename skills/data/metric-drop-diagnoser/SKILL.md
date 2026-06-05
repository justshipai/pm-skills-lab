---
name: metric-drop-diagnoser
description: Use when a key metric suddenly moved (dropped or spiked) and you need to find out why. Produces a structured diagnosis — first confirm it's real (not an instrumentation/reporting bug), then segment to localize it, then separate internal change vs. external/seasonality vs. mix shift, ending in ranked hypotheses each with how to check — not a list of guesses.
---

# Metric drop diagnoser

When a metric drops, the instinct is to brainstorm reasons. The disciplined move is to *localize* the drop before theorizing — most "mystery drops" are either a tracking bug or are concentrated in one segment that points straight at the cause. This skill runs the diagnosis in the right order so you find the real reason fast instead of chasing plausible-but-wrong stories.

## The judgment this skill encodes

- **First, is it even real?** Before any theory: could this be an **instrumentation/reporting artifact** — a tracking change, a logging deploy, a data-pipeline delay, a definition change, a dashboard bug? A huge fraction of "drops" are measurement, not reality. Rule this out first.
- **Localize before you theorize.** Segment the metric to find *where* the drop lives: platform/OS, app version (a bad release!), geography, channel, new vs. returning, browser, device, customer tier. A drop concentrated in one segment usually names the cause (e.g. all on the new app version → a release bug).
- **Sudden vs. gradual tells you the type.** A sharp step-change points to a discrete event (a deploy, an outage, a pricing change, a tracking break, an external event). A gradual slide points to a trend (seasonality, decay, competition, mix shift).
- **Timeline it.** Line the drop up against a **change log** — what did we ship/change at that moment? Deploys, experiments, pricing, marketing, third-party/API changes. Correlate the timing.
- **External & seasonal.** Day-of-week/holiday/seasonality, an outage at a dependency, a platform change (iOS/Google update), a competitor move, the news. Compare to the same period last year/week.
- **Mix shift.** The metric can drop with no segment getting worse — if the *mix* shifted toward lower-performing segments (e.g. a marketing push brought low-intent traffic). Check composition.
- **Rank hypotheses by likelihood × checkability; give the check.** Output a short ranked list, each with the cheapest way to confirm or kill it. Don't present a guess as the answer.

## Process

1. **Confirm it's real** — instrumentation / tracking / pipeline / definition checks first.
2. **Characterize** — sudden vs. gradual, magnitude, when exactly it started.
3. **Segment / localize** — find where the drop concentrates (version, platform, geo, channel, cohort).
4. **Timeline vs. changes** — align with deploys/experiments/pricing/marketing/external events.
5. **Consider mix shift** — did composition change rather than any segment worsening?
6. **Ranked hypotheses + checks** — most-likely causes, each with how to confirm cheaply, and the first thing to look at.

## Output format

```
# <Metric> drop — Diagnosis

## Is it real?            (instrumentation / tracking / pipeline / definition checks — do these first)
## Shape & timing          (sudden vs gradual; when it started; size)
## Localize (segment)       (where the drop concentrates: version / platform / geo / channel / cohort)
## Timeline vs. changes     (what shipped/changed at that moment)
## Mix shift?               (did composition change vs. a segment getting worse)
## Ranked hypotheses        | hypothesis | likelihood | how to check |
## Start here               (the first check to run)
```

## Anti-patterns to refuse

- Jumping straight to theories → Confirm it's real (instrumentation) first.
- A flat brainstorm of reasons → Localize by segment, then rank with checks.
- Ignoring the change log → Timeline the drop against deploys/experiments.
- Assuming a segment got worse → Check for mix shift.
- Presenting one guess as the cause → Give ranked hypotheses + how to verify.
