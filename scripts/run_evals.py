#!/usr/bin/env python3
"""
run_evals.py — the pm-skills-lab eval harness.

Self-contained. No Tessl, no third-party services, no pip installs — just an
LLM API key. For each skill scenario it runs the task TWICE:

  • baseline   — the task with NO skill in context
  • treatment  — the same task WITH the skill's SKILL.md as the system prompt

then grades both against the scenario's criteria.json using an LLM judge, and
writes the result into the skill's evals/ folder. A skill "earns its place" when
the treatment passes the rubric AND scores higher than the baseline — i.e. the
skill measurably improved the output. Finally it regenerates EVALS.md (the
repo-wide results dashboard).

Usage:
  export ANTHROPIC_API_KEY=sk-ant-...
  python3 scripts/run_evals.py                      # run every skill
  python3 scripts/run_evals.py skills/specs/prd-generator [more...]
  python3 scripts/run_evals.py --model claude-sonnet-4-6 --judge-model claude-opus-4-6

Provider: defaults to the Anthropic Messages API. Set EVAL_BASE_URL / the call
helper to point elsewhere if you prefer another provider.
"""
import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
DASHBOARD = ROOT / "EVALS.md"

DEFAULT_MODEL = os.environ.get("EVAL_MODEL", "claude-sonnet-4-6")
DEFAULT_JUDGE = os.environ.get("EVAL_JUDGE_MODEL", "claude-sonnet-4-6")
API_URL = os.environ.get("EVAL_BASE_URL", "https://api.anthropic.com/v1/messages")
ANTHROPIC_VERSION = "2023-06-01"


# ---------------------------------------------------------------- model call

def call_model(system: str, user: str, model: str, max_tokens: int = 2000) -> str:
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("ERROR: set ANTHROPIC_API_KEY in your environment to run evals.")
    body = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": user}],
    }
    if system:
        body["system"] = system
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        API_URL, data=data, method="POST",
        headers={
            "x-api-key": key,
            "anthropic-version": ANTHROPIC_VERSION,
            "content-type": "application/json",
        },
    )
    last_err = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                payload = json.loads(resp.read())
            return "".join(b.get("text", "") for b in payload.get("content", []))
        except urllib.error.HTTPError as e:
            last_err = f"HTTP {e.code}: {e.read().decode('utf-8', 'ignore')[:200]}"
            if e.code in (429, 500, 502, 503, 529):
                time.sleep(2 * (attempt + 1)); continue
            break
        except Exception as e:  # noqa
            last_err = str(e); time.sleep(2 * (attempt + 1))
    sys.exit(f"ERROR calling model {model}: {last_err}")


# ---------------------------------------------------------------- helpers

def strip_frontmatter(text: str) -> str:
    m = re.match(r"^---\s*\n.*?\n---\s*\n", text, re.DOTALL)
    return text[m.end():] if m else text


def extract_json(text: str):
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.MULTILINE).strip()
    start = text.find("{")
    if start == -1:
        raise ValueError("no JSON object in judge output")
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{": depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start:i + 1])
    raise ValueError("unbalanced JSON in judge output")


VERDICT_VALUE = {"pass": 1.0, "partial": 0.5, "fail": 0.0}


def judge(output: str, criteria: dict, judge_model: str) -> dict:
    crits = criteria["criteria"]
    rubric_lines = [
        f'- id "{c["id"]}" (weight {c["weight"]}'
        f'{", REQUIRED/gate" if c.get("required") else ""}): {c["description"]}'
        for c in crits
    ]
    system = (
        "You are a strict, fair evaluator. You grade a candidate output against a "
        "rubric. For each criterion decide pass, partial, or fail based ONLY on "
        "whether the output demonstrably satisfies it. Be skeptical of generic "
        "filler. Return ONLY a JSON object."
    )
    user = (
        "RUBRIC:\n" + "\n".join(rubric_lines) +
        "\n\nCANDIDATE OUTPUT:\n\"\"\"\n" + output + "\n\"\"\"\n\n"
        "Return ONLY this JSON shape (no prose, no code fence):\n"
        '{ "<criterion_id>": { "verdict": "pass|partial|fail", "why": "<short>" }, ... }'
    )
    raw = call_model(system, user, judge_model, max_tokens=1500)
    verdicts = extract_json(raw)

    total_w = sum(c["weight"] for c in crits)
    got = 0.0
    gate_failed = False
    norm = {}
    for c in crits:
        v = (verdicts.get(c["id"], {}) or {}).get("verdict", "fail").lower()
        if v not in VERDICT_VALUE:
            v = "fail"
        norm[c["id"]] = {"verdict": v, "why": (verdicts.get(c["id"], {}) or {}).get("why", "")}
        got += c["weight"] * VERDICT_VALUE[v]
        if c.get("required") and v == "fail":
            gate_failed = True
    score = round(got / total_w, 3) if total_w else 0.0
    passed = (not gate_failed) and score >= criteria.get("pass_threshold", 0.7)
    return {"score": score, "passed": passed, "gate_failed": gate_failed, "verdicts": norm}


# ---------------------------------------------------------------- per skill

def run_skill(skill_dir: Path, model: str, judge_model: str) -> dict:
    skill_md = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    skill_body = strip_frontmatter(skill_md)
    scenarios = sorted(p for p in (skill_dir / "evals").glob("scenario-*") if p.is_dir())
    rel = skill_dir.relative_to(ROOT).as_posix()
    print(f"\n▶ {rel}  ({len(scenarios)} scenario[s])")

    scenario_results = []
    for sc in scenarios:
        task = (sc / "task.md").read_text(encoding="utf-8")
        criteria = json.loads((sc / "criteria.json").read_text(encoding="utf-8"))

        print(f"   · {sc.name}: baseline…", end="", flush=True)
        base_out = call_model("", task, model)
        print(" treatment…", end="", flush=True)
        treat_out = call_model(skill_body, task, model)
        print(" judging…", end="", flush=True)
        base = judge(base_out, criteria, judge_model)
        treat = judge(treat_out, criteria, judge_model)
        lift = round(treat["score"] - base["score"], 3)
        earns = treat["passed"] and lift > 0
        print(f" base={base['score']} treat={treat['score']} lift={lift:+} "
              f"{'✓ earns place' if earns else '✗'}")
        scenario_results.append({
            "scenario": sc.name,
            "baseline_score": base["score"],
            "treatment_score": treat["score"],
            "lift": lift,
            "treatment_passed": treat["passed"],
            "earns_place": earns,
            "treatment_verdicts": treat["verdicts"],
        })

    verified = bool(scenario_results) and all(s["earns_place"] for s in scenario_results)
    result = {
        "skill": rel,
        "run_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "model": model,
        "judge_model": judge_model,
        "verified": verified,
        "scenarios": scenario_results,
    }
    (skill_dir / "evals" / "results.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8")
    write_results_md(skill_dir, result)
    return result


def write_results_md(skill_dir: Path, r: dict):
    lines = [f"# Eval results — `{Path(r['skill']).name}`", "",
             f"- **Run:** {r['run_at']}",
             f"- **Model under test:** {r['model']}  ·  **Judge:** {r['judge_model']}",
             f"- **Verdict:** {'✅ VERIFIED — skill beats the no-skill baseline on every scenario' if r['verified'] else '❌ not verified — see below'}",
             "",
             "| Scenario | Baseline | With skill | Lift | Earns its place? |",
             "|---|---|---|---|---|"]
    for s in r["scenarios"]:
        lines.append(f"| {s['scenario']} | {s['baseline_score']} | {s['treatment_score']} "
                     f"| {s['lift']:+} | {'✅' if s['earns_place'] else '❌'} |")
    lines += ["", "_Baseline = the task with no skill. With skill = the same task and model, "
              "SKILL.md supplied as the system prompt. Scores are the weighted fraction of the "
              "scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with "
              "`python3 scripts/run_evals.py " + r["skill"] + "`._"]
    (skill_dir / "evals" / "RESULTS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- dashboard

def discover_skills():
    out = []
    if SKILLS_DIR.exists():
        for cat in sorted(SKILLS_DIR.iterdir()):
            if cat.is_dir():
                for s in sorted(cat.iterdir()):
                    if s.is_dir() and (s / "SKILL.md").exists():
                        out.append(s)
    return out


def regenerate_dashboard():
    rows, verified_n, run_n, total = [], 0, 0, 0
    for s in discover_skills():
        total += 1
        rel = s.relative_to(ROOT).as_posix()
        rj = s / "evals" / "results.json"
        if rj.exists():
            r = json.loads(rj.read_text(encoding="utf-8"))
            run_n += 1
            verified_n += 1 if r["verified"] else 0
            base = ", ".join(str(x["baseline_score"]) for x in r["scenarios"])
            treat = ", ".join(str(x["treatment_score"]) for x in r["scenarios"])
            status = "✅ verified" if r["verified"] else "❌ not verified"
            rows.append(f"| `{Path(rel).name}` | {status} | {base} | {treat} | {r['run_at']} |")
        else:
            rows.append(f"| `{Path(rel).name}` | ⏳ not yet run | – | – | – |")
    header = [
        "# Eval results dashboard", "",
        "Every skill ships with a scenario eval. This table shows, for each skill, whether it "
        "**measurably beats the no-skill baseline** when run through `scripts/run_evals.py`. "
        "A skill is **verified** only when its treatment run passes the rubric and scores higher "
        "than the baseline on every scenario. Per-skill detail lives in each skill's "
        "`evals/RESULTS.md`.", "",
        f"**Status: {verified_n} verified · {run_n}/{total} run · {total - run_n} not yet run.**", "",
        "| Skill | Status | Baseline | With skill | Last run |",
        "|---|---|---|---|---|",
    ]
    DASHBOARD.write_text("\n".join(header + rows) + "\n", encoding="utf-8")
    print(f"\nDashboard: {verified_n} verified, {run_n}/{total} run → {DASHBOARD.relative_to(ROOT)}")


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("skills", nargs="*", help="skill dirs (default: all)")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--judge-model", default=DEFAULT_JUDGE)
    ap.add_argument("--dashboard-only", action="store_true",
                    help="just regenerate EVALS.md from existing results.json files")
    args = ap.parse_args(argv)

    if args.dashboard_only:
        regenerate_dashboard(); return 0

    targets = [Path(s).resolve() for s in args.skills] or discover_skills()
    for sd in targets:
        run_skill(sd, args.model, args.judge_model)
    regenerate_dashboard()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
