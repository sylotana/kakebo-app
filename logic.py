def get_filtered_transactions(data, t_type, date):
    return [tx for tx in data if tx["type"] == t_type and tx["date"] == date]


def calculate_totals(data, date):
    incomes = get_filtered_transactions(data, "income", date)
    expenses = get_filtered_transactions(data, "expense", date)
    total_income = sum(tx["amount"] for tx in incomes)
    total_expense = sum(tx["amount"] for tx in expenses)
    balance = round(total_income - total_expense, 2)
    return total_income, total_expense, balance


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


def add_transaction(data, date, type, amount, comment):
    data.append({
        "date": date,
        "type": type,
        "amount": amount,
        "comment": comment
    })


def get_date():
    while not bool(date := input(
        "Enter a today's date in the format: <dd-mm-yyyy>: "
    )):
        pass

    return date
