from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator 

from apps.app_infrastructure.type import CLIENT_TYPE
from apps.app_contrib.models import SoftDeleteModel


class Subscribe(SoftDeleteModel):
    name = models.CharField(max_length=255, verbose_name="Название подписки", help_text="Введите название подписки")
    short_description = models.CharField(max_length=255, verbose_name="Описание подписки", help_text="Введите описание подписки (максимальное количество символов 255)")
    client_type = models.CharField(max_length=1, choices=CLIENT_TYPE.get_choices(), verbose_name="Тип клиента", help_text="Выберите тип клиент, для которого работает эта подписка")
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Стоимость подписки", help_text="Введите стоимость подписки")
    day_range = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(20000)],
        default=0,
        verbose_name="Дни",
        help_text="Продолжительность работы подписки в днях"
    )

    created_by = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, verbose_name="Создатель")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания", help_text="Дата создания подписки")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата обновления", help_text="Дата обновления данных о подписке")

    def __str__(self) -> str:
        return str(self.name)
    
    def delete(self, *args, **kwargs):
        raise Exception(kwargs)
        return super().delete(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'