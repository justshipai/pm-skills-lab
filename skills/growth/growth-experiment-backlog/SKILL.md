---
name: growth-experiment-backlog
description: Use when turning growth ideas into a prioritized experiment backlog. Produces experiments written as testable hypotheses (if we do X, metric Y moves because Z), each tied to the specific funnel/loop stage it targets, ICE-scored, and sequenced by expected learning and effort — not a brainstormed list of tactics.
---

# Growth experiment backlog

Growth isn't a list of tactics to do — it's a queue of *hypotheses to test*, ordered so you learn the most for the least effort. This skill turns "here are some growth ideas" into a real experiment backlog: each idea framed as a falsifiable bet on a specific metric at a specific stage, scored, and sequenced — so the team runs the highest-leverage tests first instead of doing whatever's loudest.

## The judgment this skill encodes

- **An experiment is a hypothesis, not a task.** Write each as **"If we [change], then [specific metric] will [move by ~], because [reason]."** "Add a referral program" is a task; "If we add a post-purchase referral prompt, week-4 referred-signup share rises to ~5%, because that's the delight moment" is an experiment. Falsifiable = runnable.
- **Tie each to one funnel/loop stage and metric.** Acquisition, activation, retention, referral, revenue — name which lever it pulls and the one metric it should move. Spreads of "general growth" don't get measured.
- **Score with ICE (Impact × Confidence × Ease).** Impact = how much it could move the metric; Confidence = evidence it'll work; Ease = effort to run. Score 1–10 each; ICE = the driver of order. Be honest about confidence (most ideas are low).
- **Sequence by learning, not just score.** Run cheap, high-uncertainty tests that *unlock* big decisions early (high learning value), even if their direct impact is modest. A quick test that tells you whether a whole channel works beats a sure +2%.
- **Target the constraint.** Prioritize experiments on the stage that's actually limiting growth (the leakiest step / weakest loop stage), not the stage that's easiest to ideate on. (Pairs with `funnel-analysis` / `growth-loop`.)
- **Define success and the decision up front.** Each experiment states the metric, the bar that counts as a win, and what you'll do if it wins/loses — so results turn into decisions.
- **Small, fast, reversible first.** Favor tests you can run this week over quarter-long builds; you're buying *learning rate*.

## Process

1. **Anchor to the constraint** — which stage limits growth right now (brief).
2. **Frame each idea as a hypothesis** — if X then metric Y because Z; tag the stage.
3. **ICE-score** each (Impact / Confidence / Ease, 1–10) → ICE.
4. **Add learning value** — does it de-risk a bigger bet? (can re-rank above raw ICE).
5. **Sequence** — the order to run, highest leverage/learning first; note what each unlocks.
6. **Define success + decision** per top experiment.

## Output format

```
# <Product> — Growth Experiment Backlog

## The constraint we're attacking   (the limiting stage; brief why)
## Backlog
   | Experiment (if X → metric Y because Z) | Stage | Impact | Conf | Ease | ICE | Learning value |
## Run order                         (sequenced; what each unlocks)
## Top 3 — success metric & decision  (win bar + what we do win/lose)
```

## Anti-patterns to refuse

- A brainstormed list of tactics → Rewrite each as a falsifiable hypothesis with a metric.
- No stage/metric per idea → Tag the funnel/loop stage and the one metric.
- No prioritization → ICE-score and sequence.
- Ranking only by raw impact → Weight learning value / de-risking, and target the constraint.
- No success bar or decision → Define the win threshold and the if-win/if-lose action.
