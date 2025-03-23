# Generated by Django 5.1.2 on 2024-10-30 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSubscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribe_type', models.CharField(choices=[('N', 'Няни'), ('P', 'Родители')], default='P', help_text='Подписка, которую оформил пользователь', max_length=1, verbose_name='Тип подписки')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата оформления')),
            ],
            options={
                'verbose_name': 'Подписка пользователя',
                'verbose_name_plural': 'Подписки пользователей',
            },
        ),
    ]
