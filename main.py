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
while True:
    print("\nSelect a menu item:")
    print(*menu_items, sep="\n")

    choice = input("Select: ")

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
