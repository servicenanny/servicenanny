from typing import Any

from django.http import HttpRequest
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse

from .stylizations import SpinnerStylization
from apps.p_home.models import FAQ, Review
from apps.app_infrastructure.models import City
from apps.app_subscribe.repository import UserSubscribeRepository
from apps.app_subscribe.services.payment_url_factory import ParentPaymentURLFactory, NannyPaymentURLFactory
from apps.app_user.utils.to_domain import to_domain_user
from domain.entity.type.client_type import CLIENT_TYPE
from domain.const.subscribe import SUBSCRIBE_NANNY_COST, SUBSCRIBE_PARENT_COST
from domain.services.subscribe import LeftoverDays
from domain.services.prizes import PrizesSpinner


class HomeView(TemplateView):
    template_name = 'home.html'

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.user = None
        self.leftover_days = LeftoverDays()
        self.repository = UserSubscribeRepository()
        self.nanny_factory = NannyPaymentURLFactory()
        self.parent_factory = ParentPaymentURLFactory()
        self.prizes = PrizesSpinner()
        self.stylization = SpinnerStylization()

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.user = request.user
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        context['nanny_prizes'] = self.prizes.get_client_context(CLIENT_TYPE.NANNY)
        context['parent_prizes'] = self.prizes.get_client_context(CLIENT_TYPE.PARENT)
        if self.user.is_anonymous:
            context['nanny_payment_link'] = reverse('account_signup')
            context['parent_payment_link'] = reverse('account_signup')
        else:
            d_user = to_domain_user(self.user)
            context['nanny_payment_link'] = self.nanny_factory.create_payment_url(d_user)
            context['parent_payment_link'] = self.parent_factory.create_payment_url(d_user)
        context['nanny_cost'] = SUBSCRIBE_NANNY_COST
        context['parent_cost'] = SUBSCRIBE_PARENT_COST
        context['reviews'] = Review.objects.all()
        context['faqs'] = FAQ.objects.all()
        context['nanny_spinner_style'] = self.stylization.get_conic_gradient(context['nanny_prizes'])
        context['parent_spinner_style'] = self.stylization.get_conic_gradient(context['parent_prizes'])
        return context