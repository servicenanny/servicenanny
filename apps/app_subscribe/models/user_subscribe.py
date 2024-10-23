from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from .subscribe import Subscribe


class LeftoverUserSubscribeQuerySet(models.QuerySet):
    def fresh_subscribe(self, *args, **kwargs):
        today = datetime.now()
        return self.filter(
            created_at__gte = today - models.F('subscribe__day_range')
        )


class LeftoverUserSubscribeManager(models.Manager):
    def get_queryset(self):
        return LeftoverUserSubscribeQuerySet(self.model, using=self._db)

    def fresh_subscribe(self, *args, **kwargs):
        return self.get_queryset().fresh_subscribe()
    
    def get_leftover_days(self, *args, **kwargs):
        raise Exception(args)


class UserSubscribe(models.Model):
    user = models.ForeignKey(get_user_model(), db_index=True, on_delete=models.CASCADE, verbose_name="Пользователь", help_text="Пользователь, который оформил подписку")
    subscribe = models.ForeignKey(Subscribe, on_delete=models.CASCADE, verbose_name="Подписка", help_text="Подписка, которую оформил пользователь")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")

    leftover = LeftoverUserSubscribeManager()

    def __str__(self) -> str:
        return self.created_at
    
    class Meta:
        verbose_name = 'Подписка пользователя'
        verbose_name_plural = 'Подписки пользователей'