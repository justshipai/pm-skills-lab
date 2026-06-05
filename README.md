# pm-skills-lab

> **Evaluated, vendor-neutral PM skills for AI agents.** Every skill ships with an eval that checks it actually makes an agent better at a real product-management task.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](./LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](./CONTRIBUTING.md)
[![Eval harness included](https://img.shields.io/badge/evals-self--serve%20harness-blue.svg?style=flat-square)](./EVALS.md)

## Why this exists

Most PM skill libraries are *"trust me, here's a markdown file."* You can't tell which skills actually help and which just add words.

**pm-skills-lab takes the opposite stance: every skill ships with a scenario eval and an in-repo harness that runs the task _with and without_ the skill, then grades both against a rubric.** A skill earns the **verified** mark only when the with-skill run beats the no-skill baseline. Results are published in [`EVALS.md`](./EVALS.md) — so "it works" is a number you can check, not a claim you have to trust. Running evals needs only an LLM API key; no external eval service required.

> **Status:** 46 skills authored across 9 categories. 41 have been run through the harness so far — **30 verified, 11 no-measurable-lift (strong baseline), 0 failed**; the 5 newest (data & experimentation) are eval-ready and awaiting their run. Live status and per-criterion detail are in [`EVALS.md`](./EVALS.md). Running the evals also surfaced (and fixed) a real measurement bug along the way — which is exactly what evals are for.

This is a **curated, maintained library** — the skills here are authored and held to the eval bar, so you can install the set and trust it. Contributions are welcome (see below) and held to the same bar, but the core is a deliberately-built collection, not a free-for-all.

Two more commitments:

- **Vendor-neutral and open.** No upsell, no paywall, no newsletter gate. MIT-licensed.
- **Portable by default.** Built on the open [Agent Skills](https://agentskills.io/) standard, so skills work in Claude Code, Claude Cowork, Gemini CLI, Cursor, and Codex — not just one tool.

## Launch wedge: skills for building AI products

The deepest, most battle-tested category in the lab is **AI-product PM** — the work of shipping features powered by LLMs and agents, where generic PM advice runs out fast. Start here:

| Skill | What it does |
|---|---|
| [`ai-feature-spec`](./skills/ai-product/ai-feature-spec/) | Specs an AI feature with an eval plan, guardrails, and graceful fallbacks baked in |
| [`ai-prd`](./skills/ai-product/ai-prd/) | Full AI PRD anchored on a model card, data strategy, and evaluation strategy |
| [`llm-eval-set-designer`](./skills/ai-product/llm-eval-set-designer/) | Designs a runnable eval set (stratified cases + graders + bars), Hamel-style |
| [`model-selection`](./skills/ai-product/model-selection/) | Eval-driven model/cost/latency/quality trade-off and recommendation |
| [`hallucination-risk-register`](./skills/ai-product/hallucination-risk-register/) | Enumerates failure modes with detection + mitigation, ranked by exposure |
| [`staged-ai-rollout`](./skills/ai-product/staged-ai-rollout/) | Shadow → canary → GA rollout plan with eval gates and a kill switch |
| [`eval-rubric-designer`](./skills/ai-product/eval-rubric-designer/) | Builds an LLM-as-judge rubric with anchored criteria and calibration |
| [`agent-capability-spec`](./skills/ai-product/agent-capability-spec/) | Specs an agent's tools, permissions, autonomy, and scope boundaries |
| [`human-in-the-loop-design`](./skills/ai-product/human-in-the-loop-design/) | Maps each action to the right human oversight by risk and confidence |
| [`ai-pricing-model`](./skills/ai-product/ai-pricing-model/) | Unit-economics-grounded pricing with margin guardrails |

Live **verified status for every skill is tracked in [`EVALS.md`](./EVALS.md)** — currently 12/15 verified across the repo, with 3 marked *no measurable lift* (a strong base model already aces those scenarios unaided; see the status key in EVALS.md). The rest of the wedge (11 more) is catalogued in [`CATALOG.md`](./CATALOG.md) and **open for contribution**.

Beyond the wedge, the generic library is underway too — `prd-generator`, `rice-scorer`, `okr-drafting`, `roadmap-builder`, and `stakeholder-map` are authored, with ~140 more catalogued.

## How it works

Each skill is a self-contained folder built to one standard:

```
skills/<category>/<skill-name>/
├── SKILL.md      # the skill — short trigger description + detailed body (Agent Skills standard)
├── EXAMPLE.md    # one real input → the resulting output
└── evals/
    ├── scenario-1/
    │   ├── task.md         # the brief shown to the agent (no mention of the skill)
    │   ├── criteria.json   # the scoring rubric
    │   └── capability.txt  # which capability of the skill this tests
    ├── results.json        # written by the harness when you run it
    └── RESULTS.md          # human-readable results: baseline vs. with-skill
```

## Eval results

The proof lives in the repo, not in a claim. [`scripts/run_evals.py`](./scripts/run_evals.py) runs each scenario **twice** — once with no skill (baseline) and once with `SKILL.md` supplied as the system prompt (treatment) — then an LLM judge scores both against `criteria.json`. A skill is **verified** when the treatment passes the rubric *and* beats the baseline on every scenario. Per-skill detail lands in `evals/RESULTS.md`; the roll-up is in [`EVALS.md`](./EVALS.md).

It's deliberately simple — no Tessl, no service, no install. Just:

```sh
export ANTHROPIC_API_KEY=sk-ant-...
python3 scripts/run_evals.py                       # all skills
python3 scripts/run_evals.py skills/specs/prd-generator   # one skill
```

(The scenario format is inspired by [Tessl's scenario evals](https://docs.tessl.io/improving-your-skills/evaluate-skill-quality-using-scenarios), but you never need Tessl to use this repo.)

## Install (use a skill)

Skills follow the open [Agent Skills](https://agentskills.io/) standard — a folder with a `SKILL.md`. To use one, copy its folder into your tool's skills directory:

```sh
# Claude Code / Claude Cowork
cp -r skills/ai-product/ai-feature-spec ~/.claude/skills/

# Gemini CLI → ~/.gemini/skills/ · Cursor → .cursor/skills/ · Codex → .codex/skills/
```

Claude then loads the skill automatically when your request matches its description, or you can invoke it explicitly. (No marketplace or plugin install required — grab exactly the skills you want.)

## The skill catalog

The full roadmap lives in [`CATALOG.md`](./CATALOG.md) — ~160 skills across 14 categories, from discovery to growth to AI-product. Anything not yet authored is fair game for a PR.

| Category | Planned | Authored |
|---|---|---|
| AI-product PM *(launch wedge)* | 21 | 10 |
| Discovery & customer research | 20 | 4 |
| Market & competitive | 12 | 5 |
| Strategy & vision | 14 | 5 |
| Prioritization & planning | 15 | 3 |
| Specs & definition | 15 | 1 |
| Design & UX | 10 | 7 |
| Data, metrics & experimentation | 12 | 5 |
| Go-to-market & launch | 11 | 0 |
| Growth | 7 | 0 |
| Communication & stakeholder | 12 | 6 |
| People, leadership & career | 10 | 0 |
| Meta / repo utilities | 5 | 0 |

## Contributing

The library is actively maintained, but good skills from the community are very welcome — held to exactly the same eval bar as first-party ones. Read [CONTRIBUTING.md](./CONTRIBUTING.md). The short version: pick a skill from the catalog, scaffold it with `scripts/new-skill.sh`, write the `SKILL.md`, add a worked `EXAMPLE.md`, write a scenario eval, then run `python3 scripts/run_evals.py <skill>` and commit the `RESULTS.md` showing it beats the no-skill baseline. CI checks structure; the result file is the proof.

## Credits & prior art

Standing on the shoulders of the people who proved PM skills were worth packaging — [Paweł Huryn](https://github.com/phuryn/pm-skills), [Niko Vijayaratnam](https://github.com/nikovijay/pm-ai-skills-kit), and [Aman Khan](https://github.com/amanaiproduct/amans-skills) — and the PM thinkers whose frameworks these skills encode (Cagan, Torres, Martin, Savoia, Dunford, Biddle, Ulwick, and others). Design & AI-UX skills drew inspiration from the [AI UX Playground](https://www.aiuxplayground.com/). Eval format adapted from [Tessl](https://docs.tessl.io/).

## License

[MIT](./LICENSE). Use it, fork it, ship it.
