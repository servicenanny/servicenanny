from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

from apps.app_infrastructure.models import City


class BaseWorker(models.Model):
    """
    Base Worker implementing base advanced of worker
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Аккаунт работника", help_text="Выберите аккаунт работника")
    phone_number = PhoneNumberField(verbose_name="Номер телефона", help_text="Введите номер телефона работника")
    city = models.ForeignKey(
        City,
        on_delete=models.DO_NOTHING,
        verbose_name="Города", 
        help_text="Города, в которых работает работник"
    )
    
    def __str__(self) -> str:
        return str(self.user)
    
    class Meta:
        abstract = True