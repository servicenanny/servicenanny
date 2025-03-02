from django.views.generic import RedirectView
import logging

from django.http import HttpRequest, HttpResponseServerError, HttpResponseRedirect
from django.views.generic import RedirectView
from django.contrib.auth import get_user_model
from django.urls import reverse

from domain.entity.type import CLIENT_TYPE


logger = logging.getLogger(__name__)


class LogonSubscribeRedirectView(RedirectView):
    """
    Проверяет вошел ли пользователь и переотправляет клиента на нужную страницу
    """
    http_method_names = [
        'get'
    ]

    def get(self, request, *args, **kwargs):
        try:
            if not request.user.is_authenticated:
                return HttpResponseRedirect(reverse("home"))
            else:
                return HttpResponseRedirect(self._get_client_redirect_url(request))
        except ValueError as ex:
            logger.error(f"[LogonSubscribeRedirectView: get] {str(ex)}")
            return HttpResponseServerError(content="Server error", status=500)
        except Exception as ex:
            logger.fatal(f"[LogonSubscribeRedirectView: get] {str(ex)}")
            return HttpResponseServerError(content="Server error", status=500)
    
    def _get_client_redirect_url(self, request: HttpRequest) -> str:
        if request.user.client_type == CLIENT_TYPE.PARENT:
            return reverse('nannies')
        elif request.user.client_type == CLIENT_TYPE.NANNY:
            return reverse('nanny_create')
        raise ValueError(f"Unknown client type {request.user.client_type}")
