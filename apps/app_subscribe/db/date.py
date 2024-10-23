from datetime import timedelta, datetime

from django.db.models import QuerySet, F
from django.contrib.auth.models import AbstractBaseUser


from apps.app_subscribe.models import UserSubscribe


def get_leftover_days(queryset: QuerySet[UserSubscribe], user: AbstractBaseUser) -> timedelta:
    today = datetime.now()
    result = queryset.filter(
            user__id__in = user.id
        ).annotate(
            total = F('subscribe__day_range') + F('created_at') - today
        ).values(
            'total'
        ).last()
    return result['total']