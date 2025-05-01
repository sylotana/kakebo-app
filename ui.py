from models.transaction import Transaction


def wait_for_user_input(message: str = "Press Enter to continue...") -> None:
    """Display a message and wait for the user to press Enter.

    Args:
        message (str): The message to display.
          Defaults to "Press Enter to continue...".

    Returns:
        None
    """
    input(f"\n{message}")


def divider(count: int, symbol: str = "-") -> str:
    return symbol * count


def app_description() -> tuple[str, ...]:
    return (
        divider(40),
        "Budgetshell App for Tracking Expenses",
        divider(40)
    )


def menu() -> tuple[str, ...]:
    return (
        "(1) Get balance",
        "(2) Add income",
        "(3) Add expenses",
        "(4) Get incomes",
        "(5) Get expenses",
        "(6) Exit",
    )


# This feature is currently not used in the project
def format_transaction(tx: Transaction, total: float) -> str:
    return f"Current total {tx.t_type}s: {total} (+{tx.amount})."


def info(title: str, body_lines: tuple[str, ...]) -> None:
    print(divider(40, "="))
    print(title)
    print(*body_lines, sep="\n")
    print(divider(40, "="))


def transactions(data: list[Transaction], title: str) -> None:
    if not data:
        print("No transactions to display.")
        return

    total = sum(tx.amount for tx in data)

    if title:
        print(title)

    print("+--------------------+------------------+")
    print("| Comment            | Amount           |")
    print("+--------------------+------------------+")

    for tx in data:
        print(f"| {tx.comment.ljust(18)} | {str(tx.amount).rjust(16)} |")

    print("+--------------------+------------------+")
    print(f"| {'TOTAL'.ljust(18)} | {str(total).rjust(16)} |")
    print("+--------------------+------------------+")
