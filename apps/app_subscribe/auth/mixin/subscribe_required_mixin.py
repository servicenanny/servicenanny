from django.contrib.auth.mixins import AccessMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy

from apps.app_subscribe.repository import UserSubscribeRepository
from domain.entity.user import User as DUser


class SubscribeRequiredMixin(AccessMixin):
    """Verify that the current user is subscriber."""

    subscribe_url = reverse_lazy('home')

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponseRedirect:
        d_user = self.__get_domain_user(request)
        if UserSubscribeRepository().is_have_subscribe_permission(d_user):
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(self.subscribe_url)
    
    def __get_domain_user(self, request: HttpRequest) -> DUser:
        return DUser(
            id = request.user.id,
            email = request.user.id,
            password = request.user.password,
            is_superuser = request.user.is_superuser
        )