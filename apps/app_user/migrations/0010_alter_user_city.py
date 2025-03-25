# Generated by Django 5.1.2 on 2025-03-23 08:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_infrastructure', '0001_initial'),
        ('app_user', '0009_alter_user_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app_infrastructure.city', verbose_name='Город пользователя'),
        ),
    ]
