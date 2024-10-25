from django.contrib.auth.mixins import AccessMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy

from apps.app_subscribe.auth.permission import is_have_subscribe_permission


class SubscribeRequiredMixin(AccessMixin):
    """Verify that the current user is subscriber."""

    subscribe_url = reverse_lazy('home')

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponseRedirect:
        if is_have_subscribe_permission(request.user):
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(self.subscribe_url)