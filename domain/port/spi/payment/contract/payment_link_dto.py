from dataclasses import dataclass

from domain.entity import Subscribe


@dataclass
class PaymentLinkDTO:
    linktoform: str
    secret_key: str
    products: list[Subscribe]
    paid_content: str
    client_type: str
    do: str = 'pay'