# Review an AI-built feature

A product manager asked an AI coding agent to add bulk invitations.

The request was:

> Workspace admins can paste up to 50 email addresses, review invalid entries and send invitations. Members cannot invite users. Duplicate or existing members should not receive another invitation.

Available implementation evidence:

- The agent says the feature is complete and reports that all tests pass.
- The pull request, code diff, test output and preview are inaccessible.
- There are no screenshots, logs or independently observed behaviours.
- The agent's summary says it added a modal, validation and an invitation endpoint, but provides no evidence of authorisation, duplicate handling or the 50-address boundary.

Produce a concise, evidence-backed acceptance review for the product manager and make a clear ship decision.
