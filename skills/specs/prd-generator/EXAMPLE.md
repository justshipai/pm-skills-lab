# Example: prd-generator

## Input

> Write a PRD for adding saved/reusable filters to our analytics dashboard.
> Users keep re-applying the same filter combinations every session.

## Output

# Saved Filters — PRD

## Problem & evidence
Power users re-apply the same filter combinations (date range + segment + metric) many times a day. Session replays show the average dashboard user sets filters 6× per session; 22% of support chats about "slow workflow" mention re-filtering. The dashboard treats every visit as a blank slate.

## Target user & job-to-be-done
**Analysts and ops users** who return to the same views repeatedly. **Job:** "When I open the dashboard, I want my usual view ready, so I can get to the answer without rebuilding it every time."

## Goals & success metrics
- **Primary:** reduce time-to-first-insight (dashboard open → first chart interaction) by 30%.
- **Adoption:** ≥ 40% of weekly active dashboard users save ≥ 1 filter within 60 days.
- **Guardrail:** dashboard load time must not regress.

## Solution overview
Let users save the current filter state as a named filter, see saved filters in a sidebar, apply one in a click, and set a default that loads on open. Saved filters are personal in v1; sharing is a non-goal.

## Requirements (prioritized)
- **P0 — Save current filters.** *As an analyst, I can save my current filter set with a name.* AC: name required; saving captures all active filters; appears in the list immediately; duplicate names disallowed.
- **P0 — Apply a saved filter.** AC: one click applies all of its filters; partial/invalid filters (e.g. a deleted segment) load what's valid and flag the rest — no crash.
- **P1 — Set a default.** AC: a chosen filter auto-applies on open; user can clear the default.
- **P1 — Edit/delete.** AC: rename, update to current state, delete with confirm.
- **P2 — Reorder/pin** saved filters in the sidebar.
- **Edge/error:** a saved filter referencing data the user lost access to → applies the rest, shows "1 filter skipped (no access)."

## Scope: in / non-goals
- **In:** personal saved filters, default, edit/delete.
- **Non-goals (v1):** sharing filters with teammates, scheduling/exports off a saved filter, cross-dashboard filters.

## Risks, dependencies & open questions
- Dependency: filter-state must be serializable across dashboard versions.
- Risk: schema changes break old saved filters → version them + graceful skip.
- Open: do defaults sync across devices? (Lean yes, account-level.)

## Rollout & milestones
Internal dogfood → 10% → GA. Milestone 1: save/apply (P0). Milestone 2: default + edit/delete (P1).
