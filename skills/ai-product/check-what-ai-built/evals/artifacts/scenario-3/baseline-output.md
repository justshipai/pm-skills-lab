# Acceptance review: global search caching

**Ship decision: Do not ship.** The feature fails two explicit acceptance requirements and introduces a cross-workspace data-isolation defect.

## Evidence

- **Critical — cached results can cross workspace boundaries.** In `src/search.js`, the cache key is only `query.toLowerCase()`. It does not include `workspaceId`. After searching `renewal` in Beacon, the same query in Acme returns Beacon's cached document without reapplying the workspace filter. The included demo reproduces this exactly: both calls return `b1` from Beacon. My focused check expected Acme result `a1` but received `b1`. This violates “current workspace only” and can expose one workspace's result metadata to another.
- **High — returning from a result does not preserve search state.** `openResult` stores the previous state, but `returnToSearch` ignores it and always returns `query: ''` and `type: 'all'`. A focused round-trip check starting with `query: 'renewal'` and `type: 'documents'` failed because both values were reset.
- **High — projects are not included.** The implementation exports only `searchDocuments` and filters a document collection. There is no project search, combined global-search path, or test demonstrating project results, so the requirement to search both projects and documents is unmet.
- **Tests are green but insufficient.** `node --test` passes 2/2 tests. Those tests cover one uncached document search in one workspace and verify only that `openResult` records previous state. They do not cover identical queries across workspaces, project results, cache behavior, or the `returnToSearch` round trip. The passing suite therefore does not mitigate the failures above.

## Required before approval

Key cached entries by every result-affecting scope, at minimum workspace and normalized query (and result type if types are cached separately), so cached data cannot be reused across tenants. Implement and test global results for both projects and documents within the active workspace. Restore the stored query and selected result type on return. Add regression tests for same-query searches across two workspaces in both cache orders, project/document inclusion and filtering, cache hits, and the complete open/return navigation flow.
