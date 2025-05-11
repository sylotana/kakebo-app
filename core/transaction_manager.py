from models.transaction import Transaction
from core.transaction_repository import TransactionRepository


class TransactionManager:
    def __init__(self, repository: TransactionRepository):
        self.repository = repository

    def add_transaction(self, transaction: Transaction) -> None:
        """Add a transaction to the storage."""
        self.repository.save_data(transaction)

    def get_total(self, date: str, t_type: str) -> float:
        """Calculate total income for a given date."""
        txs = self.repository.load(date)
        return sum(el.amount for el in txs if el.t_type == t_type)

    def get_balance(self, date: str) -> float:
        """Calculate balance for a given date."""
        total_income = self.get_total(date, "income")
        total_expense = self.get_total(date, "expense")
        return total_income - total_expense
