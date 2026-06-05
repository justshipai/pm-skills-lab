# Example: pre-mortem

## Input

> We're about to spend a quarter rebuilding our mobile app from scratch in a new
> framework to "modernize" it. Run a pre-mortem.

## Output

# Mobile Rewrite — Pre-mortem

## The scene
It's six months from now. We shipped the rewrite, and it was a disaster — ratings dropped, the team is demoralized, and we're slower than before. What happened? (Success was meant to be: feature parity, better performance, faster future development — with no user disruption.)

## Failure modes
| Risk (how it killed us) | Type | Likelihood | Impact | Mitigation | Owner | Early warning |
|---|---|---|---|---|---|---|
| Rewrite hit feature parity far later than planned; months with no new features | Tiger | High | High | Incremental migration screen-by-screen, not big-bang; parity checklist | Eng lead | Burn-down stalls 2 sprints |
| Reintroduced bugs users had long since stopped reporting | Tiger | High | Med | Port the test suite first; beta cohort before full release | QA | Beta crash/bug rate vs. old app |
| Nobody actually owns "why are we doing this?" — it's resume-driven | **Elephant** | Med | High | Tie the rewrite to a concrete user/business outcome or don't do it | PM + Eng dir | Can't state the user benefit in one line |
| New framework's talent pool is thin; bus-factor of 1 | **Elephant** | Med | High | Pair/spread knowledge; confirm hiring market before committing | Eng manager | Only one engineer can debug it |
| App store rejects the rebuilt app | Paper Tiger | Low | Med | (dismiss — same APIs, standard submission) | — | — |
| Users hate the "new look" | Paper Tiger | Low | Low | (dismiss — we're not redesigning UX, just the framework) | — | — |

## Top risks to act on now
1. **Parity slip / feature freeze (Tiger)** — go incremental, not big-bang. This is the classic rewrite killer.
2. **The two Elephants** — *why* are we doing this, and the single-point-of-failure talent risk. If we can't answer the "why" in one user-benefit sentence, that's a stop signal.

## Paper Tigers (stop worrying about these)
App-store rejection and "users hate the new look" — neither is real here; don't spend the meeting on them.

## Watch list
Beta cohort crash/bug rate vs. the current app — if it's worse at 50% parity, pause the ramp.
