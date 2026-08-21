# Feature acceptance report

## Verdict
Not ready

The bulk-archive happy path works, but two explicit safety rules fail in the executable implementation: a member can bulk archive an inactive project, and an admin can bulk archive an active project. The UI helper hides the action from members, but the bulk operation itself does not authorize the actor, so this is a permission bypass rather than a cosmetic gap. The repository's four automated tests pass, but neither failed boundary is covered.

## Intended outcome
Workspace admins can select multiple inactive projects and archive them only after confirmation. Members cannot archive projects. Active projects and projects with unpaid invoices remain unarchived. Archiving preserves project data, and the existing single-project archive behavior does not change. These are all **Explicit** requirements; no additional role hierarchy or archive lifecycle is assumed.

## What changed
Feature commit `2221ba6` adds a bulk-archive operation, an admin-only UI-visibility helper, and tests for the admin happy path and unpaid-invoice rejection. The bulk operation accepts an actor, selected IDs, and confirmation flag, then stamps selected records with an archive time. It checks unpaid invoices but does not check the actor's role or active status. The commit is the repository's root commit, so there is no pre-feature version available for comparison of single-project behavior.

## Intent-to-evidence ledger
| Contract item | Source | Status | Evidence | Gap or consequence |
|---|---|---|---|---|
| Admin can bulk archive multiple inactive projects after confirmation | Explicit | Pass | `node --test` passed the two-project confirmed happy-path test; code returns both records with `archivedAt` | End-to-end selection and confirmation UI is not present in the fixture |
| Members cannot archive projects | Explicit | Fail | Focused runtime check showed `memberCanSee: false` but `memberArchived: true`; `bulkArchiveProjects` never evaluates `actor` | Hiding the control does not prevent a direct or alternate caller from archiving |
| Active projects cannot be archived | Explicit | Fail | Focused runtime check returned `activeArchived: true`; bulk logic has no active-status check | Admins can archive an expressly ineligible project |
| Projects with unpaid invoices cannot be archived | Explicit | Pass | Automated test passed; bulk logic rejects a selected unpaid project before mapping changes | Covered at service level |
| No archive occurs without confirmation | Explicit | Pass | Focused runtime check reported `cancelledUnchanged: true`; unconfirmed calls return the input unchanged | No runnable UI evidence that confirmation is actually requested |
| Archiving does not delete project data | Explicit | Pass | Focused check preserved project count and name and left the input object unchanged; implementation spreads existing fields and adds `archivedAt` | Persistence behavior is outside this in-memory fixture |
| Existing single-project archive behavior remains unchanged | Explicit | Unverified | Current focused checks reject a member, active project, and unpaid invoice with the expected errors; all passed. However, the feature is the root commit and provides no prior implementation or regression baseline | Current behavior looks consistent with the stated rules, but “unchanged” cannot be established |
| Only admins see the bulk-archive control | Explicit permission outcome | Pass | Focused check showed the UI helper returns false for a member; code inspection returns true only for `role === 'admin'` | Visibility is not authorization and does not mitigate the failing service check |

## Unexpected changes
The authorization-sensitive operation is guarded only at the UI-visibility layer, creating a high-blast-radius permission bypass. No unrelated orphan change was found. Because the feature commit is also the repository's initial commit, the claimed preservation of existing single-project behavior cannot be audited against a parent version.

## Risks worth acting on
| Priority | Risk | Why it matters | Required action |
|---|---|---|---|
| Critical | Member bulk-archive permission bypass | A non-admin can change project state by calling the operation directly | Enforce `actor.role === 'admin'` inside the bulk operation and add a failing-then-passing member test |
| Critical | Active projects can be bulk archived | The implementation violates an explicit eligibility rule and can change protected projects | Reject any selected active project before applying changes and add active-only and mixed-selection tests |
| High | UI journey is unproven | A service flag is not evidence that users must confirm or can correctly select projects | Exercise the actual selection, confirmation, cancel, and error journeys when a runnable UI is available |
| Medium | Single-project regression claim is unauditable | The root commit has no prior behavior to compare | Supply the pre-feature revision or an authoritative regression suite and run it unchanged |

## Before shipping
1. Add role authorization and active-project validation to `bulkArchiveProjects`, with no records archived if any selected record is ineligible.
2. Add focused tests for member access, active projects, mixed eligible/ineligible selections, cancellation, and preservation of all records.
3. Run those tests plus the existing suite; directly verify that unauthorized and active-project calls fail.
4. Verify the real selection and confirmation journey, and compare single-project behavior with the pre-feature baseline if it exists.

## Open questions
- When a selection mixes eligible and ineligible projects, should the entire operation fail atomically or archive only eligible projects? This affects both implementation and acceptance tests.
- Is there a pre-feature revision or regression suite that can prove the single-project archive behavior remained unchanged?
