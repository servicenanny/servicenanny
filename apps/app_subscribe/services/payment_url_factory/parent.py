from apps.app_subscribe.helper.payment import PaymentHelper
from domain.services.subscribe import APaymentURLFactory
from domain.entity.subscribe import Subscribe
from domain.const.subscribe import SUBSCRIBE_PARENT_NAME, SUBSCRIBE_PARENT_COST
from domain.services.prizes.const import DISCOUNTS_PARENT


class ParentPaymentURLFactory(APaymentURLFactory):
    def __init__(self):
        super().__init__()
        self.payment_helper = PaymentHelper()
        
    def create_payment_url(self, user):
        subscribe = Subscribe(
            name = SUBSCRIBE_PARENT_NAME,
            price = self.get_cost(user),
            quantity = 1
        )
        return self.payment_helper.create_link(subscribe, user.email, user.client_type)
    
    def get_cost(self, user):
        return SUBSCRIBE_PARENT_COST