from dataclasses import dataclass
from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.app_worker.auth.mixin import NannySubscribeRequiredMixin
from apps.app_worker.forms import NannyForm, UserForm
from apps.app_worker.services import NannyProfileHandler, UpdateProfileDTO


@dataclass
class MultipleNannyTypeForm:
    nanny_type: type[NannyForm]
    user_type: type[UserForm]


@dataclass
class MultipleNannyForm:
    nanny_form: NannyForm
    user_form: UserForm


class NannyProfileUpdateView(LoginRequiredMixin, NannySubscribeRequiredMixin, CreateView):
    template_name = 'nanny_register.html'
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.user = None
        self.handler = NannyProfileHandler()

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        forms = self.get_form()
        if forms.user_form.is_valid() and forms.nanny_form.is_valid():
            self.handler.update_user_info(UpdateProfileDTO(
                    user_id = request.user.id,
                    first_name = forms.nanny_form.cleaned_data['first_name'],
                    last_name = forms.nanny_form.cleaned_data['last_name'],
                    phone_number = forms.nanny_form.cleaned_data['phone_number'],
                    cost_per_hour = forms.nanny_form.cleaned_data['cost_per_hour'],
                    photo = forms.nanny_form.cleaned_data['photo'],
                    city = forms.nanny_form.cleaned_data['city'],
                    work_days = forms.nanny_form.cleaned_data['work_days'],
                    age = forms.nanny_form.cleaned_data['age'],
                    experience = forms.nanny_form.cleaned_data['experience'],
                    describe = forms.nanny_form.cleaned_data['describe']
                )
            )
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=forms))
    
    def get_form_class(self):
        return MultipleNannyTypeForm(NannyForm, UserForm)
    
    def get_form(self, form_class: MultipleNannyTypeForm = None) -> MultipleNannyForm:
        """Return an instance of the form to be used in this view."""
        if form_class is None:
            form_class = self.get_form_class()
        return MultipleNannyForm(
            nanny_form = form_class.nanny_type(**self.get_form_kwargs()),
            user_form = form_class.user_type(**self.get_form_kwargs())
        )