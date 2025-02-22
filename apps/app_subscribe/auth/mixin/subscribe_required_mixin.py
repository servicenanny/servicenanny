from django.contrib.auth.mixins import AccessMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy

from apps.app_subscribe.repository import UserSubscribeRepository
from apps.app_user.utils import to_domain_user
from domain.entity.type.client_type import CLIENT_TYPE
from domain.repository.user_subscribe_repository import IUserSubscribeRepository as IUserSubscribeRepository


class SubscribeRequiredMixin(AccessMixin):
    """Verify that the current user is subscriber."""

    subscribe_url = reverse_lazy('home')

    def __init__(self, subscribe_type: CLIENT_TYPE):
        self.subscribe_type = subscribe_type
        self.user_subscribe_repository: IUserSubscribeRepository = UserSubscribeRepository()

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponseRedirect:
        d_user = to_domain_user(request.user)
        if self.user_subscribe_repository.is_have_subscribe_permission(d_user, self.subscribe_type):
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(self.subscribe_url)