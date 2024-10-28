from django.forms import BooleanField, CheckboxInput

import account.forms


class SignupForm(account.forms.SignupForm):

    is_worker = BooleanField(
        required = False, 
        initial = True,
        label = "Я — няня"
    )
    is_accept = BooleanField(
        widget = CheckboxInput()
    )

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]
