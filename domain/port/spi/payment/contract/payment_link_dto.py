from dataclasses import dataclass

from domain.entity import Subscribe


@dataclass
class PaymentLinkDTO:
    linktoform: str
    secret_key: str
    customer_email: str
    products: list[Subscribe]
    paid_content: str
    do: str = 'pay'