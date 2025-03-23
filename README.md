
## Creation Site

```
python manage.py shell

from django.contrib.sites.models import Site

site = Site.objects.create(name='My Site', domain='localhost:8000')
```