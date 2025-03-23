from dataclasses import dataclass


@dataclass
class ProductContract:
    name: str
    price: str
    quantity: str
    sum: str