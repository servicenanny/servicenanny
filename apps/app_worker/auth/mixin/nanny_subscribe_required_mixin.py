from django.http import HttpRequest

from apps.app_subscribe.auth.mixin import SubscribeRequiredMixin
from apps.app_worker.repository.nanny_repository import NannyRepository
from apps.app_user.utils import to_domain_user
from domain.entity.type import CLIENT_TYPE
from domain.repository import NannyRepository as INannyRepository


class NannySubscribeRequiredMixin(SubscribeRequiredMixin):
    """Verify that the current nanny is subscriber."""

    def __init__(self):
        subscribe_type = CLIENT_TYPE.NANNY.value[0]
        self.nanny_repository: INannyRepository = NannyRepository()
        super().__init__(subscribe_type)

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        d_user = to_domain_user(request.user)
        if not self.nanny_repository.is_have_nanny_permission(d_user):
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()