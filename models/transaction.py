from dataclasses import dataclass, field
import uuid


@dataclass
class Transaction:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    date: str
    t_type: str
    amount: float
    comment: str
