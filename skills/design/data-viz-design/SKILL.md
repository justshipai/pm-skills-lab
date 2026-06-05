---
name: data-viz-design
description: Use when designing a chart, dashboard, or data visualization — deciding how to show data, not just defaulting to a chart type. Produces a viz design that starts from the question/decision, picks the encoding that fits the data, strips chart-junk, stays accessible and non-misleading, and surfaces the takeaway — not "throw it in a pie chart".
---

# Data viz design

Most charts are chosen by habit (pie chart, default bar) rather than by what the data is and what question it answers — so they mislead, bury the point, or are unreadable. This skill designs a visualization the right way: start from the **decision the viewer needs to make**, match the **encoding to the data relationship**, remove everything that isn't signal, and make the **takeaway** obvious. Useful for dashboards and prototype charts (incl. ones generated in Bolt/v0, which default to whatever the library makes easy).

## The judgment this skill encodes

- **Question first, chart second.** What decision or comparison does the viewer need? The chart serves that. If you can't name the question, you can't pick the chart.
- **Match encoding to the data relationship:**
  - *Trend over time* → line. *Comparison across categories* → bar (sorted). *Part-to-whole* → bar/stacked or a single stat; **avoid pie/donut** beyond 2–3 slices. *Correlation* → scatter. *Distribution* → histogram/box. *A single key number* → big number, not a chart.
- **Pie charts are usually the wrong answer.** Humans compare angles poorly. Default to a sorted bar; reserve pie for 2–3 parts where part-to-whole is the literal point.
- **Maximize data-ink, kill chart-junk (Tufte).** Remove gridlines, 3D, heavy borders, redundant legends, decorative gradients. Every pixel should carry information.
- **Label directly; minimize legend lookup.** Put labels on/near the data; don't make the eye ping-pong to a legend.
- **Don't mislead.** Bar charts start the axis at zero; don't truncate to exaggerate. Don't dual-axis to imply correlation. Note when a scale choice changes the story.
- **Accessible.** Don't encode meaning by color alone (use labels/patterns); check color-blind-safe palettes and contrast.
- **Show the takeaway.** A good chart has a title that states the *insight* ("Signups fell 30% after the price change"), not just the variable ("Signups by week"), and highlights the relevant point.

## Process

1. **The question/decision** the viz must answer, and the audience.
2. **The data relationship** (trend / comparison / part-to-whole / correlation / distribution / single value).
3. **Pick the encoding** that fits — justify it; note what you rejected (e.g. why not a pie).
4. **Strip to signal** — what to remove (junk) and how to label directly.
5. **Integrity & accessibility** — axis/scale honesty, color-not-alone, contrast.
6. **Takeaway** — the insight-led title and what to highlight. (For a dashboard: the few charts that matter and their layout.)

## Output format

```
# <Data/Dashboard> — Visualization Design

## Question & audience       (the decision this must support)
## Data relationship          (trend / comparison / part-to-whole / …)
## Recommended chart          (the encoding + why; what was rejected & why)
## Strip to signal            (chart-junk to remove; direct labeling)
## Integrity & accessibility   (axis honesty; not color-alone; contrast)
## Takeaway & title            (insight-led title; what to highlight)
## (Dashboard) layout          (which charts, ordered by importance — if applicable)
```

## Anti-patterns to refuse

- Defaulting to a pie chart / a chart type by habit → Start from the question and the data relationship.
- Decorative junk (3D, gradients, heavy gridlines) → Strip to data-ink.
- Legend the eye has to hunt → Label directly.
- Truncated/zoomed axes that exaggerate → Honest scale; flag the effect.
- Color-only encoding → Add labels/patterns; check color-blind safety.
- Variable-name title ("Revenue by month") → Insight-led title that states the point.
