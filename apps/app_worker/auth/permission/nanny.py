from django.contrib.auth.models import AbstractUser

from apps.app_worker.models import Nanny

def is_have_nanny_permission(user: AbstractUser) -> bool:
    if user.is_superuser:
        return True
    return Nanny.objects.filter(user = user).exists()