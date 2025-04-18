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


while True:
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
        input("Press Enter to return to the menu.")

    # ADD INCOME
    elif choice == "2":
        user_input = input("Enter income as <comment> <amount>: ")
        comment, income = user_input.split()
        income = float(income)

        budget.append({
            "date": today_date,
            "type": "income",
            "amount": income,
            "comment": comment
        })

        total_incomes, _, _ = calculate_totals(today_date)

        print(
            ui.divider(40, "="),
            "Income added successfully.",
            f"Current total income: {total_incomes} (+{income}).",
            ui.divider(40, "="),
            sep="\n"
        )
        input("Press Enter to return to the menu.")

    # ADD EXPENSE
    elif choice == "3":
        user_input = input("Enter expense as <comment> <amount>: ")
        comment, expense = user_input.split()
        expense = float(expense)

        budget.append({
            "date": today_date,
            "type": "expense",
            "amount": expense,
            "comment": comment
        })

        _, total_expenses, _ = calculate_totals(today_date)

        print(
            ui.divider(40, "="),
            "Expense added successfully.",
            f"Current total expenses: {total_expenses} (+{expense}).",
            ui.divider(40, "="),
            sep="\n"
        )
        input("Press Enter to return to the menu.")

    # GET INCOMES
    elif choice == "4":
        incomes = get_filtered_transactions("income", today_date)
        if budget_incomes:
            print(ui.divider(40))
            print(f"| {"TOTAL".ljust(18)}|{str(total_incomes).rjust(17)} |")
            print(ui.divider(40))
            for tx in incomes:
                print(
                    f"| {tx['comment'].ljust(18)}"
                    f"|{str(tx['amount']).rjust(17)} |"
                )
                print(ui.divider(40))
        else:
            print("The income list is empty.")

        input("Press Enter to return to the menu.")

    # GET EXPENSES
    elif choice == "5":
        expenses = get_filtered_transactions("expense", today_date)
        if budget_expenses:
            print(ui.divider(40))
            print(f"| {"TOTAL".ljust(18)}|{str(total_expenses).rjust(17)} |")
            print(ui.divider(40))
            for tx in expenses:
                print(
                    f"| {tx['comment'].ljust(18)}"
                    f"|{str(tx['amount']).rjust(17)} |"
                )
                print(ui.divider(40))
        else:
            print("The expenses list is empty.")

        input("Press Enter to return to the menu.")

    # EXIT
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Try again.")
