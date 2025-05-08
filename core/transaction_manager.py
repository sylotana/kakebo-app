from models.transaction import Transaction
from validators import is_positive_number, is_non_empty_string
from storage.transaction_storage import TransactionStorage
from ui import get_transaction_input


class TransactionManager:
    def __init__(self, repository: TransactionStorage, date: str):
        self.repository = repository
        self.date = date

    def get_transaction_data(self, t_type: str) -> tuple[float, str]:
        """Get data for a transaction from the user."""
        amount = get_transaction_input(
            f"Enter {t_type} amount: ",
            float,
            validator=is_positive_number,
            error_message="Amount must be a positive number."
        )
        comment = get_transaction_input(
            f"Enter {t_type} comment (can contain spaces): ",
            str,
            validator=is_non_empty_string,
            error_message="Comment cannot be empty."
        )
        return amount, comment

    def create_transaction(
            self,
            t_type: str,
            amount: float,
            comment: str) -> Transaction:
        """Create a new transaction object."""
        return Transaction(
            date=self.date,
            t_type=t_type,
            amount=amount,
            comment=comment
        )

    def add_transaction(self, transaction: Transaction) -> None:
        """Add a transaction to the storage."""
        self.repository.save_data(transaction)


def process_transaction(
        t_type: str,
        manager: TransactionManager) -> tuple[Transaction, str]:
    """Get data from user, create transaction, and add it to storage."""
    amount, comment = manager.get_transaction_data(t_type)
    transaction = manager.create_transaction(t_type, amount, comment)
    manager.add_transaction(transaction)
    return transaction, f"Transaction added: {transaction}"
