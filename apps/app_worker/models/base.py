from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator 

from apps.app_infrastructure.models import City


class BaseWorker(models.Model):
    """
    Base Worker implementing base advanced of worker
    """
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, verbose_name="Аккаунт работника", help_text="Выберите аккаунт работника")
    phone_number = PhoneNumberField(verbose_name="Номер телефона", help_text="Введите номер телефона работника", null=True)
    cost_per_hour = models.PositiveIntegerField(verbose_name="Стоимость в час", help_text="Введите стоимость в час", validators=[MinValueValidator(450)], null=True)
    city = models.ForeignKey(
        City,
        on_delete=models.DO_NOTHING,
        verbose_name="Города", 
        help_text="Города, в которых работает работник",
        null=True
    )
    photo = models.ImageField(verbose_name="Фото работника", help_text="Загрузите фото", null=True)
    
    def __str__(self) -> str:
        return str(self.user)
    
    class Meta:
        abstract = True