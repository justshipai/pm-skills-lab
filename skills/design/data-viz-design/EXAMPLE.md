# Example: data-viz-design

## Input

> We want to show our exec dashboard the breakdown of revenue across our 6 product
> lines for this quarter. Someone suggested a pie chart. Design the visualization.

## Output

# Revenue by Product Line — Visualization Design

## Question & audience
Audience: execs. Decision: *which product lines drive revenue, and which are lagging* — i.e. compare magnitudes across 6 categories and spot the outliers. (Not "what fraction of a whole" for its own sake.)

## Data relationship
Comparison across 6 categories (with an implicit part-to-whole). 6 categories is already too many for angle-comparison.

## Recommended chart
**Horizontal bar chart, sorted descending by revenue.** Bars make magnitude comparison precise; sorting instantly shows the leaders and laggards; horizontal fits long product-line names. **Rejected: pie/donut** — 6 slices force the eye to compare angles (which people do badly) and the ranking isn't obvious. If the part-to-whole share genuinely matters, add the % as a label on each bar rather than switching to a pie.

## Strip to signal
Remove gridlines, 3D, and the legend (label each bar directly with the product line + value). No gradient fills — one accent color, with the top/bottom bar optionally emphasized.

## Integrity & accessibility
Axis starts at zero (bars must). Don't color each bar a different hue for decoration (implies categories differ in kind) — single color, emphasis only where it carries meaning. Ensure labels meet contrast; don't rely on color to distinguish bars (they're labeled).

## Takeaway & title
Insight-led title: **"Two product lines drive 70% of Q3 revenue; [Line F] is shrinking."** Highlight the top two bars and flag the declining one (e.g. a small ▼ vs last quarter). For execs, pair the chart with that one-line so-what.

## (Dashboard) layout
If this sits on a dashboard: lead with the single revenue total (big number) + trend sparkline, then this sorted bar beneath it — total and direction first, breakdown second.
