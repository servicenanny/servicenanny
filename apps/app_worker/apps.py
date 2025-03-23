from django.apps import AppConfig


class AppWorkerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.app_worker'
    verbose_name = 'Работники'
