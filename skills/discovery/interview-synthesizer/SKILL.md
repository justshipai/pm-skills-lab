---
name: interview-synthesizer
description: Use when turning raw user-interview notes or transcripts into structured insight — synthesizing one or many interviews into themes, jobs, and evidence. Produces themes backed by verbatim quotes and an honest read on evidence strength, separating what users DID from what they SAID and flagging where you're over-reading thin data.
---

# Interview synthesizer

A summary of an interview is not insight. The job is to turn messy transcripts into **themes grounded in evidence** — what people actually did, how often, and how strongly the data supports each conclusion — without laundering one person's offhand comment into "users want X." This skill synthesizes interviews the way good researchers do: quotes first, claims second, confidence stated.

## The judgment this skill encodes

- **Separate behavior from opinion.** What someone *did* (switched tools, built a workaround, abandoned a task) is strong signal; what they *said they'd want* is weak. Tag and weight accordingly.
- **Theme by pattern, not by anecdote.** A theme needs recurrence across people or strong evidence from one. One vivid quote is a hypothesis, not a finding.
- **Quote the evidence.** Every theme carries 1–3 verbatim quotes (or specific observed behaviors). No quote, no theme.
- **State evidence strength honestly.** Mark each theme strong / moderate / weak based on how many sources support it and whether it's behavior or opinion. Resist the pull to overclaim.
- **Surface the jobs and pains, and the surprises.** Extract the underlying job-to-be-done, the pains/workarounds, and especially the things that contradicted your assumptions.
- **Note bias and gaps.** Small n, leading questions, a skewed sample — say what this data can't tell you, and what to ask next.

## Process

1. **Read for behavior and verbatims** — pull the specific actions, workarounds, and quotable moments.
2. **Cluster into themes** — group recurring patterns; name each theme as the user's reality, not your solution.
3. **For each theme:** the insight, supporting quotes/behaviors, # of sources, and evidence strength (strong/moderate/weak).
4. **Extract jobs, pains, and surprises** that cut across themes.
5. **State confidence and gaps** — sample size, biases, what to validate next.
6. **Recommend next steps** — the questions or experiments the data points to (not features).

## Output format

```
# <Study> — Interview Synthesis

## Method & sample           (how many, who, caveats)
## Themes
   For each: **Theme** — insight | evidence: "<quote>" (+ behavior) | sources: N | strength: strong/moderate/weak
## Jobs & pains              (the underlying JTBD and the workarounds observed)
## Surprises / disconfirming  (what contradicted our assumptions)
## What we still don't know   (gaps, biases, sample limits)
## Suggested next steps        (questions / experiments, not features)
```

## Anti-patterns to refuse

- A narrative summary with no themes or quotes → Restructure into evidenced themes.
- "Users want <feature>" → Reframe as the underlying job/pain; features are hypotheses.
- Treating a single comment as a finding → Mark it weak / a hypothesis.
- Equal confidence on everything → Grade evidence strength per theme.
- Ignoring disconfirming data → Give surprises their own section.
