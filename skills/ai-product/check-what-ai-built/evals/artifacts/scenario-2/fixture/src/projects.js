function createProject(id, name) {
  return { id, name, archivedAt: null };
}

function archiveProject(project, now = '2026-08-21T00:00:00Z') {
  return { ...project, archivedAt: now };
}

function restoreProject(project) {
  return { ...project, archivedAt: null };
}

function visibleProjects(projects) {
  return projects.filter(project => !project.archivedAt);
}

module.exports = { createProject, archiveProject, restoreProject, visibleProjects };
