from django.urls import path

from .api import SuccessPaymentView
from .views import LogonSubscribeRedirectView, SuccessPaymentPageView


urlpatterns = [
     path('success/', SuccessPaymentView.as_view(), name='success_payment'),
     path('success_redirect/', SuccessPaymentPageView.as_view(), name="success_redirect"),
     path('', LogonSubscribeRedirectView.as_view(), name='logon_redirect')
]
