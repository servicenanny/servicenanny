from django.views.generic import RedirectView
from datetime import datetime
import logging

from django.http import HttpRequest, HttpResponseServerError, HttpResponseRedirect
from django.views.generic import RedirectView
from django.contrib.auth import get_user_model
from django.urls import reverse

from domain.entity.type import CLIENT_TYPE
from domain.port.api.payment import SuccessAPI
from domain.repository.user_subscribe_repository import AddUserSubscribeDTO
from domain.repository.user_repository import UserRepository as IUserRepository
from apps.app_subscribe.helper import ProdamusVerificate
from apps.app_subscribe.repository import UserSubscribeRepository
from apps.app_user.repository import UserRepository
from apps.app_user.utils import to_domain_user


logger = logging.getLogger(__name__)


class LogonSubscribeRedirectView(RedirectView):
    """
    Проверяет вошел ли пользователь и переотправляет клиента на нужную страницу
    """
    http_method_names = [
        'get'
    ]

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home"))
        else:
            return HttpResponseRedirect(self._get_client_redirect_url(request))
    
    def _get_client_redirect_url(self, request: HttpRequest) -> str:
        if request.user.client_type == CLIENT_TYPE.PARENT:
            return reverse('nannies')
        elif request.user.client_type == CLIENT_TYPE.NANNY:
            return reverse('nanny_create')
        raise ValueError(f"Unknown client type {request.user.client_type}")
