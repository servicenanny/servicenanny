from django.forms import ModelForm

from apps.app_worker.models import Nanny


class NannyForm(ModelForm):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

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