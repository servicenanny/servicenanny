from django.db import models
from multiselectfield import MultiSelectField
from django.utils.translation import gettext_lazy as _

from .base import BaseWorker
from apps.app_infrastructure.type import WEEKDAYS


class Nanny(BaseWorker):
    """
    Nanny model based by BaseWorker
    """
    first_name = models.CharField(
        _('first name'),
        max_length=30
    )
    last_name = models.CharField(
        _('last name'),
        max_length=150
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания", help_text="Дата создания няни")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата обновления", help_text="Дата обновления данных няни")
    work_days = MultiSelectField(
        choices=WEEKDAYS,
        max_choices=7,
        max_length=13,
        default=WEEKDAYS[0][0],
        verbose_name="Рабочие дни недели",
        help_text="Выберите рабочие дни недели"
    )
    age = models.PositiveSmallIntegerField(verbose_name="Возраст", help_text="Введите возраст")
    experience = models.PositiveSmallIntegerField(verbose_name="Опыт", help_text="Введите кол-во лет")
    describe = models.TextField(verbose_name="Описание", help_text="Введите описание")

    class Meta:
        verbose_name = 'Няня'
        verbose_name_plural = 'Няни'