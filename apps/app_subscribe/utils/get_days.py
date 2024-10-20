from datetime import datetime

from django.db.models import F

from ..models import SubscribeMove


def get_remaining_days(user):
    now = datetime.now()
    SubscribeMove.objects.filter(
        user = user
    ).aggregate(total = now - F("end_date"))