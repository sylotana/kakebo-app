import ui

print(*ui.app_description(), sep="\n")

while not bool(today_date := input(
    "Enter a today's date in the format: <dd-mm-yyyy>: "
)):
    pass

budget = {
    today_date: {
        'incomes': [],
        'expenses': []
    }
}

while True:
    budget_incomes = budget[today_date]["incomes"]
    budget_expenses = budget[today_date]["expenses"]

    print("\nSelect a menu item:")
    print(*ui.menu(), sep="\n")

    choice = input("Select: ")

    # GET BALANCE
    if choice == "1":
        total_incomes = sum((i[1] for i in budget_incomes))
        total_expenses = sum((i[1] for i in budget_expenses))
        balance = round(total_incomes - total_expenses, 2)
        print(
            ui.divider(40, "="),
            f"Total balance: {balance}",
            f"Total income: {total_incomes}",
            f"Total expenses: {total_expenses}",
            ui.divider(40, "="),
            sep='\n'
        )
        input(
            "Press Enter to return to the menu."
        )

    # ADD INCOME
    elif choice == "2":
        income_comment, income = (
            input('Enter your income in the format: <comment> <income>: ')
            .split()
        )
        budget_incomes.append((income_comment, float(income)))
        total_incomes = sum((i[1] for i in budget_incomes))

        print(
            ui.divider(40, "="),
            "Income added successfully.",
            f"Current income: {total_incomes} (+{income}).",
            ui.divider(40, "="),
            sep="\n"
        )
        input(
            "Press Enter to return to the menu."
        )

    # ADD EXPENSE
    elif choice == "3":
        expense_comment, expense = (
            input('Enter your expense in the format: <comment> <expense>: ')
            .split()
        )
        budget_expenses.append((expense_comment, float(expense)))
        total_expenses = sum((i[1] for i in budget_expenses))

        print(
            ui.divider(40, "="),
            "Expenses added successfully.",
            f"Current expenses: {total_expenses} (+{expense}).",
            ui.divider(40, "="),
            sep="\n"
        )
        input(
            "Press Enter to return to the menu."
        )

    # GET INCOMES
    elif choice == "4":
        if budget_incomes:
            print(ui.divider(40))
            print(f"| {"TOTAL".ljust(18)}|{str(total_incomes).rjust(17)} |")
            print(ui.divider(40))
            for comment, income in budget_incomes:
                print(f"| {comment.ljust(18)}|{str(income).rjust(17)} |")
                print(ui.divider(40))
        else:
            print("The income list is empty.")

        input("Press Enter to return to the menu.")

    # GET EXPENSES
    elif choice == "5":
        if budget_expenses:
            print(ui.divider(40))
            print(f"| {"TOTAL".ljust(18)}|{str(total_expenses).rjust(17)} |")
            print(ui.divider(40))
            for comment, expense in budget_expenses:
                print(f"| {comment.ljust(18)}|{str(expense).rjust(17)} |")
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
