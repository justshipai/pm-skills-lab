# Example: eval-rubric-designer

## Input

> We use an LLM-as-judge to score the answers from our "Ask Docs" assistant, but
> the scores are all over the place. Write a rubric the judge can apply
> consistently. An answer = the assistant's reply + the sources it cited.

## Output

# Ask Docs Answer — Scoring Rubric

## Quality goal & criteria
A good answer correctly and concisely answers the question using only our docs, cites real sources, and refuses when the docs don't cover it. Four criteria:
1. **Grounding** (gate) 2. **Correctness** 3. **Completeness** 4. **Conciseness/tone**

## Per-criterion rubric

**1. Grounding — pass/fail — GATE**
- **PASS:** every factual claim is supported by the cited source text; all cited links exist in the retrieved set.
- **FAIL:** any claim not supported by a cited source, or any fabricated/irrelevant citation.
- *Calibration:* PASS — "Rate limits are 100 req/min [link to /limits]" and the page says exactly that. FAIL — "Rate limits are 500 req/min" when the page says 100 (fabricated). BORDERLINE — correct fact but cites the wrong page → FAIL (citation must support the claim).

**2. Correctness — pass / partial / fail**
- **PASS:** directly and accurately answers the question asked.
- **PARTIAL:** accurate but answers a related, not the exact, question.
- **FAIL:** wrong, or answers a different question.
- *Calibration:* Q "How do I rotate an API key?" PASS = steps to rotate; PARTIAL = how to *create* a key; FAIL = "keys can't be changed."

**3. Completeness — pass / partial / fail**
- **PASS:** includes the steps/caveats needed to act; nothing critical missing.
- **PARTIAL:** mostly there, omits a non-critical detail.
- **FAIL:** omits a step that would block the user.

**4. Conciseness & tone — pass / fail**
- **PASS:** ≤ 200 words, no filler, neutral-helpful tone.
- **FAIL:** rambling, padded, or off-tone.

## Aggregate verdict
Item **passes** iff: Grounding = PASS (gate) **AND** Correctness = PASS **AND** Completeness ≠ FAIL **AND** Conciseness = PASS. Any grounding failure fails the item outright regardless of the rest.

## Judge validation
Hand-label 50 answers against this rubric; require **≥ 90% verdict agreement** between the LLM-judge and the human labels before trusting it. Re-validate on any judge-model or prompt change, and quarterly. If agreement drops below 90%, tighten the anchors (usually Correctness vs. Completeness confusion).

## Pairwise mode (optional)
For tuning prompts/models where absolute scores are close, run pairwise: "Given the question and sources, which answer is better — A or B — on grounding then correctness?" More reliable than scoring each in isolation for ranking two candidates.
