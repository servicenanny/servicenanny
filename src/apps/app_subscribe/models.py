from django.db import models
from django.contrib.auth import get_user_model
    

class SubscribeMove(models.Model):
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата обновления")
    user = models.ForeignKey(get_user_model(), db_index=True, on_delete=models.CASCADE, verbose_name="Пользователь", help_text="Пользователь, который оформил подписку")

    def __str__(self) -> str:
        return self.end_date
