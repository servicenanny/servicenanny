from django.urls import path

from .views import *


urlpatterns = [
     path('', NannyListView.as_view(), name='nannies'),
     path('register', NannyCreateOrUpdateView.as_view())
]
