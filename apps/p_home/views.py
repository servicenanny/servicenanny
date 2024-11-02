from typing import Any

from django.http import HttpRequest
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse

from apps.app_infrastructure.models import City
from apps.app_subscribe.repository import UserSubscribeRepository
from domain.entity.subscribe import Subscribe
from domain.entity.type import CLIENT_TYPE
from domain.const.subscribe import SUBSCRIBE_NANNY_COST, SUBSCRIBE_NANNY_NAME, SUBSCRIBE_PARENT_COST, SUBSCRIBE_PARENT_NAME
from domain.services.subscribe import LeftoverDays
from apps.app_subscribe.helper import PaymentHelper


class HomeView(TemplateView):
    template_name = 'home.html'

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.user = None
        self.leftover_days = LeftoverDays()
        self.repository = UserSubscribeRepository()
        self.payment_helper = PaymentHelper()

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.user = request.user
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        context['nanny_payment_link'] = self.create_nanny_payment_url()
        context['parent_payment_link'] = self.create_parent_payment_url()
        return context
    
    def create_nanny_payment_url(self) -> str:
        if self.user.is_anonymous:
            return reverse('account_signup')
        elif self.user.client_type == CLIENT_TYPE.PARENT:
            return ''
        subscribe = Subscribe(
            name = SUBSCRIBE_NANNY_NAME,
            price = SUBSCRIBE_NANNY_COST,
            quantity = 1
        )
        return self.payment_helper.create_link(subscribe, self.user.email, self.user.client_type)
    
    def create_parent_payment_url(self) -> str:
        if self.user.is_anonymous:
            return reverse('account_signup')
        elif self.user.client_type == CLIENT_TYPE.NANNY:
            return ''
        subscribe = Subscribe(
            name = SUBSCRIBE_PARENT_NAME,
            price = SUBSCRIBE_PARENT_COST,
            quantity = 1
        )
        return self.payment_helper.create_link(subscribe, self.user.email, self.user.client_type)
