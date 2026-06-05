# Example: roadmap-builder

## Input

> Turn this feature list into a roadmap for our B2B scheduling product:
> calendar sync v2, team availability view, Zoom integration, AI scheduling
> assistant, mobile app, SSO, reporting dashboard, customizable booking pages.
> Our goal this year is to move upmarket to mid-size teams.

## Output

# Scheduling Product — Roadmap (Now / Next / Later)

## Strategy this serves
**Move upmarket to mid-size teams.** That means winning on *team* coordination, security/compliance buyers expect, and reliability — not more solo-user features.

## Now (high confidence)
- **Teams can see and book across each other's availability** — candidate: team availability view + calendar sync v2 — moves: multi-seat activation, seats per account.
- **We clear the security bar for mid-size buyers** — candidate: SSO (SAML) — moves: deals lost to "no SSO" → 0; enterprise-tier conversion.

## Next (medium confidence)
- **Admins can prove the product's value** — candidate: reporting dashboard (utilization, no-shows) — moves: renewal/expansion in mid-size accounts.
- **Meetings happen where teams already work** — candidate: Zoom integration — moves: scheduled-meeting completion rate.

## Later (directional, low confidence)
- **Booking that scales to a whole org** — themes: customizable booking pages, role-based admin.
- **AI scheduling assistant** — a bet on reducing back-and-forth; revisit once team workflows are solid and we have usage data to ground it.
- **Mobile app** — only if data shows mid-size buyers need it; web-first for now.

## How to read this
**Now** is committed and specific. **Next** is our current best guess and will firm up as Now ships. **Later** is directional — themes and bets we'll validate, not promises. Confidence decreases left → right; don't read Later as scheduled.

## Dependencies / external dates
- SSO depends on the auth-service refactor (eng) — only hard dependency.
- No external date commitments except the SOC 2 audit window, which SSO supports.
