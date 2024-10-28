from django.http import HttpRequest

from apps.app_subscribe.auth.mixin import SubscribeRequiredMixin
from apps.app_worker.repository.nanny_repository import NannyRepository
from apps.app_user.utils import to_domain_user


class NannySubscribeRequiredMixin(SubscribeRequiredMixin):
    """Verify that the current nanny is subscriber."""
    def dispatch(self, request: HttpRequest, *args, **kwargs):
        d_user = to_domain_user(request.user)
        if not NannyRepository().is_have_nanny_permission(d_user):
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()