from django.http import HttpRequest

from domain.entity import Subscribe
from domain.entity.type import CLIENT_TYPE
from domain.const.subscribe import SUBSCRIBE_PARENT_COST, SUBSCRIBE_PARENT_NAME
from apps.app_subscribe.auth.mixin import SubscribeRequiredMixin
from apps.app_subscribe.helper.payment import PaymentHelper


class ParentSubscribeRequiredMixin(SubscribeRequiredMixin):
    """Verify that the current nanny is subscriber."""

    def __init__(self):
        subscribe_type = CLIENT_TYPE.PARENT
        super().__init__(subscribe_type)
        self.payment_helper = PaymentHelper()

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        self.subscribe_url = self._generate_payment_link(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)
    
    def _generate_payment_link(self,  request: HttpRequest, *args, **kwargs) -> str:
        subscribe = Subscribe(
            name = SUBSCRIBE_PARENT_NAME,
            price = SUBSCRIBE_PARENT_COST,
            quantity = 1
        )
        return self.payment_helper.create_link(subscribe, request.user.email, self.subscribe_type)
