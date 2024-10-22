import account.forms
import account.views

from .forms import SignupForm


class LoginView(account.views.LoginView):

    form_class = account.forms.LoginEmailForm


class SignupView(account.views.SignupView):

    form_class =  SignupForm
    identifier_field = 'email'

    def generate_username(self, form):
        username = form.cleaned_data["email"]
        return username

    def after_signup(self, form):
        super(SignupView, self).after_signup(form)