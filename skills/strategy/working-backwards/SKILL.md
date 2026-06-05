---
name: working-backwards
description: Use when pressure-testing or framing a product idea before building — writing an Amazon-style "working backwards" PR/FAQ. Produces a mock launch-day press release written for the customer plus a hard FAQ, forcing clarity on the customer, the problem, and the value before a line of code is written. Surfaces whether the idea is actually worth building.
---

# Working backwards (PR/FAQ)

Amazon's "working backwards" method: before you build anything, write the **press release you'd publish on launch day** — from the customer's point of view — and an **FAQ** that answers the hard questions. If you can't write a compelling, specific PR, the idea isn't ready. The discipline forces you to start from the customer and the value, not the feature, and exposes weak ideas cheaply.

## The judgment this skill encodes

- **Write it as if it already shipped.** Past tense, launch day. This forces concreteness — vague ideas can't survive a real headline.
- **Customer-obsessed, not company-obsessed.** The PR leads with the customer's problem and how their life is better — not your tech or your milestones. Quotes are from customers, not just execs.
- **Plain language, no jargon.** If the press release needs buzzwords to sound good, the idea is thin. Write so a normal person gets excited.
- **The FAQ is where honesty lives.** Answer the questions you'd rather avoid: Why will customers care? Why us? What's the hardest part? What could make this fail? What are we NOT doing? How do we make money? A PR with no tough FAQ is marketing, not thinking.
- **If the PR is boring, kill or reshape the idea.** The point isn't to produce a doc — it's to find out, cheaply, whether there's a there there. Say so if the PR comes out flat.
- **Quantify the customer benefit.** "Saves hours" → how many, for whom, vs. what today.

## Process

1. **Press release** — headline (the customer benefit), subhead, opening paragraph (the problem + the new reality), how it works in 2-3 plain sentences, a believable customer quote, a how-to-get-started line.
2. **Customer FAQ** — the practical questions a real customer would ask (cost, effort, trust, what it replaces).
3. **Internal/stakeholder FAQ** — the hard ones: why customers will care, why us, biggest risks, what we're explicitly not doing, how it makes money, what has to be true.
4. **Verdict** — is this PR compelling and specific? If it reads flat or generic, say what's missing or whether to drop it.

## Output format

```
# <Idea> — Working Backwards (PR/FAQ)

## PRESS RELEASE (launch day)
   ## <Headline: the customer benefit>
   *<Subhead>*
   <Opening: the problem, and the new reality>
   <How it works — plain language>
   "<Customer quote>"
   <How to get started>

## Customer FAQ
## Internal FAQ              (why care · why us · risks · non-goals · business model · what must be true)
## Verdict                   (compelling & specific? what's weak? build / reshape / drop)
```

## Anti-patterns to refuse

- A PR full of jargon/buzzwords → Rewrite in plain, specific language.
- Company-centric framing (our platform, our AI) → Lead with the customer's problem and benefit.
- An FAQ that dodges the hard questions → Force the uncomfortable ones (why us, what could fail, non-goals).
- Producing the doc while ignoring that the idea reads flat → State that honestly in the verdict.
