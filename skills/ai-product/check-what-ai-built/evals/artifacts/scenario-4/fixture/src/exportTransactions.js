const { filterTransactions } = require('./transactions');

function csvCell(value) {
  const text = String(value ?? '');
  const spreadsheetSafe = /^[\t\r\n ]*[=+\-@]/.test(text) ? `'${text}` : text;
  return /[",\t\r\n]/.test(spreadsheetSafe)
    ? `"${spreadsheetSafe.replaceAll('"', '""')}"`
    : spreadsheetSafe;
}

function exportTransactions(actor, transactions, filters) {
  if (actor.role !== 'admin') throw new Error('forbidden');
  const columns = ['id', 'date', 'status', 'description'];
  const matching = filterTransactions(transactions, filters);
  const lines = matching.map(transaction => columns.map(column => csvCell(transaction[column])).join(','));
  return [columns.join(','), ...lines].join('\n');
}

module.exports = { csvCell, exportTransactions };
