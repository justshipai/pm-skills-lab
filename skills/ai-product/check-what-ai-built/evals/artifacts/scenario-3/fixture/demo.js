const { searchDocuments, clearCache } = require('./src/search');

const documents = [
  { id: 'b1', workspaceId: 'beacon', title: 'Renewal plan' },
  { id: 'a1', workspaceId: 'acme', title: 'Renewal forecast' }
];

clearCache();
console.log('Beacon:', searchDocuments(documents, 'beacon', 'renewal'));
console.log('Acme:', searchDocuments(documents, 'acme', 'renewal'));
