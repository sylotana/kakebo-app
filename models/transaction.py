class Transaction:
    def __init__(self, date: str, t_type: str, amount: float, comment: str):
        self.date = date
        self.t_type = t_type
        self.amount = amount
        self.comment = comment

    def __str__(self):
        return f"{self.date};{self.t_type};{self.amount};{self.comment}"
