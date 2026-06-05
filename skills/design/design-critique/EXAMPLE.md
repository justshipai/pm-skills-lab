# Example: design-critique

## Input

> Critique this pricing page mockup: a 3-column plan comparison (Free / Pro /
> Business), each with a feature list and a "Choose plan" button. Goal is to get
> more visitors to start a Pro trial. All three buttons look identical; the
> feature lists are long and identical-looking; Business is on the right.

## Output

# Pricing Page — Critique

## Goal & user
Goal: **drive more Pro trials.** User: a visitor deciding which plan to pick. So the design should make Pro the obvious, easy choice and reduce comparison effort.

## What works (keep)
- Clear 3-tier structure is conventional and scannable — keep the familiar layout.
- Per-plan CTA on each column (not one shared button) — good.

## Findings
| Dimension | Observation | Priority | Specific change |
|---|---|---|---|
| Goal/flow | Nothing steers the eye to Pro — all three plans have equal visual weight, so the design doesn't serve its own goal | **Must-fix** | Make Pro the visual hero: highlight border, "Most popular" badge, slightly larger card |
| Hierarchy | All three "Choose plan" buttons are identical filled buttons | **Must-fix** | Only Pro's button is filled/primary; Free and Business become outline/secondary |
| Usability | Long, identical-looking feature lists force the user to diff them line-by-line | Should-fix | Show only differences + a "what's different" emphasis; collapse the shared baseline |
| Content | "Choose plan" is generic | Should-fix | Pro CTA: "Start free Pro trial"; reduces commitment fear, matches the goal |
| States | No annual/monthly toggle or "no card required" reassurance shown | Should-fix | Add billing toggle + trust line ("No credit card for trial") near Pro |
| Visual | Business on the far right can anchor attention away from Pro | Polish | Consider Pro center (it already is) and ensure Business doesn't out-shout it |
| Accessibility | Plan differences likely conveyed by layout/color only | Polish | Ensure the "popular" status isn't color-only; check contrast on badges |

## Top 3 to address first
1. **Make Pro the visual hero** (badge + emphasis) — the page currently doesn't push its own goal.
2. **Differentiate the CTAs** — only Pro is primary; change its label to "Start free Pro trial."
3. **Cut comparison effort** — surface differences, not three long identical lists.

## Open questions
- Is there a free trial on Pro specifically, and is a card required? (Changes the CTA + reassurance copy.)
- Is annual pricing in scope? (Affects whether to add the toggle now.)
