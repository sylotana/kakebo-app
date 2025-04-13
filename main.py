print("Budgetshell App for Tracking Expenses")

while True:
    # Menu
    print(
        "Menu",
        "1. Add income",
        "2. Add expense",
        "3. Exit",
        sep='\n'
    )
    menu_select = input()

    if menu_select == '1':
        income = input("Enter your day income: ")
    elif menu_select == '2':
        expense = input("Enter your day expense: ")
    elif menu_select == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid input. Try again.")

print("Your income:", income)
print("Your expense:", expense)
