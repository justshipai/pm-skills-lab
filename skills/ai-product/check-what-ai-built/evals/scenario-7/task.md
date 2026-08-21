# Review an AI-built feature

A founder asked an AI coding agent:

> Add a share button to the revenue dashboard.

No further requirements were supplied.

Available implementation evidence:

- The preview shows a Share button that creates a public link requiring no sign-in.
- The shared page exposes customer names, deal values and monthly revenue.
- Links do not expire and cannot be revoked. Search engines are blocked through `noindex`, but anyone with the URL can open it.
- The pull request adds a public dashboard endpoint and token generator. It includes a happy-path test that the URL renders.
- The founder has not said whether sharing should be public, workspace-restricted or limited to selected metrics.

Produce a concise, evidence-backed acceptance review for the founder and make a clear ship decision.
