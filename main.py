import ui

print(*ui.app_description(), sep="\n")

while not bool(today_date := input(
    "Enter a today's date in the format: <dd-mm-yyyy>: "
)):
    pass

budget = []


def get_filtered_transactions(t_type, date):
    return [tx for tx in budget if tx["type"] == t_type and tx["date"] == date]


def calculate_totals(date):
    incomes = get_filtered_transactions("income", date)
    expenses = get_filtered_transactions("expense", date)
    total_income = sum(tx["amount"] for tx in incomes)
    total_expense = sum(tx["amount"] for tx in expenses)
    balance = round(total_income - total_expense, 2)
    return total_income, total_expense, balance


def wait_for_enter(text):
    input(text)


def print_transactions(transactions, title):
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


def add_transaction(date, type, amount, comment):
    budget.append({
        "date": date,
        "type": type,
        "amount": amount,
        "comment": comment
    })


def format_transaction(type, total, amount):
    return f"Current total {type}s: {total} (+{amount})."


def print_block(title, body_lines):
    print(ui.divider(40, "="))
    print(title)
    print(*body_lines, sep="\n")
    print(ui.divider(40, "="))


def get_transaction_input(prompt, t_type=str):
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


while True:
    wait_text = "Press Enter to return to the menu."
    print("\nSelect a menu item:")
    print(*ui.menu(), sep="\n")

    choice = input("Select: ")

    # GET BALANCE
    if choice == "1":
        total_incomes, total_expenses, balance = calculate_totals(today_date)

        print_block("Current Balance.", (
            f"Total balance: {balance}",
            f"Total income: {total_incomes}",
            f"Total expenses: {total_expenses}")
        )
        wait_for_enter(wait_text)

    # ADD INCOME
    elif choice == "2":
        amount = get_transaction_input("Enter income amount: ", float)
        comment = get_transaction_input(
            "Enter income comment (can contain spaces): "
        )
        add_transaction(today_date, "income", amount, comment)

        total_incomes, _, _ = calculate_totals(today_date)
        result_line = format_transaction("income", total_incomes, amount)

        print_block("Income added successfully.", (result_line,))
        wait_for_enter(wait_text)

    # ADD EXPENSE
    elif choice == "3":
        amount = get_transaction_input("Enter expense amount: ", float)
        comment = get_transaction_input(
            "Enter expense comment (can contain spaces): "
        )
        add_transaction(today_date, "expense", amount, comment)

        _, total_expenses, _ = calculate_totals(today_date)
        result_line = format_transaction("expense", total_expenses, amount)

        print_block("Expense added successfully.", (result_line,))
        wait_for_enter(wait_text)

    # GET INCOMES
    elif choice == "4":
        incomes = get_filtered_transactions("income", today_date)
        print_transactions(incomes, today_date)
        wait_for_enter(wait_text)

    # GET EXPENSES
    elif choice == "5":
        expenses = get_filtered_transactions("expense", today_date)
        print_transactions(expenses, today_date)
        wait_for_enter(wait_text)

    # EXIT
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Try again.")
