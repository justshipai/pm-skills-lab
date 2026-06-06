# Example: launch-tiering

## Input

> Marketing wants to do a huge launch — press release, webinar, paid campaign,
> launch event — for our new dark mode. Plan the launch.

## Output

# Dark Mode — Launch Tiering & Plan

## Assessment
- **Strategic importance:** low — it's a quality-of-life feature, not a strategic bet.
- **Audience:** broad (many users will like it) but it doesn't change what the product *does*.
- **Revenue/competitive:** ~none directly; table-stakes parity, not a differentiator.
- **Newsworthiness:** low — dark mode is expected; a press release would land flat (and risk looking out of touch).
- **Risk:** low.

## Tier
**T2 at most — likely T2-minus.** The proposed full motion (PR, webinar, paid campaign, event) is a **mismatch — tier it down.** A press release and launch event for dark mode spends scarce launch capital and audience attention on a parity feature, and can make the company look like it's celebrating catching up. Save the full motion for something strategic.

## Right-sized activities
- **In-app announcement** (a tasteful "Dark mode is here" toast/highlight — this is where most users will discover and delight in it).
- **Changelog + a short, fun blog/social post** (dark mode is very shareable visually — lean into the screenshots, not a corporate PR).
- **Email** to users (especially night-users, if you can segment).
- **Docs/help** update. Light support heads-up.
- **Skip:** press release, webinar, paid campaign, launch event.

## Owners & timeline
PM + design own the in-app moment; marketing owns the blog/social/email. ~1 week of light coordination, not a launch war room. No formal go/no-go needed (low risk) — just QA the toggle across themes.

## Risk overlay
Low risk; the only watch-item is rendering bugs in dark mode across screens — ship behind a setting so users can revert, and QA the `ui-states-matrix` of key screens in dark theme before the in-app push.

*Recommendation to marketing: bank the campaign energy for the next T1. Dark mode delights users in-product; it doesn't need a megaphone.*
