from django.http import HttpRequest

from apps.app_subscribe.auth.mixin import SubscribeRequiredMixin
from apps.app_worker.repository.nanny_repository import NannyRepository
from apps.app_user.utils import to_domain_user
from domain.entity.type import CLIENT_TYPE
from domain.repository import NannyRepository as INannyRepository


class ParentSubscribeRequiredMixin(SubscribeRequiredMixin):
    """Verify that the current nanny is subscriber."""

    def __init__(self):
        subscribe_type = CLIENT_TYPE.PARENT.value[0]
        super().__init__(subscribe_type)

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
