from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView

from apps.app_infrastructure.models import City
from apps.app_subscribe.db.date import get_leftover_days
from apps.app_subscribe.models import UserSubscribe

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.user = None

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.user = request.user
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['end_range'] = get_leftover_days(UserSubscribe.leftover.get_queryset(), self.user)
        context['cities'] = City.objects.all()
        return context