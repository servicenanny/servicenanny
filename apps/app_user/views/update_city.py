from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from apps.app_user.models import User
from apps.app_user.forms import UpdateUserCityForm
from apps.app_user.auth.mixin import UserOwnRequiredMixin


class UpdateUserCityView(LoginRequiredMixin, UserOwnRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('home')
    form_class = UpdateUserCityForm
    
    http_method_names = [
        "post"
    ]

    def dispatch(self, request, *args, **kwargs):
        kwargs['user_id'] = kwargs['pk']
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        if 'success_url' in kwargs:
            self.success_url = kwargs.get('success_url')
        form = self.get_form()
        result = super().post(request, *args, **kwargs)
        return result
    
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.success_url)
    
    def form_invalid(self, form):
        raise Exception(form)
        return super().form_invalid(form)
    
