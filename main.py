import storage
import logic
import ui

print(*ui.app_description(), sep="\n")

date = logic.get_date()


def handle_transaction(data: list[dict], date: str, t_type: str) -> None:
    """Add a transaction to the data list based on the given date and type.

    Args:
        data (list[dict]): List of transaction dictionaries.
        date (str): Date in "dd-mm-yyyy" format.
        t_type (str): Transaction type ("income" or "expense").

    Returns:
        None
    """
    transaction, result_line = logic.add_transaction(data, date, t_type)
    storage.save_data(transaction)
    ui.info("{t_type.title()} added successfully.", (result_line,))
    ui.wait_for_user_input()


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
        handle_transaction(data, date, "income")

    # ADD EXPENSE
    elif choice == "3":
        handle_transaction(data, date, "expense")

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
