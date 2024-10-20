from django.db import models
from apps.app_contrib.models import SoftDeleteModel


# Create your models here.
class City(SoftDeleteModel):
    name = models.CharField(max_length=63, verbose_name="Имя города", help_text="Ввведите имя города")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'