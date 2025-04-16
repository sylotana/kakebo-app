def divider(count, symbol="-"):
    return symbol * count


print(
    divider(40),
    "Budgetshell App for Tracking Expenses",
    divider(40),
    sep="\n"
)

menu_items = [
    "(1) Get balance",
    "(2) Add income",
    "(3) Add expenses",
    "(4) Get incomes",
    "(5) Get expenses",
    "(6) Exit",
]

incomes = []
total_incomes = 0.0
expenses = []
total_expenses = 0.0

while True:
    print("\nSelect a menu item:")
    print(*menu_items, sep="\n")

    choice = input("Select: ")

    # GET BALANCE
    if choice == "1":
        balance = round(total_incomes - total_expenses, 2)
        print(
            divider(40, "="),
            f"Total balance: {balance}",
            f"Total income: {total_incomes}",
            f"Total expenses: {total_expenses}",
            divider(40, "="),
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
        incomes.append((income_comment, float(income)))
        total_incomes += float(income)

        print(
            divider(40, "="),
            "Income added successfully.",
            f"Current income: {total_incomes} (+{income}).",
            divider(40, "="),
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
        expenses.append((expense_comment, float(expense)))
        total_expenses += float(expense)

        print(
            divider(40, "="),
            "Expenses added successfully.",
            f"Current expenses: {total_expenses} (+{expense}).",
            divider(40, "="),
            sep="\n"
        )
        input(
            "Press Enter to return to the menu."
        )

    # GET INCOMES
    elif choice == "4":
        if incomes:
            print(divider(40))
            print(f"| {"TOTAL".ljust(18)}|{str(total_incomes).rjust(17)} |")
            print(divider(40))
            for comment, income in incomes:
                print(f"| {comment.ljust(18)}|{str(income).rjust(17)} |")
                print(divider(40))
        else:
            print("The income list is empty.")

        input("Press Enter to return to the menu.")

    # GET EXPENSES
    elif choice == "5":
        if expenses:
            print(divider(40))
            print(f"| {"TOTAL".ljust(18)}|{str(total_expenses).rjust(17)} |")
            print(divider(40))
            for comment, expense in expenses:
                print(f"| {comment.ljust(18)}|{str(expense).rjust(17)} |")
                print(divider(40))
        else:
            print("The expenses list is empty.")

        input("Press Enter to return to the menu.")

    # EXIT
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Try again.")
