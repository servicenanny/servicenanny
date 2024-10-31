import logging
from django.conf import settings

from domain.entity import Subscribe
from domain.port.spi.payment.contract import PaymentLinkDTO
from apps.app_subscribe.helper import PaymentLinkBuilder


logger = logging.getLogger(__name__)


class PaymentHelper:
    def __init__(self):
        self.builder = PaymentLinkBuilder()
    
    def create_link(self, product: Subscribe, user_email: str):
        PAYMENT_URL = getattr(settings, "PAYMENT_URL")
        PAYMENT_SECRET_KEY = getattr(settings, "PAYMENT_URL")
        dto = PaymentLinkDTO(
            linktoform = PAYMENT_URL,
            secret_key = PAYMENT_SECRET_KEY,
            customer_email = user_email,
            products = [product]
        )
        return self.builder.generate_payment_link(dto)
