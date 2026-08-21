# Acceptance review: Project archiving

**Decision: Do not ship.** The feature has release-blocking data-migration, restoration, and access-control defects.

## Blocking findings

1. **The migration changes visibility for every existing project.** `db/002_project_archiving.sql:2` adds `archived_at` as `NOT NULL DEFAULT CURRENT_TIMESTAMP`. Existing rows therefore cannot remain unarchived, while `visibleProjects` in `src/projects.js:13-15` hides every project with an archive timestamp. This directly violates both “existing projects must remain active” and “do not change visibility until explicitly archived.” New database rows that omit the column would also default to archived.

2. **A restore cannot be persisted under the new schema.** `restoreProject` sets `archivedAt` to `null` (`src/projects.js:9-11`), but the database column is `NOT NULL`. The in-memory test passes without exercising that database constraint, so it does not demonstrate a working restorable archive.

3. **Admin-only and inactive-only rules are not enforced.** `archiveProject` accepts only a project and timestamp and unconditionally archives it (`src/projects.js:5-7`); there is no actor/role check or inactive-state validation anywhere in the implementation. A direct local call successfully archived an object explicitly marked `status: 'active'`. The supplied test also archives a newly created project without establishing inactivity or admin authority.

4. **Persistence and migration behavior are untested.** The implementation only returns copied JavaScript objects; it contains no database update path for archive or restore. The test suite has two in-memory tests and no coverage for existing-row migration, durable archive/restore, authorization, or rejection of active projects.

## Checks performed

`node --test` passes both supplied tests (2 passed, 0 failed). That result confirms the basic in-memory visibility helper works, but it does not cover any of the blocking requirements above.

## Required before approval

- Make `archived_at` nullable with a default of `NULL`, and ensure the migration preserves all existing rows as active.
- Persist archive and restore operations, including restoring by writing `NULL` successfully.
- Enforce admin authorization and reject archive attempts for active projects on the server-side operation.
- Add integration tests for migration of existing data, persistence across reloads, restore, visibility before explicit archive, authorization, and inactive-state enforcement.
