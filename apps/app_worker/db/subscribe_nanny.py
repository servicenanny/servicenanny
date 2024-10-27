from datetime import datetime
from django.db.models import QuerySet, F

from apps.app_worker.models import Nanny
from apps.app_subscribe.models import UserSubscribe


def get_subscriber_nanny(queryset: QuerySet[Nanny]) -> QuerySet[Nanny]:
    return queryset.filter(user__in = UserSubscribe.leftover.fresh_subscribe().values('user'))