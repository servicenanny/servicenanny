from django.urls import path

from .api import SuccessPaymentView
from .views import LogonSubscribeRedirectView


urlpatterns = [
     path('success/', SuccessPaymentView.as_view(), name='success_payment'),
     path('', LogonSubscribeRedirectView.as_view(), name='logon_redirect')
]
