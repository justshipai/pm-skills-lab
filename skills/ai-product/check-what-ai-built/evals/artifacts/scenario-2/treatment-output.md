# Feature acceptance report

## Verdict
Not ready

The feature must not ship. The migration is incompatible with the central product rule that existing projects remain active: it makes `archived_at` non-null with a current-time default, so an engine that applies it will give existing rows an archive timestamp, while a representative run of the exact DDL on SQLite failed before deployment because the default is non-constant. The same non-null constraint conflicts with restoration, which the application represents by setting the archive timestamp to null. The implementation also archives an active project without checking project state or actor. The two supplied tests pass, but they exercise only in-memory helpers and do not prove migration safety, persistence, admin access, or inactive-project eligibility.

## Intended outcome

Existing and newly created projects remain active and visible unless deliberately soft-archived. An admin can archive an inactive project without deleting its data, and that project can later be restored and become visible again.

Consequential contract labels:

- **Explicit:** Existing projects must remain active.
- **Explicit:** Project visibility must not change before explicit archiving.
- **Explicit:** An admin can archive an inactive project without deleting it.
- **Explicit:** An archived project can later be restored.
- **Assumption:** “Inactive” is a distinct project state that must be checked before archiving; the brief does not define how it is represented.
- **Assumption:** Naming an admin as the actor requires an application-level admin check; the brief does not explicitly state what non-admin roles may do.

## What changed

The feature adds an `archived_at` database column, in-memory archive and restore helpers, and visibility filtering based on the archive timestamp. It also changes newly created project objects to carry a null archive timestamp. The schema change has a much larger effect than the requested explicit archive action: it requires an archive timestamp on every database row and supplies the current time by default.

## Intent-to-evidence ledger

| Contract item | Source | Status | Evidence | Gap or consequence |
|---|---|---|---|---|
| Existing projects remain active through deployment | Explicit | **Fail** | Code inspection shows `archived_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP`. Running the exact migration against a SQLite database containing an existing project returned `OperationalError: Cannot add a column with non-constant default`. On engines that accept this DDL and apply the default to existing rows, those rows receive non-null archive timestamps. | Depending on engine, deployment either fails or changes existing projects to archived state; neither satisfies the request. |
| Visibility changes only after explicit archiving | Explicit | **Fail** | `visibleProjects` hides every project with a truthy archive timestamp, while the migration supplies a timestamp without a user archive action. | Existing rows can disappear from the default visible set solely because of deployment. |
| An admin can archive an inactive project | Explicit | **Unverified** | The in-memory `archiveProject` helper sets a timestamp, and the supplied archive/restore test passes. No persisted or actor-aware admin journey exists in the fixture. | The product-level admin archive operation has not been demonstrated. |
| Active projects are not archived through the inactive-only operation | Explicit | **Fail** | A focused run passed `{status: 'active'}` to `archiveProject`; it returned the same project with an archive timestamp, and `visibleProjects` hid it. The helper contains no state check. | The implementation accepts projects outside the requested eligibility boundary. |
| Archiving preserves project data | Explicit | **Unverified** | The helper uses object spread and retained the sample project's id, name, and status in a focused run; no database archive write or persisted-data check exists. | In-memory preservation is promising but does not prove the real soft-archive path retains stored data. |
| An archived project can be restored | Explicit | **Fail** | The supplied test and focused run show in-memory restoration by setting `archivedAt` to null. The database column is declared `NOT NULL`, so the schema cannot store that restored representation. | The tested helper behavior is incompatible with the persisted schema. |
| New projects start active and visible | Existing rule | **Unverified** | `createProject` returns `archivedAt: null`, and its unit test passes. The database default instead supplies the current timestamp when `archived_at` is omitted, while explicitly writing null conflicts with `NOT NULL`. | No demonstrated database create path can reliably preserve the application’s active state. |

## Unexpected changes

- **High blast radius:** The migration assigns or requires archive state for every project row instead of adding a nullable marker changed only by an explicit archive action.
- **Data-model conflict:** Application restore and create behavior uses a null archive timestamp, but the new schema forbids null.
- **Operability gap:** No reverse migration or recovery procedure is present for a deployment that fails or timestamps existing projects.

## Risks worth acting on

| Priority | Risk | Why it matters | Required action |
|---|---|---|---|
| Blocker | Migration fails or implicitly archives existing data | It can prevent deployment or hide projects without user action, directly violating two explicit requirements. | Replace it with a nullable `archived_at` migration that preserves existing rows as null; run it against representative existing data on the production database engine and verify row counts, values, and visibility. |
| Blocker | Restore state cannot be persisted | `restoreProject` produces null while the schema rejects null. | Align schema and persistence semantics, then prove archive followed by restore against the real database. |
| Blocker | Active projects can be archived | The requested operation is limited to inactive projects, but the helper has no eligibility check. | Define the inactive state and enforce it at the authoritative write boundary; add active and inactive integration tests. |
| High | Admin behavior and access boundary are absent | The implementation does not show that an admin can complete the persisted action or that actor rules are enforced. | Add the actor-aware application path and a focused authorization test based on the clarified non-admin policy. |
| High | Passing tests mask schema incompatibility | Both tests run only JavaScript objects and never apply the migration or write archive state. | Add migration and persistence integration tests; keep helper tests as lower-level coverage only. |

## Before shipping

1. Replace the migration with a nullable archive marker that leaves all existing values null, and add a safe reverse/recovery migration.
2. Apply and reverse the migration on the actual production database engine using representative existing and newly created rows; prove no project becomes archived or hidden during deployment.
3. Implement the persisted archive boundary with admin and inactive-state checks, then prove that an active project is rejected without state change.
4. Run an integration test that archives an eligible project, verifies its data is retained and hidden, restores it by clearing the timestamp, and verifies it is visible again.
5. Test the normal project-create path against the migrated schema and prove new projects start active and visible.

## Open questions

- What field or rule defines an “inactive” project? This is required to implement and test the eligibility boundary.
- Is archiving restricted exclusively to admins, or may any other role archive? The answer determines the required authorization tests, though it does not change the current **Not ready** verdict.
