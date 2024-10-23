from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model

from apps.app_worker.models import Nanny
from apps.app_worker.forms import NannyForm, UserForm


class NannyCreateOrUpdateView(CreateView):
    template_name = 'nanny_register.html'
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.user = None
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.method == 'POST':
            user_form = UserForm(request.POST)
            nanny_form = NannyForm(request.POST)
            if user_form.is_valid() and nanny_form.is_valid():
                user_form.save()
                nanny_form.save()
                return HttpResponseRedirect('/home')        
            else:
                context = {
                    'user_form': user_form,
                    'nanny_form': nanny_form,
                }
        else:
            context = {
                'user_form': UserForm(),
                'nanny_form': NannyForm(),
            }
        return render(request, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ...
        return context