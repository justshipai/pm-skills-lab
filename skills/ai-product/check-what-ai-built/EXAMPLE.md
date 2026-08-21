# Example: check-what-ai-built

## Input

> I asked an AI coding tool to add CSV export to our customer table. Admins should be able to export the currently filtered results, ordinary members must not see the action and exports above 10,000 rows should be rejected with a useful message. Existing search and pagination must keep working.
>
> The PR changes the customer-table component, adds `GET /api/customers/export` and introduces a shared `exportToCsv` helper. The preview is available. CI is green with unit tests for CSV escaping and the 10,000-row limit. There are no browser tests. In the preview, an admin export downloads the expected filtered rows. A member account also sees the Export button and can download the file. The diff also changes the default table page size from 25 to 100.

## Output

# Feature acceptance report

## Verdict

**Not ready**

The critical permission rule fails in observed behaviour: an ordinary member can see and use the export action. The requested admin journey works and the row-limit logic has focused automated coverage, but the unauthorised access and unexplained pagination change make this unsafe to ship.

## Intended outcome

Admins can export the customer rows matching the table's current filters as CSV. Members cannot discover or invoke export. Exports over 10,000 rows fail with a useful message while existing search and pagination behaviour remain unchanged.

The member restriction, row limit and regression constraints are **Explicit**. I assume the CSV should contain all filtered rows rather than only the visible page because the request says "currently filtered results".

## What changed

The implementation adds an export action to the customer table, a server endpoint and a shared CSV helper. It also changes the table's default page size from 25 to 100, which is outside the stated scope.

## Intent-to-evidence ledger

| Contract item | Source | Status | Evidence | Gap or consequence |
|---|---|---|---|---|
| Admin can export filtered results | Explicit | Pass | Observed in preview: downloaded rows matched the active filters | No material gap found |
| Members cannot see or use export | Explicit | Fail | Observed in preview: member saw the button and downloaded a file | Permission boundary is broken |
| Reject exports above 10,000 rows with a useful message | Explicit | Unverified | Unit test covers rejection at the limit | No evidence that the user sees a useful message |
| Existing search continues to work | Explicit | Unverified | No browser test or reported preview check | Regression remains possible |
| Existing pagination remains unchanged | Explicit | Fail | Diff changes default page size from 25 to 100 | Observable behaviour changed without a product reason |
| CSV values are escaped safely | Assumption | Pass | Focused unit tests are green | User-level download was also observed for the admin path |

## Unexpected changes

- The default page size changes from 25 to 100. This is an orphan change with potential performance and usability impact.
- The export endpoint appears callable by members, so the problem is not merely a hidden-button defect.

## Risks worth acting on

| Priority | Risk | Why it matters | Required action |
|---|---|---|---|
| Critical | Missing server-side authorisation | Hiding the button alone would not prevent data export | Enforce admin permission at the endpoint and add a negative integration test |
| High | Pagination regression | Larger responses may slow the table and change an established workflow | Revert the page-size change or document and test the product decision |
| Medium | Error UX unproven | A correct API rejection can still leave the user with a silent failure | Exercise the over-limit path in the preview and verify the message |

## Before shipping

1. Enforce the admin permission in the export endpoint and prove a member receives a forbidden response.
2. Re-test both admin and member journeys in the preview.
3. Revert or explicitly approve the page-size change.
4. Observe the over-limit error and a representative search-and-pagination journey.

## Open questions

- Should an export include all filtered rows or only the current page? The answer changes both the query and the expected 10,000-row behaviour.
