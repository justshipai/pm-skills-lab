# Example: stakeholder-map

## Input

> I'm leading a project to migrate our billing system to a new payments provider.
> Help me map the stakeholders and how to manage them.

## Output

# Billing Migration — Stakeholder Map

## Power × Interest grid
- **Manage closely:** VP Finance (owns revenue + reconciliation), Eng Lead (Payments), Head of Customer Support.
- **Keep satisfied:** CTO, CFO.
- **Keep informed:** Sales (pricing impact), Data/Analytics (revenue reporting), Legal/Compliance (PCI).
- **Monitor:** Marketing, individual account managers.

## Engagement plan
| Stakeholder | Quadrant | Cares about | Needs from us | Cadence | Channel |
|---|---|---|---|---|---|
| VP Finance | Manage closely | Zero revenue leakage, clean reconciliation | Cutover plan, rollback, reconciliation proof | Weekly working session | 1:1 + doc |
| Eng Lead (Payments) | Manage closely | Feasibility, migration risk | Clear scope, test plan, timeline | Weekly + async | Standup + Slack |
| Head of Support | Manage closely | Customer impact during cutover | Comms plan, known issues, FAQ | Weekly | 1:1 + runbook |
| CTO | Keep satisfied | Architectural risk, security | Concise risk summary, decisions needed | Biweekly | Summary email |
| CFO | Keep satisfied | Cost, financial risk | Cost delta + risk one-pager | At milestones | Brief |
| Sales | Keep informed | Pricing/feature changes | Heads-up on any customer-facing change | Milestone updates | Group update |
| Legal/Compliance | Keep informed | PCI / data handling | Compliance checklist sign-off | At gates | Doc review |
| Marketing | Monitor | Any external comms | Notify only if customer-facing | As needed | — |

## Champions & blockers
- **Champion:** VP Finance — the migration fixes reconciliation pain they've flagged for a year. Enlist them to sponsor in exec reviews.
- **Likely blocker:** CTO — burned by a past migration; skeptical of risk. *Plan:* bring them a detailed rollback + phased-cutover plan early, 1:1, before the steering review — don't let the skepticism surface cold in front of the CFO.
- **Watch:** Support — supportive but will turn fast if cutover spikes tickets; over-invest in their runbook.

## Revisit
Once cutover is scheduled, Sales and Support move toward "manage closely" (customer-facing window); re-rate the map two weeks before go-live.
