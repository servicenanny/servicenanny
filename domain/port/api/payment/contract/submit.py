from dataclasses import dataclass

from .product import ProductContract


@dataclass
class SubmitContract:
    order_num: str
    customer_phone: str
    customer_email: str
    products: list[ProductContract]
    payment_status: str
    payment_status_description: str
    payment_init: str
    date: str | None = None
    order_id: str | None = None
    domain: str | None = None
    sum: str | None = None
    currency: str | None = None
    customer_extra: str | None = None
    callbackType: str | None = None
    payment_type: str | None = None
    commission: str | None = None
    commission_sum: str | None = None
    attempt: str | None = None
    sys: str | None = None
    link_expired: str | None = None
    