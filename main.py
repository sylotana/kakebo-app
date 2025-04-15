print(
    "-------------------------------------",
    "Budgetshell App for Tracking Expenses",
    "-------------------------------------",
    sep="\n"
)

menu_items = [
    "(1) Get balance",
    "(2) Add income",
    "(3) Add expenses",
    "(4) Exit"
]

incomes = []
total_incomes = 0.0
expenses = []
total_expenses = 0.0

while True:
    print("\nSelect a menu item:")
    print(*menu_items, sep="\n")

    choice = input("Select: ")

    if choice == "1":
        balance = round(total_incomes - total_expenses, 2)
        print(
            "=====================================",
            f"Total balance: {balance}",
            f"Total income: {total_incomes}",
            f"Total expenses: {total_expenses}",
            "=====================================",
            sep='\n'
        )
        input(
            "Press Enter to return to the menu."
        )

    elif choice == "2":
        income_comment, income = (
            input('Enter your income in the format: <comment> <income>: ')
            .split()
        )
        incomes.append((income_comment, float(income)))
        total_incomes += float(income)

        print(
            "=====================================",
            "Income added successfully.",
            f"Current income: {total_incomes} (+{income}).",
            "=====================================",
            sep="\n"
        )
        input(
            "Press Enter to return to the menu."
        )

    elif choice == "3":
        expense_comment, expense = (
            input('Enter your expense in the format: <comment> <expense>: ')
            .split()
        )
        expenses.append((expense_comment, float(expense)))
        total_expenses += float(expense)

        print(
            "=====================================",
            "Expenses added successfully.",
            f"Current expenses: {total_expenses} (+{expense}).",
            "=====================================",
            sep="\n"
        )
        input(
            "Press Enter to return to the menu."
        )

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Try again.")
