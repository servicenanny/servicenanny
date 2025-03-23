from datetime import datetime, timedelta, date

from django.db.models import QuerySet, Q
from django.contrib.auth import get_user_model

from .mapper import UserSubscribeMapper
from apps.app_subscribe.models import UserSubscribe
from domain.const.subscribe import WORKING_DAYS
from domain.repository import IUserSubscribeRepository as IUserSubscribeRepository


class UserSubscribeRepository(IUserSubscribeRepository):
    def __init__(self):
        self.mapper = UserSubscribeMapper()
        super().__init__()

    def get_leftover_days(self, user_id: int) -> timedelta:
        today = date.today()
        last_subscribe = UserSubscribe.objects.filter(
                user__id = user_id
            ).last()
        if last_subscribe is None:
            return None
        return last_subscribe.created_at + timedelta(days=WORKING_DAYS) - today

    def get_fresh_subscriber(self, *args, **kwargs):
        today = datetime.now()
        return UserSubscribe.objects.filter(
            created_at__gte = today - timedelta(days=WORKING_DAYS)
        ).values('user__id')
    
    def get_fresh_subscriber_by_type(self, client_type, *args, **kwargs):
        today = datetime.now()
        return UserSubscribe.objects.filter(
                user__client_type = client_type
            ).filter(
                created_at__gte = today - timedelta(days=WORKING_DAYS)
            ).values('user__id')

    def filter_subscriber_by_type(self, user_subscribers: QuerySet[UserSubscribe], client_type, *args, **kwargs):
        return user_subscribers.filter(
            user__client_type = client_type.value[0]
        )
    
    def is_have_subscribe_permission(self, user, client_type, *args, **kwargs):
        if user.is_superuser:
            return True
        return UserSubscribe.objects.filter(
                Q(user__id = user.id) & Q(subscribe_type = client_type.value[0])
            ).filter(
                user__id__in = self.get_fresh_subscriber_by_type(user.client_type)
            ).exists()
    
    def add(self, dto, *args, **kwargs):
        User = get_user_model()
        subscribe = UserSubscribe(
            user = User.objects.get(id = dto.user.id),
            subscribe_type = dto.user.client_type
        )
        subscribe.save()
        return self.mapper.deep_to_domain(subscribe)