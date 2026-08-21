# Review an AI-built feature

A product manager asked an AI coding tool to add bulk project archiving to a multi-tenant SaaS admin page.

The request was:

> Workspace admins can select several inactive projects and archive them after a confirmation step. Members must not be able to archive projects. Active projects and projects with unpaid invoices cannot be archived. Archiving must not delete data and the existing single-project restore flow must continue to work.

Available implementation evidence:

- The pull request adds multi-select controls, a confirmation modal, a bulk archive API endpoint and a database migration that changes `projects.archived_at` from nullable to non-null with a default timestamp.
- In the preview, an admin can select three inactive projects and archive them. The archived projects disappear from the default list.
- A member does not see the bulk action in the UI. No one has attempted to call the endpoint as a member.
- In the preview, selecting one active project and one inactive project results in both being archived.
- There is a unit test showing projects with unpaid invoices are rejected.
- CI is green. There are no integration or end-to-end tests for permissions, mixed selections, confirmation cancellation or restoring a project archived by the new bulk flow.
- The migration has no documented rollback and would assign an archive timestamp to every existing project.

Produce a concise, evidence-backed acceptance review for the product manager and make a clear ship decision.
