from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from domain.entity.type import CLIENT_TYPE



class UserSubscribe(models.Model):
    user = models.ForeignKey(get_user_model(), db_index=True, on_delete=models.CASCADE, verbose_name="Пользователь", help_text="Пользователь, который оформил подписку")
    # Можно было бы хранить только пользователя и получать тип подписки от него, но предполагалась, что таким образом будут храниться подписки с разной продолжительностью
    subscribe_type = models.CharField(
        choices=CLIENT_TYPE.get_choices(),
        max_length=1,
        default=CLIENT_TYPE.PARENT.value[0],
        verbose_name="Тип подписки",
        help_text="Подписка, которую оформил пользователь"
        )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата оформления")

    def __str__(self) -> str:
        return datetime.strftime(self.created_at, '%d.%m.%y')
    
    class Meta:
        verbose_name = 'Подписка пользователя'
        verbose_name_plural = 'Подписки пользователей'