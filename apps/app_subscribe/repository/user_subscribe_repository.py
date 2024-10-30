from datetime import datetime, timedelta, date

from django.db.models import F, QuerySet, Q

from apps.app_subscribe.models import UserSubscribe
from domain.const.subscribe import WORKING_DAYS
from domain.repository import UserSubscribeRepository as IUserSubscribeRepository
from domain.entity.user import User


class UserSubscribeRepository(IUserSubscribeRepository):
    def get_leftover_days(self, user_id: int) -> timedelta:
        today = date.today()
        last_subscribe = UserSubscribe.objects.filter(
                user__id = user_id
            ).last()
        if last_subscribe is None:
            return None
        return last_subscribe.created_at +  - today

    def get_fresh_subscriber(self, *args, **kwargs):
        today = datetime.now()
        return UserSubscribe.objects.filter(
            created_at__gte = today - timedelta(days=WORKING_DAYS)
        ).values('user__id')

    def filter_subscriber_by_type(self, user_subscribers: QuerySet[UserSubscribe], client_type, *args, **kwargs):
        return user_subscribers.filter(
            user__client_type = client_type.value[0]
        )
    
    def is_have_subscribe_permission(self, user: User) -> bool:
        if user.is_superuser:
            return True
        return UserSubscribe.objects.filter(
                Q(user__id = user.id) & Q(client_type = user.client_type)
            ).filter(
                user__id__in = self.get_fresh_subscriber()
            ).exists()