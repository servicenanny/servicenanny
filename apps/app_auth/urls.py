from django.urls import path, include
from . import views


urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="account_signup"),
    path("login/", views.LoginView.as_view(), name="account_login"),
    path("", include("account.urls")),
]