function canSeeBulkArchive(actor) {
  return actor.role === 'admin';
}

module.exports = { canSeeBulkArchive };
