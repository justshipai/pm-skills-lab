# Example: human-in-the-loop-design

## Input

> Our AP (accounts payable) tool is adding AI that reads incoming invoices and
> books them: extracts vendor/amount/GL code, matches to a PO, and queues
> payment. Design where humans stay in the loop.

## Output

# AI Invoice Booking — Human-in-the-Loop Design

## Action → oversight map
| Action | Risk | Reversible? | Oversight | Why |
|---|---|---|---|---|
| Extract fields (vendor, amount, date) | Low | Yes | **Review-after (on loop)** | Wrong field is caught at approval; show extracted vs. document |
| Assign GL code | Med | Yes | **Confirm if low confidence; auto if high + known vendor** | Mis-coding distorts books but is correctable |
| Match to PO | Med | Yes | **Auto if exact match; confirm if fuzzy/none** | Exact match is safe; ambiguity needs a human |
| Queue payment | **High** | **No (money leaves)** | **Defer-to-human approval, always** | Irreversible spend — never automatic |
| Pay invoice with no PO | High | No | **Defer + extra approver** | Highest fraud/error risk |

## Confidence routing
- **Extraction confidence ≥ 0.95 and known vendor:** fields + GL prefilled, queued for one-click approval.
- **< 0.95, new vendor, or amount over $X:** flagged for field-by-field review before it can be approved.
- **PO match score < threshold:** present top candidates; human picks or marks "no PO."

## Review surface
A single approval card: the invoice image **side-by-side** with extracted fields, each field showing confidence (low ones highlighted), the matched PO (or "no match"), and the proposed GL code. Approver can **edit any field inline, approve, or reject with reason** in seconds — no hunting through the PDF.

## Undo & escalation
- **Undo:** before payment, everything is editable/reversible; an approved-but-not-yet-paid invoice can be recalled.
- **Escalation:** missing PO, amount over the approver's limit, or a duplicate-invoice signal routes to a senior approver with the duplicate/PO context attached — the AI never books around it.

## Trust ramp
Start with **confirm** on GL coding for all vendors. After 4 weeks, auto-code vendors where the AI's GL matches the human's choice ≥ 98% of the time (per the eval + live data); keep confirm for the rest. **Guardrail:** if live coding accuracy for an auto'd vendor drops below 95%, revert it to confirm. Payment approval **never** ramps to auto.
