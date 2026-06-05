# Example: prototype-brief

## Input

> I want to prototype a "saved searches" feature for our job board in Bolt — users
> save a search and get a list of matching jobs. Write the brief.

## Output

# Saved Searches — Prototype Brief
*(paste into Bolt / v0 / Lovable)*

## Goal & scope
Demonstrate the saved-searches flow: a user views their saved searches, opens one, and sees matching jobs. **In scope:** the saved-searches list + the results view. **Out of scope:** creating/editing search filters, auth, real job data.

## Screens & components
1. **Saved Searches (list)** — page header ("Saved searches" + count); list of *SavedSearchCard* (name, filter summary, "new since last viewed" badge, last-run time); primary "New search" button.
2. **Search Results** — header (search name + edit/delete actions); result count + sort control; list of *JobCard* (title, company, location, salary, posted date, "new" tag); pagination/"load more".

## States
- **Saved Searches list:** *empty* ("No saved searches yet — save a search to track new jobs," with CTA); *loading* (3 skeleton cards); *error* ("Couldn't load your searches — Retry"); *success* (cards). 
- **Search Results:** *empty* ("No jobs match this search right now — we'll show new matches here"); *loading* (skeleton job cards); *error* (retry); *success*; *edge* — very long job titles truncate; 100+ results paginate.

## Data shape
```
SavedSearch { id, name, filterSummary, newCount, lastRunAt }
Job { id, title, company, location, salaryRange, postedAt, isNew }
```
Seed with ~3 saved searches and ~8 jobs (mix of new/old, one with a very long title, one search with 0 results).

## Interactions & flow
- Click a SavedSearchCard → Search Results for that search (clears its newCount badge).
- "New search" → (out of scope; show a placeholder toast).
- Edit/Delete on results header → delete asks confirm, returns to list; edit shows placeholder.
- Sort control reorders results client-side.

## Style & constraints
Clean, modern, light theme; use a standard component set (cards, skeletons, toasts). Mobile-responsive (cards stack). No custom branding needed.

## Acceptance criteria
The prototype is right when: all four list states and all five results states are reachable (add a way to toggle them for the demo); clicking a saved search navigates and clears its badge; the 0-results search shows the empty state (not a blank page); long titles don't break layout; it's usable on mobile width.
