from django.conf import settings
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse

from domain.entity import Subscribe
from domain.entity.type import CLIENT_TYPE
from domain.const.subscribe import SUBSCRIBE_NANNY_NAME, SUBSCRIBE_NANNY_COST
from domain.repository import NannyRepository as INannyRepository
from apps.app_subscribe.auth.mixin import SubscribeRequiredMixin
from apps.app_worker.repository.nanny_repository import NannyRepository
from apps.app_subscribe.helper import PaymentHelper
from apps.app_user.utils import to_domain_user


class NannySubscribeRequiredMixin(SubscribeRequiredMixin):
    """Verify that the current nanny is subscriber."""

    def __init__(self):
        subscribe_type = CLIENT_TYPE.NANNY
        self.nanny_repository: INannyRepository = NannyRepository()
        super().__init__(subscribe_type)
        self.payment_helper = PaymentHelper()

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        d_user = to_domain_user(request.user)
        self.subscribe_url = self._generate_payment_link(request, *args, **kwargs)
        if self.nanny_repository.is_have_nanny_permission(d_user):
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()
    
    def _generate_payment_link(self,  request: HttpRequest, *args, **kwargs) -> str:
        subscribe = Subscribe(
            name = SUBSCRIBE_NANNY_NAME,
            price = SUBSCRIBE_NANNY_COST,
            quantity = 1
        )
        return self.payment_helper.create_link(subscribe, request.user.email, self.subscribe_type)
    

class NotNannySubscribeRequiredMixin(SubscribeRequiredMixin):
    """Verify that the current nanny is subscriber and doesn't create account."""

    def __init__(self):
        subscribe_type = CLIENT_TYPE.NANNY
        self.nanny_repository: INannyRepository = NannyRepository()
        super().__init__(subscribe_type)
        self.payment_helper = PaymentHelper()

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        d_user = to_domain_user(request.user)
        self.subscribe_url = self._generate_payment_link(request, *args, **kwargs)
        if not self.nanny_repository.is_have_nanny_permission(d_user):
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('nanny_update'))
    
    def _generate_payment_link(self,  request: HttpRequest, *args, **kwargs) -> str:
        subscribe = Subscribe(
            name = SUBSCRIBE_NANNY_NAME,
            price = SUBSCRIBE_NANNY_COST,
            quantity = 1
        )
        return self.payment_helper.create_link(subscribe, request.user.email, self.subscribe_type)