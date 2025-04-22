import os
from datetime import datetime
from typing import Union

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


def load_data(date: str) -> list[dict[str, Union[str, float]]]:
    """Load transaction data from file by date.

    Args:
        date (str): Date string in the format "dd-mm-yyyy".

    Returns:
        list[dict[str, Union[str, float]]]: List of transactions with keys:
          "date", "type", "amount", and "comment".
    """
    file_name = f"{DIR}{get_filename_by_date(date)}"
    try:
        data = []
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                values = line.strip().split(";")
                data.append({
                    "date": values[0],
                    "type": values[1],
                    "amount": float(values[2]),
                    "comment": values[3]
                })

        return data
    except IOError as e:
        print(e)


def save_data(info: dict[str, Union[str, float]]) -> None:
    """Save transaction to file by date

    Args:
        info (dict): Dictionary containing "date", "type",
          "amount", and "comment"

    Returns:
        None
    """
    file_name = f"{DIR}{get_filename_by_date(info['date'])}"
    try:
        with open(file_name, "a", encoding="utf-8") as f:
            result_line = ";".join(map(str, info.values()))

            f.write(result_line + "\n")
    except IOError as e:
        print(e)
