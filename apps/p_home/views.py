from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView

from apps.app_infrastructure.models import City
from apps.app_subscribe.repository import UserSubscribeRepository
from domain.services.subscribe import LeftoverDays

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.user = None
        self.leftover_days = LeftoverDays()

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.user = request.user
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.user.is_authenticated:
            context['end_range'] = self.leftover_days.get_subscribe_button_text(
                repository = UserSubscribeRepository(), 
                user_id = self.user.id
            )
        context['cities'] = City.objects.all()
        return context