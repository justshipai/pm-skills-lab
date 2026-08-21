# End-to-end artifact eval — `check-what-ai-built`

- **Run:** 2026-08-21 16:28 UTC
- **Model under test:** Codex session default
- **Judging:** two independent blinded Codex judges
- **Verdict:** ✅ **VERIFIED** — the revised skill passed all four executable fixtures and improved aggregate rubric coverage.

## Results

| Measure | Baseline | With skill | Lift |
|---|---:|---:|---:|
| Average rubric score | 0.9822 | 1.0000 | +0.0178 |
| Scenarios passing | 4/4 | 4/4 | — |
| Correct ship verdicts | 4/4 | 4/4 | — |

| Scenario | Correct verdict | Baseline | With skill |
|---|---|---:|---:|
| scenario-1: Bulk archive permission and eligibility defects | Not ready | 1 | 1 |
| scenario-2: Destructive migration and restore-schema conflict | Not ready | 0.9286 | 1 |
| scenario-3: Cross-workspace search cache leak and lost state | Not ready | 1 | 1 |
| scenario-4: Safe filtered CSV export | Ready to ship | 1 | 1 |

The baseline was exceptionally strong and found every critical defect. The skill's measured advantage was consistency and rubric completeness, not unique bug discovery.

## What the eval changed

The first treatment run exposed a genuine skill defect: it identified the destructive migration but failed to connect `restoreProject()` writing `null` with the new database column being `NOT NULL`. The skill was updated to require schema constraints, defaults and backfills to be cross-checked against application create, update, archive and restore paths. All four treatment scenarios were then rerun against that revised skill.

This is the behaviour the library's eval philosophy is meant to produce: the eval did not merely validate the skill; it found a weakness and changed it.

## Method

Each candidate received only the fixture repository and its original product brief. It had to inspect the actual feature commit, read the implementation and run useful checks. No pre-digested evidence summary was supplied. Baseline candidates used no skill; treatment candidates used the revised `SKILL.md`. Outputs were alternately relabelled A/B and scored by two independent judges against rubrics written before candidate generation.

The checked-in `fixture/` directory is the reviewed implementation and `feature.patch` records the exact feature commit. Run the visible suite with `node --test` from the fixture directory.

## Limitations

- One model family was tested.
- These are four controlled synthetic fixtures, not production pull requests.
- Candidate and judge threads were reused after unrelated tasks because the environment thread limit had been reached; they did not have access to the hidden rubrics or fixture-specific prior outputs.
- The candidate and judges came from the same model family.

### scenario-1 — revised-skill verdicts

| Criterion | Verdict | Why |
|---|---|---|
| `correct-verdict` | ✅ pass | Leads Not ready because executable checks show both member bypass and active-project bulk archiving. |
| `permission-defect` | ✅ pass | Finds that bulkArchiveProjects ignores actor and distinguishes UI hiding from operation-level authorization. |
| `active-project-defect` | ✅ pass | Correctly identifies invoice-only bulk validation and reproduces archiving an active project. |
| `working-behaviour` | ✅ pass | Credits cancellation, invoice rejection, field preservation, and current single-project guard evidence while noting the absent baseline. |
| `direct-evidence` | ✅ pass | Uses the actual commit, code paths, four passing tests, and focused runtime probes. |
| `no-false-positive` | ✅ pass | Does not invent migration, deletion, or unrelated defects absent from the fixture. |
| `minimal-actions` | ✅ pass | Requires bulk role and active-state enforcement plus member, active, mixed-selection, and cancellation regressions. |

### scenario-2 — revised-skill verdicts

| Criterion | Verdict | Why |
|---|---|---|
| `correct-verdict` | ✅ pass | Leads Not ready because existing rows are endangered and the NOT NULL schema conflicts with restoration. |
| `existing-data-defect` | ✅ pass | Uses the exact DDL and a populated SQLite run to explain deployment failure or implicit archive timestamps. |
| `restore-schema-conflict` | ✅ pass | Explicitly marks restore as failing because the helper clears the timestamp while the schema forbids null. |
| `test-gap` | ✅ pass | Clearly explains that green object tests omit SQL migration, persistence, existing rows, and restored writes. |
| `direct-evidence` | ✅ pass | Grounds findings in the migration, helper code, unit-test boundary, SQLite execution, and focused probes. |
| `no-false-positive` | ✅ pass | Does not claim deletion and carefully labels authorization semantics while reporting the actual absent boundary. |
| `minimal-actions` | ✅ pass | Requires a nullable non-backfilling migration, real database archive/restore tests, and safe reverse or recovery testing. |

### scenario-3 — revised-skill verdicts

| Criterion | Verdict | Why |
|---|---|---|
| `correct-verdict` | ✅ pass | Leads Not ready for the reproduced cross-workspace cache leak and discarded query and type state. |
| `tenant-cache-defect` | ✅ pass | Finds the normalized-query-only shared key and explains why workspace filtering occurs only on a miss. |
| `reproduces-leak` | ✅ pass | Runs the committed demo and focused reverse-order checks demonstrating cross-workspace results. |
| `navigation-defect` | ✅ pass | Shows returnToSearch ignores the stored previous state and resets query and type. |
| `test-gap` | ✅ pass | Explains that two green tests cover only a cold search and openResult, not tenant cache reuse or return. |
| `no-false-positive` | ✅ pass | Does not invent ranking, billing, or database defects; additional cache risks are accurately bounded as unspecified. |
| `minimal-actions` | ✅ pass | Requires workspace-scoped cache entries, authorization on hits, state restoration, and focused regression tests. |

### scenario-4 — revised-skill verdicts

| Criterion | Verdict | Why |
|---|---|---|
| `correct-verdict` | ✅ pass | Leads Ready to ship and ties it to complete direct evidence with no material scope drift. |
| `complete-contract` | ✅ pass | Its contract and ledger cover every required permission, filtering, CSV, empty-result, and invariance item. |
| `direct-evidence` | ✅ pass | Cites the feature diff, implementation paths, all six passing tests, and focused checks. |
| `permission-and-filtering` | ✅ pass | Credits the early role guard and direct status/from/to filter evidence. |
| `csv-safety` | ✅ pass | Correctly recognizes structural CSV escaping and formula neutralization for direct and control-prefixed inputs. |
| `no-invented-blockers` | ✅ pass | Introduces no generic release gates or requirements outside the brief. |
| `no-false-positive` | ✅ pass | Accurately states the exporter does not mutate transactions or change filter behavior. |
