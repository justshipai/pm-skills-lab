# Example: assumption-mapping

## Input

> We want to add a feature that lets our e-commerce sellers auto-generate product
> descriptions with AI. Map the assumptions before we build it.

## Output

# AI Product Descriptions — Assumption Map

## The idea & outcome
Let sellers auto-generate product descriptions from a few inputs. **Outcome:** more listings completed (and published) per seller, lifting catalog size and conversions.

## Assumptions by risk

**Value**
- We assume sellers *want* help writing descriptions (vs. it being a non-problem). (impact: **H** · evidence: **L**) ← leap-of-faith
- We assume weak descriptions are actually costing them sales they care about. (impact: H · evidence: L) ← leap-of-faith

**Usability**
- We assume sellers can give enough input (a few words/specs) to get a usable draft. (impact: M · evidence: L)
- We assume they'll trust and lightly edit the draft rather than abandon it. (impact: M · evidence: L)

**Feasibility**
- We assume current models produce on-brand, accurate descriptions without inventing specs. (impact: H · evidence: M)
- We assume we can do it within an acceptable per-listing cost. (impact: M · evidence: M)

**Viability**
- We assume generated descriptions won't create returns/complaints from inaccurate claims (legal/support risk). (impact: **H** · evidence: **L**) ← leap-of-faith
- We assume this fits our monetization (free perk vs. paid add-on). (impact: M · evidence: M)

## Leap-of-faith assumptions (high impact × low evidence — test first)
| Assumption | Risk | Cheapest test | What would change our mind |
|---|---|---|---|
| Sellers want description help | Value | Interview 8 sellers about the last listing they wrote; fake-door "Generate description" button, measure click-rate | <10% click / sellers say writing isn't their pain |
| Weak descriptions cost real sales | Value | Analyze conversion vs. description quality on existing listings | No correlation |
| Inaccurate AI claims won't spike returns/complaints | Viability | Concierge test: hand-generate 50 descriptions, ship, watch returns/complaint rate | Return/complaint rate rises vs. control |

## Test sequence
1. **Seller-wants-it interviews + fake-door** (a day; kills or confirms the whole idea cheaply).
2. If positive → **concierge accuracy/returns test** (the scary Viability risk) before any build.
3. Only then invest in the real generation feature. Feasibility is medium-evidence and least likely to be the thing that kills this — don't start there.
