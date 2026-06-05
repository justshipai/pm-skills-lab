# Example: working-backwards

## Input

> We want to add a feature that lets our accounting-software users get their books
> "audit-ready" with one click. Write a working-backwards PR/FAQ.

## Output

# One-Click Audit-Ready — Working Backwards (PR/FAQ)

## PRESS RELEASE (launch day)

### Small businesses can now get audit-ready in one click — not three stressful weeks
*New in [Product]: instantly assemble every document an accountant or auditor asks for.*

Tax season and audits turn small-business owners into part-time clerks — hunting for receipts, reconciling statements, and assembling folders auditors request. Today [Product] launches **Audit-Ready**: one click assembles a complete, organized package of statements, reconciliations, and supporting documents, flags anything missing, and hands it to your accountant in the format they expect.

It works by continuously organizing the records you already keep in [Product], so the package is ready the moment you need it — no scramble.

"Last year my audit prep took three weekends and a lot of antacids," said [Customer], owner of a 6-person bakery. "This year I clicked one button and emailed my accountant the whole thing in five minutes."

Audit-Ready is available today for all [Product] Business plan users — find it under Reports.

## Customer FAQ
- **What does it actually produce?** A downloadable/shareable package: P&L, balance sheet, bank reconciliations, and categorized supporting docs, with a checklist of anything missing.
- **What if my records are incomplete?** It flags gaps and tells you exactly what to add — it won't fake data.
- **Does my accountant have to use your tool?** No — the package exports in standard formats they already accept.
- **What does it cost?** Included in the Business plan.

## Internal FAQ
- **Why will customers care?** Audit/tax prep is a concentrated, dreaded, recurring pain with a hard deadline — high willingness to pay attention.
- **Why us?** The records already live in our product; we're uniquely positioned to assemble them. A standalone tool would have to import everything first.
- **Biggest risks?** (1) Accuracy/completeness — a package that misses something erodes trust fast (see `hallucination-risk-register`). (2) Accountants' formats vary by region.
- **What we're NOT doing:** we're not replacing the accountant, not filing taxes, not auditing — we're assembling.
- **Business model:** retention + Business-plan upsell driver; not separately metered in v1.
- **What must be true:** our categorization is accurate enough that the package needs minimal cleanup.

## Verdict
**Compelling and specific — worth pursuing.** The headline benefit is concrete and the "why us" is strong (we already hold the data). The make-or-break is accuracy; validate that before building the polished one-click flow — a concierge test assembling 20 real packages by hand would de-risk it cheaply.
