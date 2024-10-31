import account.forms
import account.views
from django.contrib.auth import get_user_model

from .forms import SignupForm
from apps.app_worker.repository import NannyRepository
from domain.repository.nanny_repository import AddNannyDTO


class LoginView(account.views.LoginView):

    form_class = account.forms.LoginEmailForm


class SignupView(account.views.SignupView):

    form_class =  SignupForm
    identifier_field = 'email'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nanny_repository = NannyRepository()

    def create_user(self, form, commit=True, model=None, **kwargs):
        User = model
        if User is None:
            User = get_user_model()
        user = User(**kwargs)
        user.email = form.cleaned_data["email"].strip()
        password = form.cleaned_data.get("password")
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.client_type = form.cleaned_data.get('client_type')
        if commit:
            user.save()
        return user