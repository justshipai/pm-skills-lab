# Example: hallucination-risk-register

## Input

> Build a risk register for our new AI feature: an in-app assistant for our
> personal-finance app that answers questions about the user's own spending
> ("how much did I spend on groceries last month?") and can, on request,
> categorize or move transactions. Pre-launch review.

## Output

# Spending Assistant — Failure-Mode Risk Register

## Scope
- **Inputs:** user's natural-language question + their own transaction data (retrieved).
- **Outputs:** a spoken-style answer, sometimes with figures; can **take actions** (re-categorize / move transactions) on confirmation.
- **Audience & trust:** end consumers making money decisions — high trust, low ability to verify. Actions touch real financial records.

## Register
| # | Failure mode | Trigger | Sev | Likelihood | Detection | Mitigation | Residual risk | Owner |
|---|---|---|---|---|---|---|---|---|
| 1 | Fabricated figure | Sparse/ambiguous data; model "fills in" | 5 | 3 | Cross-check stated number against a deterministic query over the data | Compute all figures in code, not the model; model only narrates verified numbers | Rare narration mismatch | PM |
| 2 | Wrong action (miscategorize / move wrong txn) | Ambiguous reference ("move that one") | 5 | 3 | Confirmation diff before commit; post-action audit log | Require explicit confirm with the exact txn shown; everything reversible | User confirms a wrong diff | Eng |
| 3 | Omission (misses transactions in a total) | Retrieval misses a category/date edge | 4 | 3 | Reconcile assistant total vs. ledger total; flag mismatch | Deterministic aggregation; show "based on N transactions" | Edge date/timezone gaps | Eng |
| 4 | Data leakage (another user's data) | Retrieval scope bug | 5 | 1 | Per-request tenant assertion; red-team | Hard tenant isolation on retrieval; no cross-user index | Infra misconfig | Security |
| 5 | Prompt injection via memo text | Malicious text in a transaction memo | 4 | 2 | Treat retrieved memo text as data, not instructions; injection eval cases | Strip/escape memo content; model can't act without user confirm | Novel injection | Eng |
| 6 | Overconfidence (no uncertainty signal) | Genuinely ambiguous question | 3 | 4 | Confidence/threshold on retrieval coverage | Ask a clarifying question or show assumptions when coverage is low | User over-trusts | PM |
| 7 | Financial/tax advice (out of scope) | "Should I invest in…?" | 4 | 3 | Intent classifier flags advice requests | Refuse + disclaimer; route to help content | Edge phrasing slips through | PM |
| 8 | Silent degradation | Model/prompt update | 3 | 3 | Eval set runs on every change; live answer-accuracy monitor | Gate releases on eval; alert on drift | Slow drift between evals | Eng |

## Top risks & guards to build (sev × likelihood)
1. **#1 Fabricated figure (15)** and **#2 Wrong action (15)** — compute figures deterministically; confirm + reversible actions. These are launch-blocking.
2. **#3 Omission (12)** — reconcile against the ledger.
3. **#7 Out-of-scope advice (12)** — intent guard + refusal.

## Cannot currently detect
- Subtle over-confidence on ambiguous questions (#6) — we can threshold retrieval coverage but can't fully detect "should have asked a clarifying question." **Watchlist item; add eval cases.**

## Residual risk accepted by
Head of Product (overall), with Security signing off on #4 (data isolation) before GA.
