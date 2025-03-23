from datetime import datetime
from django.db.models import QuerySet, F

from domain.repository import NannyRepository as INannyRepository
from apps.app_worker.models import Nanny
from domain.entity import User as DUser
from domain.entity import Nanny as DNanny
from domain.repository import IUserSubscribeRepository
from domain.repository.nanny_repository import AddNannyDTO


class NannyRepository(INannyRepository[Nanny]):
    def get_by_user_id(self, user_id, *args, **kwargs):
        return Nanny.objects.get(user__id = user_id)
    
    def is_nanny_exist(self, user_id, *args, **kwargs):
        return Nanny.objects.filter(user__id = user_id).exists()
    
    def get_fresh_subscriber_nanny(self, user_subscribe_repository: IUserSubscribeRepository, *args, **kwargs) -> QuerySet[Nanny]:
        return Nanny.objects.filter(user__id__in = user_subscribe_repository.get_fresh_subscriber())
    
    def get_fresh_subscriber_nanny_pagination(self, user_subscribe_repository: IUserSubscribeRepository, count: int, *args, **kwargs) -> QuerySet[Nanny]:
        return self.get_fresh_subscriber_nanny(user_subscribe_repository)[:count]
    
    def get_fresh_subscriber_nannies_by_city(self, user_subscribe_repository, city_id, *args, **kwargs):
        result = Nanny.objects.filter(
                user__id__in = user_subscribe_repository.get_fresh_subscriber()
            ).filter(
                user__city__id = city_id
            )
        return result
    
    def is_have_nanny_permission(self, user: DUser) -> bool:
        return Nanny.objects.filter(user__id = user.id).exists()
