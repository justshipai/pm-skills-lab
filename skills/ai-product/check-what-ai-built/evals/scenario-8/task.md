# Review an AI-built feature

A product manager asked an AI coding agent to replace an unsupported date picker without changing product behaviour.

The request was:

> Replace the deprecated booking date picker with the supported component. Preserve date ranges, disabled dates, locale formatting, keyboard behaviour, mobile layout and the existing UTC storage format.

Available implementation evidence:

- The pull request changes 914 lines. Most are generated snapshots and localisation fixtures from the supported component.
- Side-by-side preview checks pass for single dates, ranges, disabled dates, four locales, month boundaries and mobile layouts.
- Keyboard-only testing confirms focus order, arrow navigation, selection and escape behaviour.
- Integration tests confirm the same UTC values are submitted across DST boundaries. Existing booking-edit and cancellation tests pass.
- The old date-picker dependency is removed and no new unapproved dependency is introduced.
- The diff contains no changes to booking rules, APIs, permissions, billing or database schemas.

Produce a concise, evidence-backed acceptance review for the product manager and make a clear ship decision.
