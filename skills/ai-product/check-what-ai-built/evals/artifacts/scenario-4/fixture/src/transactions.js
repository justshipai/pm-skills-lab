function filterTransactions(transactions, filters) {
  return transactions.filter(transaction =>
    (!filters.status || transaction.status === filters.status) &&
    (!filters.from || transaction.date >= filters.from) &&
    (!filters.to || transaction.date <= filters.to)
  );
}

module.exports = { filterTransactions };
