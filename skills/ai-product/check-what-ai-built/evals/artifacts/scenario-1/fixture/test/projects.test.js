const test = require('node:test');
const assert = require('node:assert/strict');
const { archiveProject, bulkArchiveProjects } = require('../src/projects');

test('an admin can archive an inactive project', () => {
  const project = { id: 'p1', status: 'inactive', unpaidInvoice: false };
  assert.ok(archiveProject({ role: 'admin' }, project).archivedAt);
});

test('a member cannot archive a project', () => {
  const project = { id: 'p1', status: 'inactive', unpaidInvoice: false };
  assert.throws(() => archiveProject({ role: 'member' }, project), /forbidden/);
});

test('an admin can bulk archive inactive projects after confirmation', () => {
  const projects = [
    { id: 'p1', status: 'inactive', unpaidInvoice: false, name: 'Alpha' },
    { id: 'p2', status: 'inactive', unpaidInvoice: false, name: 'Beta' }
  ];
  const result = bulkArchiveProjects({ role: 'admin' }, projects, ['p1', 'p2'], true);
  assert.ok(result.every(project => project.archivedAt));
  assert.equal(result[0].name, 'Alpha');
});

test('bulk archive rejects projects with unpaid invoices', () => {
  const projects = [{ id: 'p1', status: 'inactive', unpaidInvoice: true }];
  assert.throws(
    () => bulkArchiveProjects({ role: 'admin' }, projects, ['p1'], true),
    /unpaid_invoice/
  );
});
