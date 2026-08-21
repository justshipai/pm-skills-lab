# Acceptance review: Transaction CSV export

**Ship decision: Ship.** I found no release-blocking defect in the reviewed commit.

## Evidence

- **Admin-only access:** `exportTransactions` checks `actor.role === 'admin'` before filtering or producing output and throws `forbidden` otherwise (`src/exportTransactions.js:11-12`). The committed member test passes; additional checks for member, viewer, empty, and missing roles also all rejected export.
- **Active filters are preserved:** export delegates matching to the existing `filterTransactions` function (`src/exportTransactions.js:14`). The feature commit does not modify `src/transactions.js`, so existing filtering behavior is unchanged. Tests pass for combined status and upper-date filtering, and an added check confirmed inclusive `from`/`to` boundaries with status filtering.
- **Required CSV shape:** the implementation fixes the column order to `id,date,status,description` and emits each matching row in that order (`src/exportTransactions.js:13-16`). A custom exact-output check passed.
- **CSV and spreadsheet safety:** every exported field goes through `csvCell`, which prefixes values beginning with optional spaces/control whitespace followed by `=`, `+`, `-`, or `@`, and applies standard CSV quoting with doubled embedded quotes (`src/exportTransactions.js:3-8`). Repository tests pass for commas, quotes, formula strings, tab-prefixed formulas, and carriage returns; additional probes passed for all four dangerous formula prefixes, leading space/tab/CR/LF variants, newlines, tabs, and quotes.
- **No matches:** joining the header with an empty row list produces exactly `id,date,status,description`; the explicit header-only test passes.
- **No data mutation:** filtering uses `Array.prototype.filter` and export maps results into new strings. A deep snapshot check confirmed the supplied transaction records were unchanged.
- **Verification:** `node --test` completed with **6/6 passing**, `git diff --check` passed, and targeted boundary/security checks passed.

## Residual risk

This repository exposes the export as a function rather than an end-to-end UI or download route, so browser download behavior, response headers, and wiring to the visible active filters are outside the available implementation surface. Within the commit’s code scope, the requested authorization, filtering, output columns, escaping, empty result, and non-mutation behavior are implemented and verified.
