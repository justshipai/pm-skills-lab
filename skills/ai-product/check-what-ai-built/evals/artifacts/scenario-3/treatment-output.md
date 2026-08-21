# Feature acceptance report

## Verdict
**Not ready.** The feature adds a working repeated-query cache, but its key contains only normalized query text. The committed demo and focused checks directly show cross-workspace leakage: the second workspace receives the first workspace's cached result for the same query. The return journey also explicitly resets the query and selected type. Both failures violate critical requirements, and project search remains unproven.

## Intended outcome
Users should get faster repeated global searches across both projects and documents, limited to the current workspace. After opening a result and returning, they must see the same query and selected result type. These are **Explicit** requirements. It is an **Assumption** that a result-type selector can represent at least projects, documents, and all results; the brief does not define its exact labels, cache lifetime, or freshness policy.

## What changed
The root feature commit adds an in-memory shared search cache, a document-search helper, navigation-state helpers, two tests, and a demo. The cache is global to the process and keyed only by lowercased query. The search helper filters workspace membership only on a cache miss. Opening a result stores the previous state, but returning ignores that stored state and constructs a blank search. No project-specific data source, combined project/document search path, or project test is present.

## Intent-to-evidence ledger

| Contract item | Source | Status | Evidence | Gap or consequence |
|---|---|---|---|---|
| Repeated searches use caching | Explicit | **Pass** | Code inspection shows a process-level `Map`. A focused check confirmed that `renewal` followed by `RENEWAL` returned the same cached result reference despite input data changing. | Caching exists, but no performance measurement proves the size of the improvement and there is no freshness policy. |
| Search includes documents from the current workspace | Explicit | **Fail** | The supplied cold-cache test passes for one workspace. However, the committed demo searches Beacon then Acme and returns Beacon's document to Acme; a focused reverse-order check returns Acme's document to Beacon. | Document search is not reliably scoped after the cache is warm. |
| Search includes projects from the current workspace | Explicit | **Unverified** | The only API is `searchDocuments`; the demo, tests, and fixtures exercise documents only. No combined result path or project coverage exists. | A required result type has no direct evidence. |
| Never return another workspace's result | Explicit invariant | **Fail** | `node demo.js` outputs Beacon's `b1` result for Acme. Focused testing confirmed the leak is order-dependent because the cache key omits workspace ID. | This is a tenant-isolation and potential data-disclosure defect. |
| Preserve query after opening a result and returning | Explicit | **Fail** | `openResult` retains the prior state, but `returnToSearch` ignores it. A focused journey returned `{ page: 'search', query: '', type: 'all' }` from a state whose query was `renewal`. | Users lose their search context. |
| Preserve selected result type after returning | Explicit | **Fail** | The same focused journey changed `type: 'documents'` to `type: 'all'`. No supplied test calls `returnToSearch`. | Users lose the selected result type. |
| Supplied automated checks pass | Supporting evidence | **Pass** | `node --test` ran 2 tests with 2 passes and 0 failures. | Tests cover only a cold-cache workspace search and recording previous state; they do not cover cache isolation, projects, or restoration. |

## Unexpected changes
The shared process-level cache is a high-blast-radius change because it crosses user and workspace requests. It has no workspace or result-type partitioning, TTL, bounded size, or automatic invalidation. The lack of tenant partitioning directly explains the observed leak; freshness and memory behavior are additional operational risks whose acceptable policy is unspecified.

## Risks worth acting on

| Priority | Risk | Why it matters | Required action |
|---|---|---|---|
| Critical | Cross-workspace cache leakage | Results from another tenant can be disclosed, violating the explicit current-workspace boundary. | Include workspace identity in cache partitioning and re-enforce authorization before returning cached results; clear existing unsafe cache entries. |
| High | Search context is discarded on return | Both query and selected type are explicit parts of the user journey. | Restore the stored prior search state in `returnToSearch` and test the complete open/return flow. |
| High | Project search is unproven | The requested global search must cover two result types, but only documents are demonstrated. | Implement or identify the combined project/document path and add project and mixed-result tests. |
| Medium | Cache freshness and growth are undefined | A permanent, unbounded process cache can serve stale results and consume memory over time. | Define product-appropriate invalidation/TTL and bounds, then test update and eviction behavior. |

## Before shipping

1. Partition cache entries by workspace and all inputs that affect results, including result type; retain authorization filtering on cache hits.
2. Add an automated two-workspace test that runs identical queries in both orders and proves neither workspace can receive the other's projects or documents.
3. Restore the saved query and selected result type on return, with an end-to-end open-result/return regression test.
4. Demonstrate project-only, document-only, and mixed searches in the active workspace.
5. Define and verify cache freshness, invalidation, and size limits, then rerun the supplied tests, focused isolation checks, and the demo with tenant-safe expected output.

## Open questions

- What freshness, invalidation, and maximum-size behavior is required for cached search results?
- Should result type be part of the search request and cache key, or is it only a presentation filter over a combined project/document result set?
