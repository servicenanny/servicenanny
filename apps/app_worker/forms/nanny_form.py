from django.forms import ModelForm, Textarea

from apps.app_worker.models import Nanny


class NannyForm(ModelForm):   
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Nanny
        fields = ['phone_number', 'age', 'experience', 'cost_per_hour', 'describe', 'skills', 'work_days']