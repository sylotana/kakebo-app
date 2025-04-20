WAIT_TEXT = "Press Enter to return to the menu."


def divider(count, sybmol="-"):
    return sybmol * count


def app_description():
    return (
        divider(40),
        "Budgetshell App for Tracking Expenses",
        divider(40)
    )


def menu():
    return (
        "(1) Get balance",
        "(2) Add income",
        "(3) Add expenses",
        "(4) Get incomes",
        "(5) Get expenses",
        "(6) Exit",
    )


def table():
    pass


def format_transaction(type, total, amount):
    return f"Current total {type}s: {total} (+{amount})."


def info(title, body_lines):
    print(divider(40, "="))
    print(title)
    print(*body_lines, sep="\n")
    print(divider(40, "="))


def transactions(transactions, title):
    if not transactions:
        print("No transactions to display.")
        return

    total = sum(tx["amount"] for tx in transactions)

    if title:
        print(title)

    print("+--------------------+------------------+")
    print("| Comment            | Amount           |")
    print("+--------------------+------------------+")

    for tx in transactions:
        print(f"| {tx['comment'].ljust(18)} | {str(tx['amount']).rjust(16)} |")

    print("+--------------------+------------------+")
    print(f"| {'TOTAL'.ljust(18)} | {str(total).rjust(16)} |")
    print("+--------------------+------------------+")
