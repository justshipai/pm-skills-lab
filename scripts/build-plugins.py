#!/usr/bin/env python3
"""
Build installable Claude Code / Cowork plugins from the flat skills/ source.

Source of truth is skills/<category>/<skill>/. This script assembles one plugin
per non-empty category under plugins/, copying each skill's SKILL.md (and any
extra reference files) into <plugin>/skills/<skill>/, and regenerates the
top-level .claude-plugin/marketplace.json so `claude plugin marketplace add
justshipai/pm-skills-lab` works.

evals/ and EXAMPLE.md are intentionally NOT shipped in the installable plugin —
they are repo-quality artifacts, not runtime context.

Usage: python3 scripts/build-plugins.py
No third-party dependencies.
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
PLUGINS_DIR = ROOT / "plugins"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
VERSION = "0.1.0"

CATEGORY_META = {
    "ai-product":     ("pm-ai-product",     "Skills for building AI products: specs, evals, guardrails, rollout, pricing."),
    "discovery":      ("pm-discovery",      "Customer discovery and research: interviews, OSTs, assumptions, journeys."),
    "market":         ("pm-market",         "Market and competitive analysis: teardowns, sizing, battlecards, positioning."),
    "strategy":       ("pm-strategy",       "Strategy and vision: canvases, North Star, working-backwards, moats."),
    "prioritization": ("pm-prioritization", "Prioritization and planning: RICE/ICE/Kano, OKRs, roadmaps."),
    "specs":          ("pm-specs",          "Specs and definition: PRDs, user/job stories, acceptance criteria."),
    "design":         ("pm-design",         "Design and UX for PMs: heuristic audits, IA, onboarding flows."),
    "data":           ("pm-data",           "Data, metrics and experimentation: SQL, cohorts, A/B tests, metric trees."),
    "gtm":            ("pm-gtm",            "Go-to-market and launch: GTM strategy, tiering, positioning, release notes."),
    "growth":         ("pm-growth",         "Growth: loops, activation, retention, referral, PLG."),
    "comms":          ("pm-comms",          "Communication and stakeholder: updates, pre-mortems, decision logs."),
    "people":         ("pm-people",         "People, leadership and career: 1:1s, hiring kits, 30-60-90, promo packets."),
    "meta":           ("pm-meta",           "Repo utilities: skill scaffolding, eval scenarios, framework selection."),
}


def build():
    if PLUGINS_DIR.exists():
        shutil.rmtree(PLUGINS_DIR)

    plugins = []
    for category in sorted(SKILLS_DIR.iterdir()) if SKILLS_DIR.exists() else []:
        if not category.is_dir():
            continue
        skills = [s for s in sorted(category.iterdir())
                  if s.is_dir() and (s / "SKILL.md").exists()]
        if not skills:
            continue

        plugin_name, description = CATEGORY_META.get(
            category.name, (f"pm-{category.name}", f"PM skills: {category.name}.")
        )
        plugin_root = PLUGINS_DIR / plugin_name
        (plugin_root / ".claude-plugin").mkdir(parents=True, exist_ok=True)

        for skill in skills:
            dest = plugin_root / "skills" / skill.name
            dest.mkdir(parents=True, exist_ok=True)
            for item in skill.iterdir():
                if item.name in ("evals", "EXAMPLE.md"):
                    continue
                if item.is_dir():
                    shutil.copytree(item, dest / item.name)
                else:
                    shutil.copy2(item, dest / item.name)

        (plugin_root / ".claude-plugin" / "plugin.json").write_text(
            json.dumps({
                "name": plugin_name,
                "version": VERSION,
                "description": description,
            }, indent=2) + "\n",
            encoding="utf-8",
        )

        plugins.append({
            "name": plugin_name,
            "source": f"./plugins/{plugin_name}",
            "description": description,
        })
        print(f"built {plugin_name} ({len(skills)} skill[s])")

    MARKETPLACE.parent.mkdir(parents=True, exist_ok=True)
    MARKETPLACE.write_text(
        json.dumps({
            "name": "pm-skills-lab",
            "owner": {"name": "justshipai", "url": "https://github.com/justshipai"},
            "metadata": {
                "description": "Evaluated, vendor-neutral PM skills for AI agents.",
                "version": VERSION,
            },
            "plugins": plugins,
        }, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {MARKETPLACE.relative_to(ROOT)} ({len(plugins)} plugin[s])")


if __name__ == "__main__":
    build()
