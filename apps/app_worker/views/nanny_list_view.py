from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.app_worker.auth.mixin import NannySubscribeRequiredMixin
from apps.app_worker.models import Nanny
from apps.app_worker.db.subscribe_nanny import get_subscriber_nanny

# Create your views here.

class NannyListView(LoginRequiredMixin, NannySubscribeRequiredMixin, ListView):
    model = Nanny
    template_name = 'nanny_list.html'

    def get_queryset(self):
        return get_subscriber_nanny(Nanny.objects)[:10]
    
    def get_template_names(self):
        return super().get_template_names()