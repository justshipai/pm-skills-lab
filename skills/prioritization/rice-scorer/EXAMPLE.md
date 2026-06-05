# Example: rice-scorer

## Input

> Prioritize these four with RICE: (1) Google SSO login, (2) onboarding
> checklist, (3) CSV export, (4) redesign the settings page. ~20,000 monthly
> active users; small team.

## Output

# Q3 Backlog — RICE Prioritization

## Units & assumptions
- **Reach window:** users affected per quarter.
- **Effort unit:** person-weeks (all functions).
- **Impact scale:** 3/2/1/0.5/0.25. **Confidence:** 100/80/50%.

## Scores
| Item | Reach (per qtr) | Impact | Confidence | Effort (pw) | RICE | Key assumption |
|---|---|---|---|---|---|---|
| Onboarding checklist | 6,000 new signups | 2 | 80% | 4 | **2,400** | Lifts activation for new users |
| Google SSO | 20,000 (all) | 0.5 | 100% | 3 | **3,333** | Minor friction reducer, but reliable & cheap |
| CSV export | 3,000 (power users) | 1 | 80% | 2 | **1,200** | Requested by data-heavy accounts |
| Settings redesign | 20,000 (all) | 0.25 | 50% | 6 | **417** | Unclear it changes behaviour |

## Ranked order
1. Google SSO (3,333) 2. Onboarding checklist (2,400) 3. CSV export (1,200) 4. Settings redesign (417)

## Sanity check
- **SSO tops the list** mostly because it's cheap and reaches everyone, despite low impact — a fair "quick win," ship it.
- **Onboarding checklist** is the higher-leverage bet (drives activation, a real goal); don't let SSO's narrow lead bury it — sequence both into the quarter.
- **Settings redesign** scores lowest *and* sits at 50% confidence (we're unsure it changes anything) → don't build yet; run a cheap test on the actual settings pain first.
- RICE ignores dependencies: if SSO unblocks enterprise deals (strategic), its true value is higher than the score shows — note for the strategy call.

## Recommendation
Do **SSO + onboarding checklist** this quarter (quick win + leverage bet), then **CSV export**. Park the settings redesign pending evidence.
