from django.http import Http404
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.app_worker.auth.mixin import ParentSubscribeRequiredMixin
from apps.app_worker.models import Nanny
from apps.app_worker.repository import NannyRepository
from apps.app_subscribe.repository import UserSubscribeRepository
from apps.app_user.forms import UpdateUserCityForm
from apps.app_user.models import User


class NannyListView(LoginRequiredMixin, ParentSubscribeRequiredMixin, ListView):
    model = Nanny
    template_name = 'nanny_list.html'
    paginate_by = 10

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nanny_repository = NannyRepository()
        self.user_subscribe_repository = UserSubscribeRepository()
        self.user: User | None = None

    def get(self, request, *args, **kwargs):
        self.user = request.user
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(
                self.object_list, "exists"
            ):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(
                    _("Empty list and “%(class_name)s.allow_empty” is False.")
                    % {
                        "class_name": self.__class__.__name__,
                    }
                )
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_queryset(self):
        queryset = self.nanny_repository.get_fresh_subscriber_nannies_by_city(
            user_subscribe_repository=self.user_subscribe_repository,
            city_id=self.user.city.id
        )
        filters = {
            'age_groups__contains': self.request.GET.get('age_groups'),
            'work_types__contains': self.request.GET.get('work_types'),
            'qualification_levels__contains': self.request.GET.get('qualification_levels'),
            'additional_services__contains': self.request.GET.get('additional_services'),
            'living_arrangements__contains': self.request.GET.get('living_arrangements'),
            'foreign_languages__contains': self.request.GET.get('foreign_languages'),
        }
        filters = {k: v for k, v in filters.items() if v}
        return queryset.filter(**filters)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['change_city_form'] = UpdateUserCityForm()
        context['cities'] = context['change_city_form'].fields['city'].queryset
        context['filters'] = {
            'age_groups': self.request.GET.get('age_groups', ''),
            'work_types': self.request.GET.get('work_types', ''),
            'qualification_levels': self.request.GET.get('qualification_levels', ''),
            'additional_services': self.request.GET.get('additional_services', ''),
            'living_arrangements': self.request.GET.get('living_arrangements', ''),
            'foreign_languages': self.request.GET.get('foreign_languages', ''),
        }
        return context