from django.urls import path

from .api import SuccessPaymentView


urlpatterns = [
     path('success/', SuccessPaymentView.as_view(), name='success_payment'),
]
