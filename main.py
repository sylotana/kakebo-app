import storage
import logic
import ui

print(*ui.app_description(), sep="\n")

date = logic.get_date()

while True:
    data = storage.load_data(date)
    print("\nSelect a menu item:")
    print(*ui.menu(), sep="\n")

    choice = input("Select: ")

    # GET BALANCE
    if choice == "1":
        total_incomes, total_expenses, balance = (
            logic.calculate_totals(data, date)
        )

        ui.info("Current Balance.", (
            f"Total balance: {balance}",
            f"Total income: {total_incomes}",
            f"Total expenses: {total_expenses}")
        )
        input(ui.WAIT_TEXT)

    # ADD INCOME
    elif choice == "2":
        transaction, result_line = logic.add_transaction(data, date, "income")
        storage.save_data(transaction)
        ui.info("Income added successfully.", (result_line,))
        input(ui.WAIT_TEXT)

    # ADD EXPENSE
    elif choice == "3":
        transaction, result_line = logic.add_transaction(data, date, "expense")
        storage.save_data(transaction)
        ui.info("Expense added successfully.", (result_line,))
        input(ui.WAIT_TEXT)

    # GET INCOMES
    elif choice == "4":
        incomes = logic.get_filtered_transactions(data, "income", date)
        ui.transactions(incomes, date)
        input(ui.WAIT_TEXT)

    # GET EXPENSES
    elif choice == "5":
        expenses = logic.get_filtered_transactions(data, "expense", date)
        ui.transactions(expenses, date)
        input(ui.WAIT_TEXT)

    # EXIT
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Try again.")
