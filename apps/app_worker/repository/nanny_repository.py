from datetime import datetime
from django.db.models import QuerySet, F

from apps.app_worker.models import Nanny
from domain.repository.user_subscribe_repository import UserSubscribeRepository


class NannyRepository:
    def get_fresh_subscriber_nanny(self, user_subscribe_repository: UserSubscribeRepository, *args, **kwargs) -> QuerySet[Nanny]:
        return Nanny.objects.filter(user__id__in = user_subscribe_repository.get_fresh_subscriber())