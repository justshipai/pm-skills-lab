# Example: ai-prd

## Input

> We're building "Ask Docs" — a natural-language Q&A assistant over our product
> documentation, embedded in our help center. Users type a question, get an answer
> with sources. B2B dev-tools company, docs are public. Write the PRD.

## Output

# Ask Docs — AI PRD

## 1. Problem, users & the bet
Developers can't find answers in our 1,200-page docs; 38% of support tickets are "it's in the docs" questions. **Users:** developers evaluating or using our API. **Bet:** an in-docs Q&A assistant deflects routine questions and speeds time-to-first-call, reducing ticket volume and improving activation.

## 2. Approach: buy vs. build
**Decision: RAG over a hosted API model — no fine-tuning.** Docs change weekly, so retrieval keeps answers current without retraining; a hosted model gets us to quality fastest. Revisit fine-tuning only if retrieval quality plateaus. Trade-off accepted: per-query API cost vs. the control/latency of self-hosting (within budget at §9).

## 3. Model card
- **Intended use:** answer questions about our product/API using our public docs, with citations.
- **Capabilities:** retrieve relevant doc passages; synthesize a concise answer; cite sources; say "I don't know / here's where to look" when docs don't cover it.
- **Limitations (explicit):** no access to a user's account state, code, or private data; can be wrong on ambiguous or newly-changed docs; English only at launch; not a substitute for the API reference for exact signatures.
- **Prohibited / out-of-scope:** generating code that makes live API calls; advising on pricing/contracts; answering off-topic (non-product) questions; promising SLAs or roadmap.
- **Inputs → outputs:** question (≤500 chars) + retrieved doc chunks → answer (≤200 words) + 1–3 source links.

## 4. Data strategy
- **Data required & sourcing:** our public docs (already ours), chunked + embedded; refreshed on every docs deploy.
- **Rights / privacy:** docs are our content — no third-party rights issue. User questions may contain PII or secrets; we **redact/avoid logging secrets**, store questions under existing privacy policy, no training on user input without opt-in.
- **Labeling & quality:** no labeling for v1 (retrieval, not supervised training); a 150-question golden set is hand-labeled for eval (§5).
- **Feedback data captured:** thumbs, "answer didn't help," and which sources were clicked — feeds eval growth and retrieval tuning.

## 5. Evaluation strategy
**Good enough to ship:** ≥85% of golden-set answers judged correct-and-grounded; **near-zero confidently-wrong answers** (fabricated facts/links). **Offline:** golden set graded by an LLM-as-judge rubric (correctness vs. source, grounding/citation validity, refusal-when-unknown) + human review of failures. **Online:** thumbs-up rate, click-through on citations, and ticket-deflection rate vs. baseline. Detail lives in a separate eval set (see `llm-eval-set-designer`).

## 6. UX & trust principles
Answers always show their **source links** (verifiable); a visible "AI-generated — check the docs" note; an obvious path to "still stuck? contact support"; the assistant **refuses gracefully** ("I couldn't find this in the docs — try X") rather than guessing.

## 7. Risks, safety & compliance
- Fabricated answer/link → grounding rubric + suppress when retrieval is weak (link `hallucination-risk-register`).
- Prompt injection via crafted questions → input constraints; no tool/account access to abuse.
- Regulatory: low tier (public docs, informational, human-checkable) — no high-risk EU AI Act exposure; legal sign-off on the disclaimer.

## 8. Rollout, milestones & RACI
Offline eval gate → internal dogfood → 10% canary on low-risk doc sections → GA, with kill switch to a plain docs-search fallback (see `staged-ai-rollout`). **R:** PM (me); **A:** Head of Product; **C:** Docs lead, Security, Support lead; **I:** Marketing.

## 9. Success & guardrail metrics
- **Primary:** docs-related ticket deflection (target −25%).
- **Quality:** thumbs-up rate ≥70%; confidently-wrong rate ≈0 (guardrail).
- **Cost/latency:** < $0.02/query; < 3s to first token (guardrails).
- **Adoption:** % docs sessions that use Ask Docs.

## 10. Open questions
- Retrieval quality on recently-changed pages — needs a freshness test pre-canary.
- Do we expose Ask Docs in-product (IDE/dashboard) as a fast-follow, or help-center only for v1?
- Threshold for "weak retrieval → refuse" — tune on the golden set.
