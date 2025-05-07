import os
import json
from datetime import datetime

from models.transaction import Transaction

DIR = "./storage/"

if not os.path.exists(DIR):
    os.makedirs(DIR)


def get_filename_by_date(date_str: str) -> str:
    """Convert a date string to a filename based on year and month.

    Args:
        date_str (str): Date string in the format "dd-mm-yyyy".

    Returns:
        str: Filename in the format "yyyy-mm.json"
    """
    date = datetime.strptime(date_str, "%d-%m-%Y").date()
    return date.strftime("%Y-%m") + ".json"


def load_data(date: str) -> list[Transaction]:
    """Load transaction data from JSON file by date.

    Args:
        date (str): Date string in the format "dd-mm-yyyy".

    Returns:
        list[Transaction]: List of Transaction objects.
    """
    file_name = f"{DIR}{get_filename_by_date(date)}"
    try:
        data = []
        with open(file_name, "r", encoding="utf-8") as f:
            transactions = json.load(f)
            for tx in transactions:
                data.append(Transaction(**tx))
        return data
    except (IOError, json.JSONDecodeError):
        return []


def save_data(tx: Transaction) -> None:
    """Save transaction to a JSON file by date.

    Args:
        tx (Transaction): Transaction object to be saved.

    Returns:
        None
    """
    file_name = f"{DIR}{get_filename_by_date(tx.date)}"
    try:
        transactions = load_data(tx.date)  # Load existing transactions
        transactions.append(tx)  # Add the new transaction

        with open(file_name, "w", encoding="utf-8") as f:
            # Save transactions list as JSON
            json.dump(
                [tx.__dict__ for tx in transactions],
                f,
                ensure_ascii=False,
                indent=4
            )
    except IOError as e:
        print(e)
