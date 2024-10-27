from datetime import datetime
from django.db.models import QuerySet, F

from apps.app_worker.models import Nanny
from domain.entity import User as DUser
from domain.repository.user_subscribe_repository import UserSubscribeRepository


class NannyRepository:
    def get_fresh_subscriber_nanny(self, user_subscribe_repository: UserSubscribeRepository, *args, **kwargs) -> QuerySet[Nanny]:
        return Nanny.objects.filter(user__id__in = user_subscribe_repository.get_fresh_subscriber())
    
    def get_fresh_subscriber_nanny_pagination(self, user_subscribe_repository: UserSubscribeRepository, count: int, *args, **kwargs) -> QuerySet[Nanny]:
        return self.get_fresh_subscriber_nanny(user_subscribe_repository)[:count]
    
    def is_have_nanny_permission(self, user: DUser) -> bool:
        return Nanny.objects.filter(user__id = user.id).exists()
