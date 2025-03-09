from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.app_worker.auth.mixin import ParentSubscribeRequiredMixin
from apps.app_worker.models import Nanny
from apps.app_worker.repository import NannyRepository
from apps.app_subscribe.repository import UserSubscribeRepository
from apps.app_user.forms import UpdateUserCityForm


class NannyListView(LoginRequiredMixin, ParentSubscribeRequiredMixin, ListView):
    model = Nanny
    template_name = 'nanny_list.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nanny_repository = NannyRepository()
        self.user_subscribe_repository = UserSubscribeRepository()

    def get_queryset(self):
        return self.nanny_repository.get_fresh_subscriber_nanny_pagination(
                user_subscribe_repository = self.user_subscribe_repository, 
                count = 10
            )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['change_city_form'] = UpdateUserCityForm()
        context['cities'] = context['change_city_form'].fields['city'].queryset
        return context