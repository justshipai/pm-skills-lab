# Acceptance review: bulk project archive

**Decision: Do not ship.** The bulk path bypasses two explicit safety rules and allows prohibited projects to be archived.

## Blocking findings

1. **Members can bulk archive projects.** `bulkArchiveProjects` never checks `actor.role` (`src/projects.js:8-20`). Hiding the control from members in `canSeeBulkArchive` (`src/bulkArchiveUi.js:1-3`) is not authorization enforcement; a member who invokes the operation directly succeeds. A local check with `{ role: 'member' }` confirmed that the function returns the selected project with `archivedAt` set.

2. **Active projects can be bulk archived.** The bulk implementation checks selected projects only for unpaid invoices (`src/projects.js:11-14`) and applies `archivedAt` to every selected ID (`src/projects.js:16-19`). A local check with an active project confirmed that it was archived successfully.

These defects are release blockers because they violate the core permission and eligibility requirements and could cause unauthorized state changes.

## What is working

- Confirmation is respected: when `confirmed` is false, the project list is returned without archive changes (`src/projects.js:9`).
- Selected projects with unpaid invoices are rejected (`src/projects.js:11-14`).
- Archiving is non-destructive at this layer: selected objects are copied with an added `archivedAt` field, retaining their other data (`src/projects.js:17-19`).
- The single-project function still enforces admin-only access, inactive status, and no unpaid invoice (`src/projects.js:1-5`). However, this repository has no parent commit, so unchanged behaviour cannot be verified against a pre-feature baseline from git history.

## Verification and required fixes

The committed test suite passes all 4 tests with `node --test`, but it has no member or active-project coverage for the bulk function; its member test exercises only the single-project function (`test/projects.test.js:10-13`). Before shipping, enforce admin authorization and inactive-project eligibility inside the bulk operation itself, then add negative bulk tests for members and active projects. Re-run the full suite and verify mixed selections behave atomically when any selected project is ineligible.
