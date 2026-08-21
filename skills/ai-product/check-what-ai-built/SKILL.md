---
name: check-what-ai-built
description: Evaluate whether a feature produced by an AI coding tool matches the product intent and is safe to ship. Use when reviewing a generated implementation, pull request, code diff or preview, especially when a PM or non-technical stakeholder needs an evidence-backed acceptance report rather than a line-by-line code review.
---

# Check what AI built

Treat generated code as an untrusted implementation of product intent. Do not ask a PM to judge code volume or architectural elegance. Determine whether the observable behaviour matches the intended outcome, whether important existing behaviour changed and what remains unproven.

Use the **Intent-to-Evidence Review**:

1. Convert intent into a testable contract.
2. Map the implementation footprint to that contract.
3. Gather evidence for each claim.
4. Expose failures, scope drift and uncertainty.
5. Make a ship decision with explicit conditions.

## Establish the review boundary

Collect what is available:

- the original request, ticket or prompt
- acceptance criteria, designs and product rules
- the code diff or pull request
- a runnable preview or local application
- tests, logs and check results

Do not mistake missing evidence for a pass. If the implementation or preview cannot be inspected, continue with a provisional review and mark affected claims **Unverified**. Ask a clarifying question only when the answer could change the ship decision. Otherwise state the assumption.

## Build the feature contract

Translate the request into observable claims before judging the implementation:

- **Outcome:** what the user must be able to accomplish
- **Actors and permissions:** who can and cannot do it
- **States:** happy path, loading, empty, error and meaningful boundaries
- **Invariants:** behaviour, data, permissions, billing and integrations that must not change
- **Non-goals:** what this change should not attempt
- **Operational needs:** analytics, accessibility, observability and rollback where material

Do not silently invent requirements. Label each item **Explicit**, **Existing rule** or **Assumption**. A short prompt is not a complete specification; surface the consequential gaps.

## Map the change footprint

Inspect the diff and summarise changed product surfaces in plain language. Map every material change to a contract item.

Flag:

- **Uncovered requirements:** intended behaviour with no implementation or evidence
- **Orphan changes:** implementation changes with no stated product reason
- **High-blast-radius changes:** authentication, permissions, data migrations, billing, shared components, dependencies, infrastructure and destructive actions

Do not narrate files line by line. Mention technical detail only when it changes the product or ship decision.

## Gather evidence

Prefer direct evidence in this order:

1. observed behaviour in a preview or running application
2. focused automated tests and their output
3. code-path inspection
4. author or agent claims

Use available browser, repository and shell tools to inspect or run the feature. Test the highest-risk claims first. For each contract item, record:

- expected behaviour
- actual behaviour
- evidence source
- status: **Pass**, **Fail** or **Unverified**

Passing tests prove only what those tests assert. A plausible implementation is not proof that a user journey works. Never manufacture screenshots, test results or confidence.

## Check for regression and operability risk

Review adjacent risks proportional to the change:

- access control and tenant boundaries
- data integrity, migrations and reversibility
- changed billing, limits or entitlements
- search, notifications, analytics and integrations
- responsive, loading, empty, error and accessibility states
- monitoring, failure visibility and rollback

For migrations and data-state changes, cross-check the schema against every application write path. Compare nullability, defaults and backfills with create, update, archive, delete and restore behaviour. A helper-level test does not prove database compatibility if it never executes the real constraint or migration. When feasible, run the migration against representative existing data and exercise the reverse or restore path.

Prioritise plausible material failures. Avoid dumping a generic QA checklist.

## Make the decision

Use one verdict:

- **Ready to ship:** all critical contract items have direct evidence and no material unresolved risk exists
- **Ready with conditions:** only bounded, low-risk gaps remain, with a named condition and owner
- **Not ready:** a critical item failed, scope drift creates material risk or a required behaviour is unverified
- **Cannot verify:** the artefacts needed for a meaningful review are inaccessible

Never use a numeric confidence score to disguise missing evidence. When evidence is incomplete, say exactly what would change the verdict.

## Output format

Lead with the verdict and its reason.

```markdown
# Feature acceptance report

## Verdict
<Ready to ship | Ready with conditions | Not ready | Cannot verify>
<One-paragraph rationale>

## Intended outcome
<Plain-language restatement plus consequential assumptions>

## What changed
<Short product-level summary, including unexpected scope>

## Intent-to-evidence ledger
| Contract item | Source | Status | Evidence | Gap or consequence |
|---|---|---|---|---|

## Unexpected changes
<Only orphan or high-blast-radius changes; say "None found" when appropriate>

## Risks worth acting on
| Priority | Risk | Why it matters | Required action |
|---|---|---|---|

## Before shipping
<Smallest ordered set of actions that could change the verdict>

## Open questions
<Only questions whose answers affect acceptance or risk>
```

Write for a product manager. Be decisive, distinguish fact from inference and preserve an audit trail from the original request to the evidence.
