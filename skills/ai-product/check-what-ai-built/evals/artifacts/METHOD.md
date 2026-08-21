# Artifact eval method

These scenarios test the full job: starting with a product brief and an AI-generated implementation, the agent must inspect the code, run useful checks, build its own evidence and make a ship decision.

Each scenario contains:

- `fixture/` — the implementation reviewed by candidate agents
- `feature.patch` — the exact AI-generated feature commit
- `criteria.json` — the hidden weighted rubric
- `baseline-output.md` — review without the skill
- `treatment-output.md` — review with the revised skill
- `capability.txt` — the capability under test

Run `node --test` inside a fixture to reproduce its visible test suite. The fixture intentionally does not contain its scoring rubric.
