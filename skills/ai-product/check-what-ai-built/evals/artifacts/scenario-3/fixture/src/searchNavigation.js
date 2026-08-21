function openResult(state, resultId) {
  return { page: 'result', resultId, previous: state };
}

function returnToSearch(openedResult) {
  return { page: 'search', query: '', type: 'all' };
}

module.exports = { openResult, returnToSearch };
