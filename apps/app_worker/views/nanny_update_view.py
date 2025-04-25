from typing import Any

from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from apps.app_worker.models import Nanny

class NannyUpdateView(UpdateView):
    model = Nanny
    template_name = 'nanny_update.html'
    fields = ['first_name', 'last_name', 'phone_number', 'age', 'experience', 'cost_per_hour', 'city', 'photo', 'describe', 'work_days']

    def form_valid(self, form):
        response = super().form_valid(form)
        return render(self.request, self.template_name, {'form': form, 'success': True})
