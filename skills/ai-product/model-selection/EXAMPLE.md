# Example: model-selection

## Input

> We're choosing a model for our AI feature that auto-tags incoming support
> tickets with a category and priority (12 categories, 3 priorities). ~80,000
> tickets/month. We have a labeled eval set. Which model should we use?

## Output

# Ticket Auto-Tagging — Model Selection

## Constraints & quality bar
- **Hard constraints:** data stays in our cloud region (EU); no PII sent to a provider without a DPA; short prompt, small output (classification, not generation).
- **Minimum quality:** ≥ 92% category accuracy and ≥ 90% priority accuracy on our eval set (current human-agent agreement is ~93%).
- **Latency budget:** async (not user-facing) — p95 < 5s is fine.
- **Cost ceiling:** < $400/month at current volume.
- **Volume:** ~80k/month (~2,700/day), spiky.

## Candidates
- **Frontier model** — sanity-check ceiling on accuracy.
- **Mid-tier model** — expected sweet spot for classification.
- **Small/cheap model** — can a tiny model clear the bar?
- **Open model (self-hosted)** — keeps data fully in-region; higher ops cost.

## Decision matrix
| Model | Category acc | Priority acc | $/req | p95 latency | Constraint fit | Lock-in |
|---|---|---|---|---|---|---|
| Frontier | 96% | 93% | ~$0.006 | 2s | DPA ok | High |
| **Mid-tier** | **94%** | **91%** | **~$0.0015** | 1.5s | DPA ok | Med |
| Small/cheap | 88% | 86% | ~$0.0004 | 1s | DPA ok | Med |
| Open (self-host) | 93% | 90% | ~$0.001* | 3s | Best (in-region) | Low |

\*open-model $/req is amortized GPU + ops, not API price.

## Cost projection
- Mid-tier @ 80k/mo ≈ **$120/mo** (well under ceiling). At 10× volume (800k) ≈ $1,200/mo — still reasonable; renegotiate or add caching then.
- Frontier ≈ $480/mo — over ceiling now, and the extra 2pts accuracy isn't needed.
- Small/cheap is tempting at ~$32/mo but **misses the bar** (88% < 92%).

## Recommendation
**Mid-tier model.** It's the cheapest option that clears the quality bar (94% / 91%), fits latency and cost with large headroom, and meets the DPA constraint. The frontier model's extra accuracy is real but unused against our bar and 4× the cost.

## Sensitivity / what would change this
- If accuracy bar rose to 96% → frontier becomes necessary; re-budget.
- If volume 10×'d and cost mattered → add a cascade: small/cheap model handles high-confidence cases, mid-tier handles the rest.
- If legal disallowed any external provider → switch to the open self-hosted model (clears the bar at 93/90, fully in-region) and accept the ops cost.

## Re-evaluation trigger
Re-run this against the eval set on any new model release in this tier, a >20% price change, or if live accuracy drifts below 92%.
