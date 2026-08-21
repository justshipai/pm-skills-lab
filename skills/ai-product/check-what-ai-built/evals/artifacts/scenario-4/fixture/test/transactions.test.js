const test = require('node:test');
const assert = require('node:assert/strict');
const { filterTransactions } = require('../src/transactions');
const { exportTransactions } = require('../src/exportTransactions');

test('filters transactions by status', () => {
  const rows = [{ id: '1', status: 'paid', date: '2026-08-01' }, { id: '2', status: 'failed', date: '2026-08-02' }];
  assert.deepEqual(filterTransactions(rows, { status: 'paid' }).map(x => x.id), ['1']);
});

const rows = [
  { id: '1', status: 'paid', date: '2026-08-01', description: 'Standard' },
  { id: '2', status: 'failed', date: '2026-08-02', description: 'Needs, review' },
  { id: '3', status: 'paid', date: '2026-09-01', description: 'Said "hello"' },
  { id: '4', status: 'paid', date: '2026-09-02', description: '=IMPORTDATA("bad")' }
];

test('exports only transactions matching active status and date filters', () => {
  const csv = exportTransactions({ role: 'admin' }, rows, { status: 'paid', to: '2026-08-31' });
  assert.equal(csv, 'id,date,status,description\n1,2026-08-01,paid,Standard');
});

test('members cannot export', () => {
  assert.throws(() => exportTransactions({ role: 'member' }, rows, {}), /forbidden/);
});

test('escapes commas, quotes and formula values', () => {
  const csv = exportTransactions({ role: 'admin' }, rows, {});
  assert.match(csv, /"Needs, review"/);
  assert.match(csv, /"Said ""hello"""/);
  assert.match(csv, /"'=IMPORTDATA\(""bad""\)"/);
});

test('neutralises control-prefixed formulas and quotes carriage returns', () => {
  const csv = exportTransactions(
    { role: 'admin' },
    [
      { id: '5', status: 'paid', date: '2026-09-03', description: '\t=1+1' },
      { id: '6', status: 'paid', date: '2026-09-04', description: 'left\rright' }
    ],
    {}
  );
  assert.match(csv, /"'\t=1\+1"/);
  assert.match(csv, /"left\rright"/);
});

test('returns headers when no rows match', () => {
  assert.equal(
    exportTransactions({ role: 'admin' }, rows, { status: 'refunded' }),
    'id,date,status,description'
  );
});
