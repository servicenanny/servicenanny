from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model

from apps.app_worker.models import Nanny
from apps.app_worker.forms import NannyForm, UserForm


class NannyCreateOrUpdateView(TemplateView):
    template_name = 'nanny_register.html'
    model_user = get_user_model()
    model_nanny = Nanny

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ...
        return context


def nanny_resigter(request):
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
    return render(request, 'nanny_register.html', context)