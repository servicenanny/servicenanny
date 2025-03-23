from django.urls import path, re_path

from .views import *


urlpatterns = [
     path('', NannyListView.as_view(), name='nannies'),
     path('create/', NannyCreateView.as_view(), name="nanny_create"),
     path('update/', NannyUpdateView.as_view(), name="nanny_update"),
     path('profile/', NannyProfileRedirectView.as_view(), name="nanny_profile"),
]
