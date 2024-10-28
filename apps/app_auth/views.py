import account.forms
import account.views

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

    def generate_username(self, form):
        username = form.cleaned_data["email"]
        return username

    def after_signup(self, form):
        self.create_profile(form)
        super(SignupView, self).after_signup(form)

    def create_profile(self, form):
        if form.cleaned_data['is_worker'] == True:
            self.nanny_repository.add(AddNannyDTO(
                user_id = self.created_user.id
            ))