# Eval results — `check-what-ai-built`

- **Run:** 2026-08-21 15:13 UTC
- **Model under test:** Codex session default
- **Judging:** two independent blinded Codex judges
- **Verdict:** ✅ **VERIFIED** — the skill passed all eight scenarios and improved the average rubric score over the no-skill baseline.

## Summary

| Measure | Baseline | With skill | Lift |
|---|---:|---:|---:|
| Average rubric score | 0.9344 | 1 | +0.0656 |
| Scenarios passing the rubric | 8/8 | 8/8 | — |
| Correct ship verdict | 8/8 | 8/8 | — |

The baseline was already strong and made the correct ship decision in every scenario. The skill's measurable value was **completeness and decision traceability**: explicit intent contracts, complete Pass/Fail/Unverified ledgers, sharper handling of missing evidence and better separation of assumptions from requirements.

## Scenario results

| Scenario | Expected verdict | Baseline | With skill | Lift |
|---|---|---:|---:|---:|
| scenario-1: Bulk archive: permission and migration defects | Not ready | 0.9118 | 1 | +0.0882 |
| scenario-2: Notification preferences: complete safe implementation | Ready to ship | 1 | 1 | +0 |
| scenario-3: CSV export: bounded analytics condition | Ready with conditions | 0.9667 | 1 | +0.0333 |
| scenario-4: Bulk invitations: inaccessible evidence | Cannot verify | 0.8333 | 1 | +0.1667 |
| scenario-5: Global search: tenant data leak | Not ready | 0.9465 | 1 | +0.0535 |
| scenario-6: Pricing copy: billing and entitlement drift | Not ready | 0.9 | 1 | +0.1 |
| scenario-7: Revenue sharing: ambiguous high-risk intent | Not ready | 0.9166 | 1 | +0.0834 |
| scenario-8: Date picker: large but evidenced safe change | Ready to ship | 1 | 1 | +0 |

A zero-lift scenario is a ceiling effect, not a failure: the baseline and treatment both fully satisfied that scenario's rubric. Verification is based on the treatment passing every scenario and improving the aggregate score across the suite.

## Where the lift came from

- A complete evidence ledger rather than accurate but loosely structured findings
- The precise **Cannot verify** verdict when only agent claims were available
- More complete intent contracts covering invariants and consequential assumptions
- Explicit conditions, owners and rollout boundaries for a conditional ship decision
- No over-blocking: the skill correctly approved both a small safe feature and a 914-line migration with strong evidence

## Method

The eight scenarios and rubrics were written before candidate generation. For each scenario, two fresh isolated agents received the same task: a baseline with no skill and a treatment explicitly supplied `SKILL.md`. Candidate outputs were relabelled A/B with alternating assignment. Two additional fresh judges independently scored the blinded outputs against the pre-authored weighted rubric using Pass = 1, Partial = 0.5 and Fail = 0. The table reports the mean of both judges.

### Limitations

This run tests one model family on synthetic but realistic scenarios. Both judges were also from the Codex model family. The next useful extension is cross-model replication with Claude and Gemini, not more near-duplicate scenarios.

### scenario-1 — with-skill verdicts

| Criterion | Verdict | Why |
|---|---|---|
| `decisive-verdict` | ✅ pass | Leads Not ready and directly cites the active-project failure and mass-archiving migration. |
| `intent-contract` | ✅ pass | Enumerates admin, member, eligibility, confirmation, retention, and restore outcomes. |
| `evidence-ledger` | ✅ pass | Explicit ledger assigns Pass, Fail, or Unverified with the supplied evidence for every material item. |
| `permission-uncertainty` | ✅ pass | Clearly says hidden UI is not server-side authorization and marks endpoint enforcement unverified. |
| `migration-blast-radius` | ✅ pass | Explains that the non-null default would archive all existing projects and notes the absent rollback. |
| `minimal-next-actions` | ✅ pass | Provides an ordered blocker-focused list covering migration, eligibility, permissions, restore, and cancellation. |
| `pm-readable` | ✅ pass | States customer and operational consequences plainly and decision-first. |

### scenario-2 — with-skill verdicts

| Criterion | Verdict | Why |
|---|---|---|
| `correct-verdict` | ✅ pass | Leads Ready to ship and accurately states that all critical behaviors have direct evidence. |
| `intent-contract` | ✅ pass | Fully states optional controls, immutable transactional messages, persistence, and current-user isolation. |
| `evidence-ledger` | ✅ pass | The ledger assigns Pass with relevant direct evidence to each material requirement. |
| `no-invented-blockers` | ✅ pass | Treats the nullable-default question as non-blocking rather than manufacturing a release gate. |
| `risk-proportionality` | ✅ pass | Correctly treats residual default-semantics risk as low and bounded. |
| `pm-readable` | ✅ pass | Decision and product consequences are clearly summarized. |

### scenario-3 — with-skill verdicts

| Criterion | Verdict | Why |
|---|---|---|
| `correct-verdict` | ✅ pass | Leads Ready with conditions for the pilot and keeps analytics as the GA gate. |
| `scope-aware-contract` | ✅ pass | Covers filters, authorization, empty/escaping behavior, analytics, and flag boundary. |
| `evidence-ledger` | ✅ pass | Explicitly marks export and authorization Pass and analytics Fail with strong evidence. |
| `proportionality` | ✅ pass | Allows the bounded internal pilot without presenting the feature as GA-ready. |
| `condition-owner` | ✅ pass | Names export_started, the feature owner, and the before-GA boundary. |
| `pm-readable` | ✅ pass | Decision-oriented and concise despite a structured report format. |

### scenario-4 — with-skill verdicts

| Criterion | Verdict | Why |
|---|---|---|
| `correct-verdict` | ✅ pass | Leads Cannot verify and grounds it in inaccessible artifacts. |
| `intent-contract` | ✅ pass | Fully extracts the admin journey, boundary, validation review, authorization, and suppression rules. |
| `claim-scepticism` | ✅ pass | Explicitly calls completion statements and summaries claims rather than evidence. |
| `unverified-ledger` | ✅ pass | Marks every material behavior Unverified with the precise missing evidence. |
| `minimal-evidence-request` | ✅ pass | Asks for accessible diff, focused test output, runnable preview, and prioritizes permissions and duplicates. |
| `no-speculation` | ✅ pass | Separates possible consequences from established facts and avoids alleging defects. |

### scenario-5 — with-skill verdicts

| Criterion | Verdict | Why |
|---|---|---|
| `correct-verdict` | ✅ pass | Leads Not ready and prioritizes the tenant leak while also citing lost state. |
| `intent-contract` | ✅ pass | Covers project/document scope, current-workspace isolation, and query/filter restoration. |
| `direct-evidence` | ✅ pass | Treats both preview failures as decisive despite green CI and happy-path coverage. |
| `root-risk` | ✅ pass | Connects the query-only cache key to a credible tenant-boundary risk without asserting certainty. |
| `minimal-actions` | ✅ pass | Requires tenant-aware caching and authorization, state restoration, and focused regressions. |
| `pm-readable` | ✅ pass | Clearly explains disclosure and user-experience consequences. |

### scenario-6 — with-skill verdicts

| Criterion | Verdict | Why |
|---|---|---|
| `correct-verdict` | ✅ pass | Leads Not ready and directly cites both invariant violations and absent behavioral evidence. |
| `intent-contract` | ✅ pass | Captures both copy changes and the full plans, prices, discounts, and entitlements invariant. |
| `orphan-changes` | ✅ pass | Labels the discount and SSO mapping as undisclosed, high-blast-radius scope drift. |
| `evidence-ledger` | ✅ pass | Explicit ledger marks copy Pass, discount and entitlement Fail, and affected flows Unverified. |
| `minimal-actions` | ✅ pass | Orders reversion, diff confirmation, and focused billing/entitlement regression checks. |
| `pm-readable` | ✅ pass | Commercial and customer-access consequences are plainly stated. |

### scenario-7 — with-skill verdicts

| Criterion | Verdict | Why |
|---|---|---|
| `correct-verdict` | ✅ pass | Leads Not ready because public access and disclosure choices were never authorized. |
| `assumption-discipline` | ✅ pass | Separates the explicit Share button from undefined audience, auth, fields, expiry, and revocation decisions. |
| `risk-recognition` | ✅ pass | Clearly explains the permanent public exposure and why noindex is not access control. |
| `evidence-ledger` | ✅ pass | Distinguishes observed rendering and exposure from undefined policy and unverified security properties. |
| `decision-changing-question` | ✅ pass | Asks for decisions on audience, data fields, authentication model, expiry, and revocation. |
| `minimal-actions` | ✅ pass | Withholds shipping until access policy is settled, implemented, and tested. |

### scenario-8 — with-skill verdicts

| Criterion | Verdict | Why |
|---|---|---|
| `correct-verdict` | ✅ pass | Leads Ready to ship and emphasizes complete direct behavioral evidence. |
| `intent-contract` | ✅ pass | States every requested preserved behavior, including unchanged UTC storage. |
| `evidence-ledger` | ✅ pass | A complete ledger maps every invariant to its strongest supplied evidence. |
| `diff-size-discipline` | ✅ pass | Treats the large explained generated footprint proportionally and finds no scope drift. |
| `regression-scope` | ✅ pass | Recognizes adjacent booking tests, dependency removal, and no high-risk unrelated changes. |
| `no-generic-checklist` | ✅ pass | Recommends only normal release flow and invents no extra acceptance work. |

