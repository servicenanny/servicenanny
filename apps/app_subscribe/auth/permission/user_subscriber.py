from django.contrib.auth.models import AbstractUser

from apps.app_subscribe.models import UserSubscribe


def is_have_subscribe_permission(user: AbstractUser) -> bool:
    if user.is_superuser:
        return True
    return UserSubscribe.leftover.filter(user=user).fresh_subscribe().exists()