from django.db import models

from .base import BaseWorker
from apps.app_contrib.fields import WeekdayField


class Nanny(BaseWorker):
    """
    Nanny model based by BaseWorker
    """
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания", help_text="Дата создания няни")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата обновления", help_text="Дата обновления данных няни")
    work_days = WeekdayField(verbose_name="Рабочие дни недели", help_text="Выберите рабочие дни недели")
    describe = models.TextField(verbose_name="Описание", help_text="Введите описание")
    skills = models.TextField(verbose_name="Навыки", help_text="Что вы умеете?")

    class Meta:
        verbose_name = 'Няня'
        verbose_name_plural = 'Няни'