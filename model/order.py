from dataclasses import dataclass
from datetime import date

@dataclass
class Order:
    order_id: int
    customer_id: int
    order_status: int
    order_date: date
    required_date: date
    shipped_date: date
    store_id: int
    staff_id: int
    def __str__(self):
        return "ordine numero "+ str(self.order_id)

    def __hash__(self):
        return hash(self.order_id)
