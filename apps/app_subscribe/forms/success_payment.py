from datetime import datetime

from django import forms


class SuccessPaymentForm(forms.Form):
    date = forms.DateTimeField(required=False)
    order_id = forms.CharField(max_length=6, required=False)
    order_num = forms.CharField(max_length=255, required=False)
    domain = forms.CharField(max_length=255, required=False)
    sum = forms.CharField(max_length=255, required=False)
    customer_phone = forms.CharField(max_length=12, required=False)
    customer_email = forms.CharField(max_length=255, required=True)
    customer_extra = forms.CharField(max_length=255, required=False)
    payment_type = forms.CharField(max_length=255, required=False)
    commission = forms.CharField(max_length=32, required=False)
    commission_sum = forms.CharField(max_length=255, required=False)
    attempt = forms.IntegerField(required=False)
    sys = forms.CharField(max_length=255, required=False)
    vk_user_id = forms.CharField(max_length=255, required=False)
    payment_status = forms.CharField(max_length=32, required=False)
    payment_status_description = forms.CharField(max_length=255, required=False)