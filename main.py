import storage
import logic
import ui

print(*ui.app_description(), sep="\n")

date = logic.get_date()

while True:
    print("\nSelect a menu item:")
    print(*ui.menu(), sep="\n")

    choice = input("Select: ")

    # GET BALANCE
    if choice == "1":
        total_incomes, total_expenses, balance = (
            logic.calculate_totals(storage.data, date)
        )

        ui.info("Current Balance.", (
            f"Total balance: {balance}",
            f"Total income: {total_incomes}",
            f"Total expenses: {total_expenses}")
        )
        input(ui.WAIT_TEXT)

    # ADD INCOME
    elif choice == "2":
        amount = logic.get_transaction_input("Enter income amount: ", float)
        comment = logic.get_transaction_input(
            "Enter income comment (can contain spaces): "
        )
        logic.add_transaction(storage.data, date, "income", amount, comment)

        total_incomes, _, _ = logic.calculate_totals(storage.data, date)
        result_line = ui.format_transaction("income", total_incomes, amount)

        ui.info("Income added successfully.", (result_line,))
        input(ui.WAIT_TEXT)

    # ADD EXPENSE
    elif choice == "3":
        amount = logic.get_transaction_input("Enter expense amount: ", float)
        comment = logic.get_transaction_input(
            "Enter expense comment (can contain spaces): "
        )
        logic.add_transaction(storage.data, date, "expense", amount, comment)

        _, total_expenses, _ = logic.calculate_totals(storage.data, date)
        result_line = ui.format_transaction("expense", total_expenses, amount)

        ui.info("Expense added successfully.", (result_line,))
        input(ui.WAIT_TEXT)

    # GET INCOMES
    elif choice == "4":
        incomes = logic.get_filtered_transactions(storage.data, "income", date)
        ui.transactions(incomes, date)
        input(ui.WAIT_TEXT)

    # GET EXPENSES
    elif choice == "5":
        expenses = logic.get_filtered_transactions(storage.data, "expense", date)
        ui.transactions(expenses, date)
        input(ui.WAIT_TEXT)

    # EXIT
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Try again.")
