# Review an AI-built feature

A product manager asked an AI coding agent to add notification preferences to account settings.

The request was:

> Let signed-in users turn product-update and marketing emails on or off. Transactional security and billing emails must remain enabled. Preferences must persist across sessions and apply only to the current user.

Available implementation evidence:

- The pull request adds two labelled toggles, a per-user preferences endpoint and two nullable preference columns. It does not change the transactional notification service.
- In the preview, a user disables both optional categories, refreshes and signs out and back in; both choices persist.
- A second user in the same workspace retains their original settings.
- Direct API calls attempting to disable `security` or `billing` return `400 unsupported_preference`.
- Focused integration tests cover persistence, tenant separation and rejection of transactional categories. An end-to-end test covers keyboard operation and refresh persistence.
- CI and accessibility checks pass. The diff contains no dependency, billing, permission or infrastructure changes.

Produce a concise, evidence-backed acceptance review for the product manager and make a clear ship decision.
