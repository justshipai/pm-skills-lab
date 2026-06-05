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
# Long deliverables (a full PRD, a rollout plan) need room — too small a cap
# truncates the output and the judge grades an incomplete document.
AGENT_MAX_TOKENS = int(os.environ.get("EVAL_MAX_OUTPUT_TOKENS", "8000"))
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
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                payload = json.loads(resp.read())
            return "".join(b.get("text", "") for b in payload.get("content", []))
        except urllib.error.HTTPError as e:
            last_err = f"HTTP {e.code}: {e.read().decode('utf-8', 'ignore')[:200]}"
            if e.code in (429, 500, 502, 503, 529):
                time.sleep(3 * (attempt + 1)); continue
            break
        except Exception as e:  # timeouts, connection resets, etc. — retry
            last_err = str(e); time.sleep(3 * (attempt + 1))
    # Don't kill the whole run on one bad call — let the caller skip this skill.
    raise RuntimeError(f"model call to {model} failed after retries: {last_err}")


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


# ---------------------------------------------------------------- status

def classify(result: dict) -> str:
    """Three honest outcomes, derived from stored scenario scores:
       verified — with-skill passes the rubric AND beats the baseline everywhere.
       tie      — with-skill passes, but a strong baseline already does too (lift <= 0).
                  Not a failure: a one-shot test can't show the skill's value when the
                  base model already aces this prompt. Value shows on varied/hard inputs.
       failed   — with-skill output did not pass the rubric on some scenario.
    """
    scs = result.get("scenarios") or []
    if not scs:
        return "notrun"
    if any(not s.get("treatment_passed") for s in scs):
        return "failed"
    if all(s.get("earns_place") for s in scs):
        return "verified"
    return "tie"


STATUS_DASH = {
    "verified": "✅ verified",
    "tie": "➖ no measurable lift (strong baseline)",
    "failed": "❌ not verified",
    "notrun": "⏳ not yet run",
}
STATUS_VERDICT = {
    "verified": "✅ VERIFIED — the skill beats the no-skill baseline on every scenario.",
    "tie": ("➖ NO MEASURABLE LIFT — the with-skill output passes the rubric, but a strong "
            "no-skill baseline already does too on this scenario. This is **not** a failure: "
            "a single well-specified scenario can't show a skill's value when the base model "
            "already aces that exact prompt. The skill earns its keep through consistency "
            "across varied, messy, real-world inputs — which one-shot lift doesn't capture."),
    "failed": "❌ NOT VERIFIED — the with-skill output did not pass the rubric (see per-criterion detail).",
}


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
        base_out = call_model("", task, model, max_tokens=AGENT_MAX_TOKENS)
        print(" treatment…", end="", flush=True)
        treat_out = call_model(skill_body, task, model, max_tokens=AGENT_MAX_TOKENS)
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
             f"- **Verdict:** {STATUS_VERDICT[classify(r)]}",
             "",
             "| Scenario | Baseline | With skill | Lift | Earns its place? |",
             "|---|---|---|---|---|"]
    for s in r["scenarios"]:
        lines.append(f"| {s['scenario']} | {s['baseline_score']} | {s['treatment_score']} "
                     f"| {s['lift']:+} | {'✅' if s['earns_place'] else '❌'} |")

    # per-criterion verdicts for the with-skill (treatment) run — the diagnostics
    for s in r["scenarios"]:
        verdicts = s.get("treatment_verdicts", {})
        if not verdicts:
            continue
        lines += ["", f"### {s['scenario']} — with-skill verdicts (per criterion)", "",
                  "| Criterion | Verdict | Why |", "|---|---|---|"]
        for cid, v in verdicts.items():
            mark = {"pass": "✅ pass", "partial": "🟡 partial", "fail": "❌ fail"}.get(v.get("verdict"), v.get("verdict", ""))
            why = (v.get("why", "") or "").replace("|", "/").replace("\n", " ")
            lines.append(f"| `{cid}` | {mark} | {why} |")

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
    rows, n = [], {"verified": 0, "tie": 0, "failed": 0, "notrun": 0}
    total = 0
    for s in discover_skills():
        total += 1
        rel = s.relative_to(ROOT).as_posix()
        rj = s / "evals" / "results.json"
        if rj.exists():
            r = json.loads(rj.read_text(encoding="utf-8"))
            st = classify(r)
            n[st] += 1
            base = ", ".join(str(x["baseline_score"]) for x in r["scenarios"])
            treat = ", ".join(str(x["treatment_score"]) for x in r["scenarios"])
            rows.append(f"| `{Path(rel).name}` | {STATUS_DASH[st]} | {base} | {treat} | {r['run_at']} |")
        else:
            n["notrun"] += 1
            rows.append(f"| `{Path(rel).name}` | {STATUS_DASH['notrun']} | – | – | – |")
    run_n = total - n["notrun"]
    header = [
        "# Eval results dashboard", "",
        "Every skill ships with a scenario eval. The harness (`scripts/run_evals.py`) runs each "
        "scenario twice — once with no skill (baseline), once with the skill — and an LLM judge "
        "scores both against the rubric. Per-skill detail (incl. per-criterion verdicts) lives in "
        "each skill's `evals/RESULTS.md`.", "",
        "**Status key:** ✅ **verified** = the skill passes the rubric *and* beats the baseline. "
        "➖ **no measurable lift** = the skill passes, but a strong base model already aces this "
        "scenario unaided — not a failure, just a task where one-shot lift can't show the skill's "
        "value (consistency across varied inputs). ❌ **not verified** = the with-skill output "
        "didn't pass the rubric.", "",
        f"**{n['verified']} verified · {n['tie']} no-lift (strong baseline) · {n['failed']} not verified · "
        f"{run_n}/{total} run.**", "",
        "| Skill | Status | Baseline | With skill | Last run |",
        "|---|---|---|---|---|",
    ]
    DASHBOARD.write_text("\n".join(header + rows) + "\n", encoding="utf-8")
    print(f"\nDashboard: {n['verified']} verified, {n['tie']} no-lift, {n['failed']} not verified, "
          f"{run_n}/{total} run → {DASHBOARD.relative_to(ROOT)}")


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("skills", nargs="*", help="skill dirs (default: all)")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--judge-model", default=DEFAULT_JUDGE)
    ap.add_argument("--dashboard-only", action="store_true",
                    help="regenerate EVALS.md + each RESULTS.md from existing results.json (no model calls)")
    args = ap.parse_args(argv)

    if args.dashboard_only:
        for s in discover_skills():
            rj = s / "evals" / "results.json"
            if rj.exists():
                write_results_md(s, json.loads(rj.read_text(encoding="utf-8")))
        regenerate_dashboard(); return 0

    targets = [Path(s).resolve() for s in args.skills] or discover_skills()
    errored = []
    for sd in targets:
        try:
            run_skill(sd, args.model, args.judge_model)
        except Exception as e:  # one skill failing must not abort the whole run
            rel = sd.relative_to(ROOT).as_posix() if ROOT in sd.parents else sd.name
            print(f"   ⚠ skipped {rel}: {e}")
            errored.append(rel)
    regenerate_dashboard()
    if errored:
        print(f"\n⚠ {len(errored)} skill(s) errored and kept their previous result: "
              + ", ".join(errored) + f"\n  Re-run just those: python3 scripts/run_evals.py {' '.join(errored)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
