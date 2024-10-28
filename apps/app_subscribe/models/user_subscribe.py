from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from .subscribe import Subscribe


class UserSubscribe(models.Model):
    user = models.ForeignKey(get_user_model(), db_index=True, on_delete=models.CASCADE, verbose_name="Пользователь", help_text="Пользователь, который оформил подписку")
    subscribe = models.ForeignKey(Subscribe, on_delete=models.CASCADE, verbose_name="Подписка", help_text="Подписка, которую оформил пользователь")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return datetime.strftime(self.created_at, '%d.%m.%y')
    
    class Meta:
        verbose_name = 'Подписка пользователя'
        verbose_name_plural = 'Подписки пользователей'