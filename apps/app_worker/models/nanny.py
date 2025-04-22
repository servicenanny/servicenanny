from django.db import models
from multiselectfield import MultiSelectField
from django.utils.translation import gettext_lazy as _

from .base import BaseWorker
from apps.app_infrastructure.type import WEEKDAYS

AGE_GROUPS = [
    ('newborns', 'Няни для новорожденных'),
    ('under_3', 'Няни для детей до 3 лет'),
    ('ages_3_7', 'Няни для детей 3-7 лет'),
    ('schoolkids', 'Няни для школьников'),
]

WORK_TYPES = [
    ('full_day', 'Няни на полный день'),
    ('part_day', 'Няни на неполный день'),
    ('weekends', 'Няни на выходные'),
    ('hourly', 'Няни по часам'),
    ('temporary', 'Няни для временной работы'),
]

QUALIFICATION_LEVELS = [
    ('experienced', 'Опытные няни (с опытом работы)'),
    ('medical', 'Няни с медицинским образованием'),
    ('pedagogical', 'Няни с педагогическим образованием'),
    ('beginner', 'Няни без опыта (студенты, начинающие)'),
]

ADDITIONAL_SERVICES = [
    ('cleaning', 'Няни с обязанностями по уборке'),
    ('cooking', 'Няни с обязанностями по приготовлению пищи'),
    ('tutoring', 'Няни с образовательной функцией (репетиторы)'),
    ('special_needs', 'Няни с навыками ухода за детьми с особыми потребностями'),
]

LIVING_ARRANGEMENTS = [
    ('live_in', 'Няни, проживающие с семьей'),
    ('live_out', 'Няни, приходящие на работу'),
]

FOREIGN_LANGUAGES = [
    ('english', 'Английский'),
    ('french', 'Французский'),
    # Add more languages as needed
]

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
    age_groups = MultiSelectField(
        choices=AGE_GROUPS,
        max_choices=4,
        max_length=50,
        default="---",
        verbose_name="Возрастные группы детей",
        help_text="Выберите возрастные группы детей"
    )
    work_types = MultiSelectField(
        choices=WORK_TYPES,
        max_choices=5,
        max_length=50,
        default="---",
        verbose_name="Тип работы",
        help_text="Выберите тип работы"
    )
    qualification_levels = MultiSelectField(
        choices=QUALIFICATION_LEVELS,
        max_choices=4,
        max_length=50,
        default="---",
        verbose_name="Уровень квалификации",
        help_text="Выберите уровень квалификации"
    )
    additional_services = MultiSelectField(
        choices=ADDITIONAL_SERVICES,
        max_choices=4,
        max_length=50,
        default="---",
        verbose_name="Дополнительные услуги",
        help_text="Выберите дополнительные услуги"
    )
    living_arrangements = MultiSelectField(
        choices=LIVING_ARRANGEMENTS,
        max_choices=2,
        max_length=30,
        default="---",
        verbose_name="Проживание",
        help_text="Выберите тип проживания"
    )
    foreign_languages = MultiSelectField(
        choices=FOREIGN_LANGUAGES,
        max_choices=10,
        max_length=100,
        default="---",
        verbose_name="Иностранные няни",
        help_text="Выберите иностранные языки"
    )

    class Meta:
        verbose_name = 'Няня'
        verbose_name_plural = 'Няни'