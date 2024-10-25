from django.http import HttpRequest

from apps.app_subscribe.auth.mixin import SubscribeRequiredMixin
from apps.app_worker.auth.permission import is_have_nanny_permission


class NannySubscribeRequiredMixin(SubscribeRequiredMixin):
    """Verify that the current nanny is subscriber."""

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        if is_have_nanny_permission(request.user):
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()