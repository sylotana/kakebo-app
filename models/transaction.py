from dataclasses import dataclass


@dataclass
class Transaction:
    date: str
    t_type: str
    amount: float
    comment: str
