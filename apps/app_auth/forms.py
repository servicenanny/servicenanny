from django.forms import BooleanField, CheckboxInput, CharField
import account.forms

from domain.entity.type import CLIENT_TYPE


class SignupForm(account.forms.SignupForm):
    client_type = CharField(
        max_length = 1,
        required = False, 
        initial = CLIENT_TYPE.NANNY.value[0],
        label = "Я — няня"
    )
    is_accept = BooleanField(
        widget = CheckboxInput()
    )

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]