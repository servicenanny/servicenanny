from typing import Any

from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin

from domain.repository import NannyRepository as INannyRepository
from apps.app_worker.repository import NannyRepository


class NannyProfileRedirectView(
        LoginRequiredMixin, 
        RedirectView
    ):    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.nanny_repository: INannyRepository = NannyRepository()

    def get(self, request, *args, **kwargs):
        if self.nanny_repository.is_nanny_exist(request.user.id):
            return HttpResponsePermanentRedirect(reverse('nanny_update'))
        else:
            return HttpResponsePermanentRedirect(reverse('nanny_create'))
