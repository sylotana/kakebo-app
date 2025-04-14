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

total_income = 0.0
total_expenses = 0.0

while True:
    print("\nSelect a menu item:")
    print(*menu_items, sep="\n")

    choice = input("Select: ")

    if choice == "1":
        balance = total_income - total_expenses
        print(
            "=====================================",
            f"Total balance: {balance}",
            f"Total income: {total_income}",
            f"Total expenses: {total_expenses}",
            "=====================================",
            sep='\n'
        )
        input(
            "Press Enter to return to the menu."
        )

    elif choice == "2":
        income = float(input("Enter your income: "))
        total_income += income
        print(
            "=====================================",
            "Income added successfully.",
            f"Current income: {total_income} (+{income}).",
            "=====================================",
            sep="\n"
        )
        input(
            "Press Enter to return to the menu."
        )

    elif choice == "3":
        expenses = float(input("Enter your expenses: "))
        total_expenses += expenses
        print(
            "=====================================",
            "Expenses added successfully.",
            f"Current expenses: {total_expenses} (-{expenses}).",
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
