# Review an AI-built feature

A product manager asked an AI coding agent to improve global search.

The request was:

> Search across projects and documents in the current workspace. Preserve the query and filters when someone opens a result and returns. Never show results from another workspace.

Available implementation evidence:

- CI is green. Unit tests cover ranking and an end-to-end test checks that clicking a result opens the correct document.
- In the preview, searching for `renewal`, applying the Documents filter, opening a result and pressing Back clears both the query and filter.
- In the same preview, a result titled `Acme renewal forecast` appears. The signed-in user belongs only to the Beacon workspace; inspection shows the result belongs to the Acme workspace.
- The pull request adds a shared server-side search cache keyed only by query text. It does not include workspace ID in the cache key.
- No test covers browser-back state or tenant isolation.

Produce a concise, evidence-backed acceptance review for the product manager and make a clear ship decision.
