from datetime import timedelta, datetime

from django.db.models import QuerySet, F, Func, DateTimeField
from django.contrib.auth.models import AbstractBaseUser


from apps.app_subscribe.models import UserSubscribe


class IntervalSeconds(Func):
    function = 'INTERVAL'
    template = "(%(expressions)s * %(function)s '1 days')"


def get_leftover_days(queryset: QuerySet[UserSubscribe], user: AbstractBaseUser) -> timedelta:
    today = datetime.now()
    result = queryset.filter(
            user = user
        ).annotate(
            total = F('created_at') - today
        ).last()
    if result is None:
        return None
    return result.total