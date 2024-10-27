from datetime import datetime, timedelta, date

from django.db.models import F

from apps.app_subscribe.models import UserSubscribe
from domain.entity.user import User


class UserSubscribeRepository:
    def get_leftover_days(self, user_id: int) -> timedelta:
        today = date.today()
        last_subscribe = UserSubscribe.leftover.filter(
                user__id = user_id
            ).last()
        if last_subscribe is None:
            return None
        return last_subscribe.created_at + timedelta(days=last_subscribe.subscribe.day_range) - today
    
    def get_fresh_subscriber(self) -> list[int]:
        today = datetime.now()
        return UserSubscribe.objects.filter(
            created_at__gte = today - F('subscribe__day_range')
        ).values('user__id')
    
    def is_have_subscribe_permission(self, user: User) -> bool:
        if user.is_superuser:
            return True
        return UserSubscribe.objects.filter(
                user__id = user.id
            ).filter(
                user__id__in = self.get_fresh_subscriber()
            ).exists()