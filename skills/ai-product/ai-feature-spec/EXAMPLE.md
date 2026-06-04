# Example: ai-feature-spec

## Input

> We want to add AI-drafted replies to our customer support inbox. When an agent
> opens a ticket, we suggest a reply they can send or edit. B2B SaaS, ~40 support
> agents, ~3,000 tickets/week. Goal is faster responses. Can you spec it?

## Output

# AI-Drafted Support Replies — AI Feature Spec

## 1. Problem & job-to-be-done
Support agents spend most of their handle time *writing*, not deciding. For routine tickets the answer is knowable from past tickets and help docs. **Job:** when an agent opens a ticket, help them send an accurate reply in seconds, not minutes.

## 2. Why AI (and the non-AI baseline)
Canned-response macros (the non-AI baseline) already exist but cover <30% of tickets and require the agent to pick the right one. The long tail is too varied for templates — a generation model can adapt tone and pull specifics. **We keep macros as the fallback** (see §6). Recommend building only if the draft is accepted/lightly-edited on ≥50% of eligible tickets in the canary (§10).

## 3. The AI capability
- **Inputs:** ticket thread, customer plan/metadata, top-k retrieved help-doc and past-resolved-ticket chunks.
- **Outputs:** one suggested reply (≤180 words) + the source chunks it used.
- **Model & approach:** retrieval-augmented generation; mid-tier model (e.g. Sonnet-class) — quality close to frontier at materially lower cost/latency (§9). Re-evaluate model quarterly via the eval set.
- **In scope:** drafting replies for English tickets tagged "how-to" / "account" / "billing".
- **Out of scope:** auto-sending; refunds/legal/security tickets (routed, never drafted); non-English (v2).

## 4. Quality bar & evaluation plan
- **Good enough to ship:** ≥85% of drafts rated "send as-is or minor edit" by agents on the golden set; **0 tolerance** for confidently-wrong factual claims (e.g. inventing a refund policy).
- **Offline:** golden set of 200 representative resolved tickets; LLM-as-judge rubric (factual accuracy vs. source, policy compliance, tone, completeness) + human spot-check of the bottom quartile.
- **Online:** draft acceptance rate, edit distance before send, agent thumbs, and post-send CSAT vs. control.

## 5. Failure modes & guardrails
| Failure | Likelihood | Detection | Mitigation |
|---|---|---|---|
| Hallucinated policy/fact | Med | Claim not grounded in retrieved sources | Constrain to retrieved context; show citations; suppress draft if retrieval is empty (→ §6) |
| Confidently wrong on edge ticket | Med | Low retrieval score / out-of-scope tag | Don't draft; fall back to macros |
| Wrong tone (curt/over-promising) | Med | Rubric flags in eval; agent thumbs live | Tone guidance in prompt; agent always edits before send |
| Leaks another customer's data | Low | Retrieval scoped to this customer + public docs only | Hard filter on retrieval namespace; red-team before GA |
| Slow draft | Med | Latency monitor | Stream tokens; 6s budget then show macros |

## 6. Fallback behaviour
If retrieval is weak, the ticket is out-of-scope, or generation fails/times out, the agent sees the **existing macro picker** with no AI draft and no error noise — never a blank box or a dead end. Drafting is additive; the agent's normal workflow always remains.

## 7. UX for uncertainty & reversibility
Draft is clearly labelled "AI suggestion," pre-fills the reply box in an **editable** state (never auto-sends), and shows the **source links** it drew from. Agent edits and sends as normal — human-in-the-loop by construction. A one-click "not helpful" logs the case.

## 8. Data & feedback loop
Log ticket → draft → final-sent pairs and the thumbs/edit signal to grow the golden set and prompt-tune. Customer content stays in-tenant; covered by existing DPA; no training on customer data without contractual opt-in. PII handling reviewed with security before canary.

## 9. Cost, latency & scale
~3k tickets/wk × eligible share. Target **< $0.04 / draft** and **< 6s** to first useful token (stream). Mid-tier model keeps unit cost below the loaded cost of the agent minutes saved — the unit economics that justify the feature. Per-tenant rate limits; degrade to macros under load.

## 10. Rollout plan
1. **Shadow:** generate drafts invisibly on live tickets; score against agents' actual sent replies.
2. **Canary:** 5 volunteer agents; gate to GA on acceptance ≥50% and zero confidently-wrong factual incidents.
3. **GA:** staged by ticket tag. **Kill switch** disables drafting and reverts to macros instantly.

## 11. Success & guardrail metrics
- **Primary:** median first-response time on eligible tickets (target −30%).
- **Quality:** draft acceptance rate, CSAT (must not drop vs. control — guardrail).
- **Cost/latency:** $/draft and p90 time-to-draft within budget (guardrail).
- **Adoption:** % eligible tickets where a draft is used.

## 12. Risks & open questions
- Will agents over-trust drafts and skip verifying facts? (Mitigation: citations + accuracy in onboarding.)
- Retrieval quality on sparse/new docs — needs a content audit before canary.
- Where exactly is the line between "draftable" and "route to human"? Needs the support lead's sign-off.
