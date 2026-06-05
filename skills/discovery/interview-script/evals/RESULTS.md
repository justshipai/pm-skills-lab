# Eval results — `interview-script`

- **Run:** 2026-06-05 11:32 UTC
- **Model under test:** claude-sonnet-4-6  ·  **Judge:** claude-sonnet-4-6
- **Verdict:** ✅ VERIFIED — the skill beats the no-skill baseline on every scenario.

| Scenario | Baseline | With skill | Lift | Earns its place? |
|---|---|---|---|---|
| scenario-1 | 0.682 | 1.0 | +0.318 | ✅ |

### scenario-1 — with-skill verdicts (per criterion)

| Criterion | Verdict | Why |
|---|---|---|
| `past-behavior-anchored` | ✅ pass | The core of the interview is anchored to specific recent instances ('think back to the last time…', 'walk me through that day'). Questions 3-9 all ask about what actually happened in that specific episode, not opinions or hypotheticals. |
| `non-leading` | ✅ pass | Questions are open-ended and chronological. The script explicitly lists phrases to avoid ('would you use something that…', 'do you wish your email could just…', 'how often do you feel overwhelmed') and warns interviewers against nodding or confirming hypotheses. No questions smuggle in the proposed solution. |
| `stated-learning-goal` | ✅ pass | The script opens with an explicit 'Learning goal' section stating the decision it informs (whether to build AI auto-reply) and four specific things to learn. The questions clearly ladder to those goals. |
| `probes` | ✅ pass | A dedicated probes table maps specific interview moments to follow-up questions. Standard follow-ups ('what happened next?', 'why did that matter?') are provided as a back-pocket list. The instruction to use probes throughout rather than at the end is explicit. |
| `no-pitching` | ✅ pass | Solution reactions are explicitly fenced to a final section with a warning not to introduce it early. The script prohibits describing the feature before asking, bans AI/auto/draft vocabulary until that section, and states clearly the interview is not validating a solution. |
| `workarounds-and-emotion` | ✅ pass | Question 8 directly asks about workarounds. The probe table includes rows for strong emotion ('say more about that') and workarounds ('how long have you been doing it that way?'). Interviewer notes explicitly flag workarounds as 'clearest signal about real pain' and ask who they feel accountable to. |

_Baseline = the task with no skill. With skill = the same task and model, SKILL.md supplied as the system prompt. Scores are the weighted fraction of the scenario's `criteria.json` rubric, graded by an LLM judge. Reproduce with `python3 scripts/run_evals.py skills/discovery/interview-script`._
