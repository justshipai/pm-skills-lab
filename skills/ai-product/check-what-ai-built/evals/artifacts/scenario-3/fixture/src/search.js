const cache = new Map();

function searchDocuments(documents, workspaceId, query) {
  const cacheKey = query.toLowerCase();
  if (cache.has(cacheKey)) return cache.get(cacheKey);

  const results = documents.filter(document =>
    document.workspaceId === workspaceId &&
    document.title.toLowerCase().includes(query.toLowerCase())
  );
  cache.set(cacheKey, results);
  return results;
}

function clearCache() {
  cache.clear();
}

module.exports = { searchDocuments, clearCache };
