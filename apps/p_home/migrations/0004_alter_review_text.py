# Generated by Django 5.1.2 on 2025-01-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_home', '0003_alter_review_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(help_text='Основной текст блока. Максимум 2047 символов', max_length=2047, verbose_name='Отзыв'),
        ),
    ]
