from django.contrib.auth.mixins import AccessMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy

from apps.app_subscribe.repository import UserSubscribeRepository
from apps.app_user.utils import to_domain_user


class SubscribeRequiredMixin(AccessMixin):
    """Verify that the current user is subscriber."""

    subscribe_url = reverse_lazy('home')

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponseRedirect:
        d_user = to_domain_user(request.user)
        if UserSubscribeRepository().is_have_subscribe_permission(d_user):
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(self.subscribe_url)