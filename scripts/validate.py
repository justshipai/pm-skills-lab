#!/usr/bin/env python3
"""
Validate skills against the pm-skills-lab standard.

Checks each skill folder has:
  - SKILL.md with YAML frontmatter containing non-empty `name` and `description`
  - EXAMPLE.md
  - evals/ with at least one scenario-* containing task.md, capability.txt,
    and a well-formed criteria.json (criteria[], weights, pass_threshold)
  - no leftover TODO placeholders in shipped files

Usage:
  python3 scripts/validate.py                       # validate every skill
  python3 scripts/validate.py skills/ai-product/ai-feature-spec [more...]

Exit code is non-zero if any skill fails. No third-party dependencies.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"


def parse_frontmatter(text: str):
    """Return dict of top-level scalar keys in a leading --- ... --- block."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return None
    data = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" in line and not line.startswith((" ", "\t")):
            key, _, val = line.partition(":")
            data[key.strip()] = val.strip().strip('"').strip("'")
    return data


def has_todo(text: str) -> bool:
    return "TODO" in text


def validate_skill(skill_dir: Path):
    errors = []
    rel = skill_dir.relative_to(ROOT)

    # SKILL.md
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        errors.append("missing SKILL.md")
    else:
        text = skill_md.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append("SKILL.md has no YAML frontmatter (--- block)")
        else:
            if not fm.get("name"):
                errors.append("SKILL.md frontmatter missing `name`")
            desc = fm.get("description", "")
            if not desc:
                errors.append("SKILL.md frontmatter missing `description`")
            elif len(desc) > 500:
                errors.append("SKILL.md `description` too long (>500 chars) — keep it short")
        if has_todo(text):
            errors.append("SKILL.md still contains TODO placeholders")

    # EXAMPLE.md
    example_md = skill_dir / "EXAMPLE.md"
    if not example_md.exists():
        errors.append("missing EXAMPLE.md")
    elif has_todo(example_md.read_text(encoding="utf-8")):
        errors.append("EXAMPLE.md still contains TODO placeholders")

    # evals/
    evals_dir = skill_dir / "evals"
    scenarios = sorted(p for p in evals_dir.glob("scenario-*") if p.is_dir()) if evals_dir.exists() else []
    if not scenarios:
        errors.append("missing evals/scenario-* (need at least one)")
    for sc in scenarios:
        screl = sc.relative_to(skill_dir)
        for required in ("task.md", "capability.txt"):
            f = sc / required
            if not f.exists():
                errors.append(f"{screl}: missing {required}")
            elif has_todo(f.read_text(encoding="utf-8")):
                errors.append(f"{screl}/{required}: still contains TODO placeholders")
        crit = sc / "criteria.json"
        if not crit.exists():
            errors.append(f"{screl}: missing criteria.json")
        else:
            try:
                data = json.loads(crit.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                errors.append(f"{screl}/criteria.json: invalid JSON ({e})")
            else:
                items = data.get("criteria")
                if not isinstance(items, list) or not items:
                    errors.append(f"{screl}/criteria.json: `criteria` must be a non-empty list")
                else:
                    for i, c in enumerate(items):
                        if "id" not in c or "description" not in c or "weight" not in c:
                            errors.append(f"{screl}/criteria.json: criterion {i} needs id, description, weight")
                        if "TODO" in json.dumps(c):
                            errors.append(f"{screl}/criteria.json: criterion {i} still contains TODO")
                    thr = data.get("pass_threshold")
                    if not isinstance(thr, (int, float)) or not (0 < thr <= 1):
                        errors.append(f"{screl}/criteria.json: pass_threshold must be a number in (0, 1]")

    return rel, errors


def discover_skills():
    skills = []
    if not SKILLS_DIR.exists():
        return skills
    for category in sorted(SKILLS_DIR.iterdir()):
        if not category.is_dir():
            continue
        for skill in sorted(category.iterdir()):
            if skill.is_dir() and (skill / "SKILL.md").exists():
                skills.append(skill)
    return skills


def main(argv):
    if argv:
        targets = [Path(a).resolve() for a in argv]
    else:
        targets = discover_skills()

    if not targets:
        print("No skills found to validate.")
        return 0

    failed = 0
    for skill_dir in targets:
        rel, errors = validate_skill(skill_dir)
        if errors:
            failed += 1
            print(f"FAIL  {rel}")
            for e in errors:
                print(f"        - {e}")
        else:
            print(f"PASS  {rel}")

    print()
    total = len(targets)
    print(f"{total - failed}/{total} skill(s) passed structural validation.")
    if failed:
        print("Note: structural validation does not run the eval. A maintainer "
              "confirms the with/without-skill lift before merge.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
