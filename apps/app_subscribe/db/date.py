from datetime import timedelta, datetime

from django.db.models import QuerySet, Func
from django.contrib.auth.models import AbstractBaseUser


from apps.app_subscribe.models import UserSubscribe


class IntervalSeconds(Func):
    function = 'INTERVAL'
    template = "(%(expressions)s * %(function)s '1 days')"


def get_leftover_days(queryset: QuerySet[UserSubscribe], user: AbstractBaseUser) -> timedelta:
    today = datetime.now()
    last = queryset.filter(
            user = user
        ).last()
    if last is None:
        return None
    return last.created_at + timedelta(days=last.subscribe.day_range) - today