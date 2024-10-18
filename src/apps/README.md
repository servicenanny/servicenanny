# Naming rules

1. All pages are marked with the prefix 'p'
2. All apps that are not page marked with the prefix 'app'

# Creation app rules

1. When creating a new django application, you need to select the apps folder to create
2. In the created django application in the file apps.py if the class of the application config. Add the name of the apps directory to the name field. An example of correct naming:

```
class AppAboutUsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.p_about_us'

```