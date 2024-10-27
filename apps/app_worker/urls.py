from django.urls import path

from .views import *


urlpatterns = [
     path('', NannyListView.as_view(), name='nannies'),
     path('profile', NannyProfileUpdateView.as_view(), name="nanny_profile")
]
