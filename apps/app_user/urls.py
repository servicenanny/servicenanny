from django.urls import path, include
from . import views


urlpatterns = [
    path("change_city/<int:pk>/", views.UpdateUserCityView.as_view(), name="change_city"),
]