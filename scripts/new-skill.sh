#!/usr/bin/env bash
# Scaffold a new skill folder to the pm-skills-lab standard.
# Usage: ./scripts/new-skill.sh <category> <skill-name>
#   e.g. ./scripts/new-skill.sh ai-product ai-prd
set -euo pipefail

CATEGORY="${1:-}"
SKILL="${2:-}"

if [[ -z "$CATEGORY" || -z "$SKILL" ]]; then
  echo "Usage: $0 <category> <skill-name>"
  echo "Categories: ai-product, discovery, market, strategy, prioritization,"
  echo "            specs, design, data, gtm, growth, comms, people, meta"
  exit 1
fi

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$ROOT/skills/$CATEGORY/$SKILL"

if [[ -d "$DIR" ]]; then
  echo "Error: $DIR already exists."
  exit 1
fi

mkdir -p "$DIR/evals/scenario-1"

cat > "$DIR/SKILL.md" <<EOF
---
name: $SKILL
description: TODO — one or two sentences. Start with "Use when…" and name the trigger precisely. This is what makes the skill auto-fire, so be specific.
---

# $(echo "$SKILL" | tr '-' ' ')

## When to use
TODO — the situation this skill is for.

## What it does
TODO — step by step. Name the framework(s) it encodes.

## Process
1. TODO
2. TODO

## Output format
TODO — what the skill produces.
EOF

cat > "$DIR/EXAMPLE.md" <<EOF
# Example: $SKILL

## Input
TODO — a real, non-toy input.

## Output
TODO — the output the skill produces from that input.
EOF

cat > "$DIR/evals/scenario-1/task.md" <<EOF
TODO — the task brief an agent receives. Describe the job to be done.
Do NOT mention this skill by name; we test whether the skill helps an agent
that was simply asked to do the task.
EOF

cat > "$DIR/evals/scenario-1/capability.txt" <<EOF
TODO — one line naming the capability of the skill this scenario tests.
EOF

cat > "$DIR/evals/scenario-1/criteria.json" <<'EOF'
{
  "criteria": [
    {
      "id": "todo-criterion-1",
      "description": "TODO — a checkable property a good output must have.",
      "weight": 3,
      "required": true
    },
    {
      "id": "todo-criterion-2",
      "description": "TODO — another checkable property.",
      "weight": 2,
      "required": false
    }
  ],
  "pass_threshold": 0.7
}
EOF

echo "Scaffolded $DIR"
echo "Next: fill in SKILL.md, EXAMPLE.md, and evals/scenario-1/*, then run:"
echo "  python3 scripts/validate.py skills/$CATEGORY/$SKILL"
