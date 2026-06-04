# pm-skills-lab

> **Evaluated, vendor-neutral PM skills for AI agents.** Every skill is proven to make an agent better at a real product-management task — or it doesn't ship.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](./LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](./CONTRIBUTING.md)
[![Skills: verified by eval](https://img.shields.io/badge/skills-verified%20by%20eval-blue.svg?style=flat-square)](./CONTRIBUTING.md)

## Why this exists

Most PM skill libraries are *"trust me, here's a markdown file."* You can't tell which skills actually help and which just add words.

**pm-skills-lab is different: every skill ships with a scenario eval, and CI runs the agent _with and without_ the skill.** A skill only merges if it **measurably improves** the output against a rubric. So you get skills that demonstrably work — not just more prompts.

This is a **curated, maintained library** — the skills here are authored and held to the eval bar, so you can install the set and trust it. Contributions are welcome (see below) and held to the same bar, but the core is a deliberately-built collection, not a free-for-all.

Two more commitments:

- **Vendor-neutral and open.** No upsell, no paywall, no newsletter gate. MIT-licensed.
- **Portable by default.** Built on the open [Agent Skills](https://agentskills.io/) standard, so skills work in Claude Code, Claude Cowork, Gemini CLI, Cursor, and Codex — not just one tool.

## Launch wedge: skills for building AI products

The deepest, most battle-tested category in the lab is **AI-product PM** — the work of shipping features powered by LLMs and agents, where generic PM advice runs out fast. Start here:

| Skill | What it does |
|---|---|
| [`ai-feature-spec`](./skills/ai-product/ai-feature-spec/) ✅ | Specs an AI feature with an eval plan, guardrails, and graceful fallbacks baked in |
| `ai-prd` | PRD for an AI feature — model card, data requirements, quality/cost/latency success criteria |
| `llm-eval-set-designer` | Designs an eval set (cases + rubric) for an AI feature, Hamel-style |
| `eval-rubric-designer` | Builds an LLM-as-judge rubric that actually discriminates good from bad |
| `model-selection` | Model/cost/latency/quality trade-off analysis for a given use case |
| `hallucination-risk-register` | Enumerates failure modes and the guardrail for each |
| `agent-capability-spec` | Specs an agent's tools, permissions, and scope boundaries |
| `human-in-the-loop-design` | Designs review/escalation/undo for AI actions |
| `ai-pricing-model` | Token/usage-based pricing and unit economics |
| `staged-ai-rollout` | Shadow → canary → GA rollout plan with eval gates |

✅ = live and verified. The rest are on the roadmap and **open for contribution** — see [CONTRIBUTING.md](./CONTRIBUTING.md).

## How it works

Each skill is a self-contained folder built to one standard:

```
skills/<category>/<skill-name>/
├── SKILL.md      # the skill — short trigger description + detailed body (Agent Skills standard)
├── EXAMPLE.md    # one real input → the resulting output
└── evals/
    └── scenario-1/
        ├── task.md         # the brief shown to the agent
        ├── criteria.json   # the scoring rubric
        └── capability.txt  # which capability of the skill this tests
```

The eval format follows [Tessl's scenario evals](https://docs.tessl.io/improving-your-skills/evaluate-skill-quality-using-scenarios) so you can use `tessl scenario generate` / `tessl eval run` instead of building a harness. The merge gate: the **with-skill** run must beat the **without-skill** run on the rubric. Skills that clear it carry the **verified** badge.

## Install

**Claude Cowork**
1. Open **Customize** (bottom-left) → **Browse plugins** → **Personal** → **+**
2. **Add marketplace from GitHub** → enter `justshipai/pm-skills-lab`

**Claude Code (CLI)**
```sh
claude plugin marketplace add justshipai/pm-skills-lab
claude plugin install pm-ai-product@pm-skills-lab   # the launch wedge
# …or install other category plugins as they ship
```

**Other agents (skills only)** — copy any `skills/<category>/<skill-name>/` folder into your tool's skills directory (e.g. `~/.gemini/skills/`, `.cursor/skills/`, `.codex/skills/`).

## The skill catalog

The full roadmap lives in [`CATALOG.md`](./CATALOG.md) — ~160 skills across 14 categories, from discovery to growth to AI-product. Anything not yet live is fair game for a PR.

| Category | Planned | Live |
|---|---|---|
| AI-product PM *(launch wedge)* | 21 | 1 |
| Discovery & customer research | 20 | 0 |
| Market & competitive | 11 | 0 |
| Strategy & vision | 14 | 0 |
| Prioritization & planning | 15 | 0 |
| Specs & definition | 15 | 0 |
| Design & UX | 8 | 0 |
| Data, metrics & experimentation | 12 | 0 |
| Go-to-market & launch | 11 | 0 |
| Growth | 7 | 0 |
| Communication & stakeholder | 12 | 0 |
| People, leadership & career | 10 | 0 |
| Meta / repo utilities | 5 | 0 |

## Contributing

The library is actively maintained, but good skills from the community are very welcome — held to exactly the same eval bar as first-party ones. Read [CONTRIBUTING.md](./CONTRIBUTING.md). The short version: pick a skill from the catalog, scaffold it with `scripts/new-skill.sh`, write the `SKILL.md`, add a worked `EXAMPLE.md`, and include a scenario eval that shows the skill beats the no-skill baseline. CI checks the structure; a maintainer runs the eval.

## Credits & prior art

Standing on the shoulders of the people who proved PM skills were worth packaging — [Paweł Huryn](https://github.com/phuryn/pm-skills), [Niko Vijayaratnam](https://github.com/nikovijay/pm-ai-skills-kit), and [Aman Khan](https://github.com/amanaiproduct/amans-skills) — and the PM thinkers whose frameworks these skills encode (Cagan, Torres, Martin, Savoia, Dunford, Biddle, Ulwick, and others). Eval format adapted from [Tessl](https://docs.tessl.io/).

## License

[MIT](./LICENSE). Use it, fork it, ship it.
