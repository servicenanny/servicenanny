from django.db import models
from multiselectfield import MultiSelectField

from .base import BaseWorker
from apps.app_infrastructure.type import WEEKDAYS


class Nanny(BaseWorker):
    """
    Nanny model based by BaseWorker
    """
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания", help_text="Дата создания няни")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата обновления", help_text="Дата обновления данных няни")
    work_days = MultiSelectField(
        choices=WEEKDAYS,
        max_choices=7,
        max_length=7,
        default=WEEKDAYS[0][0],
        verbose_name="Рабочие дни недели",
        help_text="Выберите рабочие дни недели"
    )
    age = models.PositiveSmallIntegerField(verbose_name="Возраст", help_text="Введите возраст", default=0)
    experience = models.PositiveSmallIntegerField(verbose_name="Опыт", help_text="Введите кол-во лет", default=0)
    describe = models.TextField(verbose_name="Описание", help_text="Введите описание")
    skills = models.TextField(verbose_name="Навыки", help_text="Что вы умеете?")

    class Meta:
        verbose_name = 'Няня'
        verbose_name_plural = 'Няни'