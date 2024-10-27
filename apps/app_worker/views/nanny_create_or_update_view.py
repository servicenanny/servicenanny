from dataclasses import dataclass
from typing import Any
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.app_worker.auth.mixin import NannySubscribeRequiredMixin
from apps.app_worker.forms import NannyForm, UserForm


@dataclass
class MultipleNannyTypeForm:
    nanny_type: type[NannyForm]
    user_type: type[UserForm]


@dataclass
class MultipleNannyForm:
    nanny_form: NannyForm
    user_form: UserForm


class NannyCreateOrUpdateView(LoginRequiredMixin, NannySubscribeRequiredMixin, CreateView):
    template_name = 'nanny_register.html'
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.user = None

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)
    
    def get_form_class(self):
        return MultipleNannyTypeForm(NannyForm, UserForm)
    
    def get_form(self, form_class: MultipleNannyTypeForm = None) -> BaseModelForm:
        """Return an instance of the form to be used in this view."""
        if form_class is None:
            form_class = self.get_form_class()
        return MultipleNannyForm(
            nanny_form = form_class.nanny_type(**self.get_form_kwargs()),
            user_form = form_class.user_type(**self.get_form_kwargs())
        )