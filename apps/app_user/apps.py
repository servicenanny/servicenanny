from django.apps import AppConfig


class AppUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.app_user'
    verbose_name = 'Пользователи'
    label = 'app_user'