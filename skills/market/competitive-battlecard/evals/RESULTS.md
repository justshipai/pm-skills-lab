# Eval results — `competitive-battlecard`

- **Run:** 2026-06-05 14:18 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.95 | 1.0 | +0.05 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `how-to-win-and-differentiators` | ✅ pass | Opens with a clear one-line win thesis, lists specific differentiators framed for the buyer (external participant parity, fast deployment, dedicated roadmap, visible ROI, no lock-in), and is explicitly positioned as a sales tool throughout. |
| `honest-strengths` | ✅ pass | Dedicates a full table to genuine competitor strengths (bundle pricing, single-vendor simplicity, native integration, brand trust) and reframes each with the real cost to the buyer rather than dismissing them. |
| `exploitable-weaknesses` | ✅ pass | Five named, buyer-felt weaknesses with operational specificity: external participant degradation, quality on unmanaged networks, roadmap latency, low actual adoption with a concrete benchmark (30-40%), and licensing lock-in. These are deal-usable, not cosmetic. |
| `objection-handling-or-landmines` | ✅ pass | Six discovery landmine questions with intent annotations, plus a full objection-handling table covering six common objections with specific, non-generic responses including a pilot close and cost-reframing. |
| `when-to-walk` | ✅ pass | Explicitly names five walk-away conditions (IT/procurement-only buyer, no external calls, mid-license cycle, box-checking mandate, decision already made) alongside clear win conditions, with honest guidance like 'protect your team's time.' |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/market/competitive-battlecard`._
