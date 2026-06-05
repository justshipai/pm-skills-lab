---
name: accessibility-audit
description: Use when checking a screen, component, or prototype for accessibility — a quick WCAG-based a11y audit. Produces a structured review across the high-impact accessibility areas (contrast, keyboard, focus, labels/semantics, target size, motion, content structure), each issue tied to a WCAG criterion with a severity and a concrete fix — not "add alt text" and a vibe.
---

# Accessibility audit

Accessibility gets reduced to "add alt text" and forgotten — then the product is unusable for keyboard and screen-reader users, and (increasingly) legally exposed. This skill runs a quick, practical audit against the **high-impact WCAG areas**, names the specific criterion each issue violates, rates it, and gives the concrete fix. Especially useful on AI-generated prototypes (Bolt/v0 output is often inaccessible by default — no focus states, poor contrast, div-soup).

## The areas to check (high-impact WCAG)

- **Color contrast** — text and meaningful UI vs. background (WCAG 1.4.3 / 1.4.11; 4.5:1 normal text, 3:1 large/UI).
- **Keyboard operability** — everything usable without a mouse; logical tab order; no traps (2.1.1, 2.1.2).
- **Visible focus** — a clear focus indicator on every interactive element (2.4.7). (AI-generated UIs routinely strip this.)
- **Names, roles, labels** — inputs have labels; buttons/icons have accessible names; correct semantics/ARIA (1.1.1, 4.1.2, 3.3.2).
- **Don't rely on color alone** — status/errors also use text/icon, not just red/green (1.4.1).
- **Target size & spacing** — tap targets large enough (2.5.8; ~24–44px).
- **Motion & autoplay** — respect reduced-motion; no unstoppable movement (2.3.3, 2.2.2).
- **Structure & reading order** — headings/landmarks; meaningful order; lang set (1.3.1, 2.4.6).
- **Forms & errors** — errors identified in text and associated with the field (3.3.1).

## The judgment this skill encodes

- **Be specific and criterion-based.** Cite the WCAG area/criterion and the actual problem ("icon-only buttons have no accessible name → screen readers announce 'button'"), not "improve accessibility."
- **Cover keyboard and focus, always.** The most common and most ignored failures. A mouse-only UI is broken for many users.
- **Severity = how much it blocks.** Blocker (can't use it) > major > minor. A missing focus ring blocks keyboard users → high.
- **Concrete, implementable fixes.** "Add `aria-label="Delete"` to the trash icon button"; "raise text from #999 on #fff (2.8:1) to at least #767676 (4.5:1)."
- **Color alone is a classic miss.** Check that errors/status don't rely solely on color.
- **Note what you can't assess statically.** Some checks need the running UI or a screen reader — flag those as "verify in-app" rather than guessing.

## Process

1. **Context** — what the surface is and its interactive elements.
2. **Walk the high-impact areas** — note pass or the specific violation + WCAG criterion.
3. **Rate severity** (blocker / major / minor).
4. **Give the concrete fix** per issue.
5. **Flag verify-in-app** items that need the live UI / a screen reader.

## Output format

```
# <Screen/Component> — Accessibility Audit (WCAG)

## Context
## Findings
   | Area / WCAG | Issue (or ✓) | Severity | Fix |
   (contrast · keyboard · focus · names/labels · color-only · target size · motion · structure · forms)
## Blockers to fix first
## Verify in-app          (needs the running UI / screen reader)
```

## Anti-patterns to refuse

- "Add alt text" as the whole audit → Cover keyboard, focus, contrast, labels, semantics.
- Vague advice with no criterion → Cite the WCAG area and the specific problem.
- No severity → Mark blockers vs. minor.
- Hand-wavy fixes → Give the concrete change (the aria attribute, the contrast value).
- Pretending to assess things that need the live app → Flag them as verify-in-app.
