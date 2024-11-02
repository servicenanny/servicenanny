from django.forms import ModelForm

from apps.app_worker.models import Nanny


class NannyForm(ModelForm):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['placeholder'] = "+7 999 999 99 99"
        self.fields['cost_per_hour'].widget.attrs['placeholder'] = "от 450₽"
        self.fields['experience'].widget.attrs['placeholder'] = "10 лет"
        self.fields['describe'].widget.attrs['placeholder'] = "Работаю с детьми от 3-х лет..."

    class Meta:
        model = Nanny
        fields = [
            'phone_number',
            'cost_per_hour',
            'city',
            'photo',
            'work_days',
            'age',
            'experience',
            'describe',
        ]