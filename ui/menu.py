class MenuUI:
    def __init__(self, menu_handler):
        self.menu_handler = menu_handler
        h = self.menu_handler

        def make_add_action(t_type):
            return lambda: h.add_transaction(t_type)

        def make_get_action(t_type):
            return lambda: h.get_transaction(t_type)

        self.menu_items = [
            {"label": "Get Balance", "action": h.show_balance},
            {"label": "Add Income", "action": make_add_action("income")},
            {"label": "Add Expense", "action": make_add_action("expense")},
            {"label": "Get Incomes", "action": make_get_action("income")},
            {"label": "Get Expenses", "action": make_get_action("expense")},
            {"label": "Exit", "action": h.exit_app},
        ]

    def show_menu(self):
        while True:
            for i, item in enumerate(self.menu_items, 1):
                print(f"{i}. {item['label']}")

            choice = input("Choose an option: ")
            if (
                not choice.isdigit() or
                not (1 <= int(choice) <= len(self.menu_items))
            ):
                print("Invalid choice")
                continue

            self.menu_items[int(choice) - 1]["action"]()
