from dataclasses import dataclass

from .product import ProductContract
from .submit import SubmitContract


@dataclass
class PaymentResponseContract:
    order_num: str
    customer_phone: str
    products: list[ProductContract]
    payment_status: str
    payment_status_description: str
    payment_init: str
    submit: SubmitContract
    date: str | None = None
    order_id: str | None = None
    domain: str | None = None
    sum: str | None = None
    callbackType: str | None = None
    customer_extra: str | None = None
    payment_type: str | None = None
    commission: str | None = None
    commission_sum: str | None = None
    attempt: str | None = None
    sys: str | None = None