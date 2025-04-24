from typing import Type, TypeVar, Union


T = TypeVar("T")


def get_filtered_transactions(
        data: list[dict[str, Union[str, float]]],
        t_type: str,
        date: str) -> list[dict[str, Union[str, float]]]:
    return [tx for tx in data if tx["type"] == t_type and tx["date"] == date]


def calculate_totals(
        data: list[dict[str, Union[str, float]]],
        date: str) -> tuple[float, float, float]:
    incomes = get_filtered_transactions(data, "income", date)
    expenses = get_filtered_transactions(data, "expense", date)
    total_income = sum(tx["amount"] for tx in incomes)
    total_expense = sum(tx["amount"] for tx in expenses)
    balance = round(total_income - total_expense, 2)
    return total_income, total_expense, balance


def get_transaction_input(prompt: str, t_type: Type[T] = str) -> T:
    while True:
        try:
            result_value = input(prompt).strip()
            return t_type(result_value)
        except ValueError:
            print(
                f"Invalid input: '{result_value}', "
                f"expected value of type '{t_type.__name__}'"
            )
            continue


def add_transaction(
        data: list[dict[str, Union[str, float]]],
        date: str,
        t_type: str) -> tuple[dict[str, Union[str, float]], str]:
    amount = get_transaction_input(f"Enter {t_type} amount: ", float)
    comment = get_transaction_input(
        f"Enter {t_type} comment (can contain spaces): "
    )
    transaction = {
        "date": date,
        "type": t_type,
        "amount": amount,
        "comment": comment
    }

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
