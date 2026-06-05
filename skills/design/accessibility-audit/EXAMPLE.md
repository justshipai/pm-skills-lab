# Example: accessibility-audit

## Input

> Audit the accessibility of a prototype dashboard our team vibe-coded: a top nav
> with icon-only buttons, a sidebar, KPI cards (numbers in light gray), a chart,
> and a data table with row actions (pencil/trash icons). Red/green status dots.

## Output

# Dashboard Prototype — Accessibility Audit (WCAG)

## Context
A generated dashboard: icon-only top nav, sidebar nav, KPI cards, a chart, a data table with icon row-actions, and red/green status indicators. Typical AI-generated output — check the usual gaps.

## Findings
| Area / WCAG | Issue | Severity | Fix |
|---|---|---|---|
| Names/labels (4.1.2) | Icon-only nav and row-action buttons have no accessible name — screen readers say "button" | **Blocker** | Add `aria-label` ("Edit row", "Delete row", "Notifications") to each icon button |
| Focus visible (2.4.7) | Generated CSS removed focus outlines (`outline:none`) | **Blocker** | Restore a visible focus ring on all interactive elements (`:focus-visible`) |
| Keyboard (2.1.1) | Row actions only appear on hover → unreachable by keyboard | **Blocker** | Make actions keyboard-focusable and visible on focus, not hover-only |
| Contrast (1.4.3) | KPI numbers in light gray (~#aaa on white ≈ 2.3:1) | Major | Darken to ≥ 4.5:1 (e.g. #595959); these are the key content |
| Color alone (1.4.1) | Status shown only by red/green dots | Major | Add a text label or shape/icon difference, not just color |
| Structure (1.3.1) | Likely div-soup, no headings/landmarks | Major | Use real `<nav>`, `<main>`, headings; label regions |
| Forms (3.3.1) | (table filters, if any) — verify labels | — | Verify in-app |
| Target size (2.5.8) | Icon buttons look ~20px | Minor | Increase hit area to ≥ 24–44px |

## Blockers to fix first
1. **Accessible names** on all icon buttons (nav + row actions) — without these the dashboard is unusable with a screen reader.
2. **Visible focus** — restore it; the generated UI stripped it.
3. **Keyboard-reachable row actions** — hover-only hides them from keyboard users.

## Verify in-app
- Actual contrast ratios (measure rendered colors), tab order through the table, and screen-reader announcement of the chart (needs a text alternative/summary).
