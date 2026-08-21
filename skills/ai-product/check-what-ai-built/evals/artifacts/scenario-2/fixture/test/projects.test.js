const test = require('node:test');
const assert = require('node:assert/strict');
const { createProject, archiveProject, restoreProject, visibleProjects } = require('../src/projects');

test('creates a project', () => {
  assert.deepEqual(createProject('p1', 'Alpha'), { id: 'p1', name: 'Alpha', archivedAt: null });
});

test('archives and restores a newly created project', () => {
  const project = createProject('p1', 'Alpha');
  const archived = archiveProject(project);
  assert.deepEqual(visibleProjects([archived]), []);
  assert.deepEqual(visibleProjects([restoreProject(archived)]).map(x => x.id), ['p1']);
});
