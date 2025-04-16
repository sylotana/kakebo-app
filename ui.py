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
