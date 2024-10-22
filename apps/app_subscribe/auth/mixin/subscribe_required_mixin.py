from django.contrib.auth.mixins import AccessMixin
from django.http import HttpRequest

from apps.app_subscribe.auth.permission import is_have_subscribe_permission


class SubscribeRequiredMixin(AccessMixin):
    """Verify that the current user is subscriber."""

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        if is_have_subscribe_permission(request.user):
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()