import logging

from django.conf import settings

from domain.entity import Subscribe
from domain.entity.type import CLIENT_TYPE
from domain.port.spi.payment.contract import PaymentLinkDTO
from .prodamus_link_builder import PaymentLinkBuilder
from .prodamus_paid_content_builder import ProdamusPaidContentBuilder


logger = logging.getLogger(__name__)


class PaymentHelper:
    def __init__(self):
        self.builder = PaymentLinkBuilder()
        self.paid_content_builder = ProdamusPaidContentBuilder()
    
    def create_link(
            self, 
            product: Subscribe, 
            user_email: str,
            client_type: CLIENT_TYPE
        ):
        PAYMENT_URL = getattr(settings, "PAYMENT_URL")
        PAYMENT_SECRET_KEY = getattr(settings, "PAYMENT_SECRET_KEY")
        paid_content = self.paid_content_builder.build(client_type)
        dto = PaymentLinkDTO(
            linktoform = PAYMENT_URL,
            secret_key = PAYMENT_SECRET_KEY,
            customer_email = user_email,
            products = [product],
            paid_content = paid_content
        )
        return self.builder.generate_payment_link(dto)
