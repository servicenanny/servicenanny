# Generated by Django 5.1.2 on 2024-11-01 23:18

import django.core.validators
import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_worker', '0006_alter_nanny_age_alter_nanny_describe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nanny',
            name='cost_per_hour',
            field=models.PositiveIntegerField(help_text='Введите стоимость в час', null=True, validators=[django.core.validators.MinValueValidator(450)], verbose_name='Стоимость в час'),
        ),
        migrations.AlterField(
            model_name='nanny',
            name='work_days',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(0, 'Пн'), (1, 'Вт'), (2, 'Ср'), (3, 'Чт'), (4, 'Пт'), (5, 'Сб'), (6, 'Вс')], default=0, help_text='Выберите рабочие дни недели', max_length=13, verbose_name='Рабочие дни недели'),
        ),
    ]
