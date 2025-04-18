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


while True:
    wait_text = "Press Enter to return to the menu."
    print("\nSelect a menu item:")
    print(*ui.menu(), sep="\n")

    choice = input("Select: ")

    # GET BALANCE
    if choice == "1":
        total_incomes, total_expenses, balance = calculate_totals(today_date)

        print(
            ui.divider(40, "="),
            f"Total balance: {balance}",
            f"Total income: {total_incomes}",
            f"Total expenses: {total_expenses}",
            ui.divider(40, "="),
            sep='\n'
        )
        wait_for_enter(wait_text)

    # ADD INCOME
    elif choice == "2":
        user_input = input("Enter income as <comment> <amount>: ")
        comment, amount = user_input.split()
        amount = float(amount)
        add_transaction(today_date, "income", amount, comment)

        total_incomes, _, _ = calculate_totals(today_date)

        print(
            ui.divider(40, "="),
            "Income added successfully.",
            f"Current total income: {total_incomes} (+{income}).",
            ui.divider(40, "="),
            sep="\n"
        )
        wait_for_enter(wait_text)

    # ADD EXPENSE
    elif choice == "3":
        user_input = input("Enter expense as <comment> <amount>: ")
        comment, amount = user_input.split()
        amount = float(amount)
        add_transaction(today_date, "expense", amount, comment)
        
        _, total_expenses, _ = calculate_totals(today_date)

        print(
            ui.divider(40, "="),
            "Expense added successfully.",
            f"Current total expenses: {total_expenses} (+{expense}).",
            ui.divider(40, "="),
            sep="\n"
        )
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
