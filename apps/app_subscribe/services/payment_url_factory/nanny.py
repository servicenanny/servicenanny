from apps.app_subscribe.helper.payment import PaymentHelper
from domain.services.subscribe import APaymentURLFactory
from domain.entity.subscribe import Subscribe
from domain.const.subscribe import SUBSCRIBE_NANNY_COST, SUBSCRIBE_NANNY_NAME
from domain.services.prizes.const import DISCOUNTS_NANNY
from domain.entity.type.client_type import CLIENT_TYPE

class NannyPaymentURLFactory(APaymentURLFactory):
    def __init__(self):
        super().__init__()
        self.payment_helper = PaymentHelper()
        
    def create_payment_url(self):
        subscribe = Subscribe(
            name = SUBSCRIBE_NANNY_NAME,
            price = self.get_cost(),
            quantity = 1
        )
        return self.payment_helper.create_link(subscribe, CLIENT_TYPE.NANNY.value[0])
    
    def get_cost(self):
        return SUBSCRIBE_NANNY_COST