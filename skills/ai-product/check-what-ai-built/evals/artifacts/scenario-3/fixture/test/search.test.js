const test = require('node:test');
const assert = require('node:assert/strict');
const { searchDocuments, clearCache } = require('../src/search');
const { openResult } = require('../src/searchNavigation');

test('searches documents in the current workspace', () => {
  clearCache();
  const docs = [
    { id: '1', workspaceId: 'beacon', title: 'Renewal plan' },
    { id: '2', workspaceId: 'acme', title: 'Renewal forecast' }
  ];
  assert.deepEqual(searchDocuments(docs, 'beacon', 'renewal').map(x => x.id), ['1']);
});

test('opening a result records the previous search state', () => {
  const state = { page: 'search', query: 'renewal', type: 'documents' };
  assert.deepEqual(openResult(state, '1').previous, state);
});
