from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.app_worker.auth.mixin import NotNannySubscribeRequiredMixin
from apps.app_worker.models import Nanny


class NannyCreateView(
        LoginRequiredMixin,
        NotNannySubscribeRequiredMixin,
        CreateView
    ):
    template_name = 'nanny_create.html'
    model = Nanny
    fields = ['phone_number', 'cost_per_hour', 'city', 'photo', 'first_name', 'last_name', 'work_days', 'age', 'experience', 'describe']
    success_url = reverse_lazy('nanny_update')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = None
        if form.is_valid():
            form.instance.user = request.user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def get_form(self, form_class = None):
        form =  super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
        form.fields['first_name'].widget.attrs['placeholder'] = "Татьяна"
        form.fields['last_name'].widget.attrs['placeholder'] = "Попова"
        form.fields['phone_number'].widget.attrs['placeholder'] = "+7 999 999 99 99"
        form.fields['age'].widget.attrs['placeholder'] = "65 лет"
        form.fields['cost_per_hour'].widget.attrs['placeholder'] = "от 450₽"
        form.fields['experience'].widget.attrs['placeholder'] = "10 лет"
        form.fields['describe'].widget.attrs['placeholder'] = "Работаю с детьми от 3-х лет..."
        return form
    
