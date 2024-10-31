from dataclasses import dataclass


@dataclass
class Subscribe:
    name: str
    price: int
    quantity: int