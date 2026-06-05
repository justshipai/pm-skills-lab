# Skill catalog

The full roadmap — ~160 skills across 14 categories. `[x]` = authored & eval-ready, `[ ]` = open for contribution. Whether an authored skill is **verified** (beats its baseline on a real eval run) is tracked separately in [`EVALS.md`](./EVALS.md). Want to build one? Open an issue to claim it, then follow [CONTRIBUTING.md](./CONTRIBUTING.md).

## AI-product PM — launch wedge (10 / 21)

- [x] `ai-feature-spec` — Spec an AI feature with eval plan, guardrails, and fallbacks
- [x] `ai-prd` — PRD for an AI feature (model card, data requirements, success criteria)
- [x] `llm-eval-set-designer` — Design an eval set (cases + rubric) for an AI feature
- [x] `eval-rubric-designer` — Build an LLM-as-judge rubric that discriminates good from bad
- [ ] `golden-set-curation` — Curate a golden/test set for an AI feature
- [ ] `synthetic-eval-data` — Generate synthetic evaluation data
- [ ] `prompt-spec` — Prompt spec / prompt review
- [x] `model-selection` — Model / cost / latency / quality trade-off analysis
- [ ] `model-migration-plan` — Model upgrade/migration plan with regression eval
- [x] `hallucination-risk-register` — Failure modes and the guardrail for each
- [ ] `prompt-injection-threat-model` — Prompt-injection / jailbreak threat model
- [ ] `rag-quality-eval` — RAG / retrieval-quality eval
- [x] `agent-capability-spec` — Agent tools, permissions, and scope boundaries
- [x] `human-in-the-loop-design` — Review / escalation / undo for AI actions
- [ ] `ai-ux-patterns-review` — Trust, transparency, undo, citations
- [ ] `confidence-uncertainty-ux` — When to surface "I'm not sure"
- [ ] `ai-success-metrics` — Quality, cost, latency, deflection metrics
- [x] `ai-pricing-model` — Token / usage-based pricing and unit economics
- [x] `staged-ai-rollout` — Shadow → canary → GA rollout with eval gates
- [ ] `data-flywheel-design` — Feedback loops that improve the model
- [ ] `responsible-ai-checklist` — Responsible-AI / red-team checklist

## Discovery & customer research (4 / 20)

- [x] `interview-script` — Customer interview script (JTBD probing)
- [x] `interview-synthesizer` — Transcript → themes, JTBD, signal strength
- [x] `opportunity-solution-tree` — Build an OST (Teresa Torres)
- [ ] `discovery-cadence-planner` — Continuous discovery cadence
- [x] `assumption-mapping` — Value / Usability / Feasibility / Viability
- [ ] `assumption-prioritizer` — Impact × Risk → experiments
- [ ] `survey-designer` — Question bank + bias checks
- [ ] `survey-analyzer` — NPS/survey responses → sentiment + themes
- [ ] `feedback-clusterer` — Cluster support tickets / feedback
- [ ] `feature-request-triage` — Theme-tag and triage requests
- [ ] `jtbd-extractor` — Extract Jobs-to-be-Done
- [ ] `persona-builder` — Evidence-based personas
- [ ] `empathy-map` — Empathy map generator
- [ ] `journey-map` — Customer journey map
- [ ] `service-blueprint` — Service blueprint
- [ ] `winloss-analyzer` — Win/loss interview analysis
- [ ] `churn-analyzer` — Cancellation/churn reason analysis
- [ ] `diary-study-planner` — Longitudinal study plan
- [ ] `usability-test-plan` — Usability test plan + script
- [ ] `insight-nuggetizer` — Atomic, taggable insights

## Market & competitive (0 / 11)

- [ ] `competitor-teardown` — Competitor profile/teardown
- [ ] `battlecard` — Sales-ready competitive battlecard
- [ ] `feature-comparison-matrix` — Feature comparison matrix
- [ ] `market-sizing` — TAM/SAM/SOM (top-down + bottom-up)
- [ ] `pestle-scan` — Macro landscape (PESTLE)
- [ ] `porters-five-forces` — Five Forces analysis
- [ ] `positioning-map` — 2×2 perceptual map
- [ ] `dhm-profile` — Gibson Biddle DHM profile
- [ ] `competitor-pricing-teardown` — Competitor pricing & packaging
- [ ] `analyst-report-digest` — Gartner/Forrester-style synthesis
- [ ] `changelog-monitor` — Competitor release monitor

## Strategy & vision (5 / 14)

- [x] `product-vision` — Product vision statement
- [x] `product-strategy-canvas` — Vision → defensibility canvas
- [ ] `strategy-doc` — Context / insight / choices / actions
- [x] `playing-to-win` — Roger Martin strategy cascade
- [x] `north-star-metric` — North Star + input-metric tree
- [ ] `product-principles` — Product principles / tenets
- [ ] `business-model-canvas` — Business Model Canvas
- [ ] `lean-canvas` — Lean Canvas
- [ ] `value-proposition` — JTBD 6-part value prop
- [ ] `moats-analysis` — Defensibility / moats
- [ ] `build-buy-partner` — Build/buy/partner decision
- [ ] `platform-strategy` — Platform-vs-product analysis
- [x] `working-backwards` — PR/FAQ narrative (Amazon)
- [ ] `bets-and-themes` — Annual bets & themes framing

## Prioritization & planning (3 / 15)

- [x] `rice-scorer` — RICE scoring
- [ ] `ice-scorer` — ICE scoring
- [ ] `wsjf` — Cost-of-delay / WSJF
- [ ] `kano-model` — Kano classification
- [ ] `moscow` — MoSCoW sorting
- [ ] `opportunity-scoring` — Ulwick opportunity scores
- [ ] `backlog-prioritizer` — Multi-criteria backlog prioritization
- [x] `okr-drafting` — Objective + measurable KRs
- [ ] `okr-health-check` — Alignment audit
- [ ] `quarterly-planning` — Capacity × priorities synthesis
- [x] `roadmap-builder` — Now/Next/Later outcome roadmap
- [ ] `roadmap-narrative` — Stakeholder story for a roadmap
- [ ] `capacity-planner` — Capacity & resource planning
- [ ] `dependency-mapper` — Dependency mapping
- [ ] `outcome-roadmap-converter` — Features → outcomes

## Specs & definition (1 / 15)

- [x] `prd-generator` — PRD (problem/value/risks, Cagan framing)
- [ ] `one-pager` — One-pager / brief
- [ ] `feature-spec` — Stories, AC, edge cases
- [ ] `user-stories` — INVEST, 3 C's
- [ ] `job-stories` — "When… I want… so I can…"
- [ ] `acceptance-criteria` — Gherkin / AC writer
- [ ] `edge-case-enumerator` — Edge & error-state enumeration
- [ ] `nfr-checklist` — Non-functional requirements
- [ ] `open-questions` — Technical-design questions
- [ ] `platform-api-requirements` — Platform/API requirements
- [ ] `test-scenarios` — Happy / edge / error scenarios
- [ ] `synthetic-dataset` — Dummy dataset generator
- [ ] `spec-red-team` — Spec gap-finder
- [ ] `decision-record` — RFC / ADR (options, trade-offs, reversibility)
- [ ] `mvp-scope-cutter` — Thinnest-slice scoping

## Design & UX (0 / 8)

- [ ] `ux-heuristic-audit` — Nielsen heuristics
- [ ] `accessibility-audit` — WCAG quick audit
- [ ] `ia-review` — Information architecture / nav
- [ ] `wireframe-from-spec` — Wireframe prompt for prototyping tools
- [ ] `microcopy-pass` — UX-writing pass
- [ ] `design-critique` — Design critique facilitator
- [ ] `onboarding-flow` — Onboarding flow design
- [ ] `empty-state-designer` — Empty/error-state design

## Data, metrics & experimentation (0 / 12)

- [ ] `nl-to-sql` — Natural language → SQL
- [ ] `metrics-dashboard` — North Star + inputs + guardrails
- [ ] `funnel-analysis` — Funnel interpretation
- [ ] `cohort-analysis` — Retention / cohort analysis
- [ ] `ab-test-designer` — Hypothesis, MDE, sample size
- [ ] `ab-test-interpreter` — Significance, ship/stop/extend
- [ ] `experiment-backlog` — Experiment roadmap
- [ ] `metric-tree` — Metric definition / tree
- [ ] `guardrail-metrics` — Guardrail metric definition
- [ ] `data-storytelling` — Metrics → narrative
- [ ] `metric-drop-diagnoser` — Anomaly diagnosis
- [ ] `willingness-to-pay` — Van Westendorp WTP analysis

## Go-to-market & launch (0 / 11)

- [ ] `gtm-strategy` — Channels, messaging, motion
- [ ] `launch-tiering` — T1/T2/T3 + plan
- [ ] `launch-checklist` — Launch readiness checklist
- [ ] `beachhead-segment` — Beachhead segment selection
- [ ] `icp-definition` — Ideal customer profile
- [ ] `positioning-statement` — April Dunford style
- [ ] `messaging-house` — Value-prop ladder
- [ ] `release-notes` — Release notes / changelog
- [ ] `enablement-kit` — Internal launch brief / enablement
- [ ] `press-release-faq` — Working-backwards PR + FAQ
- [ ] `pricing-packaging` — Pricing & packaging design

## Growth (0 / 7)

- [ ] `growth-loop` — Growth loop / flywheel design
- [ ] `activation-finder` — Aha-moment / activation
- [ ] `funnel-optimization` — Funnel optimization plan
- [ ] `retention-lifecycle` — Lifecycle (email/notification) strategy
- [ ] `referral-mechanic` — Referral / virality design
- [ ] `growth-experiment-backlog` — Growth experiment backlog
- [ ] `plg-motion` — PLG motion design

## Communication & stakeholder (1 / 12)

- [x] `stakeholder-map` — Power × Interest + comms plan
- [ ] `weekly-update` — Outcomes-led weekly update
- [ ] `exec-board-update` — Exec/board update + narrative
- [ ] `status-multi-audience` — Exec / team / Slack formats
- [ ] `meeting-prep` — Meeting prep brief
- [ ] `meeting-notes-actions` — Notes → decisions + actions
- [ ] `decision-log` — Decision log keeper
- [ ] `pre-mortem` — Pre-mortem facilitator
- [ ] `post-mortem` — Incident / post-mortem writeup
- [ ] `retrospective` — Retro facilitator
- [ ] `saying-no` — Scope-pushback drafter
- [ ] `xfn-alignment-brief` — Cross-functional alignment brief

## People, leadership & career (0 / 10)

- [ ] `one-on-one-prep` — 1:1 prep / coaching agenda
- [ ] `interview-kit` — Questions, scorecards, debrief
- [ ] `candidate-debrief` — Debrief synthesizer
- [ ] `30-60-90` — Onboarding plan
- [ ] `team-health` — Team health assessor
- [ ] `pm-competency-assessment` — Self-assessment + growth plan
- [ ] `brag-doc` — Performance-review / brag doc
- [ ] `resume-reviewer` — PM resume review (XYZ+S)
- [ ] `resume-tailoring` — Tailor resume to a JD
- [ ] `promo-packet` — Promotion case writer

## Meta / repo utilities (0 / 5)

- [ ] `skill-scaffolder` — Write a new PM skill to the repo standard
- [ ] `description-optimizer` — Trigger-reliability tuning
- [ ] `eval-scenario-writer` — Generate scenario evals for a skill
- [ ] `framework-selector` — "Which framework for this situation?"
- [ ] `the-council` — Multi-perspective decision debate
