import os
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
        str: Filename in the format "yyyy-mm.txt"
    """
    date = datetime.strptime(date_str, "%d-%m-%Y").date()
    return date.strftime("%Y-%m") + ".txt"


def load_data(date: str) -> list[Transaction]:
    """Load transaction data from file by date.

    Args:
        date (str): Date string in the format "dd-mm-yyyy".

    Returns:
        list[Transaction]: List of transactions with keys:
          "date", "type", "amount", and "comment".
    """
    file_name = f"{DIR}{get_filename_by_date(date)}"
    try:
        data = []
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                values = line.strip().split(";")
                transaction = Transaction(
                    date=values[0],
                    t_type=values[1],
                    amount=float(values[2]),
                    comment=values[3]
                )
                data.append(transaction)

        return data
    except IOError as e:
        print(e)
        # to avoid returning `None`
        return []


def save_data(tx: Transaction) -> None:
    """Save transaction to file by date

    Args:
        tx (dict): Dictionary containing "date", "type",
          "amount", and "comment"

    Returns:
        None
    """
    file_name = f"{DIR}{get_filename_by_date(tx.date)}"
    try:
        with open(file_name, "a", encoding="utf-8") as f:
            result_line = f"{tx.date};{tx.t_type};{tx.amount};{tx.comment}"

            f.write(result_line + "\n")
    except IOError as e:
        print(e)
