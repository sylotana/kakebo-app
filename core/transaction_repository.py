import os
import json
from datetime import datetime

from models.transaction import Transaction


class TransactionRepository:
    DIR = "./data/"

    def __init__(self) -> None:
        if not os.path.exists(self.DIR):
            os.makedirs(self.DIR)

    def _get_filename_by_date(self, date_str: str) -> str:
        date = datetime.strptime(date_str, "%d-%m-%Y").date()
        return os.path.join(self.DIR, date.strftime("%Y-%m") + ".json")

    def load(self, date: str) -> list[Transaction]:
        file_name = self._get_filename_by_date(date)
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Transaction(**tx) for tx in data]
        except (IOError, json.JSONDecodeError):
            return []

    def save(self, tx: Transaction) -> None:
        transactions = self.load(tx.date)
        transactions.append(tx)

        file_name = self._get_filename_by_date(tx.date)
        try:
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(
                    [t.__dict__ for t in transactions],
                    f,
                    ensure_ascii=False,
                    indent=4
                )
        except IOError as e:
            print(f"Error saving transaction: {e}")
