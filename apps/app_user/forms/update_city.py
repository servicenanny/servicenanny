from django import forms
from django.utils.translation import gettext_lazy as _

from apps.app_user.models import User
from apps.app_infrastructure.models import City


class UpdateUserCityForm(forms.ModelForm):
    city = forms.ModelChoiceField(
        queryset = City.objects,
        required = True,
        label = _("Города"),
        help_text = _("Выберите город"), 
        widget=forms.HiddenInput()
    )
    
    class Meta:
        model = User
        fields = ['city']
