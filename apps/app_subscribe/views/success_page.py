from django.http import HttpRequest
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from domain.entity.type.client_type import CLIENT_TYPE


class SuccessPaymentPageView(LoginRequiredMixin, TemplateView):
    template_name = "success_payment.html"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.request: HttpRequest | None = None

    def get(self, request, *args, **kwargs):
        self.request = request
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        if self.request.user.client_type == CLIENT_TYPE.PARENT:
            data['client_content'] = "базу нянь"
            data['redirect_to'] = reverse('nannies')
        elif self.request.user.client_type == CLIENT_TYPE.NANNY:
            data['client_content'] = "профиль няни"
            data['redirect_to'] = reverse('nanny_create')
        else:
            raise ValueError(f"Unknown client type {self.request.user.client_type}")
        return data