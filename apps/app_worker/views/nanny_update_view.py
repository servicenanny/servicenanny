from typing import Any

from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from domain.repository import NannyRepository as INannyRepository
from apps.app_worker.repository import NannyRepository
from apps.app_worker.auth.mixin import NannySubscribeRequiredMixin
from apps.app_worker.models import Nanny


class NannyUpdateView(
        LoginRequiredMixin,
        NannySubscribeRequiredMixin,
        UpdateView
    ):
    template_name = 'nanny_update.html'
    model = Nanny
    fields = ['phone_number', 'cost_per_hour', 'city', 'photo', 'first_name', 'last_name', 'work_days', 'age', 'experience', 'describe']
    success_url = reverse_lazy('nanny_update')
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.nanny_repository: INannyRepository = NannyRepository()
        self.user = None

    def get(self, request, *args, **kwargs):
        self.user = request.user
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.user = request.user
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class = None):
        form =  super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
        if 'object' in self.__dict__:
            form.fields['first_name'].initial = self.object.first_name
            form.fields['last_name'].initial = self.object.last_name
            form.fields['phone_number'].initial = self.object.phone_number
            form.fields['age'].initial = self.object.age
            form.fields['cost_per_hour'].initial = self.object.cost_per_hour
            form.fields['experience'].initial = self.object.experience
            form.fields['describe'].initial = self.object.describe
            form.fields['work_days'].initial = self.object.work_days
        return form
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if 'object' in self.__dict__:
            context["checked_providers"] = list(map(int, self.object.work_days))
        return context
    
    
    def get_object(self, queryset = None):
        if queryset is None:
            queryset = self.get_queryset()
        return self.nanny_repository.get_by_user_id(self.user.id)
