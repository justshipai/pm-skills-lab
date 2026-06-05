# Example: llm-eval-set-designer

## Input

> We shipped an AI feature that extracts structured expense data (merchant, date,
> amount, category, currency) from a photo of a receipt. We need an eval set to
> decide if a new model version is good enough to roll out. Design it.

## Output

# Receipt Extraction — Eval Set Spec

## Capability & definition of good
Given a receipt image, return structured fields. "Good" =
- **Correct:** each field matches the receipt.
- **Complete:** no required field dropped when present on the receipt.
- **Well-formed:** valid JSON; amount is a number; date is ISO-8601; currency is a valid ISO code.
- **Safe-failing:** when a field is illegible, return `null` + low confidence — never guess a value.

## Failure modes observed (from reviewing ~40 real outputs)
- Confuses subtotal vs. total (picks the wrong amount).
- Mis-reads currency on foreign receipts (assumes USD).
- Hallucinates a plausible date when the printed date is faded.
- Mis-categorizes ambiguous merchants (e.g. a hotel that's really "travel").
- Breaks on crumpled / rotated / multi-receipt photos.

## Case set
| Bucket | # cases | Source | Example |
|---|---|---|---|
| Happy path | 60 | Real, hand-labeled | Clear US restaurant receipt |
| Hard / edge | 50 | Real | Foreign currency, faded date, subtotal+total+tip, handwritten |
| Adversarial / abuse | 15 | Hand-written | Non-receipt image, screenshot of a receipt, two receipts in frame |
| Out-of-scope (should null/refuse) | 25 | Real | Illegible amount, missing date, blank/cropped fields |
| **Total** | **150** | | Stratified for coverage, not volume |

## Graders
| Dimension | Grader | Rubric / assertion |
|---|---|---|
| Format | Code assertion | JSON parses; amount is float; date matches ISO regex; currency in ISO-4217 set |
| Field correctness | Code assertion vs. labels | Exact match for amount/date/currency; normalized match for merchant |
| Category | LLM-as-judge | Rubric: "Is the category defensible given the merchant?" (allows >1 correct) |
| Safe-failing | Code assertion | Illegible fields are `null` with confidence < 0.5, never a fabricated value |

## Pass bars (per bucket)
- Happy path: ≥ 98% field-level exact match on amount + date + currency.
- Hard/edge: ≥ 90% field-level exact match; currency correct ≥ 95%.
- Adversarial: 100% handled (non-receipts rejected, multi-receipt flagged).
- Out-of-scope: **zero tolerance** — 0 fabricated values on illegible fields. A single hallucinated amount fails the release.

## Judge validation & cadence
Before trusting the category judge, label 50 cases by hand and confirm ≥ 90% judge-human agreement; re-check quarterly. **Cadence:** full set runs pre-release and on any model/prompt change; the zero-tolerance subset runs in CI on every change. Every production mis-extraction reported by a user is added as a new hard/edge case.
