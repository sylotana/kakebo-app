from typing import Type, TypeVar, Callable

from .validators import is_positive_number, is_non_empty_string
from models.transaction import Transaction


T = TypeVar("T")


def get_filtered_transactions(
        data: list[Transaction],
        date: str,
        t_type: str) -> list[Transaction]:
    return [tx for tx in data if tx.t_type == t_type and tx.date == date]


def calculate_totals(
        data: list[Transaction],
        date: str) -> tuple[float, float, float]:
    incomes = get_filtered_transactions(data, date, "income")
    expenses = get_filtered_transactions(data, date, "expense")
    total_income = sum(tx.amount for tx in incomes)
    total_expense = sum(tx.amount for tx in expenses)
    balance = round(total_income - total_expense, 2)
    return total_income, total_expense, balance


def get_transaction_input(
        prompt: str,
        cast_type: Type[T] = str,
        validator: Callable[[str], bool] | None = None,
        error_message: str = "Invalid input.") -> T:
    while True:
        try:
            user_input = input(prompt).strip()
            if validator and not validator(user_input):
                raise ValueError(error_message)
            return cast_type(user_input)
        except ValueError as e:
            print(e)


def add_transaction(
        data: list[Transaction],
        date: str,
        t_type: str) -> tuple[Transaction, str]:
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

    transaction = Transaction(
        date=date,
        t_type=t_type,
        amount=amount,
        comment=comment
    )

    data.append(transaction)
    totals = calculate_totals(data, date)

    if t_type == "income":
        total = totals[0]  # total_income
    else:
        total = totals[1]  # total_expense

    result_line = f"Current total {t_type}s: {total} (+{amount})."

    return transaction, result_line


def get_date() -> str:
    while not bool(date := input(
        "Enter a today's date in the format: <dd-mm-yyyy>: "
    )):
        pass

    return date
