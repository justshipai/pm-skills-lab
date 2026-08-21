function archiveProject(actor, project) {
  if (actor.role !== 'admin') throw new Error('forbidden');
  if (project.status === 'active') throw new Error('active_project');
  if (project.unpaidInvoice) throw new Error('unpaid_invoice');
  return { ...project, archivedAt: '2026-08-21T00:00:00Z' };
}

function bulkArchiveProjects(actor, projects, selectedIds, confirmed) {
  if (!confirmed) return projects;

  const selected = projects.filter(project => selectedIds.includes(project.id));
  if (selected.some(project => project.unpaidInvoice)) {
    throw new Error('unpaid_invoice');
  }

  const archivedAt = '2026-08-21T00:00:00Z';
  return projects.map(project =>
    selectedIds.includes(project.id) ? { ...project, archivedAt } : project
  );
}

module.exports = { archiveProject, bulkArchiveProjects };
